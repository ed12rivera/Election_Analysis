# Add our dependencies.
import csv
import os

 # Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Initialize vote count variable equal to zero.
total_votes = 0

# Create a list for the candidate options
candidate_options = []

# Declare empty dictionary to hold each candidate's votes
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)

    for row in file_reader:
        # Count all the votes
        total_votes += 1
        # Add candidate names to candidate list
        candidate_name = row[2]

        # Add the candidate to the candidate list if they are not already in it
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Initialize candidate votes to zero and begin counting
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:
    # Print election results to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the election results to the text file.
    txt_file.write(election_results)

    # Find percentage of votes each candidate received
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print candidate results and write to the text file
        print(candidate_results)

        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate

    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n")

    # Print winning candidate and write to the text file.
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)


