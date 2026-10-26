# calculate_variance

numbers = [2, 4, 4, 4, 5, 6, 6, 7]

def calculate_variance(nums):
    mean_value = 0
    squared_diff = 0
    sample_variance = 0
    for num in nums:
        mean_value += num

    mean_value = mean_value / len(nums)

    for num in nums:
        squared_diff += (mean_value - num) ** 2


    sample_variance = squared_diff/ (len(nums) - 1)
    return sample_variance
print(calculate_variance(numbers))
