# Write a program that reads an array of integers and display how many times a specific number appears in the array.


# Prompt the user for the size of the array 
n=int(input('Enter the size of the array :'))


# Initialize an empty list to store the array elements
array=[]


# Read the elements of array from the user
for i in range(n):
    element=int(input("Enter the element {} is :".format(i+1)))
    array.append(element)


# Prompt the searching element of the user input 
target=int(input("Enter  searching element : "))


# Count the target number is frequancy is
count=0
for element in array:
    if element==target:
        count+=1


# Display the count of the target frequancy
print("The number", target,"appears", count,"times in the array.")