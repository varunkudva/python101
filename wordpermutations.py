"""
Problem:


Approach/Solution:


Notes:

Compexity:
 Time: O(n)
 Space:


Source:
None
"""

def permute(s, res=''):

    if len(res) == len(s):
        print res,

    # candidate list
    for char in s:
         # is_valid_candidate
        if char not in res:
            #make_move, unmake_move
            permute(s, res+char)



def unique_digit_num_count(n):
    unique_digit = 9
    available_num = 9
    res = 10 # for n == 1
    while n > 1:
       unique_number = unique_number * available_num
       res += unique_number
       available_num -= 1




def combination_sum(res, idx, sum, input):
    if sum == 0:
        print res
    else:
        for i in range(idx, len(input)):
            num = input[idx]
            if num <= sum and num not in res:
                res.append(num)
                combination_sum(res, sum - num, input)
                res.pop()

# combination_sum([], 0, 7, [2,3,6,7].sort())
# combination_sum([], 0, 8, [10, 1, 2, 7, 6, 1, 5].sort())

def pattern_match(str, pattern, j=0, n=0):
    if j == len(pattern):
        if j == n:
            return True
        return False
    for i in range(0, len(str)):
        if pattern[j] == '*' and j < len(pattern)-1 and str[i] != pattern[j+1]:
            return pattern_match(str[i+1:], pattern, j, n)
        elif str[i] == pattern[j] or pattern[j] == '?':
            return pattern_match(str[i+1:], pattern, j+1, n)
    return False

def test_pattern_match():
    print pattern_match('aa', 'a', n=len('aa'))
    print pattern_match('aa', 'aa', n=len('aa'))
    print pattern_match('aaa', 'aa', n=len('aaa'))
    print pattern_match('aa', '*', n=len('aa'))


if __name__ == '__main__':
    permute('abc')
    permute('')
    permute('ab')
