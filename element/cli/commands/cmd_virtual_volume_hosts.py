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

@cli.command('list', short_help="ListVirtualVolumeHosts")
@click.argument('virtual_volume_host_ids', type=UUID, required=False)
@pass_context
def list(ctx, virtual_volume_host_ids = None):
    """ListVirtualVolumeHosts returns a list of known ESX hosts."""
    ListVirtualVolumeHostsResult = ctx.element.list_virtual_volume_hosts(virtual_volume_host_ids=virtual_volume_host_ids)
    print(ListVirtualVolumeHostsResult)

