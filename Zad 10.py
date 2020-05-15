x = 12
while 0 > x or x > 11:
    x = int(input("Podaj wysokość wieży: ")) + 1

    for i in range(0, x):
        print("A" * i)