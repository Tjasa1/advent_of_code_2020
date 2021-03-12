#Advent of Code 2020: Puzzle 1, Part 1

#0 import the data
with open("day1.txt", "r") as inputfile:
    data = inputfile.read()

#1 Make a list
numbers = data.split("\n")

#2 make the list into numbers
numbers = [int(i) for i in numbers]
print(numbers[0:10])

# 3 Two loops with a sum = 2020
for n in numbers:
    for m in numbers:
        if n + m == 2020:
            print(n, m)
            #4 multiply these numbers
            print("Find the two entries that sum to 2020; what do you get if you multiply them together? ",n * m)