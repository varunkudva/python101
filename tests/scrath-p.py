"""
given a sorted array of integers, find the maximum number of integers from it, such that the difference between every two consecutive integers is the same
		4, 8, 12=> 3
		4, 7, 8, 12=> 3 (4, 8, 12)

longest increasing subsequence where increase is fixed
lis(i,j) = lis(i, j-1),lis(i,j-k)+1 for k < j and arr[k] < arr[j]
brute force:

		4, 7, 8, 9, 10, 12=> 4 (7, 8, 9, 10)

"""
def find_max_difference(nums):
    n = len(nums)
    maxnum = 0
    for i in range(len(nums)-1):
        count = 1
        for j in range(i+1, len(nums)):
            diff = nums[j]-nums[i]
            while (nums[j] + diff) in nums:
                count += 1
                diff += diff
        maxnum = max(maxnum, count)
    return maxnum

nums_arr = [[4, 8, 12], [3, 4, 7, 8, 12], [4, 7, 8, 9, 10, 12]]
for nums in nums_arr:
    print(find_max_difference(nums))


class Node:
    def __init__(self):
        self.data = None
        self.prev = self.next = None

class Cll:
    def __init__(self):
        self.head = self.tail = None

    def enqueue(self, data):
        # enqueue in sorted manner
        node = Node(data)
        if self.head == self.tail == None:
            self.head = self.tail = node
        else:
            cur = self.head
            while cur.val < node.val and cur != tail:
                cur = cur.next

            node.next = cur.next
            cur.next = node
            node.prev = cur


