# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']

def add_item(food_stuff,new_item):
    new_list = food_stuff.copy()
    new_list.append(new_item)
    return new_list
print(add_item(food_stuff,"Meat"))

print(food_stuff)