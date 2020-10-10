def solution(arr):
    # Type your solution here
    """
    find left subtree sum
    find right subtree sum
    [3, 6, 2, 9, -1, 10]
    0   1
    """
    def find_sum(arr, idx):
      queue = []
      queue.append(idx)
      sum = 0
      while queue:
        idx = queue.pop(0)
        sum += arr[idx]
        left = 2 * idx + 1
        right = left + 1
        if left < len(arr):
          queue.append(left)
        if right < len(arr):
          queue.append(right)
      return sum

    if len(arr) < 2:
      return ""

    if len(arr) == 2:
      return "Left"

    left_sum = find_sum(arr, 1)
    right_sum = find_sum(arr, 2)
    if left_sum == right_sum:
        return ""

    return "Left" if left_sum > right_sum else "Right"

arr = [3, 6, 2, 9, -1, 10]
print(solution(arr))