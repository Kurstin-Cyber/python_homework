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
            return f'Vector<{self.x}, {self.y}'
    
    def __add__(self, other):
         if not isinstance(other, Point):
              raise TypeError('Operand must be a Vector or Point')
         return Vector(self.x + other.x, self.y + other.y)
        
    
if __name__ == '__main__':
        p1 = Point(1, 2)
        p2 = Point(4, 6)

        print('Points:')
        print(p1)
        print(p2)
        print(f'Distance between p1 and p2: {p1.distance_to(p2)}')

        v1 = Vector(1, 2)
        v2 = Vector(4, 6)

        print('\nVectors (inheriting from Point):')
        print(v1)
        print(v2)
        print(f'Vector Addition (v1 + v2):  {v1 + v2}')
        print(f'Are p1 and v1 equal? {p1 == v1}')