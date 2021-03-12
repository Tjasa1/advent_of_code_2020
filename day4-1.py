# Advent of Code 2020: Puzzle 4, Part 1

# 1 import the data
with open("day4-1.txt", "r") as inputfile:
    data = inputfile.read()

# 2 Separate data per passport.
# 2.1 Separate data based on an empty line (2 new line characters --> 2x \n)
splitted_data_1 = data.split("\n\n")
# print(splitted_data_1)

# 2.2 Group the data for each passport (data is in different lines (\n) or with whitespace (" "), regular expression split)
listed_passport = []
# 3 Make dictionary of passports:
# 3.1 Split every item on ":"Dictionary {key:value, }
# 3.2 Assign every left item to the key and every right item to the value
for potential_passport_data in splitted_data_1:
    # splitted_data.append(potential_passport_data.split())
    potential_passport = {}
    # print("\n")
    # this for loop splits big string on spaces or new lines.
    for field in potential_passport_data.split():
        key, value = field.split(":")
        potential_passport[key] = value
        #print(potential_passport)
    listed_passport.append(potential_passport)
#print(listed_passport)

# 4 Determine what is valid passport
# 4.1 It must include all the data except "cid" information
expected_fields = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
]

# 4.2 Loop through the passports in order to determine valid ones
number_of_valid_pas = 0
for potential_passport in listed_passport:
    counter = 0
    for i in expected_fields:
        if i in potential_passport:
            counter += 1
    # 4.2.1 Count and return the amount of valid passports
    if counter == 7:
        number_of_valid_pas += 1
print("In your batch file, how many passports are valid?", number_of_valid_pas)