# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
#
# The sum of all evens is 2550. And the sum of all odds is 2500.

countEven = 0
countOdd = 0

for i in range(1,101):
    if i % 2 == 0:
        countEven += i
    else:
        countOdd += i

print(countEven)
print(countOdd)