# Write a program that reads  a 3x3 matrix and calculates the average of the values present in the even positions (sum of the even indices) of the matrix.


# Initialize the 3x3 matrix 
matrix=[]


# Read the values for the matrix
print(" Enter the values of the 3x3 matrix :")
for _ in range(3):
    row=[]
    for _ in range(3):
        value=int(input("Enter the value :"))
        row.append(value)
    matrix.append(row)



# Initialize the sum and count of the position
sum_even=0
count_even=0


for i in range(3):
    for j in range(3):
        if (i+j)%2==0:
            sum_even+=matrix[i][j]
            count_even+=1


# Calculate the average of the values present in the even positions 
average_even=sum_even/count_even



# Display the average of the values present in the even positions 
print("Average of values at even positions is :",average_even)






