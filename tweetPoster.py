import tweepy
import webbrowser
from ConfigParser import SafeConfigParser

# Call this function if you need to get access tokens
def getAccessTokens():

    config = SafeConfigParser()
    config.read('config.ini')

    try:
        consumerKey = config.get('auth', 'consumerKey')
        consumerSecret = config.get('auth', 'consumerSecret')
    except:
        print "Error! Could not find consumer key or consumer secret"

    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    try:
        redirect_url = auth.get_authorization_url()
        print redirect_url
        webbrowser.open(redirect_url)
    except tweepy.TweepError:
        print 'Error! Failed to get request token.'

    verifier = raw_input('Verifier PIN:')

    try:
        auth.get_access_token(verifier)
    except tweepy.TweepError:
        print 'Error! Failed to get access token.'

    config = SafeConfigParser()
    config.read('config.ini')
    config.set('auth', 'accessKey', auth.access_token)
    config.set('auth', 'accessSecret', auth.access_token_secret)
    with open('config.ini', 'w') as f:
        config.write(f)

# Call this function to post a tweet
def postTweet(tweetText):

    config = SafeConfigParser()
    config.read('config.ini')

    try:
        consumerKey = config.get('auth', 'consumerKey')
        consumerSecret = config.get('auth', 'consumerSecret')
    except:
        print "Error! config.ini must contain the consumer key and consumer secret."
        config.add_section('auth')
        config.set('auth', 'consumerKey', '')
        config.set('auth', 'consumerSecret', '')
        with open('config.ini', 'w') as f:
            config.write(f)

    try:
        acessKey = config.get('auth', 'accessKey')
        accessSecret = config.get('auth', 'accessSecret')
    except:
        getAccessTokens()
        config.read('config.ini')
        acessKey = config.get('auth', 'accessKey')
        accessSecret = config.get('auth', 'accessSecret')

    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(acessKey, accessSecret)
    api = tweepy.API(auth)

    try:
        api.update_status('tweetText')
    except tweepy.TweepError:
        print 'Error! Failed to post status update.'
