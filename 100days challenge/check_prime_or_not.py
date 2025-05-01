# Write a program that asks the user for a number N and says whether it is prime or not.

# prompt the user input as integer 
num=int(input("Enter the number :"))

for i in range(2,num+1):
    if num%i==0:
        break
if num==i:
    print(num,"is prime number")
else:
    print(num,"is not a prime number")