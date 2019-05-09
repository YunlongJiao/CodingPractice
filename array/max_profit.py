# NOTE


def max_profit(prices):
    """
    121. Best Time to Buy and Sell Stock
    Say you have an array for which the ith element is the price of a given stock on day i.
    If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
    design an algorithm to find the maximum profit.
    Note that you cannot sell a stock before you buy one.

    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

    """

    best = 0

    if len(prices) > 1:
        m = prices[0]
        for p in prices[1:]:
            best = max(best, p-m)
            m = min(m, p)

    return best


if __name__ == '__main__':
    print(max_profit([7,1,5,3,6,4]))
    print(max_profit([7,6,4,3,1]))
