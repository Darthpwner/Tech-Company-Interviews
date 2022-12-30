# Buy low, sell high

def max_profit(prices: list[int]) -> int:
    l, r = 0, 1
    maxProfit = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)
        else:   # No longer a profit, reset left pointer
            l = r
        r += 1

    return maxProfit

prices = [1, 9, 5, 16, 1, 9, 13]  # maxProfit = 15
print(max_profit(prices))