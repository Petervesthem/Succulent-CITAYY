import pygame

class Text:
    def __init__(self, text, x, y, font_size=30, color=(255, 255, 255), font_path=None):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.font = pygame.font.Font(font_path, font_size)
        self.rendered_text = self.font.render(self.text, True, self.color)
        self.rect = self.rendered_text.get_rect(topleft=(x, y))

    
    def draw(self,screen):
        screen.blit(self.rendered_text, self.rect.topleft)

    
    def update_text(self, new_text):
        self.text = new_text
        self.rendered_text = self.font.render(self.text, True, self.color)