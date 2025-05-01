# Create  a program that reads a word and displays the number of vowels present in it.

# Prompt the user input as the word
word=input("Enter the word :")


# Define the vowels 
vowels=['a','e','i','o','u']


# Initialize the variable to count the number of the vowels 
count=0

# Iterate over each charecter in the word
for char in word:
    if char.lower() in vowels:
        count+=1
# Display  the count of the number of the vowels present in the input word

print("Number of the vowels in the given word is  :",count)