"""
Problem:
All subsets of a given set or Power set problem


Approach/Solution:
With a set with n items, there are 2**n subsets that can be formed.
This is similar to the bits pattern where with n bits we can represent
2**n numbers. Use bit representation to index elements of the subset
to form all possible subsets.


Notes:

Compexity:
 Time: O(2**n)
 Space:


Source:
None
"""

def generate_subsets(s):
   n = len(s)
   for num in range(0, 2**n-1):
      sub = list()
      for i in range(n):
       if num & (1 << i):
          sub.append(s[i])
      print sub,


if __name__ == '__main__':
   s = ['a', 'b', 'c', 'd']
   generate_subsets(s)
