# Write a program that calculates the series below up to the tenth element.
# Maclaurin series

#e^x=1+x+x^2/2!+x^3/3!+x^4/4!+...............

import math
 
# Prompt the user for the value of x
x=float(input("Enter the value of the x :"))

# Initailize the sum and the term
term=1
sum=1

# Calculate the series up to the element
for n in range(1,11):
    term*=x/n
    sum+=term


# Display the result 
result=math.exp(x)
print("Approximation of e^x :",sum)
print("Actual value of e^x :",result)
