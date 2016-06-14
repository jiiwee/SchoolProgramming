# -*- coding: cp1252 -*-

import math

# Panu Partanen Viikko 1 Teht�v�t
# GitHub https://github.com/Hea7hcliff/SchoolProgramming/tree/master/Python/Python16A
'''
#------------------------------------------#

# Teht�v� 1

something = "merkkijonosis�lt��"
print(something)

#------------------------------------------#

# Teht�v� 2

num1 = 1000
num2 = 24

total = (num1+num2+15)**2
print(total)

#------------------------------------------#

# Teht�v� 3

print("T�m� on usean rivin tulostus:\nTeksti on jaettu usealle eri riville.\nNimi:\tPetteri\nAmmatti: Kartturi")

#------------------------------------------#

# Teht�v� 4

print("Laskin")
number1 = input("Anna ensimm�inen luku: ")
number1 = int(number1)
number2 = input("Anna toinen luku: ")
number2 = int(number2)
sum = number1+number2
print("Tulos on: " , sum)

#------------------------------------------#

# Teht�v� 5

word = "Hattukauppias"
print("Muuttujan 4 ensimm�ist� kirjainta ovat", word[:4])
print("Muuttujan 4 viimeist� kirjainta ovat", word[9:])
print("Muuttujan teksti on v��rinp�in", word[::-1])

#------------------------------------------#

# Teht�v� 6

number1 = input("Anna luku: ")
number1 = int(number1)
remainder = number1 % 2

if remainder == 0 : print("Luku on parillinen")
else : print("Luku ei ole parillinen")

#------------------------------------------#

# Teht�v� 7

number = input("Valitse kohde (1-3): ")
number = int(number)

if number == 1 : print("Haukion kala Oy") 
elif number == 2 : print("Metallipaja VasaraAika") 
elif number == 3 : print("Balin palapelitehdas") 
else : print("Luku ei ole 1-3 sis�ll�")

#------------------------------------------#

# Teht�v� 8

number1 = input("Anna ensimm�inen luku: ")
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
else : print("Luku ei ole 1-4 sis�ll�")

print("Tulos on: ", total)

#------------------------------------------#

# Teht�v� 9

for i in range(0, 5):
  line = 'Olemme kierroksella'
  print(line, i)

#------------------------------------------#

# Teht�v� 10

running = True
while running : 
    merkkijono = input("Kirjoita jotain: ")
    merkkijono = str(merkkijono)
    print(merkkijono)
    if merkkijono == "lopeta" : running = False

#------------------------------------------#

# Teht�v� 11

number1 = input("Anna ensimm�inen luku: ")
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
        number1 = input("Anna uusi ensimm�inen luku: ")
        number1 = int(number1)
        number2 = input("Anna uusi toinen luku: ")
        number2 = int(number2)
        continue
    elif number3 == 6 : running = False
    else : print("Luku ei ole 1-6 sis�ll�")
    print()
    print("Tulos on: ", total)

#------------------------------------------#

# Teht�v� 12

money = input("Anna valuuttam��r� euroissa: ")
money = int(money)

dollar = money/0.73
print("Muunnettu valuutta: ", dollar, "$")

#------------------------------------------#

# Teht�v� 13

measure = input("Anna kartan mittakaava: 1:")
measure = int(measure)
distance = input("Anna kartalta mitattu matka senttimetrein�: ")
distance = int(distance)
measure = measure/10000
km = distance*measure
print("Kuljettu matka = " , km , "km")

#------------------------------------------#

# Teht�v� 14

radius = input("Anna ympyr�n s�de: ")
radius = int(radius)

area = math.pi*radius**2
print("Ympyr�n pinta-ala =", area)

#------------------------------------------#

# Teht�v� 15

for i in range(0, 50):
  line = 'Panu Partanen'
  print(line)

#------------------------------------------#

# Teht�v� 16

while True :    
    temperature = input("Anna l�mp�tila: ")
    temperature = float(temperature)
    if temperature < -30 : print("Todella kylm��")
    elif temperature >= -30 and temperature <= 0 : print("Kylm��")
    elif temperature > 0 and temperature <= 20 : print("Sopivaa")
    else : print("Todella kuumaa")

#------------------------------------------#

# Teht�v� 17

total = 0
piece = input("Anna arvosanojen m��r�: ")
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

# Teht�v� 18

num = input("Anna  0, 1 tai 2: ")
num = int(num)

# TAPA 1

# if num == 0 or num == 1 or num == 2 : print()
# else : print("VIRHE")

# TAPA 2

#if num != 0 and num != 1 and num !=2 : print("VIRHE")

#------------------------------------------#

# Teht�v� 19

friction = input("Anna frictionkerroin v�lilt� 0.1 - 0.8: ")
friction = float(friction)

for i in range (30,140,10) :
    brakingDist = (i/3.6)**2/(2*friction*9.81)
    brakingDist = float(brakingDist)
    print("Jarrutusmatka nopeudesta ", i , " on " , brakingDist , "m")
'''