prices = []
total_items = int(input("Enter a total items : "))
for i in range(1, total_items + 1):
    items = int(input(f"Enter product {i} price : "))
    prices.append(items)
total_prices = sum(prices)
print(f"total : {total_prices}")