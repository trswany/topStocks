"""Script to find top stocks and post them to Twitter."""
import sys
import tweetPoster
""" Max, import your library here """

def main():
    """ Max, call your library and set 'tweetText' to the text you want to post """
    tweetPoster.postTweet(tweetText)
    pass

if __name__ == '__main__':
    sys.exit(main())
