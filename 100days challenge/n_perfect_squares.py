# Create a program that displays the first N first perfect squares, where N is informed by the user , uing a loop.


# Prompt the user input as interger
N=int(input('Enter the value of the N ;'))
count=0
num=1
while count<N:
    square=num**2
    print(square,end=" ")
    count+=1
    num+=1
print()



