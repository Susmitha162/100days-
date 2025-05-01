# Write a program that takes a full name and displays only the first name.



# Prompt the full name as the user input
full_name=input("Enter your full name :")


# Split the full name into a list of names using whitespace

names=full_name.split()
print(names)

#Get the first name from the list
first_name=names[0]

# Print the result of the first name 
print("First name is :",first_name)