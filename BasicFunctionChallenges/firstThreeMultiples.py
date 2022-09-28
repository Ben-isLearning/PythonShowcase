# first_three_multiples() that has one parameter named num.

# This function should print the first three multiples of num.
# Then, it should return the third multiple.

# For example, first_three_multiples(7) should print 7, 14, and 21
# on three different lines, and return 21.


def first_three_multiples(num):
    for i in range(1, 4):
        print(i * num)
    return(3 * num)


first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0
