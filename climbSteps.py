# climb stairs problem from leetcode
# Backtracking solution
def climb(top, ways, path):

    if top == 0:
        ways += 1
        print path

    if top < 0: return

    for step in (1, 2):
        path.append(step)
        climb(top-step, ways, path)
        path.pop()

    return ways

path = list()
print "ways:{}".format(climb(4, 0, path))

