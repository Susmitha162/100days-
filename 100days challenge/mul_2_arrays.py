# Write a program that reads two arrays of integers with the same size and displays a new array with the elements resulting from the multiplication of the corresponding elements of the two arrays.


# Prompt the user for the size of the arrays 
size =int(input("Enter the size of the array :"))


# Initialize the empty lists to store the lements of the arrays 
array1=[]
array2=[]



# Read the elements of the first array
print("Enter the elements of the first array1 :")
for i in  range(size):
    element=int(input("Enter the element  {} :".format(i+1)))
    array1.append(element)




# Read the elements of the second array
print("Enter the elements for the array 2:")
for i in range(size):
    element=int(input("Enter the element  {}:".format(i+1)))
    array2.append(element)



# Initialize an empty list to strore the resulting array
result_array=[]


# Calculate the multiplication of the corresponding elements
for i in range(size):
    result=(array1[i])*(array2[i])
    result_array.append(result)





# Display the resulting array
print("Resulting array:",result_array)

