#Zadanie 8
#𝑥∈[−4,4]
#krokiem 0.5
"""
x=-4
while x <= 4:
    y=2*x*x-5*x-8
    print(f"Dla x= {x} funkcja ma wartość {y}")
    x+=0.5
"""
from pickletools import long1

#Zadanie 9
"""
while True:
    liczba = int(input("Podaj liczbę całkowitą: "))
    if liczba < 0:
        break

print("Działanie pętli się zakończyło")
"""

#Zadanie 10
"""
l1 = int(input("podaj pierwsza liczbę całkowitą: "))
l2 = int(input("podaj drugą liczbę całkowitą: "))

if l1 > l2:
    l1, l2 = l2, l1
#od treraz zawsze l1 < l2

while l1<=l2 :
    print(l1)
    l1+=1
"""
#Zadanie 11
l1 = int(input("podaj pierwsza liczbę całkowitą: "))
l2 = int(input("podaj drugą liczbę całkowitą: "))

if l1 > l2:
    l1, l2 = l2, l1

while l1<=l2 :
    if l1%2 == 0:
        print(l1-1)
        l1 += 1
    else:
        l1 += 1
        continue
