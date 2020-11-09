stock_price_list = [1, 6, 19, 59, 30, 60]
def calculate_profit(stock_price):
    max_profit = 0
    for i in range(len(stock_price)):
        for j in range(i+1, len(stock_price)):
            if (stock_price[j]-stock_price[i]) > max_profit:
                max_profit = stock_price[j]-stock_price[i]
    return max_profit
print(calculate_profit(stock_price_list))
# def calculate_profit2(stock_price):
#     result = [max(stock_price[(i+1):])-stock_price[i] for i in range(len(stock_price)-1)]
#     return max(result)
# print(calculate_profit2(stock_price_list))