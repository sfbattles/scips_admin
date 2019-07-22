from agent.models import Agent
from agent.models import AgentMaster
from agent.models import agentname

import csv, os

file_loc = '/Users/richl/dev/source/scips_admin/agent/agentname.csv'
print (file_loc)
with open(file_loc, "r") as csvfile:
    reader = csv.DictReader(csvfile, delimiter="|")
    for row in reader:
        print(row['agent_no'],row['agent_master_code'])
        agent_master_obj, created = AgentMaster.objects.get_or_create(master_code=row['agent_master_code'])
        p = Agent(agent_no=row['agent_no'],
        
        agent_master_code = agent_master_obj,
        name=row['name'],
        p.save()