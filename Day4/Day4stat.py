class Math:
    @staticmethod
    def toplama(a,b):
        return a + b
    @staticmethod
    def cikarma(a, b):
        return a - b
    @staticmethod
    def carpma(a, b):
        return a * b
    @staticmethod
    def bolme(a, b):
        if b == 0:
            return "Bir sayı sıfıra bölünemez!"
        return a / b
toplam = Math.toplama(5, 3)
fark = Math.cikarma(10, 4)
carpim = Math.carpma(6, 7)
bolum = Math.bolme(8, 2)
bolum_sifir = Math.bolme(5, 0)

print(f"Toplama: {toplam}")
print(f"Çıkarma: {fark}")
print(f"Çarpma: {carpim}")
print(f"Bölme: {bolum}")
print(f"Bölme (Sıfıra bölme): {bolum_sifir}")
    
    
    