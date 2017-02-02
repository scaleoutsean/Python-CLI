-----------------
Intended Audience
-----------------
The SolidFire CLI is intended as an alternate method for interefacing with SolidFire products. It is a sibling
product of the PowerShell CLI, which is intended to be used on Windows and Macintosh. If, for some reason, the
PowerShell CLI is undesirable for you, we've created a python CLI which will deliver string based solutions!

----------
To Install
----------
pip install solidfire-cli

-----------------------------------
Operating Systems and Distributions
-----------------------------------
Windows 7, 8, 10

---------------------
Connection Management
---------------------
# To run a command on a given connection, use the mvip, login, and password options.
sfcli --mvip 10.117.60.15 --login admin --password admin Account List

# To store a given connection, use the Connection Push and supply the name option.
sfcli --mvip 10.117.60.15 --login admin --password admin --name "Example" Connection Push

# To use a connection you've stored, use -n or --name or -c or -connectionIndex
#   Find by name:
sfcli -n Example Account List
#   Find by index:
sfcli -c 0 Account List
#   Use index 0 if no connection is provided, but at least one is stored.
sfcli Account List

# To remove a given connection, use the Connection Remove command.
#   Remove by name:
sfcli Connection Remove -n Example
#   Remove by index:
sfcli Connection Remove -i -1 # Removes the newly pushed connection.
sfcli Connection Remove -i 0 # Removes the oldest pushed connection.
sfcli Connection Remove -i 1 # Removes the second oldest connection.

------------------
Executing Commands
------------------
# There are two types of commands: commands with standard parameters and commands
# which take json as an input. Most often the latter type of command is specifically
# designed for large configuration files where you might want to back up the configuration
# and recover it again later or when you are storing key-value pairs as an attributes.
# This keeps the CLI similar enough to other SolidFire tools that it is easily usable.

# Command with standard parameters:
sfcli -c 0 Account GetByID --account_id 94

# Commands with non-standard parameters:
# There are a total of 5 of these commands:
# 1. Node SetConfig
# Example:
#     First, we get the existing network config.
$returnValue = sfcli -c 0 -j Node GetConfig | ConvertFrom-Json
#     Next, we extract the network part of the config and escape the '"'s.
$config = $returnValue.config | ConvertTo-Json
$escaped = $config.replace('"', '\"')
#     HERE IS WHERE WE'D MAKE ANY CHANGES
#     And here, we feed it back in.
sfcli -c 0 -j Node SetNetworkConfig --config $escaped

# 2. Node SetNetworkConfig
# Example:
#     First, we get the existing network config.
$returnValue = sfcli -c 0 -j Node GetNetworkConfig | ConvertFrom-Json
#     Next, we extract the network part of the config and escape the '"'s.
$network = $returnValue.network | ConvertTo-Json
$escaped = $network.replace('"', '\"')
#     HERE IS WHERE WE'D MAKE ANY CHANGES
#     And here, we feed it back in.
sfcli -c 0 -j Node SetNetworkConfig --network $escaped

# 3. SFApi Invoke
# Example:
$account = sfcli -c 0 SFApi Invoke --method GetAccountByID --parameters '{\"accountID\":94}'

# 4. Snapshot CreateSchedule
# Example:


# 5. Snapshot ModifySchedule

----------------------
Nonstandard Parameters
----------------------
Below are some template strings for each of the nonstandard parameters. To run the command, you can use one of the methods listed above to get the current values and substitute some new ones, or you can copy/paste the below parameters.
Note:
- If running in a PowerShell window, surround the string like so: 'STRING'
- If running in a Bash window, surround the string like so ^"STRING^"
So, if I were running sfcli volume clonemultiple on windows, I could use the following command:
sfcli --mvip 10.117.61.44 -p --username admin --password admin Volume CloneMultiple --volumes '[{\"volume_id\": 1979},{\"volume_id\": 1980}]'

--lunassignments
[
    {
        \"volume_id\": int        [Required],
        \"lun\": int        [Required]
    }
]

--network
{
    \"bond10_g\": {
        \"_default\": true/false,
        \"bond_master\": \"string\"        [Required],
        \"virtual_network_tag\": \"string\"        [Required],
        \"address\": \"string\",
        \"auto\": true/false,
        \"bond_downdelay\": \"string\",
        \"bond_fail_over_mac\": \"string\",
        \"bond_primary_reselect\": \"string\",
        \"bond_lacp_rate\": \"string\",
        \"bond_miimon\": \"string\",
        \"bond_mode\": \"string\",
        \"bond_slaves\": \"string\",
        \"bond_updelay\": \"string\",
        \"broadcast\": \"string\",
        \"dns_nameservers\": \"string\",
        \"dns_search\": \"string\",
        \"family\": \"string\",
        \"gateway\": \"string\",
        \"mac_address\": \"string\",
        \"mac_address_permanent\": \"string\",
        \"method\": \"string\",
        \"mtu\": \"string\",
        \"netmask\": \"string\",
        \"network\": \"string\",
        \"physical\": {
            \"address\": \"string\",
            \"mac_address\": \"string\",
            \"mac_address_permanent\": \"string\",
            \"mtu\": \"string\",
            \"netmask\": \"string\",
            \"network\": \"string\",
            \"up_and_running\": true/false
        },
        \"routes\": [
            \"string\"
        ],
        \"status\": \"string\",
        \"symmetric_route_rules\": [
            \"string\"
        ],
        \"up_and_running\": true/false
    },
    \"bond1_g\": {
        \"_default\": true/false,
        \"bond_master\": \"string\"        [Required],
        \"virtual_network_tag\": \"string\"        [Required],
        \"address\": \"string\",
        \"auto\": true/false,
        \"bond_downdelay\": \"string\",
        \"bond_fail_over_mac\": \"string\",
        \"bond_primary_reselect\": \"string\",
        \"bond_lacp_rate\": \"string\",
        \"bond_miimon\": \"string\",
        \"bond_mode\": \"string\",
        \"bond_slaves\": \"string\",
        \"bond_updelay\": \"string\",
        \"broadcast\": \"string\",
        \"dns_nameservers\": \"string\",
        \"dns_search\": \"string\",
        \"family\": \"string\",
        \"gateway\": \"string\",
        \"mac_address\": \"string\",
        \"mac_address_permanent\": \"string\",
        \"method\": \"string\",
        \"mtu\": \"string\",
        \"netmask\": \"string\",
        \"network\": \"string\",
        \"physical\": {
            \"address\": \"string\",
            \"mac_address\": \"string\",
            \"mac_address_permanent\": \"string\",
            \"mtu\": \"string\",
            \"netmask\": \"string\",
            \"network\": \"string\",
            \"up_and_running\": true/false
        },
        \"routes\": [
            \"string\"
        ],
        \"status\": \"string\",
        \"symmetric_route_rules\": [
            \"string\"
        ],
        \"up_and_running\": true/false
    },
    \"eth0\": {
        \"_default\": true/false,
        \"bond_master\": \"string\"        [Required],
        \"virtual_network_tag\": \"string\"        [Required],
        \"address\": \"string\",
        \"auto\": true/false,
        \"bond_downdelay\": \"string\",
        \"bond_fail_over_mac\": \"string\",
        \"bond_primary_reselect\": \"string\",
        \"bond_lacp_rate\": \"string\",
        \"bond_miimon\": \"string\",
        \"bond_mode\": \"string\",
        \"bond_slaves\": \"string\",
        \"bond_updelay\": \"string\",
        \"broadcast\": \"string\",
        \"dns_nameservers\": \"string\",
        \"dns_search\": \"string\",
        \"family\": \"string\",
        \"gateway\": \"string\",
        \"mac_address\": \"string\",
        \"mac_address_permanent\": \"string\",
        \"method\": \"string\",
        \"mtu\": \"string\",
        \"netmask\": \"string\",
        \"network\": \"string\",
        \"physical\": {
            \"address\": \"string\",
            \"mac_address\": \"string\",
            \"mac_address_permanent\": \"string\",
            \"mtu\": \"string\",
            \"netmask\": \"string\",
            \"network\": \"string\",
            \"up_and_running\": true/false
        },
        \"routes\": [
            \"string\"
        ],
        \"status\": \"string\",
        \"symmetric_route_rules\": [
            \"string\"
        ],
        \"up_and_running\": true/false
    },
    \"eth1\": {
        \"_default\": true/false,
        \"bond_master\": \"string\"        [Required],
        \"virtual_network_tag\": \"string\"        [Required],
        \"address\": \"string\",
        \"auto\": true/false,
        \"bond_downdelay\": \"string\",
        \"bond_fail_over_mac\": \"string\",
        \"bond_primary_reselect\": \"string\",
        \"bond_lacp_rate\": \"string\",
        \"bond_miimon\": \"string\",
        \"bond_mode\": \"string\",
        \"bond_slaves\": \"string\",
        \"bond_updelay\": \"string\",
        \"broadcast\": \"string\",
        \"dns_nameservers\": \"string\",
        \"dns_search\": \"string\",
        \"family\": \"string\",
        \"gateway\": \"string\",
        \"mac_address\": \"string\",
        \"mac_address_permanent\": \"string\",
        \"method\": \"string\",
        \"mtu\": \"string\",
        \"netmask\": \"string\",
        \"network\": \"string\",
        \"physical\": {
            \"address\": \"string\",
            \"mac_address\": \"string\",
            \"mac_address_permanent\": \"string\",
            \"mtu\": \"string\",
            \"netmask\": \"string\",
            \"network\": \"string\",
            \"up_and_running\": true/false
        },
        \"routes\": [
            \"string\"
        ],
        \"status\": \"string\",
        \"symmetric_route_rules\": [
            \"string\"
        ],
        \"up_and_running\": true/false
    },
    \"eth2\": {
        \"_default\": true/false,
        \"bond_master\": \"string\"        [Required],
        \"virtual_network_tag\": \"string\"        [Required],
        \"address\": \"string\",
        \"auto\": true/false,
        \"bond_downdelay\": \"string\",
        \"bond_fail_over_mac\": \"string\",
        \"bond_primary_reselect\": \"string\",
        \"bond_lacp_rate\": \"string\",
        \"bond_miimon\": \"string\",
        \"bond_mode\": \"string\",
        \"bond_slaves\": \"string\",
        \"bond_updelay\": \"string\",
        \"broadcast\": \"string\",
        \"dns_nameservers\": \"string\",
        \"dns_search\": \"string\",
        \"family\": \"string\",
        \"gateway\": \"string\",
        \"mac_address\": \"string\",
        \"mac_address_permanent\": \"string\",
        \"method\": \"string\",
        \"mtu\": \"string\",
        \"netmask\": \"string\",
        \"network\": \"string\",
        \"physical\": {
            \"address\": \"string\",
            \"mac_address\": \"string\",
            \"mac_address_permanent\": \"string\",
            \"mtu\": \"string\",
            \"netmask\": \"string\",
            \"network\": \"string\",
            \"up_and_running\": true/false
        },
        \"routes\": [
            \"string\"
        ],
        \"status\": \"string\",
        \"symmetric_route_rules\": [
            \"string\"
        ],
        \"up_and_running\": true/false
    },
    \"eth3\": {
        \"_default\": true/false,
        \"bond_master\": \"string\"        [Required],
        \"virtual_network_tag\": \"string\"        [Required],
        \"address\": \"string\",
        \"auto\": true/false,
        \"bond_downdelay\": \"string\",
        \"bond_fail_over_mac\": \"string\",
        \"bond_primary_reselect\": \"string\",
        \"bond_lacp_rate\": \"string\",
        \"bond_miimon\": \"string\",
        \"bond_mode\": \"string\",
        \"bond_slaves\": \"string\",
        \"bond_updelay\": \"string\",
        \"broadcast\": \"string\",
        \"dns_nameservers\": \"string\",
        \"dns_search\": \"string\",
        \"family\": \"string\",
        \"gateway\": \"string\",
        \"mac_address\": \"string\",
        \"mac_address_permanent\": \"string\",
        \"method\": \"string\",
        \"mtu\": \"string\",
        \"netmask\": \"string\",
        \"network\": \"string\",
        \"physical\": {
            \"address\": \"string\",
            \"mac_address\": \"string\",
            \"mac_address_permanent\": \"string\",
            \"mtu\": \"string\",
            \"netmask\": \"string\",
            \"network\": \"string\",
            \"up_and_running\": true/false
        },
        \"routes\": [
            \"string\"
        ],
        \"status\": \"string\",
        \"symmetric_route_rules\": [
            \"string\"
        ],
        \"up_and_running\": true/false
    },
    \"lo\": {
        \"_default\": true/false,
        \"bond_master\": \"string\"        [Required],
        \"virtual_network_tag\": \"string\"        [Required],
        \"address\": \"string\",
        \"auto\": true/false,
        \"bond_downdelay\": \"string\",
        \"bond_fail_over_mac\": \"string\",
        \"bond_primary_reselect\": \"string\",
        \"bond_lacp_rate\": \"string\",
        \"bond_miimon\": \"string\",
        \"bond_mode\": \"string\",
        \"bond_slaves\": \"string\",
        \"bond_updelay\": \"string\",
        \"broadcast\": \"string\",
        \"dns_nameservers\": \"string\",
        \"dns_search\": \"string\",
        \"family\": \"string\",
        \"gateway\": \"string\",
        \"mac_address\": \"string\",
        \"mac_address_permanent\": \"string\",
        \"method\": \"string\",
        \"mtu\": \"string\",
        \"netmask\": \"string\",
        \"network\": \"string\",
        \"physical\": {
            \"address\": \"string\",
            \"mac_address\": \"string\",
            \"mac_address_permanent\": \"string\",
            \"mtu\": \"string\",
            \"netmask\": \"string\",
            \"network\": \"string\",
            \"up_and_running\": true/false
        },
        \"routes\": [
            \"string\"
        ],
        \"status\": \"string\",
        \"symmetric_route_rules\": [
            \"string\"
        ],
        \"up_and_running\": true/false
    }
}

--parameters
\"parameters\": { "arbitrary_key":"arbitrary_value" }

--schedule
{
    \"frequency\": {
    }        [Required],
    \"has_error\": true/false,
    \"last_run_status\": \"string\"        [Required],
    \"last_run_time_started\": \"string\"        [Required],
    \"paused\": true/false,
    \"recurring\": true/false,
    \"run_next_interval\": true/false,
    \"schedule_id\": int,
    \"schedule_info\": {
        \"volume_ids\": [
            int
        ],
        \"snapshot_name\": \"string\",
        \"enable_remote_replication\": true/false,
        \"retention\": \"string\"
    }        [Required],
    \"name\": \"string\"        [Required],
    \"starting_date\": \"string\"        [Required],
    \"to_be_deleted\": true/false
}

--drives
[
    {
        \"drive_id\": int        [Required]
    }
]

--remotehosts
[
    {
        \"host\": \"string\"        [Required],
        \"port\": int        [Required]
    }
]

--traprecipients
[
    {
        \"host\": \"string\"        [Required],
        \"community\": \"string\"        [Required],
        \"port\": int        [Required]
    }
]

--volumes
[
    {
        \"volume_id\": int        [Required],
        \"access\": \"string\",
        \"name\": \"string\",
        \"new_account_id\": int,
        \"new_size\": int,
        \"attributes\": \"attributes\": { "arbitrary_key":"arbitrary_value" }
    }
]

