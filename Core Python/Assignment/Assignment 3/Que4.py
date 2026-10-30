#4.Write a program to input all sides of a triangle and check whether triangle is valid or not.

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    print("Triangle is valid")
else:
    print("Triangle is not valid")
