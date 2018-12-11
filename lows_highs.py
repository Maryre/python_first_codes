import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)

    # for index, column_header in enumerate(header_row):
    #    print(index, column_header)

    #get date and high temprature from file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)
        low = int(row[3])
        lows.append(low)

    print(highs)

    #plot data

    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(dates, highs, c='red')
    plt.plot(dates, lows, c='blue')

    #plot format
    plt.title("Daily high and low temperature, 2014", fontsize=24)
    fig.autofmt_xdate()
    plt.xlabel('', fontsize=16)
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()