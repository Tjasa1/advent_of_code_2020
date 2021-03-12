#Advent of Code 2020: Puzzle 2, Part 2

#1 import the data
with open("day2.txt", "r") as inputfile:
    data = inputfile.read()

#2 split on lines
passwords_split_on_lines = data.split("\n")
#print(passwords_split_on_lines[:3])

#3 split on spaces
counter = 0
for entry in passwords_split_on_lines:
    #3.1 splits amount, letter and password
    amount_letter, letter, password= entry.split()
    #print(amount_letter, letter, password)
 
    #3.2 Assigns positions of the letters and splits on dash:
    position_1, position_2 = amount_letter.split("-")
    position_1 = int(position_1)
    position_2 = int(position_2)
    #print("positions:", position_1, position_2)

 
    #3.3 Removes the colon of letter
    true_letter = letter.replace(':','')
    #print(true_letter)
    
    #3.4 one of the positions in the password must contain the given letter:
    position_1_in_password = password[(position_1-1)]
    position_2_in_password = password[(position_2-1)]
    #print(password, position_1_in_password, position_2_in_password)
   
    if position_1_in_password == true_letter or position_2_in_password == true_letter:
        print(position_1_in_password, position_2_in_password, true_letter)
        #print(position_1_in_password == true_letter or position_2_in_password == true_letter)
        if position_1_in_password == true_letter and position_2_in_password == true_letter:
            #print(position_1_in_password == true_letter and position_2_in_password == true_letter)
            pass
        else:
            counter += 1
       
print("final counter:", counter)