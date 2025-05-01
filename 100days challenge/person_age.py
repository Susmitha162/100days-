# Check a program that asks for a person's age and displays whether they are a child (0-12 years old),teenager(13-17 years old),adult(18-59 years old), or elderly(60 years old or older).

# Prompt the user input as integer 
age=int(input("Enter your age :"))



# Check the age range and assign the corresponding category

if age<=12:
    category="child"
elif age<=17:
    category="teeanger"
elif age<=59:
    category="adult"
else:
    category="elderly"




# Dispaly the result
print(f"You are a {category}.")