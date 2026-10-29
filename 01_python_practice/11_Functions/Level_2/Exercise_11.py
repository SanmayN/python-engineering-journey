# Write a function called greet which takes a default argument, name. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.
from email import message


def greet(name = "Guest"):
    if name == "Guest":
        return "Hello, Guest!"
    else:
        return "Hello, " + name + "!"
print(greet())
print(greet("Sanmay"))

def greet(name = "Guest"):
    return "Hello, " + name + "!"
print(greet())
print(greet("Jatin"))
