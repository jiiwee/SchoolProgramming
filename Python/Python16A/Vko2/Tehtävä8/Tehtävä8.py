# -*- coding: cp1252 -*-

# Panu Partanen Viikko 2 Teht�v� 8
# GitHub https://github.com/Hea7hcliff/SchoolProgramming/tree/master/Python/Python16A

import Person
import Employee

def main():
    Per1 = Person.Person()
    Emp1 = Employee.Employee()

    print("Henkil�: etunimi = " , Per1.firstname," sukunimi = " , Per1.lastname, " puhelinnumero = ", Per1.number)
    print("Ty�ntekij�: etunimi = " , Emp1.firstname," sukunimi = " , Emp1.lastname, " puhelinnumero = ", Per1.number, "palkka = ", Emp1.wage , "ID = ", Emp1.id)
    
    print("\nHenkil�:")
    Per1.firstname = input("Annappa henkil�n etunimi: ")
    Per1.lastname = input("Annappa henkil�n sukunimi: ")
    Per1.number = input("Annappa henkil�n puhelinnumero: ")
    print("Henkil�: etunimi = ", Per1.firstname, ", sukunimi = ", Per1.lastname, ", Puhelinnumero = ", Per1.number)

    print("\nTy�ntekij�:")
    Emp1.firstname = input("Annappa ty�ntekij�n etunimi: ")
    Emp1.lastname = input("Annappa ty�ntekij�n sukunimi: ")
    Emp1.number = input("Annappa ty�ntekij�n puhelinnumero: ")
    Emp1.wage = input("Annappa ty�ntekij�n palkka: ")
    Emp1.id = input("Annappa ty�ntekij�n id: ")
    print("Henkil�: etunimi = ", Emp1.firstname, ", sukunimi = ", Emp1.lastname, ", Puhelinnumero = ", Emp1.number, ", palkka = ", Emp1.wage , ", ID = ", Emp1.id)
        
main()