--initiators
[
    {
        \"name\": \"string\"        [Required],
        \"alias\": \"string\",
        \"volume_access_group_id\": int,
        \"attributes\": \"attributes\": { "arbitrary_key":"arbitrary_value" }
    }
]

--attributes
\"attributes\": { "arbitrary_key":"arbitrary_value" }

--usmusers
[
    {
        \"access\": \"string\"        [Required],
        \"name\": \"string\"        [Required],
        \"password\": \"string\"        [Required],
        \"passphrase\": \"string\"        [Required],
        \"sec_level\": \"string\"        [Required]
    }
]

--config
{
    \"cluster\": {
        \"cipi\": \"string\",
        \"cluster\": \"string\",
        \"ensemble\": [
            \"string\"
        ],
        \"mipi\": \"string\",
        \"name\": \"string\",
        \"node_id\": int,
        \"pending_node_id\": int,
        \"role\": \"string\",
        \"sipi\": \"string\",
        \"state\": \"string\"
    }        [Required],
    \"network\": {
        \"bond10_g\": {
            \"_default\": true/false,
            \"bond_master\": \"string\"        [Required],
            \"virtual_network_tag\": \"string\"        [Required],
            \"address\": \"string\",
            \"auto\": true/false,
            \"bond_downdelay\": \"string\",
            \"bond_fail_over_mac\": \"string\",
            \"bond_primary_reselect\": \"string\",
            \"bond_lacp_rate\": \"string\",
            \"bond_miimon\": \"string\",
            \"bond_mode\": \"string\",
            \"bond_slaves\": \"string\",
            \"bond_updelay\": \"string\",
            \"broadcast\": \"string\",
            \"dns_nameservers\": \"string\",
            \"dns_search\": \"string\",
            \"family\": \"string\",
            \"gateway\": \"string\",
            \"mac_address\": \"string\",
            \"mac_address_permanent\": \"string\",
            \"method\": \"string\",
            \"mtu\": \"string\",
            \"netmask\": \"string\",
            \"network\": \"string\",
            \"physical\": {
                \"address\": \"string\",
                \"mac_address\": \"string\",
                \"mac_address_permanent\": \"string\",
                \"mtu\": \"string\",
                \"netmask\": \"string\",
                \"network\": \"string\",
                \"up_and_running\": true/false
            },
            \"routes\": [
                \"string\"
            ],
            \"status\": \"string\",
            \"symmetric_route_rules\": [
                \"string\"
            ],
            \"up_and_running\": true/false
        },
        \"bond1_g\": {
            \"_default\": true/false,
            \"bond_master\": \"string\"        [Required],
            \"virtual_network_tag\": \"string\"        [Required],
            \"address\": \"string\",
            \"auto\": true/false,
            \"bond_downdelay\": \"string\",
            \"bond_fail_over_mac\": \"string\",
            \"bond_primary_reselect\": \"string\",
            \"bond_lacp_rate\": \"string\",
            \"bond_miimon\": \"string\",
            \"bond_mode\": \"string\",
            \"bond_slaves\": \"string\",
            \"bond_updelay\": \"string\",
            \"broadcast\": \"string\",
            \"dns_nameservers\": \"string\",
            \"dns_search\": \"string\",
            \"family\": \"string\",
            \"gateway\": \"string\",
            \"mac_address\": \"string\",
            \"mac_address_permanent\": \"string\",
            \"method\": \"string\",
            \"mtu\": \"string\",
            \"netmask\": \"string\",
            \"network\": \"string\",
            \"physical\": {
                \"address\": \"string\",
                \"mac_address\": \"string\",
                \"mac_address_permanent\": \"string\",
                \"mtu\": \"string\",
                \"netmask\": \"string\",
                \"network\": \"string\",
                \"up_and_running\": true/false
            },
            \"routes\": [
                \"string\"
            ],
            \"status\": \"string\",
            \"symmetric_route_rules\": [
                \"string\"
            ],
            \"up_and_running\": true/false
        },
        \"eth0\": {
            \"_default\": true/false,
            \"bond_master\": \"string\"        [Required],
            \"virtual_network_tag\": \"string\"        [Required],
            \"address\": \"string\",
            \"auto\": true/false,
            \"bond_downdelay\": \"string\",
            \"bond_fail_over_mac\": \"string\",
            \"bond_primary_reselect\": \"string\",
            \"bond_lacp_rate\": \"string\",
            \"bond_miimon\": \"string\",
            \"bond_mode\": \"string\",
            \"bond_slaves\": \"string\",
            \"bond_updelay\": \"string\",
            \"broadcast\": \"string\",
            \"dns_nameservers\": \"string\",
            \"dns_search\": \"string\",
            \"family\": \"string\",
            \"gateway\": \"string\",
            \"mac_address\": \"string\",
            \"mac_address_permanent\": \"string\",
            \"method\": \"string\",
            \"mtu\": \"string\",
            \"netmask\": \"string\",
            \"network\": \"string\",
            \"physical\": {
                \"address\": \"string\",
                \"mac_address\": \"string\",
                \"mac_address_permanent\": \"string\",
                \"mtu\": \"string\",
                \"netmask\": \"string\",
                \"network\": \"string\",
                \"up_and_running\": true/false
            },
            \"routes\": [
                \"string\"
            ],
            \"status\": \"string\",
            \"symmetric_route_rules\": [
                \"string\"
            ],
            \"up_and_running\": true/false
        },
        \"eth1\": {
            \"_default\": true/false,
            \"bond_master\": \"string\"        [Required],
            \"virtual_network_tag\": \"string\"        [Required],
            \"address\": \"string\",
            \"auto\": true/false,
            \"bond_downdelay\": \"string\",
            \"bond_fail_over_mac\": \"string\",
            \"bond_primary_reselect\": \"string\",
            \"bond_lacp_rate\": \"string\",
            \"bond_miimon\": \"string\",
            \"bond_mode\": \"string\",
            \"bond_slaves\": \"string\",
            \"bond_updelay\": \"string\",
            \"broadcast\": \"string\",
            \"dns_nameservers\": \"string\",
            \"dns_search\": \"string\",
            \"family\": \"string\",
            \"gateway\": \"string\",
            \"mac_address\": \"string\",
            \"mac_address_permanent\": \"string\",
            \"method\": \"string\",
            \"mtu\": \"string\",
            \"netmask\": \"string\",
            \"network\": \"string\",
            \"physical\": {
                \"address\": \"string\",
                \"mac_address\": \"string\",
                \"mac_address_permanent\": \"string\",
                \"mtu\": \"string\",
                \"netmask\": \"string\",
                \"network\": \"string\",
                \"up_and_running\": true/false
            },
            \"routes\": [
                \"string\"
            ],
            \"status\": \"string\",
            \"symmetric_route_rules\": [
                \"string\"
            ],
            \"up_and_running\": true/false
        },
        \"eth2\": {
            \"_default\": true/false,
            \"bond_master\": \"string\"        [Required],
            \"virtual_network_tag\": \"string\"        [Required],
            \"address\": \"string\",
            \"auto\": true/false,
            \"bond_downdelay\": \"string\",
            \"bond_fail_over_mac\": \"string\",
            \"bond_primary_reselect\": \"string\",
            \"bond_lacp_rate\": \"string\",
            \"bond_miimon\": \"string\",
            \"bond_mode\": \"string\",
            \"bond_slaves\": \"string\",
            \"bond_updelay\": \"string\",
            \"broadcast\": \"string\",
            \"dns_nameservers\": \"string\",
            \"dns_search\": \"string\",
            \"family\": \"string\",
            \"gateway\": \"string\",
            \"mac_address\": \"string\",
            \"mac_address_permanent\": \"string\",
            \"method\": \"string\",
            \"mtu\": \"string\",
            \"netmask\": \"string\",
            \"network\": \"string\",
            \"physical\": {
                \"address\": \"string\",
                \"mac_address\": \"string\",
                \"mac_address_permanent\": \"string\",
                \"mtu\": \"string\",
                \"netmask\": \"string\",
                \"network\": \"string\",
                \"up_and_running\": true/false
            },
            \"routes\": [
                \"string\"
            ],
            \"status\": \"string\",
            \"symmetric_route_rules\": [
                \"string\"
            ],
            \"up_and_running\": true/false
        },
        \"eth3\": {
            \"_default\": true/false,
            \"bond_master\": \"string\"        [Required],
            \"virtual_network_tag\": \"string\"        [Required],
            \"address\": \"string\",
            \"auto\": true/false,
            \"bond_downdelay\": \"string\",
            \"bond_fail_over_mac\": \"string\",
            \"bond_primary_reselect\": \"string\",
            \"bond_lacp_rate\": \"string\",
            \"bond_miimon\": \"string\",
            \"bond_mode\": \"string\",
            \"bond_slaves\": \"string\",
            \"bond_updelay\": \"string\",
            \"broadcast\": \"string\",
            \"dns_nameservers\": \"string\",
            \"dns_search\": \"string\",
            \"family\": \"string\",
            \"gateway\": \"string\",
            \"mac_address\": \"string\",
            \"mac_address_permanent\": \"string\",
            \"method\": \"string\",
            \"mtu\": \"string\",
            \"netmask\": \"string\",
            \"network\": \"string\",
            \"physical\": {
                \"address\": \"string\",
                \"mac_address\": \"string\",
                \"mac_address_permanent\": \"string\",
                \"mtu\": \"string\",
                \"netmask\": \"string\",
                \"network\": \"string\",
                \"up_and_running\": true/false
            },
            \"routes\": [
                \"string\"
            ],
            \"status\": \"string\",
            \"symmetric_route_rules\": [
                \"string\"
            ],
            \"up_and_running\": true/false
        },
        \"lo\": {
            \"_default\": true/false,
            \"bond_master\": \"string\"        [Required],
            \"virtual_network_tag\": \"string\"        [Required],
            \"address\": \"string\",
            \"auto\": true/false,
            \"bond_downdelay\": \"string\",
            \"bond_fail_over_mac\": \"string\",
            \"bond_primary_reselect\": \"string\",
            \"bond_lacp_rate\": \"string\",
            \"bond_miimon\": \"string\",
            \"bond_mode\": \"string\",
            \"bond_slaves\": \"string\",
            \"bond_updelay\": \"string\",
            \"broadcast\": \"string\",
            \"dns_nameservers\": \"string\",
            \"dns_search\": \"string\",
            \"family\": \"string\",
            \"gateway\": \"string\",
            \"mac_address\": \"string\",
            \"mac_address_permanent\": \"string\",
            \"method\": \"string\",
            \"mtu\": \"string\",
            \"netmask\": \"string\",
            \"network\": \"string\",
            \"physical\": {
                \"address\": \"string\",
                \"mac_address\": \"string\",
                \"mac_address_permanent\": \"string\",
                \"mtu\": \"string\",
                \"netmask\": \"string\",
                \"network\": \"string\",
                \"up_and_running\": true/false
            },
            \"routes\": [
                \"string\"
            ],
            \"status\": \"string\",
            \"symmetric_route_rules\": [
                \"string\"
            ],
            \"up_and_running\": true/false
        }
    }        [Required]
}

--networks
[
    {
        \"access\": \"string\"        [Required],
        \"cidr\": int        [Required],
        \"community\": \"string\"        [Required],
        \"network\": \"string\"        [Required]
    }
]

--addressblocks
[
    {
        \"start\": \"string\"        [Required],
        \"size\": int        [Required]
    }
]



---------------
Command Details
---------------
Usage: sfcli [OPTIONS] COMMAND [ARGS]...

  SolidFire command line interface.

