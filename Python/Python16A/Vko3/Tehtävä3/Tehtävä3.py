# -*- coding: cp1252 -*-

# Panu Partanen Viikko 3 Tehtävä 3
# GitHub https://github.com/Hea7hcliff/SchoolProgramming/tree/master/Python/Python16A

def main():

    with open('passwords.txt') as x:
        for line in x:
            realline = line.strip('\n') 
            if realline.isalnum() == True :       
                print(realline, end = " : Kelpaa salasanaksi\n")        
            else :       
                print(realline, end = " : Ei kelpaa salasanaksi\n")

main()