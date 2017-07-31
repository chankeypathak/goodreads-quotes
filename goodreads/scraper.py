import requests
from bs4 import BeautifulSoup

class GoodReads(object):
    def __init__(self):
        print "Starting..."

    def get_quotes(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "lxml")
        quotes = [quote.text.strip().split("\n")[0] for quote in soup.findAll('div', {'class':'quoteText'})]
        return quotes


if __name__ == '__main__':
    url = 'https://www.goodreads.com/quotes'
    scraper = GoodReads()
    for quote in scraper.get_quotes(url):
        print quote
