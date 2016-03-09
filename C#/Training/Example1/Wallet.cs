using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Example1
{
    class Wallet
    {
        private float money = 0;
        float amount = 0;              

        public void AddMoney()
        {
            Console.Write("How much you want to add money? : ");
            amount = float.Parse(Console.ReadLine());
            money += amount;
        }

        public void TakeMoney()
        {
            Console.Write("How much you want to take money? : ");
            amount = float.Parse(Console.ReadLine());

            if (amount < money)
            {
                money -= amount;
            }
            else 
            {
                Console.WriteLine("Not enough money");
                Console.WriteLine("Try again");
            }
        }

        public void ShowMoney()
        {
            Console.Write("Cash now : ");
            Console.WriteLine(money);
        }
    }
}
