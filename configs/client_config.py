import finnhub

# Setup Finnhub client
def setUpClient():
    finnhub_api_key = 'cqsn8o1r01qg43b90th0cqsn8o1r01qg43b90thg'
    finnhub_client = finnhub.Client(api_key=finnhub_api_key)
    print("Finish Set Up")
    return finnhub_client