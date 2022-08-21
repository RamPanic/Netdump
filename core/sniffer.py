
import socket
from struct import unpack

import core.frames.datalink as datalinklib
import core.frames.ipv4 as ipv4lib
import core.frames.icmp as icmplib
import core.frames.udp as udplib
import core.frames.tcp as tcplib
import core.utils as utils
import core.exceptions as exceptions


class Netdump:

    def __init__(self, interface):
    
        #network_protocol = utils.get_network_protocol(network_protocol)

        #if not network_protocol:
        #    raise exceptions.NetdumpException("No network protocol with this name")

        #transport_protocol = utils.get_transport_protocol(transport_protocol)

        #if not transport_protocol:
        #    raise exceptions.NetdumpException("No transport protocol with this name")

        self.__tcp_packets = 0
        self.__udp_packets = 0
        self.__icmp_packets = 0


        self.__socket = socket.socket(

            socket.AF_PACKET,
            socket.SOCK_RAW,    
            socket.ntohs(3)
        
        )

        if not utils.interface_exists(interface):
            raise exceptions.NetdumpException("No interface with this name")

        self.__socket.bind((interface, 0))


    def run(self):

        try:

            self.__run()

        except KeyboardInterrupt:

            self.__socket.close()

        finally:

            print(f"\n\nTotal TCP Packets: {self.__tcp_packets}")
            print(f"Total UDP Packets: {self.__udp_packets}")
            print(f"Total ICMP Packets: {self.__icmp_packets}")
            print("\nNetdump Sniffer has been closed")


    def __run(self):

        packet_counter = 0

        while True:

            raw_data = self.__socket.recvfrom(65535)[0]

            output = self.__generate_output(packet_counter, raw_data)

            print(output)

            packet_counter += 1


    def __generate_output(self, packet_number, raw_data):

        network_protocol_outputs = {

            "IPv4": self.__generate_IPv4_output,

        }

        datalink = self.__get_datalink_packet(raw_data)

        output = f"\n============ Ethernet Frame {packet_number} ============\n\n"

        output += f"--> Datalink Header <--\n\n"
        output += f"Destination MAC: {datalink.dst_mac}; Source MAC: {datalink.src_mac}\n"
        output += f"Ether Type: {datalink.ether_type} ({datalink.ether_type_description})\n"

        network_protocol_output = network_protocol_outputs.get(datalink.ether_type_description)

        if network_protocol_output:

            output += network_protocol_output(datalink.data)

        return output


    def __get_datalink_packet(self, raw_data):

        data = unpack(
            datalinklib.DATALINK_HEADER_FORMAT, 
            raw_data[:datalinklib.DATALINK_MAX_HEADER_LENGTH]
        )

        datalink = datalinklib.Datalink()
        datalink.dst_mac = utils.convert_to_MAC_readable(data[0])
        datalink.src_mac = utils.convert_to_MAC_readable(data[1])
        datalink.ether_type = datalinklib.Datalink.convert_to_ether_type_readable(data[2])
        datalink.data = raw_data[datalinklib.DATALINK_MAX_HEADER_LENGTH:]

        return datalink


    def __generate_IPv4_output(self, raw_data):

        transport_protocol_outputs = {

            "ICMP": self.__generate_ICMP_output,
            "UDP": self.__generate_UDP_output,
            "TCP": self.__generate_TCP_output

        }

        ipv4 = self.__get_IPv4_packet(raw_data)

        output = "\n--> IP Header <--\n\n"

        output += f"Version: {ipv4.version}; "
        output += f"Length: {ipv4.length}; "
        output += f"Service Type: {ipv4.service_type}; "
        output += f"Total Length: {ipv4.total_length}\n"

        output += f"Identification: {ipv4.identification}; "
        output += f"Flags: {ipv4.flags}; "
        output += f"Fragmentation Offset: {ipv4.fragmentation_offset}\n"

        output += f"Time To Live: {ipv4.ttl}; "
        output += f"Protocol: {ipv4.protocol} ({ipv4.protocol_description});\n"

        output += f"Source IP Address: {ipv4.src_ip_address}\n"
        output += f"Destination IP Address: {ipv4.dst_ip_address}\n"

        transport_protocol_output = transport_protocol_outputs.get(ipv4.protocol_description)

        if transport_protocol_output:

            output += transport_protocol_output(ipv4.data)

        return output


    def __get_IPv4_packet(self, raw_data):

        data = unpack(
            ipv4lib.IPV4_HEADER_FORMAT, 
            raw_data[:ipv4lib.IPV4_MAX_HEADER_LENGTH]
        )

        ipv4 = ipv4lib.IPv4()
        ipv4.version = data[0] >> 4
        ipv4.length = data[0] & 0xf
        ipv4.service_type = data[1]
        ipv4.total_length = data[2]
        ipv4.identification = data[3]
        ipv4.flags = ipv4lib.IPv4.convert_to_flags_readable(data[4])
        ipv4.fragmentation_offset = data[4] & 0xf
        ipv4.ttl = data[5]
        ipv4.protocol = data[6]
        ipv4.src_ip_address = utils.convert_to_IPv4_readable(data[8])
        ipv4.dst_ip_address = utils.convert_to_IPv4_readable(data[9])
        ipv4.data = raw_data[ipv4lib.IPV4_MAX_HEADER_LENGTH:]

        return ipv4


    def __generate_ICMP_output(self, raw_data):

        self.__icmp_packets += 1

        icmp = self.__get_ICMP_packet(raw_data)

        output = "\n--> ICMP Header <--\n\n"

        output += f"Type: {icmp.type} ({icmp.type_description}); "
        output += f"Code: {icmp.code}; "
        output += f"Checksum: {icmp.checksum}\n"

        output += f"Identifier: {icmp.identifier} {hex(icmp.identifier)}; "
        output += f"Sequence: {icmp.sequence} ({hex(icmp.sequence)})\n"

        output += f"Data: {icmp.data} {len(icmp.data)}\n"

        return output


    def __get_ICMP_packet(self, raw_data):

        data = unpack(
            icmplib.ICMP_HEADER_FORMAT, 
            raw_data[:icmplib.ICMP_MAX_HEADER_LENGTH]
        )

        icmp = icmplib.ICMP()
        icmp.type = data[0]
        icmp.code = data[1]
        icmp.checksum = data[2] 
        icmp.identifier = data[3]
        icmp.sequence = data[4]
        icmp.data = raw_data[icmplib.ICMP_MAX_HEADER_LENGTH:]

        return icmp


    def __generate_UDP_output(self, raw_data):

        self.__udp_packets += 1

        udp = self.__get_UDP_packet(raw_data)

        output = "\n--> UDP Header <--\n\n"

        output += f"Source Port: {udp.src_port}; "
        output += f"Destination Port: {udp.dst_port};\n"

        output += f"Length: {udp.length}; "
        output += f"Checksum: {udp.checksum}\n"

        output += f"Data: {udp.data} {len(udp.data)}\n"

        return output


    def __get_UDP_packet(self, raw_data):

        data = unpack(
            udplib.UDP_HEADER_FORMAT, 
            raw_data[:udplib.UDP_MAX_HEADER_LENGTH]
        )

        udp = udplib.UDP()
        udp.src_port = data[0]
        udp.dst_port = data[1]
        udp.length = data[2]
        udp.checksum = data[3] 
        udp.data = raw_data[icmplib.ICMP_MAX_HEADER_LENGTH:]

        return udp


    def __generate_TCP_output(self, raw_data):

        self.__tcp_packets += 1

        tcp = self.__get_TCP_packet(raw_data)

        output = "\n--> TCP Header <--\n\n"

        output += f"Source Port: {tcp.src_port}; "
        output += f"Destination Port: {tcp.dst_port}\n"
        
        output += f"Sequence Number (raw): {tcp.sequence_number}\n"
        
        output += f"Acknowledgement Number: (raw): {tcp.ack_number}\n"        
        
        output += f"Length: {tcp.length}; "
        output += f"Reserved: {tcp.reserved}; "
        output += f"Flags: {tcp.flags}; "
        output += f"Window: {tcp.window}\n"

        output += f"Checksum: {tcp.checksum}; "
        output += f"Urgent: {tcp.urgent}\n"

        output += f"Data: {tcp.data} ({len(tcp.data)})"

        return output


    def __get_TCP_packet(self, raw_data):

        data = unpack(
            tcplib.TCP_HEADER_FORMAT, 
            raw_data[:tcplib.TCP_MAX_HEADER_LENGTH]
        )

        tcp = tcplib.TCP()
        tcp.src_port = data[0]
        tcp.dst_port = data[1]
        tcp.sequence_number = data[2]
        tcp.ack_number = data[3]
        tcp.length = data[4] >> 12
        tcp.reserved = ( data[4] >> 6 ) & 0x3f
        tcp.flags = tcplib.TCP.convert_to_flags_readable(data[4])
        tcp.window = data[5]
        tcp.checksum = data[6]
        tcp.urgent = data[7]        
        tcp.data = raw_data[tcplib.TCP_MAX_HEADER_LENGTH:]

        return tcp
