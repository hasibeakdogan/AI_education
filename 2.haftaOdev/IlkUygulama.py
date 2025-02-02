#1
def ortalama_hesapla(sayilar):
    if len(sayilar) == 0:
        return 0
    
    toplam = sum(sayilar)
    adet = len(sayilar)
    ortalama = toplam / adet
    
    return ortalama 

sayilar =[10,20,30,40,50]
sonuc = ortalama_hesapla(sayilar)

print(f"Verilen sayıların ortalaması: {sonuc}")

#2
def buyukSayiBulma(sayi1, sayi2):
    return max(sayi1, sayi2)

sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

sonuc = buyukSayiBulma(sayi1, sayi2)

print(f"Büyük sayı: {sonuc}")

#3
def kelime_sayisi_sayma(metin):
    kelimeler = metin.split()
    return len(kelimeler)

metin = input("Bir metin girin: ")
sonuc = kelime_sayisi_sayma(metin)

print(f"Girilen metndeki kelime sayısı: {sonuc}")

