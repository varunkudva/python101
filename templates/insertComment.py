#!/usr/bin/python

problem_string = '''"""
Problem:


Approach/Solution:


Notes:

Compexity:
 Time: O(n)
 Space:


Source:
None
"""
'''
import sys
def main(filename):
    global problem_string
    text = ''
    with open(filename) as fd:
        if fd.readline().startswith('"""'):
            return
        else:
            fd.seek(0)
            line = fd.readline()
            if line.startswith('#!'):
                problem_string = line + problem_string
                text = fd.read()
            else:
                fd.seek(0)
                text = fd.read()

    with open(filename, 'w') as fd:
        if text.startswith('\n\n'):
            fd.write(problem_string + text)
        elif text.startswith('\n'):
            fd.write(problem_string + '\n' + text)
        else:
            fd.write(problem_string + '\n\n' + text)


if __name__ == '__main__':
    filename = sys.argv[1]
    if '.py' in filename:
        # only in python files
        main(filename)
