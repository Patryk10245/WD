a = input("Podaj a: ")
b = input("Podaj b: ")
c = input("Podaj c: ")

a = int(a)
b = int(b)
c = int(c)

if a > 0 or a <= 10:
    print("a zawiera się w przedziale (0,10>")
else:
    print("a nie zawiera się w przedziale (0,10>")    
    pass
if a > b or b > c:
    print("a jest większe od b lub b jest większe od c")
else:
    print("b jest większe od a lub c jest większe od b")
    pass