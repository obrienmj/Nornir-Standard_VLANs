from nornir import InitNornir
from nornir.plugins.tasks import networking, text
import logging

#This Task has 2 subtasks:
####First is build the configuration with a j2 template.
######This takes access & trunk ports as input into the template to build the interface configs
####Second task pushes the new configuration to the device as a merge
def build_configs(task):
    r = task.run(task=text.template_file,
                name="New Configuration",
                template="base.j2",
                path=f"templates",
                access_ports=task.host['access_ports'],
                trunk_ports=task.host['trunk_ports'],
                SVI=task.host['SVI'],
                severity_level=logging.DEBUG
                )

    cmds = r.result
    print(cmds)

    task.host['nconfig'] = r.result

    task.run(task=networking.napalm_configure,
            name="Loading Configuration on the device",
            replace=False,
            configuration=task.host['nconfig'],
            severity_level=logging.INFO
            )
