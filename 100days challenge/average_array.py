# Write a program that reads an array of integers and displays the average of the elements.

# Prompts the user for the number of elements in the array
n=int(input("Enter the number of the elements :"))


# Initialize the empty list to store the elements
array=[]


# Read the elements form the user
for i in range(n):
    element=int(input("Enter the element {} :".format(i+1)))
    array.append(element)


# Calculate the sum of the elements 
sum=0
for elements in array:
    sum+=element


# Calculate the average 
average=sum/n


# Display the average
print("Average :",average)

