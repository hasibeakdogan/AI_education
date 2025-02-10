#1
"""
numbers = [1, 2, 3, 4, 5]


squared_numbers = list(map(lambda x: x ** 2, numbers))

print("Karesi alınmış liste:", squared_numbers)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Çift sayılar:", even_numbers)

from functools import reduce

numbers = [1, 2, 3, 4, 5]


sum_numbers = reduce(lambda x, y: x + y, numbers)

print("Listedeki sayıların toplamı:",sum_numbers)"""

#2

numbers = [5, 2, 9, 1, 7]

sorted_numbers = sorted(numbers, key=lambda x: x)  # Varsayılan olarak küçükten büyüğe sıralar

print("Küçükten büyüğe sıralı liste:", sorted_numbers)

numbers = [5, 2, 9, 1, 7]

sorted_numbers_desc = sorted(numbers, key=lambda x: x, reverse=True)

print("Büyükten küçüğe sıralı liste:",sorted_numbers_desc)

words = ["elma", "armut", "kiraz", "muz", "karpuz"]

worted_words = sorted(words, key=lambda x: len(x))

print("Kelime uzunluklarına göre sıralı liste:",sorted_words)

people = [["Ali", 25], ["Zeynep", 22], ["Mehmet", 30]]

sorted_people = sorted(people, key=lambda x: x[1])  # Yaşa göre sıralama

print("Yaşa göre sıralı liste:", sorted_people)

words = ["elma", "armut", "kiraz", "muz", "karpuz"]

sorted_by_last_char = sorted(words, key=lambda x: x[-1])

print("Son harfine göre sıralı liste:",sorted_by_last_char)