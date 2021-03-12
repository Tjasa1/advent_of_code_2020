#Advent of Code 2020: Puzzle 3, Part 1

#1 import the data
with open("day3.txt", "r") as inputfile:
    data = inputfile.read()

#2 Separates slope into the list of lines
slope_in_lines = data.split("\n")
slope_height = len(slope_in_lines)
#print(slope_height)

#3 Separates lines into lists of characters
true_slope = []
for lines in slope_in_lines:
    true_slope.append(list(lines))
    #print(true_slope)
    #print(len(characters_in_lines))

#4 Defines the width of slope
slope_width = len(true_slope[0])
#print(slope_width)

#5 Moves for 3 characters to the right and one down
#5.1 Initial position
x = 0
y = 0
amount_of_trees = 0
while y < slope_height:
    #5.2 Moves three characters to the right
    if true_slope[y][x] == "#":
        amount_of_trees += 1   
    x += 3
    if x >= slope_width:
        x = x - slope_width 
    y += 1
    #print(x,y)
     
print("Amount of trees: ",amount_of_trees)