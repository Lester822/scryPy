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
        card_list = CardList(data)
        return card_list
    else:
        raise Exception(f'No Cards Found With Parameter at link {link}')


def _card_search(link):
    """Send Scryfall Request and Return A Card object"""
    response = requests.get(link)
    response = response.content.decode('utf8')
    data = json.loads(response)
    print(data)
    if 'status' not in data.keys():
        card = CardList(data).first_card()
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


def name_search(card_name):
    """Return a CardList of all results with name search"""
    return _card_list_search(f'http://api.scryfall.com/cards/search?q=name={card_name}')


def oracle_search(text):
    """Return a CardList of all results with oracle text search"""
    return _card_list_search(f'http://api.scryfall.com/cards/search?q=o="{text}"')


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


