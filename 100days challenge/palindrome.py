# Write a program that reads a word and checks if it is a polindrome (if it can read backwards the sum way).


word=input("Enter the word :")
reverse=word[::-1]
if word==reverse:
    print("The given word is polindrome")
else:
    print("The given word is not a polindrome")





# Another method to solve
word=input("Enter the word :")
is_polindrome=True
for i in range(len(word)//2):
    if word[i]!=word[len(word)-1-i]:
        is_polindrome=False
        break
if is_polindrome:
    print('The given word is polindrome ')
else:
    print("The given word is not a polindrome")