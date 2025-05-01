# the difference between the terms is less than 0.001.


import math
# Prompt the user for the value of x
x=float(input("Enter the value of x :"))
 

term=1.0
sum=1.0
n=1

while abs(term)>=0.001:
    term *=x/n
    sum+=term
    n+=1

# Caluculate e^x using the math library's exponentialfunction
math_result=math.exp(x)


# Display the calculated result and the math library's result

print("Custom calculation :",sum)
print("math.exp :",math_result)