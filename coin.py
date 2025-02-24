from item import Item
class Coin(Item):
    def __init__(self, x, y, name, desc, image_path):
        super().__init__(x,y,name,desc,image_path)

    #Dont know what this should do yet or if it is even useful
    def use(self,player):
        raise NotImplementedError("doesnt work")


    def draw(self, screen):
        screen.blit(self.image_path, (self.x, self.y))