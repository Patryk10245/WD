#Zad 2

import sys
print("Podaj pierwsza liczbe") 
x = sys.stdin.readline() 
print("Pierwsza liczba: " + x) 

print("Podaj druga liczbe") 
y = sys.stdin.readline() 
print("Druga liczba: " + y)  

wynik = int(x) * int(y)
tekst = str(wynik)
sys.stdout.write("Wynik =" + str(wynik))

