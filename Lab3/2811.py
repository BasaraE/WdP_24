"""
imiona=["Oleh", "Patryk", "Paweł", "James"]

posortowane=sorted(imiona)

imiona.append("Patrycja")
imiona.append("Weronika")

for i in imiona:
    print(i, end=" ")
print("")

dziewczyna=imiona.pop()
print(dziewczyna)

imiona.insert(2, "Basia")

for i in imiona:
    print(i, end=" ")
print("")

imiona.reverse()

for i in imiona :
    print(f"{i} "*2,end="")
"""
from tkinter import XView

from pkg_resources import load_entry_point

#zad 4
"""
lista=["sdk", "qwer", "sktkt", "kkt", "abc"]
krotka=tuple(lista)

#print(lista)
#print(krotka)
sumaZ=0
sumaK=0
sumaKT=0
sumaW=0

s=int(input("Podaj minimalną długosć słowa: "))

for k in krotka:
    #print(len(k))
    sumaZ+=len(k)
    #print(sumaZ)
    for z in k:
        #if "k" in z:
        if z == "k":
            sumaK += 1
    #if "kt" in k:
    #    sumaKT+=1
    sumaKT+=k.count("kt")
        #jak znaleźć wszystkie "kt"?
    if len(k)>s:
        sumaW+=1

print(sumaZ)
print(sumaK)
print(sumaKT)
print(sumaW)
"""
"""
#Zadanie 5
lista=[4,9,4,7]
lista[0], lista[3]
listaZakupow={"piwo":4, "czipsy":9, "kitkat":4, "redbull":7 }
listaZakupow[kitkat]

print(listaZakupow)
print(listaZakupow.keys())
print(listaZakupow.items())
print(listaZakupow.values())


for el in listaZakupow:
    #print(el)
    print(f"Na rachunku znajduje się {el} za {listaZakupow[el]} zł")
    #print(f"Na rachunku znajduje się {el.keys()} za {listaZakupow[el]} zł")

for i in listaZakupow.items():
    print(f"Na rachunku znajduje się {i[0]} za {i[1]} zł")

#for i in range():
#    listaZakupow.keys()[i]
#    listaZakupow.values()[i]
"""

X = {1,2,4,6,8,0,12}
Y = {1,2,4,6,3,9,13}

if 5 in X :
    print("tak")
else:
    print("nie")
# if w jednej lini

print(X.issubset(Y)) #podzbiór
print(X.union(Y)) #suma
print(X.difference(Y)) #różnica
print(X.intersection(Y)) #iloczyn
print(max(Y)) # max
Y.add(X.pop())
print(Y)

Y=Y.union(X) # przypisanie wszystkich wartości w jednym zbiorze
print(Y)

X.clear() # wyczyszczenie zbioru
print(X)