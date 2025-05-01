# Write a program that reads numbers form the user until zero is entered, and displays the average of the numbers entered.

# Initialize variables
total=0
count=0

# Read numbers form the user zero is entered
while True:
    number=int(input("enter the number(enter 0 to stop :)"))
    # Check if the number is zero or not
    if number==0:
        break


    # Add the number to the total and increment the count 
    total+=number
    count+=1

# Calculate the average
if count>0:
    avarage=total//count
    print("Average :", avarage)
else:
    print("No numbers were entered.")