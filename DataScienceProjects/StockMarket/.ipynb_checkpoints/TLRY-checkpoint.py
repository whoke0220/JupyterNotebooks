import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta
import plotly.graph_objects as go
import plotly.express as px

today = date.today()
d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days=365)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2

data = yf.download('TLRY',
                   start = start_date,
                   end = end_date, 
                   progress = False)

data["Date"] = data.index
data = data[["Date", "Open", "High", "Low",
             "Close", "Adj Close", "Volume"]]
data.reset_index(drop = True, inplace = True)
print(data.head())

candlestick_chart = go.Figure(data = [go.Candlestick(x = data['Date'],
                                                      open = data['Open'],
                                                      high = data['High'],
                                                      low = data['Low'],
                                                      close = data['Close'])
                                      ]
                              )
candlestick_chart.update_layout(title = 'Tilray Stock Price Analysis',
                                xaxis_rangeslider_visible = False)
candlestick_chart.show()

bar_plot = px.bar(data,
                  x = 'Date',
                  y = 'Close')
bar_plot.show()

line_chart_slider = px.line(data,
                            x = 'Date',
                            y = 'Close',
                            title = 'Stock Market Analysis with Rangeslider')
line_chart_slider.update_xaxes(rangeslider_visible = True)
line_chart_slider.show()

time_selectors = px.line(data, 
                 x = 'Date',
                 y = 'Close',
                 title = 'Stock Market Analysis with Time Period Selectors')

time_selectors.update_xaxes(
    rangeselector = dict(
        buttons = list([
            dict(count = 1, 
                 label = '1m',
                 step = 'month',
                 stepmode = 'backward'),
            dict(count = 6,
                 label = '6m', 
                 step = 'month',
                 stepmode = 'backward'),
            dict(count = 3,
                 label = '3m',
                 step = 'month',
                 stepmode = 'backward'),
            dict(count = 1,
                 label = '1y', 
                 step = 'year',
                 stepmode = 'backward'),
            dict(step = 'all')
        ])
    )
)

time_selectors.show()

scatter = px.scatter(data, 
                     x = 'Date',
                     y = 'Close',
                     range_x = ['2023-05-30', '2024-05-31'],
                     title = 'Stock Market Analysis by Hiding Weekend Gaps')
scatter.update_xaxes(
    rangebreaks = [
        dict(bounds = ['sat', 'sun'])
    ]
)
scatter.show()
