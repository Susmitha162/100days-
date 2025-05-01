# Create a program thatr reads an array of intergers and the second largest element in the array.



# Prompt the user for the size of the array
n=int(input("Enter the size of the array :"))



# Initailize an empty list to store the array elements 
array=[]


# Read the elements of the array form the user 
print("Enter the elements for the array :")
for i in range(n):
    element=int(input("Enter element {} :".format(i+1)))
    array.append(element)


# Initialize variable to store the largest and second largest elements

largest=float('-inf')
second_largest=float('-inf')


# Find the largest and second largest elements 
for element in array:
    if element>largest:
        second_largest=largest
        largest=element
    elif element>second_largest and element!=largest:
        second_largest=element



# Diplay the second largest element 
print(" Second largest element:",second_largest)

