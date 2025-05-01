# Prompt the user input enter integer
number =int(input("Enter the integer :"))



# Check if the number is divisible by 3 and 5
if number % 3==0 and number%5==0:
    result="divisible by 3 and 5"
else:
    result="not divisible by 3 and 5"


# Display the result
print(f"The number {number} is {result}.")