# Create a program that reads an array of integers and checks that all elements are even.



# Prompt the user input as the size of the array
size=int(input("Enter the size of the array :"))


# Initialize the empty array to store the elements of the array
array=[]


# Read the elements of the array 
for i in range(size):
    element=int(input("Enter the element :".format(i+1)))
    array.append(element)


# Flag to track if all elements are even
all_even=True



# Check if all elements aare even
for element in array:
    if element%2!=0: 
        all_even=False
        break



# Display the result
if all_even:
    print("All elements are even.")
else:
    print("Not all elements are even.")














