class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def  start_engine(self):
        print("Motor Çalıştırıldı")
    def stop_engine(self):
        print("Motor durduruldu")
arac1 = Car("mercedes", "E200" , 2000)
arac2 = Car("Volkswagen", "Polo" , 2014)
arac3 = Car("Mazda", "L2000" , 2008)

arac1.start_engine()
arac2.stop_engine()
arac3.stop_engine()

class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_size = 0):
        super().__init__(brand, model, year)
        self.battery_size = battery_size

    def charge_battery(self):
        print(f"Batarya {self.battery_size} kWh olarak şarj ediliyor.")
electric_car = ElectricCar("Tesla", "Model S", 2022, 100)
electric_car.charge_battery
electric_car.start_engine
electric_car.start_engine()
