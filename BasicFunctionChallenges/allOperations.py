# lots_of_math(). This function should have four parameters
# a, b, c, and d. The function should print 3 lines and return 1 value.

# First, print the sum of a and b.
# Second, print c minus d.
# Third, print the first number printed, multiplied by the second number printed.
# Finally, return the third number printed modulo a.


def lots_of_math(a, b, c, d):
    add = a + b
    print(add)
    sub = c - d
    print(sub)
    multi = add * sub
    print(multi)
    return multi % a


print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0
