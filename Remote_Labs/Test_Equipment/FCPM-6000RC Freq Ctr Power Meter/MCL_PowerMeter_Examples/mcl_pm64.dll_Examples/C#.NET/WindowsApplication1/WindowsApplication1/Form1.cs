using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace WindowsApplication1
{
    public partial class Form1 : Form
    {
        bool StopRun;
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // mcl_pm64.dll should be loaded as a reference file to the project project
            double ReadResult;
            string FreqSTR = "";
            mcl_pm64.usb_pm pm1 = new mcl_pm64.usb_pm();
            short Status = 0;
            string pm_SN = ""; //if more then 1 sensor connected to the computer than the Serial Number of the sensor should provide
            Status = pm1.Open_Sensor(ref(pm_SN));
            StopRun = false;
            while (!StopRun)
            {
            FreqSTR = textBox1.Text;
            if (FreqSTR == "") FreqSTR = "10";   
            pm1.Freq = Convert.ToDouble(FreqSTR);      // Set the Frequency cal factor in MHz
            ReadResult = pm1.ReadPower(); // read the power in dbm
            label3.Text = string.Format("{0:0.00}",  ReadResult)  ; 
            Application.DoEvents();
            }
            pm1.Close_Sensor();  
        }

        private void button2_Click(object sender, EventArgs e)
        {
            StopRun = true;
        }

        
    }
}