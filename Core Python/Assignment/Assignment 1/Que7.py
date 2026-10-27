# Q7. Program to find the roots of a Quadratic Equation

import math 

a = float(input("Enter a:"))
b = float(input("Enter b:"))
c = float(input("Enter c:"))

d = b*b - 4*a*c

if a == 0:
    print("Not a quadratic equation")
elif d > 0:
    r1 =(-b + math.sqrt(d))/(2*a)
    r2 =(-b - math.sqrt(d))/(2*a)
    print("Roots are:",r1,"and",r2)

elif d ==0:
    r = -b / (2*a)
    print("Equal roots:",r)
else:
    real = -b / (2*a)
    imag = math.sqrt(-d)/(2*a)
    print("Complex roots:",complex(real,imag),"and",complex(real,-imag))
    