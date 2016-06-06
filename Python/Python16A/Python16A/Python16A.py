#-*- coding: utf-8 -*-
# -*- coding: cp1252 -*-
import math
'''
# Week 1
#------------------------------------------#

# Excercise 1

merkkijono = "merkkijonosisältöä"
print(merkkijono)

#------------------------------------------#

# Excercise 2

num1 = 1000
num2 = 24

total = (num1+num2+15)**2
print(total)

#------------------------------------------#

# Excercise 3

print("Tämä on usean rivin tulostus:\nTeksti on jaettu usealle eri riville.\nNimi:\tPetteri\nAmmatti: Kartturi")

#------------------------------------------#

# Excercise 4

print("Laskin")
number1 = input("Anna ensimmäinen luku: ")
number1 = int(number1)
number2 = input("Anna toinen luku: ")
number2 = int(number2)
sum = number1+number2
print("Tulos on: " , sum)

#------------------------------------------#

# Excercise 5

word = "Hattukauppias"
print("Muuttujan 4 ensimmäistä kirjainta ovat", word[:4])
print("Muuttujan 4 viimeistä kirjainta ovat", word[9:])
print("Muuttujan teksti on väärinpäin", word[::-1])

#------------------------------------------#

# Excercise 6

number1 = input("Anna luku: ")
number1 = int(number1)
jakojäännös = number1 % 2

if jakojäännös == 0 : print("Luku on parillinen")
else : print("Luku ei ole parillinen")

#------------------------------------------#

# Excercise 7

number = input("Valitse kohde (1-3): ")
number = int(number)

if number == 1 : print("Haukion kala Oy") 
elif number == 2 : print("Metallipaja VasaraAika") 
elif number == 3 : print("Balin palapelitehdas") 
else : print("Luku ei ole 1-3 sisällä")

#------------------------------------------#

# Excercise 8

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

# Excercise 9

for i in range(0, 5):
  line = 'Olemme kierroksella'
  print(line, i)

#------------------------------------------#

# Excercise 10

running = True
while running : 
    merkkijono = input("Kirjoita jotain: ")
    merkkijono = str(merkkijono)
    print(merkkijono)
    if merkkijono == "lopeta" : running = False

#------------------------------------------#

# Excercise 11

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

# Excercise 12

money = input("Anna valuuttamäärä euroissa: ")
money = int(money)

dollar = money/0.73
print("Muunnettu valuutta: ", dollar, "$")

#------------------------------------------#

# Excercise 13

mitta = input("Anna kartan mittakaava: 1:")
mitta = int(mitta)
matka = input("Anna kartalta mitattu matka senttimetreinä: ")
matka = int(matka)
mitta = mitta/10000
km = matka*mitta
print("Kuljettu matka = " , km , "km")

#------------------------------------------#

# Excercise 14

säde = input("Anna ympyrän säde: ")
säde = int(säde)

ala = math.pi*säde**2
print("Ympyrän pinta-ala =", ala)

#------------------------------------------#

# Excercise 15

for i in range(0, 50):
  line = 'Panu Partanen'
  print(line)

#------------------------------------------#

# Excercise 16

while True :    
    temperature = input("Anna lämpötila: ")
    temperature = float(temperature)
    if temperature < -30 : print("Todella kylmää")
    elif temperature >= -30 and temperature <= 0 : print("Kylmää")
    elif temperature > 0 and temperature <= 20 : print("Sopivaa")
    else : print("Todella kuumaa")

#------------------------------------------#

# Excercise 17

summa = 0
kappale = input("Anna arvosanojen määrä: ")
kappale = int(kappale)
for i in range (0, kappale) :
    arvosana = input("Arvosana: ")
    arvosana = int(arvosana)
    if arvosana < 0 : break
    elif arvosana > 5 :         
        print("Uusi arvosana")        
        arvosana = input("Arvosana: ")
        arvosana = int(arvosana)
        summa += arvosana
        continue
    else : summa += arvosana
ka = summa / kappale
print("Keskiarvo on: ", ka)

#------------------------------------------#

# Excercise 18

luku = input("Anna  0, 1 tai 2: ")
luku = int(luku)

#TAPA 1

# if luku == 0 or luku == 1 or luku == 2 : print()
# else : print("VIRHE")

#TAPA 2

#if luku != 0 and luku != 1 and luku !=2 : print("VIRHE")

#------------------------------------------#

# Excercise 19

kitka = input("Anna kitkakerroin väliltä 0.1 - 0.8: ")
kitka = float(kitka)

for i in range (30,140,10) :
    jmatka = (i/3.6)**2/(2*kitka*9.81)
    jtmatka = float(jmatka)
    print("Jarrutusmatka nopeudesta ", i , " on " , jmatka , "m")
'''