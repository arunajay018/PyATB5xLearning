side1=float(input("Enter side1 of triangle\n"))
side2=float(input("Enter side2 of triangle\n"))
side3=float(input("Enter side3 of triangle\n"))

if side1==side2==side3:
    print("equilateral triangle")
elif side1==side2 or side2==side3 or side3==side1:
    print("isoceles triangle")
else:
    print("scalene triangle")