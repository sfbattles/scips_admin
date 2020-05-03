from agent.models import Agent
from agent.models import AgentEmail

import csv, os

file_loc = '/Users/richl/dev/source/document_portal_project/agent/agentemail.csv'
print (file_loc)
with open(file_loc, "r") as csvfile:
    reader = csv.DictReader(csvfile, delimiter="|")
    for row in reader:
        print(row['agent_no'],row['email'])
        agent_obj, created = Agent.objects.get_or_create(agent_no=row['agent_no'])
        p = AgentEmail(agent_no = agent_obj,
            email=row['email'])
        p.save()
