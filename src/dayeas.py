import entry
import miner
import csv

def mineFromFile(file):
    journal = []
    with open(file,'rt') as csvfile:
        jreader = csv.reader(csvfile, delimiter=",") #does not support emoji.
        for row in jreader:
            #currently reads in the column name row. Not tops!
            # year,date,weekday,time,mood,activities,note
            date = row[0]+"-"+row[1]+"-"+row[3]
            mood = row[4]
            activities = set(row[5].split(" | "))
            note = row[6]
            journal.append(entry.Entry(date,mood,activities,note))

        jminer = miner.Miner(journal)
        results = jminer.apriori(10,1)
        return results

# with is a nice boy.
file = "data/daylio_export.csv"

data = mineFromFile(file)
for key in data:
    for e in key:
        print(e+", ",end="")

    print(":"+str(data[key]))