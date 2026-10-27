#4. Write a program to enter P, T, R and calculate simple Interest.

principle_amount = int(input('Enter the value of P:'))
Rate_of_interest = int(input('Enter the value of R:'))
Time = int(input('Enter the value of T:'))

#Fomula for simple interest using P,R,T.

simple_interest=  (principle_amount*Rate_of_interest*Time)/100

#print simple interest using P,R,T.

print("The Simple Interest for given P,R,T value's is",simple_interest)
