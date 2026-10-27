# Q8. Write a program to convert days into years, weeks and days.

days=1000

# code for calculating years 
years=days//365

#for remaing days
days=days%365

#code for calculating weeks 
weeks=days//7

#for remaing days
days=days%7

#result for years, weeks and days.

print('There are',years, weeks,'weeks and',days,'days')

      