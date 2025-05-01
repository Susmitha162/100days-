# Write a program that prompts the user for a number N and displays all prime numbers less than N.


# P rompts the user for a number 
n=int(input("Enter the number :"))


# Iterate through the numbers from 2 to n
for i in range(2,n+1):
    if n%i==0:
        continue
    else:
        print(i,end=" ")

    