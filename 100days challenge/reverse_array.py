# Write a program that reads an array of integers and displays the elements in reverse order


# Prompt the user input as array
arr=list(map(int,input().split()))
reverse_array=[]
for i in range(len(arr),-1,-1,-1):
    reverse_array.append(arr[i])
print("the reverse of the given array is :",)

