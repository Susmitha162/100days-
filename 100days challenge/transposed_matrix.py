# Write a program that fills 4x4 matrix with  random values and displays the transposed matirx


# Initislize the matrix
import random
matrix=[[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

# Fill the matrix with random values
for i in range(4):
    for j in range(4):
        matrix[i][j]=random.randint(1,100)


# Display the matrix
print("Original Matrix :")
for row in matrix:
    print(row)


# Transpose the matrix
transposed_matirx=[[0,0,0,0],
                   [0,0,0,0],
                   [0,0,0,0],
                   [0,0,0,0]]


for i in range(4):
    for j in range(4):
        transposed_matirx[i][j]=matrix[j][i]





# Display the transposed matrix
print("Transposed matrix :")
for row in transposed_matirx:
    print(row)











