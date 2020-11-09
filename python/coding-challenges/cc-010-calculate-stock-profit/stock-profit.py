from collections import deque

def stock_max_profit(prices):
    max = 0
    prices = deque(prices)
    buy_price = prices.popleft()

    for price in prices:
        if price < buy_price:
            buy_price = price
        else:
            profit = price - buy_price
            if profit > max:
                max = profit
    if max:
        return max
    else:
        return -1

prices = [1,6,19,59,30,60]
max_profit = stock_max_profit(prices)
print(max_profit)