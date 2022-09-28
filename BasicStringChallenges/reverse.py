# reverse_string that takes a string.
# The function should return word in reverse.

# Write your reverse_string function here:
def reverse_string(word):
    new_str = ""
    for letter in range(len(word)-1, -1, -1):
        new_str += word[letter]
    return new_str


# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string("Tweetie Pie"))
# should print eiP eiteewT
