import pygame 

from constants import BUTTON_TEXT_COLOR
from .my_sprite import MySprite 



font = pygame.font.Font(None, 24)  



class ButtonState:
    NOT_HOVERED_OVER = 0 
    HOVERED_OVER = 1 
    PRESSED = 2   

    colors = [(90, 150, 90), (64, 54, 60), (40, 40, 40)]  # corrospoinding to each state 


class Button(MySprite):
    # original_color = pygame.Color(70, 70, 70) 
    # pressed_color = pygame.Color(30, 30, 30) 

    def __init__(self, size, text: str, func = None):
        super().__init__() 
    
        self._image = pygame.Surface(size)
        self.rect = self._image.get_rect() 


        self.text_surface : pygame.Surface = font.render(text, True, BUTTON_TEXT_COLOR) 
        self.text_rect = self.text_surface.get_rect(center = self.rect.center) 
        
        self.state = None 
        self._func = default_func if func is None else func 
    

    def render_text(self):
        self._image.blit(self.text_surface, self.text_rect) 

    def update(self):
        new_state = self.get_desired_state() 
        if self.state != new_state:
            self.check_press(new_state) 

            self.state = new_state 
            self.update_color() 
        
        super().update() 
    
    def get_desired_state(self):
        global_rect = self.get_global_rect() 
        mouse_pos = pygame.mouse.get_pos() 
        is_clicked = pygame.mouse.get_pressed()[0] 

        if not global_rect.collidepoint(mouse_pos):
            return ButtonState.NOT_HOVERED_OVER 
        
        # mouse is over button right now 
        return ButtonState.PRESSED if is_clicked else ButtonState.HOVERED_OVER 

    def check_press(self, new_state):
        if self.state == ButtonState.PRESSED and new_state == ButtonState.HOVERED_OVER:
            self._func() 

    def update_color(self):
        self._image.fill(ButtonState.colors[self.state]) 
        self.render_text() 
        

def default_func():
    raise NotImplementedError("Button Click isn't bounded with any function.")