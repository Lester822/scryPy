class Card:
    def __init__(self, data):
        self._name = data['name']
        self._set = data['set'].upper()
        self._data = data

    def data(self):
        """Return a dictonary with all the card data in it"""
        return self._data

    def name(self):
        """Return the Card's name"""
        return self._name

    def overview(self):
        """Return a formatted output with all critical details"""
        output = f'{self._name} - {self._set}'
        if self._data["mana_cost"] != "":
            output += f'- {self._data["mana_cost"]}'
        output += f'\n{self._data["type_line"]}\n{self._data["oracle_text"]}'
        if 'power' in self._data:
            output += f'\n{self._data["power"]}/{self._data["toughness"]}'
        return output

    def __str__(self):
        return f"{self._name} ({self._set})"

    def __repr__(self):
        return f"{self._name} ({self._set})"
