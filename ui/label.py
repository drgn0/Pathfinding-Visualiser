import pygame 

from .my_sprite import MySprite 
from constants import LABEL_TEXT_COLOR

font = pygame.font.Font(None, 24)  


class Label(MySprite):
    def __init__(self, text: str):
        super().__init__() 

        self.set_image(font.render(text, False, LABEL_TEXT_COLOR)) 

        