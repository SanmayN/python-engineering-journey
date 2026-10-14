# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

def sum_of_numbers(nums):
    sumnums = 0
    for num in range(1,nums + 1):
        sumnums += num
    return sumnums
print(sum_of_numbers(5))