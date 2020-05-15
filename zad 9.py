liczba = input("Podaj liczbe wielocyfrowa")
count = len(liczba)

wynik = 0
i = 0
while i < count:
    wynik += int(liczba[i])
    i += 1
print("wynik = " + str(wynik))

