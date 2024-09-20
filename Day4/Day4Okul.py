"""class Okul:
    def kayit(self):
        pass
class Ogrenci(Okul):
    def __init__(self,ogr_no,adsoyad , bolum):
        self.ogr_no = ogr_no
        self.adsoyad = adsoyad
        self.bolum = bolum
    def kayitol(self,ogrenci):
        self.ogrenci = ogrenci
        print(f"{self.adsoyad} {self.bolum} e kaydoldu")
class Ders(Ogrenci):
    def __init__(self, mat , fizik , kimya):
        self.mat = mat
        self.fizik = fizik
        self.kimya = kimya
    def dersgiris(self):
        print(f"{self.adsoyad} {self.Ders} dersine girdi")
class Ogretmen(Okul):
    def __init__(Ders):
        print(f"{self.Ogretmen} {self.Ders} öğretmeni.")"""
class Okul:
    def __init__(self):
        self.ogrenciler = []

    def kayit(self, ogrenci):
        self.ogrenciler.append(ogrenci)
        print(f"{ogrenci.adsoyad} okula kaydedildi.")

class Ogrenci:
    def __init__(self, ogr_no, adsoyad, bolum):
        self.ogr_no = ogr_no
        self.adsoyad = adsoyad
        self.bolum = bolum
        self.dersler = {}

    def ders_al(self, ders):
        if ders.ders_adi not in self.dersler:
            self.dersler[ders.ders_adi] = None  # İlk başta notsuz
            print(f"{self.adsoyad}, {ders.ders_adi} dersini aldı.")
        else:
            print(f"{self.adsoyad} zaten {ders.ders_adi} dersine kayıtlı.")

    def not_ekle(self, ders, vize, final):
        if ders.ders_adi in self.dersler:
            self.dersler[ders.ders_adi] = {"Vize": vize, "Final": final}
        else:
            print(f"{self.adsoyad} bu derse kayıtlı değil.")

    def ortalama_hesapla(self, ders):
        if ders.ders_adi in self.dersler and self.dersler[ders.ders_adi]:
            vize = self.dersler[ders.ders_adi]["Vize"]
            final = self.dersler[ders.ders_adi]["Final"]
            ortalama = (vize * 0.4) + (final * 0.6)
            return ortalama
        else:
            print(f"{self.adsoyad} için not bilgisi bulunmuyor.")
            return None

    def gecme_durumu(self, ders):
        ortalama = self.ortalama_hesapla(ders)
        if ortalama is not None:
            if ortalama >= 60:
                print(f"{self.adsoyad}, {ders.ders_adi} dersinden geçti.")
            else:
                print(f"{self.adsoyad}, {ders.ders_adi} dersinden kaldı.")

class Ders:
    def __init__(self, ders_adi):
        self.ders_adi = ders_adi

class Ogretmen:
    def __init__(self, ogretmen_adi):
        self.ogretmen_adi = ogretmen_adi
        self.dersler = []

    def ders_ver(self, ders):
        self.dersler.append(ders)
        print(f"{self.ogretmen_adi}, {ders.ders_adi} dersini vermeye başladı.")

    def verdi_dersler(self):
        print(f"{self.ogretmen_adi} şu dersleri veriyor:")
        for ders in self.dersler:
            print(f"- {ders.ders_adi}")

# Örnek kullanım:
okul = Okul()

ogrenci1 = Ogrenci(123, "Ahmet Yılmaz", "Bilgisayar Mühendisliği")
okul.kayit(ogrenci1)

matematik = Ders("Matematik")
fizik = Ders("Fizik")

ogrenci1.ders_al(matematik)
ogrenci1.ders_al(fizik)

ogrenci1.not_ekle(matematik, 70, 80)
ogrenci1.gecme_durumu(matematik)

ogretmen1 = Ogretmen("Mehmet Hoca")
ogretmen1.ders_ver(matematik)
ogretmen1.ders_ver(fizik)

ogretmen1.verdi_dersler()
