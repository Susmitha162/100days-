# Write a program that asks the user for a number N and displays the sum of all numbers from 1 to N.

N=int(input("Enter a number :"))
sum_of_numbers=0
for num in range(1,N+1):
    sum_of_numbers+=num
print("The sum of numbers from 1 to",N,"is :",sum_of_numbers)