<<<<<<< HEAD
#6. Write a program to calculate profit or loss.

cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))

if sp > cp:
    profit = sp - cp
    print("Profit =", profit)
elif cp > sp:
    loss = cp - sp
    print("Loss =", loss)
else:
=======
#6. Write a program to calculate profit or loss.

cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))

if sp > cp:
    profit = sp - cp
    print("Profit =", profit)
elif cp > sp:
    loss = cp - sp
    print("Loss =", loss)
else:
>>>>>>> 83baa457bbe14bbc168b78c3199c5d9c5e6656d9
    print("No Profit No Loss")