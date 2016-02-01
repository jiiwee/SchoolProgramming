﻿/*
Tehtävä 4.
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOB
{
    class Vehicle
    {
        public string name { get; set; }
        public int speed { get; set; }
        public int tyres { get; set; }

        public Vehicle(string name, int speed, int tyres)
        {
            this.name = name;
            this.speed = speed;
            this.tyres = tyres;
        }

        public void PrintData()
        {
            Console.WriteLine(ToString());
            
        }

        public override string ToString()
        {
            return name + " " + speed + " " + tyres;
        }
    }

    class Exercise4
    {
        static void Main(string[] args)
        {
            Vehicle truck = new Vehicle("John Deere", 200, 16);
            truck.PrintData();
            truck.name = "Car";
            truck.PrintData();
        }
    }
}

Tehtävä 5.
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOB
{
    class Student
    {
        public string name { get; set; }
        public int age { get; set; }
        public float average { get; set; }
        public string school { get; set; }

        public Student(string name, int age, float average, string school)
        {
            this.name = name;
            this.age = age;
            this.average = average;
            this.school = school;
        }
    }

    class Exercise5
    {
        static void Main(string[] args)
        {
            string[] Students = new string[5];

            Student person1 = new Student("Name1", 11, 6.2f, "School1");                   
            Students[0] = person1.name + " " + person1.age + " " + person1.average + " " + person1.school;
            
            Student person2 = new Student("Name2", 12, 7.3f, "School2");
            Students[1] = person2.name + " " + person2.age + " " + person2.average + " " + person2.school; ;

            Student person3 = new Student("Name3", 13, 8.4f, "School3");
            Students[2] = person3.name + " " + person3.age + " " + person3.average + " " + person3.school; ;

            Student person4 = new Student("Name4", 14, 9.5f, "School4");
            Students[3] = person4.name + " " + person4.age + " " + person4.average + " " + person4.school; ;

            Student person5 = new Student("Name5", 15, 10.0f, "School5");
            Students[4] = person5.name + " " + person5.age + " " + person5.average + " " + person5.school; ;

            for ( int  x = 0; x < Students.Length;x++)
            {
                Console.WriteLine(Students[x]);
            }
        }
    }
}

Tehtävä 6.
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOB
{
    class Alcohol
    {
        public string brand { get; set; }
        public string type { get; set; }
        public float alcprc { get; set; }
        public string container { get; set; }
        private int Rating{ get; set; }
        public int rating
        {
            get { return Rating; }
            set
            {
                if (value <= MaxRating) { Rating = value; }
                      
            }
        }
        private readonly int MaxRating = 5;

        public Alcohol(string brand, string type, float alcprc, string container, int rating)
        {
            this.brand = brand;
            this.type = type;
            this.alcprc = alcprc;
            this.container = container;
            this.rating = rating;
        }

        public void PrintData()
        {
            Console.WriteLine("Alcohol database : ");
            Console.WriteLine("- Brand : " + brand);
            Console.WriteLine("- Type : " + type);
            Console.WriteLine("- Alcohol procent : " + alcprc);
            Console.WriteLine("- Rating : " + rating + "\n");
        }       
    }

    class Exercise6
    {
        static void Main(string[] args)
        {
            Alcohol alc1 = new Alcohol("brand", "type", 15.5f, "container", 5);
            alc1.PrintData();
        }
    }
}
*/
