import csv
import os


# Read storm_data file and modify data to suitable format 
rows = []
with open("storm_data.csv",'r',newline='') as f:
		reader = csv.reader(f)
		next(reader)
		rows = [row for row in reader]

rows.pop()
for row in rows:
	row[1:4] = ['-'.join(row[1:4])]
	row[2] = row[2][0:2] + ':' + row[2][2:4] + ':' + '00' 
	row[1:3] = [' '.join(row[1:3])]
	row[10] = str(row[10]).replace("\\r","")


# Delete temp file if exists and create a new one with modified data
if os.path.isfile("to_load.csv"):
	os.remove("to_load.csv")

with open("to_load.csv","w", newline='') as f:
	wr = csv.writer(f)
	wr.writerows(rows)


# print output to_load.csv record

rows_toload = []
with open("to_load.csv",'r') as f:
		reader = csv.reader(f)
		rows_toload = [row for row in reader]
print(rows_toload[0])