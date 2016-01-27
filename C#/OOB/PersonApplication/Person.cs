using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PersonApplication
{
    class Person
    {
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public string Address { get; set; }
        public int Age { get; set; }
        public string PhoneNumber { get; set; }

        public Person(string fn, string ln, string ad, int a, string pn)
        {
            FirstName = fn;
            LastName = ln;
            Address = ad;
            Age = a;
            PhoneNumber = pn;
        }

        public void personMethod()
        {
            Console.WriteLine("This method belongs to Person!");
        }

        public override string ToString()
        {
            return FirstName + " " + LastName + " " + Address + " " + Age + " " + PhoneNumber;
        }
    }
}
