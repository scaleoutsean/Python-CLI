import click
from click.testing import CliRunner
from element.cli import cli
import jsonpickle
import random
import os
import csv
from solidfire.models import *
from unittest.mock import MagicMock

def rand_string(length):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(length))

def check_strange_inputs():
    # First, make a new account. Set the CHAPSecret to confirm that CHAPSecrets work. This exercises a CHAPSecret parameter
    runner = CliRunner()
    account_name = rand_string(15)
    result = runner.invoke(cli.cli, ['-c','0','-j',"Account", "Add", '--username', account_name, '--initiator_secret', "solidfire1234"])
    account = jsonpickle.decode(result.output)
    result = runner.invoke(cli.cli, ['-c','0','-j',"Account", "GetByID", '--account_id', account.account_id])
    fullAccount = jsonpickle.decode(result.output)

    # Verify that CHAPSecret is working.
    assert fullAccount.account.initiator_secret.secret == "solidfire1234"

    # Next, make two volumes
    result = runner.invoke(cli.cli, ['-c','0','-j',"Volume", "Create", '--name', rand_string(15), "--account_id", account.account_id, "--total_size", "1000000000", "--enable512e", True])
    volume1 = jsonpickle.decode(result.output)
    result = runner.invoke(cli.cli, ['-c','0','-j',"Volume", "Create", '--name', rand_string(15), "--account_id", account.account_id, "--total_size", "1000000000", "--enable512e", True])
    volume2 = jsonpickle.decode(result.output)

    # Now we modify the QoS settings on Volume1 in order to test the functionality of a complex param type:
    result = runner.invoke(cli.cli, ['-c','0','-j',"Volume", "Modify", '--volume_ids', volume1.volume_id, '--qos_min_iops', 100])

    # Now we get the volumes from the given account to make sure they're there and that the QoS Change took.:
    result = runner.invoke(cli.cli, ['-c','0','-j',"Volume", "List", '--accounts', account.account_id])
    volumes_list = jsonpickle.decode(result.output)
    assert len(volumes_list.volumes) == 2
    newVolume1 = [volume for volume in volumes_list.volumes if volume.volume_id == volume1.volume_id][0]
    assert newVolume1.qos.min_iops == 100

    # Now we delete and purge them. This exercises the use of an array.
    result = runner.invoke(cli.cli, ['-c','0','-j',"Volume", "Delete", '--volume_ids', ','.join([str(volume1.volume_id), str(volume2.volume_id)])])
    result = runner.invoke(cli.cli, ['-c','0','-j',"Volume", "PurgeDeleted", '--volume_ids', ','.join([str(volume1.volume_id), str(volume2.volume_id)])])

    # Finally, we check to make sure they're gone.
    result = runner.invoke(cli.cli, ['-c','0','-j',"Volume", "List", '--accounts', account.account_id])
    volumes_list = jsonpickle.decode(result.output)
    assert len(volumes_list.volumes) == 0

    # Now tear down the account.
    result = runner.invoke(cli.cli, ['-c','0','-j',"Account", "Remove", '--account_id', account.account_id])

    # Now, to test a supercomplex parameter, we need to make a volume access group and set the attributes via json:
    result = runner.invoke(cli.cli, ['-c','0','-j',"VolumeAccessGroup","Create","--name", "DISPOSABLE", '--attributes', '{\"blah\":\"blah\"}'])
    volume_access_group = jsonpickle.decode(result.output)
    assert volume_access_group.volume_access_group.attributes["blah"] == "blah"
    result = runner.invoke(cli.cli, ['-c','0','-j',"VolumeAccessGroup", "Delete", '--volume_access_group_id', volume_access_group.volume_access_group_id])


check_strange_inputs()