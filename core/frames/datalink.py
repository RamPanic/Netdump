
from socket import htons


# Constants

DATALINK_HEADER_FORMAT = "!6s6sH"
DATALINK_MAX_HEADER_LENGTH = 14

NETWORK_PROTOCOLS = { 8: "IPv4" }


# Classes

class Datalink:

    def __init__(self):

        self.__dst_mac = None
        self.__src_mac = None
        self.__ether_type = None
        self.__data = None


    @property
    def dst_mac(self):

        return self.__dst_mac


    @dst_mac.setter
    def dst_mac(self, dst_mac):

        self.__dst_mac = dst_mac


    @property
    def src_mac(self):

        return self.__src_mac


    @src_mac.setter
    def src_mac(self, src_mac):

        self.__src_mac = src_mac


    @property
    def ether_type(self):

        return self.__ether_type


    @ether_type.setter
    def ether_type(self, ether_type):

        self.__ether_type = ether_type


    @property
    def data(self):

        return self.__data


    @data.setter
    def data(self, data):

        self.__data = data


    @property
    def ether_type_description(self):

        return NETWORK_PROTOCOLS.get(self.__ether_type)


    @staticmethod
    def convert_to_ether_type_readable(raw_ether_type):

        return htons(raw_ether_type)