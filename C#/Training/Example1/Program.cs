using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Example1
{
    class Program
    {
        static void Main(string[] args)
        {
            Wallet wallet = new Wallet();
            bool running = true;

            Console.WriteLine("Menu");
            Console.WriteLine("1. Add money");
            Console.WriteLine("2. Take money");
            Console.WriteLine("3. Show money");
            Console.WriteLine("4. Throw wallet away\n");
            
            while (running)
            {
                int choice = int.Parse(Console.ReadLine());
                switch(choice)
                {
                    case 1:
                        wallet.AddMoney();
                        break;                        
                    case 2:
                        wallet.TakeMoney();                        
                        break;
                    case 3:
                        wallet.ShowMoney();
                        break;
                    case 4:
                        running = false;
                        break;                      
                }
            } 
        }
    }
}
