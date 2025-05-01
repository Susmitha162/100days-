# Make a program that reads three numbers, and displays them on the screen in ascending order.

number1=float(input("enter the first number :"))
number2=float(input("Enter the second number :"))
number3=float(input("Enter the third number :"))


# Create a list to store the numbers
numbers=[number1,number2,number3]

# Sort the list in ascending order
numbers.sort()


# Display the numbers in ascending order
print("The numbers inn ascending order are:",numbers)




