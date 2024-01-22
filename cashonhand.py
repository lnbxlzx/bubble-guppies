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
    deficit = []
    surplus = []
    
    # append cash on hand into the cash_on_hand list
    for row in reader:
        #get the day and amount for each record
        #and append to the cash on hand list
        cash_on_hand.append([row[0],row[1]]) 

highest_surplus = 0
highest_deficit = 0
day = None
final_surplus = 0
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
                
    if cashsurplus > highest_surplus:
        highest_surplus = final_surplus
        day_number = day

    
    

output_file = "Summary_report.txt"
with open(output_file, "w") as file:

    #write driver data in txt file
    file.write(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
    file.write(f"[HIGHEST CASH SURPLUS] {day} {highest_surplus}%")

    
