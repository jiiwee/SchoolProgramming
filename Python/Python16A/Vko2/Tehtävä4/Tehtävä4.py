# -*- coding: cp1252 -*-

# Panu Partanen Viikko 2 Tehtävä 4
# GitHub https://github.com/Hea7hcliff/SchoolProgramming/tree/master/Python/Python16A

def main():
     running = True
     while (running):
        text = input("Anna syöte ('Lopeta' lopettaa): ")
        text = str(text)
        length = len(text)
        if text == "Lopeta" : 
            running = False
            break
        if length == 0:
         print("Et antanut syötettä")
        else : print("Antamasi syöte oli" , lengthsize(text) , "merkkiä pitkä")
        
def lengthsize(text):
    return len(text)

main()