def jump_game(arr):
    last_good_idx = len(arr) - 1
    for i in range(len(arr) - 1, -1, -1):
        if i + arr[i] >= last_good_idx:
            last_good_idx = i

    if last_good_idx == 0:
        return True
    return False


arr = [1, 0, 1, 1, 4]
print(jump_game(arr))
