# Write aprogram that reads a 3x3 matrix and calculates the determinant of the matrix


# Read the element of the 3x3 matrix from the user 
matrix=[]
for i in range(3):
    row=[]
    for j in range(3):
        element=int(input(f"enter an element {i+1} {j+1}:"))
        row.append(element)
    matrix.append(row)


# Calculate the determinant using formula
det={
    matrix[0][0] * (matrix[1][1]*matrix[2][2]-matrix[1][2] * matrix[2][1])
    -matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0])
    +matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0])
}

# Display the determinant using the formula
print("Determinant :",det)

#determinant formula =>>>>>>> a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)