# promt user input for the grades
grade1=float(input("enter the  first grade :"))
grade2=float(input("enter the second grade :"))
grade3=float(input("enter the third grade :"))


#calculate th arithmatic mean
mean=(grade1+grade2+grade3)/3

# Round the mean to  two decimals places
rounded_mean=round(mean,2)

# Display the result with two decomal places
print("Arithmatic mean:","{:.2f}".format(rounded_mean))