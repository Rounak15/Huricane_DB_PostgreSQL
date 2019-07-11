from urllib import request
import os

# Retrieve the webpage as a string
response = request.urlopen("https://dq-content.s3.amazonaws.com/251/storm_data.csv")
csv = response.read()

# Save the string to a file
csvstr = str(csv).strip("b'")

lines = csvstr.split("\\n")

if os.path.isfile("storm_data.csv"):
	os.remove("storm_data.csv")

f = open("storm_data.csv", "w")
for line in lines:
   f.write(line + "\n")
f.close()