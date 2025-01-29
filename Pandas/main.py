# # Extract data from a CSV
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file, delimiter=',')
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv('weather_data.csv')
#
# print(data[data.temp == data.temp.max()])
#
#
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # print(data["temp"].max())
# # # print the row named temp
# # print(data["temp"])

import pandas

# transformation csv en data frame
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241007.csv")

#  nombre de reference couleurs
grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrels, red_squirrels, black_squirrels)
#  Transformation en dictionnaire
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels, red_squirrels, black_squirrels]
}
#  Transformation en dataframe et en CSV
pandas.DataFrame(data_dict).to_csv("data_dict.csv")
