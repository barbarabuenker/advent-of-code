# Advent of Code 2023: Day One, Part One

# Given:
## A file containing consisting of lines of text;
## each line originally contained a specific calibration value. 
## On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number. 
# Return: The sum of all of the calibration values.

# 1 - extract lines out of input file:
input = open("day_one_one_input.txt", "r")

list_of_lines = []

for line in input:
    list_of_lines.append(line)

input.close()

# 2 - Create a list of calibration numbers of each line
list_of_calibration_numbers = []

# for every item in list_of_lines ...
for item in list_of_lines:
    # ... create a list called numbers
    numbers = []
    # ... and at every position of the item ...
    for index in range(len(item)):
        # ... if the value at this position of the item is a number ...
        if item[index] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            # ... append the number to the list of numbers
            numbers += item[index]
    # ... form the calibration number by extracting the first and last number out of the list of numbers ...
    result = numbers[0] + numbers[-1]
    # ... and append the result to the list of calibration numbers
    list_of_calibration_numbers.append(result)

# 3 - Calculate the sum of calibration numbers
sum_of_calibration_numbers = 0

# for every item in the list of calibration numbers ...
for item in list_of_calibration_numbers:
    # ... make an integer out of the item and add it to the sum of calibration numbers
    sum_of_calibration_numbers = sum_of_calibration_numbers + (int(item))

print(sum_of_calibration_numbers)
