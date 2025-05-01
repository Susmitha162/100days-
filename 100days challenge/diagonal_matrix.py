# Write  a program that reads a 4x4 matrix and checks if the matrix is diagonal matrix. that is , if all elements outside the main diagonal are equal to zero 

# Read the elements of the matrix
matrix=[]
for _ in range(4):
    row=[]
    for _ in range(4):
        element=int(input("Enter the elements of the matrix :"))
        row.append(element)
    matrix.append(row)




# Check if it is  a diagonal matrix
is_diagonal=True
for i in range(4):
    for j in range(4):
        if i!=j and matrix[i][j]!=0:
            is_diagonal=False
            break



# Display the result 
if is_diagonal:
    print("The matrix is a diagonal matrix :")
else:
    print("The given matrix is not a diagonal matrix :")