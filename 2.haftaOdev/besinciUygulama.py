#Kalıtım
#1
class Hayvan:
    def __init__(self, ad):
        self.ad = ad
    
    def ses_cikar(self):
        raise NotImplementedError("Bu metod alt sınıflarda tanımlanmaktadır.")
    
class Kedi(Hayvan):
    def ses_cikar(self):
        return f"{self.ad}: Miyav!"
    
class Kopek(Hayvan):
    def ses_cikar(self):
        return f"{self.ad}: Hav hav!"

kedi = Kedi("Minnak")
kopek = Kopek("Karabaş")

print(kedi.ses_cikar())
print(kopek.ses_cikar())


#2
class Araba:
    def __init__(self, marka, model, yil, ):
        self.marka = marka
        self.model = model
        self.yil = yil
        
    
    def bilgileri_goster(self):
        return f"{self.yil} {self.marka} {self.model} "
    
class ElektrikliAraba(Araba):
    def __init__(self, marka, model, yil, pil_kap):
        super().__init__(marka, model, yil )
        self.pil_kap = pil_kap
        self.pil_seviye = 10
        
    def pil_durumu(self):
        return f"Pil Seviyesi: {self.pil_seviye}%"
    def sarj_et(self):
        self.pil_seviye = 100
        return "Araç tamamen şarj oldu"
    
tesla = ElektrikliAraba("Tesla", "Model S", 2023, 100)

print(tesla.bilgileri_goster())
print(tesla.pil_durumu())
print(tesla.sarj_et())
print(tesla.pil_durumu())
