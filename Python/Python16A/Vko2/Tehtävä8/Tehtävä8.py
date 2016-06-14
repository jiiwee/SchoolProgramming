# -*- coding: cp1252 -*-

# Panu Partanen Viikko 2 Tehtävä 8
# GitHub https://github.com/Hea7hcliff/SchoolProgramming/tree/master/Python/Python16A

import Person
import Employee

def main():
    Per1 = Person.Person()
    Emp1 = Employee.Employee()

    print("Henkilö: etunimi = " , Per1.firstname," sukunimi = " , Per1.lastname, " puhelinnumero = ", Per1.number)
    print("Työntekijä: etunimi = " , Emp1.firstname," sukunimi = " , Emp1.lastname, " puhelinnumero = ", Per1.number, "palkka = ", Emp1.wage , "ID = ", Emp1.id)
    
    print("\nHenkilö:")
    Per1.firstname = input("Annappa henkilön etunimi: ")
    Per1.lastname = input("Annappa henkilön sukunimi: ")
    Per1.number = input("Annappa henkilön puhelinnumero: ")
    print("Henkilö: etunimi = ", Per1.firstname, ", sukunimi = ", Per1.lastname, ", Puhelinnumero = ", Per1.number)

    print("\nTyöntekijä:")
    Emp1.firstname = input("Annappa työntekijän etunimi: ")
    Emp1.lastname = input("Annappa työntekijän sukunimi: ")
    Emp1.number = input("Annappa työntekijän puhelinnumero: ")
    Emp1.wage = input("Annappa työntekijän palkka: ")
    Emp1.id = input("Annappa työntekijän id: ")
    print("Henkilö: etunimi = ", Emp1.firstname, ", sukunimi = ", Emp1.lastname, ", Puhelinnumero = ", Emp1.number, ", palkka = ", Emp1.wage , ", ID = ", Emp1.id)
        
main()