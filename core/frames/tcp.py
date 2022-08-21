

TCP_HEADER_FORMAT = "!2H2L4H"
TCP_MAX_HEADER_LENGTH = 20


class TCP:

    def __init__(self):

        self.__src_port = None
        self.__dst_port = None
        self.__sequence_number = None
        self.__ack_number = None
        self.__length = None
        self.__reserved = None
        self.__flags = None
        self.__window = None
        self.__checksum = None
        self.__urgent = None


    def __str__(self):

        output = f"TCP(\
        source_port={self.__src_port},\
        destination_port={self.__dst_port},\
        sequence_number={self.__sequence_number},\
        ack_number={self.__ack_number},\
        length={self.__length},\
        reserved={self.__reserved}\
        flags={self.__flags},\
        window={self.__window},\
        checksum={self.__checksum},\
        urgent={self.__urgent}\
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
    def sequence_number(self):

        return self.__sequence_number


    @sequence_number.setter
    def sequence_number(self, sequence):

        self.__sequence_number = sequence


    @property
    def ack_number(self):

        return self.__ack_number


    @ack_number.setter
    def ack_number(self, ack_num):

        self.__ack_number = ack_num


    @property
    def length(self):

        return self.__length


    @length.setter
    def length(self, length):

        self.__length = length


    @property
    def reserved(self):

        return self.__reserved


    @reserved.setter
    def reserved(self, reserved):

        self.__reserved = reserved


    @property
    def flags(self):

        return self.__flags


    @flags.setter
    def flags(self, flags):

        self.__flags = flags


    @property
    def window(self):

        return self.__window


    @window.setter
    def window(self, window):

        self.__window = window


    @property
    def checksum(self):

        return self.__checksum


    @checksum.setter
    def checksum(self, checksum):

        self.__checksum = checksum    


    @property
    def urgent(self):

        return self.__urgent


    @urgent.setter
    def urgent(self, urgent):

        self.__urgent = urgent


    @property
    def data(self):

        return self.__data


    @data.setter
    def data(self, data):

        self.__data = data


    @staticmethod
    def convert_to_flags_readable(raw_flags):

        bits_string = format(raw_flags & 0x003f, "06b")

        bits = [ int(bit) for bit in bits_string ]

        return {

            "URG": bits[0],
            "ACK": bits[1],
            "PSH": bits[2],
            "RST": bits[3],
            "SYN": bits[4],
            "FIN": bits[5]

        }