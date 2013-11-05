__author__ = 'Captain Vasoline'

from bs4 import BeautifulSoup
import urllib.request
import sqlite3

generation = ["I", "II", "III", "IV", "V", "VI"]

db = sqlite3.connect('../pokedexDB.db')
cur = db.cursor()


def scrapescreen():
    createtable()
    for version in generation:
        url = "http://pokemon.wikia.com/wiki/Category:Generation_" + version + "_Pok%C3%A9mon"
        content = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(content)
        getpokemonforgeneration(soup)

    cur.execute('SELECT * FROM Pokemon')
    test = cur.fetchall()
    print(test)

    db.commit()
    db.close()
    print('You caught em all!')


def createtable():
    cur.execute('DROP TABLE IF EXISTS Pokemon')

    cur.execute('''CREATE TABLE IF NOT EXISTS Pokemon(
                    Number TEXT, Name TEXT, Type_1 TEXT, Type_2 TEXT)''')


def getpokemonforgeneration(html):
    for pokemon in html.find_all("div", {"class": 'lightbox-caption'}):
        number = pokemon.contents[0]
        name = pokemon.contents[1].text
        type1 = pokemon.contents[3].text
        fullPokemon = [number, name, type1]

        if len(pokemon.contents) > 4:
            type2 = pokemon.contents[5].text
            fullPokemon.append(type2)

        if len(fullPokemon) < 4:
            cur.execute('INSERT INTO Pokemon VALUES (?,?,?, NULL)', fullPokemon)

        if len(fullPokemon) > 3:
            cur.execute('INSERT INTO Pokemon VALUES (?,?,?,?)', fullPokemon)

scrapescreen()