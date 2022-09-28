# over_nine_thousand() that takes a list of numbers.

# The function should sum the elements of the list until the sum is greater
#  than 9000.
#
# When this happens, the function should return the sum.
# If the sum of all of the elements is never greater than 9000,
# the function should return total sum of all the elements.
# If the list is empty, the function should return 0.

# For example, if lst was [8000, 900, 120, 5000],
# then the function should return 9020.

def over_nine_thousand(num_list):
    sumNums = 0
    for num in num_list:
        sumNums += num
        if sumNums > 9000:
            break
    return sumNums


print(over_nine_thousand([8000, 900, 120, 5000]))

print(over_nine_thousand([8000, 900, 99, ]))
