# Write a program that asks for the name of a day week and displays whether it is a weekday (Monday to friday)


# Prompt the user input enter day
day=input("Enter the day :")

# Convert the lowercase for case-insensitive comparision 
day=day.lower()


# Check whether the given day is weekend or weekday 
if day == "saturday" or day=="sunday":
    result="Weekend"
else:
    result="Weekday"


# Display the result
print(f"{day.capitalize()} is a {result}.")