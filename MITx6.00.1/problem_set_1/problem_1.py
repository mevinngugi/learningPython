# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
# For example, if s = 'azcbobobegghakl', your program should print:

# Number of vowels: 5


def count_vowels(s):
    vowels = ["a", "e", "i", "o", "u"]
    number_of_vowels = 0
    try:
        for i in list(s):
            if i in vowels:
                number_of_vowels += 1
        return ("Number of vowels:", number_of_vowels)

    except TypeError:
        return "Please provide a string"


print(*count_vowels("azcbobobegghakl"))
