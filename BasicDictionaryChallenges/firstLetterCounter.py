# count_first_letter that takes a dictionary named names as a parameter.
# names should be a dictionary where the key is a last name and
# the value is a list of first names.
#
# For example, the dictionary might look like this:
# names = {
# "Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"],
# "Lannister": ["Jaime", "Cersei", "Tywin"]
# }

# The function would return;
#   {"S" : 4, "L": 3}


# Write your count_first_letter function here:
def count_first_letter(names):
    letters = {}
    for key, value in names.items():
        #letters[key[0]] = 0
        if key[0] not in letters:
            letters[key[0]] = 0
        letters[key[0]] += len(value)
    return letters


# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow": [
      "Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow": [
      "Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}
