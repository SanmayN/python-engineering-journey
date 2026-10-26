# Call your function is_empty, it takes a parameter and it checks if it is empty or not

def is_empty(value):
    if not value:
        return False
    else:
        return True
print(is_empty([10,20]))