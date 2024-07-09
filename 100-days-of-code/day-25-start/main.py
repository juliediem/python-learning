# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))

import pandas

# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
#
# temp_series = pandas.Series(data_dict["temp"])
# temp_list = temp_series.to_list()
#
# avg_temp = temp_series.mean()
# max_temp = temp_series.max()
# # print(temp_list)
# # print(avg_temp)
# # print(max_temp)
#
# print(data)
# # This allows us to filter for a row
# print(data[data.temp == max_temp])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
# # # TODO Convert Celsius to Farenheit (celsius× 9/5) + 32
# # print(monday.temp[0] * 9 / 5 + 32)
#
# # Create a dataframe from scratch
#
# data_dict = {
#     "students": ["Amy","James","Angela"],
#     "scores": [76,78,80]
# }
#
# new_data = pandas.DataFrame(data_dict)
# new_data.to_csv("new_data.csv")

import pandas
df = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240624.csv")
primary_fur_color = df["Primary Fur Color"]

# df.height.nunique()

fur_count = df["Primary Fur Color"].value_counts()
fur_count.to_csv("squirrel_count.csv")