#Accept area of one wall
area = float(input('Enter area of wall:'))

#Accept painting cost per unit area
interior_cost = float(input('Enter interior painting cost per unit area:'))
exterior_cost = float(input('Enetr exterior painting cost per unit area:'))

#Calculate total painting cost 
interior_total = 4 * area * interior_cost
exterior_total = 4 * area * exterior_cost

total_cost = interior_total + exterior_total

#Dispaly the result 
print('interior painting cost =',interior_total)
print('exterior painting cost =',exterior_total)
print('total painting cost =',total_cost)

