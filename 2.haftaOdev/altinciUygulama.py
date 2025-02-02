#Özel Metotlar
#1
class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        if isinstance(other, Vektor):
            return Vektor(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Toplama işlemi yalnızca iki Vektor arasında olabilir.")
    
    def __repr__(self):
        return f"Vektor ({self.x}, {self.y})"
    
vektor1 = Vektor(3, 4)
vektor2 = Vektor(1, 2)

toplam = vektor1 + vektor2

print(toplam)

#2
class Kitap:
    def __init__(self, baslik, yazar, sayfa_sayisi):
        self.baslik = baslik
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        
    def __str__(self):
        return f"Kitap: {self.baslik}, Yazar: {self.yazar}, Sayfa Sayısı: {self.sayfa_sayisi}"
    
kitap1 = Kitap("1984", "George Orwell", 328)
kitap2 = Kitap("Küçük Prens", "Antoine de Saint-Exupery", 96)

print(kitap1)
print(kitap2)