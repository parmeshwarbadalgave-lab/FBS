#4. Write a program to calculate area of triangle and rectangle.

#Calculate the area of a triangle

base = float(input("Enter the base of triangle:"))
height = float(input("Enter the height of triangle:"))

triangle_area = 0.5 * base * height
print("Area of triangle =",triangle_area)

#Calculate the area of a rectangle

length = float(input("Enter the length of rectangle: "))
breadth = float(input("Enter the breadth of rectangle:"))

rectangle_area = length * breadth
print("Area of rectangle =",rectangle_area)

