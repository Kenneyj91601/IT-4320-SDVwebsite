# IT-4320-StockDataVisualizer
## Software application in python to visualize stock data trends.

### Authors: Jonathan Hatfield, Kenneth Jackson, Desmond Jones, Danny Camino

This application will allow the user to enter a stock symbol (GOOGL) and to see stock data for trades done within the past few days, or even between multiple months. This information will be opened in the users default web browser and graphed according to user's choice of bar or line graphs.
 
To start the program you need to enter <Python main.py> into your terminal and hit enter.

First you enter which stock symbol you want to use. 

Next you will be asked to choose between bar or line graphs using 1 or 2 and clicking enter. The program will default to line if any errors occur. 

Next you will be asked to select a Time series. You will make a choice from 1-4 and click enter.  
NOTE: IN THE NEXT STEP, INTRADAY_TIME_SERIES WILL ONLY ACCEPT DATES WITHIN THE PAST MONTH OR SO. Otherwise you will be told there is no data for that selected date. 

Next you will be asked to input a valid start date and end date. Use YYYY-MM-DD. 

Next the application will fetch the api call data and prepare it and save it into an svg file named after the stock symbol. 

After the file is created, the application will open the folder in your default browser. 

In the graph you can toggle the High low open options.

The application will then ask if you would like to make another query or quit. Enter either yes or no. The program will default to quitting if any errors occur. 

Thank you for using our application!




