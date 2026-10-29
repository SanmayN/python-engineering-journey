# Create a function called show_args to take an arbitrary number of named arguments and print their names and values

def show_args(**kwargs):
    for key,value in kwargs.items():
        print (f"{key}:{value}")
(show_args(name= "asd", age= 54))
