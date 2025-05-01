# Write a program that determines the lowest common multiple(LCM) between two numbers entered by the user.

# Prompt the user for two numbers
num1=int(input("Enter the first number :"))
num2=int(input("Enter the second number :"))


# Find the mximum of the two numbers
maximum=max(num1,num2)

# Calculate the LCM
while True:
    if maximum % num1 ==0 and maximum %num2 ==0:
        lcm=maximum
        break
    maximum+=1

# Display the LCM
print("LCM OF ",num1,num2,"is :",lcm)