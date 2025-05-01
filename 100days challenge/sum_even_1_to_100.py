# Write a program that calculates and displays the sum of even numbers form 1 to 100 using a repeating loop.


# Initialize variables
sum_of_evens=0
num=2

# Use a while loop to iterate until num reaches 100
while num <=100:
    sum_of_evens+=num
    num+=2
print("The sum of even numbers form 1 to 100 is :",sum_of_evens)