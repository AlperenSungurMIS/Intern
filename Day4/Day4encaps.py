class BankaHesabi:
    def __init__(self, baslangic_bakiyesi=0):
        self.__bakiye = baslangic_bakiyesi

    def bakiyegoster(self):
        return self.__bakiye

    def para_yatir(self, miktar):
        if miktar > 0:
            self.__bakiye += miktar
            print(f"{miktar} TL yatırıldı. Güncel bakiye: {self.__bakiye}")
        else:
            print("Yatırılacak miktar sıfırdan büyük olmalı.")

    def para_cek(self, miktar):
        if miktar > self.__bakiye:
            print(f"En fazla {self.__bakiye} TL kadar para çekebilirsiniz.")
        elif miktar > 0:
            self.__bakiye -= miktar
            print(f"{miktar} TL çekildi. Güncel bakiye: {self.__bakiye}")
        else:
            print("Çekilecek miktar sıfırdan büyük olmalı.")
