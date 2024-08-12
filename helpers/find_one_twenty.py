import finnhub
import yfinance as yf

def get_all_tickers(client, exchange='US'):
    print("Enter Get Tickers")
    tickers = client.stock_symbols(exchange)
    print(f"tickers are  {[ticker['symbol'] for ticker in tickers]}")
    return [ticker['symbol'] for ticker in tickers]



def find_stocks_with_price_range(min_price, max_price, client):
    tickers_in_price_range = []
    tickers = get_all_tickers(client, exchange='US')
    for ticker in tickers:
        try:
            # Fetch the stock data from yfinance
            current_price = yf.Ticker(ticker).info['currentPrice']
            
            if min_price <= current_price <= max_price:
                tickers_in_price_range.append(ticker)
        except Exception as e:
            print(f"Could not retrieve data for {ticker}: {e}")
    
    return tickers_in_price_range
