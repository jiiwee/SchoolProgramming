# -*- coding: cp1252 -*-

import math

# Panu Partanen Viikko 1 Tehtävät
# GitHub https://github.com/Hea7hcliff/SchoolProgramming/tree/master/Python/Python16A
'''
#------------------------------------------#

# Tehtävä 1

something = "merkkijonosisältöä"
print(something)

#------------------------------------------#

# Tehtävä 2

num1 = 1000
num2 = 24

total = (num1+num2+15)**2
print(total)

#------------------------------------------#

# Tehtävä 3

print("Tämä on usean rivin tulostus:\nTeksti on jaettu usealle eri riville.\nNimi:\tPetteri\nAmmatti: Kartturi")

#------------------------------------------#

# Tehtävä 4

print("Laskin")
number1 = input("Anna ensimmäinen luku: ")
number1 = int(number1)
number2 = input("Anna toinen luku: ")
number2 = int(number2)
sum = number1+number2
print("Tulos on: " , sum)

#------------------------------------------#

# Tehtävä 5

word = "Hattukauppias"
print("Muuttujan 4 ensimmäistä kirjainta ovat", word[:4])
print("Muuttujan 4 viimeistä kirjainta ovat", word[9:])
print("Muuttujan teksti on väärinpäin", word[::-1])

#------------------------------------------#

# Tehtävä 6

number1 = input("Anna luku: ")
number1 = int(number1)
remainder = number1 % 2

if remainder == 0 : print("Luku on parillinen")
else : print("Luku ei ole parillinen")

#------------------------------------------#

# Tehtävä 7

number = input("Valitse kohde (1-3): ")
number = int(number)

if number == 1 : print("Haukion kala Oy") 
elif number == 2 : print("Metallipaja VasaraAika") 
elif number == 3 : print("Balin palapelitehdas") 
else : print("Luku ei ole 1-3 sisällä")

#------------------------------------------#

# Tehtävä 8

number1 = input("Anna ensimmäinen luku: ")
number1 = int(number1)
number2 = input("Anna toinen luku: ")
number2 = int(number2)

info = "(1) +\n(2) -\n(3) *\n(4) /"
print(info)
number3 = input("Tee valinta 1-4: ")
number3 = int(number3)

if number3 == 1 : total = number1 + number2
elif number3 == 2 : total = number1 - number2
elif number3 == 3 : total = number1 * number2
elif number3 == 4 : total = number1 / number2
else : print("Luku ei ole 1-4 sisällä")

print("Tulos on: ", total)

#------------------------------------------#

# Tehtävä 9

for i in range(0, 5):
  line = 'Olemme kierroksella'
  print(line, i)

#------------------------------------------#

# Tehtävä 10

running = True
while running : 
    merkkijono = input("Kirjoita jotain: ")
    merkkijono = str(merkkijono)
    print(merkkijono)
    if merkkijono == "lopeta" : running = False

#------------------------------------------#

# Tehtävä 11

number1 = input("Anna ensimmäinen luku: ")
number1 = int(number1)
number2 = input("Anna toinen luku: ")
number2 = int(number2)

running = True
while running : 
    info = "(1) +\n(2) -\n(3) *\n(4) /\n(5) Vaihda luvut\n(6)Lopeta"
    print(info)
    number3 = input("Tee valinta 1-6: ")
    number3 = int(number3)

    if number3 == 1 : total = number1 + number2
    elif number3 == 2 : total = number1 - number2
    elif number3 == 3 : total = number1 * number2
    elif number3 == 4 : total = number1 / number2
    elif number3 == 5 : 
        number1 = input("Anna uusi ensimmäinen luku: ")
        number1 = int(number1)
        number2 = input("Anna uusi toinen luku: ")
        number2 = int(number2)
        continue
    elif number3 == 6 : running = False
    else : print("Luku ei ole 1-6 sisällä")
    print()
    print("Tulos on: ", total)

#------------------------------------------#

# Tehtävä 12

money = input("Anna valuuttamäärä euroissa: ")
money = int(money)

dollar = money/0.73
print("Muunnettu valuutta: ", dollar, "$")

#------------------------------------------#

# Tehtävä 13

measure = input("Anna kartan mittakaava: 1:")
measure = int(measure)
distance = input("Anna kartalta mitattu matka senttimetreinä: ")
distance = int(distance)
measure = measure/10000
km = distance*measure
print("Kuljettu matka = " , km , "km")

#------------------------------------------#

# Tehtävä 14

radius = input("Anna ympyrän säde: ")
radius = int(radius)

area = math.pi*radius**2
print("Ympyrän pinta-ala =", area)

#------------------------------------------#

# Tehtävä 15

for i in range(0, 50):
  line = 'Panu Partanen'
  print(line)

#------------------------------------------#

# Tehtävä 16

while True :    
    temperature = input("Anna lämpötila: ")
    temperature = float(temperature)
    if temperature < -30 : print("Todella kylmää")
    elif temperature >= -30 and temperature <= 0 : print("Kylmää")
    elif temperature > 0 and temperature <= 20 : print("Sopivaa")
    else : print("Todella kuumaa")

#------------------------------------------#

# Tehtävä 17

total = 0
piece = input("Anna arvosanojen määrä: ")
piece = int(piece)
for i in range (0, piece) :
    grade = input("Arvosana: ")
    grade = int(grade)
    if grade < 0 : break
    elif grade > 5 :         
        print("Uusi arvosana")        
        grade = input("Arvosana: ")
        grade = int(grade)
        total += grade
        continue
    else : total += grade
average = total / piece
print("Keskiarvo on: ", average)

#------------------------------------------#

# Tehtävä 18

num = input("Anna  0, 1 tai 2: ")
num = int(num)

# TAPA 1

# if num == 0 or num == 1 or num == 2 : print()
# else : print("VIRHE")

# TAPA 2

#if num != 0 and num != 1 and num !=2 : print("VIRHE")

#------------------------------------------#

# Tehtävä 19

friction = input("Anna frictionkerroin väliltä 0.1 - 0.8: ")
friction = float(friction)

for i in range (30,140,10) :
    brakingDist = (i/3.6)**2/(2*friction*9.81)
    brakingDist = float(brakingDist)
    print("Jarrutusmatka nopeudesta ", i , " on " , brakingDist , "m")
'''