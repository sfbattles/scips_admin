from agent.models import State

import csv, os

file_loc = '/Users/richl/dev/source/document_portal_project/agent/stateabbreviation.csv'
print (file_loc)
with open(file_loc, "r") as csvfile:
    reader = csv.DictReader(csvfile, delimiter="|")
    for row in reader:
        print(row['State'],row['Abbreviation'])
        state_obj, created = State.objects.get_or_create(state_abbreviation=row['Abbreviation'],state=row['State'])
        state_obj.save()