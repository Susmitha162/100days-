# Create a program that prompts the user for a number and displays the table of that number using a loop.

for i in range(1,11):
    for j in range(1,11):
        product=i*j
        print(i,"X",j,"=",product)
    print("-"*20)