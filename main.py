import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

aapl = yf.Ticker('AAPL')

days = 20
aapl.history()