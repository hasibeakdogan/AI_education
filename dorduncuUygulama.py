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
        
    



    