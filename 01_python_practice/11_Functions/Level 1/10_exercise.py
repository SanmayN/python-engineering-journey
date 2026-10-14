# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.


food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']

def remove_item(food_stuff, new_item):
        new_list = food_stuff.copy()
        new_list.remove(new_item)
        return new_list

print(remove_item(food_stuff,"Milk"))

print(food_stuff)