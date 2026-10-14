# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

def sum_of_odds(nums):
    sumnums = 0
    for num in range(1,nums + 1):
        if num % 2 != 0:
            sumnums += num
    return sumnums
print(sum_of_odds(5))