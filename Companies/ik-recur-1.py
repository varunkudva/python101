"""
```
Generate All Possible Expressions That Evaluate To The Given Target Value
Generate All Possible Expressions That Evaluate To The Given Target Value
Given a string s that consists of digits ("0".."9") and target, a non-negative integer, find all expressions that can be built from string s that evaluate to the target.
When building expressions, you have to insert one of the following operators between each pair of consecutive characters in s: "join" or "*" or "+". For example, by inserting different operators between the two characters of string "12" we can get either 12 (1 joined with 2) or 2 (1*2) or 3 (1+2).
Other operators such as "-" or "÷" are NOT supported.
Expressions that evaluate to the target but only utilize a part of s do not count: entire s has to be consumed.
Precedence of the operators is conventional: "join" has the highest precedence, "*" – medium and "+" has the lowest precedence. For example, 1+2*34=(1+(2*(34)))=1+68=69.
You have to return ALL expressions that can be built from string s and evaluate to the target.
Example One
Input:
s="222", target=24.
Output:
["22+2", "2+22"] and ["2+22", "22+2"] are both correct outputs.
    22+2=24: we inserted the "join" operator between the first two characters and the "+" operator between the last two characters of s.
    2+22=24: we inserted the "+" operator between the first two characters and the "join" operator between the last two characters of s.
Example Two
Input: s="1234", target=11.
Output: ["1+2*3+4"]
Example Three
Input:
s="99", target=1.
Output:
[]
"""


class Solution:
    def solve(self, s, target):
        operators = ['', '*', '+']

        def is_valid(res, op, i):
            if res:
                return True
            else:
                return True if op == '' else False

        def helper(res, idx, n):
            if idx == n:
                if '*' in res or '+' in res:
                    if eval(res.lstrip('0')) == target:
                        out.append(res)
                elif int(res) == target:
                    out.append(res)
                return

            for op in operators:
                if is_valid(res, op, idx):
                    print(res)
                    helper(op.join([res, s[idx]]), idx + 1, n)

        res, out = '', []
        helper(res, 0, len(s))
        return out


# print(Solution().solve('222', 24))
# print(Solution().solve('1234', 11))
# print(Solution().solve('99', 1))
print(Solution().solve('050505', 5))
