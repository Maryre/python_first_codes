import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_07-2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)

    # for index, column_header in enumerate(header_row):
    #    print(index, column_header)

    #get data of rainfall
    dates, rainfalls = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            rainfall = float(row[19])
        except ValueError:
            print(current_date, 'missing data')
        else:

            dates.append(current_date)
            rainfalls.append(rainfall)



#plot data
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, rainfalls, c='blue', alpha=0.5)
plt.fill_between(dates, rainfalls, facecolor='blue', alpha=0.2)


#format plot
plt.title("Rainfall in Death Valley in 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Rainfalls in', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()


