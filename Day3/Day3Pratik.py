class Araba:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil
        self.hiz = 0  # Hız başlangıçta 0

    def hizlanma(self):
        self.hiz += 10
        print(f"Araç hızlandı: {self.hiz} km/h")

    def fren_yap(self):
        if self.hiz >= 10:
            self.hiz -= 10
        else:
            self.hiz = 0  # Hız 0'ın altına düşmemeli
        print(f"Araç yavaşladı: {self.hiz} km/h")

    def hiz_bilgisi(self):
        print(f"Şu anki hız: {self.hiz} km/h")
araba = Araba("Mercedes", "e200",2000)
araba.hizlanma()
araba.hizlanma()
araba.fren_yap()
araba.fren_yap()
araba.fren_yap()
araba.hizlanma()
araba.fren_yap()
araba.hizlanma()
araba.hizlanma()
araba.fren_yap()
araba.fren_yap()
araba.fren_yap()
araba.fren_yap()
araba.fren_yap()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()

araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.fren_yap()
araba.fren_yap()
araba.fren_yap()
araba.fren_yap()
araba.fren_yap()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.fren_yap()
araba.fren_yap()
araba.fren_yap()
araba.fren_yap()
araba.fren_yap()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.fren_yap()
araba.fren_yap()
araba.fren_yap()
araba.fren_yap()
araba.fren_yap()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.fren_yap()
araba.fren_yap()
araba.fren_yap()
araba.fren_yap()
araba.fren_yap()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.fren_yap()
araba.fren_yap()
araba.fren_yap()
araba.fren_yap()
araba.fren_yap()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.fren_yap()
araba.fren_yap()
araba.fren_yap()
araba.fren_yap()
araba.fren_yap()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hizlanma()
araba.hiz_bilgisi()
     
