#1. Write a program to find the area and perimeter of following figure(Accept the length, breadth and radius from user)
import math
l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
r = float(input("Enter radius: "))

# Rectangle
area_rectangle = l * b
perimeter_rectangle = 2 * (l + b)

# Circle
area_circle = math.pi * r * r
perimeter_circle = 2 * math.pi * r

print("Area of Rectangle =", area_rectangle)
print("Perimeter of Rectangle =", perimeter_rectangle)

print("Area of Circle =", area_circle)
print("Perimeter of Circle =", perimeter_circle)



