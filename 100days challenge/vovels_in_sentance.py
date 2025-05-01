# Write a program that prompts the user for a sentance and displays the number of vowels in the sentance


# Prompt the user for a sentance 
sentance=input("enter a sentance :")

# Initialize the vowel count to 0
vowel_count=0

# Iterate over each charecter in the sentence
for char in sentance:
    # Convert the charecter into lowercase 
    char_lower=char.lower()
      
    
    #check if the charecter is vowel or not
    if char_lower in 'aeiou':
        # Increament the vowel count
        vowel_count+=1
# Display the number of vowels in the sentence
print("Number of vowels :",vowel_count)