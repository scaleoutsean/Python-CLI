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
from solidfire.custom.models import *
from uuid import UUID
from element import exceptions
from solidfire import common


@click.group()
@pass_context
def cli(ctx):
    """completecluster completevolume listclusterpairs removevolumepair startvolume listactivepairedvolumes modifyvolumepair startcluster removeclusterpair """

@cli.command('completecluster', short_help="""The CompleteClusterPairing method is the second step in the cluster pairing process. Use this method with the encoded key received from the "StartClusterPairing" API method to complete the cluster pairing process. """)
@click.option('--clusterpairingkey',
              type=str,
              required=True,
              help="""A string of characters that is returned from the "StartClusterPairing" API method. """)
@pass_context
def completecluster(ctx,
           clusterpairingkey):
    """The CompleteClusterPairing method is the second step in the cluster pairing process."""
    """Use this method with the encoded key received from the &quot;StartClusterPairing&quot; API method to complete the cluster pairing process."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("""clusterpairingkey = """+str(clusterpairingkey)+""";"""+"")
    try:
        _CompleteClusterPairingResult = ctx.element.complete_cluster_pairing(cluster_pairing_key=clusterpairingkey)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_CompleteClusterPairingResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('completevolume', short_help="""CompleteVolumePairing is used to complete the pairing of two volumes. """)
@click.option('--volumepairingkey',
              type=str,
              required=True,
              help="""The key returned from the "StartVolumePairing" API method. """)
@click.option('--volumeid',
              type=int,
              required=True,
              help="""The ID of volume on which to complete the pairing process. """)
@pass_context
def completevolume(ctx,
           volumepairingkey,
           volumeid):
    """CompleteVolumePairing is used to complete the pairing of two volumes."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("""volumepairingkey = """+str(volumepairingkey)+""";"""+"""volumeid = """+str(volumeid)+""";"""+"")
    try:
        _CompleteVolumePairingResult = ctx.element.complete_volume_pairing(volume_pairing_key=volumepairingkey, volume_id=volumeid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_CompleteVolumePairingResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listclusterpairs', short_help="""ListClusterPairs is used to list all of the clusters a cluster is paired with. This method returns information about active and pending cluster pairings, such as statistics about the current pairing as well as the connectivity and latency (in milliseconds) of the cluster pairing. """)
@pass_context
def listclusterpairs(ctx):
    """ListClusterPairs is used to list all of the clusters a cluster is paired with."""
    """This method returns information about active and pending cluster pairings, such as statistics about the current pairing as well as the connectivity and latency (in milliseconds) of the cluster pairing."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _ListClusterPairsResult = ctx.element.list_cluster_pairs()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListClusterPairsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('removevolumepair', short_help="""RemoveVolumePair is used to remove the remote pairing between two volumes. When the volume pairing information is removed, data is no longer replicated to or from the volume. This method should be run on both the source and target volumes that are paired together. """)
@click.option('--volumeid',
              type=int,
              required=True,
              help="""ID of the volume on which to stop the replication process. """)
@pass_context
def removevolumepair(ctx,
           volumeid):
    """RemoveVolumePair is used to remove the remote pairing between two volumes."""
    """When the volume pairing information is removed, data is no longer replicated to or from the volume."""
    """This method should be run on both the source and target volumes that are paired together."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("""volumeid = """+str(volumeid)+""";"""+"")
    try:
        _RemoveVolumePairResult = ctx.element.remove_volume_pair(volume_id=volumeid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_RemoveVolumePairResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('startvolume', short_help="""StartVolumePairing is used to create an encoded key from a volume that is used to pair with another volume. The key that this method creates is used in the "CompleteVolumePairing" API method to establish a volume pairing. """)
@click.option('--volumeid',
              type=int,
              required=True,
              help="""The ID of the volume on which to start the pairing process. """)
@click.option('--mode',
              type=str,
              required=False,
              help="""The mode of the volume on which to start the pairing process. The mode can only be set if the volume is the source volume. Possible values: Async: (default if no mode parameter specified) Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster. Sync: Source acknowledges write when the data is stored locally and on the remote cluster. SnapshotsOnly: Only snapshots created on the source cluster will be replicated. Active writes from the source volume will not be replicated. """)
@pass_context
def startvolume(ctx,
           volumeid,
           mode = None):
    """StartVolumePairing is used to create an encoded key from a volume that is used to pair with another volume."""
    """The key that this method creates is used in the &quot;CompleteVolumePairing&quot; API method to establish a volume pairing."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("""volumeid = """+str(volumeid)+""";"""+"""mode = """+str(mode)+""";"""+"")
    try:
        _StartVolumePairingResult = ctx.element.start_volume_pairing(volume_id=volumeid, mode=mode)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_StartVolumePairingResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listactivepairedvolumes', short_help="""ListActivePairedVolumes is used to list all of the active volumes paired with a volume. Volumes listed in the return for this method include volumes with active and pending pairings. """)
@pass_context
def listactivepairedvolumes(ctx):
    """ListActivePairedVolumes is used to list all of the active volumes paired with a volume."""
    """Volumes listed in the return for this method include volumes with active and pending pairings."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _ListActivePairedVolumesResult = ctx.element.list_active_paired_volumes()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListActivePairedVolumesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('modifyvolumepair', short_help="""ModifyVolumePair is used to pause or restart replication between a pair of volumes. """)
@click.option('--volumeid',
              type=int,
              required=True,
              help="""Identification number of the volume to be modified. """)
@click.option('--pausedmanual',
              type=bool,
              required=False,
              help="""Valid values that can be entered: true: to pause volume replication. false: to restart volume replication. If no value is specified, no change in replication is performed. """)
@click.option('--mode',
              type=str,
              required=False,
              help="""Volume replication mode. Possible values: Async: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster. Sync: The source acknowledges the write when the data is stored locally and on the remote cluster. SnapshotsOnly: Only snapshots created on the source cluster will be replicated. Active writes from the source volume are not replicated. """)
@pass_context
def modifyvolumepair(ctx,
           volumeid,
           pausedmanual = None,
           mode = None):
    """ModifyVolumePair is used to pause or restart replication between a pair of volumes."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("""volumeid = """+str(volumeid)+""";"""+"""pausedmanual = """+str(pausedmanual)+""";"""+"""mode = """+str(mode)+""";"""+"")
    try:
        _ModifyVolumePairResult = ctx.element.modify_volume_pair(volume_id=volumeid, paused_manual=pausedmanual, mode=mode)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ModifyVolumePairResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('startcluster', short_help="""StartClusterPairing is used to create an encoded key from a cluster that is used to pair with another cluster. The key created from this API method is used in the "CompleteClusterPairing" API method to establish a cluster pairing. You can pair a cluster with a maximum of four other SolidFire clusters. """)
@pass_context
def startcluster(ctx):
    """StartClusterPairing is used to create an encoded key from a cluster that is used to pair with another cluster."""
    """The key created from this API method is used in the &quot;CompleteClusterPairing&quot; API method to establish a cluster pairing."""
    """You can pair a cluster with a maximum of four other SolidFire clusters."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _StartClusterPairingResult = ctx.element.start_cluster_pairing()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_StartClusterPairingResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('removeclusterpair', short_help="""You can use the RemoveClusterPair method to close the open connections between two paired clusters. Note: Before you remove a cluster pair, you must first remove all volume pairing to the clusters with the "RemoveVolumePair" API method. """)
@click.option('--clusterpairid',
              type=int,
              required=True,
              help="""Unique identifier used to pair two clusters. """)
@pass_context
def removeclusterpair(ctx,
           clusterpairid):
    """You can use the RemoveClusterPair method to close the open connections between two paired clusters."""
    """Note: Before you remove a cluster pair, you must first remove all volume pairing to the clusters with the &quot;RemoveVolumePair&quot; API method."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("""clusterpairid = """+str(clusterpairid)+""";"""+"")
    try:
        _RemoveClusterPairResult = ctx.element.remove_cluster_pair(cluster_pair_id=clusterpairid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_RemoveClusterPairResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

