using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices.WindowsRuntime;
using Windows.Foundation;
using Windows.Foundation.Collections;
using Windows.UI.Xaml;
using Windows.UI.Xaml.Controls;
using Windows.UI.Xaml.Controls.Primitives;
using Windows.UI.Xaml.Data;
using Windows.UI.Xaml.Input;
using Windows.UI.Xaml.Media;
using Windows.UI.Xaml.Navigation;

// The Blank Page item template is documented at http://go.microsoft.com/fwlink/?LinkId=402352&clcid=0x409

namespace Demo10_Hw04
{
    /// <summary>
    /// An empty page that can be used on its own or navigated to within a Frame.
    /// </summary>
    public sealed partial class MainPage : Page
    {
        string input;
        Stove stove = new Stove();

        public MainPage()
        {
            this.InitializeComponent();            
        }

        private void button0_Click(object sender, RoutedEventArgs e)
        {
            string buttonString = (((Button)sender).Content).ToString();
            input = textBoxInput.Text;
            if (input == "0") textBoxInput.Text = buttonString;            
            else textBoxInput.Text += buttonString;
        }

        private void buttonDel_Click(object sender, RoutedEventArgs e)
        {
            string newLine = textBoxInput.Text.Substring(0, textBoxInput.Text.Length - 1);
            if (newLine == "") newLine = "0";
            textBoxInput.Text = newLine;            
        }

        private void buttonOK_Click(object sender, RoutedEventArgs e)
        {     
           if ((bool)radioButtonTemp.IsChecked) stove.Temperature = float.Parse(textBoxInput.Text);
           else if ((bool)radioButtonHum.IsChecked) stove.Humidity = float.Parse(textBoxInput.Text);
           textBoxTemp.Text = "" + stove.Temperature;
           textBoxHum.Text = "" + stove.Humidity;
           textBlockInfo.Text = stove.info;
           textBoxInput.Text = "0";
        }
    }
}
