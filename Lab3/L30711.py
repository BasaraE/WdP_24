#Zadanie 1
"""
imiona=["Katia", "Aleks", "Władek", "Zosia"]
#A
posortowane=sorted(imiona)
#print(imiona)
#print(posortowane)
#B
imiona.append("Michał")
imiona.append("Ola")

ostatni=imiona.pop()
print(ostatni)
#C
imiona.insert(2, "Basia")

#D
imiona.reverse()

for imie in imiona *2 :
    print(imie, end= " ")
"""
from sys import int_info

#Zadanie 4
"""
krotka = ("sdas","khrtk", "safktd","ktktdvsk")
suma=0
liczbak=0
liczbakt=0
maxznaki=int(input("Podaj maksymalną długość słowa"))
liczbaslow=0

for slowo in krotka:
    # A
    suma+=len(slowo)
    # B
    for znak in slowo:
        if znak =="k":
            liczbak+=1
    #C
    if slowo.find("kt") >= 0:
       liczbakt+=1
        #co kiedy jest wiele podciagów w jednym słowie

    if len(slowo)<= maxznaki: liczbaslow+=1

print(suma)
print(liczbak)
print(liczbakt)
"""

#Zadanie 5
"""
listaZakupow={"mleko":3.5, "chleb":4, "kiełbasa":20, "piwo":4, "papierosy":17.5 }

for element in listaZakupow:
    print(f"Na liście jest {element} za {listaZakupow[element]} zł")
    #zmienna pomocnicza sumy
    # += lista[el]

print(sum(listaZakupow.values()))
"""

#Zadanie 7

X={3,5,1,8,-9}
Y={3,5,2,-8,0}

#A
print(5 in X)
#B
print (X.issubset(Y))
#D
print(X.union(Y))
#E
print(X.difference(Y))
#G
print(X.intersection(Y))
#H
print(max(X))
#I
a=X.pop()
print(a)
Y.add(a)
print(X)
print(Y)

#J

#Y.add(X)
#1. iteracja po elementach X
#2
Y=X.union(Y)

print(Y)

#K
X.clear()
print(X)