# Write a program that two 2x2 matrices and displys the sum of the two matrices


# Initialize the two 2x2 matrices
matrix_1=[[0,0],[0,0]]
matrix_2=[[0,0],[0,0]]
sum_matrix=[[0,0],[0,0]]



# Read the values for the first matrix
print("Enter the elements of the first matrix :")
for i in range(2):
    for j in range(2):
        matrix_1[i][j]=int(input(f"Enter element at position ({i+1},{j+1}):"))




# Read the vlaues of the second matrix
print("Enter the elements of the second matrix :")
for i in range(2):
    for j in range(2):
        matrix_2[i][j]=int(input(f"Enter element at position ({i+1},{j+1}):"))






# Calculate the sum of the two matrices
for i in range(2):
    for j in range(2):
        sum_matrix[i][j]=matrix_1[i][j]+matrix_2[i][j]





# Display the sum of the two matrices 
print("The sum of the two matirces is :")
for row in sum_matrix:
    print(row)






