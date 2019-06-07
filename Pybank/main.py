import os 
import csv

csvpath = os.path.join("..", "PyBank", "budget_data.csv")

counter = 0
dates = []
averagechange = []
changeoverperiod = []
x = 0 

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    header = next(csvreader)
    
    for row in csvreader:
        counter += 1
        averagechange.append(int(row[1]))  
        dates.append(row[0])

#while loop to go through the csv and find the differences between each line.
#Sum those differences and divide that by the lenght to find the average change over entire period. 
while (x < (len(averagechange) - 1)):
        changeoverperiod.append(averagechange[x + 1] - averagechange[x])
        x += 1
change_over_period = round(sum(changeoverperiod) / len(changeoverperiod), 2)

#find greatest increase in profits and greatest decrease in profits
max_difference = max(changeoverperiod)
min_difference = min(changeoverperiod)

#find index of the max difference and min difference
index = changeoverperiod.index(max_difference)
indexmin = changeoverperiod.index(min_difference)

#use index found previously to associate max difference and min difference with the correct months
maxdiffmonth = dates[index + 1]
mindiffmonth = dates[indexmin + 1]

#make output for txt file
output = (f"Financial Analysis\n"
f"-------------------\n"
f"Total Months: {counter}\n"
f"Total:${sum(averagechange)}\n"
f"Average Change ${change_over_period}\n"
f"Greatest Increase in Profits: {maxdiffmonth} (${max_difference})\n"
f"Greatest Decrease in Profits: {mindiffmonth} (${min_difference})\n")

#create text file with the output
with open("output.txt", "w") as the_file:
    the_file.write(output)


#Print answer to terminal
print("Financial Analysis")
print("-------------------")
print(f"Total Months: {counter}")
print(f"Total:${sum(averagechange)}")
print(f"Average Change ${change_over_period}")
print(f"Greatest Increase in Profits: {maxdiffmonth} (${max_difference})")
print(f"Greatest Decrease in Profits: {mindiffmonth} (${min_difference})")