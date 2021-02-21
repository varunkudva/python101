"""
hashmap with sliding window

"""
class Solution(object):
    def minWindow(self, s, t):
        from collections import Counter

        "count characters in t"
        hashmap = Counter(t)
        remaining_count = len(t)

        " sliding window pointers"
        start, end = 0, 0
        minlen = float('inf')
        head = 0

        while end < len(s):
            if hashmap[s[end]] > 0:
                """ if character exists in t, 
                decrement the  character count """
                remaining_count -= 1

            hashmap[s[end]] -= 1
            end += 1
            while remaining_count == 0:
                """
                found a window with all character in t
                start shrinking the window and check if its still valid
                """
                wlen = end - start
                if wlen < minlen:
                    head = start
                    minlen = wlen

                if hashmap[s[start]] == 0:
                    """ make the window invalid again """
                    remaining_count += 1

                hashmap[s[start]] += 1
                start += 1

        if minlen < float('inf'):
            return s[head:head + minlen]
        return ""