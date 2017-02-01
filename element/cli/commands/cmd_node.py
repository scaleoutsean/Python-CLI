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
    """setnetworkconfig listpending getorigin listpendingactive listall getpendingoperation liststats add setconfig getnetworkconfig getstats getconfig remove listactive getbootstrapconfig """

@cli.command('setnetworkconfig', short_help="""The "SetNetworkConfig" method is used to set the network configuration for a node. To see the states in which these objects can be modified, see "Network Object for 1G and 10G Interfaces" on page 109 of the Element API. To display the current network settings for a node, run the "GetNetworkConfig" method.  WARNING! Changing the "bond-mode" on a node can cause a temporary loss of network connectivity. Caution should be taken when using this method.  Note: This method is available only through the per-node API endpoint 5.0 or later. """)
@click.option('--network',
              type=str,
              required=True,
              help="""Provide in json format: Objects that will be changed for the node network settings. """)
@pass_context
def setnetworkconfig(ctx,
           network):
    """The &quot;SetNetworkConfig&quot; method is used to set the network configuration for a node. To see the states in which these objects can be modified, see &quot;Network Object for 1G and 10G Interfaces&quot; on page 109 of the Element API. To display the current network settings for a node, run the &quot;GetNetworkConfig&quot; method."""
    """"""
    """WARNING! Changing the &quot;bond-mode&quot; on a node can cause a temporary loss of network connectivity. Caution should be taken when using this method."""
    """"""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    if(network is not None):
        try:
            kwargsDict = simplejson.loads(network)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1) 
        network = Network(**kwargsDict)
    

    ctx.logger.info("""network = """+str(network)+""";"""+"")
    try:
        _SetNetworkConfigResult = ctx.element.set_network_config(network=network)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_SetNetworkConfigResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listpending', short_help="""Gets the list of pending nodes. Pending nodes are running and configured to join the cluster, but have not been added via the AddNodes method. """)
