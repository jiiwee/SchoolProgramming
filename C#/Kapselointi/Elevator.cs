﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Kapselointi
{
    class Elevator
    {
        private const int minFloor = 1;
        private const int maxFloor = 9;        

        private int floor = 1;
        public int Floor
        {
            get
            {
                return floor;
            }
            set
            {
                if (value < minFloor)
                {
                    Console.WriteLine("Floor is too small");
                }
                else if (value > maxFloor)
                {
                    Console.WriteLine("Floor is too high");
                }                   
                else
                {
                    floor = value;
                }
            
            }
        }          
    }
}
