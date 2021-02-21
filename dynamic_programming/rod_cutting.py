"""
Max profit that can be made from cutting a rod
length = 6
prices = [0,1,3,3,8,8,10]
     len: 0 1 2 3 4 5 6
what is the maximum profit that can be made by cutting the rod any no. of times (0 or more)
Guess:
length of first cut going to be (n choices)
subproblem:
max profit for cutting a rod of smaller length
dp[i] => max profit for cutting a rod of length i
Recurrence:
profit by making a cut of length l == dp[i-l] + price[l]
dp[i] = max(dp[i-l]) + price[l]) for l in range(cutlength)


"""
def rod_length(length, prices):
    dp = [0] * (length+1)
    for i in range(1, length+1):
        for cut_len in range(len(prices)):
            if cut_len <= i:
                dp[i] = max(dp[i], dp[i-cut_len]+prices[cut_len])

    print(dp)
    return dp[length]

length = 6
prices = [0,1,3,3,8,8,10]
print(rod_length(6, prices))
