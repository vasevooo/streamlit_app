import yfinance as yf
import streamlit as st


st.header ('Simple App showing Prices and Trading Volumes of selected stocks')


###########
# sidebar #
###########

option = st.sidebar.selectbox('Select one symbol', ( 'AAPL', 'MSFT',"SPY",'WMT', 'GOOGL'))


import datetime

today = datetime.date.today()
before = today - datetime.timedelta(days=700)
start_date = st.sidebar.date_input('Start date', before)
end_date = st.sidebar.date_input('End date', today)
user_interval = st.sidebar.selectbox ('Select data interval', ('1d','1wk','1mo', '3mo'))
if start_date < end_date:
    st.sidebar.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
else:
    st.sidebar.error('Error: End date must fall after start date.')


##############
# Stock data #
##############

# Download data
df = yf.download(option,start= start_date,end= end_date, progress=False, interval=user_interval)
stock_name = yf.Ticker(option).info['longName']

###################
# Set up main app #
###################

st.write(f'{stock_name} Stock Close Price')
st.line_chart(df.Close)

st.write(f'{stock_name} Stock Volume')
st.line_chart(df.Volume)


# credits: https://python.plainenglish.io/building-a-stock-market-app-with-python-streamlit-in-20-minutes-2765467870ee