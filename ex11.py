class Triangle:
    def __init__(self):
        self.side1 =5
        self.side2 =8
        self.side3 = 12
    def findperimeter(self):
        print(self.side1+self.side2+self.side3)
        
class EquilateralTriangle(Triangle):
    def __init__(self,side):
        self.side=side
    def findperimeter(self):
        print(self.side*3)
        
obj1 = Triangle()
obj2 = EquilateralTriangle(10)
obj1.findperimeter()
obj2.findperimeter()

#changed the definition of find perimeter method in the child class. Overriding done successfully
