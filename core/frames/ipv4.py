
# Constants

IPV4_HEADER_FORMAT = "!2B3H2BH4s4s"
IPV4_MAX_HEADER_LENGTH = 20
PROTOCOLS = { 1: "ICMP", 6: "TCP", 17: "UDP" }

# Classes


class IPv4:

    def __init__(self):

        self.__version = None
        self.__length = None
        self.__service_type = None
        self.__total_length = None
        self.__identification = None
        self.__flags = None
        self.__fragmentation_offset = None
        self.__ttl = None
        self.__protocol = None
        self.__src_ip_address = None
        self.__dst_ip_address = None
        self.__data = None


    @property
    def version(self):

        return self.__version   


    @version.setter
    def version(self, version):

        self.__version = version


    @property
    def length(self):

        return self.__length    


    @length.setter
    def length(self, length):

        self.__length = length


    @property
    def service_type(self):

        return self.__service_type  


    @service_type.setter
    def service_type(self, service_type):

        self.__service_type = service_type


    @property
    def total_length(self):

        return self.__total_length    


    @total_length.setter
    def total_length(self, total_length):

        self.__total_length = total_length


    @property
    def identification(self):

        return self.__identification  


    @identification.setter
    def identification(self, identification):

        self.__total_length = identification


    @property
    def flags(self):

        return self.__flags    


    @flags.setter
    def flags(self, flags):

        self.__flags = flags


    @property
    def fragmentation_offset(self):

        return self.__fragmentation_offset  


    @fragmentation_offset.setter
    def fragmentation_offset(self, fragmentation_offset):

        self.__fragmentation_offset = fragmentation_offset


    @property
    def ttl(self):

        return self.__ttl  


    @ttl.setter
    def ttl(self, ttl):

        self.__ttl = ttl


    @property
    def protocol(self):

        return self.__protocol  


    @protocol.setter
    def protocol(self, protocol):

        self.__protocol = protocol


    @property
    def protocol_description(self):

        return PROTOCOLS.get(self.__protocol)


    @property
    def src_ip_address(self):

        return self.__src_ip_address


    @src_ip_address.setter
    def src_ip_address(self, src_ip_address):

        self.__src_ip_address = src_ip_address


    @property
    def dst_ip_address(self):

        return self.__dst_ip_address


    @dst_ip_address.setter
    def dst_ip_address(self, dst_ip_address):

        self.__dst_ip_address = dst_ip_address


    @property
    def data(self):

        return self.__data


    @data.setter
    def data(self, data):

        self.__data = data


    @staticmethod
    def convert_to_flags_readable(raw_flags):

        bits_string = format(raw_flags >> 13, "010b")[-3:]

        bits = [ int(bit) for bit in bits_string ]
        
        return { 
        
            "Reserved bit": bits[0], 
            "Don't fragment": bits[1], 
            "More fragments": bits[2] 
        
        }
