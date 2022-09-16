import csv

with open("fruitslist.csv", "r") as filedata:
    fruitslist = csv.reader(filedata, delimiter=",")
    for output in fruitslist:
        print(",".join(output))