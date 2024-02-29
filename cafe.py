#Create a menu with four items sold in the cafe, calculating the total value with stock value and price for each of the four items
menu = ['a', 'b', 'c', 'd']
stock = {'a': 1,
         'b': 2,
         'c': 3,
         'd': 4
         }

price = {'a': 15,
         'b': 10,
         'c': 20,
         'd': 5
         }

item_value = 0
for items in menu:
    item_value += stock[items] * price[items]

print(item_value)