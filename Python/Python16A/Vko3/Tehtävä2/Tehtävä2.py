# -*- coding: cp1252 -*-

# Panu Partanen Viikko 3 Tehtävä 2
# GitHub https://github.com/Hea7hcliff/SchoolProgramming/tree/master/Python/Python16A

def main():
    
    filename = input("Minkä niminen tiedosto luodaan? (tekstitiedosto = .txt pääte): ")
    file = open(filename, "w")

    text = input("Mitä haluat kirjotitaa tiedostoon? : ")
    file.write(text)
    file.close()
  
    file = open(filename, "r", encoding="cp1252")
    all = file.read()

    print("Luotiin tiedosto", filename)
    print("ja siihen tallennettiin teksti: ", all) 
    file.close()

main()