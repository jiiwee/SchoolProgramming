# -*- coding: cp1252 -*-

class TestResults():
        
    def __init__(self):
        self.results = []

    def askScore(self):
        running = True
        while (running):
            
            num = input("Koepisteet? (<0 = lopeta) : ") 
            num = int(num)      
            if num < 0: running = False    
            self.results.append(num)

    def printBest(self):
        print("Paras pistemäärä oli: ", max(self.results))