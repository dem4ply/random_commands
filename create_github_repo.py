#!/usr/bin/env python
import os

from argparse import ArgumentParser
from chibi.config import basic_config
from chibi_github import Github_api

basic_config()
parser = ArgumentParser()
parser.add_argument(
    "repo_name",
    help="nombre del repositorio que se creara" )

parser.add_argument(
    "description",
    help="nombre del repositorio que se creara" )


if __name__ == '__main__':
    args = parser.parse_args()
    api = Github_api()
    api.login()
    response = api.me.repos.create(
        name=args.repo_name,
        description=args.description,
        private=False,
    )
    if not response.ok:
        import pdb
        pdb.set_trace()
        raise NotImplementedError(
            "no esta implementado el manejo de error de github" )
    ssh_url = response.native.ssh_url
    print( f"url: {response.native.html_url}" )
    print( f"ssh_url: {ssh_url}" )
