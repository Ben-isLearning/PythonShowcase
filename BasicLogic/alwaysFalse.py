# always_false() that has one parameter named num.
# this function will return False no matter what number is stored in num.


def always_false(num):
    if (num > 0 and num < 0):
        return True
    return False


print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False
