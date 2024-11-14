#Zadanie 1
"""
a) 1, 2, 3, ... , 99, 100
b) 100, 99, ... , 2, 1, 0
c) 7, 14, 21, ... , 70, 77
d) 20, 18, ... , 2, 0
"""
#for i in range(1, 101):
#    print(i)

#for i in range(100, -1, -1):
#    print(i)

#for i in range(7, 78, 7):
#    print(i)

#for i in range(20, -1, -2):
#    print(i)

#Zadanie 2
#liczbaG=int(input("Ile gwiadek? "))
#print(liczbaG)
"""
#A
for j in range(liczbaG):
    for i in range(liczbaG):
        print("*", end=" ")
    print("")
"""
#B
"""
for j in range(liczbaG):
    for i in range(j+1):
        print("*", end=" ")
    print("")
    """
#C
"""
for j in range(liczbaG):
    print((liczbaG-1-j) * " ", end="")
    for i in range(j+1):
        print("*", end=" ")
    print("")
"""
#Zadanie 6
"""
tresc ="Python jest super"

print(tresc[0])

print(tresc[16])
print(tresc[-1])

#Tekst[i : j : k] - od indeksu i do j z krokiem k

print(tresc[ : : 2])
print(tresc[1: : 3])
print(tresc[10 : : -1])

print(tresc[ : : -1])
#Dlaczego nie wyświetliło się 'P' na początku (index = 0)?

#Zadanie 7
polaczone=tresc+tresc
#print(len(tresc))
"""

#Zadanie 8
# x = <-4, 4>
x=-4
"""
while x <= 4:
    y = 2 * x * x - 5 * x - 8  # Wartosc funkcji
    print(f"Dla argumentu x= {x} wartoś funkcji wynosi {y}")
    x = x + 0.5
    #x += 0.5
else:
    print("Else: Działanie pętli kończy się")
"""
#Zadanie 9

while True:
    a=int(input("Podaj liczbe całkowitą: "))
    print(a)
    if a < 0:
        break




