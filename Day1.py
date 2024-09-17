                                                




                                                                  #CLASS   /   __INIT__  / CLASS VERIABLES


class calisan:

    per_sayi = 0
    zam_oranı = 1.05
    def __init__(self,ad,soyad,maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        calisan.per_sayi = calisan.per_sayi +1
    def tamad(self):
            return "adı : {} soyadı : {}".format(self.ad,self.soyad)
    def arttir(self):
         self.maas = (self.maas*1.05)
    

personel1 = calisan("ali", "demir" ,2500)
print(calisan.per_sayi)

"""personel1.ad = "ali"
personel1.soyad = "demir"
personel1.maas = 2500 """

personel2 = calisan("mehmet","yavuz" ,1500)
print(calisan.per_sayi)


"""personel2.ad = "mehmet"
personel2.soyad = "yavuz"
personel2.maas = 1850"""


print(personel1.maas)
personel1.arttir()
print(personel1.maas)
personel2.arttir()
print(personel2.maas)
"""print(personel1)
print(personel1.ad,personel1.soyad)
print(personel2)
print(personel2.ad,personel2.soyad)
print(personel1.tamad())"""