# Make a program that reads the scores of two tests and whether the student passed(score greater than or equal to 6) or failed (score less than 6) in each of the tests.

# Prompt the user to enter the score of the  tests

score1=float(input("Enter the score of the first test:"))
score2=float(input("Enter the score of the second test:"))

# Check if the student passed or failed in each test
if score1>=6:
    print("The student passed the first test.")
else:
    print("The student failed the first test.")

if score2>=6:
    print("The student passed the second test.")
else:
    print("The student failed the second test.")






