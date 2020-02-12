import matplotlib.pyplot as plt
import csv
from datetime import datetime
#death valley
open_file = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")
###lets try it for sitka now hopefully it works
open_file2 = open("sitka_weather_2018_simple.csv", "r")

csv_file2 = csv.reader(open_file2, delimiter=",")

#death valley header row
header_row = next(csv_file)
#try for sitka
header_row2 = next(csv_file2)
print(type(header_row))

for index,column_header in enumerate(header_row):
    print(index,column_header)

highs = []
dates = []
lows = []
names = []

#sitka new lists
highs2 = []
dates2 = []
lows2 = []
names2 = []
for row in csv_file:
    try:
        high=int(row[header_row.index("TMAX")])
        low=int(row[header_row.index("TMIN")])
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        name=str(row[header_row.index("NAME")])
    except ValueError:
        print("Missing data for {}".format(current_date))
    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)
        names.append(name)

#attempt 2 for sitka

for row in csv_file2:
    try:
        high2=int(row[header_row2.index("TMAX")])
        low2=int(row[header_row2.index("TMIN")])
        current_date2 = datetime.strptime(row[2], '%Y-%m-%d')
        name2=str(row[header_row2.index("NAME")])
    except ValueError:
        print("Missing data for {}".format(current_date))
    else:
        highs2.append(high2)
        lows2.append(low2)
        dates2.append(current_date2)
        names2.append(name2)


#fig = plt.figure()
#Plot for Death Valley
fig, (ax1, ax2) = plt.subplots(2,1)

ax2.plot(dates, highs,color = 'red', alpha=0.5)
ax2.plot(dates, lows, color = 'blue', alpha=0.5)

ax2.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

ax2.set_title(names[1], fontsize= 16)
ax2.set_xlabel("", fontsize= 10)
ax2.set_ylabel("Temperature (F)", fontsize= 12)
ax2.tick_params(axis='both',which="major",labelsize=12)

#plot for sitka weather
ax1.plot(dates2, highs2,color = 'red', alpha=0.5)
ax1.plot(dates2, lows2, color = 'blue', alpha=0.5)

ax1.fill_between(dates2,highs2,lows2,facecolor='blue',alpha=0.1)

ax1.set_title(names2[1], fontsize= 16)
ax1.set_xlabel("", fontsize= 10)
ax1.set_ylabel("Temperature (F)", fontsize= 12)
ax1.tick_params(axis='both',which="major",labelsize=12)


fig.autofmt_xdate()

plt.show()

