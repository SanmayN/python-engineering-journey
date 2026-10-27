# calculate_std (standard deviation).

import math
from exercise_09 import calculate_variance

numbers = [2, 4, 4, 4, 5, 6, 6, 7]

def calculate_std(nums):
    variance_value = calculate_variance(nums)
    std_value = math.sqrt(variance_value)
    return std_value
print(calculate_std(numbers))