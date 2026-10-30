#1.Write a program to accept year from user and check if it is a leap year or not.
year = int(input("Enter a year:"))

if(year % 4 == 0):
    print("leap year.")

elif(year % 100 == 0):
    print("not a leap yera.")

elif (year % 4 == 0):
    print("leap year.")

else:
    print("not a leap year.")    