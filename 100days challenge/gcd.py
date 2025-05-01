# Write a program that determines the greatest common divisor (GDD) between two numbers entered by the user.



# Prompt the user for numbers 
num1=int(input("Enter the first number :"))
num2=int(input("Enter the second number :"))


# find the smallar number of the two numbers
smallar=min(num1,num2)

# Initailize the gcd variable
gcd=1


# Calculate the gcd
for i in range(1, smallar+1):
    if num1 % i==0 and num2%i==0:
        gcd=i

# Display the gcd
print("gcd of the ", num1, num1 ,"is :",gcd)
