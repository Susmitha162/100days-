# Write  a program that fills a 3x3 matrix  with random values and displays the transposed matrix

import random

# Iinitialize the matrix
matrix=[[0,0,0],
        [0,0,0],
        [0,0,0]]



# fill the matrix with random vlaues 

for i in range(3):
    for j in range(3):
        matrix[i][j]=random.randint(1,100)


# Display the Original matrix 
print("Original matrix is :")
for row in matrix:
    print(row)



# Calculate the transpose of the matrix
transpose_matrix=[[0,0,0],
                  [0,0,0],
                  [0,0,0]]



for i in range(3):
    for j in range(3):
        transpose_matrix[i][j]=matrix[j][i]





# Display the transposed matrix
print("Transeposed matrix is :")
for row in transpose_matrix:
    print(row)