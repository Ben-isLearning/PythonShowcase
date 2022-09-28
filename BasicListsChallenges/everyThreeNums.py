# function should accept one parameter - the starting number
# Calculate the numbers between the starting number and 100
#   while incrementing by 3
# Store the numbers in a list
# Return the list

def every_three_nums(start):
    num_list = []
    for element in range(start, 105, 3):
        num_list.append(element)
    return num_list


print(every_three_nums(91))
