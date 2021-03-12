#Advent of Code 2020: Puzzle 4, Part 2

# 1 import the data
with open("day4-1.txt", "r") as inputfile:
    data = inputfile.read()

# 2 Separate data per passport.
# 2.1 Separate data based on an empty line (2 new line characters --> 2x \n)
splitted_data_1 = data.split("\n\n")
#print(splitted_data_1)

# 2.2 Group the data for each passport 
listed_passport = []
# 3 Make dictionary of passports:
# 3.1 Split every item on ":"Dictionary {key:value, }
# 3.2 Assign every left item to the key and every right item to the value
for potential_passport_data in splitted_data_1:
    # splitted_data.append(potential_passport_data.split())
    potential_passport = {}
    # print("\n")
    # this function splits big string on spaces or new lines.
    for field in potential_passport_data.split():
        key, value = field.split(":")
        potential_passport[key] = value
        # print(potential_passport)
    listed_passport.append(potential_passport)
#print(listed_passport)

#Stricter rules:
#    byr (Birth Year) - four digits; at least 1920 and at most 2002.
#    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
#    hgt (Height) - a number followed by either cm or in:
#        - If cm, the number must be at least 150 and at most 193.
#        - If in, the number must be at least 59 and at most 76.
#    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
#    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#    pid (Passport ID) - a nine-digit number, including leading zeroes.
#    cid (Country ID) - ignored, missing or not.")

# if in the passport
# and if it is valid int he passport
def valid_birth_year(birth_year):
    return 1920 <= int(birth_year) <= 2002

# issue year
def valid_issue_year(issue_year):
    return 2010 <= int(issue_year) <= 2020

# expiration year
def valid_expiration_year(expiration_year):
    return 2020 <= int(expiration_year) <= 2030

# height
def valid_height(height):
    if height.endswith("cm"):
        return 150 <= int(height[0:-2]) <= 193
    elif height.endswith("in"):
        return 59 <= int(height[0:-2]) <= 76
    else:
        return False

# hair color
def valid_hair_color(hair_color):
    listy = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
    ]
    if hair_color[0] == "#" and len(hair_color) == 7:
        for character in hair_color[1:]:
            if character not in listy:
                return False
        return True
    return False

# eye color
def valid_eye_color(eye_color):
    potential_eye_color = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return eye_color in potential_eye_color

# Passport ID
def valid_passport_id(passport_id):
    if len(passport_id) == 9:
        return passport_id.isdigit()
    return False

# 4 Determine what is valid passport
# 4.1 It has all the data except cid is optional. It connects functions above with the rules.
expected_fields = [
    ["byr", valid_birth_year],
    ["iyr", valid_issue_year],
    ["eyr", valid_expiration_year],
    ["hgt", valid_height],
    ["hcl", valid_hair_color],
    ["ecl", valid_eye_color],
    ["pid", valid_passport_id],
]

# 4.3 Loop through the passports
# 4.4 Count the number of valid passports
number_of_valid_pas = 0
for potential_passport in listed_passport:
    counter = 0
    for field, validator in expected_fields:
        if field in potential_passport and validator(potential_passport[field]):
            counter += 1
    # 5 Return the amount of valid passports
    if counter == 7:
        number_of_valid_pas += 1
print("Count the number of valid passports - those that have all required fields and valid values. In your batch file, how many passports are valid?", number_of_valid_pas)

