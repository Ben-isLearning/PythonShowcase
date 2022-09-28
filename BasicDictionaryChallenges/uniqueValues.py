# unique_values that takes a dictionary named
# my_dictionary as a parameter.

# The function should return the number of unique values in the dictionary.

def unique_values(my_dictionary):
    new_lst = []
    for value in my_dictionary.values():
        if value not in new_lst:
            new_lst.append(value)
    return (len(new_lst))


print(unique_values({0: 3, 1: 1, 4: 1, 5: 3}))
# should print 2
print(unique_values({0: 3, 1: 3, 4: 3, 5: 3}))
# should print 1
