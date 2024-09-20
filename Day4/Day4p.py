class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Hav")

class Cat(Animal):
    def sound(self):
        print("Miav")

class Cow(Animal):
    def sound(self):
        print("Möö")

do = Dog()
ca = Cat()
co = Cow()

do.sound()
ca.sound()
co.sound()
