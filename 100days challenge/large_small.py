# Write a program that prompts the user for a list of numbers,until the uer types the number zero, and displays the largest and smallest numbers in the list.


# Initialize variables
largest=float('-inf')
smallest=float('inf')
while True:
    number =float(input("Enter the number (enter 0 to stopp):"))
    if number ==0:
        break
    if number >largest:
        largest=number
    if  number<smallest:
        smallest=number
    

# Display the largest and smallest numbers
if largest != float('-inf') and smallest != float('inf'):
    print("largest number is :",largest)
    print("smallest number is :",smallest)
else:
    print(" no numbers were entered")