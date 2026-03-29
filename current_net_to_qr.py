#!/usr/bin/env python3

from chibi.command.nmap import nmap
from chibi.command.network import ip_addr
from argparse import ArgumentParser
from chibi.atlas import Chibi_atlas
#from chibi.command.qr import wifi
from chibi.command.nmcli import connection
from chibi_command.qr import QR_encode
from chibi_command.network.nmcli import NMcli


parser = ArgumentParser()
parser.add_argument(
    "--ssid", dest="ssid", default='current',
    help="nombre de la red para convertir en QR" )

parser.add_argument(
    "-s", "--size", dest="size", default=8,
    help="tamanno de los pixeles del QR" )

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
    nmcli connection show --show-secrets 723ea6a6-dbc3-46ee-a869-79c46d80cb2f
    ssid = list( ssid.keys() )[0]
    image = QR_encode.wifi( ssid, s=args.size )
    print( image.path )
    image.show()
