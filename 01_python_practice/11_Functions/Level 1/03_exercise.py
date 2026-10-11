def add_all_nums (*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add_all_nums(1,2,3,4,5))