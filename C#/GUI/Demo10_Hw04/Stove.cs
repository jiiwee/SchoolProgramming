using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Demo10_Hw04
{
    class Stove
    {
        private const float maxTemperature = 120;
        private const float minTemperature = 0;
        private const float maxHumidity = 100;
        private const float minHumidity = 0;
        private float temperature;
        private float humidity;
        public string info = "";

        public float Temperature
        {
            get
            {
                return temperature;
            }

            set
            {
                if (value < maxTemperature) { temperature = value; }
                else
                {
                    info = "Temperature is too high!";
                    temperature = maxTemperature;
                }

                if (value > minTemperature) { temperature = value; }
                else
                {
                    info = "Temperature is too low!";
                    temperature = minTemperature;
                }
            }
        }

        public float Humidity
        {
            get
            {
                return humidity;
            }

            set
            {
                if (value < maxHumidity) { humidity = value; } 
                else
                {
                    info = "Humidity is too high!";
                    humidity = maxHumidity;
                }

                if (value > minHumidity) { humidity = value; }
                else
                {
                    info = "Humidity is too low!";
                    humidity = minHumidity;
                }
            }
        }
    }
}
