import csv
from pathlib import Path

# create a file path to csv file.
fp = Path.cwd()/"profitandloss.csv"

# read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty list for profit and loss
    profit_and_lost=[] 

    # append cash on hand into the  profit_and_lost list
    for row in reader:
        #get the Day, Sales, Trading Profit, Operating Expense, Net Profit for each record
        #and append to the profit and lost list
        profit_and_lost.append([row[0],row[1],row[2],row[3],row[4]])   