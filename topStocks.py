"""Find top stocks and post them to Twitter."""
import sys
import tweetPoster
import stockPrices
from stockList import getStockList

def main():
    currentStockList = getStockList()
    currentStockPrices = dict()
	oldStockPrices = currentStockPrices
	currentStockPrices = stockPrices.getStockPrices(currentStockList)
    print currentStockPrices
	topStockPrices = stockPrices.getFastestChangingPrices(currentStockPrices, oldStockPrices)
    tweetText = "testTweet"
    #tweetPoster.postTweet(tweetText)
    pass

if __name__ == '__main__':
    sys.exit(main())
