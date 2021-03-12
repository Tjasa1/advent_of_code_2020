#Advent of Code 2020: Puzzle 1, Part 2

#0 import the data
with open("day1.txt", "r") as inputfile:
    data = inputfile.read()

#1 Make a list
numbers = data.split("\n")

#2 make the list into numbers
numbers = [int(i) for i in numbers]
#print(numbers[0:10])

#3 Two loops with a sum = 2020
# for n in numbers:
#     for m in numbers:
#         for x in numbers:
#             if n + m + x == 2020:
#                 print(n, m, x)
#                 #4 multiply these numbers
#                 print(n * m * x)

for (i,n) in enumerate(numbers):
    for (j,m) in enumerate(numbers[i+1:]):
        for x in numbers[j+2:]:
            if n + m + x == 2020:
                print(n, m, x)
                #4 multiply these numbers
                print(n * m * x)
