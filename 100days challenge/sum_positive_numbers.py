# Write aprogram that reads numbers form the user until a negattive number is entered, and prints the sum of the positive numbers.

sum=0
while True:
    num=int(input('ENTER THE NUMBER :'))
    if num<0:
        break
    sum+=num
print("sum of the poditive numbers :",sum)
