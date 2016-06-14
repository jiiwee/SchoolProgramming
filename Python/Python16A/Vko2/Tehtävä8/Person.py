# -*- coding: cp1252 -*-

class Person():
           
      def __init__(self):
          self.firstname = "?"
          self.lastname = "?"
          self.number = 0

      def get(self):
          return self.firstname, self.lastname, self.number
      
      def set(self, firstname, lastname, number):
          self.firstname = firstname
          self.lastname = lastname
          self.number = number