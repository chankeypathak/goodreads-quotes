import requests
from bs4 import BeautifulSoup

class GoodReads(object):
    def __init__(self):
        print "Quotes:"

    def get_quotes(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "lxml")
        quotes = [quote.text.strip().split("\n")[0] for quote in soup.findAll('div', {'class': 'quoteText'})]
        return quotes
