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

## Cards have the following methods to return data
To see what is returned, check out Scryfall's page which describes each data type https://scryfall.com/docs/api/cards.
"""
'card.all_parts()'  
'card.card_faces()'  
'card.cmc()'  
'card.color_identity()'  
'card.color_indicator()'  
'card.colors()'  
'card.edhrec_rank()'  
'card.hand_modifier()'  
'card.keywords()'  
'card.layout()'  
'card.legalities()'  
'card.life_modifier()'  
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

'card.artist()'  
'card.attraction_lights()'  
'card.booster()'  
'card.border_color()'  
'card.card_back_id()'  
'card.collector_number()'  
'card.content_warning()'  
'card.digital()'  
'card.finishes()'  
'card.flavor_name()'  
'card.flavor_text()'  
'card.frame_effects()'  
'card.frame()'  
'card.full_art()'  
'card.games()'  
'card.highres_image()'  
'card.illustration_id()'  
'card.image_status()'  
'card.image_uris()'  
'card.prices()'  
'card.printed_name()'  
'card.printed_text()'  
'card.printed_type_line()'  
'card.promo()'  
'card.promo_types()'  
'card.purchase_uris()'  
'card.rarity()'  
'card.related_uris()'  
'card.released_at()'  
'card.reprint()'  
'card.scryfall_set_uri()'  
'card.set_name()'  
'card.set_search_uri()'  
'card.set_type()'  
'card.set_uri()'  
'card.set_code()'  
'card.set_id()'  
'card.story_spotlight()'  
'card.textless()'  
'card.variation()'  
'card.variation_of()'  
'card.security_stamp()'  
'card.watermark()'  
'card.preview_previewed_at()'  
'card.preview_source_uri()'  
'card.preview_source()'  
"""
## Cards Can Also...

'card.overview()' | Return a nicely formatting output for easy display  
'card.data()' | Return the scryfall given data, if there is something else you need to access  