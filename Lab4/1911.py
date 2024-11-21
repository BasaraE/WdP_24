
"""

import math
#Zadanie 1
#Napisz funkcję, która policzy i wypisze pole koła o promieniu r.

def PoleKolaPrint(r):
    if r <= 0:
        print("Koło o takim promieniu nie istnieje")
    else:
        p = math.pi*r*r
        print(f"Koło ma powierzchnię równą: {p}")

#PoleKolaPrint(3)

def PoleKola(r):
    if r <= 0:
        print("Koło o takim promieniu nie istnieje")
    else:
        p = math.pi*r*r
        return p

#print(PoleKola(3)*2)

#Zadanie 5
#Napisz funkcję, obliczającą średnią z listy liczb. Zaprezentuj wywołanie funkcji.

def Srednia(lista):
    s=sum(lista)
    r=s/len(lista)
    return r



def factorial(n):
    if n == 0 or n == 1:
        print("Znamy wynik, wynosi on 1")
        return 1
    else:
        print(f" {n} * factorial(n-1)")
        return n * factorial(n-1)

#factorial(5)

#Zadanie 8
#n’ty stopien potęgi liczby a.

#a=float(input("Podaj liczbę a: "))
n=float(input("Podaj stopień potęgi: "))

def Potega(a, n):
    if n == 1:
        #print("Potęga pierwszego stopnia wynosi 1")
        return a
    else:
        #print(f"Potęga wynosi: {a} * Potega(a, n-1)")
        return a * Potega(a, n-1)

#Potega(a, n)
"""
n=float(input("Podaj liczbę miesięcy: "))

def Fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fib(n-1) + Fib(n-2)

print(Fib(n))

#Zadanie 10

# ver1. rekurencyjna
# wzory     f(n) = 2*f(n-1)+1       LUB     f(n) = f(n-1)+2^(n-1)

# ver2. nierekurencyjna
# wzór f(n) = 2^n -1
