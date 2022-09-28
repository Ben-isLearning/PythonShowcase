# same_values() that takes two lists of numbers of
# equal size as parameters.

# The function should return a list of the indices where
# the values were equal in lst1 and lst2.

# For example, same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])
# should return [0, 2, 3]

def same_values(list_one, list_two):
    matches = []
    for i in range(len(list_one)):
        if list_one[i] == list_two[i]:
            matches.append(i)
    return matches


print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
print(same_values([5, 1, -10, 3, 3], [1, 2, 3, 3, 3, 3]))
print(same_values([1, 2, 3], [1, 2, 3]))
