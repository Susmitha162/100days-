# Promt for the user input height ,weight
weight=float(input("enter the weight of the person :"))
height=float(input("enter the height of the person :"))

# Calculate the bmi based on the weight and height 
bmi=weight / (height ** 2)

# Displays the result of the 
print("Your BMI is :",bmi)