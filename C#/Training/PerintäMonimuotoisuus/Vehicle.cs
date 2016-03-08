using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PerintäMonimuotoisuus
{
    class Vehicle
    {
        public string Manifacture { get; set; }
        public string Model { get; set; }
        public int Year { get; set; }
        public string Color { get; set; }

        public Vehicle()
        {

        }

        public Vehicle(string manifacture, string model, int year, string color)
        {
            Manifacture = manifacture;
            Model = model;
            Year = year;
            Color = color;
        }

        public virtual void Thing()
        {
            Console.WriteLine("Vehicle object: I am a vehicle");
        }

        public override string ToString()
        {
            return "\n-Manifacture : " + Manifacture + "\n-Model : " + Model + "\n-Color : " + Color;
        }

    }
}
