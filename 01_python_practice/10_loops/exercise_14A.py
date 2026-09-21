# How do we arrange these counts from largest to smallest?
numbers = [45, 12, 91, 33, 67]
highest_num = 0
for num in numbers:
    if num > highest_num:
        highest_num = num
print(highest_num)