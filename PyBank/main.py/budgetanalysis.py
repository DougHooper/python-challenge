# import modules

import csv
import os

# source to read revenue data
fileLoad = os.path.join("budget data.csv")

outputFile = os.path.join("budgetanalysis.txt")

# print(fileLoad)

totalMonths = 0 # initializse the ttoal months to 0
totalBudget = 0 # initialize the total revenue to 0
monthlyChanges = [] # initialize the list of monthly changes
months = []          # initialize the list of months

with open(fileLoad) as budgetData:
    #create a csv reader object
    csvreader = csv.reader(budgetData)

    # read the header row
    header = next(csvreader)

    firstRow = next(csvreader) #to then go down the row from header

  # increment the count of the total months
    totalMonths += 1

        # add on to the total amount of revenue
    totalBudget += float(firstRow[1])

    # establish the previous budget
    previousBudget = float(firstRow[1])

    for row in csvreader:
        # increment the count of the total months
        totalMonths += 1

        # add on to the total amount of revenue
        totalBudget += float(row[1])

        # calcualte net change
        netChange = float(row[1]) - previousBudget

        # update the previous revenue
        previousBudget = float(row[1])

        #add on to the list of monthly changes
        monthlyChanges.append(netChange)

        # add the first month that a change occurred
            #month is in index 0
        months.append(row[0])

        # Calculate the average net change per month
        averageChangeperMonth = sum(monthlyChanges) / len(monthlyChanges)

        greatestIncrease = [months[0], monthlyChanges[0]]
        greatestDecrease = [months[0], monthlyChanges[0]]

# Calculate the greatest increase 

# Calculate the greatest decrease
for m in range(len(monthlyChanges)):

    if(monthlyChanges[m] > greatestIncrease[1]):

        greatestIncrease[1] = monthlyChanges[m]

        greatestIncrease[0] = months[m]

    
    if(monthlyChanges[m] < greatestDecrease[1]):

        greatestDecrease[1] = monthlyChanges[m]

        greatestDecrease[0] = months[m]


# start generating the output
output = (
    "Financial Analysis\n"
    "---------------------\n"
    f"\nTotal Months = {totalMonths} \n"
    f"\tTotal Budget = $ {totalBudget:,.2f} \n"
    f"\tAverage Change Per Month = $ {averageChangeperMonth:,.2f} \n"
    f"\tGreatest Increase = {greatestIncrease[0]} Amount ${greatestIncrease[1]:,.2f} \n" 
    f"\tGreatest Decrease = {greatestDecrease[0]} Amount ${greatestDecrease[1]:,.2f} \n" 
    )

print(output)


with open(outputFile, "w") as textFile:
    textFile.write(output)