Options:
  -m, --mvip TEXT
    SolidFire MVIP
  -l, --login TEXT
    SolidFire Cluster login
  -p, --password TEXT
    SolidFire cluster password
  --name TEXT
    The connection name for later reference (-n)
  -c, --connectionIndex INTEGER
    The index of the connection you wish to use in connections.csv. You can use this if you have previously stored away a connection.
  -n, --connectionName TEXT
    The name of the connection you wish to use in connections.csv. You can use this if you have previously stored away a connection.
  -j, --json
    To print the full output in json format, use this flag
  -p, --pickle
    To print the full output in a pickled json format, use this flag.
  -d, --depth INTEGER
    To print the output as a tree and specify the depth, use this option.
  -f, --filter_tree TEXT
    To filter the fields that will be displayed in a tree, use this parameter. Supply fields in a comma separated list of keypaths. For example, to filter accounts list, if I wanted only the username and status, I could supply 'accounts.username,accounts.status'.
  --debug [0|1|2|3]
    Set the debug level
  --help
    Show this help and exit.
  ---------------------------------------------------------------
  Statistics Commands
  ---------------------------------------------------------------
    |-----------------------------
    |getcompletestats
    |  Description:
    |    The GetCompleteStats API method is used by SolidFire engineering to troubleshoot new features. The data returned from GetCompleteStats is not documented, changes frequently, and is not guaranteed to be accurate. It is not recommended to ever use GetCompleteStats for collecting performance data or any other management integration with a SolidFire cluster.
    |    The data returned from GetCompleteStats changes frequently, and is not guaranteed to accurately show performance from the system. It is not recommended to ever use GetCompleteStats for collecting performance data or any other management integration with a SolidFire cluster.
    |
    |  Options:
    |-----------------------------
    |gethardwareinfo
    |  Description:
    |    GetHardwareInfo allows you to return hardware information and status for a single node. This generally includes manufacturers, vendors, versions, drives, and other associated hardware identification information.
    |
    |  Options:
    |-----------------------------
    |getrawstats
    |  Description:
    |    The GetRawStats call is used by SolidFire engineering to troubleshoot new features. The data returned from GetRawStats is not documented, it changes frequently, and is not guaranteed to be accurate. It is not recommended to ever use GetRawStats for collecting performance data or any other management integration with a SolidFire cluster.
    |    The data returned from GetRawStats changes frequently, and is not guaranteed to accurately show performance from the system. It is not recommended to ever use GetRawStats for collecting performance data or any other management integration with a SolidFire cluster.
    |
    |  Options:
    |-----------------------------
    |listvolumestatsbyvirtualvolume
    |  Description:
    |    ListVolumeStatsByVirtualVolume enables you to list statistics for volumes, sorted by virtual volumes.
    |
    |  Options:
    |     --virtualvolumeids
    |        A list of virtual volume  IDs for which to retrieve information. If you specify this parameter, the method returns information about only these virtual volumes.
    |-----------------------------
    |listvolumestats
    |  Description:
    |
    |  Options:
    |     --volumeids
    |-----------------------------
    |listdrivestats
    |  Description:
    |    ListDriveStats enables you to retrieve  high-level activity measurements for multiple drives in the cluster. By default, this method returns statistics for all drives in the cluster, and these measurements are cumulative from the addition of the drive to the cluster. Some values this method returns are specific to block drives, and some are specific to metadata drives. For more information on what data each drive type returns, see the response examples for the GetDriveStats method.
    |
    |  Options:
    |     --drives
    |        Optional list of DriveIDs for which to return drive statistics. If you omit this parameter, measurements for all drives are returned.
    |        
  ---------------------------------------------------------------
  Network Commands
  ---------------------------------------------------------------
    |-----------------------------
    |listnodefibrechannelportinfo
    |  Description:
    |    The ListNodeFibreChannelPortInfo is used to return information about the Fibre Channel ports. The API method is intended for use on individual nodes; userid and password is required for access to individual Fibre Channel nodes.
    |
    |  Options:
    |-----------------------------
    |listfibrechannelsessions
    |  Description:
    |    The ListFibreChannelSessions is used to return information about the active Fibre Channel sessions on a cluster.
    |
    |  Options:
    |-----------------------------
    |listfibrechannelportinfo
    |  Description:
    |    The ListFibreChannelPortInfo is used to return information about the Fibre Channel ports. The API method is intended for use on individual nodes; userid and password is required for access to individual Fibre Channel nodes.
    |
    |  Options:
    |-----------------------------
    |listiscsisessions
    |  Description:
    |    ListISCSISessions is used to return iSCSI connection information for volumes in the cluster.
    |
    |  Options:
    |-----------------------------
    |listinterfaces
    |  Description:
    |    The ListNetworkInterfaces API method is used to return information about each network interface on a node. The API method is intended for use on individual nodes. 
    |
    |  Options:
    |        
  ---------------------------------------------------------------
  Service Commands
  ---------------------------------------------------------------
    |-----------------------------
    |list
    |  Description:
    |    List the services in the cluster.
    |
    |  Options:
    |        
  ---------------------------------------------------------------
  Pairing Commands
  ---------------------------------------------------------------
    |-----------------------------
    |completecluster
    |  Description:
    |    The CompleteClusterPairing method is the second step in the cluster pairing process.
    |    Use this method with the encoded key received from the "StartClusterPairing" API method to complete the cluster pairing process.
    |
    |  Options:
    |     --clusterpairingkey
    |        A string of characters that is returned from the "StartClusterPairing" API method.
    |-----------------------------
    |completevolume
    |  Description:
    |    CompleteVolumePairing is used to complete the pairing of two volumes.
    |
    |  Options:
    |     --volumepairingkey
    |        The key returned from the "StartVolumePairing" API method.
    |     --volumeid
    |        The ID of volume on which to complete the pairing process.
    |-----------------------------
    |listclusterpairs
    |  Description:
    |    ListClusterPairs is used to list all of the clusters a cluster is paired with.
    |    This method returns information about active and pending cluster pairings, such as statistics about the current pairing as well as the connectivity and latency (in milliseconds) of the cluster pairing.
    |
    |  Options:
    |-----------------------------
    |removevolumepair
    |  Description:
    |    RemoveVolumePair is used to remove the remote pairing between two volumes.
    |    When the volume pairing information is removed, data is no longer replicated to or from the volume.
    |    This method should be run on both the source and target volumes that are paired together.
    |
    |  Options:
    |     --volumeid
    |        ID of the volume on which to stop the replication process.
    |-----------------------------
    |startvolume
    |  Description:
    |    StartVolumePairing is used to create an encoded key from a volume that is used to pair with another volume.
    |    The key that this method creates is used in the "CompleteVolumePairing" API method to establish a volume pairing.
    |
    |  Options:
    |     --volumeid
    |        The ID of the volume on which to start the pairing process.
    |     --mode
    |        The mode of the volume on which to start the pairing process. The mode can only be set if the volume is the source volume.
    |        Possible values:
    |        Async: (default if no mode parameter specified) Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.
    |        Sync: Source acknowledges write when the data is stored locally and on the remote cluster.
    |        SnapshotsOnly: Only snapshots created on the source cluster will be replicated. Active writes from the source volume will not be replicated.
    |-----------------------------
    |listactivepairedvolumes
    |  Description:
    |    ListActivePairedVolumes is used to list all of the active volumes paired with a volume.
    |    Volumes listed in the return for this method include volumes with active and pending pairings.
    |
    |  Options:
    |-----------------------------
    |modifyvolumepair
    |  Description:
    |    ModifyVolumePair is used to pause or restart replication between a pair of volumes.
    |
    |  Options:
    |     --volumeid
    |        Identification number of the volume to be modified.
    |     --pausedmanual
    |        Valid values that can be entered:
    |        true: to pause volume replication.
    |        false: to restart volume replication.
    |        If no value is specified, no change in replication is performed.
    |     --mode
    |        Volume replication mode.
    |        Possible values:
    |        Async: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.
    |        Sync: The source acknowledges the write when the data is stored locally and on the remote cluster.
    |        SnapshotsOnly: Only snapshots created on the source cluster will be replicated. Active writes from the source volume are not replicated.
    |-----------------------------
    |startcluster
    |  Description:
    |    StartClusterPairing is used to create an encoded key from a cluster that is used to pair with another cluster.
    |    The key created from this API method is used in the "CompleteClusterPairing" API method to establish a cluster pairing.
    |    You can pair a cluster with a maximum of four other SolidFire clusters.
    |
    |  Options:
    |-----------------------------
    |removeclusterpair
    |  Description:
    |    You can use the RemoveClusterPair method to close the open connections between two paired clusters.
    |    Note: Before you remove a cluster pair, you must first remove all volume pairing to the clusters with the "RemoveVolumePair" API method.
    |
    |  Options:
    |     --clusterpairid
    |        Unique identifier used to pair two clusters.
    |        
  ---------------------------------------------------------------
  Test Commands
  ---------------------------------------------------------------
    |-----------------------------
    |list
    |  Description:
    |    The ListTests API method is used to return the tests that are available to run on a node.
    |    Note: This method is available only through the per-node API endpoint 5.0 or later.
    |
    |  Options:
    |-----------------------------
    |ping
    |  Description:
    |    The TestPing API method is used to validate the connection to all nodes in the cluster on both 1G and 10G interfaces using ICMP packets. The test uses the appropriate MTU sizes for each packet based on the MTU settings in the network configuration.
    |    Note: This method is available only through the per-node API endpoint 5.0 or later.
    |
    |  Options:
    |     --attempts
    |        Specifies the number of times the system should repeat the test ping. Default is 5.
    |     --hosts
    |        Specify address or hostnames of devices to ping.
    |     --totaltimeoutsec
    |        Specifies the length of time the ping should wait for a system response before issuing the next ping attempt or ending the process.
    |     --packetsize
    |        Specify the number of bytes to send in the ICMP packet sent to each IP. Number be less than the maximum MTU specified in the network configuration.
    |     --pingtimeoutmsec
    |        Specify the number of milliseconds to wait for each individual ping response. Default is 500ms.
    |-----------------------------
    |connectmvip
    |  Description:
    |    The TestConnectMvip API method is used to test the management connection to the cluster. The test pings the MVIP and executes a simple API method to verify connectivity.
    |    Note: This method is available only through the per-node API endpoint 5.0 or later.
    |
    |  Options:
    |     --mvip
    |        Optionally, use to test the management connection of a different MVIP. This is not needed to test the connection to the target cluster.
    |-----------------------------
    |listutilities
    |  Description:
    |    The ListUtilities API method is used to return the tests that are available to run on a node.
    |    Note: This method is available only through the per-node API endpoint 5.0 or later.
    |
    |  Options:
    |-----------------------------
    |connectensemble
    |  Description:
    |    The TestConnectEnsemble API method is used to verify connectivity with a sepcified database ensemble. By default it uses the ensemble for the cluster the node is associated with. Alternatively you can provide a different ensemble to test connectivity with.
    |    Note: This method is available only through the per-node API endpoint 5.0 or later.
    |
    |  Options:
    |     --ensemble
    |        A comma-separated list of ensemble node CIPs for connectivity testing
    |-----------------------------
    |connectsvip
    |  Description:
    |    The TestConnectSvip API method is used to test the storage connection to the cluster. The test pings the SVIP using ICMP packets and when successful connects as an iSCSI initiator.
    |    Note: This method is available only through the per-node API endpoint 5.0 or later.
    |
    |  Options:
    |     --svip
    |        Optionally, use to test the storage connection of a different SVIP. This is not needed to test the connection to the target cluster.
    |        
  ---------------------------------------------------------------
  VolumeAccessGroup Commands
  ---------------------------------------------------------------
    |-----------------------------
    |removevolumesfrom
    |  Description:
    |    Remove volumes from a volume access group.
    |
    |  Options:
    |     --volumeaccessgroupid
    |        The ID of the volume access group to modify.
    |     --volumes
    |        List of volumes to remove from this volume access group.
    |-----------------------------
    |modify
    |  Description:
    |    Update initiators and add or remove volumes from a volume access group.
    |    A specified initiator or volume that duplicates an existing volume or initiator in a volume access group is left as-is.
    |    If a value is not specified for volumes or initiators, the current list of initiators and volumes are not changed.
    |    
    |    Often, it is easier to use the convenience functions to modify initiators and volumes independently:
    |    
    |    AddInitiatorsToVolumeAccessGroup
    |    RemoveInitiatorsFromVolumeAccessGroup
    |    AddVolumesToVolumeAccessGroup
    |    RemoveVolumesFromVolumeAccessGroup
    |
    |  Options:
    |     --volumeaccessgroupid
    |        The ID of the volume access group to modify.
    |     --virtualnetworkid
    |        The ID of the SolidFire Virtual Network ID to associate the volume access group with.
    |     --virtualnetworktags
    |        The ID of the VLAN Virtual Network Tag to associate the volume access group with.
    |     --name
    |        Name of the volume access group.
    |        It is not required to be unique, but recommended.
    |     --initiators
    |        List of initiators to include in the volume access group.
    |        If unspecified, the access group's configured initiators will not be modified.
    |     --volumes
    |        List of volumes to initially include in the volume access group.
    |        If unspecified, the access group's volumes will not be modified.
    |     --attributes
    |        List of Name/Value pairs in JSON object format.
    |-----------------------------
    |create
    |  Description:
    |    Creates a new volume access group.
    |    The new volume access group must be given a name when it is created.
    |    Entering initiators and volumes are optional when creating a volume access group.
    |    Once the group is created volumes and initiator IQNs can be added.
    |    Any initiator IQN that is successfully added to the volume access group is able to access any volume in the group without CHAP authentication.
    |
    |  Options:
    |     --name
    |        Name of the volume access group.
    |        It is not required to be unique, but recommended.
    |     --initiators
    |        List of initiators to include in the volume access group.
    |        If unspecified, the access group will start out without configured initiators.
    |     --volumes
    |        List of volumes to initially include in the volume access group.
    |        If unspecified, the access group will start without any volumes.
    |     --virtualnetworkid
    |        The ID of the SolidFire Virtual Network ID to associate the volume access group with.
    |     --virtualnetworktags
    |        The ID of the VLAN Virtual Network Tag to associate the volume access group with.
    |     --attributes
    |        List of Name/Value pairs in JSON object format.
    |-----------------------------
    |modifylunassignments
    |  Description:
    |    The ModifytVolumeAccessGroupLunAssignments is used to define custom LUN assignments for specific volumes. Only LUN values set on the lunAssignments parameter will be changed in the volume access group. All other LUN assignments will remain unchanged.
    |    
    |    LUN assignment values must be unique for volumes in a volume access group. An exception will be seen if LUN assignments are duplicated in a volume access group. However, the same LUN values can be used again in different volume access groups.
    |    
    |    Note: Correct LUN values are 0 - 16383. An exception will be seen if an incorrect LUN value is passed. None of the specified LUN assignments will be modified if there is an exception.
    |    
    |    Caution: If a LUN assignment is changed for a volume with active I/O, the I/O could be disrupted. Changes to the server configuration may be required in order to change volume LUN assignments.
    |
    |  Options:
    |     --volumeaccessgroupid
    |        Unique volume access group ID for which the LUN assignments will be modified.
    |     --lunassignments
    |        The volume IDs with new assigned LUN values.
    |-----------------------------
    |list
    |  Description:
    |    ListVolumeAccessGroups is used to return information about the volume access groups that are currently in the system.
    |
    |  Options:
    |     --startvolumeaccessgroupid
    |        The lowest VolumeAccessGroupID to return.
    |        This can be useful for paging.
    |        If unspecified, there is no lower limit (implicitly 0).
    |     --limit
    |        The maximum number of results to return.
    |        This can be useful for paging.
    |-----------------------------
    |addinitiatorsto
    |  Description:
    |    Add initiators to a volume access group.
    |
    |  Options:
    |     --volumeaccessgroupid
    |        The ID of the volume access group to modify.
    |     --initiators
    |        List of initiators to add to the volume access group.
    |-----------------------------
    |getlunassignments
    |  Description:
    |    The GetVolumeAccessGroupLunAssignments is used to return information LUN mappings of a specified volume access group.
    |
    |  Options:
    |     --volumeaccessgroupid
    |        Unique volume access group ID used to return information.
    |-----------------------------
    |addvolumesto
    |  Description:
    |    Add volumes to a volume access group.
    |
    |  Options:
    |     --volumeaccessgroupid
    |        The ID of the volume access group to modify.
    |     --volumes
    |        List of volumes to add to this volume access group.
    |-----------------------------
    |removeinitiatorsfrom
    |  Description:
    |    Remove initiators from a volume access group.
    |
    |  Options:
    |     --volumeaccessgroupid
    |        The ID of the volume access group to modify.
    |     --initiators
    |        List of initiators to remove from the volume access group.
    |-----------------------------
    |getefficiency
    |  Description:
    |    GetVolumeAccessGroupEfficiency is used to retrieve efficiency information about a volume access group. Only the volume access group provided as parameters in this API method is used to compute the capacity.
    |
    |  Options:
    |     --volumeaccessgroupid
    |        Specifies the volume access group for which capacity is computed.
    |-----------------------------
    |delete
    |  Description:
    |    Delete a volume access group from the system.
    |
    |  Options:
    |     --volumeaccessgroupid
    |        The ID of the volume access group to delete.
    |        
  ---------------------------------------------------------------
  Node Commands
  ---------------------------------------------------------------
    |-----------------------------
    |setnetworkconfig
    |  Description:
    |    The "SetNetworkConfig" method is used to set the network configuration for a node. To see the states in which these objects can be modified, see "Network Object for 1G and 10G Interfaces" on page 109 of the Element API. To display the current network settings for a node, run the "GetNetworkConfig" method.
    |    
    |    WARNING! Changing the "bond-mode" on a node can cause a temporary loss of network connectivity. Caution should be taken when using this method.
    |    
    |    Note: This method is available only through the per-node API endpoint 5.0 or later.
    |
    |  Options:
    |     --network
    |        Objects that will be changed for the node network settings.
    |-----------------------------
    |listpending
    |  Description:
    |    Gets the list of pending nodes.
    |    Pending nodes are running and configured to join the cluster, but have not been added via the AddNodes method.
    |
    |  Options:
    |-----------------------------
    |getorigin
    |  Description:
    |    GetOrigin enables you to retrieve the origination certificate for where the node was built.NOTE: The GetOrigin method may return "null" if there is no origination certification.
    |
    |  Options:
    |     --force
    |-----------------------------
    |listpendingactive
    |  Description:
    |    ListPendingActiveNodes returns the list of nodes in the cluster that are currently in the PendingActive state, between the pending and active states. These are nodes that are currently being returned to the factory image.
    |
    |  Options:
    |-----------------------------
    |listall
    |  Description:
    |    ListAllNodes enables you to retrieve a list of active and pending nodes in the cluster.
    |
    |  Options:
    |-----------------------------
    |getpendingoperation
    |  Description:
    |    GetPendingOperation is used to detect an operation on a node that is currently in progress. This method can also be used to report back when an operation has completed.
    |    
    |    Note: This method is available only through the per-node API endpoint 5.0 or later.
    |
    |  Options:
    |-----------------------------
    |liststats
    |  Description:
    |    ListNodeStats is used to return the high-level activity measurements for all nodes in a cluster.
    |
    |  Options:
    |-----------------------------
    |add
    |  Description:
    |    AddNodes is used to add one or more new nodes to the cluster. When a node is not configured and starts up for the first time you are prompted to configure the node. Once a node is configured it is registered as a "pending node" with the cluster.
    |    
    |    Adding a node to a cluster that has been set up for virtual networking will require a sufficient number of virtual storage IP addresses to allocate a virtual IP to the new node. If there are no virtual IP addresses available for the new node, the AddNode operation will not complete successfully. Use the "ModifyVirtualNetwork" method to add more storage IP addresses to your virtual network.
    |    
    |    The software version on each node in a cluster must be compatible. Run the "ListAllNodes" API to see what versions of software are currently running on the cluster nodes. For an explanation of software version compatibility, see "Node Versioning and Compatibility" in the Element API guide.
    |    
    |    Once a node has been added, the drives on the node are made available and can then be added via the "AddDrives" method to increase the storage capacity of the cluster.
    |    
    |    Note: It may take several seconds after adding a new Node for it to start up and register the drives as being available.
    |
    |  Options:
    |     --pendingnodes
    |        List of PendingNodeIDs for the Nodes to be added. You can obtain the list of Pending Nodes via the ListPendingNodes method.
    |-----------------------------
    |setconfig
    |  Description:
    |    The SetConfig API method is used to set all the configuration information for the node. This includes the same information available via calls to SetClusterConfig and SetNetworkConfig in one API method.
    |    
    |    Warning! Changing the 'bond-mode' on a node can cause a temporary loss of network connectivity. Caution should be taken when using this method.
    |    
    |    Note: This method is available only through the per-node API endpoint 5.0 or later.
    |
    |  Options:
    |     --config
    |        Objects that you want changed for the cluster interface settings.
    |-----------------------------
    |getnetworkconfig
    |  Description:
    |    The GetNetworkConfig API method is used to display the network configuration information for a node.
    |    
    |    Note: This method is available only through the per-node API endpoint 5.0 or later.
    |
    |  Options:
    |-----------------------------
    |getstats
    |  Description:
    |    GetNodeStats is used to return the high-level activity measurements for a single node.
    |
    |  Options:
    |     --nodeid
    |        Specifies the node for which statistics are gathered.
    |-----------------------------
    |getconfig
    |  Description:
    |    The GetConfig API method is used to retrieve all the configuration information for the node. This one API method includes the same information available in both "GetClusterConfig" and "GetNetworkConfig" methods.
    |    
    |    Note: This method is available only through the per-node API endpoint 5.0 or later.
    |
    |  Options:
    |-----------------------------
    |remove
    |  Description:
    |    RemoveNodes is used to remove one or more nodes that should no longer participate in the cluster. Before removing a node, all drives it contains must first be removed with "RemoveDrives" method. A node cannot be removed until the RemoveDrives process has completed and all data has been migrated away from the node.
    |    
    |    Once removed, a node registers itself as a pending node and can be added again, or shut down which removes it from the "Pending Node" list.
    |
    |  Options:
    |     --nodes
    |        List of NodeIDs for the nodes to be removed.
    |-----------------------------
    |listactive
    |  Description:
    |    ListActiveNodes returns the list of currently active nodes that are in the cluster.
    |
    |  Options:
    |-----------------------------
    |getbootstrapconfig
    |  Description:
    |    GetBootstrapConfig returns the cluster name and node name from the bootstrap configuration file. This API method should be performed on an individual node before it has been configured into a cluster. The resulting information from this method is used in the Cluster Configuration UI when the cluster is eventually created.
    |
    |  Options:
    |        
  ---------------------------------------------------------------
  ProtocolEndpoints Commands
  ---------------------------------------------------------------
    |-----------------------------
    |list
    |  Description:
    |    Gets protocol endpoints in the system
    |    If protocolEndpointIDs isn't specified all protocol endpoints
    |    are returned. Else the supplied protocolEndpointIDs are.
    |
    |  Options:
    |     --protocolendpointids
    |        
  ---------------------------------------------------------------
  LoginSession Commands
  ---------------------------------------------------------------
    |-----------------------------
    |getremotelogginghosts
    |  Description:
    |    GetRemoteLoggingHosts is used to retrieve the current list of log servers.
    |
    |  Options:
    |-----------------------------
    |setremotelogginghosts
    |  Description:
    |    RemoteLoggingHosts is used to configure remote logging from the nodes in the storage cluster to a centralized log server or servers. Remote logging is performed over TCP using the default port 514. This API does not add to the existing logging hosts. Rather, it replaces what currently exists with new values specified by this API method. You can use the GetRemoteLoggingHosts to determine what the current logging hosts are and then use the SetRemoteLoggingHosts to set the desired list of current and new logging hosts.
    |
    |  Options:
    |     --remotehosts
    |        List of hosts to send log messages to.
    |-----------------------------
    |setinfo
    |  Description:
    |    SetLoginSessionInfo is used to set the period of time a log in authentication is valid. After the log in period elapses without activity on the system the authentication will expire. New log in credentials will be required for continued access to the cluster once the timeout period has elapsed.
    |
    |  Options:
    |     --timeout
    |        Cluster authentication expiration period. Formatted in HH:mm:ss. For example: 01:30:00, 00:90:00, and 00:00:5400 can all be used to equal a 90 minute timeout period. Default is 30 minutes.
    |-----------------------------
    |getinfo
    |  Description:
    |    GetLoginSessionInfo is used to return the period of time a log in authentication is valid for both log in shells and the TUI.
    |
    |  Options:
    |        
  ---------------------------------------------------------------
  Volume Commands
  ---------------------------------------------------------------
    |-----------------------------
    |getefficiency
    |  Description:
    |    GetVolumeEfficiency is used to retrieve information about a volume.
    |    Only the volume given as a parameter in this API method is used to compute the capacity.
    |
    |  Options:
    |     --volumeid
    |        Specifies the volume for which capacity is computed.
    |-----------------------------
    |liststatsbyaccount
    |  Description:
    |    ListVolumeStatsByAccount returns high-level activity measurements for every account.
    |    Values are summed from all the volumes owned by the account.
    |
    |  Options:
    |-----------------------------
    |startbulkwrite
    |  Description:
    |    StartBulkVolumeWrite allows you to initialize a bulk volume write session on a specified volume.
    |    Only two bulk volume processes can run simultaneously on a volume.
    |    When the session is initialized, data can be written to a SolidFire storage volume from an external backup source.
    |    The external data is accessed by a web server running on a SolidFire node.
    |    Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system.
    |
    |  Options:
    |     --volumeid
    |        ID of the volume to be written to.
    |     --format
    |        The format of the volume data. Can be either:
    |        uncompressed: every byte of the volume is returned without any compression.
    |        native: opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write
    |     --script
    |        Executable name of a script.
    |        If no script name is given then the key and URL are necessary to access SolidFire nodes.
    |        The script runs on the primary node and the key and URL is returned to the script so the local web server can be contacted.
    |     --scriptparameters
    |        JSON parameters to pass to the script.
    |     --attributes
    |        JSON attributes for the bulk volume job.
    |-----------------------------
    |updatebulkstatus
    |  Description:
    |    You can use UpdateBulkVolumeStatus in a script to return to the SolidFire system the status of a bulk volume job that you have started with the "StartBulkVolumeRead" or "StartBulkVolumeWrite" methods.
    |
    |  Options:
    |     --key
    |        The key assigned during initialization of a "StartBulkVolumeRead" or "StartBulkVolumeWrite" session.
    |     --status
    |        The SolidFire system sets the status of the given bulk volume job.
    |        Possible values:
    |        running: jobs that are still active.
    |        complete: jobs that are done. failed - jobs that have failed.
    |        failed: jobs that have failed.
    |     --percentcomplete
    |        The completed progress of the bulk volume job as a percentage.
    |     --message
    |        Returns the status of the bulk volume job when the job has completed.
    |     --attributes
    |        JSON attributes  updates what is on the bulk volume job.
    |-----------------------------
    |startbulkread
    |  Description:
    |    StartBulkVolumeRead allows you to initialize a bulk volume read session on a specified volume.
    |    Only two bulk volume processes can run simultaneously on a volume.
    |    When you initialize the session, data is read from a SolidFire storage volume for the purposes of storing the data on an external backup source.
    |    The external data is accessed by a web server running on a SolidFire node.
    |    Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system.
    |    
    |    At the start of a bulk volume read operation, a snapshot of the volume is made and the snapshot is deleted when the read has completed.
    |    You can also read a snapshot of the volume by entering the ID of the snapshot as a parameter.
    |    Reading a previous snapshot does not create a new snapshot of the volume, nor does the previous snapshot be deleted when the read completes.
    |    
    |    Note: This process creates a new snapshot if the ID of an existing snapshot is not provided.
    |    Snapshots can be created if cluster fullness is at stage 2 or 3.
    |    Snapshots are not created when cluster fullness is at stage 4 or 5.
    |
    |  Options:
    |     --volumeid
    |        ID of the volume to be read.
    |     --format
    |        The format of the volume data. Can be either:
    |        uncompressed: every byte of the volume is returned without any compression.
    |        native: opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write.
    |     --snapshotid
    |        ID of a previously created snapshot used for bulk volume reads.
    |        If no ID is entered, a snapshot of the current active volume image is made.
    |     --script
    |        Executable name of a script.
    |        If no script name is given then the key and URL is necessary to access SolidFire nodes.
    |        The script is run on the primary node and the key and URL is returned to the script so the local web server can be contacted.
    |     --scriptparameters
    |        JSON parameters to pass to the script.
    |     --attributes
    |        JSON attributes for the bulk volume job.
    |-----------------------------
    |listdeleted
    |  Description:
    |    ListDeletedVolumes is used to return the entire list of volumes that have been marked for deletion and is purged from the system.
    |
    |  Options:
    |-----------------------------
    |purgedeleted
    |  Description:
    |    PurgeDeletedVolume immediately and permanently purges a volume which has been deleted.
    |    A volume must be deleted using DeleteVolume before it can be purged.
    |    Volumes are purged automatically after a period of time, so usage of this method is not typically required.
    |
    |  Options:
    |     --volumeid
    |        The ID of the volume to purge.
    |-----------------------------
    |liststatsby
    |  Description:
    |    ListVolumeStatsByVolume returns high-level activity measurements for every volume, by volume.
    |    Values are cumulative from the creation of the volume.
    |
    |  Options:
    |-----------------------------
    |create
    |  Description:
    |    CreateVolume is used to create a new (empty) volume on the cluster.
    |    When the volume is created successfully it is available for connection via iSCSI.
    |
    |  Options:
    |     --name
    |        Name of the volume.
    |        Not required to be unique, but it is recommended.
    |        May be 1 to 64 characters in length.
    |     --accountid
    |        AccountID for the owner of this volume.
    |     --totalsize
    |        Total size of the volume, in bytes. Size is rounded up to the nearest 1MB size.
    |     --enable512e
    |        Should the volume provides 512-byte sector emulation?
    |     --qos
    |        Initial quality of service settings for this volume.
    |        
    |        Volumes created without specified QoS values are created with the default values for QoS.
    |        Default values for a volume can be found by running the GetDefaultQoS method.
    |     --attributes
    |        List of Name/Value pairs in JSON object format.
    |-----------------------------
    |cancelclone
    |  Description:
    |    Cancels a currently running clone operation. This method does not return anything.
    |
    |  Options:
    |     --cloneid
    |-----------------------------
    |getdefaultqos
    |  Description:
    |    GetDefaultQoS is used to retrieve the default QoS values that are set for a volume if QoS is not supplied.
    |
    |  Options:
    |-----------------------------
    |getasyncresult
    |  Description:
    |    Used to retrieve the result of asynchronous method calls.
    |    Some method calls are long running and do not complete when the initial response is sent.
    |    To obtain the result of the method call, polling with GetAsyncResult is required.
    |    
    |    GetAsyncResult returns the overall status of the operation (in progress, completed, or error) in a standard fashion,
    |    but the actual data returned for the operation depends on the original method call and the return data is documented with each method.
    |    
    |    The result for a completed asynchronous method call can only be retrieved once.
    |    Once the final result has been returned, later attempts returns an error.
    |
    |  Options:
    |     --asynchandle
    |        A value that was returned from the original asynchronous method call.
    |-----------------------------
    |listasyncresults
    |  Description:
    |    You can use ListAsyncResults to list the results of all currently running and completed asynchronous methods on the system. Querying asynchronous results with ListAsyncResults does not cause completed asyncHandles to expire; you can use GetAsyncResult to query any of the asyncHandles returned by ListAsyncResults.
    |
    |  Options:
    |     --asyncresulttypes
    |        An optional list of types of results. You can use this list to restrict the results to only these types of operations. Possible values:BulkVolume: Copy operations between volumes, such as backups or restores.Clone: Volume cloning operations.DriveRemoval: Operations involving the system copying data from a drive in preparation to remove it from the cluster.RtfiPendingNode: Operations involving the system installing compatible software on a node before adding it to the cluster.
    |-----------------------------
    |liststatsbyaccessgroup
    |  Description:
    |    ListVolumeStatsByVolumeAccessGroup is used to get total activity measurements for all of the volumes that are a member of the specified volume access group(s).
    |
    |  Options:
    |     --volumeaccessgroups
    |        An array of VolumeAccessGroupIDs for which volume activity is returned.
    |        If no VolumeAccessGroupID is specified, stats for all volume access groups is returned.
    |-----------------------------
    |listbulkjobs
    |  Description:
    |    ListBulkVolumeJobs is used to return information about each bulk volume read or write operation that is occurring in the system.
    |
    |  Options:
    |-----------------------------
    |clone
    |  Description:
    |    CloneVolume is used to create a copy of the volume.
    |    This method is asynchronous and may take a variable amount of time to complete.
    |    The cloning process begins immediately when the CloneVolume request is made and is representative of the state of the volume when the API method is issued.
    |    GetAsyncResults can be used to determine when the cloning process is complete and the new volume is available for connections.
    |    ListSyncJobs can be used to see the progress of creating the clone.
    |    
    |    Note: The initial attributes and quality of service settings for the volume are inherited from the volume being cloned.
    |    If different settings are required, they can be changed via ModifyVolume.
    |    
    |    Note: Cloned volumes do not inherit volume access group memberships from the source volume.
    |
    |  Options:
    |     --volumeid
    |        The ID of the volume to clone.
    |     --name
    |        The name for the newly-created volume.
    |     --newaccountid
    |        AccountID for the owner of the new volume.
    |        If unspecified, the AccountID of the owner of the volume being cloned is used.
    |     --newsize
    |        New size of the volume, in bytes.
    |        May be greater or less than the size of the volume being cloned.
    |        If unspecified, the clone's volume size will be the same as the source volume.
    |        Size is rounded up to the nearest 1 MiB.
    |     --access
    |        Access settings for the new volume.
    |        readOnly: Only read operations are allowed.
    |        readWrite: Reads and writes are allowed.
    |        locked: No reads or writes are allowed.
    |        replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.
    |        
    |        If unspecified, the access settings of the clone will be the same as the source.
    |     --snapshotid
    |        ID of the snapshot to use as the source of the clone.
    |        If unspecified, the clone will be created with a snapshot of the active volume.
    |     --attributes
    |        List of Name/Value pairs in JSON object format.
    |-----------------------------
    |modify
    |  Description:
    |    ModifyVolume is used to modify settings on an existing volume.
    |    Modifications can be made to one volume at a time and changes take place immediately.
    |    If an optional parameter is left unspecified, the value will not be changed.
    |    
    |    Extending the size of a volume that is being replicated should be done in an order.
    |    The target (Replication Target) volume should first be increased in size, then the source (Read/Write) volume can be resized.
    |    It is recommended that both the target and the source volumes be the same size.
    |    
    |    Note: If you change access status to locked or target all existing iSCSI connections are terminated.
    |
    |  Options:
    |     --volumeid
    |        VolumeID for the volume to be modified.
    |     --accountid
    |        AccountID to which the volume is reassigned.
    |        If none is specified, the previous account name is used.
    |     --access
    |        Access allowed for the volume.
    |        readOnly: Only read operations are allowed.
    |        readWrite: Reads and writes are allowed.
    |        locked: No reads or writes are allowed.
    |        replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.
    |        
    |        If unspecified, the access settings of the clone will be the same as the source.
    |     --qos
    |        New quality of service settings for this volume.
    |     --totalsize
    |        New size of the volume in bytes.
    |        Size is rounded up to the nearest 1MiB size.
    |        This parameter can only be used to *increase* the size of a volume.
    |     --attributes
    |        List of Name/Value pairs in JSON object format.
    |-----------------------------
    |restoredeleted
    |  Description:
    |    RestoreDeletedVolume marks a deleted volume as active again.
    |    This action makes the volume immediately available for iSCSI connection.
    |
    |  Options:
    |     --volumeid
    |        VolumeID for the deleted volume to restore.
    |-----------------------------
    |copy
    |  Description:
    |    Copies one volume to another.
    |
    |  Options:
    |     --volumeid
    |        Source volume to copy.
    |     --dstvolumeid
    |        Destination volume for the copy.
    |     --snapshotid
    |        Snapshot ID of the source volume to create the copy from.
    |-----------------------------
    |listactive
    |  Description:
    |    ListActiveVolumes is used to return the list of active volumes currently in the system.
    |    The list of volumes is returned sorted in VolumeID order and can be returned in multiple parts (pages).
    |
    |  Options:
    |     --startvolumeid
    |        The ID of the first volume to list.
    |        This can be useful for paging results.
    |        By default, this starts at the lowest VolumeID.
    |     --limit
    |        The maximum number of volumes to return from the API.
    |-----------------------------
    |list
    |  Description:
    |    The ListVolumes method is used to return a list of volumes that are in a cluster.
    |    You can specify the volumes you want to return in the list by using the available parameters.
    |
    |  Options:
    |     --startvolumeid
    |        The ID of the first volume to list.
    |        This can be useful for paging results.
    |        By default, this starts at the lowest VolumeID.
    |     --limit
    |        The maximum number of volumes to return from the API.
    |     --volumestatus
    |        If specified, filter to only volumes with the provided status.
    |        By default, list all volumes.
    |     --accounts
    |        If specified, only fetch volumes which belong to the provided accounts.
    |        By default, list volumes for all accounts.
    |     --ispaired
    |        If specified, only fetch volumes which are paired (if true) or non-paired (if false).
    |        By default, list all volumes regardless of their pairing status.
    |     --volumeids
    |        If specified, only fetch volumes specified in this list.
    |        This option cannot be specified if startVolumeID, limit, or accounts option is specified.
    |-----------------------------
    |clonemultiple
    |  Description:
    |    CloneMultipleVolumes is used to create a clone of a group of specified volumes. A consistent set of characteristics can be assigned to a group of multiple volume when they are cloned together.
    |    If groupSnapshotID is going to be used to clone the volumes in a group snapshot, the group snapshot must be created first using the CreateGroupSnapshot API method or the SolidFire Element WebUI. Using groupSnapshotID is optional when cloning multiple volumes.
    |    
    |    Note: Cloning multiple volumes is allowed if cluster fullness is at stage 2 or 3. Clones are not created when cluster fullness is at stage 4 or 5.
    |
    |  Options:
    |     --volumes
    |        Array of Unique ID for each volume to include in the clone with optional parameters. If optional parameters are not specified, the values will be inherited from the source volumes.
    |     --access
    |        New default access method for the new volumes if not overridden by information passed in the volumes array.
    |        readOnly: Only read operations are allowed.
    |        readWrite: Reads and writes are allowed.
    |        locked: No reads or writes are allowed.
    |        replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.
    |        
    |        If unspecified, the access settings of the clone will be the same as the source.
    |     --groupsnapshotid
    |        ID of the group snapshot to use as a basis for the clone.
    |     --newaccountid
    |        New account ID for the volumes if not overridden by information passed in the volumes array.
    |-----------------------------
    |setdefaultqos
    |  Description:
    |    SetDefaultQoS enables you to configure the default Quality of Service (QoS) values (measured in inputs and outputs per second, or IOPS) for all volumes not yet created.
    |
    |  Options:
    |     --miniops
    |        The minimum number of sustained IOPS that are provided by the cluster to a volume.
    |     --maxiops
    |        The maximum number of sustained IOPS that are provided by the cluster to a volume.
    |     --burstiops
    |        The maximum number of IOPS allowed in a short burst scenario.
    |-----------------------------
    |getstats
    |  Description:
    |    GetVolumeStats is used to retrieve high-level activity measurements for a single volume.
    |    Values are cumulative from the creation of the volume.
    |
    |  Options:
    |     --volumeid
    |        Specifies the volume for which statistics is gathered.
    |-----------------------------
    |listforaccount
    |  Description:
    |    ListVolumesForAccount returns the list of active AND (pending) deleted volumes for an account.
    |
    |  Options:
    |     --accountid
    |        The ID of the account to list the volumes for.
    |     --startvolumeid
    |        The ID of the first volume to list.
    |        This can be useful for paging results.
    |        By default, this starts at the lowest VolumeID.
    |     --limit
    |        The maximum number of volumes to return from the API.
    |-----------------------------
    |getcount
    |  Description:
    |    GetVolumeCount enables you to retrieve the number of volumes currently in the system.
    |
    |  Options:
    |-----------------------------
    |cancelgroupclone
    |  Description:
    |    CancelGroupClone enables you to stop an ongoing CloneMultipleVolumes process for a group of clones. When you cancel a group clone operation, the system completes and removes the operation's associated asyncHandle. This method does not return anything.
    |
    |  Options:
    |     --groupcloneid
    |        cloneID for the ongoing clone process.
    |-----------------------------
    |delete
    |  Description:
    |    DeleteVolume marks an active volume for deletion.
    |    It is purged (permanently deleted) after the cleanup interval elapses.
    |    After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state.
    |    It is not returned in target discovery requests.
    |    
    |    Any snapshots of a volume that has been marked to delete are not affected.
    |    Snapshots are kept until the volume is purged from the system.
    |    
    |    If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.
    |    
    |    If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state.
    |    The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume.
    |    Until the deleted volume is purged, it can be restored and data transfers resumes.
    |    If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed.
    |    The purged volume becomes permanently unavailable.
    |
    |  Options:
    |     --volumeid
    |        The ID of the volume to delete.
    |        
  ---------------------------------------------------------------
  Sensors Commands
  ---------------------------------------------------------------
    |-----------------------------
    |getipmiinfo
    |  Description:
    |    GetIpmiInfo allows you to display a detailed reporting of sensors (objects) for node fans, intake and exhaust temperatures, and power supplies  that are monitored by . 
    |
    |  Options:
    |     --force
    |-----------------------------
    |getipmiconfig
    |  Description:
    |    GetIpmiConfig enables you to retrieve hardware sensor information from sensors that are in your node.
    |
    |  Options:
    |     --chassistype
    |        Used to display information for each node chassis type. Valid values:all - returns sensor information for each chassis type. {chassis type} - returns sensor information for a specified chassis type.
    |     --force
    |        
  ---------------------------------------------------------------
  Restart Commands
  ---------------------------------------------------------------
    |-----------------------------
    |services
    |  Description:
    |    The RestartServices API method is used to restart the  Element services on a node.Caution: This method causes temporary node services interruption. Exercise caution when using this method.
    |
    |  Options:
    |     --force
    |        The "force" parameter must be included on this method to successfully restart services on a node.   
    |     --service
    |        Service name to be restarted.
    |     --action
    |        Action to perform on the service (start, stop, restart).
    |-----------------------------
    |networking
    |  Description:
    |    The RestartNetworking API method is used to restart the networking services on a node.WARNING! This method restarts all networking services on a node, causing temporary loss of networking connectivity. Exercise caution when using this method.
    |
    |  Options:
    |     --force
    |        The "force" parameter must be included on this method to successfully restart the networking.
    |-----------------------------
    |resetnode
    |  Description:
    |    Allows you to reset a node to the SolidFire factory settings. All data will be deleted from the node when you call this method. A node participating in a cluster cannot be reset.
    |
    |  Options:
    |     --build
    |        Used to specify the URL to a remote Element software image to which the node will be reset.
    |     --force
    |        The force parameter must be included in order to successfully reset the node.
    |     --option
    |        Used to enter specifications for running the reset operation.
    |-----------------------------
    |shutdown
    |  Description:
    |    The Shutdown API method enables you to restart or shutdown a node that has not yet been added to a cluster. To use this method, login in to the MIP for the pending node and enter the "shutdown" method with either the "restart" or "halt" options in the following table.
    |
    |  Options:
    |     --nodes
    |        List of NodeIDs for the nodes to be shutdown.
    |     --option
    |        Action to take for the node shutdown:restart: Restarts the node.halt: Performs full power-off of the node.
    |        
  ---------------------------------------------------------------
  VirtualNetwork Commands
  ---------------------------------------------------------------
    |-----------------------------
    |modify
    |  Description:
    |    ModifyVirtualNetwork is used to change various attributes of a VirtualNetwork object. This method can be used to add or remove address blocks, change the netmask IP, or modify the name or description of the virtual network.
    |    
    |    Note: This method requires either the VirtualNetworkID or the VirtualNetworkTag as a parameter, but not both.
    |
    |  Options:
    |     --virtualnetworkid
    |        Unique identifier of the virtual network to modify. This is the virtual network ID assigned by the SolidFire cluster.
    |     --virtualnetworktag
    |        Network Tag that identifies the virtual network to modify.
    |     --name
    |        New name for the virtual network.
    |     --addressblocks
    |        New addressBlock to set for this Virtual Network object. This may contain new address blocks to add to the existing object or it may omit unused address blocks that need to be removed. Alternatively, existing address blocks may be extended or reduced in size. The size of the starting addressBlocks for a Virtual Network object can only be increased, and can never be decreased.
    |        Attributes for this parameter are:
    |        start: start of the IP address range. (String)
    |        size: numbre of IP addresses to include in the block. (Integer)
    |     --netmask
    |        New netmask for this virtual network.
    |     --svip
    |        The storage virtual IP address for this virtual network. The svip for Virtual Network cannot be changed. A new Virtual Network must be created in order to use a different svip address.
    |     --gateway
    |        
    |     --namespace
    |        
    |     --attributes
    |        A new list of Name/Value pairs in JSON object format.
    |-----------------------------
    |add
    |  Description:
    |    AddVirtualNetwork is used to add a new virtual network to a cluster configuration. When a virtual network is added, an interface for each node is created and each will require a virtual network IP address. The number of IP addresses specified as a parameter for this API method must be equal to or greater than the number of nodes in the cluster. Virtual network addresses are bulk provisioned by SolidFire and assigned to individual nodes automatically. Virtual network addresses do not need to be assigned to nodes manually.
    |    
    |    Note: The AddVirtualNetwork method is used only to create a new virtual network. If you want to make changes to a virtual network, please use the ModifyVirtualNetwork method.
    |
    |  Options:
    |     --virtualnetworktag
    |        A unique virtual network (VLAN) tag. Supported values are 1 to 4095 (the number zero (0) is not supported).
    |     --name
    |        User defined name for the new virtual network.
    |     --addressblocks
    |        Unique Range of IP addresses to include in the virtual network.
    |        Attributes for this parameter are:
    |        start: start of the IP address range. (String)
    |        size: numbre of IP addresses to include in the block. (Integer)
    |     --netmask
    |        Unique netmask for the virtual network being created.
    |     --svip
    |        Unique storage IP address for the virtual network being created.
    |     --gateway
    |        
    |     --namespace
    |        
    |     --attributes
    |        List of Name/Value pairs in JSON object format.
    |-----------------------------
    |list
    |  Description:
    |    ListVirtualNetworks is used to get a list of all the configured virtual networks for the cluster. This method can be used to verify the virtual network settings in the cluster.
    |    
    |    This method does not require any parameters to be passed. But, one or more VirtualNetworkIDs or VirtualNetworkTags can be passed in order to filter the results.
    |
    |  Options:
    |     --virtualnetworkid
    |        Network ID to filter the list for a single virtual network
    |     --virtualnetworktag
    |        Network Tag to filter the list for a single virtual network
    |     --virtualnetworkids
    |        NetworkIDs to include in the list.
    |     --virtualnetworktags
    |        Network Tags to include in the list.
    |-----------------------------
    |remove
    |  Description:
    |    RemoveVirtualNetwork is used to remove a previously added virtual network.
    |    
    |    Note: This method requires either the VirtualNetworkID of the VirtualNetworkTag as a parameter, but not both.
    |
    |  Options:
    |     --virtualnetworkid
    |        Network ID that identifies the virtual network to remove.
    |     --virtualnetworktag
    |        Network Tag that identifies the virtual network to remove.
    |        
  ---------------------------------------------------------------
  Account Commands
  ---------------------------------------------------------------
    |-----------------------------
    |list
    |  Description:
    |    Returns the entire list of accounts, with optional paging support.
    |
    |  Options:
    |     --startaccountid
    |        Starting AccountID to return.
    |        If no Account exists with this AccountID,
    |        the next Account by AccountID order is used as the start of the list.
    |        To page through the list, pass the AccountID of the last Account in the previous response + 1
    |     --limit
    |        Maximum number of AccountInfo objects to return.
    |-----------------------------
    |getefficiency
    |  Description:
    |    GetAccountEfficiency is used to retrieve information about a volume account. Only the account given as a parameter in this API method is used to compute the capacity.
    |
    |  Options:
    |     --accountid
    |        Specifies the volume account for which capacity is computed.
    |-----------------------------
    |modify
    |  Description:
    |    Used to modify an existing account.
    |    When locking an account, any existing connections from that account are immediately terminated.
    |    When changing CHAP settings, any existing connections continue to be active,
    |    and the new CHAP values are only used on subsequent connection or reconnection.
    |
    |  Options:
    |     --accountid
    |        AccountID for the account to modify.
    |     --username
    |        Change the username of the account to this value.
    |     --status
    |        Status of the account.
    |     --initiatorsecret
    |        CHAP secret to use for the initiator.
    |        Should be 12-16 characters long and impenetrable.
    |     --targetsecret
    |        CHAP secret to use for the target (mutual CHAP authentication).
    |        Should be 12-16 characters long and impenetrable.
    |     --attributes
    |        List of Name/Value pairs in JSON object format.
    |-----------------------------
    |remove
    |  Description:
    |    Used to remove an existing account.
    |    All Volumes must be deleted and purged on the account before it can be removed.
    |    If volumes on the account are still pending deletion, RemoveAccount cannot be used until DeleteVolume to delete and purge the volumes.
    |
    |  Options:
    |     --accountid
    |        AccountID for the account to remove.
    |-----------------------------
    |getbyname
    |  Description:
    |    Returns details about an account, given its Username.
    |
    |  Options:
    |     --username
    |        Username for the account.
    |-----------------------------
    |add
    |  Description:
    |    Used to add a new account to the system.
    |    New volumes can be created under the new account.
    |    The CHAP settings specified for the account applies to all volumes owned by the account.
    |
    |  Options:
    |     --username
    |        Unique username for this account.
    |        (May be 1 to 64 characters in length).
    |     --initiatorsecret
    |        CHAP secret to use for the initiator.
    |        Should be 12-16 characters long and impenetrable.
    |        The CHAP initiator secrets must be unique and cannot be the same as the target CHAP secret.
    |        
    |        If not specified, a random secret is created.
    |     --targetsecret
    |        CHAP secret to use for the target (mutual CHAP authentication).
    |        Should be 12-16 characters long and impenetrable.
    |        The CHAP target secrets must be unique and cannot be the same as the initiator CHAP secret.
    |        
    |        If not specified, a random secret is created.
    |     --attributes
    |        List of Name/Value pairs in JSON object format.
    |-----------------------------
    |getbyid
    |  Description:
    |    Returns details about an account, given its AccountID.
    |
    |  Options:
    |     --accountid
    |        Specifies the account for which details are gathered.
    |        
  ---------------------------------------------------------------
  Drive Commands
  ---------------------------------------------------------------
    |-----------------------------
    |reset
    |  Description:
    |    ResetDrives is used to pro-actively initialize drives and remove all data currently residing on the drive. The drive can then be reused in an existing node or used in an upgraded SolidFire node. This method requires the force=true parameter to be included in the method call.
    |    
    |    Note: This method is available only through the per-node API endpoint 5.0 or later.
    |
    |  Options:
    |     --drives
    |        List of device names (not driveIDs) to reset.
    |     --force
    |        The "force" parameter must be included on this method to successfully reset a drive.
    |-----------------------------
    |secureerase
    |  Description:
    |    SecureEraseDrives is used to remove any residual data from drives that have a status of "available." For example, when replacing a drive at its end-of-life that contained sensitive data.
    |    It uses a Security Erase Unit command to write a predetermined pattern to the drive and resets the encryption key on the drive. The method may take up to two minutes to complete, so it is an asynchronous method.
    |    The GetAsyncResult method can be used to check on the status of the secure erase operation.
    |    
    |    Use the "ListDrives" method to obtain the driveIDs for the drives you want to secure erase.
    |
    |  Options:
    |     --drives
    |        List of driveIDs to secure erase.
    |-----------------------------
    |list
    |  Description:
    |    ListDrives allows you to retrieve the list of the drives that exist in the cluster's active nodes.
    |    This method returns drives that have been added as volume metadata or block drives as well as drives that have not been added and are available.
    |
    |  Options:
    |-----------------------------
    |remove
    |  Description:
    |    You can use RemoveDrives to proactively remove drives that are part of the cluster.
    |    You may want to use this method when reducing cluster capacity or preparing to replace drives nearing the end of their service life.
    |    Any data on the drives is removed and migrated to other drives in the cluster before the drive is removed from the cluster. This is an asynchronous method.
    |    Depending on the total capacity of the drives being removed, it may take several minutes to migrate all of the data.
    |    Use the "GetAsyncResult" method to check the status of the remove operation.
    |    
    |    When removing multiple drives, use a single "RemoveDrives" method call rather than multiple individual methods with a single drive each.
    |    This reduces the amount of data balancing that must occur to even stabilize the storage load on the cluster.
    |    
    |    You can also remove drives with a "failed" status using "RemoveDrives".
    |    When you remove a drive with a "failed" status it is not returned to an "available" or "active" status.
    |    The drive is unavailable for use in the cluster.
    |    
    |    Use the "ListDrives" method to obtain the driveIDs for the drives you want to remove.
    |
    |  Options:
    |     --drives
    |        List of driveIDs to remove from the cluster.
    |-----------------------------
    |gethardwareinfo
    |  Description:
    |    GetDriveHardwareInfo returns all the hardware info for the given drive. This generally includes manufacturers, vendors, versions, and other associated hardware identification information.
    |
    |  Options:
    |     --driveid
    |        DriveID for the drive information requested. DriveIDs can be obtained via the "ListDrives" method.
    |-----------------------------
    |add
    |  Description:
    |    AddDrives is used to add one or more available drives to the cluster enabling the drives to host a portion of the cluster's data.
    |    When you add a node to the cluster or install new drives in an existing node, the new drives are marked as "available" and must be added via AddDrives before they can be utilized.
    |    Use the "ListDrives" method to display drives that are "available" to be added.
    |    When you add multiple drives, it is more efficient to add them in a single "AddDrives" method call rather than multiple individual methods with a single drive each.
    |    This reduces the amount of data balancing that must occur to stabilize the storage load on the cluster.
    |    
    |    When you add a drive, the system automatically determines the "type" of drive it should be.
    |    
    |    The method returns immediately. However, it may take some time for the data in the cluster to be rebalanced using the newly added drives.
    |    As the new drive(s) are syncing on the system, you can use the "ListSyncJobs" method to see how the drive(s) are being rebalanced and the progress of adding the new drive.
    |
    |  Options:
    |     --drives
    |        List of drives to add to the cluster.
    |-----------------------------
    |getstats
    |  Description:
    |    GetDriveStats return high-level activity measurements for a single drive. Values are cumulative from the addition of the drive to the cluster. Some values are specific to Block Drives. Statistical data may not be returned for both block and metadata drives when running this method.
    |    For more information on which drive type returns which data, see Response Example (Block Drive) and Response Example (Volume Metadata Drive) in the SolidFire API guide.
    |
    |  Options:
    |     --driveid
    |        Specifies the drive for which statistics are gathered.
    |-----------------------------
    |getconfig
    |  Description:
    |    GetDriveConfig is used to display drive information for expected slice and block drive counts as well as the number of slices and block drives that are currently connected to the node.
    |    
    |    Note: This method is available only through the per-node API endpoint 5.0 or later.
    |
    |  Options:
    |-----------------------------
    |test
    |  Description:
    |    The TestDrives API method is used to run a hardware validation on all the drives on the node. Hardware failures on the drives are detected if present and they are reported in the results of the validation tests.
    |    
    |    Note: This test takes approximately 10 minutes.
    |    
    |    Note: This method is available only through the per-node API endpoint 5.0 or later.
    |
    |  Options:
    |     --minutes
    |        The number of minutes to run the test can be specified.
    |-----------------------------
    |listhardware
    |  Description:
    |    ListDriveHardware returns all the drives connected to a node. Use this method on the cluster to return drive hardware information for all the drives on all nodes.
    |
    |  Options:
    |     --force
    |        To run this command, the force parameter must be set to true.
    |        
  ---------------------------------------------------------------
  Snapshot Commands
  ---------------------------------------------------------------
    |-----------------------------
    |listgroup
    |  Description:
    |    ListGroupSnapshots is used to return information about all group snapshots that have been created.
    |
    |  Options:
    |     --volumeid
    |        An array of unique volume IDs to query.
    |        If this parameter is not specified, all group snapshots on the cluster will be included.
    |-----------------------------
    |modifygroup
    |  Description:
    |    ModifyGroupSnapshot is used to change the attributes currently assigned to a group snapshot.
    |
    |  Options:
    |     --groupsnapshotid
    |        ID of the snapshot.
    |     --expirationtime
    |        Use to set the time when the snapshot should be removed.
    |     --enableremotereplication
    |        Use to enable the snapshot created to be replicated to a remote SolidFire cluster.
    |        Possible values:
    |        true: the snapshot will be replicated to remote storage.
    |        false: Default. No replication.
    |-----------------------------
    |modify
    |  Description:
    |    ModifySnapshot is used to change the attributes currently assigned to a snapshot.
    |    Use this API method to enable the snapshots created on the Read/Write (source) volume to be remotely replicated to a target SolidFire storage system.
    |
    |  Options:
    |     --snapshotid
    |        ID of the snapshot.
    |     --expirationtime
    |        Use to set the time when the snapshot should be removed.
    |     --enableremotereplication
    |        Use to enable the snapshot created to be replicated to a remote SolidFire cluster.
    |        Possible values:
    |        true: the snapshot will be replicated to remote storage.
    |        false: Default. No replication.
    |-----------------------------
    |create
    |  Description:
    |    CreateSnapshot is used to create a point-in-time copy of a volume.
    |    A snapshot can be created from any volume or from an existing snapshot.
    |    
    |    Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3.
    |    Snapshots are not created when cluster fullness is at stage 4 or 5.
    |
    |  Options:
    |     --volumeid
    |        ID of the volume image from which to copy.
    |     --snapshotid
    |        Unique ID of a snapshot from which the new snapshot is made.
    |        The snapshotID passed must be a snapshot on the given volume.
    |        If a SnapshotID is not provided, a snapshot is created from the volume's active branch.
    |     --name
    |        A name for the snapshot.
    |        If no name is provided, the date and time the snapshot was taken is used.
    |     --enableremotereplication
    |        Identifies if snapshot is enabled for remote replication.
    |     --retention
    |        The amount of time the snapshot will be retained. Enter in HH:mm:ss
    |     --attributes
    |        List of Name/Value pairs in JSON object format.
    |-----------------------------
    |list
    |  Description:
    |    ListSnapshots is used to return the attributes of each snapshot taken on the volume.
    |
    |  Options:
    |     --volumeid
    |        The volume to list snapshots for.
    |        If not provided, all snapshots for all volumes are returned.
    |-----------------------------
    |createschedule
    |  Description:
    |    CreateSchedule is used to create a schedule that will autonomously make a snapshot of a volume at a defined interval.
    |    
    |    The snapshot created can be used later as a backup or rollback to ensure the data on a volume or group of volumes is consistent for the point in time in which the snapshot was created. 
    |    
    |    Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5.
    |
    |  Options:
    |     --schedule
    |        The "Schedule" object will be used to create a new schedule.
    |        Do not set ScheduleID property, it will be ignored.
    |        Frequency property must be of type that inherits from Frequency. Valid types are:
    |        DaysOfMonthFrequency
    |        DaysOrWeekFrequency
    |        TimeIntervalFrequency
    |-----------------------------
    |deletegroup
    |  Description:
    |    DeleteGroupSnapshot is used to delete a group snapshot.
    |    The saveMembers parameter can be used to preserve all the snapshots that
    |    were made for the volumes in the group but the group association will be removed.
    |
    |  Options:
    |     --groupsnapshotid
    |        Unique ID of the group snapshot.
    |     --savemembers
    |        true: Snapshots are kept, but group association is removed.
    |        false: The group and snapshots are deleted.
    |-----------------------------
    |getschedule
    |  Description:
    |    GetSchedule is used to return information about a scheduled snapshot that has been created. You can see information about a specified schedule if there are many snapshot schedules in the system. You can include more than one schedule with this method by specifying additional scheduleIDs to the parameter.
    |
    |  Options:
    |     --scheduleid
    |        Unique ID of the schedule or multiple schedules to display
    |-----------------------------
    |rollbacktogroup
    |  Description:
    |    RollbackToGroupSnapshot is used to roll back each individual volume in a snapshot group to a copy of their individual snapshots.
    |    
    |    Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3.
    |    Snapshots are not created when cluster fullness is at stage 4 or 5.
    |
    |  Options:
    |     --groupsnapshotid
    |        Unique ID of the group snapshot.
    |     --savecurrentstate
    |        true: The previous active volume image is kept.
    |        false: (default) The previous active volume image is deleted.
    |     --name
    |        Name for the snapshot. If no name is given, then the name of the snapshot being rolled back to is used with 
    |        "-copy" appended to the end of the name.
    |     --attributes
    |        List of Name/Value pairs in JSON object format
    |-----------------------------
    |rollbackto
    |  Description:
    |    RollbackToSnapshot is used to make an existing snapshot the "active" volume image. This method creates a new 
    |    snapshot from an existing snapshot. The new snapshot becomes "active" and the existing snapshot is preserved until 
    |    it is manually deleted. The previously "active" snapshot is deleted unless the parameter saveCurrentState is set with 
    |    a value of "true."
    |    Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3.
    |    Snapshots are not created when cluster fullness is at stage 4 or 5.
    |
    |  Options:
    |     --volumeid
    |        VolumeID for the volume.
    |     --snapshotid
    |        ID of a previously created snapshot on the given volume.
    |     --savecurrentstate
    |        true: The previous active volume image is kept.
    |        false: (default) The previous active volume image is deleted.
    |     --name
    |        Name for the snapshot. If no name is given, then the name of the snapshot being rolled back to is used with 
    |        "-copy" appended to the end of the name.
    |     --attributes
    |        List of Name/Value pairs in JSON object format
    |-----------------------------
    |creategroup
    |  Description:
    |    CreateGroupSnapshot is used to create a point-in-time copy of a group of volumes.
    |    The snapshot created can then be used later as a backup or rollback to ensure the data on the group of volumes is consistent for the point in time in which the snapshot was created.
    |    
    |    Note: Creating a group snapshot is allowed if cluster fullness is at stage 2 or 3.
    |    Snapshots are not created when cluster fullness is at stage 4 or 5.
    |
    |  Options:
    |     --volumes
    |        Unique ID of the volume image from which to copy.
    |     --name
    |        A name for the snapshot.
    |        If no name is provided, the date and time the snapshot was taken is used.
    |     --enableremotereplication
    |        Identifies if snapshot is enabled for remote replication.
    |     --retention
    |        The amount of time the snapshot will be retained. Enter in HH:mm:ss
    |     --attributes
    |        List of Name/Value pairs in JSON object format.
    |-----------------------------
    |modifyschedule
    |  Description:
    |    ModifySchedule is used to change the intervals at which a scheduled snapshot occurs. This allows for adjustment to the snapshot frequency and retention.
    |
    |  Options:
    |     --schedule
    |        The "Schedule" object will be used to modify an existing schedule.
    |        The ScheduleID property is required.
    |        Frequency property must be of type that inherits from Frequency. Valid types are:
    |        DaysOfMonthFrequency
    |        DaysOrWeekFrequency
    |        TimeIntervalFrequency
    |-----------------------------
    |listschedules
    |  Description:
    |    ListSchedule is used to return information about all scheduled snapshots that have been created.
    |
    |  Options:
    |-----------------------------
    |delete
    |  Description:
    |    DeleteSnapshot is used to delete a snapshot.
    |    A snapshot that is currently the "active" snapshot cannot be deleted.
    |    You must rollback and make another snapshot "active" before the current snapshot can be deleted.
    |    To rollback a snapshot, use RollbackToSnapshot.
    |
    |  Options:
    |     --snapshotid
    |        The ID of the snapshot to delete.
    |        
  ---------------------------------------------------------------
  Initiators Commands
  ---------------------------------------------------------------
    |-----------------------------
    |modify
    |  Description:
    |    ModifyInitiators enables you to change the attributes of an existing initiator. You cannot change the name of an existing initiator. If you need to change the name of an initiator, delete the existing initiator with DeleteInitiators and create a new one with CreateInitiators.
    |    If ModifyInitiators fails to change one of the initiators provided in the parameter, the method returns an error and does not create any initiators (no partial completion is possible).
    |
    |  Options:
    |     --initiators
    |        A list of Initiator objects containing characteristics of each initiator to modify.
    |-----------------------------
    |create
    |  Description:
    |    CreateInitiators enables you to create multiple new initiator IQNs or World Wide Port Names (WWPNs) and optionally assign them aliases and attributes. When you use CreateInitiators to create new initiators, you can also add them to volume access groups.
    |    If CreateInitiators fails to create one of the initiators provided in the parameter, the method returns an error and does not create any initiators (no partial completion is possible).
    |
    |  Options:
    |     --initiators
    |        A list of Initiator objects containing characteristics of each new initiator
    |-----------------------------
    |list
    |  Description:
    |    ListInitiators enables you to list initiator IQNs or World Wide Port Names (WWPNs).
    |
    |  Options:
    |     --startinitiatorid
    |        The initiator ID at which to begin the listing. You can supply this parameter or the "initiators" parameter, but not both.
    |     --limit
    |        The maximum number of initiator objects to return.
    |     --initiators
    |        A list of initiator IDs to retrieve. You can supply this parameter or the "startInitiatorID" parameter, but not both.
    |-----------------------------
    |delete
    |  Description:
    |    DeleteInitiators enables you to delete one or more initiators from the system (and from any associated volumes or volume access groups).
    |    If DeleteInitiators fails to delete one of the initiators provided in the parameter, the system returns an error and does not delete any initiators (no partial completion is possible).
    |
    |  Options:
    |     --initiators
    |        An array of IDs of initiators to delete.
    |        
  ---------------------------------------------------------------
  SFApi Commands
  ---------------------------------------------------------------
    |-----------------------------
    |invoke
    |  Description:
    |    This will invoke any API method supported by the SolidFire API for the version and port the connection is using.
    |    Returns a nested hashtable of key/value pairs that contain the result of the invoked method.
    |
    |  Options:
    |     --method
    |        The name of the method to invoke. This is case sensitive.
    |     --parameters
    |        An object, normally a dictionary or hashtable of the key/value pairs, to be passed as the params for the method being invoked.
    |        
  ---------------------------------------------------------------
  VirtualVolume Commands
  ---------------------------------------------------------------
    |-----------------------------
    |listhosts
    |  Description:
    |    ListVirtualVolumeHosts returns a list of known ESX hosts.
    |
    |  Options:
    |     --virtualvolumehostids
    |-----------------------------
    |listtasks
    |  Description:
    |    ListVirtualVolumeTasks returns a list of VVol Async Tasks.
    |
    |  Options:
    |     --virtualvolumetaskids
    |-----------------------------
    |enablefeature
    |  Description:
    |    EnableFeature allows you to enable cluster features that are disabled by default.
    |
    |  Options:
    |     --feature
    |        Valid values: vvols: Enable the Virtual Volumes (VVOLs) cluster feature.
    |-----------------------------
    |list
    |  Description:
    |    ListVirtualVolumes enables you to list the virtual volumes currently in the system. You can use this method to list all virtual volumes, or only list a subset.
    |
    |  Options:
    |     --details
    |        Possible values:true: Include more details about each VVOL in the response.false: Include the standard level of detail about each VVOL in the response.
    |     --limit
    |        The maximum number of virtual volumes to list.
    |     --recursive
    |        Possible values:true: Include information about the children of each VVOL in the response.false: Do not include information about the children of each VVOL in the response.
    |     --startvirtualvolumeid
    |        The ID of the virtual volume at which to begin the list.
    |     --virtualvolumeids
    |        A list of virtual volume  IDs for which to retrieve information. If you specify this parameter, the method returns information about only these virtual volumes.
    |-----------------------------
    |listbindings
    |  Description:
    |    ListVirtualVolumeBindings returns a list of VVol bindings.
    |
    |  Options:
    |     --virtualvolumebindingids
    |-----------------------------
    |getcount
    |  Description:
    |    Enables retrieval of the number of virtual volumes currently in the system.
    |
    |  Options:
    |-----------------------------
    |getfeaturestatus
    |  Description:
    |    GetFeatureStatus allows you to retrieve the status of a cluster feature.
    |
    |  Options:
    |     --feature
    |        Valid values: vvols: Find the status of the Virtual Volumes (VVOLs) cluster feature.
    |        
  ---------------------------------------------------------------
  Hardware Commands
  ---------------------------------------------------------------
    |-----------------------------
    |getnvraminfo
    |  Description:
    |    GetNvramInfo allows you to retrieve information from each node about the NVRAM card.  
    |
    |  Options:
    |-----------------------------
    |getnodeinfo
    |  Description:
    |    GetNodeHardwareInfo is used to return all the hardware info and status for the node specified. This generally includes manufacturers, vendors, versions, and other associated hardware identification information.
    |
    |  Options:
    |     --nodeid
    |        The ID of the node for which hardware information is being requested.  Information about a  node is returned if a   node is specified.
    |-----------------------------
    |getclusterinfo
    |  Description:
    |    You can use the GetClusterHardwareInfo method to retrieve the hardware status and information for all Fibre Channel nodes, iSCSI nodes and drives in the cluster. This generally includes manufacturers, vendors, versions, and other associated hardware identification information.
    |
    |  Options:
    |     --type
    |        Include only a certain type of hardware information in the response. Can be one of the following:drives: List only drive information in the response.nodes: List only node information in the response.all: Include both drive and node information in the response.If this parameter is omitted, a type of "all" is assumed.
    |-----------------------------
    |getconfig
    |  Description:
    |    GetHardwareConfig enables you to display the hardware configuration information for a node. NOTE: This method is available only through the per-node API endpoint 5.0 or later.
    |
    |  Options:
    |        
  ---------------------------------------------------------------
  Cluster Commands
  ---------------------------------------------------------------
    |-----------------------------
    |getinfo
    |  Description:
    |    Return configuration information about the cluster.
    |
    |  Options:
    |-----------------------------
    |getapi
    |  Description:
    |    Retrieves the current version of the API and a list of all supported versions.
    |
    |  Options:
    |-----------------------------
    |disablesnmp
    |  Description:
    |    DisableSnmp is used to disable SNMP on the cluster nodes.
    |
    |  Options:
    |-----------------------------
    |getsnmpstate
    |  Description:
    |    GetSnmpState is used to return the current state of the SNMP feature.
    |    
    |    Note: GetSnmpState is new for Element OS 8. Please use this method and SetSnmpACL to migrate your SNMP functionality in the future.
    |
    |  Options:
    |-----------------------------
    |getsnmpinfo
    |  Description:
    |    GetSnmpInfo is used to return the current simple network management protocol (SNMP) configuration information.
    |    
    |    Note: GetSnmpInfo will be available for Element OS 8 and prior releases. It will be deprecated after Element OS 8. There are two new SNMP API methods that you should migrate over to. They are GetSnmpState and GetSnmpACL. Please see details in this document for their descriptions and usage.
    |
    |  Options:
    |-----------------------------
    |getconfig
    |  Description:
    |    The GetClusterConfig API method is used to return information about the cluster configuration this node uses to communicate with the cluster it is a part of.
    |    
    |    Note: This method is available only through the per-node API endpoint 5.0 or later.
    |
    |  Options:
    |-----------------------------
    |deleteallsupportbundles
    |  Description:
    |    DeleteAllSupportBundles is used to delete all support bundles generated with the CreateSupportBundle API method.
    |
    |  Options:
    |-----------------------------
    |getsystemstatus
    |  Description:
    |
    |  Options:
    |-----------------------------
    |setsnmptrapinfo
    |  Description:
    |    SetSnmpTrapInfo is used to enable and disable the generation of SolidFire SNMP notifications (traps) and to specify the set of network host computers that are to receive the notifications. The values passed with each SetSnmpTrapInfo method replaces all values set in any previous method to SetSnmpTrapInfo.
    |
    |  Options:
    |     --traprecipients
    |        List of hosts that are to receive the traps generated by the Cluster Master. At least one object is required if any one of the trap types is enabled.
    |     --clusterfaulttrapsenabled
    |        If "true", when a cluster fault is logged a corresponding solidFireClusterFaultNotification is sent to the configured list of trap recipients.
    |     --clusterfaultresolvedtrapsenabled
    |        If "true", when a cluster fault is logged a corresponding solidFireClusterFaultResolvedNotification is sent to the configured list of trap recipients.
    |     --clustereventtrapsenabled
    |        If "true", when a cluster fault is logged a corresponding solidFireClusterEventNotification is sent to the configured list of trap recipients.
    |-----------------------------
    |listfaults
    |  Description:
    |    ListClusterFaults is used to retrieve information about any faults detected on the cluster.
    |    With this method, both current and resolved faults can be retrieved. The system caches faults every 30 seconds.
    |
    |  Options:
    |     --exceptions
    |     --bestpractices
    |        Include faults triggered by sub-optimal system configuration.
    |        Possible values: true, false
    |     --update
    |     --faulttypes
    |        Determines the types of faults returned: current: List active, unresolved faults.
    |        resolved: List faults that were previously detected and resolved.
    |        all: (Default) List both current and resolved faults. You can see the fault status in the 'resolved' field of the Cluster Fault object.
    |-----------------------------
    |listadmins
    |  Description:
    |    ListClusterAdmins returns the list of all cluster administrators for the cluster. There can be several cluster administrators that have different levels of permissions. There can be only one primary cluster administrator in the system. The primary Cluster Admin is the administrator that was created when the cluster was created. LDAP administrators can also be created when setting up an LDAP system on the cluster.
    |
    |  Options:
    |-----------------------------
    |create
    |  Description:
    |    The CreateCluster method is used to initialize the node in a cluster that has ownership of the "mvip" and "svip" addresses. Each new cluster is initialized using the MIP of the first node in the cluster. This method also automatically adds all the nodes being configured into the cluster. The method is used only once each time a new cluster is initialized.
    |    
    |    Note: You need to log into the node that is used as the master node for the cluster. Once logged in, run the GetBootstrapConfig method on the node to get the IP addresses for the rest of the nodes that you want to include in the cluster. Then run the CreateCluster method.
    |
    |  Options:
    |     --accepteula
    |        Indicate your acceptance of the End User License Agreement when creating this cluster. To accept the EULA, set this parameter to true.
    |     --mvip
    |        Floating (virtual) IP address for the cluster on the management network.
    |     --svip
    |        Floating (virtual) IP address for the cluster on the storage (iSCSI) network.
    |     --repcount
    |        Number of replicas of each piece of data to store in the cluster. Valid value is "2".
    |     --username
    |        User name for the cluster admin.
    |     --password
    |        Initial password for the cluster admin account.
    |     --nodes
    |        CIP/SIP addresses of the initial set of nodes making up the cluster. This node's IP must be in the list.
    |     --attributes
    |        List of Name/Value pairs in JSON object format.
    |-----------------------------
    |disableencryptionatrest
    |  Description:
    |    The DisableEncryptionAtRest method enables you to remove the encryption that was previously applied to the cluster using the EnableEncryptionAtRest method.
    |    This disable method is asynchronous and returns a response before encryption is disabled.
    |    You can use the GetClusterInfo method to poll the system to see when the process has completed.
    |
    |  Options:
    |-----------------------------
    |addadmin
    |  Description:
    |    AddClusterAdmin adds a new Cluster Admin. A Cluster Admin can be used to manage the cluster via the API and management tools. Cluster Admins are completely separate and unrelated to standard tenant accounts.
    |    
    |    Each Cluster Admin can be restricted to a sub-set of the API. SolidFire recommends using multiple Cluster Admins for different users and applications. Each Cluster Admin should be given the minimal permissions necessary to reduce the potential impact of credential compromise.
    |
    |  Options:
    |     --username
    |        Unique username for this Cluster Admin.
    |     --password
    |        Password used to authenticate this Cluster Admin.
    |     --access
    |        Controls which methods this Cluster Admin can use. For more details on the levels of access, see "Access Control" in the Element API Guide.
    |     --accepteula
    |        Indicate your acceptance of the End User License Agreement when creating this cluster admin. To accept the EULA, set this parameter to true.
    |     --attributes
    |        List of Name/Value pairs in JSON object format.
    |-----------------------------
    |setntpinfo
    |  Description:
    |    SetNtpInfo is used to configure the NTP on cluster nodes. The values set with this interface apply to all nodes in the cluster. The nodes can only be configured as a server where a host is selected to administrate the networking and/or a broadcast client where each host sends each message to each peer.
    |
    |  Options:
    |     --servers
    |        List of NTP servers to add to each node's NTP configuration.
    |     --broadcastclient
    |        Enable every node in the cluster as a broadcase client.
    |-----------------------------
    |setconfig
    |  Description:
    |    The SetClusterConfig API method is used to set the configuration this node uses to communicate with the cluster it is associated with. To see the states in which these objects can be modified see Cluster Object on page 109. To display the current cluster interface settings for a node, run the GetClusterConfig API method.
    |    
    |    Note: This method is available only through the per-node API endpoint 5.0 or later.
    |
    |  Options:
    |     --cluster
    |        Objects that are changed for the cluster interface settings. Only the fields you want changed need to be added to this method as objects in the "cluster" parameter.
    |-----------------------------
    |modifyadmin
    |  Description:
    |    ModifyClusterAdmin is used to change the settings for a Cluster Admin or LDAP Cluster Admin. Access for the administrator Cluster Admin account cannot be changed.
    |
    |  Options:
    |     --clusteradminid
    |        ClusterAdminID for the Cluster Admin or LDAP Cluster Admin to modify.
    |     --password
    |        Password used to authenticate this Cluster Admin.
    |     --access
    |        Controls which methods this Cluster Admin can use. For more details on the levels of access, see "Access Control" in the Element API Guide.
    |     --attributes
    |        List of Name/Value pairs in JSON object format.
    |-----------------------------
    |getsnmptrapinfo
    |  Description:
    |    GetSnmpTrapInfo is used to return current SNMP trap configuration information.
    |
    |  Options:
    |-----------------------------
    |listevents
    |  Description:
    |    ListEvents returns events detected on the cluster, sorted from oldest to newest.
    |
    |  Options:
    |     --maxevents
    |        Specifies the maximum number of events to return.
    |     --starteventid
    |        Identifies the beginning of a range of events to return.
    |     --endeventid
    |        Identifies the end of a range of events to return.
    |     --eventqueuetype
    |-----------------------------
    |snmpsendtesttraps
    |  Description:
    |    SnmpSendTestTraps enables you to test SNMP functionality for a cluster. This method instructs the cluster to send test SNMP traps to the currently configured SNMP manager.
    |
    |  Options:
    |-----------------------------
    |removeadmin
    |  Description:
    |    RemoveClusterAdmin is used to remove a Cluster Admin. The "admin" Cluster Admin cannot be removed.
    |
    |  Options:
    |     --clusteradminid
    |        ClusterAdminID for the Cluster Admin to remove.
    |-----------------------------
    |modifyfullthreshold
    |  Description:
    |    ModifyClusterFullThreshold is used to change the level at which an event is generated when the storage cluster approaches the capacity utilization requested. The number entered in this setting is used to indicate the number of node failures the system is required to recover from. For example, on a 10 node cluster, if you want to be alerted when the system cannot recover from 3 nodes failures, enter the value of "3". When this number is reached, a message alert is sent to the Event Log in the Cluster Management Console.
    |
    |  Options:
    |     --stage2awarethreshold
    |        Number of nodes worth of capacity remaining on the cluster that triggers a notification.
    |     --stage3blockthresholdpercent
    |        Percent below "Error" state to raise a cluster "Warning" alert.
    |     --maxmetadataoverprovisionfactor
    |        A value representative of the number of times metadata space can be over provisioned relative to the amount of space available. For example, if there was enough metadata space to store 100 TiB of volumes and this number was set to 5, then 500 TiB worth of volumes could be created.
    |-----------------------------
    |getlimits
    |  Description:
    |    GetLimits enables you to retrieve the limit values set by the API. These values might change between releases of  Element, but do not change without an update to the system. Knowing the limit values set by the API can be useful when writing API scripts for user-facing tools.NOTE: The GetLimits method returns the limits for the current software version regardless of the API endpoint version used to pass the method.
    |
    |  Options:
    |-----------------------------
    |getcurrentadmin
    |  Description:
    |    GetCurrentClusterAdmin returns information for the current primary cluster administrator. The primary Cluster Admin was ncreated when the cluster was created.
    |
    |  Options:
    |-----------------------------
    |createsupportbundle
    |  Description:
    |    CreateSupportBundle is used to create a support bundle file under the node's directory. When the bundle has been successfully created, the bundle is stored on the node as a tar.gz file.
    |
    |  Options:
    |     --bundlename
    |        Unique name for each support bundle created. If no name is provided, then 'supportbundle' and the node name is used as a file name.
    |     --extraargs
    |        This parameter is fed to the sf_make_support_bundle script. Should be used only at the request of SolidFire Support.
    |     --timeoutsec
    |        The number of seconds to let the support bundle script run before timing out and stopping. Default is 1500 seconds.
    |-----------------------------
    |getcapacity
    |  Description:
    |    Return the high-level capacity measurements for an entire cluster.
    |    The fields returned from this method can be used to calculate the efficiency rates that are displayed in the Element User Interface.
    |
    |  Options:
    |-----------------------------
    |getntpinfo
    |  Description:
    |    GetNtpInfo is used to return the current network time protocol (NTP) configuration information.
    |
    |  Options:
    |-----------------------------
    |enableencryptionatrest
    |  Description:
    |    The EnableEncryptionAtRest method is used to enable the Advanced Encryption Standard (AES) 256-bit encryption at rest on the cluster so that the cluster can manage the encryption key used for the drives on each node. This feature is not enabled by default. Enabling this operation allows the cluster to automatically manage encryption keys internally for the drives on each node in the cluster. Nodes do not store the keys to unlock drives and the keys are never passed over the network. Two nodes participating in a cluster are required to access the key to disable encryption on a drive. The encryption management does not affect performance or efficiency on the cluster. If an encryption-enabled drive or node is removed from the cluster with the API, all data is secure erased and any data left on the drive cannot be read or accessed.
    |    Enabling or disabling encryption should be performed when the cluster is running and in a healthy state. Encryption can be enabled or disabled at your discretion and can be performed as often as you need.
    |    Note: This process is asynchronous and returns a response before encryption is enabled. The GetClusterInfo method can be used to poll the system to see when the process has completed.
    |
    |  Options:
    |-----------------------------
    |getversioninfo
    |  Description:
    |    Return information about the Element software version running on each node in the cluster.
    |    Information about the nodes that are currently in the process of upgrading software is also returned.
    |
    |  Options:
    |-----------------------------
    |setsnmpacl
    |  Description:
    |    SetSnmpACL is used to configure SNMP access permissions on the cluster nodes. The values set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpACL. Also note that the values set with this interface replace all "network" or "usmUsers" values set with the older SetSnmpInfo.
    |
    |  Options:
    |     --networks
    |        List of networks and what type of access they have to the SNMP servers running on the cluster nodes. See SNMP Network Object for possible "networks" values. REQUIRED if SNMP v# is disabled.
    |     --usmusers
    |        List of users and the type of access they have to the SNMP servers running on the cluster nodes. REQUIRED if SNMP v3 is enabled.
    |-----------------------------
    |clearfaults
    |  Description:
    |    ClearClusterFaults is used to clear information about both current faults that are resolved as well as faults that were previously detected and resolved can be cleared.
    |
    |  Options:
    |     --faulttypes
    |        Determines the types of faults cleared:
    |        current: Faults that are currently detected and have not been resolved.
    |        resolved: Faults that were previously detected and resolved.
    |        all: Both current and resolved faults are cleared. The fault status can be determined by the "resolved" field of the fault object.
    |-----------------------------
    |getsnmpacl
    |  Description:
    |    GetSnmpACL is used to return the current SNMP access permissions on the cluster nodes.
    |
    |  Options:
    |-----------------------------
    |getstate
    |  Description:
    |    The GetClusterState method is used to indicate if a node is part of a cluster or not. The three states are: Available: Node has not been configured with a cluster name.Pending: Node is pending for a specific named cluster and can be added.Active: Node is active and a member of a cluster and may not be added to another cluster.
    |
    |  Options:
    |     --force
    |        To run this command, the force parameter must be set to true.
    |-----------------------------
    |enablesnmp
    |  Description:
    |    EnableSnmp is used to enable SNMP on the cluster nodes. The values set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to EnableSnmp.
    |
    |  Options:
    |     --snmpv3enabled
    |        If set to "true", then SNMP v3 is enabled on each node in the cluster. If set to "false", then SNMP v2 is enabled.
    |-----------------------------
    |getstats
    |  Description:
    |    GetClusterStats is used to return high-level activity measurements for the cluster. Values returned are cumulative from the creation of the cluster.
    |
    |  Options:
    |-----------------------------
    |getmasternodeid
    |  Description:
    |    GetClusterMasterNodeID is used to return the ID of the node that can perform cluster-wide administration tasks and holds the storage virtual IP (SVIP) and management virtual IP (MVIP).
    |
    |  Options:
    |-----------------------------
    |setsnmpinfo
    |  Description:
    |    SetSnmpInfo is used to configure SNMP v2 and v3 on the cluster nodes. The values set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpInfo.
    |    
    |    Note: EnableSnmp and SetSnmpACL methods can be used to accomplish the same results as SetSnmpInfo. SetSnmpInfo will no longer be available after the Element 8 release. Please use EnableSnmp and SetSnmpACL in the future.
    |
    |  Options:
    |     --networks
    |        List of networks and what type of access they have to the SNMP servers running on the cluster nodes. See SNMP Network Object for possible "networks" values. SNMP v2 only.
    |     --enabled
    |        If set to "true", then SNMP is enabled on each node in the cluster.
    |     --snmpv3enabled
    |        If set to "true", then SNMP v3 is enabled on each node in the cluster.
    |     --usmusers
    |        If SNMP v3 is enabled, this value must be passed in place of the "networks" parameter. SNMP v3 only.
    |-----------------------------
    |getfullthreshold
    |  Description:
    |    GetClusterFullThreshold is used to view the stages set for cluster fullness levels. All levels are returned when this method is entered.
    |
    |  Options:
    |-----------------------------
    |listsyncjobs
    |  Description:
    |    ListSyncJobs is used to return information about synchronization jobs that are running on a SolidFire cluster. Synchronization jobs that are returned with this method are, "slice," "clone" and "remote."
    |
    |  Options:
    |        
  ---------------------------------------------------------------
  StorageContainers Commands
  ---------------------------------------------------------------
    |-----------------------------
    |modifystoragecontainer
    |  Description:
    |    Modifies an existing storage container.
    |
    |  Options:
    |     --storagecontainerid
    |     --initiatorsecret
    |     --targetsecret
    |-----------------------------
    |list
    |  Description:
    |    Gets information for all storage containers currently in the system.
    |
    |  Options:
    |     --storagecontainerids
    |        List of storage containers to get
    |-----------------------------
    |getstoragecontainerefficiency
    |  Description:
    |    GetStorageContainerEfficiency enables you to retrieve efficiency information about a virtual volume storage container.
    |
    |  Options:
    |     --storagecontainerid
    |        The ID of the storage container for which to retrieve efficiency information.
    |-----------------------------
    |createstoragecontainer
    |  Description:
    |    Creates a new VVols storage container.
    |
    |  Options:
    |     --name
    |        Name of the storage container.
    |     --initiatorsecret
    |        The secret for CHAP authentication for the initiator
    |     --targetsecret
    |        The secret for CHAP authentication for the target
    |-----------------------------
    |delete
    |  Description:
    |    Deletes a storage container from the system.
    |
    |  Options:
    |     --storagecontainerids
    |        list of storageContainerID of the storage container to delete.
    |        
  ---------------------------------------------------------------
  LDAP Commands
  ---------------------------------------------------------------
    |-----------------------------
    |addclusteradmin
    |  Description:
    |    AddLdapClusterAdmin is used to add a new LDAP Cluster Admin. An LDAP Cluster Admin can be used to manage the cluster via the API and management tools. LDAP Cluster Admins are completely separate and unrelated to standard tenant accounts.
    |    
    |    An LDAP group that has been defined in Active Directory can also be added using this API method. The access level that is given to the group will be passed to the individual users in the LDAP group.
    |
    |  Options:
    |     --username
    |        The distinguished user name for the new LDAP cluster admin.
    |     --access
    |        Controls which methods this Cluster Admin can use. For more details on the levels of access, see the Access Control appendix in the SolidFire API Reference.
    |     --accepteula
    |        Indicate your acceptance of the End User License Agreement when creating this cluster admin. To accept the EULA, set this parameter to true.
    |     --attributes
    |        List of Name/Value pairs in JSON object format.
    |-----------------------------
    |getconfiguration
    |  Description:
    |    The GetLdapConfiguration is used to get the LDAP configuration currently active on the cluster.
    |
    |  Options:
    |-----------------------------
    |testauthentication
    |  Description:
    |    The TestLdapAuthentication is used to verify the currently enabled LDAP authentication configuration settings are correct. If the configuration settings are correct, the API call returns a list of the groups the tested user is a member of.
    |
    |  Options:
    |     --username
    |        The username to be tested.
    |     --password
    |        The password for the username to be tester.
    |     --ldapconfiguration
    |        An ldapConfiguration object to be tested. If this parameter is provided, the API call will test the provided configuration even if LDAP authentication is currently disabled.
    |-----------------------------
    |disableauthentication
    |  Description:
    |    The DisableLdapAuthentication method is used disable LDAP authentication and remove all LDAP configuration settings. This call will not remove any configured cluster admin accounts (user or group). However, those cluster admin accounts will no longer be able to log in.
    |
    |  Options:
    |-----------------------------
    |enableauthentication
    |  Description:
    |    The EnableLdapAuthentication method is used to configure an LDAP server connection to use for LDAP authentication to a SolidFire cluster. Users that are members on the LDAP server can then log in to a SolidFire storage system using their LDAP authentication userid and password.
    |
    |  Options:
    |     --authtype
    |        Identifies which user authentcation method will be used. 
    |        Must be one of the following:
    |        DirectBind
    |        SearchAndBind (default)
    |     --groupsearchbasedn
    |        The base DN of the tree to start the group search (will do a subtree search from here).
    |     --groupsearchcustomfilter
    |        REQUIRED for CustomFilter
    |        For use with the CustomFilter search type, an LDAP filter to use to return the DNs of a user's groups.
    |        The string can have placeholder text of %USERNAME% and %USERDN% to be replaced with their username and full userDN as needed.
    |     --groupsearchtype
    |        Controls the default group search filter used, can be one of the following:
    |        NoGroups: No group support.
    |        ActiveDirectory: (default) Nested membership of all of a user's AD groups.
    |        MemberDN: MemberDN style groups (single-level).
    |     --searchbinddn
    |        REQUIRED for SearchAndBind
    |        A fully qualified DN to log in with to perform an LDAP search for the user (needs read access to the LDAP directory).
    |     --searchbindpassword
    |        REQUIRED for SearchAndBind
    |        The password for the searchBindDN account used for searching.
    |     --serveruris
    |        A list of LDAP server URIs (examples: "ldap://1.2.3.4" and ldaps://1.2.3.4:123")
    |     --userdntemplate
    |        REQUIRED for DirectBind
    |        A string that is used to form a fully qualified user DN.
    |        The string should have the placeholder text "%USERNAME%" which will be replaced with the username of the authenticating user.
    |     --usersearchbasedn
    |        REQUIRED for SearchAndBind
    |        The base DN of the tree used to start the search (will do a subtree search from here).
    |     --usersearchfilter
    |        REQUIRED for SearchAndBind.
    |        The LDAP filter to use.
    |        The string should have the placeholder text "%USERNAME%" which will be replaced with the username of the authenticating user.
    |        Example: (&(objectClass=person) (sAMAccountName=%USERNAME%)) will use the sAMAccountName field in Active Directory to match the nusername entered at cluster login.
    |        
  ---------------------------------------------------------------
  BackupTarget Commands
  ---------------------------------------------------------------
    |-----------------------------
    |modify
    |  Description:
    |    ModifyBackupTarget is used to change attributes of a backup target.
    |
    |  Options:
    |     --backuptargetid
    |        Unique identifier assigned to the backup target.
    |     --name
    |        Name for the backup target.
    |     --attributes
    |        List of Name/Value pairs in JSON object format.
    |-----------------------------
    |create
    |  Description:
    |    CreateBackupTarget allows you to create and store backup target information so that you do not need to re-enter it each time a backup is created.
    |
    |  Options:
    |     --name
    |        Name for the backup target.
    |     --attributes
    |        List of Name/Value pairs in JSON object format.
    |-----------------------------
    |list
    |  Description:
    |    You can use ListBackupTargets to retrieve information about all backup targets that have been created.
    |
    |  Options:
    |-----------------------------
    |remove
    |  Description:
    |    RemoveBackupTarget allows you to delete backup targets.
    |
    |  Options:
    |     --backuptargetid
    |        Unique target ID of the target to remove.
    |-----------------------------
    |get
    |  Description:
    |    GetBackupTarget allows you to return information about a specific backup target that has been created.
    |
    |  Options:
    |     --backuptargetid
    |        Unique identifier assigned to the backup target.
    |        
