# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']

def capitalize_list_items(items):
    capitalize = []
    for item in items:
        capitalize.append(item.upper())
    return capitalize
print(capitalize_list_items(food_stuff))