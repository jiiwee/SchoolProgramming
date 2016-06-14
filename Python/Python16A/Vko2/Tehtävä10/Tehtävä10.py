# -*- coding: cp1252 -*-

# Panu Partanen Viikko 2 Tehtävä 10
# GitHub https://github.com/Hea7hcliff/SchoolProgramming/tree/master/Python/Python16A

def main():
    products = []
    running = True
    while(running) :
        choice = input("--------------------------------------------------------\nHaluatko:\n(1) Lisätä listaan\n(2) Poistaa listalta\n(3) Näyttää listan\n(4) Lopettaa?\nValintasi : ")
        choice = int(choice)
        if choice == 1 :  
            product = input("Mitä lisätään  : ")
            products.append(product)            
        elif choice == 2 : 
            length = len(products)
            print("Listalla on ", length, "alkiota (1 on ensimmäinen alkio)")
            print(products)
            delete = input("Monesko niistä poistetaan : ")
            delete = int(delete)
            del products[delete-1] # alkion paikka muutettu
        elif choice == 3 :
            print(products)
        elif choice == 4 : 
            running = False    
            break        
        else : 
            print("Väärä valinta, valitse 1, 2 tai 3")
main()