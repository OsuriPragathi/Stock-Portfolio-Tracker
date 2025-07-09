# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

print("📈 Welcome to Your Stock Portfolio Tracker!")
print("You can enter the stocks you own and we'll calculate your total investment.\n")

portfolio = {}

# Take user input
while True:
    stock = input("Enter a stock symbol (like AAPL, TSLA) or type 'done' to finish: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Sorry, we don't have the price for that stock. Try another one.")
        continue
    try:
        quantity = int(input(f"How many shares of {stock} do you own? "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Oops! Please enter a valid number for quantity.")

# Calculate total investment
total = 0
print("\n🧾 Here's a summary of your investments:\n")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total += investment
    print(f"- {stock}: {qty} shares @ ${price} = ${investment}")

print(f"\n💰 Total Investment Value: ${total}")

# Ask to save the result
save = input("\nWould you like to save this summary to a file? (yes/no): ").strip().lower()
if save == "yes":
    filename = input("Enter a filename to save (e.g., portfolio.csv or my_stocks.txt): ").strip()
    try:
        with open(filename, "w") as file:
            file.write("Stock,Quantity,Price,Total\n")
            for stock, qty in portfolio.items():
                file.write(f"{stock},{qty},{stock_prices[stock]},{stock_prices[stock]*qty}\n")
            file.write(f"Total Investment,,,{total}\n")
        print(f"✅ Your investment summary has been saved to '{filename}'.")
    except Exception as e:
        print(f"❌ Error saving file: {e}")
else:
    print("👍 No worries. Summary not saved.")

print("\nThanks for using the Stock Portfolio Tracker! 🚀")
