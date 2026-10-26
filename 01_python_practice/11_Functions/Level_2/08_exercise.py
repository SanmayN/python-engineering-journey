#calculate_range

numbers = [2, 4, 4, 4, 5, 6, 6, 7]

def calculate_range(num):
    highest_num = num[0]
    lowest_num = num[0]
    for n in num:
        if n > highest_num:
            highest_num = n
        if n < lowest_num:
            lowest_num = n
    return highest_num - lowest_num
rangeC = calculate_range(numbers)
print(rangeC)