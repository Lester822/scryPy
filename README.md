# ScryPy
A Python wrapper for the Scryfall API

Using ScryPy you can look up Magic: The Gathering cards through any Scryfall search term.

Instructions:

1. Download the files from above and import scrypy.py into your project
2. Install requests in order to have scrypy function.
3. Start using scrypy, by using the documentation below.

How To Use:

ScryPy functions primarly using two main data types, "CardLists" and "Cards". These can be generated in several ways, but most inquires result in "CardLists" that contain many cards within them.

# Generating Card Lists and Cards

There are several ways to generate both CardLists and Cards.

To generate CardLists you can use any of the following:
1. scrypy.name_search(CARDNAME) -> A Card List with every card that matches the name (including partial matches, no duplicates)
2. scrypy.oracle_search(TEXT) -> A Card List with every card that matches the text in the rules text (including partial matches, no duplicates)
3. scrypy.advanced_search(ARGS) -> A Card List with every card that matches the given Scryfall created arguments
4. scrypy.get_printings(CARD) -> A Card List of every version of a Card object that was passed in (for example, if you passed in a Shock Card objecet, it would return a Card List with every version of Shock)

To generate individual cards, you can access Card Lists or use any of the following:
1. scrypy.get_card(CARDNAME) -> A Card with the exact name (will pull the most recent printing)
2. scrypy.random_card() -> A Card generated randomly

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
