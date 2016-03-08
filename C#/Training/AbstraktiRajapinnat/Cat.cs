using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AbstraktiRajapinnat
{
    class Cat : IAnimal
    {
        public string Name { get; set; }

        public string Talk()
        {
            return "Miau!";
        }
    }
}
