from card import Card


class CardList:
    def __init__(self, data):
        self._data = data  # The actual data of the cards
        self._cards = self._assemble_cards()

    def _assemble_cards(self):
        """Return a list of card objects"""
        cards = []
        for card_data in self._data['data']:
            cards.append(Card(card_data))
        return cards

    def cards(self):
        """Return a list of all cards contained in CardList"""
        return self._cards

    def card_count(self):
        """Return how many cards are in CardList"""
        return len(self._cards)

    def first_card(self):
        """Return the first Card object in the list"""
        return self._cards[0]

    def __str__(self):
        return str(self._cards)

