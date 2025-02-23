from item import Item
class HealthPotion(Item):
    def __init__(self, x, y, name, desc, image_path):
        #replace name desc and image path to actual ones
        super().__init__(x, y, name, desc, image_path)

    
    def use(self,player):
        #player.health += 20
        pass