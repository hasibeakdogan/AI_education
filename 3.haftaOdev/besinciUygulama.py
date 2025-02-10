#kendi iteratör sınıfını oluştur(EvenNumbers) ve yalnızca çift sayılar üreten bir iterator yaz.


class EvenNumbers:
    def _init_(self, start=0, limit=None):
        
        self.current = start if start % 2 == 0 else start + 1
        self.limit = limit
    
    def _iter_(self):
        return self
    
    def _next_(self):
        if self.limit is not None and self.current > self.limit:
            raise StopIteration
        next_even = self.current
        self.current += 2 
        return next_even


if _name_ == "_main_":
    even_numbers = EvenNumbers(4, 30)  
    for num in even_numbers:
      print(num)


# Fibonacci serisi üreten bir generator fonksiyonu yaz ve ilk 10 fibonacci dizisini ekrana yaz.

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = fibonacci()
for _ in range(10):
    print(next(fib_gen),end=" ")