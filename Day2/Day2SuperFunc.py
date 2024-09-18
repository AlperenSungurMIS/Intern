class Human:
    def __init__(self):
        print("Human")


class GrandPa1(Human):
    def __init__(self):
        print("GrandPa1")
        super().__init__()


class GrandPa2(Human):
    def __init__(self):
        print("GrandPa2")
        super().__init__()

class GrandMa1(Human):
    def __init__(self):
        print("Grandma1")
        super().__init__()
class GrandMa2(Human):
    def __init__(self):
        print("GrandMa2")
        super().__init__()


class Father(GrandPa1,GrandMa1):
    def __init__(self):
        print("Father")
        super().__init__()

class Mother(GrandPa2,GrandMa2):
    def __init__(self):
        print("Mother")
        super().__init__()

class Child(Father,Mother):
    def __init__(self):
        print("Child")
        super().__init__()
child = Child()
print(Child.__mro__)


