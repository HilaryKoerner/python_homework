#PyBank homework

# import modules
import os
import csv

# Set path for file
bank_path = os.path.join('..', 'Resources', 'budget_data.csv')

#open the csv file
with open(bank_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#skip the header
    next(csvreader,None)

#### MONTH COUNT & P&L TOTAL ######
#Month Count - bootcamp python day one lecture (lists)
##Profit Loss Total - commbination of month count code and https://www.geeksforgeeks.org/sum-function-python/
    date = 0
    date = []
    total = []
    difference = {}
    
    prevrow = next(csvreader)
    prevdate = prevrow[0]
    prevpl = int(prevrow[1])

    # av_change = []
    # increase = []
    # decrease = []
    for row in csvreader:
        month_year=str(row[0])
        date.append(month_year)
        profit_loss=int(row[1])
        total.append(profit_loss)
        difference[row[0]] = int(row[1])-prevpl
        prevdate = row[0]
        prevpl = int(row[1])

    sum = sum(total, 0)
    month_count = len(date)
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(month_count))
    print("Total: $" + str(sum))
    # print(max(difference(row[1]))

    

