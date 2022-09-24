import datetime
import time
import finnhub

token = "ccnkjn2ad3i3sjb7e72gccnkjn2ad3i3sjb7e730"

finnhub_client = finnhub.Client(api_key=token)
companies = {'apple':'AAPL','microsoft':'MSFT','google':'GOOG','amazon':'AMZN','tesla':'TSLA','meta':'META','nvidia':'NVDA'}

for company in companies:
    symbol = companies[company]

    #Include this basic information in the visualiser
    company_profile = finnhub_client.company_profile2(symbol=symbol)
    name = company_profile['name']
    country = company_profile['country']
    exchange = company_profile['exchange']
    currency = company_profile['currency']
    outstanding_shares = company_profile['shareOutstanding']
    market_capitalisation = company_profile['marketCapitalization']

    #Calculates the unix timestamps for the respective durations
    today = datetime.date.today()
    last_week = (today - datetime.timedelta(days=7)).timetuple()
    last_month = (today - datetime.timedelta(days=31)).timetuple()
    today = today.timetuple()

    start = time.mktime(today) #Change out for today,last_week,last_month based on the required interval of observation
    start = int(start)
    to = int(time.time())

    candle_stick_data = finnhub_client.stock_candles(symbol,'D',start,to)

    #Plot these as a candlestick model in the chart, with the unix timestamp on the x-axis
    close_price_and_time = list(zip(candle_stick_data['t'],candle_stick_data['c']))
    open_price_and_time = list(zip(candle_stick_data['t'],candle_stick_data['o']))
    high_price_and_time = list(zip(candle_stick_data['t'],candle_stick_data['h']))
    low_price_and_time = list(zip(candle_stick_data['t'],candle_stick_data['l']))

