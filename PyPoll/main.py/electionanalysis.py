import csv
import os

inputFile = os.path.join("..", "Resources", "election_data.csv")

outputFile = os.path.join("..", "Resources", "election_data.txt")

totalvotes = 0 
candidate = [] # list that holds the election data
candidateVotes = {} # dictionary that holds the votes for each candidate

with open(inputFile) as surveyData:

    csvreader = csv.reader(surveyData)

    header = next(csvreader)

    # print(header)

    for row in csvreader: 

        totalvotes +=1  #totalvotes = totalvoes + 1

        #check to see if the vote is in teh list of votes
        if row[2] not in candidate:
            #if the candidate is not in the list, add the candidate to the list of canddiates
            candidate.append(row[2])

            # add the value to the dictionaty as well
            # {"key": value}
            # start the count at 1 for the values
            candidateVotes[row[2]] = 1

        else: 
            candidateVotes[row[2]] += 1

print(candidateVotes)

for candidate in candidateVotes:
    # get the vote count and teh percentage fo teh votes
    votes = candidateVotes.get(candidate)
    votePct = (float(votes) / float(totalvotes)) * 100.00

    voteOutput = f"\t{candidate}: {votePct:.2f}% \n"
    print(voteOutput)

# create an output vatiabel to hold the output
output = (
    f"\n\nSurvey Results\n"
    f"-----------------------------------\n"
    f"\tTotal Votes: {totalvotes:,}"
)

print(output)

with open(outputFile, "w") as textFile:

    textFile.write(output)