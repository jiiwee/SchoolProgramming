using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Example2
{
    class Deck
    {
        private List<Card> cards;

        public Deck()
        {
            cards = new List<Card>();

            foreach(Example2.Values v in Enum.GetValues(typeof(Values)))
            {
                foreach(Example2.Suits s in Enum.GetValues(typeof(Suits)))
                {
                    AddCard(new Card(s, v));
                }
            }
        }

        public void AddCard(Card c)
        {
            cards.Add(c);
        }

        public void Print()
        {
            foreach(Card c in cards)
            {
                Console.WriteLine(c);
            }
        }
    }
}
