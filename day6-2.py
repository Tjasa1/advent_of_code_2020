#Advent of Code 2020: Puzzle 6, Part 2

#1 import the data
with open("day6-1.txt", "r") as inputfile:
    data = inputfile.read()

#2 Separates answers into the list of lines
answ_group = data.split("\n\n")
#print(answ_group)

#3 counts the answers
answ_counter = 0
for i in answ_group:
    #3.1 splitting answers per group:
    list_of_answ = i.split()
    #3.2 Join the answers of people (strings) into one string
    string_of_answ = ''.join(list_of_answ)
    #3.3 Shows the amount of people answering
    length = len(list_of_answ)
    #print(string_of_answ, length)
    #3.4 Assigns unique letters in a string
    unique_letters = set(string_of_answ)
    #3.5 Loops through the unique letters (or questions in this code challange)
    for l in unique_letters:
        #3.5.1 Add 1 to the counter if every person answered yes to a question
        if string_of_answ.count(l) == length:
            answ_counter += 1          
print("Sum of the questions to which everyone in the group answered 'yes':",answ_counter)