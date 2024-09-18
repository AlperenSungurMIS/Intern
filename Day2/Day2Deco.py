



                                    # PROPERTY , SETTER , DELETER , DECORATOR








class kisiler:
    def __init__(self, ad, soyad):
        self.ad = ad
        self.soyad = soyad
    
    @property
    def adsoyad(self):
        return f"{self.ad} {self.soyad}"
    
    @property
    def email(self):
        return f"{self.ad}.{self.soyad}@sirket.com"
    
    @adsoyad.setter
    def adsoyad(self, isim):
        ad, soyad = isim.split(" ")
        self.ad = ad
        self.soyad = soyad

# Nesne oluşturma ve işlemler sınıfın dışında olmalı
kisi1 = kisiler("Ali", "uzun")

kisi1.ad = "Ahmet"             # Adı değiştirme
kisi1.adsoyad = "Ayşe Yıldız"   # adsoyad setter ile ad ve soyadı değiştirme

print(kisi1.ad)          # Ayşe yazdırılır
print(kisi1.adsoyad)     # Ayşe Yıldız yazdırılır
print(kisi1.email)       # Ayşe.Yıldız@sirket.com yazdırılır
