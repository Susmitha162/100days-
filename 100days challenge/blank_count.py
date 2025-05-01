# Make a program that receives a sentance and displays the amount of blank spaces present in it.


# Prompt the user input as the sentance
sentance=input("Enter the sentance :")


# Initialize the variable to count the number of blank spaces
count=0

# Iterate over each charecter in the sentance
for char in sentance:
    # Check if the charecter is a blank space
    if char==" ":
        count+=1
print("Number of the blank spaces :",count)





# another method to finding the white spaces in the sentance

sentance=input("Enter the sentance :")

# USE count method to count the number spaces present in the sentance
count=sentance.count(" ")


# displays the result
print("Number of the blank spaces :",count)