# Write a program that reads two matrices and returns the multiplication between them as an answer. the  program should observe whether or not it is possible to perform the multiplication between the two matrices.


# Read the dimentions of matrix A
rows_a=int(input("Enter the number of rows in matrix A:"))
cols_a=int(input("Enter the number of columns in matrix A:"))


# Read the dimentions of matrix B
rows_b=int(input("Enter the number of rows in matrix B:"))
cols_b=int(input("Enter the number of columns in matrix B:"))




# Check if the multiplication is possible or not
if cols_a !=rows_b:
    print("Multiplication is not possible")

else:
    # Read matrix A
    print("Enter the elements of matrix A :")
    matrix_a=[]
    for _ in range(rows_a):
        row=[]
        for _ in range(cols_a):
            element=int(input("enter the element :"))
            row.append(element)
        matrix_a.append(row)
    

    # Read matrix B
    print("Enter the elements of matrix B :")
    matrix_b=[]
    for _ in range(rows_b):
        row=[]
        for _ in range(cols_b):
            element=int(input('ENTER THE ELEMENTS OF THE MATRIX  B :'))
            row.append(element)
        matrix_b.append(row)


# Multiply the two matrices
result=[[0]*cols_a for _ in range(rows_a)]
for i in range(rows_a):
    for j in range(cols_b):
        for k in range(cols_a):
            result[i][j]+=matrix_a[i][k]*matrix_b[k][j]



# Display the result
print("The result of the multiplication is :")
for row in result:
    print(row)






