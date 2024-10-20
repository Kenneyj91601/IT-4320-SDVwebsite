API_URL = "https://www.alphavantage.co/query"
API_KEY = "5V6R95XQRW35NXAW" 

#Allows user to select a chart type
def get_chart_type():
    print("Chart Types")
    print("----------------------")
    print("1. Bar")
    print("2. Line")
    chart_choice = input("Enter the chart type you want (1, 2): ") #if user chooses 1 the result will be bar, otherwise line will be chosen
    return "bar" if chart_choice == "1" else "line"

#Allows the user to select a time series type. Choices are 1-4 to associated time series. The default is daily for error handling. 
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