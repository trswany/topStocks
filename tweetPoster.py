import tweepy
import webbrowser
from ConfigParser import SafeConfigParser

# Call this function if you need to get access tokens
def getAccessTokens():

    # Initialize the config parser and open the config.ini file
    config = SafeConfigParser()
    config.read('config.ini')

    # Try to load the consumer keys. These tell Twitter which app we are.
    # We need these before we request access to a user's account.
    try:
        consumerKey = config.get('auth', 'consumerKey')
        consumerSecret = config.get('auth', 'consumerSecret')
    except:
        print "Error! Could not find consumer key or consumer secret"

    # If the consumer keys are blank, ask the user to add them.
    if consumerKey == '' or consumerSecret == '':
        print "Error! Consumer keys are blank. Please add them to config.ini."

    # Use the consumer keys to request a verifier PIN from Twitter.
    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    try:
        redirect_url = auth.get_authorization_url()
        print redirect_url
        webbrowser.open(redirect_url)
    except tweepy.TweepError:
        print 'Error! Failed getting request token from Twitter.'

    # Ask the user to input the PIN that Twitter provides
    verifier = raw_input('Visit the URL above and enter the Twitter PIN:')

    # Try to get access tokens using the Twitter PIN
    try:
        auth.get_access_token(verifier)
    except tweepy.TweepError:
        print 'Error! Failed to get access token.'

    # Save the access keys. These are blank if we failed to get them.
    config = SafeConfigParser()
    config.read('config.ini')
    config.set('auth', 'accessKey', auth.access_token)
    config.set('auth', 'accessSecret', auth.access_token_secret)
    with open('config.ini', 'w') as f:
        config.write(f)

# Call this function to post a tweet
def postTweet(tweetText):

    # Open the config file
    config = SafeConfigParser()
    config.read('config.ini')

    # Try to get the consumer keys. If we can't, add blank entries to the config
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

    # Now try to get the access keys. If we can't, try to get them.
    try:
        acessKey = config.get('auth', 'accessKey')
        accessSecret = config.get('auth', 'accessSecret')
    except:
        getAccessTokens()
        config.read('config.ini')
        acessKey = config.get('auth', 'accessKey')
        accessSecret = config.get('auth', 'accessSecret')

    # Connect to the Twitter API
    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(acessKey, accessSecret)
    api = tweepy.API(auth)

    # Post the Tweet
    try:
        api.update_status(tweetText)
    except tweepy.TweepError:
        print 'Error! Failed to post status update.'
