from numba.core.typing.builtins import Print


def divide(a, b):
    if b!= 0:
        print(a/b)
    else:
        print('Nie dzielimy przez 0 !')

#divide(6, 0)
#LUB
#divide(b=2, a=6)

def divideR(a, b):
    if b!= 0:
        return a/b
    else:
        print('Nie dzielimy przez 0 !')

#print(divideR(6, 2))

#Zadanie1
#Napisz funkcję, która policzy i wypisze pole koła o promieniu r.

import math

def PoleKola(r):
    if r<=0:
        print("Koło o takim promieniu nie istnieje")
        #return
    else:
        p=r*r*math.pi
        return p

#print(PoleKola(4))
#dokładność 2 miejsca po ,?





def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

#Zadanie 8
def PowR(a, n):
    if n>=0:
        if n == 0:
            return 1
        elif n==1:
            return a
        else:
            return a * PowR(a, n-1)
    else:
        return "nie w tej funkcji"

# a, n są liczbami naturalnymi podawanymi przez użytkownika

#print(PowR(2,0.5))


def Fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fib(n-1) + Fib(n-2)
    


def Han(n):
    if n == 1:
        return 1
    else:
        return 2 * Han(n-1) + 1

print(Han(1))
print(Han(2))
print(Han(3))
print(Han(4))
print(Han(5))
print(Han(6))