import csv
import os


#Assign a variable for the file to load and the path.

file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to load a file from a path.

file_to_save = os.path.join("analysis", "election_analysis.txt")


# Declare the total vote accumulator, candidate list and an empty dictionary
total_votes = 0
candidate_options = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker

winning_candidate = ""
winning_count = 0
winning_percentage = 0

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Open the election results csv file to read only
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
 
     # Read the header row.
    headers = next(file_reader)
    

# Print each row in the CSV file.
    for row in file_reader:
        #Add the total vote count
        total_votes += 1
        #print(row)
        # Get the candidates names from each row
        candidate_name = row[2]
        
        # Check to see if the name is not in the list, then add it in order to retrive the unique names, rather than every row
        if candidate_name not in candidate_options:
            # Add those names to the indicates list above
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] +=1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Save the results to the text file
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    for candidate_name in candidate_votes:
        
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print the candidate name and percentage of votes.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes})\n")

   
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage 
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
        
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary) 

    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)


