#Advent of Code 2020: Puzzle 7, Part 1

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
        value4 = " ".join(value3[1:-1])
        #print(value4)
        cleaned_data.append(value4)
    splitted[key] = cleaned_data
#print(splitted)

#3 Function that counts children with gold bag inside
def has_gold(bag):
    content = splitted[bag]
    if "shiny gold" in content:
        return True
    elif ["other"] == content:
        return False
    else:
        children_have_gold = []
        for child in content:
            children_have_gold.append(has_gold(child))
        return any(children_have_gold)

#print(has_gold("light red"))
counter = 0
for key,value in splitted.items():
    counter += has_gold(key)
    #print("key: ", key, "\has gold: ", has_gold(key))
print("How many bag colors can eventually contain at least one shiny gold bag? ", counter)