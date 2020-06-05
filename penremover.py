#!python3

import csv
import pandas as pd

f1 = open('ronaldo_combined_practice.csv', 'r')
reader = csv.reader(f1)
new_rows_list = []

# f2 = open('messipens.csv', 'r')
# c2 = csv.reader(f2)
# datelist = list(c2)

with open('ronaldopens.csv', 'r') as f2:
    datelist = [row[0] for row in csv.reader(f2)]


next(reader)
print(datelist)

for host_row in reader:

    subtract = datelist.count(host_row[0])
    new_row = [host_row[0], int(host_row[1])-subtract, host_row[2]]
    new_rows_list.append(new_row)


f3 = open('ronaldo_combined_practice.csv', 'w')
writer = csv.writer(f3)
writer.writerows(new_rows_list)

f1.close()
f2.close()
f3.close()
