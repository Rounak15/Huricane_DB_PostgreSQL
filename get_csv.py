import io 
import csv
from urllib import request


reponse = request.urlopen('https://dq-content.s3.amazonaws.com/251/storm_data.csv')

reader = csv.reader(io.TextIOWrapper(reponse))



# with open("storm_data.csv","w+") as writer:
# 	writer.writelines(reader)
