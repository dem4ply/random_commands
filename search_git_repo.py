#!/usr/bin/env python3

from chibi.config import basic_config
from chibi_command.network.nmap import Nmap
from chibi_command.network.interfaces import Ip
from argparse import ArgumentParser
from chibi.atlas import Chibi_atlas
from chibi.file import Chibi_path
from chibi_git import Git
from chibi_git.exception import Git_not_initiate
from chibi.config import configuration
import logging


basic_config()
parser = ArgumentParser()
logger = logging.getLogger( 'bin.search_git_repo' )
configuration.loggers[ 'chibi.command' ].level = 'ERROR'

parser.add_argument(
    "path", nargs='+', metavar="path", type=Chibi_path,
    help="directorio donde se buscara si es un git repo" )

"""
parser.add_argument(
    "-i", "--interfacce", dest="interface", default='all',
    help="interface de red que va a usar para escanear default: (all)" )
"""


def check_if_has_git( path ):
    try:
        git = Git( path )
        if git.has_git:
            try:
                #git.fetch()
                pass
            except:
                logger.exception( "error con fetch" )
            try:
                sync = not git.is_head_synchronize_with_origin
            except:
                sync = False
            if git.is_dirty or sync:
                modified = len( git.status.modified )
                untrack = len( git.status.untrack )
                added = len( git.status.added )
                renamed = len( git.status.renamed )
                try:
                    if ( list( git.branches.remote.origin )
                            and git.is_head_synchronize_with_origin ):
                        syncronized = ""
                    else:
                        syncronized = "esta desincronizado"
                    print(
                        f"'{path}' tiene cambios sin commit"
                        f", commit final {git.head.commit} en la rama"
                        f" {git.head.branch.name}\n"
                        f"M: {modified} R: {renamed} A: {added} "
                        f"??: {untrack} {syncronized}"
                    )
                except:
                    logger.exception( f"'{path}' tiene una exception" )
    except Git_not_initiate as e:
        # logger.info( f"no tiene un repositorio git '{path}'" )
        pass



def main():
    args = parser.parse_args()
    for path in args.path:
        for p in path.find( files=False ):
            """
            if '.git' in p:
                continue
            """
            check_if_has_git( p )


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        import pdb
        #pdb.post_mortem( e.__traceback__ )
        logger.exception( "unhandled exception" )
        raise
