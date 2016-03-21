
# Download the NASDAQ's list of stock symbols
def fetchNASDAQfile():
    print "Fetching NASDAQ file."


# Reads the NASDAQ file, parses it, and returns a list of all stock symbols
def parseNASDAQfile():
    print "Parsing NASDAQ file."


# Returns a list of all stock symbols
def getStockList():
    fetchNASDAQfile()
    return parseNASDAQfile()
