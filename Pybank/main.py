# Importing dependencies
import os
import csv

csv_path = "Pybank\\Resources\\budget_data.csv"


# Initialize variables to store financial data
total_months = 0
total_profit_losses = 0
previous_profit_loss = 0
profit_loss_changes = []
dates = []

# Read the CSV file
with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    for row in csvreader:
        # Extract date and profit/loss values from each row
        date = row[0]
        profit_loss = int(row[1])

        # Calculate the total number of months and net total profit/loss
        total_months += 1
        total_profit_losses += profit_loss

        # Calculate the change in profit/loss since the previous month
        if total_months > 1:
            profit_loss_change = profit_loss - previous_profit_loss
            profit_loss_changes.append(profit_loss_change)
            dates.append(date)

        # Store the current profit/loss for the next iteration
        previous_profit_loss = profit_loss

# Calculate the average change in profit/loss
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Find the greatest increase and decrease in profit/loss
greatest_increase = max(profit_loss_changes)
greatest_increase_date = dates[profit_loss_changes.index(greatest_increase)]

greatest_decrease = min(profit_loss_changes)
greatest_decrease_date = dates[profit_loss_changes.index(greatest_decrease)]

# Print the financial analysis results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Save the analysis results to a text file in the analysis folder
pybank_result = ".\\python-challenge\\Pybank\\analysis\\"
output_file = os.path.join(pybank_result, "financial_analysis.txt")

with open(output_file, "w") as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${total_profit_losses}\n")
    textfile.write(f"Average Change: ${average_change:.2f}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

print(f"Results saved to {output_file}")
