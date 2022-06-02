class Polygon:
    def __init__(self,a,b,c):
        self.a =a
        self.b =b
        self.c = c
class Triangle(Polygon):
    def perimeter(self):
        self.s = self.a + self.b + self.c
        return self.s
    def area(self):
        s=self.perimeter()/2
        print(self.a)
        self.area = ((s*(s-self.a)*(s-self.b)*(s-self.c))**0.5)
        print("perimeter: "+ str(s*2)+ " area: "+str(self.area))
        
obj1 = Triangle(3,4,5)
obj1.area()
