# Write a program that prompts the user for a number and displays the fibonacci sequence up to the given number using a repeating loop.


# P prompt the user input as the integer
number=int(input())


# initialize variables
previous_number=0
current_number=1



# Displays the fibonacci sequence up to the given number

while current_number<=number:
    print(current_number, end=" ")

# creating the next fibonacci number
    next_number=previous_number+current_number

# Update previous_number and current_number
    previous_number=current_number
    current_number=next_number
