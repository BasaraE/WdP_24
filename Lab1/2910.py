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
123=121

