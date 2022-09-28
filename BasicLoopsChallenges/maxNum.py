# max_num() that takes a list of numbers named nums as a parameter.
#
# The function should return the largest number in nums

def max_num(nums):
    maxNum = nums[0]
    for num in nums:
        if num > maxNum:
            maxNum = num
    return maxNum


print(max_num([50, -10, 0, 75, 20]))

print(max_num([50, -10, 0, 75, 200]))
