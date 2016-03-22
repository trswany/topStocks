"""Find top stocks and post them to Twitter."""
import sys
import tweetPoster
import stockPrices
from stockList import getStockList
import time

def main():
    # Get the list of stock symobls
    currentStockList = getStockList()

    # Get the stock prices
    oldStockPrices = stockPrices.getStockPrices(currentStockList)

    # Wait a while for the stock prices to change
    print("Sleeping...")
    time.sleep(30)
    print("Done sleeping.")

    # Get the new stock prices
    currentStockPrices = stockPrices.getStockPrices(currentStockList)

    # Find the fastest-changing stocks
    topStockPrices = stockPrices.getFastestChangingPrices(currentStockPrices, oldStockPrices)

    # Format the tweet text
    tweetText = ""
    for stockPrice in topStockPrices:
        symbol  = stockPrice[0]
        percentage = round(float(stockPrice[1]), 2)
        if percentage > 0:
            percentage = '+' + str(percentage)
        else:
            percentage = str(percentage)
        tweetText = tweetText + '#' + symbol + " : " + percentage + '%, '

    # Post a tweet of the top stocks
    print tweetText
    tweetPoster.postTweet(tweetText)

if __name__ == '__main__':
    sys.exit(main())
