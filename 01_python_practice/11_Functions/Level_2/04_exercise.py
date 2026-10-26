# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

nums = [1,2,3,4,5]

def calculate_mean(mean):
    accum = 0
    for num in nums:
        accum += num
    return accum/ len(mean)

print(f"Mean is {calculate_mean(nums)}")