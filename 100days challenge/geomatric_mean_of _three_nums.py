import math
# promt the  three user input numbers
num1=float(input("enter the first number :"))
num2=float(input("enter the second number :"))
num3=float(input("enter the third number :"))

# Calculate products of the three numbers
product=num1*num2*num3
geomatric_mean=math.pow(product,1/3)

# Displays the result
print("Geomatric mean is :",geomatric_mean)