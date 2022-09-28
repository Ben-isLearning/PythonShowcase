# introduction() that has two parameters named first_name and last_name.

# The function should return the last_name, followed by a comma,
# a space, first_name another space, and finally last_name.


def introduction(f_name, l_name):
    return l_name + ", " + f_name + " " + l_name


print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Star", "Ringo"))
# should print Angelou, Maya Angelou
