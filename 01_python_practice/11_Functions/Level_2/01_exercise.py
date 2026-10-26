# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

def evens_and_odds(nums):
    countEven = 0
    countOdd = 0
    for num in range(0, nums + 1):
        if num % 2 == 0:
            countEven += 1
        else:
            countOdd += 1
    return countEven, countOdd

even, Odd = evens_and_odds(100)
print(f"The number of odds are {Odd}")
print(f"The number of evens are {even}")