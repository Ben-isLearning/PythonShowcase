# remove_middle  has three parameters - lst, start, and end.
# The function should return a list where all elements in lst
# with an index between start and end (inclusive)
# have been removed.

# For example,
# remove_middle([4, 8 , 15, 16, 23, 42], 1, 3)
# should return [4, 23, 42]
# because elements at indices 1, 2, and 3 have been removed:

# Write your function here
def remove_middle(list, starting_index, ending_index):
    return list[:starting_index] + list[ending_index+1:]


# Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
