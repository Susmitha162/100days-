# Prompt the user input three sides of the triangle
side1=float(input("Enter the length of the fisrt side :"))
side2=float(input("Enter the length of the second side :"))
side3=float(input("Enter the length of the third side :"))


# Check if the three side can form a triangle 
if side1+side2>side3 and side1+side3>side2 and side2+side3>side1:
    print("The three sides can form a triangle.")
else:
    print("The three sides connot form a triangle.")








