#Shopping cart

# Create a shopping cart programme that will continiously ask the user for a food products annd the price of that product
# Have an exit clause if the user wish to stop adding more things to their cart
# At the end show the food items and the total cost to the user

foods =[]
prices =[]
total = 0

while True:
    food =input('Enter a food to buy or press q to quit:  ')
    if food.lower()  == 'q':
        break
    else:
        price = float(input(f"Enter the price of the{food}: R"))
        foods.append(food)
        prices.append(price)

print("-----------YOUR CART--------------")        

for food in foods:
    print(food)

for price in prices:
    total += price

print(f"Your total is:  R{total}")