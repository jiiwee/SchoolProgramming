# -*- coding: cp1252 -*-

# Panu Partanen Viikko 3 Teht�v� 2
# GitHub https://github.com/Hea7hcliff/SchoolProgramming/tree/master/Python/Python16A

def main():
    
    filename = input("Mink� niminen tiedosto luodaan? (tekstitiedosto = .txt p��te): ")
    file = open(filename, "w")

    text = input("Mit� haluat kirjotitaa tiedostoon? : ")
    file.write(text)
    file.close()
  
    file = open(filename, "r", encoding="cp1252")
    all = file.read()

    print("Luotiin tiedosto", filename)
    print("ja siihen tallennettiin teksti: ", all) 
    file.close()

main()