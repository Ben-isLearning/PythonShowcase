# frequency_dictionary that takes a list of elements
# named words as a parameter.

# The function should return a dictionary containing the
# frequency of each element in words.

def frequency_dictionary(words):
    new_dict = {}
    for word in words:
        if word not in new_dict:
            new_dict[word] = 0
        new_dict[word] += 1
    return new_dict


# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0, 0, 0, 0, 0]))
# should print {0:5}
