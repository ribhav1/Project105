#imports
import math
import csv

#opens csv file
with open('data.csv', newline='') as f:
    #reads csv file
    reader = csv.reader(f)

    #reads data line by line
    file_data = list(reader)

#makes it so only the only line with data, the first line, is the data
data = file_data[0]

#function to get mean
def mean(data):
    #counts number of data points
    number_of_data_points = len(data)

    sum_of_all_data_points = 0

    #gets sum of all data points
    for data_point in data:
        sum_of_all_data_points += int(data_point)

    #gets mean
    mean = sum_of_all_data_points / number_of_data_points

    #returns mean when function is called
    return mean

all_numbers_squared_list = []

for data_point in data:
    #finds difference of data point and mean
    difference_of_data_point_and_mean = int(data_point) - mean(data)

    #squares difference of data point and mean
    squared_difference = difference_of_data_point_and_mean**2

    #adds squared difference of data point and mean to a list
    all_numbers_squared_list.append(squared_difference)

sum_of_squared_numbers = 0

#loop to add all the numbers in the squared list together
for i in all_numbers_squared_list:

    #adds all numbers in the squared list together
    sum_of_squared_numbers = sum_of_squared_numbers + i

#takes sum of squared numbers and divides is by the number of data points minus one
sum_division_result = sum_of_squared_numbers / (len(data)-1)

#square roots the sum of squared numbers and divides is by the number of data points minus one
#gets standard deviation
standard_deviation = math.sqrt(sum_division_result)

#prints standard deviation
print(standard_deviation)