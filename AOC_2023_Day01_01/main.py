#AOC 2023 Day 1 Part 1

#Inialating variable that'll store the answer
x = 0

#Opening the input file in read mode and read all the lines in a variable
file = open('input.txt','r')
lines = file.readlines()

#Loop through all the lines
for line in lines:
    #Making a list of only characters that can be converted to int (only work for positive digits)
    line_list = [s for s in line if s.isdigit()]
    #Concatenatig first and last digit from the list and converting the result to an int
    number = int(line_list[0]+line_list[-1])
    #Adding the number to the answer
    x += number

print('Day 1 part 1 answer: ',x)

#AOC 2023 Day 1 Part 2

#Inialiting variable that'll store the answer
x = 0

#No need for opening file or creating lines list since they're already created in previous part

#Creating a dictionary for the char replacements. 
#Replacing each number in letters with it's digit counterpart and the first and last letter just in case another number shares one of those characters.
replace_chars = {
     'one': 'o1e'
    ,'two': 't2o'
    ,'three': 't3e'
    ,'four': 'f4r'
    ,'five': 'f5e'
    ,'six': 's6x'
    ,'seven': 's7n'
    ,'eight': 'e8t'
    ,'nine': 'n9e'
}

#Loop through all the lines
for line in lines:
    #Replacing characters
    [line := line.replace(a, b) for a, b in replace_chars.items()]
    #Making a list of only characters that can be converted to int (only work for positive digits)
    line_list = [s for s in line if s.isdigit()]
    #Concatenatig first and last digit from the list and converting the result to an int
    number = int(line_list[0]+line_list[-1])
    #Adding the number to the answer
    x += number
    
print('Day 1 part 2 answer: ',x)

#Closing file from memory
file.close()