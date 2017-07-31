from util.goodreads import GoodReads

if __name__ == '__main__':
    suffix = ''
    print "Welcome! Choose the option to proceed"
    choice = input("1. Popular\n2. Recently added\n")
    if choice == 2:
        suffix = 'recently_added'
    url = 'https://www.goodreads.com/quotes/{}'.format(suffix)
    scraper = GoodReads()
    for quote in scraper.get_quotes(url):
        print quote
