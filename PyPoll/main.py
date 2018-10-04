import csv
import os

election_data = os.path.join("Resources","election_data.csv")

with open(election_data,newline='') as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=',')
    next(csv_reader,None)
    #Total Votes
    vote_total = 0
    candidates = []
    vote_pct = {}
    vote_cnt ={}
    for row in csv_reader:
        vote_total = vote_total + 1
        if row[2] not in candidates:
            candidates.append(row[2])
            vote_cnt[row[2]] = 0
        if row[2] in candidates:
            vote_cnt[row[2]] = vote_cnt[row[2]]+1
    for candidate in candidates:
        vote_pct[candidate] = (vote_cnt[candidate]/vote_total)

    # Test
    print(vote_total)
    print(candidates)
    print(vote_cnt)
    print(vote_pct)