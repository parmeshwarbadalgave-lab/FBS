#2. Write a program to accept 3 digit number. if first digit is double of second digit and half of third digit then display "Yes, you have done it", otherwise display "please try to next time".

num = int(input("Enter a 3 digit:"))
first = num // 100
second = (num // 10)% 10
third = num % 10 

if first == second * 2 and first *2 == third:
    print("Yes, you have done.")
else:
    print("Please try next time.")


