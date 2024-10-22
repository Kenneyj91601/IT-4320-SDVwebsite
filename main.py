import requests

API_URL = "https://www.alphavantage.co/query"
API_KEY = "5V6R95XQRW35NXAW" 

def main():
    symbol = input("Enter the stock symbol: ").upper()

    time_series = get_time_series()
    stock_data = get_stock_data(symbol, time_series)

    # print the stock data
    print("stock data:", stock_data)

def get_time_series(): 
    print("Select the Time Series of the chart you want to Generate")
    print("------------------------------")
    print("1. Intraday")
    print("2. Daily")
    print("3. Weekly")
    print("4. Monthly")
    time_series_choice = input("Enter time series option (1, 2, 3, 4): ")
    
    if time_series_choice == "1":
        return "TIME_SERIES_INTRADAY"
    elif time_series_choice == "2":
        return "TIME_SERIES_DAILY"
    elif time_series_choice == "3":
        return "TIME_SERIES_WEEKLY"
    elif time_series_choice == "4":
        return "TIME_SERIES_MONTHLY"
    else:
        print("Invalid choice. Defaulting to Daily.")
        return "TIME_SERIES_DAILY"

def get_stock_data(symbol, time_series):
    parameters = {
        "function": time_series,
        "symbol": symbol,
        "apikey": API_KEY,
        "datatype": "json",
    }

    # for testing parameters
    print("query prams:", parameters)

    response = requests.get(API_URL, params=parameters)
    data = response.json()  # makes it json

    # print the response data for debugging
    print("response data:", data)

    return data

if __name__ == "__main__":
    main()
