from configs.client_config import setUpClient
from helpers.find_one_twenty import find_stocks_with_price_range

# Main function where the client is initialized and passed
def main():
    # Initialize Finnhub client
    f_client = setUpClient()
    
    # Define the price range
    min_price = 1
    max_price = 20
    
    # Find stocks in the specified price range
    stocks_in_range = find_stocks_with_price_range(min_price, max_price, f_client)
    
    # Output the result
    print(f"Stocks with price between ${min_price} and ${max_price}: {stocks_in_range}")

if __name__ == "__main__":
    main()