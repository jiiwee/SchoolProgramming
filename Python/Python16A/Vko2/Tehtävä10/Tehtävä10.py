# -*- coding: cp1252 -*-

# Panu Partanen Viikko 2 Teht�v� 10
# GitHub https://github.com/Hea7hcliff/SchoolProgramming/tree/master/Python/Python16A

def main():
    products = []
    running = True
    while(running) :
        choice = input("--------------------------------------------------------\nHaluatko:\n(1) Lis�t� listaan\n(2) Poistaa listalta\n(3) N�ytt�� listan\n(4) Lopettaa?\nValintasi : ")
        choice = int(choice)
        if choice == 1 :  
            product = input("Mit� lis�t��n  : ")
            products.append(product)            
        elif choice == 2 : 
            length = len(products)
            print("Listalla on ", length, "alkiota (1 on ensimm�inen alkio)")
            print(products)
            delete = input("Monesko niist� poistetaan : ")
            delete = int(delete)
            del products[delete-1] # alkion paikka muutettu
        elif choice == 3 :
            print(products)
        elif choice == 4 : 
            running = False    
            break        
        else : 
            print("V��r� valinta, valitse 1, 2 tai 3")
main()