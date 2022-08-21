
import socket

from os import getuid
from sys import argv


def banner():

    output = "\n\n                      ____                      \n"
    output += "                    /      \\                      \n"
    output += "                 /  (O)  (O)  \\                   \n"
    output += "                |              |                   \n"
    output += "               |    \\      /    |                 \n"
    output += "                \\    |\\__/|    /                 \n"
    output += "                 \\ \\  \\__/  / /                 \n"
    output += "    __0_0_0_______/ \\ ____ / \\_______0_0_0_____  \n\n"
    output += "      _  _ ___ _____ ___  _   _ __  __ ___         \n"  
    output += "     | \\| | __|_   _|   \\| | | |  \\/  | _ \\    \n"
    output += "     | .` | _|  | | | |) | |_| | |\\/| |  _/       \n"
    output += "     |_|\\_|___| |_| |___/ \\___/|_|  |_|_|        \n\n"
    output += "               Created By RamPanic                  \n"

    print(output)


def is_root():

    return getuid() == 0


def arguments_exists():

    return len(argv) > 1


# def get_network_protocol(network_protocol):

#     network_protocols = { "ethernet": socket.AF_PACKET, "ipv4": socket.AF_INET }

#     return network_protocols.get(network_protocol)


# def get_transport_protocol(transport_protocol):

#     transport_protocols = { 

#         "icmp": socket.IPPROTO_ICMP, 
#         "tcp": socket.IPPROTO_TCP,
#         "udp": socket.IPPROTO_UDP,
#         "all": socket.ntohs(3)
    
#     }

#     return transport_protocols.get(transport_protocol)


def interface_exists(interface):

    try:
        socket.if_nametoindex(interface)
    except OSError:
        return False
    else:
        return True


def convert_to_IPv4_readable(raw_ip):

    return ".".join(map(str, raw_ip))


def convert_to_MAC_readable(raw_mac):

    return ":".join(map("{:02x}".format, raw_mac))
