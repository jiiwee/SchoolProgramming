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

namespace Demo10_Hw03
{
    /// <summary>
    /// An empty page that can be used on its own or navigated to within a Frame.
    /// </summary>
    public sealed partial class MainPage : Page
    {
        Lotto lotto = new Lotto();

        public MainPage()
        {
            this.InitializeComponent();
        }

        private void buttonDraw_Click(object sender, RoutedEventArgs e)
        {
            string value = comboBox.SelectedIndex.ToString();
            int draws = int.Parse(textBoxDraw.Text);
            for (int i = 1; i < draws + 1; i++)
            {
                textBlockRandomNum.Text += "Row " + i + ": " + lotto.drawNumbers(comboBox.SelectedIndex) + "\n";
            }
        }

        private void buttonClear_Click(object sender, RoutedEventArgs e)
        {
            textBlockRandomNum.Text = "";
        }
    }
}
