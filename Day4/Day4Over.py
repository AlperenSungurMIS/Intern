class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"

# Vektör nesneleri oluşturma
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

# Vektörleri toplama
v3 = v1 + v2

# Sonucu yazdırma
print(f"Birinci Vektör: {v1}")
print(f"İkinci Vektör: {v2}")
print(f"Toplama Sonucu: {v3}")
