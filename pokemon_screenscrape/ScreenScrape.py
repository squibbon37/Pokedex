__author__ = 'Captain Vasoline'

from bs4 import BeautifulSoup
import urllib.request

generation = ["I", "II", "III", "IV", "V", "VI"]


def scrapescreen():
    for version in generation:
        print(version)
        url = "http://pokemon.wikia.com/wiki/Category:Generation_" + version + "_Pok%C3%A9mon"
        content = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(content)
        getpokemonforgeneration(soup)


def getpokemonforgeneration(html):
    for pokemon in html.find_all("div", {"class": 'lightbox-caption'}):
        number = pokemon.contents[0]
        name = pokemon.contents[1].text
        type1 = pokemon.contents[3].text
        fullPokemon = [number, name, type1]

        if len(pokemon.contents) > 4:
            type2 = pokemon.contents[5].text
            fullPokemon.append(type2)

        print(fullPokemon)

scrapescreen()