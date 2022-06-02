class EquilateralTriangle:
    def __init__(self,side):
        self.side=side
    def __add__(self,new):
        return 3*self.side + 3*new.side
obj1 = EquilateralTriangle(5)
obj2 = EquilateralTriangle(10)
print(obj1+obj2)
