#!/usr/bin/env python3

from chibi.command.nmap import nmap
from chibi.command.network import ip_addr
from argparse import ArgumentParser
from chibi.atlas import Chibi_atlas
from chibi.command.qr import wifi
from chibi.command.nmcli import connection


parser = ArgumentParser()
parser.add_argument(
    "--ssid", dest="ssid", default='current',
    help="nombre de la red para convertir en qr" )

parser.add_argument(
    "-s", "--size", dest="size", default=8,
    help="nombre de la red para convertir en qr" )

args = parser.parse_args()


if args.ssid == 'current':
    ssid = connection.show.current
else:
    ssid = connection.show( args.ssid )

if len( ssid.keys() ) > 1:
    print( "selecione una sola red" )
    for s in ssid:
        print( s )
else:
    ssid = list( ssid.keys() )[0]
    image = wifi( ssid, s=args.size )
    print( image.path )
    image.show()
