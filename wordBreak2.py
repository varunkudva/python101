"""
Given a valid sentence without any spaces between the words and a dictionary of
valid English words, find all possible ways to break the sentence in individual
dictionary words.

Backtracking Solution
"""
def wordbreak(res, s, d):
    if len(s) == 0:
        if res:
            print " ".join(res)
        return

    for i in range(1, len(s)+1):
        word = s[0:i]
        if word in d:
            res.append(word)
            wordbreak(res, s[i:], d)
            res.pop()

    return None


if __name__ == '__main__':
    dictionary = ["mobile","samsung","sam","sung",
                  "man","mango", "icecream","and",
                  "go","i","love","ice","cream", "like"]

    str = "ilikeicecreamandmango"
    wordbreak([], str, dictionary)