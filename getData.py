import yfinance as yf

BTC_Ticker = yf.Ticker("BTC-USD")
BTC_Data = BTC_Ticker.history(period="5y")
BTC_Data.to_csv('daily_BTC.csv')

ETH_Ticker = yf.Ticker("ETH-USD")
ETH_Data = ETH_Ticker.history(period="5y")
ETH_Data.to_csv('daily_ETH.csv')

LTC_Ticker = yf.Ticker("LTC-USD")
LTC_Data = LTC_Ticker.history(period="5y")
LTC_Data.to_csv('daily_LTC.csv')