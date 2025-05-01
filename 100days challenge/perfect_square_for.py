# Write a program that prompts the user for two numbers A and B displays all numbers between A and B

# prompt the user input as integers
A=int(input("Enter the first number :"))
B=int(input("Enter the second number :"))

# Determine the strating ending values of the for loop
start=min(A,B)
end=max(A,B)


# Iterating the loop 
for i in range(start,end+1):
    print(i,end=" ")
print()