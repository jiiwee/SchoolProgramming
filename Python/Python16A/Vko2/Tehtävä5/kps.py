# -*- coding: cp1252 -*-

import random

def kpsLogic():
    kps = ("Kivi", "paperi", "Sakset")
    score = []
    rounds = 0
    running = True
    while (running):
        
        computer = random.choice(kps)    
        player = input("Kivi, paperi vai Sakset? ('Lopeta' Lopettaa): ")
        player = str(player)
        if player == "Lopeta" :
            running = False
            print("Pelasit", rounds , "kierrosta, joista voitit" , score.count("Voitto"), ", h�visit " , score.count("H�vi�") , " ja pelasit tasan " , score.count("Tasapeli") , " kierrosta")
            break
        print("Sin� valitsit: ", player)
        print("computer valitsi: ", computer)

        rounds += 1
        if player == computer : 
            print("Tasapeli", "\n")
            score.append("Tasapeli")
        elif player == "Kivi":
            if computer == "Paperi":
                print("H�visit,", computer, "voittaa", player, "\n")
                score.append("H�vi�")
            else:
                print("Voitit,", player, "voittaa", computer, "\n")
                score.append("Voitto")
        elif player == "Paperi":
            if computer == "Sakset":
                print("H�visit, ", computer, "voittaa", player, "\n")
                score.append("H�vi�")
            else:
                print("Voitit,", player, "voittaa", computer, "\n")
                score.append("Voitto")
        elif player == "Sakset":
            if computer == "Kivi":
                print("H�visit,", computer, "voittaa", player, "\n")
                score.append("H�vi�")                
            else:
                print("Voitit,", player, "voittaa", computer, "\n")
                score.append("Voitto")
        else:
            print("Muista isoalkukirjain (Kivi, Paperi, Sakset)\n")
            rounds -= 1