@pass_context
def listpending(ctx):
    """Gets the list of pending nodes."""
    """Pending nodes are running and configured to join the cluster, but have not been added via the AddNodes method."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _ListPendingNodesResult = ctx.element.list_pending_nodes()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListPendingNodesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getorigin', short_help="""GetOrigin enables you to retrieve the origination certificate for where the node was built.NOTE: The GetOrigin method may return "null" if there is no origination certification. """)
@click.option('--force',
              type=bool,
              required=True,
              help="""""")
@pass_context
def getorigin(ctx,
           force):
    """GetOrigin enables you to retrieve the origination certificate for where the node was built.NOTE: The GetOrigin method may return &quot;null&quot; if there is no origination certification."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("""force = """+str(force)+""";"""+"")
    try:
        _GetOriginResult = ctx.element.get_origin(force=force)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetOriginResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listpendingactive', short_help="""ListPendingActiveNodes returns the list of nodes in the cluster that are currently in the PendingActive state, between the pending and active states. These are nodes that are currently being returned to the factory image. """)
@pass_context
def listpendingactive(ctx):
    """ListPendingActiveNodes returns the list of nodes in the cluster that are currently in the PendingActive state, between the pending and active states. These are nodes that are currently being returned to the factory image."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _ListPendingActiveNodesResult = ctx.element.list_pending_active_nodes()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListPendingActiveNodesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listall', short_help="""ListAllNodes enables you to retrieve a list of active and pending nodes in the cluster. """)
@pass_context
def listall(ctx):
    """ListAllNodes enables you to retrieve a list of active and pending nodes in the cluster."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _ListAllNodesResult = ctx.element.list_all_nodes()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListAllNodesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getpendingoperation', short_help="""GetPendingOperation is used to detect an operation on a node that is currently in progress. This method can also be used to report back when an operation has completed.  Note: This method is available only through the per-node API endpoint 5.0 or later. """)
@pass_context
def getpendingoperation(ctx):
    """GetPendingOperation is used to detect an operation on a node that is currently in progress. This method can also be used to report back when an operation has completed."""
    """"""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _GetPendingOperationResult = ctx.element.get_pending_operation()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetPendingOperationResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('liststats', short_help="""ListNodeStats is used to return the high-level activity measurements for all nodes in a cluster. """)
@pass_context
def liststats(ctx):
    """ListNodeStats is used to return the high-level activity measurements for all nodes in a cluster."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _ListNodeStatsResult = ctx.element.list_node_stats()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListNodeStatsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('add', short_help="""AddNodes is used to add one or more new nodes to the cluster. When a node is not configured and starts up for the first time you are prompted to configure the node. Once a node is configured it is registered as a "pending node" with the cluster.  Adding a node to a cluster that has been set up for virtual networking will require a sufficient number of virtual storage IP addresses to allocate a virtual IP to the new node. If there are no virtual IP addresses available for the new node, the AddNode operation will not complete successfully. Use the "ModifyVirtualNetwork" method to add more storage IP addresses to your virtual network.  The software version on each node in a cluster must be compatible. Run the "ListAllNodes" API to see what versions of software are currently running on the cluster nodes. For an explanation of software version compatibility, see "Node Versioning and Compatibility" in the Element API guide.  Once a node has been added, the drives on the node are made available and can then be added via the "AddDrives" method to increase the storage capacity of the cluster.  Note: It may take several seconds after adding a new Node for it to start up and register the drives as being available. """)
@click.option('--pendingnodes',
              type=str,
              required=True,
              help="""List of PendingNodeIDs for the Nodes to be added. You can obtain the list of Pending Nodes via the ListPendingNodes method. """)
@pass_context
def add(ctx,
           pendingnodes):
    """AddNodes is used to add one or more new nodes to the cluster. When a node is not configured and starts up for the first time you are prompted to configure the node. Once a node is configured it is registered as a &quot;pending node&quot; with the cluster."""
    """"""
    """Adding a node to a cluster that has been set up for virtual networking will require a sufficient number of virtual storage IP addresses to allocate a virtual IP to the new node. If there are no virtual IP addresses available for the new node, the AddNode operation will not complete successfully. Use the &quot;ModifyVirtualNetwork&quot; method to add more storage IP addresses to your virtual network."""
    """"""
    """The software version on each node in a cluster must be compatible. Run the &quot;ListAllNodes&quot; API to see what versions of software are currently running on the cluster nodes. For an explanation of software version compatibility, see &quot;Node Versioning and Compatibility&quot; in the Element API guide."""
    """"""
    """Once a node has been added, the drives on the node are made available and can then be added via the &quot;AddDrives&quot; method to increase the storage capacity of the cluster."""
    """"""
    """Note: It may take several seconds after adding a new Node for it to start up and register the drives as being available."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    pendingnodes = parser.parse_array(pendingnodes)
    

    ctx.logger.info("""pendingnodes = """+str(pendingnodes)+""";"""+"")
    try:
        _AddNodesResult = ctx.element.add_nodes(pending_nodes=pendingnodes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_AddNodesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('setconfig', short_help="""The SetConfig API method is used to set all the configuration information for the node. This includes the same information available via calls to SetClusterConfig and SetNetworkConfig in one API method.  Warning! Changing the 'bond-mode' on a node can cause a temporary loss of network connectivity. Caution should be taken when using this method.  Note: This method is available only through the per-node API endpoint 5.0 or later. """)
@click.option('--config',
              type=str,
              required=True,
              help="""Provide in json format: Objects that you want changed for the cluster interface settings. """)
@pass_context
def setconfig(ctx,
           config):
    """The SetConfig API method is used to set all the configuration information for the node. This includes the same information available via calls to SetClusterConfig and SetNetworkConfig in one API method."""
    """"""
    """Warning! Changing the &#x27;bond-mode&#x27; on a node can cause a temporary loss of network connectivity. Caution should be taken when using this method."""
    """"""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    if(config is not None):
        try:
            kwargsDict = simplejson.loads(config)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1) 
        config = Config(**kwargsDict)
    

    ctx.logger.info("""config = """+str(config)+""";"""+"")
    try:
        _SetConfigResult = ctx.element.set_config(config=config)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_SetConfigResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getnetworkconfig', short_help="""The GetNetworkConfig API method is used to display the network configuration information for a node.  Note: This method is available only through the per-node API endpoint 5.0 or later. """)
