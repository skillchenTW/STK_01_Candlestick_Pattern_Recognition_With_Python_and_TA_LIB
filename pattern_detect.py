import talib as ta
import yfinance as yf

data = yf.download("SPY",start="2020-01-01", end="2021-08-02")
print(data)

morning_stars = ta.CDLMORNINGSTAR(data['Open'],data['High'],data['Low'],data['Close'])
engulfing = ta.CDLENGULFING(data['Open'],data['High'],data['Low'],data['Close'])
data['morning_star'] = morning_stars
data['engulfing'] = engulfing
#print(morning_stars[morning_stars !=0])
engulfing_days = data[data['engulfing'] !=0]
print(engulfing_days)