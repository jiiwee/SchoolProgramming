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
            print("Pelasit", rounds , "kierrosta, joista voitit" , score.count("Voitto"), ", hävisit " , score.count("Häviö") , " ja pelasit tasan " , score.count("Tasapeli") , " kierrosta")
            break
        print("Sinä valitsit: ", player)
        print("computer valitsi: ", computer)

        rounds += 1
        if player == computer : 
            print("Tasapeli", "\n")
            score.append("Tasapeli")
        elif player == "Kivi":
            if computer == "Paperi":
                print("Hävisit,", computer, "voittaa", player, "\n")
                score.append("Häviö")
            else:
                print("Voitit,", player, "voittaa", computer, "\n")
                score.append("Voitto")
        elif player == "Paperi":
            if computer == "Sakset":
                print("Hävisit, ", computer, "voittaa", player, "\n")
                score.append("Häviö")
            else:
                print("Voitit,", player, "voittaa", computer, "\n")
                score.append("Voitto")
        elif player == "Sakset":
            if computer == "Kivi":
                print("Hävisit,", computer, "voittaa", player, "\n")
                score.append("Häviö")                
            else:
                print("Voitit,", player, "voittaa", computer, "\n")
                score.append("Voitto")
        else:
            print("Muista isoalkukirjain (Kivi, Paperi, Sakset)\n")
            rounds -= 1