#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright &copy; 2014-2016 NetApp, Inc. All Rights Reserved.
#
# DO NOT EDIT THIS CODE BY HAND! It has been generated with jsvcgen.
#

import click

from element.cli import utils as cli_utils
from element.cli.cli import pass_context
from element.solidfire_element_api import SolidFireRequestException
from element import utils

@click.group()
@pass_context
def cli(ctx):
    """Account methods."""
    ctx.sfapi = ctx.client

@cli.command('get', short_help="GetVolumeEfficiency")
@click.argument('volume_id', type=int, required=True)
@pass_context
def get(ctx, volume_id):
    """GetVolumeEfficiency is used to retrieve information about a volume."""
    """Only the volume given as a parameter in this API method is used to compute the capacity."""
    GetVolumeEfficiencyResult = ctx.element.get_volume_efficiency(volume_id=volume_id)
    print(GetVolumeEfficiencyResult)

