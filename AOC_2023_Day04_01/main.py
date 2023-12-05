#AOC 2023 Day 3 Part 1 & 2

#Opening the input file in read mode and read all the lines in a variable
file = open('input.txt','r')
lines = file.readlines()

#Declaring variable for part 1
points = 0
#Declaring variable for part 2
scratch_cards = 0

#Dictionary for part 2 to keep track for the number of copies for each card
line_dict = {}
for i in range(0,len(lines)):
    line_dict.update({i:1})

#Loop through each line in the input
for line_number,line in enumerate(lines):
    #Looking for the separators in each line for the lists
    semi_cln_idx = line.index(':')
    bar_idx = line.index('|')

    #List of winning numbers
    winning_numbers = [word for word in line[semi_cln_idx:bar_idx].split() if word.isdigit()]
    #List of own numbers
    own_numbers = [word for word in line[bar_idx:-1].split() if word.isdigit()]
    #List of matching numbers and it's length
    point_numbers = [x for x in winning_numbers if x in own_numbers]
    point_len = len(point_numbers) 
    #Variable to part2
    scratch_cards += 1
    #Actual scratch card copies for the line    
    scratch_copies = line_dict.get(line_number)
    #If matching numbers are greater than 0 then sum points and scratch copies
    if point_len > 0:
        #Point formula is 2 ** (n-1)
        points += 2 ** (point_len-1)
        #Scratch cards takes into account the amount of copies the current card has
        scratch_cards += (point_len * scratch_copies)

    #Updating the dictionary to keep track of the next cards copies
    for i in range(line_number,line_number + point_len):
        line_copies = line_dict.get(i+1)
        line_dict.update({i+1:line_copies+(1*scratch_copies)})        
    

print('Day 4 part 1 answer: ',points)
print('Day 4 part 2 answer: ',scratch_cards)

#Closing file from memory
file.close()