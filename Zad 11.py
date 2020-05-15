a = int(input("Podaj wysokosc diamencika - liczbę nieparzystą z przedziału [3,9] "))
srodek = int((a+1)/2)
for x in range(1, a+1, 1):
    print("{:^10}".format('o'*(2*(srodek-abs(srodek-x))-1)))