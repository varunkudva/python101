#!/usr/bin/python -tt
"""
Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def asum(a1, n, d):
    an = a1 + (n-1) * d
    return (n * (a1 + an)) / 2

def lcm(x, y):
    return x*y

def main():
    range = 1000
    m3 = range / 3
    m5 = range / 5
    if range % 3 == 0:
        m3 -= 1
    if range % 5 == 0:
        m5 -= 1

    l = lcm(3,5)
    ml = range / l
    if range % l == 0:
        ml -= 1

    sum3 = asum(3, m3, 3) 
    sum5 = asum(5, m5, 5) 
    suml = asum(l, ml, l)

    print "sum %d" %(sum3 + sum5 - suml)
    

        






if __name__ == '__main__':
     main()
