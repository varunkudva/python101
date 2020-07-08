"""
Problem:
All subsets of a given set or Power set problem


Approach/Solution:
With a set with n items, there are 2 pow n subsets that can be formed.
This is similar to the bits pattern where with n bits we can represent
2**n numbers. Use bit representation to index elements of the subset
to form all possible subsets.


Notes:

Compexity:
 Time: O(2**n) exponential
 Space:


Source:
None
"""


def generate_subsets(s):
   res = []
   n = len(s)
   for num in range(0, 2 ** n):
      sub = list()
      for i in range(n):
         if num & (1 << i):
            sub.append(s[i])
      res.append(sub)

   return (res)


def generate_subsets_bfs(s):
   """
   :param s:
   :return:
   [] => [] [a] => [] [a] [b] [a, b] =>
   """
   res = [[]]
   for num in s:
      n = len(res)
      for i in range(n):
         new = list(res[i])
         new.append(num)
         res.append(new)
   return res


if __name__ == '__main__':
   s = ['a', 'b', 'c', 'd']
   print(generate_subsets(s))
   print(generate_subsets_bfs(s))
