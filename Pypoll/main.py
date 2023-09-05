import csv
import os

# Set the path to the CSV file within the new directory
# csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")
csvpath = ".\\Pypoll\\Resources\\election_data.csv"


# Initialize variables
total_votes = 0
candidates = []
winner = ""
vote_count = {}

# Read the CSV file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip the header row
    header = next(csvreader)

    # Iterate through each row in the CSV file
    for row in csvreader:
        # Count total votes
        total_votes += 1
        candidate = row[2]

        # If candidate is not in the list, add them
        if candidate not in candidates:
            candidates.append(candidate)
            vote_count[candidate] = 0

        # Count the vote for the candidate
        vote_count[candidate] += 1

# Find the winner
winner = max(vote_count, key=vote_count.get)

# Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Initialize a variable to store the results for export
results = []

# Iterate through candidates and calculate percentages
for candidate in candidates:
    percentage = (vote_count[candidate] / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({vote_count[candidate]})")
    print(f"{candidate}: {percentage:.3f}% ({vote_count[candidate]})")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Save the analysis results to a text file in the analysis folder
pypoll_result = ".\\python-challenge\\Pypoll\\analysis\\"
output_file = os.path.join(pypoll_result, "election_results.txt")

with open(output_file, "w") as textfile:
    textfile.write("Election Results\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("-------------------------\n")
    for result in results:
        textfile.write(result + "\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Winner: {winner}\n")
    textfile.write("-------------------------\n")

print(f"Results saved to {output_file}")


