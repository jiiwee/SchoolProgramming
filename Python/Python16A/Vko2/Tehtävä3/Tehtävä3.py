# -*- coding: cp1252 -*-

# Panu Partanen Viikko 2 Tehtävä 3
# GitHub https://github.com/Hea7hcliff/SchoolProgramming/tree/master/Python/Python16A

def main():
    running = True
    while (running):                
        
        userInput = input("Anna syöte ('Lopeta' lopettaa): ")
        userInput = str(userInput)
        length = len(userInput)
        if userInput == "Lopeta" : 
            running = False
            break
        if length >= 5 : printer(userInput)
        else : printer()

def printer(userInput = "Oletus tulostus"):
    print(userInput)
      
main()