import csv
from pathlib import Path

# create a file path to csv file.
fp = Path.cwd()/"overheads.csv"

# read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty list for overheads
    overheads=[] 

    # append cash on hand into the overheads list
    for row in reader:
        #get the type of overheads and its percentage for each record
        #and append to the overheads list
        overheads.append([row[0],row[1]]) 

highest_percentage = 0
highest_percentage_overheads = None

overheads = []
for row in overheads:
    Category = row[0]
    Percentage = row[1]

    highest_percentage = max(overhead[1] for overhead in overheads)
    highest_overhead = [overhead for overhead in overheads if overhead[1] == highest_percentage]

output_file = "Summary_report.txt"
with open(output_file, "w") as file:

    #write driver data in txt file

    file.write(f"[HIGHEST OVERHEADS] {max(highest_overhead)}):{highest_percentage}")

