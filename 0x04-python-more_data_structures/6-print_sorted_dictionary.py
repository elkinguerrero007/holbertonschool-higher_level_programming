def print_sorted_dictionary(a_dictionary):
    '''print dict sorted by keys'''
    if not a_dictionary:
        return
    for key in sorted(a_dictionary):
        print("{}: {}".format(key, a_dictionary[key]))
