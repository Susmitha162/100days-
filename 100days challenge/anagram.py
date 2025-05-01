#Create a program that reads two words and checks if the second word is an angram of the first.


#Prompt the user input as the two words
w=input('Enter the first word :')
w1=input("Enter the second word :")


# Convert  both words to lowercase and remove whitespace
w=w.lower().replace(" ","")
w1=w1.lower().replace(" ","")



# Sort the two words the check the two words are equal are not 
if sorted(w) == sorted(w1):
    print("The second word is anagram of the first word ")
else:
    print("The second word is not a anagram of the second word ")