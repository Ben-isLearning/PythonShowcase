# larger_sum() that takes two lists of numbers as parameters

# The function should return the list whose elements
# sum to the greater number.

# If the sum of the elements of each list are equal, return lst1.

def larger_sum(list_one, list_two):
    return list_one if sum(list_one) >= sum(list_two) else list_two


print(larger_sum([1, 9, 5], [2, 3, 7]))

print(larger_sum([1, 9, 5], [6, 3, 7]))

print(larger_sum([1, 9, 5], [2, 8, 5]))
