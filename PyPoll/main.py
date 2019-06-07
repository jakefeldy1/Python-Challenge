import os 
import csv

csvpath = os.path.join("..", "PyPoll", "election_data.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    header = next(csvreader)
    votes = 0
    Khan = 0
    Correy = 0 
    Li = 0
    OTooley = 0
    for row in csvreader:
#total number of votes
        votes += 1

# print(votes): this is printing the total number of votes
#calculating total number of votes for each candidate
        if row[2] == "Khan":
            Khan += 1
        elif row[2] == "Correy":
            Correy += 1
        elif row[2] == "Li":
            Li += 1
        elif row[2] == "O'Tooley":
            OTooley += 1
# print(Khan)
# print(Correy)
# print(Li)
# print(OTooley)

#Making percentages of the vote so I can then print it off later
khan_percent = round(((Khan / votes)*100), 2)
correy_percent = round(((Correy / votes)*100), 2)
li_percent = round(((Li / votes)*100), 2)
otooley_percent = round(((OTooley / votes)*100), 2)

#printing off all of the results

print("Election Results")
print("-------------------")
print(f"Total Votes: {votes}")
print("-------------------")
print(f"Khan: {khan_percent}% ({Khan})")
print(f"Correy: {correy_percent}% ({Correy})")
print(f"Li: {li_percent}% ({Li})")
print(f"O'Tooley: {otooley_percent}% ({OTooley})")
print("-------------------")

#create output for the text file
output = (f"Election Results\n"
f"-------------------\n"
f"Total Votes: {votes}\n"
f"-------------------\n"
f"Khan: {khan_percent}% ({Khan})\n"
f"Correy: {correy_percent}% ({Correy})\n"
f"Li: {li_percent}% ({Li})\n"
f"O'Tooley: {otooley_percent}% ({OTooley})\n"
f"-------------------\n")

#opening text file with the output
with open("output.txt", "w") as the_file:
    the_file.write(output)

#doing an if statement that says whoever has the highest votes is the winner, then printing their name into the terminal 
if Khan > Correy and Khan > Li and Khan > OTooley:
     print("Winner: Khan")
elif Correy > Khan and Correy > Li and Correy > OTooley:
     print("Winner: Correy")
elif Li > Khan and Li > Correy and Li > OTooley: 
     print("Winner: Li")
elif OTooley > Khan and OTooley > Correy and OTooley > Li: 
     print( "Winner: O'Tooley")
     print("-------------------")