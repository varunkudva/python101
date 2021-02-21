"""
All algorithms for string search
(a) Brute Force
(b) Rabin Karp
(c) KMP
"""
def string_match(pat, text):
    res = []
    m = len(pat)
    n = len(text)
    def brute_force(pat, text):
        i, j = 0, 0
        for i in range(n-m+1):
            for j in range(m):
                if text[i+j] != pat[j]:
                    break
            if j == m-1:
                # found a substring of len n
                res.append(text[i:i+m])

    def rabin_karp(pat, text):
        """
        create a hash with all characters in the pattern
        assuming only lowercase chars: lets take base as 26
        and M as 31 (prime)
        """
        M = 31
        base = 26
        def gen_hash(txt, length):
            roll_hash = 0
            for char in range(length):
                roll_hash = (roll_hash * base + (ord(char) - ord('a'))) % M
            return roll_hash

        # go through the pattern and generate hash
        pat_hash = gen_hash(pat, m)
        txt_hash = gen_hash(text, m)
        for i in range(m, n):
            txt_hash = (txt_hash - ((text[i-m] - ord('a')) * pow(base, m-1))) * base % M
            txt_hash + index






    brute_force()
    return res


text = "abacadabrac"
pat = "abra"
print(string_match(pat, text))