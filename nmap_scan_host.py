#!/usr/bin/env python3

from chibi.command.nmap import nmap
from chibi.command.network import ip_addr
from argparse import ArgumentParser
from chibi.atlas import Chibi_atlas


parser = ArgumentParser()
parser.add_argument(
    "-i", "--interfacce", dest="interface", default='all',
    help="interface de red que va a usar para escanear default: (all)" )

parser.add_argument(
    "-s", dest="scan_mode", default='sn',
    help="modo de escaneo de nmap default ( sn )" )

args = parser.parse_args()


interfaces = ip_addr()
if args.interface == 'all':
    interfaces_to_use = list( interfaces.keys() )
else:
    if ',' in args.interface:
        interfaces_to_use = map(
            lambda x: x.strip(), args.interface.split( ',' ))
    else:
        interfaces_to_use = [ args.interface ]


for current_interface in interfaces_to_use:
    interface = interfaces[ current_interface ]
    if current_interface == 'lo' or not interface.ip_v4:
        continue
    nmap_result = nmap( "-{}".format( args.scan_mode ), interface.ip_v4 )
    print( "interface: {}\tcommand: {}".format(
        current_interface, nmap_result.nmaprun.args ) )
    for result in nmap_result.nmaprun.host:
        result = Chibi_atlas( result )
        if 'address' not in result:
            import pdb
            pdb.set_trace()
        o = '\tip: {}'.format( result.address.addr )
        if result.hostnames:
            o += "\thostname: {} ( {} )".format(
                result.hostnames.hostname.name,
                result.hostnames.hostname.type )
        print( o )
