#!/usr/bin/python3
# Created by: Michael O'Brien
# Project: Standarize VLANs with Nornir

#Import Nornir Plugins
from nornir import InitNornir
from nornir.plugins.functions.text import print_title, print_result
#Import Tasks from parse.py & new_configs.py
from parse import get_config, parse_config
from new_configs import build_configs

#Initialize Nornir and Filter Inventory
nr = InitNornir(config_file="config.yaml")
switches = nr.filter(role="switch")

#Prompt for creds then assign them to devices
username = input("Enter Username: ")
password = input("Enter Password: ")
nr.inventory.defaults.username = username
nr.inventory.defaults.password = password

#Get Configuration for all hosts
#See parse.py file for task details
config = switches.run(name="Get Configurations",task=get_config)
print_title(config)

#Parse Configuration from parse.py file
parsed = switches.run(name="Parse Configurations", task=parse_config)
print_title(parsed)
print_result(parsed)

#Build & Push New configurations to devices
#See new_configs.py file for task details
new = switches.run(name="Building New Configs", task=build_configs)
print_result(new)
