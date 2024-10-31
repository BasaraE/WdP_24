# Zadanie 8
# wiek >= 18 -> dorosły

wiek = int(input("Ile masz lat? "))

#debug
#print(wiek)
#print(type(wiek))
"""
if wiek >= 18 :
    print("Osoba dorosła")
else:
    print("Dziecko")
"""

#Zadanie 9

if wiek > 0 and wiek < 150:
    if wiek < 4:
       print("Wchodzi za darmo")
    elif wiek < 18 :
        print("koszt biletu to 10 zł")
    else:
        student = input("Czy jesteś studewntem? (T/N) ")
        if student == "T":
            print("Koszt biletu wynosi 15 zł")
        else:
            print("Koszt biletu to 20 zł")
else:
    print("niepoprawny wiek")