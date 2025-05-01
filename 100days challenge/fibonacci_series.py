# Write a program that prompts the user for a number and displys the fibonacci up to the given number using a repeating loop


# Promt the user input as the integer
number=int(input("enter the number for range :"))
 
a=0
b=1
for i in range(0,number):
    c=a+b
    a=b
    b=c
    print(c,end=" ")