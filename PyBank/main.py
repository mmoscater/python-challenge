# Analyze Financial Data

#import classes
import os
import csv

filepath = os.path.join("Resources","budget_data.csv")

with open(filepath,newline='') as myfile:
    
    csvfile = csv.reader(myfile,delimiter=',')
    next(csvfile,None)
    mthCount = 0
    total = 0
    chg = 0
    lastMth = 0
    maxInc = 0
    minInc = 0
    for row in csvfile:

        if chg == 0:
            firstMth = int(row[1])
        lastChg = int(row[1])-lastMth
        chg = chg + lastChg
        mthCount = mthCount + 1
        total = total + int(row[1])
        if maxInc < lastChg:
            maxInc = lastChg
            maxMth = row[0]
        if minInc > lastChg:
            minInc = lastChg
            minMth = row[0]
        lastMth = int(row[1])
        

    chg = round((chg - firstMth)/(mthCount-1),2)
    analysis = (f'''
    Financial Analysis
    --------------------------------------------------
    Total Months: {mthCount}
    Total: ${total}
    Average Change: ${chg}
    Greatest Increase in Profits: {maxMth} (${maxInc})
    Greatest Decrease in Profits: {minMth} (${minInc})
    --------------------------------------------------
    ''')
    print(analysis)
    output = os.path.join("Resources","Financial_Analysis.txt")
    with open(output,"w") as newfile:
        newfile.write(f"{analysis}")