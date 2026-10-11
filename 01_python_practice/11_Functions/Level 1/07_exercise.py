# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

numbers = [1, 2, 3, 4, 5]

def reverse_list(numbers):
    rl = []
    for i in range(len(numbers) -1, -1 ,-1):
        rl.append(numbers[i])
    return rl

print(reverse_list(numbers))