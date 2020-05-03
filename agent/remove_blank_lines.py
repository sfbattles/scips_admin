with open("stateabbreviation.txt","r") as statefile, open("stateabbreviation.csv","w") as outputfile:
    line = statefile.readline()
    for line in statefile:
        if len(line.strip()) != 0:
            current_line = list(line.split("-"))
            output = f"{current_line[0].strip()}|{current_line[1].strip()}\n"
            outputfile.write(output)