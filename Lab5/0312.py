import  random
import math
from datetime import date, datetime

#Zadanie 1
#A
# osób 22
# losujemy 1-22

numerek = random.randint(1,22)
print("Dziesiejszy szczęśliwy numerek dla grupy GL01, to: ",numerek)

#B
roczniki = [2000, 2001, 2002, 2003, 2004, 2005]
szczesliwy_rocznik = random.choice(roczniki)
print("Szczęśliwy rocznik dla grupy GL01, to: ",szczesliwy_rocznik)

#Zadanie 2
#C
w1 = math.sqrt(2) + math.sqrt(3) + math.sqrt(6)
#print(math.sqrt(2))
#print(math.sqrt(3))
#print(math.sqrt(6))
w1 = math.ceil(w1)
# poza bibl math jest jeszcze round()

print(w1)

#w2 = math.sqrt(-5)
#print(w2)

#Zadanie 4

dzis = date.today()
zajecia = date(2024,11,19)
kolokwium = date(2025,1,7)
#YYYY-MM-DD


print(dzis)
print(zajecia)
print(kolokwium)
