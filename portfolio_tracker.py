import csv
import os
from datetime import datetime


class StockPortfolioTracker:
    def __init__(self):
        """Initialize the portfolio tracker with predefined stock prices"""
        # Hardcoded stock prices (in USD)
        self.stock_prices = {
            "AAPL": 180.50,  # Apple
            "TSLA": 250.75,  # Tesla
            "GOOGL": 140.25,  # Google
            "MSFT": 375.80,  # Microsoft
            "AMZN": 145.30,  # Amazon
            "META": 325.60,  # Meta (Facebook)
            "NVDA": 450.20,  # NVIDIA
            "NFLX": 425.40,  # Netflix
            "AMD": 105.85,  # AMD
            "INTC": 43.25  # Intel
        }

        self.portfolio = {}  # User's portfolio: {stock_symbol: quantity}
        self.portfolio_history = []  # Track all transactions

    def display_available_stocks(self):
        """Display all available stocks with their current prices"""
        print("\n📊 Available Stocks and Current Prices:")
        print("-" * 50)
        print(f"{'Stock Symbol':<12} {'Company':<15} {'Price (USD)':<12}")
        print("-" * 50)

        stock_info = {
            "AAPL": "Apple",
            "TSLA": "Tesla",
            "GOOGL": "Google",
            "MSFT": "Microsoft",
            "AMZN": "Amazon",
            "META": "Meta",
            "NVDA": "NVIDIA",
            "NFLX": "Netflix",
            "AMD": "AMD",
            "INTC": "Intel"
        }

        for symbol, price in self.stock_prices.items():
            company = stock_info.get(symbol, "Unknown")
            print(f"{symbol:<12} {company:<15} ${price:<11.2f}")

    def add_stock(self):
        """Add stock to portfolio"""
        self.display_available_stocks()

        while True:
            stock_symbol = input("\nEnter stock symbol (or 'back' to return): ").upper().strip()

            if stock_symbol == 'BACK':
                return

            if stock_symbol not in self.stock_prices:
                print("❌ Invalid stock symbol! Please choose from the available stocks.")
                continue

            try:
                quantity = int(input(f"Enter quantity of {stock_symbol} shares: "))
                if quantity <= 0:
                    print("❌ Please enter a positive number of shares.")
                    continue

                # Add to portfolio
                if stock_symbol in self.portfolio:
                    self.portfolio[stock_symbol] += quantity
                else:
                    self.portfolio[stock_symbol] = quantity

                # Calculate investment amount
                investment = quantity * self.stock_prices[stock_symbol]

                # Record transaction
                transaction = {
                    'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'action': 'BUY',
                    'symbol': stock_symbol,
                    'quantity': quantity,
                    'price': self.stock_prices[stock_symbol],
                    'total': investment
                }
                self.portfolio_history.append(transaction)

                print(f"✅ Successfully added {quantity} shares of {stock_symbol}")
                print(f"💰 Investment amount: ${investment:.2f}")
                break

            except ValueError:
                print("❌ Please enter a valid number for quantity.")

    def remove_stock(self):
        """Remove stock from portfolio"""
        if not self.portfolio:
            print("❌ Your portfolio is empty!")
            return

        self.display_portfolio()

        while True:
            stock_symbol = input("\nEnter stock symbol to remove (or 'back' to return): ").upper().strip()

            if stock_symbol == 'BACK':
                return

            if stock_symbol not in self.portfolio:
                print("❌ You don't own this stock!")
                continue

            try:
                max_shares = self.portfolio[stock_symbol]
                quantity = int(input(f"Enter quantity to remove (max {max_shares}): "))

                if quantity <= 0 or quantity > max_shares:
                    print(f"❌ Please enter a number between 1 and {max_shares}.")
                    continue

                # Calculate sell amount
                sell_amount = quantity * self.stock_prices[stock_symbol]

                # Update portfolio
                self.portfolio[stock_symbol] -= quantity
                if self.portfolio[stock_symbol] == 0:
                    del self.portfolio[stock_symbol]

                # Record transaction
                transaction = {
                    'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'action': 'SELL',
                    'symbol': stock_symbol,
                    'quantity': quantity,
                    'price': self.stock_prices[stock_symbol],
                    'total': sell_amount
                }
                self.portfolio_history.append(transaction)

                print(f"✅ Successfully sold {quantity} shares of {stock_symbol}")
                print(f"💰 Sell amount: ${sell_amount:.2f}")
                break

            except ValueError:
                print("❌ Please enter a valid number for quantity.")

    def display_portfolio(self):
        """Display current portfolio with values"""
        if not self.portfolio:
            print("❌ Your portfolio is empty!")
            return

        print("\n📈 Your Current Portfolio:")
        print("-" * 70)
        print(f"{'Stock':<8} {'Shares':<8} {'Price':<12} {'Total Value':<15} {'Weight':<10}")
        print("-" * 70)

        total_portfolio_value = 0
        portfolio_details = []

        for symbol, quantity in self.portfolio.items():
            price = self.stock_prices[symbol]
            total_value = quantity * price
            total_portfolio_value += total_value

            portfolio_details.append({
                'symbol': symbol,
                'quantity': quantity,
                'price': price,
                'total_value': total_value
            })

        # Display each stock with weight percentage
        for stock in portfolio_details:
            weight = (stock['total_value'] / total_portfolio_value) * 100
            print(f"{stock['symbol']:<8} {stock['quantity']:<8} ${stock['price']:<11.2f} "
                  f"${stock['total_value']:<14.2f} {weight:<9.1f}%")

        print("-" * 70)
        print(f"{'TOTAL PORTFOLIO VALUE:':<45} ${total_portfolio_value:.2f}")
        print("-" * 70)

    def calculate_portfolio_summary(self):
        """Calculate and display portfolio summary statistics"""
        if not self.portfolio:
            print("❌ Your portfolio is empty!")
            return

        total_value = sum(quantity * self.stock_prices[symbol]
                          for symbol, quantity in self.portfolio.items())

        total_invested = sum(t['total'] for t in self.portfolio_history if t['action'] == 'BUY')
        total_sold = sum(t['total'] for t in self.portfolio_history if t['action'] == 'SELL')

        net_invested = total_invested - total_sold
        unrealized_gain_loss = total_value - net_invested

        print("\n📊 Portfolio Summary:")
        print("-" * 40)
        print(f"Total Stocks Owned: {len(self.portfolio)}")
        print(f"Current Portfolio Value: ${total_value:.2f}")
        print(f"Total Amount Invested: ${net_invested:.2f}")
        print(f"Unrealized Gain/Loss: ${unrealized_gain_loss:.2f}")
        if net_invested > 0:
            roi_percentage = (unrealized_gain_loss / net_invested) * 100
            print(f"Return on Investment: {roi_percentage:.2f}%")

    def view_transaction_history(self):
        """Display all transaction history"""
        if not self.portfolio_history:
            print("❌ No transactions found!")
            return

        print("\n📋 Transaction History:")
        print("-" * 80)
        print(f"{'Date':<20} {'Action':<6} {'Symbol':<8} {'Shares':<8} {'Price':<12} {'Total':<12}")
        print("-" * 80)

        for transaction in self.portfolio_history:
            print(f"{transaction['date']:<20} {transaction['action']:<6} "
                  f"{transaction['symbol']:<8} {transaction['quantity']:<8} "
                  f"${transaction['price']:<11.2f} ${transaction['total']:<11.2f}")

    def save_portfolio_to_file(self):
        """Save portfolio to CSV and TXT files"""
        if not self.portfolio:
            print("❌ Your portfolio is empty! Nothing to save.")
            return

        # Create filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Save to CSV
        csv_filename = f"portfolio_{timestamp}.csv"
        try:
            with open(csv_filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Stock Symbol', 'Quantity', 'Price per Share', 'Total Value'])

                total_value = 0
                for symbol, quantity in self.portfolio.items():
                    price = self.stock_prices[symbol]
                    stock_total = quantity * price
                    total_value += stock_total
                    writer.writerow([symbol, quantity, price, stock_total])

                writer.writerow(['', '', 'TOTAL PORTFOLIO VALUE:', total_value])

            print(f"✅ Portfolio saved to CSV: {csv_filename}")
        except Exception as e:
            print(f"❌ Error saving CSV: {e}")

        # Save to TXT
        txt_filename = f"portfolio_{timestamp}.txt"
        try:
            with open(txt_filename, 'w') as txtfile:
                txtfile.write("STOCK PORTFOLIO REPORT\n")
                txtfile.write("=" * 50 + "\n")
                txtfile.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

                txtfile.write(f"{'Stock':<8} {'Shares':<8} {'Price':<12} {'Total Value':<15}\n")
                txtfile.write("-" * 50 + "\n")

                total_value = 0
                for symbol, quantity in self.portfolio.items():
                    price = self.stock_prices[symbol]
                    stock_total = quantity * price
                    total_value += stock_total
                    txtfile.write(f"{symbol:<8} {quantity:<8} ${price:<11.2f} ${stock_total:<14.2f}\n")

                txtfile.write("-" * 50 + "\n")
                txtfile.write(f"TOTAL PORTFOLIO VALUE: ${total_value:.2f}\n")

            print(f"✅ Portfolio saved to TXT: {txt_filename}")
        except Exception as e:
            print(f"❌ Error saving TXT: {e}")

    def run(self):
        """Main program loop"""
        print("💼" + "=" * 60)
        print("        WELCOME TO STOCK PORTFOLIO TRACKER")
        print("=" * 60)
        print("Track your stock investments and calculate portfolio value!")

        while True:
            print("\n🎯 Main Menu:")
            print("1. 📈 View Available Stocks")
            print("2. ➕ Add Stock to Portfolio")
            print("3. ➖ Remove Stock from Portfolio")
            print("4. 👁️  View Current Portfolio")
            print("5. 📊 Portfolio Summary")
            print("6. 📋 Transaction History")
            print("7. 💾 Save Portfolio to File")
            print("8. 🚪 Exit")

            choice = input("\nEnter your choice (1-8): ").strip()

            if choice == '1':
                self.display_available_stocks()
            elif choice == '2':
                self.add_stock()
            elif choice == '3':
                self.remove_stock()
            elif choice == '4':
                self.display_portfolio()
            elif choice == '5':
                self.calculate_portfolio_summary()
            elif choice == '6':
                self.view_transaction_history()
            elif choice == '7':
                self.save_portfolio_to_file()
            elif choice == '8':
                print("\n💼 Thank you for using Stock Portfolio Tracker!")
                print("Happy investing! 📈")
                break
            else:
                print("❌ Invalid choice! Please enter a number between 1-8.")

            input("\nPress Enter to continue...")


def main():
    """Main function to run the stock portfolio tracker"""
    tracker = StockPortfolioTracker()
    tracker.run()


if __name__ == "__main__":
    main()