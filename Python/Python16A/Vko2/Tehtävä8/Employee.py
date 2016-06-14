# -*- coding: cp1252 -*-

import Person

class Employee(Person.Person):

      def __init__(self):
          Person.Person.__init__(self)
          self.wage = 0
          self.id = 0
          
      def get(self):
          return self.firstname, self.lastname, self.number, self.id, self.wage
      
      def set(self, wage, id):
          self.wage = wage
          self.id = id