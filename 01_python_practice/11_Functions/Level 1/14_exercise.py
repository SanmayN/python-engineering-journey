# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

num = [2,1,3,4,5]
num1 = [2,1,3,4]

def calculate_mean(mean):
    calculate_mean = 0
    for num in mean:
        calculate_mean += num
    accum_mean = calculate_mean/len(mean)
    return accum_mean
print(f"Mean is {calculate_mean(num)}")

def calculate_median(median):

    sort_median = median.copy()
    sort_median.sort()
    middle_index = len(sort_median) // 2
    median_value = sort_median[middle_index]
    return median_value
print(calculate_median(num))

# EVen itmes in the list

def calculate_med_even(num1):
    sort_median = num1.copy()
    sort_median.sort()
    index_1 = len(sort_median) // 2
    median_value_1 = sort_median[index_1]
    index_2 = index_1 - 1
    median_value_2 = sort_median[index_2]
    median = (median_value_1 + median_value_2) / 2
    return median_value_1, median_value_2, median
even_med, odd_med , med = calculate_med_even(num1)
print(even_med,",", odd_med,"," "Median", med)

# Combine Median Ops

def calculate_median_value(nums):
    sort_median = nums.copy()
    sort_median.sort()

    middle_index =  len(sort_median) // 2

    if len(sort_median) % 2 == 0:
        median_value_1 = sort_median[middle_index]
        median_value_2 = sort_median[middle_index - 1]
        median = (median_value_1 + median_value_2) / 2
        return median
    else:
        median = sort_median[middle_index]
        return median

num1 = [2, 1, 3, 4]
print(calculate_median_value(num1))  # 2.5

num2 = [2, 1, 3, 4, 5]
print(calculate_median_value(num2))  # 3