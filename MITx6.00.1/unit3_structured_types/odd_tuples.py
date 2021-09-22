# Exercise: odd tuples

# Write a procedure called oddTuples, which takes a tuple as input,
# and returns a new tuple as output, where every other element of the input tuple is copied,
#  starting with the first one.
# So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'),
# then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').


def oddTuples(aTup):
    """
    aTup: a tuple

    returns: tuple, every other element of aTup.
    """
    counter = 0
    new_tuple = ()
    while counter < len(aTup):

        new_tuple += (aTup[counter],)
        counter += 2

        # Another way to solve this:
        # Slice the tuple from start to end by 2.
        # return aTup[::2]
    return new_tuple


print(oddTuples(("I", "am", "a", "test", "tuple")))
