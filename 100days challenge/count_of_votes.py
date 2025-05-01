# Make a program that reads the age of three people and how many of then are eligible for vote

age1=int(input("Enter the age of the first person :"))
age2=int(input("Enter the age of the second person :"))
age3=int(input("Enter the age of the third person :"))



# Initialize a variable
count_of_vote=0


# Check if each person is of age elible for vote
if age1>=18:
    count_of_vote+=1
if age2>=18:
    count_of_vote+=1
if age3>=18:
    count_of_vote+=1



# Display the count of votes 
print("Out of the three peoples :",count_of_vote)







