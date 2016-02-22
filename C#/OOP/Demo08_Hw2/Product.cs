using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Demo08_Hw2
{
    class Product
    {
        public string Name { get; set; }
        public float Price{ get; set; }

        public Product(string name, float price)
        {
            Name = name;
            Price = price;
        }

        public override string ToString()
        {
            return "- Product : " + Name + " " + Price + " e";
        }
    }
}
