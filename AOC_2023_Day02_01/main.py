#Import libraries to read inputs
import os

#AOC 2023 Day 2 Part 1

#Creating a function that'll resolve each line
def game_possible(line, red, green, blue):
    #Declaring ID Number of Game as 0 by default
    game_id = 0
    #Preparing the string to make it a list
    line = line.replace(';',',')
    line = line.replace(':',',')
    item_list = line.split(',')
    #Declaring booleans for each color
    red_possible = True
    green_possible = True
    blue_possible = True
    #Declaring the variable that'll store the game ID before each evaluation
    game = 0
    #Loop through each item on the list
    for i in item_list:
        #Taking the ID of the game if the item is the Game ID
        game_number_list = [int(word) for word in i.split() if word.isdigit() and 'Game' in i]
        game += sum(game_number_list)
        #Looking if the item is Red and evaluating if it passes the minimum
        red_number_list = [int(word) for word in i.split() if word.isdigit() and 'red' in i]
        if sum(red_number_list) > red:
            red_possible = False
        #Looking if the item is Green and evaluating if it passes the minimum
        green_number_list = [int(word) for word in i.split() if word.isdigit() and 'green' in i]
        if sum(green_number_list) > green:
            green_possible = False
        #Looking if the item is Blue and evaluating if it passes the minimum
        blue_number_list = [int(word) for word in i.split() if word.isdigit() and 'blue' in i]
        if sum(blue_number_list) > blue:
            blue_possible = False
    #If all the colors didn't pass the minimum, then assign the ID to the return value
    if red_possible and green_possible and blue_possible:
        game_id = game
   
    return game_id

#Declaring variables with each color
red = 12
green = 13
blue = 14

#Opening the input file in read mode and read all the lines in a variable
file = open('input.txt','r')
lines = file.readlines()
total_possible = 0
#Looping through all the lines to know if the game is possible and adding the return value
for line in lines:
    line_id = game_possible(line.strip(),red,green,blue)
    total_possible += line_id

print('Day 2 part 1 answer: ',total_possible)

#AOC 2023 Day 2 Part 2

#Creating a second function to call the game power
def game_power(line):
    #Declaring the return variable
    game_power = 0
    #Preparing the string to make it a list
    line = line.replace(';',',')
    line = line.replace(':',',')
    item_list = line.split(',')
    #Declaring each color variable
    red = 0
    green = 0
    blue = 0

    #Loop through each item on the list
    for i in item_list:
        #Evaluating the item if it has red and assigning it's value if it's the greater number than the color power
        red_number_list = [int(word) for word in i.split() if word.isdigit() and 'red' in i]
        if sum(red_number_list) > red:
            red = sum(red_number_list)

        #Evaluating the item if it has green and assigning it's value if it's the greater number than the color power
        green_number_list = [int(word) for word in i.split() if word.isdigit() and 'green' in i]
        if sum(green_number_list) > green:
            green = sum(green_number_list)

        #Evaluating the item if it has blue and assigning it's value if it's the greater number than the color power
        blue_number_list = [int(word) for word in i.split() if word.isdigit() and 'blue' in i]
        if sum(blue_number_list) > blue:
            blue = sum(blue_number_list)

    #Multiplying each color max power
    game_power = red * green * blue
   
    return game_power

#Declaring the answer variable
power_sum = 0

#Loop through each line in the file and adding each return value to the answer variable
for line in lines:
    line_power = game_power(line.strip())
    power_sum += line_power

print('Day 2 part 1 answer: ',power_sum)

#Closing file from memory
file.close()