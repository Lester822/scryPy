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

You can get a singular card object individually using any of these:  
  
    `scrypy.get_card()` returns a card object with the EXACT given name  
    `scrypy.random_card()` returns a card at random from all possible Magic cards  

You can get a list of cards based on a specific search using any of these:  
  
    `scrypy.name_search(card_name)` | Search based on given card name  
    `scrypy.oracle_search(oracle_text)` | Search based on given card text (oracle)  
    `scrypy.color_search(colors, search_type)` | Search based on card color in WUBRG standard formatting. Search type defaults to EXACT match,  but can be "exact" "at least" "at most" "up to" and "more than" by inputting those as strings into search_type.  
    `scrypy.type_search(card_type)` | Search based on given type  
    `scrypy.set_search(set)` | Search based on given set  
    `scrypy.advanced_search(arguments)` | Search using any scryfall syntax  
    `scrypy.get_printings(card)` | Search for all other printings of given card object  


# Using Cards

Every Card has many built in methods to retrieve information about the Card. If the Card does not have the requested information (for example, the power of an instant) a 'LookupError' is raised.

You can get the following information:
'card.all_parts()' | List | If this card is closely related to other cards, this property will be an array with Related Card Objects.  
'card.card_faces()' | List | A list of Card Face objects, if this card is multifaced.  
'card.cmc()' | Float | 	The card’s mana value. Note that some funny cards have fractional mana costs.  
'card.color_identity()' | String | This card’s color identity.  
'card.color_indicator()'| String | The colors in this card’s color indicator, if any. A null value for this field indicates the card does not have one..  
'card.colors()'| String | This card’s colors, if the overall card has colors defined by the rules. Otherwise the colors will be on the card_faces objects, see below.  
'card.edhrec_rank()' | Int | This card’s overall rank/popularity on EDHREC. Not all cards are ranked.  
'card.hand_modifier()' | String | This card’s hand modifier, if it is Vanguard card. This value will contain a delta, such as -1.  
'card.keywords()' | List | 	A list of keywords that this card uses, such as 'Flying' and 'Cumulative upkeep'.
'card.layout()'  | String | A code for this card’s layout.
'card.legalities()' | Object | An object describing the legality of this card across play formats. Possible legalities are legal, not_legal, restricted, and banned.
'card.life_modifier()' | String | This card’s life modifier, if it is Vanguard card. This value will contain a delta, such as +2.
'card.loyalty()'
'card.mana_cost()'
'card.name()'
'card.oracle_text()'
'card.oversized()'
'card.penny_rank()'
'card.power()'
'card.produced_mana()'
'card.reserved()'
'card.toughness()'
'card.type_line()'
