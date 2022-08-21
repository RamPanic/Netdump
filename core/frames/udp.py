 

UDP_HEADER_FORMAT = "!4H"
UDP_MAX_HEADER_LENGTH = 8


class UDP:

    def __init__(self):
        
        self.__src_port = None
        self.__dst_port = None
        self.__length = None
        self.__checksum = None
        self.__data = None


    def __str__(self):

        output = f"UDP(\
        source_port={self.__src_port},\
        destination_port={self.__dst_port},\
        length={self.__length},\
        checksum={self.__checksum}\
        )"

        return output.replace(" ", "")


    @property
    def src_port(self):

        return self.__src_port


    @src_port.setter
    def src_port(self, src_port):

        self.__src_port = src_port


    @property
    def dst_port(self):

        return self.__dst_port


    @dst_port.setter
    def dst_port(self, dst_port):

        self.__dst_port = dst_port


    @property
    def length(self):

        return self.__length


    @length.setter
    def length(self, length):

        self.__length = length


    @property
    def checksum(self):

        return self.__checksum


    @checksum.setter
    def checksum(self, checksum):

        self.__checksum = checksum


    @property
    def data(self):

        return self.__data


    @data.setter
    def data(self, data):

        self.__data = data
