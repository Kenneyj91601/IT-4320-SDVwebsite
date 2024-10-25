import requests
import pygal
import pandas as pd
from datetime import datetime
import webbrowser

# API Information
API_URL = "https://www.alphavantage.co/query"
API_KEY = "5V6R95XQRW35NXAW" 

def get_chart_type():
    print("Chart Types")
    print("----------------------")
    print("1. Bar")
    print("2. Line")
    chart_choice = input("Enter the chart type you want (1, 2): ")
    return "bar" if chart_choice == "1" else "line"

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

def validate_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return None

def fetch_stock_data(symbol, function, interval="60min", month=None):
    params = {
        "function": function,
        "symbol": symbol,
        "apikey": API_KEY,
        "datatype": "json",
        "outputsize": "full",  # Ensure full dataset
    }

    if function == "TIME_SERIES_INTRADAY":
        params["interval"] = interval
        if month:
            params["month"] = month 

    response = requests.get(API_URL, params=params)
    response.raise_for_status()
    data = response.json()

    time_series_key = next((key for key in data if "Time Series" in key), None)
    if time_series_key:
        return data[time_series_key]
    else:
        print("No valid time series data found.")
        return None

def filter_data_by_date(data, start_date, end_date):
    filtered_data = {
        date: values
        for date, values in data.items()
        if start_date <= datetime.strptime(date.split(" ")[0], "%Y-%m-%d").date() <= end_date
    }
    return pd.DataFrame.from_dict(filtered_data, orient='index')

def filter_intraday_by_day(data, target_date):
    """Filters intraday data to match the specific day from the user's input."""
    target_date_str = target_date.strftime("%Y-%m-%d")
    filtered_data = {
        date: values
        for date, values in data.items()
        if date.startswith(target_date_str)
    }
    return pd.DataFrame.from_dict(filtered_data, orient='index')

def generate_chart(data, chart_type, symbol):
    if chart_type == "bar":
        chart = pygal.Bar()
    else:
        chart = pygal.Line()

    chart.title = f"{symbol} Stock Data"
    chart.x_labels = list(data.index)

    chart.add('Open Price', data['1. open'].astype(float).tolist())
    chart.add('High Price', data['2. high'].astype(float).tolist())
    chart.add('Low Price', data['3. low'].astype(float).tolist())
    chart.add('Close Price', data['4. close'].astype(float).tolist())

    chart_file = f"{symbol}_stock_chart.svg"
    chart.render_to_file(chart_file)
    print(f"Chart saved to {chart_file}.")
    webbrowser.open(chart_file)

def main():
    while True:
        symbol = input("Enter the stock symbol (e.g., AAPL): ").upper()
        chart_type = get_chart_type()
        function = get_time_series()

        start_date_str = input("Enter the start date (YYYY-MM-DD): ")
        start_date = validate_date(start_date_str)

        if not start_date:
            print("Error: Invalid start date provided.")
            continue

        if function == "TIME_SERIES_INTRADAY":
            # Extract the YYYY-MM part for the API query
            year_month = start_date.strftime("%Y-%m")
            print(f"Fetching intraday data for {symbol} for {year_month}...")

            try:
                # Pass the `year_month` as the `month` parameter
                stock_data = fetch_stock_data(symbol, function, month=year_month)
                if not stock_data:
                    print("No data available for the given month.")
                    continue

                # Filter intraday data to match the specific day
                filtered_data = filter_intraday_by_day(stock_data, start_date)

                if filtered_data.empty:
                    print("No intraday data available for the given day.")
                else:
                    generate_chart(filtered_data, chart_type, symbol)

            except Exception as e:
                print(f"An error occurred: {e}")

        else:
            end_date_str = input("Enter the end date (YYYY-MM-DD): ")
            end_date = validate_date(end_date_str)

            if not end_date or end_date < start_date:
                print("Error: Invalid date(s) provided.")
                continue

            print(f"Fetching data for {symbol}...")
            try:
                stock_data = fetch_stock_data(symbol, function)
                if not stock_data:
                    print("No data available for the given date range.")
                    continue

                filtered_data = filter_data_by_date(stock_data, start_date, end_date)

                if filtered_data.empty:
                    print("No data available for the given date range.")
                else:
                    generate_chart(filtered_data, chart_type, symbol)

            except Exception as e:
                print(f"An error occurred: {e}")

        # Ask the user if they want to continue
        continue_prompt = input("Do you want to run another query? (yes/no): ").strip().lower()
        if continue_prompt != 'yes':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
