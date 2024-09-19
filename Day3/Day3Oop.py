class Account:
    def __init__(self, isim, numara, bakiye):
        self.isim = isim
        self.numara = numara
        self.bakiye = bakiye

    def hesapBilgileri(self):
        print("İsim:", self.isim)
        print("Numara:", self.numara)
        print("Bakiye:", self.bakiye)

    def paraCek(self, miktar):  # self ve miktar parametreleri doğru şekilde tanımlandı
        if self.bakiye - miktar < 0:
            print("Bakiye Yetersiz")
        else:
            self.bakiye -= miktar
            print("Yeni Bakiye:", self.bakiye)

    def paraYatir(self, miktar):
        self.bakiye += miktar
        print("Yeni Bakiye:", self.bakiye)

account = Account("Alperen Sungur", 123456, 4000)

account.hesapBilgileri()
account.paraCek(1200)
