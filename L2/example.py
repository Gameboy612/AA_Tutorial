import math

class Vector:
    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def dot(self, v2):
        return self.x * v2.x + self.y * v2.y

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2) 

    def angle_between(self, v2):
        return round(math.acos(v1.dot(v2) / (v1.magnitude() * v2.magnitude())) * 180 / math.pi,5)

v1 = Vector(1, 1)
v2 = Vector(-4, -4)

print(Vector.angle_between(v1,v2))