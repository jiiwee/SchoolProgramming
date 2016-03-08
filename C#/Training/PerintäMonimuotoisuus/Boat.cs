using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PerintäMonimuotoisuus
{
    class Boat : Vehicle
    {
        public string Type { get; set; }
        public int SeatCount { get; set; }

        public Boat()
        {

        }

        public Boat(string manifacture, string model, int year, string color, string type, int seatcount)
           : base(manifacture, model, year, color)
        {
            Type = type;
            SeatCount = seatcount;
        }    
        
        public override void Thing()
        {
            Console.WriteLine("Boat object: I am a boat");
        }

        public override string ToString()
        {
            return base.ToString() + "\n-Type : " + Type + "\n-Seat count : " + SeatCount + "\n";
        }
    }
}
