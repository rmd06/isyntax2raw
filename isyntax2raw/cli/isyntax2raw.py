# encoding: utf-8
#
# Copyright (c) 2019 Glencoe Software, Inc. All rights reserved.
#
# This software is distributed under the terms described by the LICENCE file
# you can find at the root of the distribution bundle.
# If the file is missing please request a copy by contacting
# support@glencoesoftware.com.

import click
import psutil

from .. import WriteTiles


@click.group()
def cli():
    pass


@click.command()
@click.option(
    "--tile_width", default=512, type=int, show_default=True,
    help="tile width in pixels"
)
@click.option(
    "--tile_height", default=512, type=int, show_default=True,
    help="tile height in pixels"
)
@click.option(
    "--no_pyramid", default=False, is_flag=True,
    help="disable subresolution writing"
)
@click.option(
    "--file_type", default="tiff", show_default=True,
    help="tile file extension (jpg, png, tiff)"
)
@click.option(
    "--max_workers", default=psutil.cpu_count(logical=False), type=int,
    show_default=True,
    help="maximum number of tile workers that will run at one time",
)
@click.argument("input_path")
@click.argument("output_path")
def write_tiles(
    tile_width, tile_height, no_pyramid, file_type, max_workers, input_path,
    output_path
):
    with WriteTiles(
        tile_width, tile_height, no_pyramid, file_type, max_workers,
        input_path, output_path
    ) as wt:
        wt.write_metadata()
        wt.write_label_image()
        wt.write_macro_image()
        wt.write_pyramid()


cli.add_command(write_tiles, name='write_tiles')


def main():
    cli()
