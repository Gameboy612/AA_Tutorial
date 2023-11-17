import math

class nVector:
    def __init__(self, *args):
        self.v = []
        for arg in args:  
            self.v.append(arg)


    def dot(self, v2):
        udot = []
        for i in range(len(self.v)):
            udot.append(self.v[i] * v2.v[i]) 
        dot = sum(udot)
        return dot
    
    def magnitude(self):
        ussmagnitude = []
        for i in range(len(self.v)):
             ussmagnitude.append(self.v[i] ** 2)
        usmagnitude = sum(ussmagnitude)
        magnitude = math.sqrt(usmagnitude)
        return magnitude
    
    def angle_between(self, v2):
        return round(math.acos(v1.dot(v2) / (v1.magnitude() * v2.magnitude())) * 180 / math.pi,5)

v1 = nVector(1, 1, 67, 9)
v2 = nVector(-4, -4, 0, -69)

print(nVector.angle_between(v1,v2))
    