#PyBank homework

# import modules
import os
import csv

# Set path for file
bank_path = os.path.join('.', 'Resources', 'budget_data.csv')

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
    for row in csvreader:
        month_year=str(row[0])
        date.append(month_year)
        profit_loss=int(row[1])
        total.append(profit_loss)
    sum_total = sum(total, 0)
    month_count = len(date)
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(month_count))
    print("Total: $" + str(sum_total))

#open the csv file
with open(bank_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#skip the header
    next(csvreader,None)
    #iterate through the date and p&l list and put into a dictionary
    difference = {}
    #this saves the previous row since it gets written over in python
    prevrow = next(csvreader)
    prevdate = prevrow[0]
    prevpl = int(prevrow[1])

    for row in csvreader:
        #this loops through so we can find the difference between months
        difference[row[0]] = int(row[1])-prevpl
        prevdate = row[0]
        prevpl = int(row[1])

    #this pulls out the key that is paired with the max/min value
    # https://www.geeksforgeeks.org/python-get-key-with-maximum-value-in-dictionary/
    keymax = max(difference, key= lambda x: difference[x])
    keymin = min(difference, key= lambda x: difference[x]) 
    
    # .values() pulls out just values from dictionary to find min and max https://www.geeksforgeeks.org/python-dictionary-values/
    # https://careerkarma.com/blog/python-typeerror-int-object-is-not-callable/ (used to debug "sum in not callable")
    #cast ROC to float before rounding https://www.programmersought.com/article/77535564709/
    pllist = difference.values()
    ROC = str(sum(pllist)/(month_count-1)) #difference is less one month
    float_ROC = float(ROC)
    round_ROC = round(float_ROC,2)
    print("Average Change: $" + str(round_ROC))
    increase = (max(pllist))
    print("Greatest Increase in Profits: " + keymax + " ($" + str(increase) + ")")
    decrease = (min(pllist))
    print("Greatest Decrease in Profits: " + keymin + " ($" + str(decrease) + ")")


# Specify the file to write to
output_path = os.path.join(".", "Analysis", "pybank_analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as writer:
    #https://realpython.com/read-write-files-python/ (this shows the writer.write() about half way down)
    writer.write("Financial Analysis" + '\n')
    writer.write("-------------------------" + '\n')
    writer.write("Total Months: " + str(month_count) + '\n')
    writer.write("Total: $" + str(sum_total) + '\n')
    writer.write("Average Change: $" + str(round_ROC) + '\n')
    writer.write("Greatest Increase in Profits: " + keymax + " ($" + str(increase) + ")" + '\n')
    writer.write("Greatest Decrease in Profits: " + keymin + " ($" + str(decrease) + ")" + '\n')
    