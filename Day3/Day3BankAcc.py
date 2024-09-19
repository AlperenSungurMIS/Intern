class BankAcc:
    def __init__(self, hesapismi, bakiye=0):
        self.hesapismi = hesapismi
        self.__bakiye = bakiye  #__ ile private yaptım

    def paraekle(self, miktar):
        if miktar > 0:
            self.__bakiye += miktar
            print(f"{miktar} TL eklendi")
        else:
            print("Geçersiz miktar. Miktar pozitif olmalıdır.")

    def paracek(self, miktar):
        if miktar > 0:
            if miktar <= self.__bakiye:
                self.__bakiye -= miktar
                print(f"{miktar} TL çekildi")
            else:
                print("Yetersiz bakiye!")
        else:
            print("Geçersiz miktar. Miktar pozitif olmalıdır.")

    def get_bakiye(self):
        return self.__bakiye  # Bakiye bilgisini dışarıya sağlar

# Kullanım örneği
hesap = BankAcc("Ali Veli")
hesap.paraekle(100)
print(f"Bakiye: {hesap.get_bakiye()} TL")  
hesap.paracek(50)
print(f"Bakiye: {hesap.get_bakiye()} TL")  
hesap.paracek(100)  

