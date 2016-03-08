using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PerintäMonimuotoisuus
{
    class Bike : Vehicle
    {
        public bool GearWheels { get; set; }
        public string GearManifacture{ get; set; }

        public Bike()
        {

        }

        public Bike(string manifacture, string model, int year, string color, bool gearwheels, string gearmanifacture)
               : base(manifacture, model, year, color)
        {
            GearWheels = gearwheels;
            GearManifacture = gearmanifacture;
        }

        public override void Thing()
        {
            Console.WriteLine("Bike object: I am a bike");
        }

        public override string ToString()
        {
            return base.ToString() + "\n-Gear wheels : " + GearWheels + "\n-Gear Manifacture : " + GearManifacture + "\n";
        }
    }
}
