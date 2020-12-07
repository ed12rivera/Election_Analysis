# Election_Analysis

## Project Overview
I am assisting a Colorado Board of Elections employee with performing an audit of a recent local election.  The audit is to be performed in a manner that can be automated and used for future election audits.  I have been tasked to find the following information for the election:

1.  Total number of votes cast in the election.
2.  A complete list of candidates who received votes in the election.
3.  The total number of votes each candidate received.
4.  The percentage of votes each candidate received.
5.  The winner of the election based on popular vote.

Additionally, there is some county date that is needed for the audit.

1.	The voter turnout for each county.
2.	The percentage of votes from each county out of the total votes.
3.	The county with the highest turnout.

## Resources 
- Data Source: election_results.csv
- Software: Python 3.7, Visual Studio Code 1.51

## Summary
The analysis of the election show:
- There were 369,711 votes cast.
- The counties and their results were:
  - Jefferson with 10.5% of the votes with 38,855 votes.
  - Denver with 82.8% of the votes with 306,055 votes.
  - Arapahoe with 6.7% of the votes with 24,801 votes.
- The county with the highest voter turnout:
  - Denver with 306,055 votes.
- The candidates in the election were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23% of the vote with 85,213 votes.
  - Diana DeGette received 73.8% of the vote with 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the vote with 11,606 votes.
-The winner of the election was:
  -Diana DeGette with 73,8% of the vote, a total of 272,892 votes.

## Challenge Summary
This script does not require any user input and has no arbitrary values within it.  All the variables used to track county and candidate results are initialized as blanks or zeros and are filled only with values from our data source.  This is necessary for automizing the process because there are no values within the script that need to be changed for future election audits.  The only changes that may be needed are updating the data source we are pulling data from and updating the text file where we want future results printed.  Once the data source is updated the script will work exactly as it did for this one; looping through the rows to get a total vote count, a list of all unique candidates and counties, and counts for each candidate and county, regardless of the number of candidates or counties.

Depending on the data available we could track any number of metrics with just a few changes to the code.  Early voting was more important and widespread in this 2020 Presidential election than probably any previous elections.  With this in mind, if we have the date on which each Ballot ID cast a vote, we could find some interesting results for the election in Colorado.  We could write a similar loop to the one used to add up the votes in each county to find how many people voted early and how early they generally voted.  We could also see if there are any patterns of specific candidates receiving more or fewer early votes than others and see how those patterns align with any beliefs or ideas the candidates have.   

With a few extra additions our code should even be able to track elections for multiple states.  With a data source similar to our current one, but with multiple states data we should be able to loop through the states as well.  After line 44 in our code we would write a for loop that starts with the first state in our data source then runs lines 47 -78 to get the candidates list, candidate results, county list, and country results for the state and then loop back and go on to the next state in the data source.  We would also start a loop after line 83 to print out the winner for each state and end at the end of our current code. 

