print("Hello world") #wersja 3.x

# C#, C++, Java, PHP
# def main():
#     pass
#     for elem in kolekcja:
#         if costam <0:
imie = "Ala" #zmienne
imie = 0
imie = None

#łańcu znaków
print(type(imie))
imie = str("Ala")
#imie = str(100) # "100"
imie = imie.lower()
print(imie)

#typy liczbowe
liczba = 0
liczbaf = 4.5
print(liczba)
print(liczbaf)
print(type(liczba))
print(type(liczbaf))

print(0.1 + 0.2 ==0.3)
print(f"{0.1:.32f}")
print(f"{0.2:.32f}")
print(f"{0.3:.32f}")
#Decimal lub zaokraglanie

liczba = "100"
print(int(liczba))
print(int(liczba, 2))

print("Ala" + "ma kota")
print("Ala" + " ma " + str(5) + " kotów ")
print("Ala ma {} kotow".format(5))
print("Ala ma {1}{0} kotow".format(5,4))

#f-string
ilosc_kotow= 5
print(f"Ala ma {ilosc_kotow} kotów")
print(f"{"Ala":>10}")