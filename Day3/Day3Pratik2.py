class Araba:
    def __init__(self, batarya, benzin):
        self.batarya = batarya
        self.benzin = benzin

class ElektrikliAraba(Araba):
    def __init__(self, batarya):
        super().__init__(batarya, 0)  # Benzin değeri 0 olarak ayarlandı
        print("ElektrikliAraba")
        
    def sarj_et(self):
        self.batarya = min(self.batarya + 10, 100)  # Batarya %100'ü geçemez
        print("Batarya %10 ŞARJ EDİLDİ")
    
    def batarya_bilgisi(self):
        print(f"Batarya seviyesi: {self.batarya}%")

class BenzinliAraba(Araba):
    def __init__(self, benzin):
        super().__init__(0, benzin)  
        print("BenzinliAraba")
    
    def benzin_doldur(self):
        self.benzin = min(self.benzin + 10, 100)  # Benzin seviyesi 100'ü geçemez
        print("Benzin 10 LT dolduruldu")
    
    def benzin_bilgisi(self):
        print(f"Benzin seviyesi: {self.benzin} LT")

# Kullanım örneği
benzinliaraba = BenzinliAraba(50)
elektrikliaraba = ElektrikliAraba(50)

benzinliaraba.benzin_doldur()
benzinliaraba.benzin_doldur()
benzinliaraba.benzin_doldur()
benzinliaraba.benzin_doldur()
benzinliaraba.benzin_bilgisi()

elektrikliaraba.sarj_et()
elektrikliaraba.sarj_et()
elektrikliaraba.sarj_et()
elektrikliaraba.sarj_et()
elektrikliaraba.sarj_et()
elektrikliaraba.batarya_bilgisi()

