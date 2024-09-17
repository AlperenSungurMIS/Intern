class Araba:
    def __init__(self, marka, model, yil, yakit_tuketimi): 
        self.marka = marka
        self.model = model
        self.yil = yil
        self.yakit_tuketimi = yakit_tuketimi
        
    def fullmodel(self):
        return "markası : {} modeli : {} yılı : {} , yakit_tuketimi: {} litre/km".format(self.marka, self.model, self.yil, self.yakit_tuketimi)
    
    def guncelle(self):
        self.yil += 1  
    
    def yakit_tuketim_hesapla(self, kilometre):
        # Bu metod aracın belirtilen km'deki yakıt tüketimini hesaplar
        return kilometre * self.yakit_tuketimi
    def karsilastir(self, diger_araba):
        if self.yil > diger_araba.yil:
            return f"{self.marka} daha yeni."
        elif self.yil < diger_araba.yil:
            return f"{diger_araba.marka} daha yeni."
        else:
            return "İki araç da aynı yıl üretildi."
    @staticmethod 
    def saseno (sase):
        return sase.split(" ")


arac1 = Araba("Mercedes", "E200", 2000, 0.08)
arac2 = Araba("Volkswagen", "Polo", 2016, 0.06)
arac3 = Araba("Mazda", "L2000", 2008, 0.07)
asaseno = "123 456 789"
print = (Araba.saseno(asaseno))

"""print(arac1.fullmodel())
print(arac2.fullmodel())
print(arac3.fullmodel())"""


arac3.guncelle()
arac2.guncelle()
arac1.guncelle()

"""print(arac3.fullmodel())
print(arac2.fullmodel())
print(arac1.fullmodel())"""


print("Arac1, 100 km için yakıt tüketimi: {} litre".format(arac1.yakit_tuketim_hesapla(1000)))
print("Arac2, 100 km için yakıt tüketimi: {} litre".format(arac2.yakit_tuketim_hesapla(1000)))
print("Arac3, 100 km için yakıt tüketimi: {} litre".format(arac3.yakit_tuketim_hesapla(1000)))
print(arac1.karsilastir(arac2))
print(arac3.karsilastir(arac1))
print(arac1.yil)
arac1.guncelle
print(arac1.yil)