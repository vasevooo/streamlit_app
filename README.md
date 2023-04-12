# simple stock price and volume app 

This is a simple app created with Streamlit and the yfinance library that displays the historical stock prices and trading volumes of selected stocks. Users can select a stock from a drop-down menu and choose a start and end date for the data, as well as the data interval.

The app displays two line charts for the selected stock: one for the close price and the other for the trading volume. The charts are interactive and users can zoom in and out to get a better view of the data.

How to run the code: 

1. Install the required libraries by running the following command in your terminal or command prompt: `pip install streamlit yfinance`
2. Fork repo to your github, clone it to your local computer
3. Open a terminal or command prompt in the directory where the Python file is saved.
4. Run the following command to start the app:`streamlit run stock_price.py`
5. Streamlit should automatically open the app in a new tab in your default web browser. If it doesn't, you can copy the URL displayed in the terminal and paste it into your web browser.
6. Select a stock from the drop-down menu, choose a start and end date for the data, and select a data interval.
7. The app will display two line charts for the selected stock: one for the close price and the other for the trading volume. You can interact with the charts by zooming in and out to get a better view of the data.
