#Advent of Code 2020: Puzzle 7, Part 2

#1 import the data
with open("day7.txt", "r") as inputfile:
    data = inputfile.read()

#2 
#split at the word "contains"
#2.1 Separates answers into the list of lines
outer_bag_amount = 0
list_of_bags = data.split("\n")
splitted = {}
for rule in list_of_bags:
    key, value = rule.split(" contain ")
    value2 = value.strip(".").split(", ")
    key = key[:-5]
    #print(key)
    cleaned_data = []
    for i in value2:
        value3 = i.split(" ")
        #print("value3", value3)
        if value3[0] == "no":
            number = 0
        else:            
            number = int(value3[0])
        value4 = " ".join(value3[1:-1])
        #print("value4", value4)
        cleaned_data.append([number, value4])
    splitted[key] = cleaned_data
#print("splitted: ",splitted)

#3 Function that counts children with gold bag inside
def count_contents(bag):
    content = splitted[bag]
    if [0, "other"] in content:
        return 1
    else:
        counter = 1
        for amount, child in content:
            counter += amount * count_contents(child)
        return counter

print("How many individual bags are required inside your single shiny gold bag?", count_contents("shiny gold")-1)