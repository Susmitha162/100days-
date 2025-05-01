# Prompt the user for the length of the sides snd height of the triangle
side_a=float(input("Enter the length of side a:"))
side_b=float(input("Enter the length of side b:"))
side_c=float(input("Enter the length of side c:"))
height=float(input("Enter the height relative to side b:"))


# Calculate  the perimeter 
perimeter =side_a+side_b+side_c


# Calculate the area
area=(side_b*height)/2

#Display the results
print("Perimeter of the triangle:",perimeter)
print("Area of the triangle :",area)




