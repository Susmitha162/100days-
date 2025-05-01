# Write a program that asks for a person's height and weight and calculates their body mass index (BMI), displaying the corresponding category (underweight,normal weight,overweight,obese,severely odese).



# Prompt the user to their height and weight
height=float(input("Enter your height in meters :"))
weight=float(input("Enter your weight in kilometers :"))



# Calculate the BMI using the height and weight 
bmi=weight/(height**2)


# Determine the corresponding BMI category
if bmi<18.5:
    category="Underweight"
elif bmi<25:
    category="Normal weight"
elif bmi<30:
    category="Over weight"
elif bmi<35:
    category="Obese"
else:
    category="Severely obese"



# Display the BMI catogory
print("YOUR bmi IS :",bmi)
print("Category :",category)

























