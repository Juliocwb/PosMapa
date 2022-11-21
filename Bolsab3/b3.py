import pandas_datareader.data as web
import yfinance as yf
import datetime

yf.pdr_override()
start = datetime.datetime(2009, 1, 1)
end = datetime.datetime(2022, 11, 1)

df_ibov = web.get_data_yahoo('^BVSP',start,end)

df_ibov.tail()