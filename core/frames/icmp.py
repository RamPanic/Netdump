

# Constants

ICMP_HEADER_FORMAT = "!2B3H"
ICMP_MAX_HEADER_LENGTH = 8

TYPES = { 

    0:  [ "Echo Reply" ],
    3:  [ "Destination Network Unreachable", 
          "Destination Host Unreachable",
          "Destination Protocol Unreachable",
          "Destination Port Unreachable",
          "",
          "",
          "Destination Network Unknown",
          "Destination Host Unknown" ],
    4:  [ "Source Quench (Congestion Control)" ],
    8:  [ "Echo Request" ],
    9:  [ "Router Advertisement" ],
    10: [ "Router Discovery" ],
    11: [ "TTL Expired" ],
    12: [ "IP Header Bad" ]

}

# Classes

class ICMP:

    def __init__(self):

        self.__type = None
        self.__code = None
        self.__checksum = None
        self.__identifier = None
        self.__sequence = None
        self.__data = None


    def __str__(self):

        output = f"ICMP(\
        type={self.__type},\
        code={self.__code},\
        checksum={self.__checksum},\
        identifier={self.__identifier},\
        sequence={self.__sequence}\
        )"

        return output.replace(" ", "")


    @property
    def type(self):

        return self.__type


    @type.setter
    def type(self, type_):

        self.__type = type_


    @property
    def code(self):

        return self.__code


    @code.setter
    def code(self, code):

        self.__code = code


    @property
    def checksum(self):

        return self.__checksum


    @checksum.setter
    def checksum(self, checksum):

        self.__checksum = checksum


    @property
    def identifier(self):

        return self.__identifier


    @identifier.setter
    def identifier(self, identifier):

        self.__identifier = identifier


    @property
    def sequence(self):

        return self.__sequence
        

    @sequence.setter
    def sequence(self, sequence):

        self.__sequence = sequence


    @property
    def data(self):

        return self.__data


    @data.setter
    def data(self, data):

        self.__data = data


    @property
    def type_description(self):

        return TYPES.get(self.__type)[self.__code]
