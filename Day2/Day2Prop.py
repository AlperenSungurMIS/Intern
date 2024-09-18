class Point:
    def __init__(self, x , y):
        self.__x = x
        self.__y = y
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        self.__x = x
    @property
    def y(self):
        return self.__y
    y.setter
    def y(self,y):
        self.__y = y

point = Point(25 , 12)
print(point.x, point.y)
point.x=15
print(point.x, point.y)
point.y =13
print(point.x, point.y)




