a = int(input("Bir Sayı Giriniz: "))
b = int(input("Bir sayı daha giriniz: "))
x = input("İşaret giriniz:  + , - , / , x")
if (x=="+"):
    print(a+b)
elif (x=="-"):
    print(a-b)
elif (x=="/"):
    print(a/b)
elif (x=="x"):
    print(a*b)
else:
    print("Yanlış İşaret girdiniz!")