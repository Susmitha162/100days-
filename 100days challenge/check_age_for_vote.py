# Make a program that asks for a porson's age and display wheather they are aligible for vote or not

# Prompt the user for their age 
age=int(input("Enter your age :"))

# Check if the given age is eligible or not 
if  age>=18:
    print("you are eligible for the vote ")
else:
    print("you are not eligible for the vote")