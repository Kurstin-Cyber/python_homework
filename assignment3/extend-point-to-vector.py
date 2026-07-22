import math

class Point:
    def __init__( self, x, y):
        self .x = x
        self .y = y
    
    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f'Point({self.x}, {self.y})'
    
    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    

class Vector(Point):
    def __init__(self, x, y):
            super().__init__(x, y)
        

    def __str__(self):
            return f'Vector<{self.x}, {self.y}>'
    
    def __add__(self, other):
         if not isinstance(other, Point):
              raise TypeError('Operand must be a Vector or Point')
         return Vector(self.x + other.x, self.y + other.y)
        
    
if __name__ == '__main__':
        p1 = Point(1, 2)
        p2 = Point(4, 6)

        print('--- Point Demonstration ---')
        print(f'Point 1: {p1}')
        print(f'Point2:  {p2}')
        print(f'Distance between p1 and p2: {p1.distance_to(p2)}')

        v1 = Vector(3, 4)
        v2 = Vector(1, 2)

        print('\n---Vector Demonstration ---')
        print(f'Vector 1 (custom string representation): {v1}')
        print(f'Vector 2 (custom string representation): {v2}')
        v3 = v1 + v2
        print(f'Vextor Addition (v1 + v2): {v1} + {v2} = {v3}')