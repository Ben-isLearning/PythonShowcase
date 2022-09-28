# every_other_letter that takes a string.
# The function should return a string containing every other letter in word.

def every_other_letter(word):
    new_str = ""
    for letter in range(0, len(word), 2):
        new_str += word[letter]
    return new_str


print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter("m1i2k3e"))
# should print mike
