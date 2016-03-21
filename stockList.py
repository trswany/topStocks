from ftplib import FTP
import csv

# Download the NASDAQ's list of stock symbols
def fetchNASDAQfile():
    print "Fetching NASDAQ file..."
    try:
        ftp = FTP('ftp.nasdaqtrader.com')
        ftp.login()
        ftp.cwd('SymbolDirectory')
        ftp.retrbinary('RETR nasdaqlisted.txt', open('nasdaqlisted.txt', 'wb').write)
        print("Done fetching NASDAQ file.")
    except:
        print("Error! Could not fetch list of NASDAQ stock symbols.")

# Reads the NASDAQ file, parses it, and returns a list of all stock symbols
def parseNASDAQfile():
    print "Parsing NASDAQ file..."
    list = []
    # Open the file and grab the first column
    with open('nasdaqlisted.txt', 'rb') as csvfile:
        symbolReader = csv.reader(csvfile, delimiter='|', quotechar='"')
        for row in symbolReader:
            list = list + [row[0]]
    print("Done parsing NASDAQ file.")
    return list

# Returns a list of all stock symbols
def getStockList():
    fetchNASDAQfile()
    return parseNASDAQfile()
