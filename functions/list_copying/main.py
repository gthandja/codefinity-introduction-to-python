def apply_discount(prices):
    prices_copy = prices.copy()
    for key in range(len(prices_copy)):
        if prices_copy[key] > 2.00:
            prices_copy[key] = prices_copy[key] * 0.90
    return prices_copy

# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)
print(f"Updated product prices: $ {updated_prices}")