# Write a program that reads an array of integers and checks if they are in ascending order.


# Prompt the user for the size of the array
arr=list(map(int,input().split()))
ascending=True
for i in range(len(arr)-1):
    if arr[i]  > arr[i+1]:
        ascending=False
        break
if ascending:
    print("The given array is ascending order :")
else:
    print("The given array is not an asecding order :")


