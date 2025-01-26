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