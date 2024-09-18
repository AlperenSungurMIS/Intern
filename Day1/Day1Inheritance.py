class Calisan:
    def __init__(self, isim,soyisim,maas) :
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim + soyisim + "@sirket.com"
    def bilgileri_goster(self):
        return "İsmim: {} Soyismim: {} Maaşım: {} Emailim : {}".format(self.isim , self.soyisim ,self.maas, self.email)

calisan1 = Calisan("ali" ,"veli" ,3000)
calisan2 = Calisan("ayşe" ,"fatma" ,5000)
print(calisan2.email)


class Yazilmci(Calisan):
    def bilgileri_goster(self):
        return "Yazılımcıyım"

yazilimci1 = Yazilmci("Ayşe", "Yıldız", 7000)
yazilimci2 = Yazilmci("Fatma" ," Ay" ,8000)
print(yazilimci2.email)
print(calisan1.bilgileri_goster())
print(yazilimci1.bilgileri_goster())