using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Demo10_Hw03
{
    class Lotto
    {
        static Random rand = new Random();
        

        public string drawNumbers(int gameMode)
        {
            int maxValue = 0;
            int numbers = 0;
            string row = "";           

            if (gameMode == 0)
            {
                maxValue = 40;
                numbers = 7;
            }

            if (gameMode == 1)
            {
                maxValue = 49;
                numbers = 6;
            }

            if (gameMode == 2)
            {
                maxValue = 51;
                numbers = 7;
            }

            for (int i = 0; i < numbers; i++)
            {
                row += rand.Next(1, maxValue) + " ";
            }

            return row;
        }
    }
}
