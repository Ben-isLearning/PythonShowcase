# word_length_dictionary that takes a list of strings
# named words as a parameter.
# The function should return a dictionary of key/value pairs
# where every key is a word in words and every value
# is the length of that word.


def word_length_dictionary(words):
    new_dict = {}
    for word in words:
        new_dict[word] = len(word)
    return new_dict


print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}
