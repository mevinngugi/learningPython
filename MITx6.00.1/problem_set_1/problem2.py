# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print

# Number of times bob occurs is: 2


def count_bob(s):
    occurrence = 0
    if type(s) == str:
        s = list(s.lower())
        for index, value in enumerate(s):
            if len(s) - index == 2:
                return "Number of times bob occurs is:", occurrence
            else:
                check_bob = value + s[index + 1] + s[index + 2]
                if check_bob == "bob":
                    occurrence += 1

    else:
        return "Your input should be a string"


print(*count_bob("azcbobobegghakl"))
