#Advent of Code 2020: Puzzle 3, Part 2

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

#5 Function where you can input skiing pattern (e.g. 3 characters to the right and 1 down)
#5.1 Initial position
def skiing(x_step,y_step):
    x = 0
    y = 0
    amount_of_trees = 0
    while y < slope_height:
        #5.2 Moves x characters to the right and y down
        if true_slope[y][x] == "#":
            amount_of_trees += 1   
        x += x_step
        #5.3 Checks if the end of the slope width is reached. Then x goes back to position 0.
        if x >= slope_width:
            x = x - slope_width 
        y += y_step
        #print(x,y)
    return amount_of_trees

#6 Number of trees encountered for skiing in the following patterns (e.g. [1,1] means 1 right, 1 down...)
skiing_versions = [[1,1],[3,1],[5,1],[7,1],[1,2]]
multiplication_list = 1

#7 For each of the skiing patterns the number of encounter trees is calculated.
for (i,n) in skiing_versions:
    multiplication_list *= skiing(i,n)

print("Listed slopes: \nRight 1 and down 1, \nRight 3 and down 1, \nRight 5 and down 1, \nRight 7 and down 1, \nRight 1 and down 2")
print("What do you get if you multiply together the number of trees encountered on each of the listed slopes?", multiplication_list)