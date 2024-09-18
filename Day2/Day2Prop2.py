class GetCollorError(Exception):
    pass

class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._color = "beyaz"

    @property
    def radius(self):
        return self._radius  # Buradaki hata düzeltildi
    
    @radius.setter
    def radius(self, value):
        self._radius = value
    
    @property
    def diameter(self):
        return self._radius * 2
    
    @property
    def color(self):
        raise TypeError("Can not get color value")
    
    @color.setter
    def color(self, value):
        self._color = value

circle = Circle(20)
print(circle.radius)   # 20 yazdırır
