from item import Item
class Armor(Item):
    def __init__(self, x, y, name, desc, image_path):
        super().__init__(x, y, name, desc, image_path)