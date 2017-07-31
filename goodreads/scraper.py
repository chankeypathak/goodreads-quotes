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


if __name__ == '__main__':
    suffix = ''
    print "Welcome! Choose the option to proceed"
    choice = input("1. Popular\n2. Recently added")
    if choice == 2:
        suffix = 'recently_added'
    url = 'https://www.goodreads.com/quotes/{}'.format(suffix)
    scraper = GoodReads()
    for quote in scraper.get_quotes(url):
        print quote
