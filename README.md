# scryPy
A Python wrapper for the Scryfall API

Using scryPy you can look up Magic: The Gathering cards through any Scryfall search term.

Instructions:

1. Download scrypy.py and import it into your project
2. Install requests in order to have scrypy function.
3. Start using scrypy, by using the documentation below.

How To Use:

ScryPy functions primarly using two main data types, "Card Lists" and "Cards". These can be generated in several ways, but most inquires result in "Card Lists" that contain many cards within them.

# Generating Card Lists and Cards

There are several ways to generate both Card Lists and Cards.

To generate Card Lists you can use any of the following:
1. scrypy.search(CARDNAME) -> A Card List with every card that matches the name (including partial matches, no duplicates)
2. scrypy.search_text(TEXT) -> A Card List with every card that matches the text in the rules text (including partial matches, no duplicates)
3. scrypy.advanced_search(ARGS) -> A Card List with every card that matches the given Scryfall created arguments
4. scrypy.versions(CARDNAME) -> A Card List of every version of a card with the name exactly as printed (no partial matches, with duplicates)

To generate individual cards, you can access Card Lists or use any of the following:
1. scrypy.exact_search(CARDNAME) -> A Card with the exact name (will pull the most recent printing)
2. scrypy.random_card() -> A Card generated randomly

# Using Card Lists and Cards

Every Card List has several methods that can be used to get data from them.

You can use:
1. CardList.card_count() to get the number of cards in the results
2. CardList.cards() to get a list of every card object in the card list
3. CardList.first_card() to get the first card in the card list (most recent)
4. CardList.advnaced_data() to get the entire data pull from Scryfall including every card and all pieces of data about every card. (This is intended mostly for high-level usage.


Every Card itself also have several methods that can be used to get data. NOTE: A Card type refers to a specific printing on a specific Scryfall page, not EVERY card with that name.

You can use:
1. Card.name() to get the cards name
2. Card.price() to get the price of the card (usd)
3. Card.price_foil() to get the foil price of the card (usd)
4. Card.set() to get the set of the card.
5. Card.data_internal to get all of the details provided by scryfall including things like mtgo_id, color, mana value, etc. (many of these may come to quick methods later)
