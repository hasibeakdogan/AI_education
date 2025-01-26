#Değişkenler ve Veri Tipleri Uygulaması:

#1
string = "Sonuç: "

int  = 20

float = 22.5

bool = True

result = int+float
print(string + str(result))


if result==42.5:
    print("Bool değeri doğrudur.")
else:
    print("Bool değeri yanlıştır.")


#2
sayi1 = int(input("İlk sayıyı giriniz: "))
sayi2 = float(input("İkinci sayıyı giriniz: "))

toplam = sayi1 + sayi2
fark = sayi1 - sayi2
carpim = sayi1 * sayi2


print(f"Sayıların toplamı: {toplam}")
print(f"Sayıların toplamı: {fark}")
print(f"Sayıların toplamı: {carpim}")

#3
int_sayi = 2
float_sayi = 2.6

int_float = float(int_sayi)
float_int = int(float_sayi)

print(f"İnteger değer floata dönüştürüldü: " + str(int_float))
print(f"Float değer integera dönüştürldü: " + str(float_int))