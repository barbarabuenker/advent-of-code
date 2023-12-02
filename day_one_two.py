# Advent of Code 2023: Day One, Part Two

# Given: 
## A file containing consisting of lines of text;
## each line originally contained a specific calibration value. 
## On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number. 
## Some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".
# Return: The sum of all of the calibration values.

# 1 - Extract lines out of input file:
input = open("day_one_two_input.txt", "r")

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
        # ... if there is a spelled out number, append the actual number to the list of numbers
        if item[index:index+(len("zero"))] == "zero":
            numbers += "0"
        if item[index:index+(len("one"))] == "one":
            numbers += "1"
        if item[index:index+(len("two"))] == "two":
            numbers += "2"
        if item[index:index+(len("three"))] == "three":
            numbers += "3"
        if item[index:index+(len("four"))] == "four":
            numbers += "4"
        if item[index:index+(len("five"))] == "five":
            numbers += "5"
        if item[index:index+(len("six"))] == "six":
            numbers += "6"
        if item[index:index+(len("seven"))] == "seven":
            numbers += "7"
        if item[index:index+(len("eight"))] == "eight":
            numbers += "8"
        if item[index:index+(len("nine"))] == "nine":
            numbers += "9"
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