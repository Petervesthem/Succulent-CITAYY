class Enemy:

    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
    
    def move(self):
        self.x += self.speed
    

    def draw(self, screen, image):
        screen.blit(image, (self.x, self.y))


