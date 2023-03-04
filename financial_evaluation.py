from yahoofinancials import YahooFinancials as yf
import pandas as pd
import numpy as np
import pprint as pp


# Code borrowed from MS&E 245A project in the fall 2022 quarter

def createPriceList(ticker, start_date, end_date, time_interval):
    financialsObject = yf(ticker)
    priceHistory = financialsObject.get_historical_price_data(start_date, end_date, time_interval)

    return pd.DataFrame(priceHistory[ticker]['prices'])[['formatted_date', \
                                                         'adjclose']].rename(
        columns={'adjclose': 'adjclose' + ticker}).set_index('formatted_date')


def getSharpeRatio(ticker, start_date, end_date, time_interval):
    # Get IRX returns as baseline
    IRX_Log_Returns = np.log(createPriceList('^IRX', start_date, end_date, time_interval) / 100. + 1.) / 252.
    ticker_Log_Returns = np.log(createPriceList(ticker, start_date, end_date, time_interval))

    merged_returns = pd.merge(IRX_Log_Returns, ticker_Log_Returns, left_index=True, right_index=True)
    merged_returns.dropna(inplace=True)
    # Get stock returns
    merged_returns['adjclose' + ticker] = merged_returns['adjclose' + ticker].diff()
    merged_returns = merged_returns.iloc[1:]
    # Get excess returns
    merged_returns['excess_return'] = merged_returns['adjclose' + ticker] - merged_returns['adjclose^IRX']

    return np.mean(merged_returns['excess_return']) / np.std(merged_returns['excess_return'])

# Will use this method to compare our allocation and performance to the S&P 500
#print(getSharpeRatio('^BTC', '2012-06-01', '2022-05-31', 'daily'))