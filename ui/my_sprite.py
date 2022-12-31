import pygame 

# from vec2 import Vec2

class MySprite(pygame.sprite.Sprite):  
    def __init__(self, image = None):
        super().__init__() 

        self.parent = None  # set when adding as children 
        self.is_visible = True  # only visible children are updated and drawn 
    
        if image:
            self.set_image(image) 
        else:
            self._image : pygame.Surface = None 
        
        self._children = pygame.sprite.Group() 
        ## self.visible_children = pygame.sprite.Group() 

    def set_image(self, image: pygame.Surface):
        ''' sets the base image of sprite. children may be drawn over it. '''
        self._image = self.image = image 
        self.rect = image.get_rect() 


    def set_local_pos(self, pos):
        if not self.parent:
            raise ValueError("setting local pos before adding as a child.") 
        self.rect.topleft = tuple(pos) 
    

    def get_local_pos(self):
        return self.rect.topleft 

    def get_local_center(self):
        return pygame.Vector2(self.rect.center) 

    def get_global_pos(self):
        pos = self.get_local_pos() 
        if self.parent:
            pos += self.parent.get_global_pos() 
        return pos 
        
    def get_global_rect(self):
        return pygame.Rect(self.get_global_pos(), self.rect.size) 

    def update(self):
        self.update_and_draw_children() 

    def update_and_draw_children(self):
        visible_children = self.get_visible_children() 
        visible_children.update() 
    
        if visible_children:
            self.image = self._image.copy() 
            visible_children.draw(self.image)  
        else:
            self.image = self._image 
    
    def get_visible_children(self):
        return pygame.sprite.Group(filter(lambda sprite: sprite.is_visible, self._children)) 
        
    def add_child(self, child):
        self._children.add(child)

        # if not isinstance(child, pygame.sprite.Sprite):
        child.parent = self  

    def _die(self):
        self.parent.remove_child(self) 
        
    def remove_child(self, child):
        self._children.remove(child) 

    def toggle_visible(self):
        self.is_visible = not self.is_visible 