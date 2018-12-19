#!/usr/bin/python -tt
"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROBLEM:


APPROACH/SOLUTION:


NOTES:

COMPEXITY:
 Time: O(n)
 Space: Constant if considering only alphabets.
        O(k) where k is the character set count.

SOURCE:
None
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PROBLEM:


APPROACH/SOLUTION:


NOTES:

COMPEXITY:
 Time: O(n)
 Space: Constant if considering only alphabets.
        O(k) where k is the character set count.

SOURCE:
None
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

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


import sys

def example_list():
    L = []
    for i in range(int(raw_input())): 
        command = raw_input().split()
        if command[0] == "insert":
            L.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print L
        elif command[0] == "remove":
            L.remove(int(command[1]))
        elif command[0] == "append":
            L.append(int(command[1]))
        elif command[0] == "sort":
            L.sort()
        elif command[0] == "pop":
            L.pop()        
        elif command[0] == "reverse":
            L.reverse()
            print L 
        else:
            none

           
def example_tuple():
    x = tuple(int (i) for i in (raw_input().split()))
    print hash(x)

def example_set():
    raw_input()
    m = set(map(int,raw_input().split()))
    raw_input()
    n = set(map(int, raw_input().split()))
    res = list(m.symmetric_difference(n))
    for i in sorted(res):
         print i

#def raw_input(input_fp=None):
#    if input_fp == None:
#        input_fp = sys.stdin
#    return input_fp.readline().rstrip("\n").strip()

def example_list_comprehension():
    x,y,z,n = map(int, list(iter(raw_input,'')))
    #print [i for i in range(0, x+1) j for j in range(0,y+1) for k in range(0,z+1)]

def solution(x):
   q = x
   r = 0
   while q!= 0:
       r += q % 10
       q = q / 10 

   if r > 9:
       solution(r)
   else:
       print r
  
def answer2(population, x, y, strength):

    res = list(population) 
    stack = [(x,y)]
    visited = []

    while (len(stack)):
        (x, y) = stack.pop()
        if (x < 0 or y < 0 or x >= len(population[0])  or y >= len(population)):
            continue;
        visited.append((x,y))
        if population[y][x] <= strength:
            res[y][x] = -1
            if (x-1, y) not in visited:
                stack.append((x-1, y))
            if (x, y-1) not in visited:
                stack.append((x, y-1))
            if (x+1, y) not in visited:
                stack.append((x+1, y))
            if (x, y+1) not in visited:
                stack.append((x, y+1))

    print res


def answer(pop, x, y, strength):
    
    if x < 0 or y < 0:
        return None
    if  x >= len(pop[0]) or y >= len(pop):
        return None
    if  pop[y][x] > strength or pop[y][x] == -1:
        return None
    
    if strength >= pop[y][x]:
        pop[y][x] = -1
        answer(pop, x-1, y, strength)
        answer(pop, x+1, y, strength)
        answer(pop, x, y-1, strength)
        answer(pop, x, y+1, strength)
    else:
        return None

    


if  __name__ == '__main__':
   #example_list()
   #example_tuple() 
   #example_set()
   #example_list_comprehension()
   #solution(int(raw_input()))
   pop = [[1, 2, 3], [2, 3, 4], [3, 2, 1]]
   pop2 = [[6, 7, 2, 7, 6], [6, 3, 1, 4, 7], [0, 2, 4, 1, 10], [8, 1, 1, 4, 9], [8, 7,
       4, 9, 9]]
   answer2(pop, 0, 0, 2)
   answer2(pop2, 2, 1, 5)

