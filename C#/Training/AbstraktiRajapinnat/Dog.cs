﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AbstraktiRajapinnat
{
    class Dog : IAnimal
    {
        public string Name { get; set; }

        public string Talk()
        {
            return "Wuw!";
        }
    }
}
