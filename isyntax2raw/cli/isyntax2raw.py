# encoding: utf-8
#
# Copyright (c) 2019 Glencoe Software, Inc. All rights reserved.
#
# This software is distributed under the terms described by the LICENCE file
# you can find at the root of the distribution bundle.
# If the file is missing please request a copy by contacting
# support@glencoesoftware.com.

import click

from .. import WriteTiles


@click.group()
def cli():
    pass


@click.command()
@click.option("input_path", help="path to isyntax file")
@click.option(
    "--tile_width", default=512, type=int, help="tile width in pixels"
)
@click.optiont(
    "--tile_height", default=512, type=int, help="tile height in pixels"
)
@click.option(
    "--no_pyramid", default=False, is_flag=True,
    help="toggle subresolution writing",
)
def write_tiles(tile_width, tile_height, no_pyramid, input_path):
    with WriteTiles(tile_width, tile_height, no_pyramid, input_path) as wt:
        wt.write_metadata()
        wt.write_macro_image()
        wt.write_pyramid()


cli.add_command(write_tiles, name='write_tiles')


def main():
    cli()
