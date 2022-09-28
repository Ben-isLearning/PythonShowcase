# dog_years() that has two parameters named name and age.

# the function should compute the age in dog years and
# return the following string:
# "{name}, you are {age} years old in dog years"


def dog_years(name, age):
    return name + " you are " + str(age*7) + " years old in dog years"


print(dog_years("Janice", 16))
# should print "Janice you are 112 years old in dog years"
print(dog_years("Baby", 2))
# should print "Baby, you are 14 years old in dog years"
