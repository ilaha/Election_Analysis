# Election_Analysis

## Project Overview

### Analysing the Colorado Board of Elections results to complete audit of recent local congressional election.

1. Calculate the total number of votes cast;
2. Get a complete list of candidates who received votes;
3. Calculate the total number of voyes each candidate won;
4. Calculate the percentage of votes each candidate won;
5. Determine the winner of the election based on popular vote



## Resources 

- Data Source: election_results.csv
- Software: Python 3.9.4


## Election Audit Results

### The analysis show that:
 
-There were *369,711* total votes in the election

- There are three candidates: 
  - Charles Casper Stockham;
  - Diana DeGette;
  - Raymon Anthony Doane

- The Candidate Results were: 
  - Charles Casper Stockham received 23.0% of the votes, 85213 number of votes
  - Diana DeGette received 73.8% and 272892 of votes
  - Raymon Anthony Doane received 3.1% and 11606 number of votes.

###_The Winner of the Election is Diana DeGette with 272, 892 votes which is %73.8 of the total votes._

- There are three counties and Denver has the highest percentage of votes, see the breakdown below:
 - Jefferson:  10.5% ( 38,855)
 - Denver:  82.8% ( 306,055)
 - Arapahoe:  6.7% ( 24,801)



## Election Audit Summary:

- The script that I wrote can be used for other elections as well with some minor modifications:
  - Change the CSV file that contains the correct election data;
  - Change the txt file name so the new data doesn't overwrite what we already have one the election_analysis test file.
  - In case you want to see lowest turnout county as well, add or update winning counry summary.

