#write a program that calculates and displays the value of the power of a number entered by the user raised to an exponent also entered by the user ,using repition loops


#prompt the user input as the number the exponent
base=int(input("enter the base number :"))
exponent=int(input("enter the exponent number :"))

# initialize the result variable to hold the calculated the value
result=1


#use the for loop interate from 1 to the exponent
for _ in range(1, exponent+1):
    result*=base

# Display the calculated result
print("The result of",base,"raised to the power of",exponent,"is :" ,result)

