"""Find top stocks and post them to Twitter."""
import sys
import tweetPoster
from stockList import getStockList
""" Max, import your library here """

def main():
    currentStockList = getStockList()
    """ Max, call your library and set 'tweetText' to the text you want to post """
    tweetText = "testTweet"
    #tweetPoster.postTweet(tweetText)
    pass

if __name__ == '__main__':
    sys.exit(main())
