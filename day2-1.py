#Advent of Code 2020: Puzzle 2, Part 1

#1 import the data
with open("day2.txt", "r") as inputfile:
    data = inputfile.read()

#2 split on lines
passwords_split_on_lines = data.split("\n")
#print(passwords_split_on_lines[:3])

#3 split on spaces
counter = 0
for entry in passwords_split_on_lines[:5]:
    #3.1 splits amount, letter and password
    amount_letter, letter, password= entry.split()
 
    #3.2 Assigns min and maximum and splits on dash:
    x_min, x_max = amount_letter.split("-")
    x_min = int(x_min)
    x_max = int(x_max)

    #3.3 Removes the colon of letter
    true_letter = letter.replace(':','')
    
    #3.4 counts amount of letters in the password:
    letter_amount_in_password = password.count(true_letter)
    print("letter:", true_letter)
    print(password)
    print("x_min:",x_min,"x_max:", x_max)
    print("amount in password:",letter_amount_in_password)
    print("--------")
    if x_min <= letter_amount_in_password <= x_max:
        counter += 1
        print("counter:", counter)
    
print("final counter:", counter)