import json
import requests

from cardlist import CardList
from card import Card


def _card_list_search(link):
    """Send Scryfall Request and Return A CardList object"""
    response = requests.get(link)
    response = response.content.decode('utf8')
    data = json.loads(response)
    if 'status' not in data.keys():
        card_list = []
        for card in data['data']:
            card_list.append(Card(card))
        return card_list
    else:
        raise Exception(f'No Cards Found With Parameter at link {link}')


def _card_search(link):
    """Send Scryfall Request and Return A Card object"""
    response = requests.get(link)
    response = response.content.decode('utf8')
    data = json.loads(response)
    if 'status' not in data.keys():
        card = data['data'][0]  # The first result in the returned card list
        return card
    else:
        raise Exception(f'No Cards Found With Parameter at link {link}')


def random_card():
    """Return a random card as a Card object"""
    response = requests.get('https://api.scryfall.com/cards/random')
    response = response.content.decode('utf8')
    data = json.loads(response)
    return Card(data)


def get_card(card_name):
    """Return a Card Object for a card with the exact given name"""
    return _card_search(f'http://api.scryfall.com/cards/search?q=!"{card_name}"')

# Search Methods // Lists

def name_search(card_name):
    """Return a CardList of all results with name search"""
    return _card_list_search(f'http://api.scryfall.com/cards/search?q=name={card_name}')


def oracle_search(oracle_text):
    """Return a CardList of all results with oracle text search"""
    return _card_list_search(f'http://api.scryfall.com/cards/search?q=o="{oracle_text}"')

def color_search(colors, search_type='exact'):
    """Return a CardList of all results with color search"""
    if search_type == 'exact':
        oper = '='
    elif search_type == 'at least':
        oper = '>='
    elif search_type == 'at most':
        oper = '<='
    elif search_type == 'up to':
        oper = '<'
    elif search_type == 'more than':
        oper = '>'
    else:
        raise LookupError(f'Invalid color search type {search_type}')
    return _card_list_search(f'http://api.scryfall.com/cards/search?q=color{oper}"{colors}"')

def type_search(card_type):
    """Return a CardList of all results with the type or subtype given"""
    return _card_list_search(f'http://api.scryfall.com/cards/search?q=type="{card_type}"')


def set_search(set):
    """Return a CardList of all results from a given set"""
    return _card_list_search(f'http://api.scryfall.com/cards/search?q=set={set}')


def advanced_search(arguments):
    """Return a CardList of all results with advanced argument search (using Scryfall args)"""
    return _card_list_search(f'http://api.scryfall.com/cards/search?q={arguments}')


def get_printings(card):
    """Return a CardList of all other versions of an inputted Card object"""
    return _card_list_search(f'http://api.scryfall.com/cards/search?q=%21"{card.name()}"+include%3Aextras&unique=prints')


