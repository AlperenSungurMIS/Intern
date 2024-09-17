class Kedi:
    def ses(self):
        print("miav")

class Kopek:
    def ses(self):
        print("hav")

class Kus:
    def ses(self):
        print("cik")


def hayvanSesi(hayvan):
    hayvan.ses()


ke = Kedi()
ko = Kopek()
ku = Kus()


hayvanSesi(ke)
hayvanSesi(ko)
hayvanSesi(ku)
