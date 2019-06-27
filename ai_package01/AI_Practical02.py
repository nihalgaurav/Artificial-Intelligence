# we can load data by folling lib
# 1. load the csv files with the python std. lib.
# 2. load csv file with numpy
# 3. load csv file with pandas
#
#
# 1. load the csv files with the python std. lib.
import csv
filename = open('indians-diabetes.data.csv','r')
reader = csv.reader(filename, delimiter = ',')
lines = list(reader)
print("\n\nNo of rows : ",len(lines),"\n\n")

print(lines)
for l in lines :
    print("\n\n", l)


