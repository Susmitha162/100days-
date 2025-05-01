# Create  a program that takes a sentance and replaces all the letters "a" with "e".


sentance=input("Enter the sentance :")
new_sentance=sentance.replace('a','e')
print("modified sentance is :",new_sentance)




# Another method 

sentance=input("Enter the sentance :")
new_sentance=""
for letter in sentance:
    if letter=='a':
        new_sentance+='e'
    else:
        new_sentance+=letter