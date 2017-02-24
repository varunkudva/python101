"""
This is a famous google interview problem
Given an input string and a dictionary of words, find out if the input
string can be segmented into a space-separated sequence of dictionary words.
See following examples for more details.

"""
d = [ 'apple', 'pie', 'gold', 'rush', 'sand', 'dune']

def word_break_recur(input, d):
    """This is a backtracking solution for wordbreak problem
    complexity: O(2 pow n)
    """
    if input in d:
        return input

    for i in range(1, len(input)+1):
        word = input[0:i]
        if word in d:
            suffix = word_break_recur(input[i:], d)
            if suffix:
                return word + " " + suffix
    return None

def word_break_iter(input, d):
    res = ""
    i = 0
    for j in range(i+1, len(input)+1):
        word = input[i:j]
        if word in d:
            res += word + " "
            i = j
    return res

#print word_break_recur('applesanddune', d)
print word_break_iter('applesanddune', d)