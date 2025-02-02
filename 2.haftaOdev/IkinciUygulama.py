#1

def tekSayilarinKaresi(liste):
    return list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 1, liste)))

sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sonuc = tekSayilarinKaresi(sayilar)

print(f"Tek sayıların kareleri: {sonuc}")

#2
def ciftSayiFiltresi(liste):
    return list(filter(lambda x: x % 2 == 0, sayilar))

sayilar = list(range(51))
sonuc = ciftSayiFiltresi(sayilar)

print(f"0-50 arasındaki çift sayılar: {sonuc}")

#3
toplam_hesapla = lambda x, y: sum(range(min(x, y), max(x, y) + 1))

sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))

sonuc = toplam_hesapla(sayi1, sayi2)

print(f"{sayi1} ile {sayi2} arasındaki tam sayıların toplamı: {sonuc}")