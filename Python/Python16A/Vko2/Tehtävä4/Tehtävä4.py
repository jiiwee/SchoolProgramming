# -*- coding: cp1252 -*-

# Panu Partanen Viikko 2 Teht�v� 4
# GitHub https://github.com/Hea7hcliff/SchoolProgramming/tree/master/Python/Python16A

def main():
     running = True
     while (running):
        text = input("Anna sy�te ('Lopeta' lopettaa): ")
        text = str(text)
        length = len(text)
        if text == "Lopeta" : 
            running = False
            break
        if length == 0:
         print("Et antanut sy�tett�")
        else : print("Antamasi sy�te oli" , lengthsize(text) , "merkki� pitk�")
        
def lengthsize(text):
    return len(text)

main()