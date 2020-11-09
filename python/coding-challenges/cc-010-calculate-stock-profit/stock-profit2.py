def profit(given_list):
    result = []
    for i in range(len(given_list) - 1):
        result.append(max(given_list[i + 1 : ]) - given_list[i])
    return max(result)
print(profit([7, 29, 4, 3, 26, 2, 1]))