# Q5. Write a program to enter P, T, R and calculate Compound Interest.

Principle_amount = float(input('Enter the value of P:'))
Rate_of_interest = float(input('Enter the value of R:'))
Time = float(input('Enter the value of T:'))

#Formula for compound interest.
Compound_interest = (Principle_amount*(1+Rate_of_interest/100)**Time)-Principle_amount

print("The Compound interest for P,R,T value's is :",Compound_interest)
