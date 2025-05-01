# Write a program that takes a full name and displays the last name first.


# Prompt the user input as the full name
full_name=input("Enter the fullname:")

# split the full anme into a list of names using whitespaces 
names =full_name.split()

# Get the last name from the list 
last_name=names[-1]


#Displays the result
print(last_name)