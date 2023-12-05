#Import libraries 
import string

#AOC 2023 Day 3 Part 1

#Creating string that involves punctuation
punct = string.punctuation
#Strip the . character since it doesn't belong to the symbol list in the excersice
punct = punct.replace('.','')

#function to part 1
def part_numbers(actual_line,previous_line,next_line):
    #making a list of the symbols and it's index for each line
    actual_sym_list = [i for i, word in enumerate(actual_line) if word in punct]
    previous_sym_list = [i for i, word in  enumerate(previous_line) if word in punct]
    next_sym_list = [i for i, word in enumerate(next_line) if word in punct]
    #Merging all the list to know the general indexing of each symbol in the three lines
    merged_list = actual_sym_list + previous_sym_list + next_sym_list
    set_symbols = set(merged_list)
    #replacing all the symbols to . since that is the separator for each line
    actual_int = actual_line.translate({ord(c): '.' for c in punct})
    #making a list for each number in the actual line
    num_list = [word for word in actual_int.split('.') if word.isdigit()]
    #variable for indexing each number
    x = 0
    #variable for answer
    power = 0
    #loop through each number in the list
    for i in num_list:
        #length of number to know the end index of the number
        y = len(i)
        #start index of the number in the line
        x = actual_line.index(i,x)
        #list of the range between the start index and end index of the number
        range_list = list(range(x-1,x+y+1))
        x += 1
        #making a set
        set_range = set(range_list)
        #if there's an intersection between general indexes of the symbols and the range of the number, then add it's value
        if set_range.intersection(set_symbols):
            power += int(i)
        
    return power

#Opening the input file in read mode and read all the lines in a variable
file = open('input.txt','r')
lines = file.readlines()
i = 0
lines_len = len(lines)-1
#Variable for answer
total_power = 0
#Doing a while loop through each line to call the function using actual line, previous line and the next line, since we need to take into account all cardinal points
while i <= lines_len:
    line_actual = lines[i].strip()
    line_previous = ''
    line_next = ''

    #making if statements to avoid any overflow of indexes in the lines list
    if i > 0:
        p = i - 1
        line_previous = lines[p].strip()
    if i < lines_len:
        n = i + 1
        line_next = lines[n].strip()
    total_power += part_numbers(line_actual,line_previous,line_next)
    i += 1

print('Day 3 part 1 answer: ',total_power)

#AOC 2023 Day 3 Part 2
#Creating the function using the same parameters as part 1. This time, we need to evaluate every * character in the line instead of the numbers
def gear_numbers(actual_line,previous_line,next_line):
    #for this part only the * character is necessary
    symbols_rpl = punct.replace('*','')

    actual_line = actual_line.translate({ord(c): '.' for c in symbols_rpl})
    previous_line = previous_line.translate({ord(c): '.' for c in symbols_rpl})
    next_line = next_line.translate({ord(c): '.' for c in symbols_rpl})
    
    #creating list for all the numbers in each line and making a general index list for them
    previous_list = []
    previous_int = [word for word in previous_line.replace('*','.').split('.') if word.isdigit()]
    idx = 0
    for i in previous_int:
        idx = previous_line.index(i,idx)
        previous_list.append([idx,i,len(i)])
        idx += len(i)

    actual_list = []
    actual_int = [word for word in actual_line.replace('*','.').split('.') if word.isdigit()]
    idx = 0
    for i in actual_int:
        idx = actual_line.index(i,idx)
        actual_list.append([idx,i,len(i)])
        idx += len(i)

    next_list = []
    next_int = [word for word in next_line.replace('*','.').split('.') if word.isdigit()]
    idx = 0
    for i in next_int:
        idx = next_line.index(i,idx)
        next_list.append([idx,i,len(i)])
        idx += len(i)

    #return variable
    gear_line = 0

    #Loop through each character looking for every *
    for i in enumerate(actual_line):
        if i[1] == '*':
            #indexing the *
            actual_index = i[0]
            prev_index = actual_index - 1
            next_index = actual_index + 1
            #making a list for the index range
            range_list = list(range(prev_index,next_index+1))
            #making a general list of all the numbers that are adjacent to the *
            previous_numbers = [int(i[1]) for i in previous_list if any(x in range_list for x in range(i[0],i[0]+i[2]))]         
            actual_numbers = [int(i[1]) for i in actual_list if any(x in range_list for x in range(i[0],i[0]+i[2]))]              
            next_numbers = [int(i[1]) for i in next_list if any(x in range_list for x in range(i[0],i[0]+i[2]))]            
                        
            adjacent_list = previous_numbers + actual_numbers + next_numbers
            #if the adjacent numbers are exactly 2, then add their product to the answer
            if len(adjacent_list) == 2:
                gear_line += (adjacent_list[0]*adjacent_list[1])

    return gear_line

i = 0
total_gear = 0

#call the second part funcion for each line
while i <= lines_len:
    line_actual = lines[i].strip()
    line_previous = ''
    line_next = ''
    if i > 0:
        p = i - 1
        line_previous = lines[p].strip()
    if i < lines_len:
        n = i + 1
        line_next = lines[n].strip()
    comp = total_gear
    total_gear += gear_numbers(line_actual,line_previous,line_next)
    i += 1
    
print('Day 3 part 2 answer: ',total_gear)

#Closing file from memory
file.close()