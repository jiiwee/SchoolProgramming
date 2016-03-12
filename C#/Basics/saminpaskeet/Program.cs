using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace saminpaskeet
{
    class Program
    {
        static void Main(string[] args)
        {
            List<char> abc = new List<char>();
            for(int i = 97; i < 124; i++)
            {
                abc.Add((char)i);
            }
            List<char> cba = new List<char>();
            for (int i = 123; i > 96; i++)
            {
                cba.Add((char)i);
            }
            Console.WriteLine(abc);
        }
    }
}
