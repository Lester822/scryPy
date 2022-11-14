import json
import requests

class CardList:
    '''CARD LIST TYPE'''
    def __init__(self, listcontent):
        self.total_cards = listcontent['total_cards']
        self.data = listcontent['data']
        self.cards_val = []  # List of cards in cardlist
        for entry in self.data:
            self.cards_val.append(Card(entry))
    def card_count(self):
        return self.total_cards
    def advanced_data(self):
        return self.data
    def cards(self):
        return self.cards_val
    def first_card(self):
        return self.cards_val[0]

class Card():
    '''CARD TYPE'''
    def __init__(self, card_data):
        if 'name' in card_data:
            self.name_internal = card_data['name']
        else:
            self.name_internal = None
        if 'prices' in card_data:  # Checks if there are prices
            if card_data['prices']['usd'] != None:  # Makes sure price is there
                self.price_internal = float(card_data['prices']['usd'])  # Sets internal price to the price
            else:
                self.price_internal = None  # Sets to none if there is no price
            if card_data['prices']['usd_foil'] != None:
                self.price_foil_internal = float(card_data['prices']['usd_foil'])
            else:
                self.price_foil_internal = None

        if 'set' in card_data:
            self.set_internal = card_data['set']
        else:
            self.set_internal = 'NONE'
        self.data_internal = card_data
    def name(self):
        return self.name_internal
    def price(self):
        return self.price_internal
    def price_foil(self):
        return self.price_foil_internal
    def set(self):
        return self.set_internal
    def __str__(self):
        return f'NAME: {self.name}\nSET: {self.set.upper()}\nUSD PRICE: {self.price}'
    def __repr__(self):
        return f'NAME: {self.name} SET: ({self.set.upper()}) USD PRICE: {self.price}'

def search_request(link):
    '''Send Scryfall Request and Return CARDLIST'''
    response = requests.get(link)
    response = response.content.decode('utf8')
    data = json.loads(response)
    cardlist = CardList(data)
    return cardlist

def card_request(link):
    response = requests.get(link)
    response = response.content.decode('utf8')
    data = json.loads(response)
    cardOut = Card(data)
    return cardOut

def search(card_name):
    '''Search by card name -> Search Query'''
    link = f'http://api.scryfall.com/cards/search?q=name={card_name}'
    return search_request(link)

def search_text(text):
    '''Search by card text -> Search Query'''
    link = f'http://api.scryfall.com/cards/search?q=o={text}'
    return search_request(link)

def advanced_search(args):
    '''Search with advanced terms -> Search Query'''
    link = f'http://api.scryfall.com/cards/search?q{args}'
    return search_request(link)


def exact_search(card_name):
    '''Search by EXACT card name -> Singular Card'''
    link = f'http://api.scryfall.com/cards/search?q=!"{card_name}"'
    return search_request(link).first_card()

def card_versions(card_name):
    '''Search by EXACT card name -> Search Query (including all variants)'''
    link = f'http://api.scryfall.com/cards/search?q=%21"{card_name}"+include%3Aextras&unique=prints'
    return search_request(link)

def random_card():
    '''Get random card and return CARD type -> Singular Card'''
    link = f'https://api.scryfall.com/cards/random'
    return card_request(link)

