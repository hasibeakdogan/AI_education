# math kütüphanesi 
import math

def hesap_makinesi():
    print("Merhaba Hesap Makinesi Uygulamasına hoşgeldiniz")
    print("İşlemler: +, -, *, /, ^ (üs), sqrt (karekök)")
    
    islem = input("İşlemi seçiniz: ")
    
    if islem == "sqrt":
        sayi = float(input("Sayıyı giriniz: "))
        print(f"Sonuç: {math.sqrt(sayi)}")
    else:
        sayi1 = float(input("Birinci sayıyı giriniz: "))
        sayi2 = float(input("İkinci sayıyı giriniz: "))
        
        if islem == "+":
            print(f"Sonuç: {sayi1 + sayi2}")
        elif islem == "-":
            print(f"Sonuç: {sayi1 - sayi2}")
        elif islem == "*":
            print(f"Sonuç: {sayi1 * sayi2}")
        elif islem == "/":
            if sayi2 != 0:
                print(f"Sonuç: {sayi1 / sayi2}")
            else:
                print("Hata: Sıfıra bölme hatası!")
        elif islem == "^":
            print(f"Sonuç: {math.pow(sayi1, sayi2)}")
        else:
            print("Geçersiz işlem!")

hesap_makinesi()
