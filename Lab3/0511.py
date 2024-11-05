#Zadanie 1
"""
imiona=["Ola", "Tadek", "Janek", "Katia"]

# A
imiona=sorted(imiona)

# B
imiona.append("Władek")
imiona.append("Magda")
#ona=imiona[-1]
ona=imiona.pop()
#print(ona)

#C
imiona.insert(2, "Gosia")

#D
imiona.reverse()
#imiona=imiona*2
#print(imiona*2)

#for imie in imiona:
#    print(imie, end=" ")

#Zadanie 4
lista=["as","kft","ktfs", "hfktrg"]
krotka=tuple(lista)
print(krotka)
#A
suma=0
sk=0
skt=0
s=int(input("Podaj minimalny rozmiar słowa: "))
slowa=[]

for el in krotka:
    #A
    suma+= len(el)
    #B
    for z in el:
        if z=="k" : sk+=1
    #C
    #1
    #if "kt" in el: skt+=1
    #2
    if el.find("kt") < 0: skt += 1

    #D
    if len(el) >= s:
        slowa.append(el)


print(f"Liczba znaków w krotce to: {suma}")
print(f"w krotce znaleziono {sk} wystąpień/nia litery 'k'")
print(f"w krotce znaleziono {skt} wystąpień/nia ciągu 'kt'")
print(f"Słowa o długości większęj niż {s}, to:", end=" ")
for s in slowa: print(s, end=" ")
import random
n= 3
x= 6
lista=[]
slowo=""
dlugosc_slowa=0

for i in range(n):
    # losuj długosć słowa z przedziału <1,x>
    # randint - jak to się ma do lososwania z przedziału

    # for j in dlugosc_slowa:
    #   losuj literę i dodaj ją do słowa
    #   ASCII - jakie kody(numery) ma alfabret małych liter? -> zakres
    #   slowo += wylosowany znak alfabetu

    lista.append(slowo)
    # slowo=""
"""
"""
#Zadanie 5
#Lista zakupów

zakupy={"chleb":5.0, "masło":7.0, "czekolada":12.0, "czipsy":12.0, "woda":2.0 }

#print(zakupy)
suma=0
for el in zakupy:
    #el - indes / klucz
    #zakupy[el] - wartość

    #suma += zakupy[el]
    print(f"{el} za {zakupy[el]} zł")

suma=sum(zakupy.values())
print(f"Za zakupy zapłacimy: {suma}")
"""

#Zadanie 7
X={5, 6, 1}
Y={3, 5, 7, 9, 1, 4, 6}

#A
print(5 in X)
#B
print(X.issubset(Y))

#D
print(X.union(Y))
#E
print(Y.difference(X))

#G
print(X.intersection(Y))
