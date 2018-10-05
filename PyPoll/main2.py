#import dep's
import csv
import os

#define file(s)
election_data = os.path.join("Resources","election_data.csv")
election_output = os.path.join("Resources","Election_results.txt")

#open csv and pass over header row
with open(election_data,newline='') as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=',')
    next(csv_reader,None)
    
    #set var's
    vote_total = 0
    canCount = 0
    winvalue = 0
    candidates = {}
    
    #loop for incremental values/dic
    for row in csv_reader:
        vote_total = vote_total + 1

        #add candidate name to dic/define and assign 1st vote
        if row[2] not in candidates:
            canCount = 1
            candidates[row[2]]= {'vote_count':canCount,'vote_pct':0.000}

        #increment votes after candidate name/key is added    
        elif row[2] in candidates:
            canCount = candidates[row[2]]['vote_count'] + 1
            candidates[row[2]]['vote_count'] = canCount
    
    #calculate pct of votes
    for candidate in candidates:
        candidates[candidate]["vote_pct"] = round((candidates[candidate]['vote_count']/vote_total)*100,3)
    
    #assign winner var by finding largest vote count
    ##couldnt figure out how to return key for max nested dic --ask later
    for c in candidates:
        if candidates[c]["vote_count"] > winvalue:
            winner = c
            winvalue = candidates[c]["vote_count"]
    
    #---testing---#
    #print(winner)
    #print(candidates)
    #print(candidates["vote_pct"])
    #print(candidtes["vote_count"])

    #Set var to print heading output --could assign multple or append?
    output = (f'\nElection Results'
            f'\n------------------------------'
            f'\nTotal Votes: {vote_total}'
            f'\n------------------------------')
    
    #loop through all candidates and append to output
    for each in candidates:
        #---testing---#
        #print(each)
        output = output + (f'\n{each}: {candidates[each]["vote_pct"]}%'
                f' ({candidates[each]["vote_count"]})')
    
    #append footer to output
    output = output + (f'\n------------------------------'
            f'\nWinner: {winner}'
            f'\n------------------------------\n')
    
    #write output to new file using defined file  
    with open(election_output,"w") as output_file:
        output_file.write(output)
    
    #print to terminal
    print(output)