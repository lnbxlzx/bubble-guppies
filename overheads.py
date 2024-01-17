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
        #get the Day, Items, Note, Amount for each record
        #and append to the overheads list
        overheads.append([row[0],row[1],row[2],row[3]]) 
        
# def percentage_calculator(Items,total_overheads):
#     """
#     function to calculate the percentage of each item in the overheads
#     """
#     return (total_amount / total_overheads) * 100


total_overheads = 0

for row in overheads:

    # read the row
    Day = row[0]
    Items = row[1] 
    Amount = float(row[3].replace("$",""))

    total_overheads += Amount