@pass_context
def getnetworkconfig(ctx):
    """The GetNetworkConfig API method is used to display the network configuration information for a node."""
    """"""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _GetNetworkConfigResult = ctx.element.get_network_config()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetNetworkConfigResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getstats', short_help="""GetNodeStats is used to return the high-level activity measurements for a single node. """)
@click.option('--nodeid',
              type=int,
              required=True,
              help="""Specifies the node for which statistics are gathered. """)
@pass_context
def getstats(ctx,
           nodeid):
    """GetNodeStats is used to return the high-level activity measurements for a single node."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("""nodeid = """+str(nodeid)+""";"""+"")
    try:
        _GetNodeStatsResult = ctx.element.get_node_stats(node_id=nodeid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetNodeStatsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getconfig', short_help="""The GetConfig API method is used to retrieve all the configuration information for the node. This one API method includes the same information available in both "GetClusterConfig" and "GetNetworkConfig" methods.  Note: This method is available only through the per-node API endpoint 5.0 or later. """)
@pass_context
def getconfig(ctx):
    """The GetConfig API method is used to retrieve all the configuration information for the node. This one API method includes the same information available in both &quot;GetClusterConfig&quot; and &quot;GetNetworkConfig&quot; methods."""
    """"""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _GetConfigResult = ctx.element.get_config()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetConfigResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('remove', short_help="""RemoveNodes is used to remove one or more nodes that should no longer participate in the cluster. Before removing a node, all drives it contains must first be removed with "RemoveDrives" method. A node cannot be removed until the RemoveDrives process has completed and all data has been migrated away from the node.  Once removed, a node registers itself as a pending node and can be added again, or shut down which removes it from the "Pending Node" list. """)
@click.option('--nodes',
              type=str,
              required=True,
              help="""List of NodeIDs for the nodes to be removed. """)
@pass_context
def remove(ctx,
           nodes):
    """RemoveNodes is used to remove one or more nodes that should no longer participate in the cluster. Before removing a node, all drives it contains must first be removed with &quot;RemoveDrives&quot; method. A node cannot be removed until the RemoveDrives process has completed and all data has been migrated away from the node."""
    """"""
    """Once removed, a node registers itself as a pending node and can be added again, or shut down which removes it from the &quot;Pending Node&quot; list."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    nodes = parser.parse_array(nodes)
    

    ctx.logger.info("""nodes = """+str(nodes)+""";"""+"")
    try:
        _RemoveNodesResult = ctx.element.remove_nodes(nodes=nodes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_RemoveNodesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listactive', short_help="""ListActiveNodes returns the list of currently active nodes that are in the cluster. """)
@pass_context
def listactive(ctx):
    """ListActiveNodes returns the list of currently active nodes that are in the cluster."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _ListActiveNodesResult = ctx.element.list_active_nodes()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListActiveNodesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getbootstrapconfig', short_help="""GetBootstrapConfig returns the cluster name and node name from the bootstrap configuration file. This API method should be performed on an individual node before it has been configured into a cluster. The resulting information from this method is used in the Cluster Configuration UI when the cluster is eventually created. """)
@pass_context
def getbootstrapconfig(ctx):
    """GetBootstrapConfig returns the cluster name and node name from the bootstrap configuration file. This API method should be performed on an individual node before it has been configured into a cluster. The resulting information from this method is used in the Cluster Configuration UI when the cluster is eventually created."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _GetBootstrapConfigResult = ctx.element.get_bootstrap_config()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetBootstrapConfigResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

