class Shape:
    def __init__(self, name='Default', height=0, base=0):
        self.area = 0
        self.name = name
        self.height = height
        self.base = base
    def get_height_base(self):
        return "Height: "+str(self.height)+",Base:"+str(self.base)




class triangle(Shape):
    def __init__(self, name='Default', height=0, base=0,side =0):
        super().__init__(name=name, height=height, base=base)
        self.side = side
        # semi-permimeter = (h)
    def calcArea(self):
        permimeter = (self.height + self.base + self.side) / 2
        return (permimeter*(permimeter - self.height)*(permimeter - self.base)* (permimeter - self.side)) ** 0.5

        
# class area(triangle):
#     def __init__(self, name='Default', height=0, base=0, side=0):
#         super().__init__(name=name, height=height, base=base, side=side)

#         permimeter = (height + base + side) / 2
#         return (permimeter*(permimeter - self.height)*(permimeter - self.base)* (permimeter - self.side)) ** 0.5


# class trapezoid(Shape):
#     def __init__(self, name='Default', height=0, base=0):
#         super().__init__(name=name, height=height, base=base)
    



#write your code here
tri_default = triangle()
tri_default.calcArea()
print(tri_default.printDetail())
print('--------------------------')
tri = triangle('Triangle', 10, 5)
tri.calcArea()
# print(tri.printDetail())
# print('---------------------------')
# trap = trapezoid('Trapezoid', 10, 6, 4)
# trap.calcArea()
# print(trap.printDetail())
