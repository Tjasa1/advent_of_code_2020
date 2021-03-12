#Advent of Code 2020: Puzzle 5, Part 1

import math

#read the file
with open("day5-1.txt", "r") as inputfile:
    data = inputfile.read()

#splits seat codes in each line for the for loop
splitted_data = data.split()
#print(splitted_data)

Seat_ID_list = []
#for loop calculating the seatID
for seat in splitted_data:
    #minimum and maximum seat numbers
    minimum_row = 0
    maximum_row = 127
    left_seat = 0
    right_seat = 7
    # Decrypting the seat row code (e.g. for B and F in BFFFBBFRRR)
    for letter_1 in seat:
        if letter_1 == "B":
            minimum_row = math.ceil((minimum_row + maximum_row)/2)
            #print(minimum_row, maximum_row)
        if letter_1 =="F":
            maximum_row = math.floor((minimum_row + maximum_row)/2)
            #print(minimum_row, maximum_row)   
    Seat_row = minimum_row
    # Decrypting the seat column code (e.g. for R and L in BFFFBBFRRR)
    for letter_2 in seat:
        if letter_2 == "R":
            left_seat = math.ceil((left_seat + right_seat)/2)
            #print(left_seat)
        if letter_2 == "L":
            right_seat = math.floor((left_seat + right_seat)/2)
            #print(right_seat)
    Seat_column = left_seat
    # Calculates seat ID
    Seat_ID = Seat_row * 8 + Seat_column
    #print(Seat_ID)
    # Appends the Seat_ID
    Seat_ID_list.append(Seat_ID)
    
#prints the maximum seat_ID number
print("Maximum seat ID = ", max(Seat_ID_list))