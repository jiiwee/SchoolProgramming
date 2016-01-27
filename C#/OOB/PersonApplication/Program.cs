using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PersonApplication
{
    class Program
    {
        static void Main(string[] args)
        {
            Person somebody = new Person("Sami", "Unknown", "Road 2", 17, "040020020");
            somebody.personMethod();
            Console.WriteLine(somebody.ToString());
        }
    }
}
