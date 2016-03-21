#!/usr/bin/env python
from yahoo_finance import Share

def getStockPrices(stocks):
  #stocks must be an array of stock symbol strings
  
  # Refresh stock prices
  [Share(symbol).refresh() for symbol in stocks]
  
  # Return list of new prices
  return dict(zip(stocks,[Share(symbol).get_price() for symbol in stocks]))