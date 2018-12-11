import csv

filename = 'sitka_weather_07-2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    # for index, column_header in enumerate(header_row):
    #    print(index, column_header)

    #get high temprature from file
    highs = []
    for row in reader:
        highs.append(row[1])

    print(highs)