# Write a program that prompts the user for a number and displays its divisors.


# Prompts the user for a number 
number =int(input("Enter the number :"))


# Display the divisors
print("Divisors of ",number,":")
for i in range(1,number+1):
    if number % i==0:
        print(i,end=" ")