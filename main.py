import pygame 
pygame.init()
from pygame import Vector2

import ui 
from ui.my_sprite import MySprite
from ui.label import Label


from constants import *
from vec2 import Vec2


class PathfindingVisualiser(MySprite):
    def __init__(self):
        super().__init__() 

        pygame.display.set_caption("Pathfinding Visualiser") 

        
        self.clock = pygame.time.Clock() 
        self.running = True 

        self.initialise_main_screen() 
        self.initialise_children() 


    def initialise_main_screen(self):
        self.main_screen = pygame.display.set_mode((
            MARGIN + GRID_SIZE.x*CELL_SIZE + MARGIN, 
            MARGIN + TOP_BAR_SIZE + MARGIN + GRID_SIZE.y*CELL_SIZE + MARGIN
        ))
        self.main_screen.fill(BACKGROUND_COLOR)

        self.set_image(self.main_screen.copy()) 


    def initialise_children(self):
        gridlines = MySprite(self.get_grid_lines()) 
        self.add_child(gridlines)
        gridlines.set_local_pos((MARGIN, MARGIN + TOP_BAR_SIZE + MARGIN))
        
        top_bar = TopBar() 
        self.add_child(top_bar) 
        top_bar.set_local_pos((MARGIN, MARGIN)) 

    
    def get_grid_lines(self) -> pygame.Surface:
        lines = pygame.Surface(tuple((GRID_SIZE + Vec2(1, 1)) * CELL_SIZE), pygame.SRCALPHA).convert_alpha() 
        color = pygame.Color(100, 100, 100, 200)
        
        # Horizontal Lines 
        for y in range(GRID_SIZE.y+1):
            pygame.draw.line(lines, color,  
                Vector2(0, y) * CELL_SIZE,
                Vector2(GRID_SIZE.x, y) * CELL_SIZE
            )
        
        # Vertical Lines 
        for x in range(GRID_SIZE.x+4):
            pygame.draw.line(lines, color,  
                Vector2(x, 0) * CELL_SIZE, 
                Vector2(x, GRID_SIZE.y) * CELL_SIZE
            )
        
        
        return lines 

    def main_loop(self):
        while self.running:
            self.handle_events() 
            self.simulate_frame() 
        
        pygame.quit()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False 

    def simulate_frame(self):
        self.update() 

        self.main_screen.blit(self.image, (0, 0))
        pygame.display.update() 
        self.clock.tick(FPS)

class TopBar(MySprite):
    def __init__(self):
        super().__init__()

        self.set_image(pygame.Surface((GRID_SIZE.x * CELL_SIZE, TOP_BAR_SIZE), pygame.SRCALPHA).convert_alpha()) 

        label = Label('Algorithm:') 
        self.add_child(label) 
        label.set_local_pos((0, self.rect.centery))






if __name__ == '__main__':
    visualiser = PathfindingVisualiser() 
    visualiser.main_loop()
