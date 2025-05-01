# Write a program that fills a 3x3 matirx with values with values entered by the user and displays the sum of the main diagonal values.


# Initialize  the matirx
matrix=[[0,0,0],
        [0,0,0],
        [0,0,0]]
print(matrix)
print(type(matrix))
# Prompt the user to enter the values for the matrix
for i in range(3):
    for j in range(3):
        values=int(input("({},{}):".format(i,j)))
        matrix[i][j]=values
# Calculate the sum of the main diagnal matirx values
sum=0
for i in range(3):
    sum+=matrix[i][j]
# Display the matrix
print("The matirx is :")
for row in matrix:
    print(row)


# Display the sum of the main diagonal values
print("The sum of the main diagonal values is :",sum)