#3. Convert distants given in feet and inches  into meter and centimeter.

feet = int(input("Enter feet:"))
inches = int(input("Enter inches"))

total_inches = feet * 12 + inches
total_cm = total_inches * 2.54

meter = int(total_cm // 100)
centimeter = total_cm % 100

print("Distance=",meter,"meter and",
      round(centimeter,2),"cemtimeters")
