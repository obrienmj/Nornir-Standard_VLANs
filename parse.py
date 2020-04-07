from ttp import ttp
from nornir import InitNornir
from nornir.plugins.tasks import networking

#Accept old configuration
#Use TTP to parse current interface configuration
#Returns all interfaces as a list of dictionaries
def parse_interfaces(config):
    parser = ttp(data=config, template='ttp/interfaces.j2')
    parser.parse()
    interfaces = parser.result()[0][0]
    return interfaces


#Parse running configuration of device
#Create new key in each host with list of interfaces, access ports, and trunks
def parse_config(task):
    print('Parsing config for ' + task.host.hostname)

    task.host['interfaces'] = [interface for interface in parse_interfaces(task.host['config'])
                             if 'mode' in interface.keys()]
    task.host['access_ports'] = [interface for interface in task.host['interfaces']
                                      if interface['mode'] == 'access'
                                      and 'access_vlan' in interface.keys()]
    task.host['trunk_ports'] = [interface for interface in task.host['interfaces']
                                     if interface['mode'] == 'trunk'
                                     and 'native_vlan' in interface.keys()]
    task.host['SVI'] = [interface for interface in parse_interfaces(task.host['config'])
                        if 'ip_address' in interface.keys()]


#Get Configs for each device with NAPALM
#Save Running config as a new device key
def get_config(task):
    r = task.run(
        task=networking.napalm_get,
        getters="config"
    )
    task.host['config'] = r.result['config']['running']
