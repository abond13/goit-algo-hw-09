import timeit

# Номінали монет фіксовані і посортовані
# Так як є монета номіналом 1, то будь–яка сума буде мати рішення,
# тому не робимо відповідних перевірок 
coins=[50, 25, 10, 5, 2, 1]


def find_min_coins(amount):
    # Створюємо масив для збереження мінімальної кількості монет для кожної суми до amount
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    # Масив для збереження номіналів монет, які використовуються для кожної суми
    coin_used = [-1] * (amount + 1)
    
    # Заповнюємо масив dp
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin
    
    # Відновлюємо номінали монет для формування суми
    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = coin_used[current_amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_amount -= coin
    
    return result


def find_coins_greedy(amount):
    result = {}
    
    for coin in coins:
        if amount == 0:
            break
        count = amount // coin  # кількість монет поточного номіналу
        if count > 0:
            result[coin] = count
            amount -= coin * count
    
    return result

def main():
    # Тест роботи
    amount = 113
    print(find_min_coins(amount))    # {1: 1, 2: 1, 10: 1, 50: 2}
    print(find_coins_greedy(amount)) # {50: 2, 10: 1, 2: 1, 1: 1}
    print()
    # Час виконання:
    setup_string = "from __main__ import find_min_coins, " + \
                   "find_coins_greedy, coins"
    
    for n in [51, 113, 1441]:
        print(f"Sum to change: {n}:")
        for find_coins_name in ["find_min_coins", "find_coins_greedy"]:
            timeit_res = timeit.timeit(f"{find_coins_name}({n})", 
                                       number=1000,
                                       setup=setup_string)
            print(f"\tTime of {find_coins_name:<20}: {timeit_res}")
        print()

if __name__ == '__main__':
    main()