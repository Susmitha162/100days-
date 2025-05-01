# write a program that calculates the kinetic energy of a moving object,using the formula e=(mv^2)/2,where E is the kinetic energy ,m is the mas of the object ,and v is the velocity.

mass=float(input("Enter the mass of the object :"))
velocity=float(input("Enter the velocity of the object :"))


# Calculate the kinetic energy 
kinetic_energy=(mass*velocity**2)/2


# Display the result of the kinetic energy of the object
print("The kinetic energy of the object is :",kinetic_energy)