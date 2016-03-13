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
                if (value < maxTemperature && value > minTemperature)
                {
                    temperature = value;                    
                }

                else if (value > maxTemperature)
                {
                    info = "Temperature is too high! Set to Max: " + maxTemperature;
                    temperature = maxTemperature;
                }

                else
                {
                    info = "Temperature is too low! Set to Min: " + minTemperature;
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
                if (value < maxHumidity && value > minHumidity)
                {                   
                    humidity = value;
                } 

                else if (value > maxHumidity)
                {
                    info = "Humidity is too high! Set to Max: " + maxHumidity;
                    humidity = maxHumidity;
                }

                else 
                {
                    info = "Humidity is too low! Set to Min: " + minHumidity;
                    humidity = minHumidity;
                }
            }
        }
    }
}
