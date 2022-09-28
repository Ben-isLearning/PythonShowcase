# in_range() that has three parameters named num, lower, and upper.
# The function should return True if num is greater than or equal to lower
# and less than or equal to upper. Otherwise, return False.

def in_range(num, lower, upper):
    if (num <= upper) and (num >= lower):
        return True
    return False


print(in_range(9, 5, 15))
# 9 is gt and 5, and lt 15. Returns true.

print(in_range(5, 10, 20))
# 5 is lt 10. Returns false.
