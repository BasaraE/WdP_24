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