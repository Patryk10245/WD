def zad_1():
    A = [1/x for x in range(1, 11)]
    B = [2**i for i in range(11)]
    C = {x: x for x in B if x % 4 == 0}
    print(A)
    print(B)
    print(C)
    print('\n')

def zad_2():
    import random
    macierz = [random.sample(range(1, 101), 4) for _ in range(4)]
    for wiersz in macierz:
        print(wiersz)

    print(macierz)
    # przekątna
    przekatna = []
    for i in range(len(macierz)):
        przekatna.append(macierz[i][i])
    print(przekatna)
    print('\n')

def zad_3():     
    produkty = {"Ziemniaki": "kg",
             "Ogórki": "sztuka",
             "Frytki": "opakowania"}
    sztuki = {klucz: wartosc for klucz, wartosc in produkty.items() if wartosc == "sztuki"}
    print(sztuki)
    print("\n")

def zad_4(a, b, x):
    monotonicznosc = a * x + b
    if (a > 0):
        print("Funkcja jest rosnaca")
        print("\n")
    elif (a < 0):
        print("Funkcja jest malejąca")
        print("\n")
    else:
        print("Funkcja jest stała")
        print("\n")
def zad_5(prosta1, prosta2):
    if prosta1[0] == prosta2[0]:
        print("Rownolegla")
        print("\n")
    elif prosta1[0] * prosta2[0] == -1:
        print("Prostopadła")    
        print("\n")

def zad_6(a = 2, b = 4, x = 6, y = 8):
    import math
    return math.sqrt((x-a)**2 + (y-b)**2)

def zad_7(a = 3, b = 4):
    import math
    return math.sqrt((a**2) + (b**2))

def zad_8(a = 1, r = 1, ile = 10):
    ciag = [x for x in range(a, r * ile+1, r)]
    return ciag

def zad_9(ciag):
    return sum(ciag)

def zad_10(** zakupy):
    return sum(zakupy.values())

zad_1()
zad_2()
zad_3()
zad_4(3,2,4)
zad_5([3,4,5], [3,4,5])
r = zad_6(2, 3, 4, 5)
print(r)
print(zad_7())
print(zad_8())
print(zad_9(zad_8()))
print(zad_10(pomidor=10, marchew=20))