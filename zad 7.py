lista = []

for x in range(0, 5):
    lista.append(float(input('Podaj liczbę: ')))
  
    lista[x] = lista[x] ** 2
    print("Spotęgowana liczba: " + str(lista[x]))