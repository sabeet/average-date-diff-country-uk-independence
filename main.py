import pandas as pd
from datetime import datetime, timezone

#function for datetime
def utcTime(month, day):
    return datetime(2000, month, day)

# Open text file for reading
with open('data.txt') as f:
    data = f.read()

# Create lists to store country and date values
countries = []
dates = []

# Split text into lines
lines = data.split("\n")
for line in lines:
    # Split each line on ": " to get country and date
    parts = line.split(": ")
    countries.append(parts[0])
    dates.append(parts[1][0:-5].split(' '))
    # dates.append(parts[1][0:-5])

# Create dataframe
df = pd.DataFrame()
df['Country'] = countries
df['Date'] = dates

#print(df)
dateDict = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

for i in range(len(dates)):
    dates[i] = [int(dates[i][0]), dateDict[dates[i][1]]]

dates.sort(key= lambda x : (x[1] , x[0]))

diff = []

for i in range(0,len(dates)-2):
    x = abs(utcTime(int(dates[i][1]), int(dates[i][0])) - utcTime(int(dates[i+1][1]), int(dates[i+1][0])))
    diff.append(x.days)

# print( utcTime(int(dates[0][1]), int(dates[0][0])) - utcTime(int(dates[1][1]), int(dates[1][0])))
print(sum(diff)/len(diff))