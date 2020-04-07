# Standardize VLANs with Nornir

This repo contains a Nornir script that uses Netbox as an inventory source.  The main script is the runbook.py file.

The runbook gets the running configuration from each device, parses the output, then reconfigures all interfaces based on new VLAN assignments.

### Inventory
Instead of a static inventory I am using Netbox as a dynamic inventory source.  This is set up in the config.yaml file.

### Parse.py
This file contains three functions.
- parse_interfaces: Parses the current configuation with the TTP template in the ttp folder.
- parse_config: Calls the parse_interfaces function in order to parse which interfaces are access ports and which are trunks.
- get_config: uses NAPALM to get the running configuration from devices.

### New_configs.py
This file contains one function with two Nornir tasks.
- The first task creates a new template based on the base.j2 Jinja2 template in the templates folder.
- The second task uses NAPALM to merge the new configuration to the devices.

### Runbook.py
This is the Nornir runbook that needs to be run with python.  It will prompt for device credentials and then execute the workflow.

### Blog Post
Please view this blog post to see how this was created:  https://journey2theccie.wordpress.com/2020/04/07/using-nornir-to-standardize-vlans-across-100-sites
