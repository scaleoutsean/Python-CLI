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
    """ListStatsBy GetEfficiency CloneMultiple ListForAccount ListActive CancelGroupClone PurgeDeleted ListBulkJobs Clone Modify CancelClone StartBulkWrite StartBulkRead Copy Create List UpdateBulkStatus ListStatsByAccount RestoreDeleted ListDeleted GetAsyncResult Delete ListAsyncResults ListStatsByAccessGroup SetDefaultQoS GetDefaultQoS GetStats GetCount """

@cli.command('ListStatsBy', short_help="""ListVolumeStatsByVolume returns high-level activity measurements for every volume, by volume. Values are cumulative from the creation of the volume. """)
@pass_context
def ListStatsBy(ctx):
    """ListVolumeStatsByVolume returns high-level activity measurements for every volume, by volume."""
    """Values are cumulative from the creation of the volume."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("")
    try:
        ListVolumeStatsByVolumeResult = ctx.element.list_volume_stats_by_volume()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(ListVolumeStatsByVolumeResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetEfficiency', short_help="""GetVolumeEfficiency is used to retrieve information about a volume. Only the volume given as a parameter in this API method is used to compute the capacity. """)
@click.option('--volume_id',
              type=int,
              required=True,
              help="""Specifies the volume for which capacity is computed. """)
@pass_context
def GetEfficiency(ctx,
           volume_id):
    """GetVolumeEfficiency is used to retrieve information about a volume."""
    """Only the volume given as a parameter in this API method is used to compute the capacity."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""volume_id = """+str(volume_id)+""";"""+"")
    try:
        GetVolumeEfficiencyResult = ctx.element.get_volume_efficiency(volume_id=volume_id)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(GetVolumeEfficiencyResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('CloneMultiple', short_help="""CloneMultipleVolumes is used to create a clone of a group of specified volumes. A consistent set of characteristics can be assigned to a group of multiple volume when they are cloned together. If groupSnapshotID is going to be used to clone the volumes in a group snapshot, the group snapshot must be created first using the CreateGroupSnapshot API method or the SolidFire Element WebUI. Using groupSnapshotID is optional when cloning multiple volumes.  Note: Cloning multiple volumes is allowed if cluster fullness is at stage 2 or 3. Clones are not created when cluster fullness is at stage 4 or 5. """)
@click.option('--clone_multiple_volume_params_volume_id',
              type=int,
              required=True,
              help="""Required parameter for "volumes" array: volumeID. """)
@click.option('--clone_multiple_volume_params_access',
              type=str,
              required=False,
              help="""Access settings for the new volume. readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.  If unspecified, the access settings of the clone will be the same as the source. """)
@click.option('--clone_multiple_volume_params_name',
              type=str,
              required=False,
              help="""New name for the clone. """)
@click.option('--clone_multiple_volume_params_new_account_id',
              type=int,
              required=False,
              help="""Account ID for the new volume. """)
@click.option('--clone_multiple_volume_params_new_size',
              type=int,
              required=False,
              help="""New size Total size of the volume, in bytes. Size is rounded up to the nearest 1MB size. """)
@click.option('--clone_multiple_volume_params_attributes',
              type=dict,
              required=False,
              help="""List of Name/Value pairs in JSON object format. """)
@click.option('--access',
              type=str,
              required=False,
              help="""New default access method for the new volumes if not overridden by information passed in the volumes array. readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.  If unspecified, the access settings of the clone will be the same as the source. """)
@click.option('--group_snapshot_id',
              type=int,
              required=False,
              help="""ID of the group snapshot to use as a basis for the clone. """)
@click.option('--new_account_id',
              type=int,
              required=False,
              help="""New account ID for the volumes if not overridden by information passed in the volumes array. """)
@pass_context
def CloneMultiple(ctx,
           clone_multiple_volume_params_volume_id,
           clone_multiple_volume_params_access = None,
           clone_multiple_volume_params_name = None,
           clone_multiple_volume_params_new_account_id = None,
           clone_multiple_volume_params_new_size = None,
           clone_multiple_volume_params_attributes = None,
           access = None,
           group_snapshot_id = None,
           new_account_id = None):
    """CloneMultipleVolumes is used to create a clone of a group of specified volumes. A consistent set of characteristics can be assigned to a group of multiple volume when they are cloned together."""
    """If groupSnapshotID is going to be used to clone the volumes in a group snapshot, the group snapshot must be created first using the CreateGroupSnapshot API method or the SolidFire Element WebUI. Using groupSnapshotID is optional when cloning multiple volumes."""
    """"""
    """Note: Cloning multiple volumes is allowed if cluster fullness is at stage 2 or 3. Clones are not created when cluster fullness is at stage 4 or 5."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    volumes = None
    if(volumes is not None or access is not None or group_snapshot_id is not None or new_account_id is not None or False):
        kwargsDict = dict()
        kwargsDict["volume_id"] = clone_multiple_volume_params_volume_id
        kwargsDict["access"] = clone_multiple_volume_params_access
        kwargsDict["name"] = clone_multiple_volume_params_name
        kwargsDict["new_account_id"] = clone_multiple_volume_params_new_account_id
        kwargsDict["new_size"] = clone_multiple_volume_params_new_size
        kwargsDict["attributes"] = clone_multiple_volume_params_attributes

        volumes = CloneMultipleVolumeParams(**kwargsDict)

    volumes = parser.parse_array(volumes)

    ctx.logger.info("""volumes = """+str(volumes)+""";"""+"""access = """+str(access)+""";"""+"""group_snapshot_id = """+str(group_snapshot_id)+""";"""+"""new_account_id = """+str(new_account_id)+""";"""+"")
    try:
        CloneMultipleVolumesResult = ctx.element.clone_multiple_volumes(volumes=volumes, access=access, group_snapshot_id=group_snapshot_id, new_account_id=new_account_id)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(CloneMultipleVolumesResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListForAccount', short_help="""ListVolumesForAccount returns the list of active AND (pending) deleted volumes for an account. """)
@click.option('--account_id',
              type=int,
              required=True,
              help="""The ID of the account to list the volumes for. """)
@click.option('--start_volume_id',
              type=int,
              required=False,
              help="""The ID of the first volume to list. This can be useful for paging results. By default, this starts at the lowest VolumeID. """)
@click.option('--limit',
              type=int,
              required=False,
              help="""The maximum number of volumes to return from the API. """)
@pass_context
def ListForAccount(ctx,
           account_id,
           start_volume_id = None,
           limit = None):
    """ListVolumesForAccount returns the list of active AND (pending) deleted volumes for an account."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""account_id = """+str(account_id)+""";"""+"""start_volume_id = """+str(start_volume_id)+""";"""+"""limit = """+str(limit)+""";"""+"")
    try:
        ListVolumesForAccountResult = ctx.element.list_volumes_for_account(account_id=account_id, start_volume_id=start_volume_id, limit=limit)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(ListVolumesForAccountResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListActive', short_help="""ListActiveVolumes is used to return the list of active volumes currently in the system. The list of volumes is returned sorted in VolumeID order and can be returned in multiple parts (pages). """)
@click.option('--start_volume_id',
              type=int,
              required=False,
              help="""The ID of the first volume to list. This can be useful for paging results. By default, this starts at the lowest VolumeID. """)
@click.option('--limit',
              type=int,
              required=False,
              help="""The maximum number of volumes to return from the API. """)
@pass_context
def ListActive(ctx,
           start_volume_id = None,
           limit = None):
    """ListActiveVolumes is used to return the list of active volumes currently in the system."""
    """The list of volumes is returned sorted in VolumeID order and can be returned in multiple parts (pages)."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""start_volume_id = """+str(start_volume_id)+""";"""+"""limit = """+str(limit)+""";"""+"")
    try:
        ListActiveVolumesResult = ctx.element.list_active_volumes(start_volume_id=start_volume_id, limit=limit)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(ListActiveVolumesResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('CancelGroupClone', short_help="""CancelGroupClone enables you to stop an ongoing CloneMultipleVolumes process for a group of clones. When you cancel a group clone operation, the system completes and removes the operation's associated asyncHandle. This method does not return anything. """)
@click.option('--group_clone_id',
              type=int,
              required=True,
              help="""cloneID for the ongoing clone process. """)
@pass_context
def CancelGroupClone(ctx,
           group_clone_id):
    """CancelGroupClone enables you to stop an ongoing CloneMultipleVolumes process for a group of clones. When you cancel a group clone operation, the system completes and removes the operation&#x27;s associated asyncHandle. This method does not return anything."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""group_clone_id = """+str(group_clone_id)+""";"""+"")
    try:
        CancelGroupCloneResult = ctx.element.cancel_group_clone(group_clone_id=group_clone_id)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(CancelGroupCloneResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('PurgeDeleted', short_help="""PurgeDeletedVolume immediately and permanently purges a volume which has been deleted. A volume must be deleted using DeleteVolume before it can be purged. Volumes are purged automatically after a period of time, so usage of this method is not typically required. """)
@click.option('--volume_id',
              type=int,
              required=True,
              help="""The ID of the volume to purge. """)
@pass_context
def PurgeDeleted(ctx,
           volume_id):
    """PurgeDeletedVolume immediately and permanently purges a volume which has been deleted."""
    """A volume must be deleted using DeleteVolume before it can be purged."""
    """Volumes are purged automatically after a period of time, so usage of this method is not typically required."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""volume_id = """+str(volume_id)+""";"""+"")
    try:
        PurgeDeletedVolumeResult = ctx.element.purge_deleted_volume(volume_id=volume_id)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(PurgeDeletedVolumeResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListBulkJobs', short_help="""ListBulkVolumeJobs is used to return information about each bulk volume read or write operation that is occurring in the system. """)
@pass_context
def ListBulkJobs(ctx):
    """ListBulkVolumeJobs is used to return information about each bulk volume read or write operation that is occurring in the system."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("")
    try:
        ListBulkVolumeJobsResult = ctx.element.list_bulk_volume_jobs()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(ListBulkVolumeJobsResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('Clone', short_help="""CloneVolume is used to create a copy of the volume. This method is asynchronous and may take a variable amount of time to complete. The cloning process begins immediately when the CloneVolume request is made and is representative of the state of the volume when the API method is issued. GetAsyncResults can be used to determine when the cloning process is complete and the new volume is available for connections. ListSyncJobs can be used to see the progress of creating the clone.  Note: The initial attributes and quality of service settings for the volume are inherited from the volume being cloned. If different settings are required, they can be changed via ModifyVolume.  Note: Cloned volumes do not inherit volume access group memberships from the source volume. """)
@click.option('--volume_id',
              type=int,
              required=True,
              help="""The ID of the volume to clone. """)
@click.option('--name',
              type=str,
              required=True,
              help="""The name for the newly-created volume. """)
@click.option('--new_account_id',
              type=int,
              required=False,
              help="""AccountID for the owner of the new volume. If unspecified, the AccountID of the owner of the volume being cloned is used. """)
@click.option('--new_size',
              type=int,
              required=False,
              help="""New size of the volume, in bytes. May be greater or less than the size of the volume being cloned. If unspecified, the clone's volume size will be the same as the source volume. Size is rounded up to the nearest 1 MiB. """)
@click.option('--access',
              type=str,
              required=False,
              help="""Access settings for the new volume. readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.  If unspecified, the access settings of the clone will be the same as the source. """)
@click.option('--snapshot_id',
              type=int,
              required=False,
              help="""ID of the snapshot to use as the source of the clone. If unspecified, the clone will be created with a snapshot of the active volume. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""Provide in json format: List of Name/Value pairs in JSON object format. """)
@pass_context
def Clone(ctx,
           volume_id,
           name,
           new_account_id = None,
           new_size = None,
           access = None,
           snapshot_id = None,
           attributes = None):
    """CloneVolume is used to create a copy of the volume."""
    """This method is asynchronous and may take a variable amount of time to complete."""
    """The cloning process begins immediately when the CloneVolume request is made and is representative of the state of the volume when the API method is issued."""
    """GetAsyncResults can be used to determine when the cloning process is complete and the new volume is available for connections."""
    """ListSyncJobs can be used to see the progress of creating the clone."""
    """"""
    """Note: The initial attributes and quality of service settings for the volume are inherited from the volume being cloned."""
    """If different settings are required, they can be changed via ModifyVolume."""
    """"""
    """Note: Cloned volumes do not inherit volume access group memberships from the source volume."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    if(attributes is not None):
        kwargsDict = simplejson.loads(attributes)
        attributes = dict(**kwargsDict)

    ctx.logger.info("""volume_id = """+str(volume_id)+""";"""+"""name = """+str(name)+""";"""+"""new_account_id = """+str(new_account_id)+""";"""+"""new_size = """+str(new_size)+""";"""+"""access = """+str(access)+""";"""+"""snapshot_id = """+str(snapshot_id)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        CloneVolumeResult = ctx.element.clone_volume(volume_id=volume_id, name=name, new_account_id=new_account_id, new_size=new_size, access=access, snapshot_id=snapshot_id, attributes=attributes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(CloneVolumeResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('Modify', short_help="""ModifyVolume is used to modify settings on an existing volume. Modifications can be made to one volume at a time and changes take place immediately. If an optional parameter is left unspecified, the value will not be changed.  Extending the size of a volume that is being replicated should be done in an order. The target (Replication Target) volume should first be increased in size, then the source (Read/Write) volume can be resized. It is recommended that both the target and the source volumes be the same size.  Note: If you change access status to locked or target all existing iSCSI connections are terminated. """)
@click.option('--volume_id',
              type=int,
              required=True,
              help="""VolumeID for the volume to be modified. """)
@click.option('--account_id',
              type=int,
              required=False,
              help="""AccountID to which the volume is reassigned. If none is specified, the previous account name is used. """)
@click.option('--access',
              type=str,
              required=False,
              help="""Access allowed for the volume. readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.  If unspecified, the access settings of the clone will be the same as the source. """)
@click.option('--qos_min_iops',
              type=int,
              required=False,
              help="""Desired minimum 4KB IOPS to guarantee. The allowed IOPS will only drop below this level if all volumes have been capped at their minimum IOPS value and there is still insufficient performance capacity. """)
@click.option('--qos_max_iops',
              type=int,
              required=False,
              help="""Desired maximum 4KB IOPS allowed over an extended period of time. """)
@click.option('--qos_burst_iops',
              type=int,
              required=False,
              help="""Maximum "peak" 4KB IOPS allowed for short periods of time. Allows for bursts of I/O activity over the normal max IOPS value. """)
@click.option('--qos_burst_time',
              type=int,
              required=False,
              help="""The length of time burst IOPS is allowed. The value returned is represented in time units of seconds. Note: this value is calculated by the system based on IOPS set for QoS. """)
@click.option('--total_size',
              type=int,
              required=False,
              help="""New size of the volume in bytes. Size is rounded up to the nearest 1MiB size. This parameter can only be used to *increase* the size of a volume. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""Provide in json format: List of Name/Value pairs in JSON object format. """)
@pass_context
def Modify(ctx,
           volume_id,
           account_id = None,
           access = None,
           qos_min_iops = None,
           qos_max_iops = None,
           qos_burst_iops = None,
           qos_burst_time = None,
           total_size = None,
           attributes = None):
    """ModifyVolume is used to modify settings on an existing volume."""
    """Modifications can be made to one volume at a time and changes take place immediately."""
    """If an optional parameter is left unspecified, the value will not be changed."""
    """"""
    """Extending the size of a volume that is being replicated should be done in an order."""
    """The target (Replication Target) volume should first be increased in size, then the source (Read/Write) volume can be resized."""
    """It is recommended that both the target and the source volumes be the same size."""
    """"""
    """Note: If you change access status to locked or target all existing iSCSI connections are terminated."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    qos = None
    if(volume_id is not None or account_id is not None or access is not None or qos is not None or total_size is not None or attributes is not None or False):
        kwargsDict = dict()
        kwargsDict["min_iops"] = qos_min_iops
        kwargsDict["max_iops"] = qos_max_iops
        kwargsDict["burst_iops"] = qos_burst_iops
        kwargsDict["burst_time"] = qos_burst_time

        qos = QoS(**kwargsDict)
    if(attributes is not None):
        kwargsDict = simplejson.loads(attributes)
        attributes = dict(**kwargsDict)

    ctx.logger.info("""volume_id = """+str(volume_id)+""";"""+"""account_id = """+str(account_id)+""";"""+"""access = """+str(access)+""";"""+"""qos = """+str(qos)+""";"""+"""total_size = """+str(total_size)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        ModifyVolumeResult = ctx.element.modify_volume(volume_id=volume_id, account_id=account_id, access=access, qos=qos, total_size=total_size, attributes=attributes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(ModifyVolumeResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('CancelClone', short_help="""Cancels a currently running clone operation. This method does not return anything. """)
@click.option('--clone_id',
              type=int,
              required=True,
              help="""""")
@pass_context
def CancelClone(ctx,
           clone_id):
    """Cancels a currently running clone operation. This method does not return anything."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""clone_id = """+str(clone_id)+""";"""+"")
    try:
        CancelCloneResult = ctx.element.cancel_clone(clone_id=clone_id)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(CancelCloneResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('StartBulkWrite', short_help="""StartBulkVolumeWrite allows you to initialize a bulk volume write session on a specified volume. Only two bulk volume processes can run simultaneously on a volume. When the session is initialized, data can be written to a SolidFire storage volume from an external backup source. The external data is accessed by a web server running on a SolidFire node. Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system. """)
@click.option('--volume_id',
              type=int,
              required=True,
              help="""ID of the volume to be written to. """)
@click.option('--format',
              type=str,
              required=True,
              help="""The format of the volume data. Can be either: uncompressed: every byte of the volume is returned without any compression. native: opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write """)
@click.option('--script',
              type=str,
              required=False,
              help="""Executable name of a script. If no script name is given then the key and URL are necessary to access SolidFire nodes. The script runs on the primary node and the key and URL is returned to the script so the local web server can be contacted. """)
@click.option('--script_parameters',
              type=str,
              required=False,
              help="""JSON parameters to pass to the script. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""Provide in json format: JSON attributes for the bulk volume job. """)
@pass_context
def StartBulkWrite(ctx,
           volume_id,
           format,
           script = None,
           script_parameters = None,
           attributes = None):
    """StartBulkVolumeWrite allows you to initialize a bulk volume write session on a specified volume."""
    """Only two bulk volume processes can run simultaneously on a volume."""
    """When the session is initialized, data can be written to a SolidFire storage volume from an external backup source."""
    """The external data is accessed by a web server running on a SolidFire node."""
    """Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    if(attributes is not None):
        kwargsDict = simplejson.loads(attributes)
        attributes = dict(**kwargsDict)

    ctx.logger.info("""volume_id = """+str(volume_id)+""";"""+"""format = """+str(format)+""";"""+"""script = """+str(script)+""";"""+"""script_parameters = """+str(script_parameters)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        StartBulkVolumeWriteResult = ctx.element.start_bulk_volume_write(volume_id=volume_id, format=format, script=script, script_parameters=script_parameters, attributes=attributes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(StartBulkVolumeWriteResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('StartBulkRead', short_help="""StartBulkVolumeRead allows you to initialize a bulk volume read session on a specified volume. Only two bulk volume processes can run simultaneously on a volume. When you initialize the session, data is read from a SolidFire storage volume for the purposes of storing the data on an external backup source. The external data is accessed by a web server running on a SolidFire node. Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system.  At the start of a bulk volume read operation, a snapshot of the volume is made and the snapshot is deleted when the read has completed. You can also read a snapshot of the volume by entering the ID of the snapshot as a parameter. Reading a previous snapshot does not create a new snapshot of the volume, nor does the previous snapshot be deleted when the read completes.  Note: This process creates a new snapshot if the ID of an existing snapshot is not provided. Snapshots can be created if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5. """)
@click.option('--volume_id',
              type=int,
              required=True,
              help="""ID of the volume to be read. """)
@click.option('--format',
              type=str,
              required=True,
              help="""The format of the volume data. Can be either: uncompressed: every byte of the volume is returned without any compression. native: opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write. """)
@click.option('--snapshot_id',
              type=int,
              required=False,
              help="""ID of a previously created snapshot used for bulk volume reads. If no ID is entered, a snapshot of the current active volume image is made. """)
@click.option('--script',
              type=str,
              required=False,
              help="""Executable name of a script. If no script name is given then the key and URL is necessary to access SolidFire nodes. The script is run on the primary node and the key and URL is returned to the script so the local web server can be contacted. """)
@click.option('--script_parameters',
              type=str,
              required=False,
              help="""JSON parameters to pass to the script. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""Provide in json format: JSON attributes for the bulk volume job. """)
@pass_context
def StartBulkRead(ctx,
           volume_id,
           format,
           snapshot_id = None,
           script = None,
           script_parameters = None,
           attributes = None):
    """StartBulkVolumeRead allows you to initialize a bulk volume read session on a specified volume."""
    """Only two bulk volume processes can run simultaneously on a volume."""
    """When you initialize the session, data is read from a SolidFire storage volume for the purposes of storing the data on an external backup source."""
    """The external data is accessed by a web server running on a SolidFire node."""
    """Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system."""
    """"""
    """At the start of a bulk volume read operation, a snapshot of the volume is made and the snapshot is deleted when the read has completed."""
    """You can also read a snapshot of the volume by entering the ID of the snapshot as a parameter."""
    """Reading a previous snapshot does not create a new snapshot of the volume, nor does the previous snapshot be deleted when the read completes."""
    """"""
    """Note: This process creates a new snapshot if the ID of an existing snapshot is not provided."""
    """Snapshots can be created if cluster fullness is at stage 2 or 3."""
    """Snapshots are not created when cluster fullness is at stage 4 or 5."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    if(attributes is not None):
        kwargsDict = simplejson.loads(attributes)
        attributes = dict(**kwargsDict)

    ctx.logger.info("""volume_id = """+str(volume_id)+""";"""+"""format = """+str(format)+""";"""+"""snapshot_id = """+str(snapshot_id)+""";"""+"""script = """+str(script)+""";"""+"""script_parameters = """+str(script_parameters)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        StartBulkVolumeReadResult = ctx.element.start_bulk_volume_read(volume_id=volume_id, format=format, snapshot_id=snapshot_id, script=script, script_parameters=script_parameters, attributes=attributes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(StartBulkVolumeReadResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('Copy', short_help="""Copies one volume to another. """)
@click.option('--volume_id',
              type=int,
              required=True,
              help="""Source volume to copy. """)
@click.option('--dst_volume_id',
              type=int,
              required=True,
              help="""Destination volume for the copy. """)
@click.option('--snapshot_id',
              type=int,
              required=False,
              help="""Snapshot ID of the source volume to create the copy from. """)
@pass_context
def Copy(ctx,
           volume_id,
           dst_volume_id,
           snapshot_id = None):
    """Copies one volume to another."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""volume_id = """+str(volume_id)+""";"""+"""dst_volume_id = """+str(dst_volume_id)+""";"""+"""snapshot_id = """+str(snapshot_id)+""";"""+"")
    try:
        CopyVolumeResult = ctx.element.copy_volume(volume_id=volume_id, dst_volume_id=dst_volume_id, snapshot_id=snapshot_id)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(CopyVolumeResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('Create', short_help="""CreateVolume is used to create a new (empty) volume on the cluster. When the volume is created successfully it is available for connection via iSCSI. """)
@click.option('--name',
              type=str,
              required=True,
              help="""Name of the volume. Not required to be unique, but it is recommended. May be 1 to 64 characters in length. """)
@click.option('--account_id',
              type=int,
              required=True,
              help="""AccountID for the owner of this volume. """)
@click.option('--total_size',
              type=int,
              required=True,
              help="""Total size of the volume, in bytes. Size is rounded up to the nearest 1MB size. """)
@click.option('--enable512e',
              type=bool,
              required=True,
              help="""Should the volume provides 512-byte sector emulation? """)
@click.option('--qos_min_iops',
              type=int,
              required=False,
              help="""Desired minimum 4KB IOPS to guarantee. The allowed IOPS will only drop below this level if all volumes have been capped at their minimum IOPS value and there is still insufficient performance capacity. """)
@click.option('--qos_max_iops',
              type=int,
              required=False,
              help="""Desired maximum 4KB IOPS allowed over an extended period of time. """)
@click.option('--qos_burst_iops',
              type=int,
              required=False,
              help="""Maximum "peak" 4KB IOPS allowed for short periods of time. Allows for bursts of I/O activity over the normal max IOPS value. """)
@click.option('--qos_burst_time',
              type=int,
              required=False,
              help="""The length of time burst IOPS is allowed. The value returned is represented in time units of seconds. Note: this value is calculated by the system based on IOPS set for QoS. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""Provide in json format: List of Name/Value pairs in JSON object format. """)
@pass_context
def Create(ctx,
           name,
           account_id,
           total_size,
           enable512e,
           qos_min_iops = None,
           qos_max_iops = None,
           qos_burst_iops = None,
           qos_burst_time = None,
           attributes = None):
    """CreateVolume is used to create a new (empty) volume on the cluster."""
    """When the volume is created successfully it is available for connection via iSCSI."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    qos = None
    if(name is not None or account_id is not None or total_size is not None or enable512e is not None or qos is not None or attributes is not None or False):
        kwargsDict = dict()
        kwargsDict["min_iops"] = qos_min_iops
        kwargsDict["max_iops"] = qos_max_iops
        kwargsDict["burst_iops"] = qos_burst_iops
        kwargsDict["burst_time"] = qos_burst_time

        qos = QoS(**kwargsDict)
    if(attributes is not None):
        kwargsDict = simplejson.loads(attributes)
        attributes = dict(**kwargsDict)

    ctx.logger.info("""name = """+str(name)+""";"""+"""account_id = """+str(account_id)+""";"""+"""total_size = """+str(total_size)+""";"""+"""enable512e = """+str(enable512e)+""";"""+"""qos = """+str(qos)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        CreateVolumeResult = ctx.element.create_volume(name=name, account_id=account_id, total_size=total_size, enable512e=enable512e, qos=qos, attributes=attributes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(CreateVolumeResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('List', short_help="""The ListVolumes method is used to return a list of volumes that are in a cluster. You can specify the volumes you want to return in the list by using the available parameters. """)
@click.option('--start_volume_id',
              type=int,
              required=False,
              help="""The ID of the first volume to list. This can be useful for paging results. By default, this starts at the lowest VolumeID. """)
@click.option('--limit',
              type=int,
              required=False,
              help="""The maximum number of volumes to return from the API. """)
@click.option('--volume_status',
              type=str,
              required=False,
              help="""If specified, filter to only volumes with the provided status. By default, list all volumes. """)
@click.option('--accounts',
              type=str,
              required=False,
              help="""If specified, only fetch volumes which belong to the provided accounts. By default, list volumes for all accounts. """)
@click.option('--is_paired',
              type=bool,
              required=False,
              help="""If specified, only fetch volumes which are paired (if true) or non-paired (if false). By default, list all volumes regardless of their pairing status. """)
@click.option('--volume_ids',
              type=str,
              required=False,
              help="""If specified, only fetch volumes specified in this list. This option cannot be specified if startVolumeID, limit, or accounts option is specified. """)
@pass_context
def List(ctx,
           start_volume_id = None,
           limit = None,
           volume_status = None,
           accounts = None,
           is_paired = None,
           volume_ids = None):
    """The ListVolumes method is used to return a list of volumes that are in a cluster."""
    """You can specify the volumes you want to return in the list by using the available parameters."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    accounts = parser.parse_array(accounts)

    volume_ids = parser.parse_array(volume_ids)

    ctx.logger.info("""start_volume_id = """+str(start_volume_id)+""";"""+"""limit = """+str(limit)+""";"""+"""volume_status = """+str(volume_status)+""";"""+"""accounts = """+str(accounts)+""";"""+"""is_paired = """+str(is_paired)+""";"""+"""volume_ids = """+str(volume_ids)+""";"""+"")
    try:
        ListVolumesResult = ctx.element.list_volumes(start_volume_id=start_volume_id, limit=limit, volume_status=volume_status, accounts=accounts, is_paired=is_paired, volume_ids=volume_ids)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(ListVolumesResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('UpdateBulkStatus', short_help="""You can use UpdateBulkVolumeStatus in a script to return to the SolidFire system the status of a bulk volume job that you have started with the "StartBulkVolumeRead" or "StartBulkVolumeWrite" methods. """)
@click.option('--key',
              type=str,
              required=True,
              help="""The key assigned during initialization of a "StartBulkVolumeRead" or "StartBulkVolumeWrite" session. """)
@click.option('--status',
              type=str,
              required=True,
              help="""The SolidFire system sets the status of the given bulk volume job. Possible values: running: jobs that are still active. complete: jobs that are done. failed - jobs that have failed. failed: jobs that have failed. """)
@click.option('--percent_complete',
              type=str,
              required=False,
              help="""The completed progress of the bulk volume job as a percentage. """)
@click.option('--message',
              type=str,
              required=False,
              help="""Returns the status of the bulk volume job when the job has completed. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""Provide in json format: JSON attributes  updates what is on the bulk volume job. """)
@pass_context
def UpdateBulkStatus(ctx,
           key,
           status,
           percent_complete = None,
           message = None,
           attributes = None):
    """You can use UpdateBulkVolumeStatus in a script to return to the SolidFire system the status of a bulk volume job that you have started with the &quot;StartBulkVolumeRead&quot; or &quot;StartBulkVolumeWrite&quot; methods."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    if(attributes is not None):
        kwargsDict = simplejson.loads(attributes)
        attributes = dict(**kwargsDict)

    ctx.logger.info("""key = """+str(key)+""";"""+"""status = """+str(status)+""";"""+"""percent_complete = """+str(percent_complete)+""";"""+"""message = """+str(message)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        UpdateBulkVolumeStatusResult = ctx.element.update_bulk_volume_status(key=key, status=status, percent_complete=percent_complete, message=message, attributes=attributes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(UpdateBulkVolumeStatusResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListStatsByAccount', short_help="""ListVolumeStatsByAccount returns high-level activity measurements for every account. Values are summed from all the volumes owned by the account. """)
@pass_context
def ListStatsByAccount(ctx):
    """ListVolumeStatsByAccount returns high-level activity measurements for every account."""
    """Values are summed from all the volumes owned by the account."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("")
    try:
        ListVolumeStatsByAccountResult = ctx.element.list_volume_stats_by_account()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(ListVolumeStatsByAccountResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('RestoreDeleted', short_help="""RestoreDeletedVolume marks a deleted volume as active again. This action makes the volume immediately available for iSCSI connection. """)
@click.option('--volume_id',
              type=int,
              required=True,
              help="""VolumeID for the deleted volume to restore. """)
@pass_context
def RestoreDeleted(ctx,
           volume_id):
    """RestoreDeletedVolume marks a deleted volume as active again."""
    """This action makes the volume immediately available for iSCSI connection."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""volume_id = """+str(volume_id)+""";"""+"")
    try:
        RestoreDeletedVolumeResult = ctx.element.restore_deleted_volume(volume_id=volume_id)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(RestoreDeletedVolumeResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListDeleted', short_help="""ListDeletedVolumes is used to return the entire list of volumes that have been marked for deletion and is purged from the system. """)
@pass_context
def ListDeleted(ctx):
    """ListDeletedVolumes is used to return the entire list of volumes that have been marked for deletion and is purged from the system."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("")
    try:
        ListDeletedVolumesResult = ctx.element.list_deleted_volumes()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(ListDeletedVolumesResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetAsyncResult', short_help="""Used to retrieve the result of asynchronous method calls. Some method calls are long running and do not complete when the initial response is sent. To obtain the result of the method call, polling with GetAsyncResult is required.  GetAsyncResult returns the overall status of the operation (in progress, completed, or error) in a standard fashion, but the actual data returned for the operation depends on the original method call and the return data is documented with each method.  The result for a completed asynchronous method call can only be retrieved once. Once the final result has been returned, later attempts returns an error. """)
@click.option('--async_handle',
              type=int,
              required=True,
              help="""A value that was returned from the original asynchronous method call. """)
@pass_context
def GetAsyncResult(ctx,
           async_handle):
    """Used to retrieve the result of asynchronous method calls."""
    """Some method calls are long running and do not complete when the initial response is sent."""
    """To obtain the result of the method call, polling with GetAsyncResult is required."""
    """"""
    """GetAsyncResult returns the overall status of the operation (in progress, completed, or error) in a standard fashion,"""
    """but the actual data returned for the operation depends on the original method call and the return data is documented with each method."""
    """"""
    """The result for a completed asynchronous method call can only be retrieved once."""
    """Once the final result has been returned, later attempts returns an error."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""async_handle = """+str(async_handle)+""";"""+"")
    try:
        GetAsyncResultResult = ctx.element.get_async_result(async_handle=async_handle)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(GetAsyncResultResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('Delete', short_help="""DeleteVolume marks an active volume for deletion. It is purged (permanently deleted) after the cleanup interval elapses. After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state. It is not returned in target discovery requests.  Any snapshots of a volume that has been marked to delete are not affected. Snapshots are kept until the volume is purged from the system.  If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.  If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state. The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume. Until the deleted volume is purged, it can be restored and data transfers resumes. If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed. The purged volume becomes permanently unavailable. """)
@click.option('--volume_id',
              type=int,
              required=True,
              help="""The ID of the volume to delete. """)
@pass_context
def Delete(ctx,
           volume_id):
    """DeleteVolume marks an active volume for deletion."""
    """It is purged (permanently deleted) after the cleanup interval elapses."""
    """After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state."""
    """It is not returned in target discovery requests."""
    """"""
    """Any snapshots of a volume that has been marked to delete are not affected."""
    """Snapshots are kept until the volume is purged from the system."""
    """"""
    """If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped."""
    """"""
    """If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state."""
    """The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume."""
    """Until the deleted volume is purged, it can be restored and data transfers resumes."""
    """If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed."""
    """The purged volume becomes permanently unavailable."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""volume_id = """+str(volume_id)+""";"""+"")
    try:
        DeleteVolumeResult = ctx.element.delete_volume(volume_id=volume_id)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(DeleteVolumeResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListAsyncResults', short_help="""You can use ListAsyncResults to list the results of all currently running and completed asynchronous methods on the system. Querying asynchronous results with ListAsyncResults does not cause completed asyncHandles to expire; you can use GetAsyncResult to query any of the asyncHandles returned by ListAsyncResults. """)
@click.option('--async_result_types',
              type=str,
              required=False,
              help="""An optional list of types of results. You can use this list to restrict the results to only these types of operations. Possible values:BulkVolume: Copy operations between volumes, such as backups or restores.Clone: Volume cloning operations.DriveRemoval: Operations involving the system copying data from a drive in preparation to remove it from the cluster.RtfiPendingNode: Operations involving the system installing compatible software on a node before adding it to the cluster. """)
@pass_context
def ListAsyncResults(ctx,
           async_result_types = None):
    """You can use ListAsyncResults to list the results of all currently running and completed asynchronous methods on the system. Querying asynchronous results with ListAsyncResults does not cause completed asyncHandles to expire; you can use GetAsyncResult to query any of the asyncHandles returned by ListAsyncResults."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    async_result_types = parser.parse_array(async_result_types)

    ctx.logger.info("""async_result_types = """+str(async_result_types)+""";"""+"")
    try:
        ListAsyncResultsResult = ctx.element.list_async_results(async_result_types=async_result_types)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(ListAsyncResultsResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListStatsByAccessGroup', short_help="""ListVolumeStatsByVolumeAccessGroup is used to get total activity measurements for all of the volumes that are a member of the specified volume access group(s). """)
@click.option('--volume_access_groups',
              type=str,
              required=False,
              help="""An array of VolumeAccessGroupIDs for which volume activity is returned. If no VolumeAccessGroupID is specified, stats for all volume access groups is returned. """)
@pass_context
def ListStatsByAccessGroup(ctx,
           volume_access_groups = None):
    """ListVolumeStatsByVolumeAccessGroup is used to get total activity measurements for all of the volumes that are a member of the specified volume access group(s)."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    volume_access_groups = parser.parse_array(volume_access_groups)

    ctx.logger.info("""volume_access_groups = """+str(volume_access_groups)+""";"""+"")
    try:
        ListVolumeStatsByVolumeAccessGroupResult = ctx.element.list_volume_stats_by_volume_access_group(volume_access_groups=volume_access_groups)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(ListVolumeStatsByVolumeAccessGroupResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('SetDefaultQoS', short_help="""SetDefaultQoS enables you to configure the default Quality of Service (QoS) values (measured in inputs and outputs per second, or IOPS) for all volumes not yet created. """)
@click.option('--min_iops',
              type=int,
              required=False,
              help="""The minimum number of sustained IOPS that are provided by the cluster to a volume. """)
@click.option('--max_iops',
              type=int,
              required=False,
              help="""The maximum number of sustained IOPS that are provided by the cluster to a volume. """)
@click.option('--burst_iops',
              type=int,
              required=False,
              help="""The maximum number of IOPS allowed in a short burst scenario. """)
@pass_context
def SetDefaultQoS(ctx,
           min_iops = None,
           max_iops = None,
           burst_iops = None):
    """SetDefaultQoS enables you to configure the default Quality of Service (QoS) values (measured in inputs and outputs per second, or IOPS) for all volumes not yet created."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""min_iops = """+str(min_iops)+""";"""+"""max_iops = """+str(max_iops)+""";"""+"""burst_iops = """+str(burst_iops)+""";"""+"")
    try:
        SetDefaultQoSResult = ctx.element.set_default_qos(min_iops=min_iops, max_iops=max_iops, burst_iops=burst_iops)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(SetDefaultQoSResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetDefaultQoS', short_help="""GetDefaultQoS is used to retrieve the default QoS values that are set for a volume if QoS is not supplied. """)
@pass_context
def GetDefaultQoS(ctx):
    """GetDefaultQoS is used to retrieve the default QoS values that are set for a volume if QoS is not supplied."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("")
    try:
        VolumeQOS = ctx.element.get_default_qos()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(VolumeQOS, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetStats', short_help="""GetVolumeStats is used to retrieve high-level activity measurements for a single volume. Values are cumulative from the creation of the volume. """)
@click.option('--volume_id',
              type=int,
              required=True,
              help="""Specifies the volume for which statistics is gathered. """)
@pass_context
def GetStats(ctx,
           volume_id):
    """GetVolumeStats is used to retrieve high-level activity measurements for a single volume."""
    """Values are cumulative from the creation of the volume."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""volume_id = """+str(volume_id)+""";"""+"")
    try:
        GetVolumeStatsResult = ctx.element.get_volume_stats(volume_id=volume_id)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(GetVolumeStatsResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetCount', short_help="""GetVolumeCount enables you to retrieve the number of volumes currently in the system. """)
@pass_context
def GetCount(ctx):
    """GetVolumeCount enables you to retrieve the number of volumes currently in the system."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("")
    try:
        GetVolumeCountResult = ctx.element.get_volume_count()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(GetVolumeCountResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

