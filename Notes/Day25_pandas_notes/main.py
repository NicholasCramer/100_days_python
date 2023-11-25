import pandas

# import csv

# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     # skip header row
#     next(data, None)
#     for row in data:
#         temperatures.append(int(row[1]))
#         print(row)
#
#     print(temperatures)

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# avg_temp = data["temp"].mean()
# print(avg_temp)
#
# max_temp = data["temp"].max()
# print(max_temp)
#
# # Get data in columns
# print(data["condition"])
# print(data.condition)
#
# # Get data in rows
# print(data[data.day == "Monday"])
#
# # row of data that had the highest temp
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Nick"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# # save to csv file
# data.to_csv("new_data.csv")

# Squirrel Data
# How many squirrels of each color?
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231125.csv")
gray_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

squirrel_data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

print(squirrel_data_dict)

df = pandas.DataFrame(squirrel_data_dict)
df.to_csv("squirrel_count.csv")
