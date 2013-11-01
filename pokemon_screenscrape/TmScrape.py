__author__ = 'Captain Vasoline'

from bs4 import BeautifulSoup
import urllib.request


def scrapescreen():
    url = "http://bulbapedia.bulbagarden.net/wiki/List_of_moves"
    content = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(content)
    getmovelist(soup)


def getmovelist(html):
    moveList = html.find('table').find_next_sibling('table')
    test = moveList.contents[1].contents[1].contents[1]
    for thing in test.find('tr'):
        print(thing)
    #print(test)
        #for moveInfo in move.find('td'):
         #   print(moveInfo)


scrapescreen()
