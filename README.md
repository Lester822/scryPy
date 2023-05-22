# ScryPy
A Python wrapper for the Scryfall API

Using ScryPy you can look up Magic: The Gathering cards through any Scryfall search term.

Instructions:

1. Download the files from above and import scrypy.py into your project
2. Install requests in order to have scrypy function.
3. Start using scrypy, by using the documentation below.

How To Use:

ScryPy functions primarly using a data type called "Card" which represents a singular printing of a Magic: The Gathering card.

# Generating Card Lists and Cards

There are several ways to get Cards, with most resulting in a list of Cards that matches the search result.

## You can get a singular card object individually using any of these:
    `scrypy.get_card()` returns a card object with the EXACT given name
    `scrypy.random_card()` returns a card at random from all possible Magic cards

## You can get a list of cards based on a specific search using any of these:
    `scrypy.name_search(card_name)` | Search based on given card name
    `scrypy.oracle_search(oracle_text)` | Search based on given card text (oracle)
    `scrypy.color_search(colors, search_type)` | Search based on card color in WUBRG standard formatting.
    `scrypy.type_search(card_type)` | Search based on given type
    `scrypy.set_search(set)` | Search based on given set
    `scrypy.advanced_search(arguments)` | Search using any scryfall syntax
    `scrypy.get_printings(card)` | Search for all other printings of given card object


# Using CardLists and Cards

Every CardList has several methods that can be used to get data from them.

You can use:
1. CardList.cards() to get a list of every Card object in the CardList
2. CardList.first_card() to get the first Card in the CardList (most recent)
3. CardList.card_count() to get the number of Card objects in the CardList


Every Card itself also have several methods that can be used to get data. NOTE: A Card type refers to a specific printing on a specific Scryfall page, not EVERY card with that name.

You can use:
1. Card.name() to get the cards name
2. Card.data() to get all of the details provided by scryfall including things like mtgo_id, color, mana value, etc. (many of these may come to quick methods later)
3. Card.overview() to get a string with the key details of the cards

That's it, expect more updates soon including easier searching.
