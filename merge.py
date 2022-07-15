from base64 import encode
import csv
import pandas as pd

d1 = []
d2 = []
data = []
with open("bright_stars.csv", 'r', encoding = 'utf8') as f: 
    csvReader = csv.reader(f)
    for i in csvReader:
        d1.append(i)

with open("units.csv", 'r', encoding = 'utf8') as f: 
    csvReader = csv.reader(f)
    for i in csvReader:
        d2.append(i)

h1 = d1[0]
h2 = d2[0]

data1 = d1[1:]
data2 = d2[1:]

h = h1+h2

for i in data1:
    data.append(i)

for i in data2:
    data.append(i)

with open("dataMerging.csv", 'w', encoding = 'utf8') as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(h)
    csvWriter.writerows(data)

df = pd.read_csv("dataMerging.csv")
df.tail(8)