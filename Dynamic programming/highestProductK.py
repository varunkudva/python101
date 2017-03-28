
def highest_product(arr, k, n):
    prod = [[1] * n for _ in range(k+1)]
    for i in range(1, k+1):
        for j in range(0, n):
            if j >= i-1:
                prod[i][j] = max(prod[i][j-1], prod[i-1][j-1] * arr[j])

    print prod
    return prod[k][n-1]

arr = [4, 9, 2, 3, -6, -8, 1, 5]
print highest_product(arr, 3, len(arr))

