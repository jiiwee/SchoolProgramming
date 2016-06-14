# -*- coding: cp1252 -*-

# Panu Partanen Viikko 2 Tehtävä 2
# GitHub https://github.com/Hea7hcliff/SchoolProgramming/tree/master/Python/Python16A

def main():
    num = input("Anna lukuarvo: ")
    num = int(num)
    potency(num)
        
def potency(num):
    num = num**2
    print("Toisen potenssin vastaus on: ", num)

main()