def greedy_coin(change):
    """Return a dictionary with the coin type as the key and the number of coins as the value"""

    print(f"Your change for {change}: ")
    coins = [0.25, 0.10, 0.05, 0.01]
    coin_lookup = {0.25: "quarter", 0.10: "dime", 0.05: "nickel", 0.01: "penny"}
    coin_dict = {}
    for coin in coins:
        coin_dict[coin] = 0
    for coin in coins:
        while change >= coin:
            change -= coin
            coin_dict[coin] += 1
    for coin in coin_dict:
        if coin_dict[coin] > 0:
            print(f"{coin_dict[coin]} {coin_lookup[coin]}")
    return coin_dict
