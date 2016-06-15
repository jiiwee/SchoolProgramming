# -*- coding: cp1252 -*-

# Panu Partanen Viikko 3 Tehtävä 1
# GitHub https://github.com/Hea7hcliff/SchoolProgramming/tree/master/Python/Python16A

def main():

    file = open("something.txt", "r", encoding="cp1252")
    all = file.read()
    print("Tiedostosta luettiin teksti: ", all, end = "") 
    file.close()

main()