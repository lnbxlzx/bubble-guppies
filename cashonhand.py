import csv
from pathlib import Path

deficit = []
surplus = []

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
    day_number = row[0]
    s_amount = row[1]
    prev_amount = row [1][0]
    cashsurplus = 0

    def calculate_surplus():
        for prev_amount in surplus:
            if s_amount > prev_amount:
                cashsurplus = s_amount - prev_amount
            else:
                None
        return 
            
    if cashsurplus > highest_surplus:
        highest_surplus = final_surplus
        day_number = day

    
    

output_file = "Summary_report.txt"
with open(output_file, "w") as file:

    #write driver data in txt file

    file.write(f"[HIGHEST OVERHEADS] {highest_percentage_overheads} {highest_percentage}%")

    
