#3. Write a program to input angles of a triangle and check whether triangle is valid or not.

a = int(input('Enter first angle:'))
b = int(input('Enter second angle:'))
c = int(input('Enter tthird angle:'))

if a > 0 and b > 0 and c > 0 and a + b + c ==180:
   print('Triangle is valid')
else:
  print('Triangle is not valid')

