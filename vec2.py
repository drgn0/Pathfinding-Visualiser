from pygame import Vector2 


def sign(x):
    if x == 0:
        return 0 
    if x > 0:
        return 1 
    return -1 
    
class Vec2:
    def __init__(self, x = 0, y = 0):
        # if isinstance(x, tuple):
        #     x, y = x
        self.x = x
        self.y = y 

    def rounded(self) -> "Vec2":
        return Vec2(round(self.x), round(self.y)) 

    def sign(self) -> "Vec2":
        return Vec2(sign(self.x), sign(self.y)) 

    def length_squared(self) -> float:
        return self.x ** 2 + self.y ** 2 

    def abs(self) -> "Vec2":
        return Vec2(abs(self.x), abs(self.y)) 
        
    def __mul__(self, val):
        return Vec2(self.x * val, self.y * val) 
    
    def __rmul__(self, val):
        return Vec2(self.x * val, self.y * val)

    def __truediv__(self, val):
        return Vec2(self.x / val, self.y / val) 

    def __floordiv__(self, val):
        return Vec2(int(self.x // val), int(self.y // val)) 

    def __add__(self, vec):
        assert(isinstance(vec, Vec2)) 
        return Vec2(
            self.x + vec.x, 
            self.y + vec.y 
        )
    
    def __sub__(self, vec):
        assert(isinstance(vec, Vec2))
        return Vec2(
            self.x - vec.x, 
            self.y - vec.y 
        )

    def __eq__(self, vec):
        if isinstance(vec, (Vec2, Vector2)):
            return self.x == vec.x and self.y == vec.y 
        return NotImplemented 

    def __ne__(self, vec) -> bool:        
        if isinstance(vec, (Vec2, Vector2)):
            return self.x != vec.x or self.y != vec.y 
        return NotImplemented 

    def __iter__(self):
        yield self.x 
        yield self.y 

    def __getitem__(self, i):
        return (self.x, self.y)[i] 

    def __repr__(self) -> str:
        return f"Vec2: {(self.x, self.y)}"



if __name__ == '__main__':
    x = Vec2(4, 2) 
    y = Vec2(5, 1) 

    print(x[0])