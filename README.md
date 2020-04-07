# Standardize VLANs with Nornir

This repo contains a Nornir script that uses Netbox as an inventory source.  The main script is the runbook.py file.

The runbook gets the running configuration from each device, parses the output, then reconfigures all interfaces based on new VLAN assignments.

### Blog Post
Please view this blog post to see how this was created:  https://journey2theccie.wordpress.com/2020/04/07/using-nornir-to-standardize-vlans-across-100-sites
