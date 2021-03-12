#Advent of Code 2020: Puzzle 6, Part 1

#1 import the data
with open("day6-1.txt", "r") as inputfile:
    data = inputfile.read()

#2 Separates answers into the list of lines
answ_group = data.split("\n\n")

#3 counts the answers
counter = 0
for i in answ_group:
    #3.1 Splits answers per group (separated by \n\n):
    list_of_answ = i.split()
    #3.2 Join the answers of several people (strings, separated by \n) into answers of the group (big string)
    string_of_answ = ''.join(list_of_answ)
    #3.3 Assigns only unique letters to the string
    differet_letters =  set(string_of_answ)
    #3.4 Shows and adds amount of different letters to the counter
    counts = len(differet_letters)
    #print(string_of_answ, differet_letters, counts)[:10]
    counter += counts
print("Sum of the questions to which anyone answered 'yes':",counter)