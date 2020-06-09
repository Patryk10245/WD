def Zad_1():
    liczby = open("liczby.txt","w") as plik:
    for x in range(1, 21):
        if x % 4 == 0:
        print(x, end="\t")

def Zad_2():
    plik = open("liczby")
    print(plik.readlines())

def Zad_3():
    with open("liczby", "r+") as plik:
        plik.write("Nowa linijka tekstu :D ")
        plik.write("I jeszcze jedna :D")
        print(plik.readlines())

Zad_1()
Zad_2()
Zad_3()