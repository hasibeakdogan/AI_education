<<<<<<< HEAD
#String İşlemleri ve Listeler:

#1
cumle = input("Bir cümle yazın: ")

print(cumle.upper())

#2
alisveris_listesi = ["Muz","Elma","Armut","Çilek","Ayva"]

alisveris_listesi.append("Portakal")
alisveris_listesi.append("Mandalina")
alisveris_listesi.remove("Ayva")

print("Güncellenmiş alışveriş listesi: ")

for urun in alisveris_listesi:
    print(urun)
=======
#Kapsam ve Değişkenler:
sayac = 0 

def sayaci_arttir():
    global sayac
    sayac += 1
    print(f"Güncellenmiş sayaç: {sayac}")
    
def yerel_ornek():
    yerel_sayac = 10
    yerel_sayac += 5
    print(f"Yerel sayac: {yerel_sayac}")
    
sayaci_arttir()
sayaci_arttir()
yerel_ornek()

print(f"Global sayacın son hali: {sayac}")
>>>>>>> 0c85095 (2. haftanın ödevleri eklendi)
