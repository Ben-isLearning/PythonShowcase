# check_for_name that takes two strings as parameters.
# The function should return True if name appears in sentence
# in all lowercase letters, all uppercase letters, or with any mix
# of uppercase and lowercase letters.
# The function should return False otherwise.

# For example,
# the following three calls should all return True:

#check_for_name("My name is Jamie", "Jamie")
#check_for_name("My name is jamie", "Jamie")
#check_for_name("My name is JAMIE", "Jamie")

def check_for_name(sentence, name):
    return name.lower() in sentence.lower()


check_for_name("Hello there DERRECK", "Derreck")

# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jaMiE", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False
