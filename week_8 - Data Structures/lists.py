#Lists

#Print the third car in the lists(index 2)
cars = ['Toyota','Hyundai','Honda','Ford' ,'Nissan']
print(cars[2]) 

# Replace the second car(index 1)with 'Renault'
cars[1] = 'Renault'
print(cars)

# Add 'Kia' to the end of the list
cars.append('Kia')
print(cars)

# Insert 'Corsa' at index 1 (second position)
cars. insert(1,'Corsa')
print(cars)

# Remove 'Ford' from the list
cars.remove('Ford')
print(cars)

# Sort the list in alphabetical order
cars.sort()
print(cars)

# Sort the list in reverse  ( Z to A)
cars.sort(reverse=True)
print(cars)