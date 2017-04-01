"""
Problem:
Write an efficient function that takes stock_prices_yesterday and returns the best
profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

The values are the price in dollars of Apple stock.
A higher index indicates a later time
You must buy before you sell. No shorting

Algorithmic Pattern:
Greedy -- "Scan once"

Approach/Solution:
For every scanned current price, find the maximum profit that can be obtained
from all the previous prices. This can be done by keeping track of the minimum
price up till the current price. Update overall maximum profit.

Notes:

Compexity:
 Time: O(n)
 Space: O(n)

Source:
https://www.interviewcake.com/question/python/stock-price>
"""
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

    return max_profit


if __name__ == '__main__':
    test_input = [[10, 7, 5, 8, 11, 9],
                  [10, 9, 8, 7, 6, 5],
                  [4, 11, 23, 5, 6, 90, 11, 24, 55]]

    expected_output = [6, -1, 86]

    for input, expected in zip(test_input, expected_output):
        assert get_max_profit(input) == expected
