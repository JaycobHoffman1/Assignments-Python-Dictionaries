# Task 1: Restaurant Menu Update

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

# Adds a new category called "Beverages" with at least two items.
restaurant_menu['Beverages'] = {'Coffee': 9.99, 'Cola': 5.99}
print('Category "Beverages" added!')

# Updates the price of "Steak" to 17.99.
restaurant_menu['Main Course']['Steak'] = 17.99
print('"Steak" price updated to 17.99!')

# Removes "Bruschetta" from "Starters". 
del restaurant_menu['Starters']['Bruschetta']
print('"Bruschetta" has been removed!')

# Prints restaurant_menu in formatted manner
print('\nRestaurant menu:')

for category, menu_items in restaurant_menu.items():
    print(f'\n{category}:')

    for menu_item, price in menu_items.items():
        print(f'{menu_item}: {price}')