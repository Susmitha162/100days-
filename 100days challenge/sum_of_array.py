# Crate a program that reads as array of integers and displays the sum of all the elements..

# Prompt the user input for number of elements in the array
n=int(input("Enter the numberr of elements :"))


# Initialize an empty list to store the elements
array=[]


# Read the elements for the user 
for i in range(n):
    element=int(input("Enter element {}:".format(i+1)))
    array.append(element)


# Calculate the sum of all elements
sum=0
for element in array:
    sum+=element


# Display the sum of all the elements
print("Sum of all the elements :",sum)