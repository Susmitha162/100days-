# Make a program that asks for two numbers and displays if the first is divisible by the second

# Prompt the two numbers
first_number=int(input("Enter the first number :"))
second_number=int(input("Enter the second number :"))


# Check the first number is divisible by second number 

if first_number%second_number==0:
    result="The first number is divisible by second number"
else:
    result="The first number is not divisible by second number"


# Display the result
print(result)