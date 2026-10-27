#1. Convert the time entered in hh,min and sec into seconds.

hh = int(input("Enter hours:"))
min = int(input("Enter minutes:"))
ss = int(input("Enter seconds:"))

total_seconds = (hh * 3600)

print("Time in seconds =",total_seconds)