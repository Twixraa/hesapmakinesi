def toplama(sayi1,sayi2):
    return sayi1+sayi2

def cikarma(sayi1,sayi2):
    return sayi1-sayi2

def carpma(sayi1,sayi2):
    return sayi1*sayi2

def bolme(sayi1,sayi2):
    return sayi1/sayi2

print("Hesap Makinesi 1.0")
print("Toplama : 1, Çıkarma :2, Çarpma :3, Bölme :4, Çıkış :q")
while True:
    secim = input("İşleminiz :")
    if secim == "q":
        break
    sayi1 = int(input("Birinci sayıyı girin :"))
    sayi2 = int(input("İkinci sayıyı girin :"))
    if secim=="1":
        print("Sonuç :", toplama(sayi1, sayi2))
    elif secim =="2":
        print("Sonuç :", cikarma(sayi1,sayi2))
    elif secim =="3":
        print("Sonuc :",carpma(sayi1,sayi2))
    elif secim=="4":
        print("Sonuç :",bolme(sayi1,sayi2))
    else:
        print("Yanlış seçim lütfen tekrar deneyin")
        break