# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who receieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate
# 5. The winner of the election based on popular vote.

# Reading a file.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)

# Writing to a file.
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
# Write a list.
outfile.write("Counties in Election\n\nArapahoe\nJefferson\nDenver")

# Close the file
outfile.close()