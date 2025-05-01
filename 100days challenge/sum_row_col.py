# Write a program that fills a 4x4 matrix with random numbers and displays the sum of the values present in each row and in each column.


import random

# Create a 4x4 matrix filled with random numbers
matrix=[[random.randint(1,10) for _ in range(4)] for _ in range(4)]

for row in matrix:
    print(row)



# Initialize variables to store the sums of rows and columns
rows_sum=[0,0,0,0]
columns_sum=[0,0,0,0]


# Calculate the sum of the values in each row and column

for i in range(4):
    for j in range(4):
        # Update the sum of the i-th row 
        rows_sum[i]+=matrix[i][j]
        
        

        # Update the sum of the j-th column
        columns_sum[j]+=matrix[i][j]
        print(columns_sum[j])


# Diplays the sums of the rows 
print(" Sum of the values in each row :")
for i in range(4):
    print("Row",i+1,":",rows_sum[i])



# Display the sums of the columns
for j in range(4):
    print("Column",j+1,":",columns_sum[j])
       




