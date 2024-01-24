from overheads import overheads
from cash_on_hand import cash_on_hand
from profit_and_loss import profit_and_loss


lines = cash_on_hand() + profit_and_loss() + overheads()

# Write the lines to a file called summary_report.txt
with open("summary_report.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")

