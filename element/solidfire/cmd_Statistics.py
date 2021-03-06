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
from element import utils
import jsonpickle
import simplejson
from solidfire.models import *
from uuid import UUID
from element import exceptions
from solidfire import common


@click.group()
@pass_context
def cli(ctx):
    """GetCompleteStats GetHardwareInfo GetRawStats ListVolumeStatsByVirtualVolume ListVolumeStats ListDriveStats """

@cli.command('GetCompleteStats', short_help="""The GetCompleteStats API method is used by SolidFire engineering to troubleshoot new features. The data returned from GetCompleteStats is not documented, changes frequently, and is not guaranteed to be accurate. It is not recommended to ever use GetCompleteStats for collecting performance data or any other management integration with a SolidFire cluster. The data returned from GetCompleteStats changes frequently, and is not guaranteed to accurately show performance from the system. It is not recommended to ever use GetCompleteStats for collecting performance data or any other management integration with a SolidFire cluster. """)
@pass_context
def GetCompleteStats(ctx):
    """The GetCompleteStats API method is used by SolidFire engineering to troubleshoot new features. The data returned from GetCompleteStats is not documented, changes frequently, and is not guaranteed to be accurate. It is not recommended to ever use GetCompleteStats for collecting performance data or any other management integration with a SolidFire cluster."""
    """The data returned from GetCompleteStats changes frequently, and is not guaranteed to accurately show performance from the system. It is not recommended to ever use GetCompleteStats for collecting performance data or any other management integration with a SolidFire cluster."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("")
    try:
        str = ctx.element.get_complete_stats()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(str, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetHardwareInfo', short_help="""GetHardwareInfo allows you to return hardware information and status for a single node. This generally includes manufacturers, vendors, versions, drives, and other associated hardware identification information. """)
@pass_context
def GetHardwareInfo(ctx):
    """GetHardwareInfo allows you to return hardware information and status for a single node. This generally includes manufacturers, vendors, versions, drives, and other associated hardware identification information."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("")
    try:
        GetHardwareInfoResult = ctx.element.get_hardware_info()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(GetHardwareInfoResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetRawStats', short_help="""The GetRawStats call is used by SolidFire engineering to troubleshoot new features. The data returned from GetRawStats is not documented, it changes frequently, and is not guaranteed to be accurate. It is not recommended to ever use GetRawStats for collecting performance data or any other management integration with a SolidFire cluster. The data returned from GetRawStats changes frequently, and is not guaranteed to accurately show performance from the system. It is not recommended to ever use GetRawStats for collecting performance data or any other management integration with a SolidFire cluster. """)
@pass_context
def GetRawStats(ctx):
    """The GetRawStats call is used by SolidFire engineering to troubleshoot new features. The data returned from GetRawStats is not documented, it changes frequently, and is not guaranteed to be accurate. It is not recommended to ever use GetRawStats for collecting performance data or any other management integration with a SolidFire cluster."""
    """The data returned from GetRawStats changes frequently, and is not guaranteed to accurately show performance from the system. It is not recommended to ever use GetRawStats for collecting performance data or any other management integration with a SolidFire cluster."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("")
    try:
        str = ctx.element.get_raw_stats()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(str, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListVolumeStatsByVirtualVolume', short_help="""ListVolumeStatsByVirtualVolume enables you to list statistics for volumes, sorted by virtual volumes. """)
@click.option('--virtual_volume_ids',
              type=str,
              required=False,
              help="""A list of virtual volume  IDs for which to retrieve information. If you specify this parameter, the method returns information about only these virtual volumes. """)
@pass_context
def ListVolumeStatsByVirtualVolume(ctx,
           virtual_volume_ids = None):
    """ListVolumeStatsByVirtualVolume enables you to list statistics for volumes, sorted by virtual volumes."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    virtual_volume_ids = parser.parse_array(virtual_volume_ids)

    ctx.logger.info("""virtual_volume_ids = """+str(virtual_volume_ids)+""";"""+"")
    try:
        ListVolumeStatsByVirtualVolumeResult = ctx.element.list_volume_stats_by_virtual_volume(virtual_volume_ids=virtual_volume_ids)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(ListVolumeStatsByVirtualVolumeResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListVolumeStats', short_help="""""")
@click.option('--volume_ids',
              type=str,
              required=False,
              help="""""")
@pass_context
def ListVolumeStats(ctx,
           volume_ids = None):
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    volume_ids = parser.parse_array(volume_ids)

    ctx.logger.info("""volume_ids = """+str(volume_ids)+""";"""+"")
    try:
        ListVolumeStatsResult = ctx.element.list_volume_stats(volume_ids=volume_ids)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(ListVolumeStatsResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListDriveStats', short_help="""ListDriveStats enables you to retrieve  high-level activity measurements for multiple drives in the cluster. By default, this method returns statistics for all drives in the cluster, and these measurements are cumulative from the addition of the drive to the cluster. Some values this method returns are specific to block drives, and some are specific to metadata drives. For more information on what data each drive type returns, see the response examples for the GetDriveStats method. """)
@click.option('--drives',
              type=str,
              required=False,
              help="""Optional list of DriveIDs for which to return drive statistics. If you omit this parameter, measurements for all drives are returned. """)
@pass_context
def ListDriveStats(ctx,
           drives = None):
    """ListDriveStats enables you to retrieve  high-level activity measurements for multiple drives in the cluster. By default, this method returns statistics for all drives in the cluster, and these measurements are cumulative from the addition of the drive to the cluster. Some values this method returns are specific to block drives, and some are specific to metadata drives. For more information on what data each drive type returns, see the response examples for the GetDriveStats method."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    drives = parser.parse_array(drives)

    ctx.logger.info("""drives = """+str(drives)+""";"""+"")
    try:
        ListDriveStatsResult = ctx.element.list_drive_stats(drives=drives)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(ListDriveStatsResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

