# middle_element that has one parameter named lst.
# If there are an odd number of elements in lst,
# the function should return the middle element.
#
# If there are an even number of elements,
# the function should return the average of the middle two elements.

def middle_element(num_list):
    if (len(num_list) % 2 == 0):
        return (num_list[int((len(num_list) / 2 - 1))] + num_list[int((len(num_list) / 2))]) / 2
    return num_list[int(len(num_list) / 2)]


print(middle_element([5, 2, -10, -4, 4, 5]))
