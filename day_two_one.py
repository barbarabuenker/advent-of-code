# Advent of Code 2023: Day Two, Part One

# Given: 
## A file containing information on the games:
## Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag.
# Return: The sum of the IDs of all possible games given the number of red (= 12), green (= 13) and blue (= 14) cubes in the bag.

# 1 - Read input file
input = open("day_two_one_input.txt", "r")

# 2 - Create list that includes the IDs of all games as well as a list that includes the IDs of all impossible games
# Create an empty variable for game ID, as well as empty lists for the IDs of all games and the IDs of all impossible games (= n(red) > 12, n(green) > 13, n(blue) > 14) to be used in for loop
game_ID = 0
all_games = []
impossible_games = []

# for line in input file ...
for line in input:
    # ... add 1 to the game ID variable to calculate current game ID ...
    game_ID = game_ID + 1
    # ... and add the current game ID to the list of all games
    all_games.append(game_ID)
    #  ... for item in line (which is created by the following code to strip line from \n and separate items by semicolons - although I'm not sure this is even necessary!)
    for item in (line.strip()).split(";"):
        # ... for every position in this item ...
        for index in range(len(item)):
            # ... if item positions equal "blue" ...
            if item[index:index+4] == "blue":
                # ... check if the number of blue cubes is larger then 14 ...
                if item[index-3:index-1] not in [" 0", " 1", " 2", " 3", " 4", " 5", " 6", " 7", " 8", " 9", "10", "11", "12", "13", "14"]:
                    # ... if that's the case (= the game is impossible), append the game number to the list of impossible games
                    impossible_games.append(game_ID)
            # ... if item positions equal "red" ...
            if item[index:index+3] == "red":
                # ... check if the number of blue cubes is larger then 12 ...
                if item[index-3:index-1] not in [" 0", " 1", " 2", " 3", " 4", " 5", " 6", " 7", " 8", " 9", "10", "11", "12"]:
                    # ... if that's the case (= the game is impossible), append the game number to the list of impossible games
                    impossible_games.append(game_ID)
            # ... if item positions equal "red" ...
            if item[index:index+5] == "green":
                # ... check if the number of blue cubes is larger then 13 ...
                if item[index-3:index-1] not in [" 0", " 1", " 2", " 3", " 4", " 5", " 6", " 7", " 8", " 9", "10", "11", "12", "13"]:
                    # ... if that's the case (= the game is impossible), append the game number to the list of impossible games
                    impossible_games.append(game_ID)

# 3 - Find out possible games and calculate sum of IDs of possible games
# Create an empty list for all possible games as well as an empty variable for the sum of possible game IDs to be used in the for loop
possible_games = []
sum_of_possible_game_IDs = 0

# for every item in the list of all games (that was created in the first for loop!) ...
for item in all_games:
    # ... if the item is not part of the list of all impossible games (that was created in the first for loop!) ...
    if item not in impossible_games:
        # ... add the integer of the item to the sum of possible game IDs
        sum_of_possible_game_IDs = sum_of_possible_game_IDs + int(item)

# to get the result, print the sum of possible game IDs
print(sum_of_possible_game_IDs)

# 4 - Close input file
input.close()

# Limitations:
## Code works only if each game is listet on a new line and if game IDs are ordered with the first game starting at the first line.
## Code works only if the elve draws cubes in the range of two digit numbers (i. e. < 100)