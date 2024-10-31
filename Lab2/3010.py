# Zadanie 1
#A
#for i in range(1, 101):
#   print(i)
#B
#for i in range(100, -1, -1):
#    print(i)
#C
#for i in range(7, 78, 7):
#    print(i)

# Zadanie 2
'''
x = int(input("Podaj rozmiar kwadratu: "))

for j in range(x):
    for i in range(x):
        print("*", end=" ")
    print("")


for j in range(x):
    for i in range(j+1):
        print("*", end=" ")
    print("")
  

for j in range(x):
    for k in range(x - j - 1):
        print(" ", end="")
    for i in range(j+1):
        print("*", end=" ")
    print("")

spc = x - 1

for i in range (x):
    print(" " * spc, end="")
    spc -= 1
    for j in range (i+1):
        print("*", end=" ")
    print("")
'''

# Zadanie 5
tekst = "Rzeszów jest piękny"

print(tekst[0])
print(tekst[6])
print(tekst[0 : 7])
print(tekst[0 : : 2])
print(tekst[-2])

print(tekst[9 : ])

print(tekst[-1 : : -1])
