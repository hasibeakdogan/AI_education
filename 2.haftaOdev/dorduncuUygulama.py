<<<<<<< HEAD
#Koşul İfadeleri:

#1
yas = int(input("Yaşınızı girin: "))

if yas >= 18:
    print("Ehliyet alabilirsiniz.")
else:
    print("Ehliyet almak için yaşınız tutmuyor.")
    
#2
import random

sayi = random.randint(1,10)

tahmin = int(input("Tahmini sayınızı yazın: "))

if tahmin == sayi:
    print("Sayıyı doğru tahmin ettiniz.")
else:
    print("Sayıyı yanlış tahmin ettiniz.")
    
#3
import random

gemi_satiri = random.randint(1, 5)
gemi_sutunu = random.randint(1, 5)

print("Amiral battı oyununa hoş geldiniz..!")
print("5x5 tahtada gemiyi vurmaya çalışın. Koordinatlar 1 ile 5 arasında olmalıdır. İyi eğlenceler:)")

while True:
    tahmin_satiri = int(input("Bir satır tahmini yapın(5x5): "))
    tahmin_sutunu = int(input("Bir sütun tahmini yapın(5x5): "))
    
    if tahmin_satiri < 1 or tahmin_satiri > 5 or tahmin_sutunu < 1 or tahmin_sutunu > 5:
        print("Lütfen 1 ile 5 arasında bir sayı girin.")
        continue
    
    if tahmin_satiri == gemi_satiri and tahmin_sutunu == gemi_sutunu:
        print("Tebrikler! Gemiyi vurdunuz.")
        break
    else:
        print("Aaa gemiyi vuramadınız tekrar deneyin!")
        
    



    
=======
#Sınıflar ve Nesneler
#1
class HesapMakinesi:
    
    def __init__(self):
        print("Hesap makinesi başlatıldı!")
        
    def toplama(self, a, b):
        return a + b
    
    def cikarma(self, a, b):
        return a - b
    
    def carpma(self, a, b):
        return a * b
    
    def bolme(self, a, b):
        if b == 0:
            return "Hata: Sıfıra bölme yapılmaz."
        return a / b
    
hesap = HesapMakinesi()

print("Toplama:", hesap.toplama(10, 5))  
print("Çıkarma:", hesap.cikarma(8, 5))
print("Çarpma:", hesap.carpma(3, 5)) 
print("Bölme:", hesap.bolme(6, 5))      
print("Sıfıra bölme testi:", hesap.bolme(1, 0)) 

#2
class Ogrenci:
    def __init__(self, ad_soyad, sinif, notlar):
        self.ad_soyad = ad_soyad
        self.sinif = sinif
        self.notlar = notlar
        
    def ortlama_hesapla(self):
        if not self.notlar:
            return "Not bulunamadı!"
        return sum(self.notlar) / len(self.notlar)
    
    def bilgileri_goster(self):
        print(f"Adı soyadı: {self.ad_soyad}")
        print(f"Sınıfı: {self.sinif}")
        print(f"Notlar: {self.notlar}")
        print(f"Ortlama: {self.ortlama_hesapla():.2f}")
        
ogrenci1 = Ogrenci("Hasibe Akdoğan", "12/A", [85, 90, 78, 92])
ogrenci1.bilgileri_goster()
>>>>>>> 0c85095 (2. haftanın ödevleri eklendi)
