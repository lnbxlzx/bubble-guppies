import csv
from pathlib import Path


def overheads():
    # File path to csv file, cwd means current working directory
    fp = Path.cwd()/"csv_reports/Overheads.csv"

    # Open the file in read mode, encoding is set to UTF-8, newline is set to "" to prevent blank lines
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        # Skip the first row of the csv file, since it is header
        next(reader) 
        overheads=[] 

        # Loop through the rows in the csv file and append them to the overheads list as a list of 2 elements, category and percentage
        for row in reader:
            overheads.append([row[0],row[1]]) 

    # Intialize the highest_percentage and highest_percentage_category variables
    highest_percentage = 0
    highest_percentage_category = None

    # Loop through the overheads list and compare the percentage to the highest_percentage, if it is higher, 
    # then set the highest_percentage to the current percentage and set the highest_percentage_category to the current category
    for row in overheads:
        # Convert the percentage from string to float and compare it to the highest_percentage
        if highest_percentage_category is None or float(row[1]) > highest_percentage:
            highest_percentage = float(row[1])
            highest_percentage_category = row[0]
    
    # Return the highest_percentage_category and highest_percentage as a list
    return [f"[HIGHEST OVERHEADS] {highest_percentage_category.upper()}: {highest_percentage}%"]
