# ==========================================
# STOCK PORTFOLIO TRACKER
# ==========================================

print("==========================================")
print("       STOCK PORTFOLIO TRACKER")
print("==========================================")

# Hardcoded stock prices dictionary
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320,
    "AMZN": 150
}

# Display available stocks
print("\nAvailable Stocks and Prices:")
for stock, price in stock_prices.items():
    print(stock, ":", "$", price)

# Variables
portfolio = {}
total_investment = 0

# Number of stocks user wants to buy
num_stocks = int(input("\nHow many different stocks do you want to enter? "))

# Input stock details
for i in range(num_stocks):

    print("\nStock", i + 1)

    stock_name = input("Enter Stock Name: ").upper()

    if stock_name in stock_prices:

        quantity = int(input("Enter Quantity: "))

        portfolio[stock_name] = quantity

    else:
        print("Invalid Stock Name!")
        print("This stock is not available.")
        continue

# Calculate investment
print("\n==========================================")
print("         PORTFOLIO SUMMARY")
print("==========================================")

for stock, quantity in portfolio.items():

    stock_price = stock_prices[stock]

    investment = stock_price * quantity

    total_investment += investment

    print("Stock Name :", stock)
    print("Price      :", stock_price)
    print("Quantity   :", quantity)
    print("Investment :", investment)
    print("----------------------------------")

# Display total investment
print("\nTotal Investment Value =", total_investment)

# Save result into text file
file = open("portfolio_report.txt", "w")

file.write("STOCK PORTFOLIO REPORT\n")
file.write("========================\n")

for stock, quantity in portfolio.items():

    stock_price = stock_prices[stock]

    investment = stock_price * quantity

    file.write(
        stock + " | Price: " +
        str(stock_price) +
        " | Quantity: " +
        str(quantity) +
        " | Investment: " +
        str(investment) + "\n"
    )

file.write("\nTotal Investment Value = " + str(total_investment))

file.close()

print("\nPortfolio report saved successfully in 'portfolio_report.txt'")

print("\nThank You For Using Stock Portfolio Tracker!")