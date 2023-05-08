import csv

import pandas

'''
with open("weather_data.csv") as weather_data:
    data = weather_data.readlines()
    print(data)
'''

'''with open("weather_data.csv") as weather_data:
    data = csv.reader(weather_data)
    temperatures = []
    for row in data:
        print(row)
        if row[1] != 'temp':
            temperatures.append(int(row[1]))

    print(temperatures)'''
'''
import pandas
data = pandas.read_csv("weather_data.csv")
print(data["temp"])
temperature_data = data["temp"]

data_dict = data.to_dict()
#print(data_dict)

temp_list = data["temp"].to_list()
days = len(temp_list)

sum_temps = 0
for temps in temperature_data:
    sum_temps += temps

average_temp = sum_temps / days

average_temp = sum(temp_list) / len(temp_list)
print(average_temp)

print(data["temp"].mean())
print(data["temp"].max())

# Get data in columns
print(data["condition"])
print(data.condition)

# Get data in rows
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp.iloc[0])
monday_temp = (monday_temp * 9 / 5) + 32
print(monday_temp)'''

# Squirrel challenge

squirrels_df = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels = len(squirrels_df[squirrels_df["Primary Fur Color"] == "Gray"])
red_squirrels = len(squirrels_df[squirrels_df["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(squirrels_df[squirrels_df["Primary Fur Color"] == "Black"])

data = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, red_squirrels, black_squirrels]
}
new_df = pandas.DataFrame(data)
new_df.to_csv("squirrel_count.csv")
print(new_df)