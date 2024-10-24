# Zadanie 3
"""
imie = "Ewa"
kierunek = "Informatyka"
uczelnia = "WSIZ"

#print(*objects, sep=' ', end='\n', file=None, flush=False)

print("Nazywam się", end=" ")
print(imie)
print("Studiuje na kierunku "+ kierunek, end=" ")
print("na uczelni", uczelnia)
"""

# Zadanie 4
#input(prompt)
#print("Jak masz na imię?")

#name=input("Jak masz na imię? ")
#print("Cześć", name)
#print(f"Witaj {name}")

# Zadanie 5
"""
# Pole = a*b
# Obwód = 2a+2b
bok1=float(input("Podaj długosć pierwszego boku "))
bok2=float(input("Podaj długosć drugiego boku "))
print("Pole prostokąta wynosi:",bok1 * bok2)
# 4* "6" -> 6666
#print(type(bok1))
obw = 2*bok1 + 2*bok2
print("Obwód prostokąta wynosi:", obw)
"""

# Zadanie 6
cena = 6.5
droga = float(input("Jaką trase przejechałeś? "))
spalanie = float(input("Ile pali twój samochód [l/100km]? "))
benzyna = droga/100 * spalanie
koszty = benzyna * cena

print(f"W trakcie tej podróży twój samochód spali {benzyna} litrów paliwa, co będzie cie kosztować {koszty} złotych.")

