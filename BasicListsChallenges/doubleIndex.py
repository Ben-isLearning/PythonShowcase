# double_index that has two parameters: a list and an index.
# The function should return a new list where all elements are
#  the same as in lst except for the element at index.
#  The element at index should be double the value of the
#  element at index of the original lst.

# If index is not a valid index, the function should return the original list.
#
# For example,  double_index([1, 2, 3, 4], 2)
# should return [1,2,6,4] because the element at index 2 has been doubled

def double_index(list_one, index_to_double):
    if index_to_double >= len(list_one):
        return list_one
    new_list = list_one[:index_to_double]
    new_list.append(list_one[index_to_double] * 2)
    new_list += (list_one[index_to_double+1:])
    return new_list


# Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))
