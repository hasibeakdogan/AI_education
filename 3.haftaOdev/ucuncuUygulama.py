#1

def veri_kaydet():
    with open("data.txt", "w", encoding="utf-8") as dosya:
        veri = input("Kaydetmek istediğiniz veriyi girin: ")
        dosya.write(veri)
        print("Veri başarıyla kaydedildi!")

# Dosyadan veriyi oku ve ekrana yazdır
def veri_oku():
    try:
        with open("data.txt", "r", encoding="utf-8") as dosya:
            icerik = dosya.read()
            print("Dosyadan okunan veri:")
            print(icerik)
    except FileNotFoundError:
        print("Hata: data.txt dosyası bulunamadı!")

# Ana program
while True:
    print("\n1 - Veri Kaydet")
    print("2 - Veriyi Oku ve Yazdır")
    print("3 - Çıkış")
    secim = input("Seçiminizi yapın: ")

    if secim == "1":
        veri_kaydet()
    elif secim == "2":
        veri_oku()
    elif secim == "3":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin!")
        
#2

{
     "ad": "Ali",
     "yas": 25,
     "sehir": "İstanbul"
}

import json

dosya_adi = "veri.json"

# JSON dosyasını oku
with open(dosya_adi, "r", encoding="utf-8") as dosya:
    veri = json.load(dosya)

print("Mevcut JSON Verisi:", veri)

# Kullanıcıdan yeni bilgileri al
veri["ad"] = input("Yeni ad girin: ")
veri["yas"] = int(input("Yeni yaş girin: "))
veri["sehir"] = input("Yeni şehir girin: ")

# Güncellenmiş veriyi JSON dosyasına kaydet
with open(dosya_adi, "w", encoding="utf-8") as dosya:
    json.dump(veri, dosya, ensure_ascii=False, indent=4)
    print("Güncellenmiş JSON Verisi:", veri)