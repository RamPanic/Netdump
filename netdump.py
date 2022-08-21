
import argparse
from sys import exit

import core.exceptions as exceptions
from core.sniffer import Netdump
from core.utils import banner, is_root, arguments_exists



EXIT_SUCCESS = 0
EXIT_FAILED = 1


def main():

    banner()

    parser = argparse.ArgumentParser()
    parser.description = "Small basic sniffer to capture ICMP, TCP and UDP packets"
    parser.usage = "netdump.py [OPTIONS]"
    parser.epilog = ""

    # Groups

    main_group = parser.add_argument_group('main arguments')
    main_group.add_argument('-i', '--interface', type=str, help='Interface')

    #optional_group = parser.add_argument_group("Optional arguments")
    #optional_group.add_argument('-np', '--network-protocol', type=str, default="ethernet", help='')
    #optional_group.add_argument('-tp', '--transport-protocol', type=str, default="all", help='')

    # Start

    args = parser.parse_args()

    if not is_root():
        print("You need to be root to run Netdump")
        exit(EXIT_FAILED)

    if not arguments_exists():
        parser.print_help()
        exit(EXIT_FAILED)


    try:

        netdump = Netdump(
            args.interface, 
            #args.network_protocol,
            #args.transport_protocol
        )

        netdump.run()

    except exceptions.NetdumpException as error:

        print(error)

        exit(EXIT_FAILED)

    else:

        exit(EXIT_SUCCESS)


if __name__ == '__main__':

    main()