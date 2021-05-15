import csv
import os


#Assign a variable for the file to load and the path.

file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to load a file from a path.

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results csv file to read only
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
 
       
Print each row in the CSV file.
    for row in file_reader:
        print(row)

# Print the header row.
    # headers = next(file_reader)
    # print(headers)

# # Using the open() function with the "w" mode we will write data to the file.
# outfile = open(file_to_save, "w")

# # Write data to the file.
# outfile.write("Counties in the Election\n---------------\nArapahoe\nDenver\nJefferson")

# # Close the file

# outfile.close()