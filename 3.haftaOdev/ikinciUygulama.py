#1
"""
def bolme_islemi():
     try:
         sayi1 = float(input("Birinci sayıyı girin: "))
         sayi2 = float(input("İkinci sayıyı girin: "))

         sonuc = sayi1 / sayi2
         print(f"Sonuç: {sonuc}")

     except ZeroDivisionError:
         print("Hata: Bir sayı sıfıra bölünemez!")
     except ValueError:
         print("Hata: Lütfen geçerli bir sayı girin!")
     except Exception as e:
         print(f"Bilinmeyen bir hata oluştu: {e}")

bolme_islemi()"""

#2

class NegatifSayiHatasi(Exception):
     """Negatif sayı girildiğinde fırlatılan özel hata sınıfı."""
def _init_(self, mesaj="Negatif sayı girişi yasaktır!"):
         super()._init_(mesaj)

def pozitif_sayi_kontrol(sayi):
        """Negatif sayı girildiğinde özel hata fırlatan fonksiyon."""
if sayi < 0:
    raise NegatifSayiHatasi(f"Hata: {sayi} negatif bir sayıdır!")
        #return f"Girilen sayı: {sayi}"
try:
    sayi = float(input("Bir sayı girin: "))
    print(pozitif_sayi_kontrol(sayi))
except NegatifSayiHatasi as e:
    print(e)
except ValueError:
    print("Hata: Lütfen geçerli bir sayı girin!")