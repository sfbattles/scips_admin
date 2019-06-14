from agent.models import AgentMaster
import csv, os

file_loc = '/Users/richl/dev/source/scips_admin/agent/agentmaster.csv'
print (file_loc)
with open(file_loc, "r") as csvfile:
    reader = csv.DictReader(csvfile, delimiter="|")
    for row in reader:
        print(row['agent_master_code'],row['Name'])
        p = AgentMaster(master_code=row['agent_master_code'],
        name=row['Name'])
        p.save()