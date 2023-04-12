from card import Card


class CardList:
    def __init__(self, data):
        self._data = data  # The actual data of the cards
        self._cards = self.assemble_cards()

    def assemble_cards(self):
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

    def in_both(self, other):
        """Return a CardList of cards that are in both CardLists"""
        combined = []
        for card in self._cards:
            for other_card in other.cards():
                print(other_card, card)
                if card == other_card:
                    combined.append(card)
        return combined


    def __str__(self):
        return str(self._cards)

