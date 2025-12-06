# Hardcoded stock prices
stock_prices = {
    "SUJAL": 180,
    "MRF": 250,
    "NXT": 140,
    "CT": 130,
    "GOOGLE": 310
}

portfolio = {}
print("Welcome to the Stock Portfolio Tracker!")
print("Available stocks and prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

print("\nEnter your stocks and quantities.")
print("Type 'done' when finished.\n")

# Input loop
while True:
    stock_name = input("Enter stock symbol (SUJAL,CT etc.): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not found! Please enter a valid symbol.\n")
        continue

    try:
        qty = int(input("Enter quantity: "))
    except ValueError:
        print("Please enter a valid number.\n")
        continue

    # Store in portfolio dictionary
    portfolio[stock_name] = portfolio.get(stock_name, 0) + qty
    print("Added!\n")

# Calculate total value
total_value = 0
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    value = qty * stock_prices[stock]
    total_value += value
    print(f"{stock} - {qty} shares -> Value: ${value}")

print(f"\nTotal Investment Value: ${total_value}")

# Optional: save to a file
save = input("\nDo you want to save this result to portfolio.txt? (yes/no): ").lower()
if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("-------------------------\n")
        for stock, qty in portfolio.items():
            value = qty * stock_prices[stock]
            file.write(f"{stock}: {qty} shares -> Value: ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_value}\n")

    print("Portfolio saved to portfolio.txt!")