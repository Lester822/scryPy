class Card:
    def __init__(self, data):
        self._data = data

    def data(self):
        """Return a dictonary with all the card data in it"""
        return self._data

    def overview(self):
        """Return a formatted output with all critical details"""
        output = f'{self.name()} - {self.set_code()}'
        if self._data["mana_cost"] != "":
            output += f'- {self._data["mana_cost"]}'
        output += f'\n{self._data["type_line"]}\n{self._data["oracle_text"]}'
        if 'power' in self._data:
            output += f'\n{self._data["power"]}/{self._data["toughness"]}'
        return output

# Data Retrieval
    def artist(self):
        if "artist" in self._data.keys():
            return self._data["artist"]
        else:
            raise LookupError('Card has no value "artist"')

    def attraction_lights(self):
        if "attraction_lights" in self._data.keys():
            return self._data["attraction_lights"]
        else:
            raise LookupError('Card has no value "attraction_lights"')

    def booster(self):
        if "booster" in self._data.keys():
            return self._data["booster"]
        else:
            raise LookupError('Card has no value "booster"')

    def border_color(self):
        if "border_color" in self._data.keys():
            return self._data["border_color"]
        else:
            raise LookupError('Card has no value "border_color"')
    
    def card_back_id(self):
        if "card_back_id" in self._data.keys():
            return self._data["card_back_id"]
        else:
            raise LookupError('Card has no value "card_back_id"')
        
    def collector_number(self):
        if "collector_number" in self._data.keys():
            return self._data["collector_number"]
        else:
            raise LookupError('Card has no value "collector_number"')
    
    def content_warning(self):
        if "content_warning" in self._data.keys():
            return self._data["content_warning"]
        else:
            raise LookupError('Card has no value "content_warning"')
    
    def digital(self):
        if "digital" in self._data.keys():
            return self._data["digital"]
        else:
            raise LookupError('Card has no value "digital"')
    
    def finishes(self):
        if "finishes" in self._data.keys():
            return self._data["finishes"]
        else:
            raise LookupError('Card has no value "finishes"')
    
    def flavor_name(self):
        if "flavor_name" in self._data.keys():
            return self._data["flavor_name"]
        else:
            raise LookupError('Card has no value "flavor_name"')
    
    def flavor_text(self):
        if "flavor_text" in self._data.keys():
            return self._data["flavor_text"]
        else:
            raise LookupError('Card has no value "flavor_text"')
    
    def frame_effects(self):
        if "frame_effects" in self._data.keys():
            return self._data["frame_effects"]
        else:
            raise LookupError('Card has no value "frame_effects"')
    
    def frame(self):
        if "frame" in self._data.keys():
            return self._data["frame"]
        else:
            raise LookupError('Card has no value "frame"')
    
    def full_art(self):
        if "full_art" in self._data.keys():
            return self._data["full_art"]
        else:
            raise LookupError('Card has no value "full_art"')
    
    def games(self):
        if "games" in self._data.keys():
            return self._data["games"]
        else:
            raise LookupError('Card has no value "games"')
    
    def highres_image(self):
        if "highres_image" in self._data.keys():
            return self._data["highres_image"]
        else:
            raise LookupError('Card has no value "highres_image"')
    
    def illustration_id(self):
        if "illustration_id" in self._data.keys():
            return self._data["illustration_id"]
        else:
            raise LookupError('Card has no value "illustration_id"')
    
    def image_status(self):
        if "image_status" in self._data.keys():
            return self._data["image_status"]
        else:
            raise LookupError('Card has no value "image_status"')
    
    def image_uris(self):
        if "image_uris" in self._data.keys():
            return self._data["image_uris"]
        else:
            raise LookupError('Card has no value "image_uris"')
## HERE https://scryfall.com/docs/api/cards
    def name(self):
        if "name" in self._data.keys():
            return self._data["name"]
        else:
            raise LookupError('Card has no value "name"')
        
    def set_code(self):
        if "set" in self._data.keys():
            return self._data["set"]
        else:
            raise LookupError('Card has no value "set_code"')
        
    def __str__(self):
        return f"{self.name()} ({self.set_code()})"

    def __repr__(self):
        return f"{self.name()} ({self.set_code()})"

    def __eq__(self, other):
        return self._data['name'] == other.data()['name']