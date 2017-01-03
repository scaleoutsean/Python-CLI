#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright &copy; 2014-2016 NetApp, Inc. All Rights Reserved.
#
# DO NOT EDIT THIS CODE BY HAND! It has been generated with jsvcgen.
#

import click

from element.cli import utils as cli_utils
from element.cli import parser
from element.cli.cli import pass_context
from element.solidfire_element_api import SolidFireRequestException
from element import utils
import jsonpickle
import simplejson
from uuid import UUID


@click.group()
@pass_context
def cli(ctx):
    """GetIpmiConfig GetIpmiInfo """
    ctx.sfapi = ctx.client

@cli.command('GetIpmiConfig', short_help="GetIpmiConfig")
@click.option('--chassis_type',
              type=str,
              required=False,
              help="""Used to display information for each node chassis type. Valid values:all - returns sensor information for each chassis type. {chassis type} - returns sensor information for a specified chassis type. """)
@click.option('--force',
              type=bool,
              required=True,
              help="""""")
@pass_context
def GetIpmiConfig(ctx,
           force,
           chassis_type = None):
    """GetIpmiConfig enables you to retrieve hardware sensor information from sensors that are in your node."""



    GetIpmiConfigResult = ctx.element.get_ipmi_config(force=force, chassis_type=chassis_type)
    cli_utils.print_result(GetIpmiConfigResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetIpmiInfo', short_help="GetIpmiInfo")
@click.option('--force',
              type=bool,
              required=True,
              help="""""")
@pass_context
def GetIpmiInfo(ctx,
           force):
    """GetIpmiInfo allows you to display a detailed reporting of sensors (objects) for node fans, intake and exhaust temperatures, and power supplies  that are monitored by . """



    GetIpmiInfoResult = ctx.element.get_ipmi_info(force=force)
    cli_utils.print_result(GetIpmiInfoResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)
