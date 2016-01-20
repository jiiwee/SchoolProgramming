using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOB
{
    class Stove
    {
        private string brand;
        private float temperature;
        private int maxtemperature = 200;
        private float dampness;
        private int power;

        public string Brand
        {
            get { return brand; }
            set { brand = value; }
        }

        public float Temp
        {
            get { return temperature; }
            set {
                if (temperature == maxtemperature)
                    Console.WriteLine("Stove is shutting down - too hot!");
                }
        }

        public float Dampness
        {
            get { return dampness; }
            set { dampness = value; }
        }
        public int Power
        {
            get { return power; }
            set { power = value; }
        }
    }


    class Exercise1
    {
        static void Main(string[] args)
        {
            Stove harvia = new Stove();
            harvia.Brand = "harvia";
            Console.WriteLine("Your stove brand is: " + harvia.Brand);
        }
    }
}
