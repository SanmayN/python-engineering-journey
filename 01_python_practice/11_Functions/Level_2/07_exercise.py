# calculate_mode

numbers = [2, 4, 4, 4, 5, 6, 6, 7]

def calculate_mode(nums):
    highest_num = 0
    mode_value = 0
    for num in nums:
        count_num = 0
        for other_num in nums:
            if num == other_num:
                count_num += 1
        if count_num > highest_num:
            highest_num = count_num
            mode_value = num
    return mode_value
print(calculate_mode(numbers))