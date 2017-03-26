def get_max_profit(stock_prices):
    if len(stock_prices) < 2:
        print "Invalid stock price list"
        return

    min_price = stock_prices[0]
    # this is to return negative profit if stockprices
    # if stock prices are going down all day
    max_profit = stock_prices[1] - stock_prices[0]

    for i in range(1, len(stock_prices)):

        # calculate profit for current price
        profit = stock_prices[i] - min_price

        # calculate max profit
        max_profit = max(max_profit, profit)

        # calculate new min price
        min_price = min(min_price, stock_prices[i])

    return max_profit, min_price, min_price + max_profit


test_input = [[10, 7, 5, 8, 11, 9], [10, 9, 8, 7, 6, 5], [4, 11, 23, 5, 6, 90, 11, 24, 55]]
for arr in test_input:
    print get_max_profit(arr)
# print "Max profit: {} by buying at {} and selling at {}".format(get_max_profit(arr))
