import csv
from pathlib import Path

# create a file path to csv file.
fp = Path.cwd()/"cashonhand.csv"

# read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty list for delivery record
    cash_on_hand=[] 

    # append cash on hand into the cash_on_hand list
    for row in reader:
        #get the day and amount for each record
        #and append to the cash on hand list
        cash_on_hand.append([row[0],row[1]]) 


cash_on_hand_diff = 0
for row in cash_on_hand:
    day = row[0]
    amount = row[1]

    