/*
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
            truck.name = "Samiauto";
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
    }

    class Exercise5
    {
        static void Main(string[] args)
        {
            string[] Students = new string[5];

            Student person1 = new Student();
            person1.name = "Mikko Reipas";
            person1.age = 21;
            person1.average = 4;
            person1.school = "JAMK";          
            Students[0] = person1.name + " " + person1.age + " " + person1.average + " " + person1.school;
            
            Student person2 = new Student();
            person2.name = "Sami Koodi";
            person2.age = 1;
            person2.average = 10;
            person2.school = "Ex Machina";
            Students[1] = person2.name + " " + person2.age + " " + person2.average + " " + person2.school; ;

            Student person3 = new Student();
            person3.name = "Panu Toivo";
            person3.age = 20;
            person3.average = 5;
            person3.school = "JAMK";
            Students[2] = person3.name + " " + person3.age + " " + person3.average + " " + person3.school; ;

            Student person4 = new Student();
            person4.name = "Kalle Jauheliha";
            person4.age = 6;
            person4.average = (float)7.2;
            person4.school = "Liha";
            Students[3] = person4.name + " " + person4.age + " " + person4.average + " " + person4.school; ;

            Student person5 = new Student();
            person5.name = "Artur Venäläinen";
            person5.age = 49;
            person5.average = 7;
            person5.school = "Raja";
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
        public string brand;
        public string type;
        public float alcprc;
        public string container;
        private int Rating;
        public int rating
        {
            get { return Rating; }
            set
            {
                if (value <= MaxRating) { Rating = value; }
                      
            }
        }
        private readonly int MaxRating = 5;

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
            

            Alcohol alc1 = new Alcohol();
            alc1.brand = "Karjala";
            alc1.type = "Beer";
            alc1.alcprc = (float)4.7;
            alc1.rating = 5;
            alc1.container = "Can";
           

            alc1.PrintData();
        }
    }
}
*/

