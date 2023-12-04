#Import libraries to read inputs
import os
import string

#AOC 2023 Day 3 Part 1

#Creating string that involves punctuation
punct = string.punctuation
#Strip the . character since it doesn't belong to the symbol list in the excersice
punct = punct.replace('.','')

#function
def part_numbers(actual_line,previous_line,next_line):
    actual_sym_list = [i for i, word in enumerate(actual_line) if word in punct]
    previous_sym_list = [i for i, word in  enumerate(previous_line) if word in punct]
    next_sym_list = [i for i, word in enumerate(next_line) if word in punct]
    
    merged_list = actual_sym_list + previous_sym_list + next_sym_list
    set_symbols = set(merged_list)
    
    actual_int = actual_line.translate({ord(c): '.' for c in punct})
    
    num_list = [word for word in actual_int.split('.') if word.isdigit()]
    x = 0
    power = 0

    for i in num_list:
        y = len(i)
        x = actual_line.index(i,x)

        range_list = list(range(x-1,x+y+1))
        x += 1
        
        set_range = set(range_list)

        if set_range.intersection(set_symbols):
            power += int(i)
        
    return power

#Opening the input file in read mode and read all the lines in a variable
file = open('input.txt','r')
lines = file.readlines()
i = 0
lines_len = len(lines)-1

total_power = 0

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
    total_power += part_numbers(line_actual,line_previous,line_next)
    i += 1

print('Day 3 part 1 answer: ',total_power)

#AOC 2023 Day 3 Part 2

def gear_numbers(actual_line,previous_line,next_line):
    symbols_rpl = punct.replace('*','')

    actual_line = actual_line.translate({ord(c): '.' for c in symbols_rpl})
    previous_line = previous_line.translate({ord(c): '.' for c in symbols_rpl})
    next_line = next_line.translate({ord(c): '.' for c in symbols_rpl})
    
    previous_list = []
    previous_int = [word for word in previous_line.replace('*','.').split('.') if word.isdigit()]
    idx = 0
    for i in previous_int:
        idx = previous_line.index(i,idx)
        previous_list.append([idx,i,len(i)])

    actual_list = []
    actual_int = [word for word in actual_line.replace('*','.').split('.') if word.isdigit()]
    idx = 0
    for i in actual_int:
        idx = actual_line.index(i,idx)
        actual_list.append([idx,i,len(i)])

    next_list = []
    next_int = [word for word in next_line.replace('*','.').split('.') if word.isdigit()]
    idx = 0
    for i in next_int:
        idx = next_line.index(i,idx)
        next_list.append([idx,i,len(i)])

    gear_line = 0

    for i in enumerate(actual_line):
        if i[1] == '*':
            actual_index = i[0]
            prev_index = actual_index - 1
            next_index = actual_index + 1

            range_list = list(range(prev_index,next_index+1))

            previous_numbers = [int(i[1]) for i in previous_list if any(x in range_list for x in range(i[0],i[0]+i[2]))]         
            actual_numbers = [int(i[1]) for i in actual_list if any(x in range_list for x in range(i[0],i[0]+i[2]))]              
            next_numbers = [int(i[1]) for i in next_list if any(x in range_list for x in range(i[0],i[0]+i[2]))]            
                        
            adjacent_list = previous_numbers + actual_numbers + next_numbers
            
            if len(adjacent_list) == 2:
                gear_line += (adjacent_list[0]*adjacent_list[1])

    return gear_line

i = 0
total_gear = 0
difference = []

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
    if i > 0:
        difference.append([i,total_gear,total_gear-comp])
    else:
        difference.append([i,total_gear,0])

def sort_li(sub_li):
 
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of 
    # sublist lambda has been used
    sub_li.sort(key = lambda x: x[2])
    return sub_li

for i in sort_li(difference):
    print(i)
print('Day 3 part 2 answer: ',total_gear)

#Closing file from memory
file.close()