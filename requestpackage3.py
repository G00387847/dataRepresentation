import requests
import json
from xlwt import *

url = "https://api.github.com/users/andrewbeattycourseware/followers"
response = requests.get(url)
data = response.json()

#Get the file name for the new file to write
filename = 'githbusers.json'
if filename:
    
    #Writing JSON data

    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

#write to excel file
w = Workbook()
ws = w.add_sheet('githbusers')
ws.write(0,0, "data1")
row = 1
col = 1
ws.write(row,col, "data")

w.save('githbusers.xls')


    

