# Locating a stock's high and low given a range of days
# variables a and b represents the start day and end day

stock_prices = [ 6.15, 5.81, 5.70, 5.65, 5.33, 5.62, 5.19, 6.13, 7.20, 7.34, 7.95, 7.53, 7.39, 7.59, 7.27 ]

def max_price(a, b):
  return max(stock_prices[(a-1):b])

def min_price(a, b):
  return min(stock_prices[(a-1):b])

def price_at(x):
  return stock_prices[x-1]

print(max_price(2, 5))
print(min_price(2, 5))
print(price_at(5))