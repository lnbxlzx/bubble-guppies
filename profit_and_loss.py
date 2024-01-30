import csv
from pathlib import Path


def profit_and_loss():
    # File path to csv file, cwd means current working directory
    fp = Path.cwd() / "csv_reports/Profit_and_Loss.csv"

    # Open the file in read mode, encoding is set to UTF-8, newline is set to "" to prevent blank lines
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        # Skip the first row of the csv file, since it is header
        next(reader)
        profit_and_lost = []

        # Initialize the prev_profit variable, this is used to store the previous profit
        prev_profit = None

        # Initialize the max_increment and max_decrement variables, these are used to store the day and amount of the highest increment and decrement
        max_increment = {'day': None, 'amount': 0}
        max_decrement = {'day': None, 'amount': 0}
        deficits = []

        # Loop through the rows in the csv file and append them to the profit_and_lost list as a list of 2 elements, day and profit
        for row in reader:
            day = row[0]
            current_profit = float(row[4])
            profit_and_lost.append([day, current_profit])

            # If prev_profit is not None, then calculate the change between the current_profit and prev_profit
            if prev_profit is not None:
                change = current_profit - prev_profit
                if change > max_increment['amount']:
                    max_increment = {'day': day, 'amount': change}
                elif change < max_decrement['amount']:
                    max_decrement = {'day': day, 'amount': change}

                # If the change is less than 0, then append the change and day to the deficits list
                if change < 0:
                    deficits.append((abs(change), day))

            prev_profit = current_profit

    # Check if the profit_and_lost list is increasing or decreasing
    is_increasing = True
    is_decreasing = True

    # Starting from the first element and iterating until the second-to-last element
    for i in range(len(profit_and_lost) - 1):
        # Compare the current element with the next one
        if profit_and_lost[i + 1][1] < profit_and_lost[i][1]:
            is_increasing = False
        if profit_and_lost[i + 1][1] > profit_and_lost[i][1]:
            is_decreasing = False

        # If both flags become false, we can break early as the sequence is neither
        if not is_increasing and not is_decreasing:
            break
    lines = []

    if is_increasing:
        lines = ["[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY"]
        lines.append(f"[HIGHEST NET PROFIT SURPLUS] DAY: {max_increment['day']}, AMOUNT: SGD {max_increment['amount']} ")
    elif is_decreasing:
        lines = ["[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN PREVIOUS DAY"]
        lines.append(f"[HIGHEST NET PROFIT DEFICIT] DAY: {max_decrement['day']}, AMOUNT: SGD {max_decrement['amount']} ")    
    else:
        lines = []
        for amount, day in deficits:
            lines.append(f"[NET PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD {amount}")

        # Sort the deficits list by the amount, then get the top 3 deficits
        deficits.sort()
        top_3_deficits = deficits[-3:]
        lines.append(f"[HIGHEST NET PROFIT DEFICIT] DAY: {top_3_deficits[-1][1]}, AMOUNT: SGD {top_3_deficits[-1][0]}")
        lines.append(f"[2ND HIGHEST NET PROFIT DEFICIT] DAY: {top_3_deficits[-2][1]}, AMOUNT: SGD {top_3_deficits[-2][0]}")
        lines.append(f"[3RD HIGHEST NET PROFIT DEFICIT] DAY: {top_3_deficits[-3][1]}, AMOUNT: SGD {top_3_deficits[-3][0]}")
    return lines
