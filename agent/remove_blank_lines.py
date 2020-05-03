flag = True
with open("stateabbreviation.txt","r") as statefile, open("stateabbreviation.csv","w") as outputfile:
    for line in statefile:
        if flag == True:
            outputfile.write("State|Abbreviation\n")
            flag = False
        if len(line.strip()) != 0:
            current_line = list(line.split("-"))
            output = f"{current_line[0].strip()}|{current_line[1].strip()}\n"
            outputfile.write(output)