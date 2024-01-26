import csv
from pathlib import Path

def cash_on_hand():
    # File path to csv file, cwd means current working directory
    fp = Path.cwd() / "csv_reports/Cash_on_Hand.csv"

    # Open the file in read mode, encoding is set to UTF-8, newline is set to "" to prevent blank lines
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        # Skip the first row of the csv file, since it is header
        next(reader)

        cash_on_hand_data = []

        # Initialize the prev_cash variable, this is used to store the previous cash
        prev_cash = None

        # Initialize the max_increment and max_decrement variables, these are used to store the day and amount of the highest increment and decrement
        max_increment = {'day': None, 'amount': 0}
        max_decrement = {'day': None, 'amount': 0}
        deficits = []

        # Loop through the rows in the csv file and append them to the cash_on_hand_data list as a list of 2 elements, day and cash
        for row in reader:
            day = row[0]
            current_cash = float(row[1])
            cash_on_hand_data.append([day, current_cash])

            if prev_cash is not None:
                change = current_cash - prev_cash
                if change > max_increment['amount']:
                    max_increment = {'day': day, 'amount': change}
                elif change < max_decrement['amount']:
                    max_decrement = {'day': day, 'amount': change}
                # If the change is less than 0, then append the change and day to the deficits list
                if change < 0:
                    deficits.append((abs(change), day))

            prev_cash = current_cash

    # Check if the cash_on_hand_data list is increasing or decreasing
    is_increasing = True
    is_decreasing = True

    # Starting from the first element and iterating until the second-to-last element
    for i in range(len(cash_on_hand_data) - 1):
        # Compare the current element with the next one
        if cash_on_hand_data[i + 1][1] < cash_on_hand_data[i][1]:
            is_increasing = False
        if cash_on_hand_data[i + 1][1] > cash_on_hand_data[i][1]:
            is_decreasing = False

        # If both flags become false, we can break early as the sequence is neither
        if not is_increasing and not is_decreasing:
            break

    if is_increasing:
        lines = ["[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN PREVIOUS DAY"]
        lines.append(f"[HIGHEST CASH SURPLUS] DAY: {max_increment['day']}, AMOUNT: SGD {max_increment['amount']} ")
    elif is_decreasing:
        lines = ["[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN PREVIOUS DAY"]
        lines.append(f"[HIGHEST CASH DEFICIT] DAY: {max_decrement['day']}, AMOUNT: SGD {max_decrement['amount']} ")    
    else:
        lines = []
        for amount, day in deficits:
            lines.append(f"[CASH DEFICIT] DAY: {day}, AMOUNT: SGD {amount}")
        deficits.sort()
        top_3_deficits = deficits[:3]
        lines.append(f"[HIGHEST CASH DEFICIT] DAY: {top_3_deficits[0][1]}, AMOUNT: SGD {top_3_deficits[0][0]}")
        lines.append(f"[2ND HIGHEST CASH DEFICIT] DAY: {top_3_deficits[1][1]}, AMOUNT: SGD {top_3_deficits[1][0]}")
        lines.append(f"[3RD HIGHEST CASH DEFICIT] DAY: {top_3_deficits[2][1]}, AMOUNT: SGD {top_3_deficits[2][0]}")
    return lines

    
