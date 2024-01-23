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


for row in overheads:
    Category = row[0]
    Percentage = float(row[1].replace("%",""))

    if Percentage > highest_percentage:
        highest_percentage = Percentage
        highest_percentage_overheads = Category

output_file = "Summary_report.txt"
with open(output_file, "w") as file:

    #write driver data in txt file

    file.write(f"[HIGHEST OVERHEADS] {highest_percentage_overheads.upper()} {highest_percentage}%")

