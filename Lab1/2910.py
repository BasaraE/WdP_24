# Zadanie 8
# czy pełnoletni?
# >=18
"""
wiek = int(input("Ile masz lat? "))

if wiek >= 18 :
    print("Jesteś pełnoletni")
else:
    print("Jesteś dzieckiem")
"""
from xml.etree.ElementInclude import include

# złe odpowiedzi:
# 0
# liczby ujemne
# >150
"""
if (wiek > 0) and (wiek < 150) :
    if wiek >= 18:
        print("Jesteś pełnoletni")
    else:
        print("Jesteś dzieckiem")
else:
    print("Podane dane są niepoprawne")
"""
#print(wiek)

# Zadanie 10
"""
x=int(input("Podaj pierwszą liczbę: "))
y=int(input("Podaj drugą liczbę: "))
z=int(input("Podaj trzecią liczbę: "))

if x > y:
    if x > z:
        if y > z:
            print( f"liczby roznąco: {z}, {y}, {x}")
        else:
            print(f"liczby roznąco: {y}, {z}, {x}")
    else:
        print(f"liczby roznąco: {y}, {x}, {z}")
else:
    if x < z:
        if y < z:
            print( f"liczby roznąco: {x}, {y}, {z}")
        else:
            print(f"liczby roznąco: {x}, {z}, {y}")
    else:
        print(f"liczby roznąco: {z}, {x}, {y}")


# Zadanie 11
## a^2 + bx + c =0
import math
a=int(input("Podaj współczynnik a: "))
b=int(input("Podaj współczynnik b: "))
c=int(input("Podaj współczynnik c: "))

delta = b*b - 4*a*c
print(delta)

if delta == 0:
    rozw= -b/ (2*a)
    print(f"Równanie ma jedno rozwiązanie: {rozw}")
elif delta > 0:
    rozw = -b - math.sqrt(delta) / (2 * a)
    rozw2 = -b + math.sqrt(delta) / (2 * a)
    print(f"Równanie ma dwa rozwiązania: {rozw}, {rozw2}")
else:
    print("Równanie jest sprzeczne")
"""








### Lab 2
# Zadanie 1
#a
#for i in range(1, 101):
#    print(i)
#b
#for i in range(100, -1, -1):
#    print(i)
#range(7, 78, 7)
#range(20, -1, -2)

# Zadanie 2

#ile=int(input("Ile lini gwiazdek wyświetlić? "))
""" A
for i in range (ile):
    for i in range (ile):
        print("*", end=" ")
    print("")
"""
""" B
for i in range (ile):
    for j in range (i+1):
        print("*", end=" ")
    print("")

# ile = "*" + " " - zawsze 2 znaki :)
spc = ile - 1

for i in range (ile):
    print(" " * spc, end="")
    spc -= 1
    for j in range (i+1):
        print("*", end=" ")
    print("")




#for znak in "spam_napis":
#    print(znak, end=' ')

"""
# Zadanie 5
tekst = "Rzeszów jest piękny"
print(tekst)
#print(tekst[6]) #7 LITERA TO INDEX 6
#print(tekst[0])
#print(tekst[-1])
#print(tekst[0 : : 2])
#print(tekst[10 : ])
#print(tekst[-1 : : -1])