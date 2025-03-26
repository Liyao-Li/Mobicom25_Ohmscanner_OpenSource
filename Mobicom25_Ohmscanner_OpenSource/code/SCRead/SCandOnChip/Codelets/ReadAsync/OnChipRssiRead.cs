using System;
using System.Collections.Generic;
using System.Text;
using System.Linq;
using ThingMagic;
using System.Diagnostics;
using System.IO;


namespace OnChipRssiRead
{
    class Program
    {
        static int totalReadCount = 20000;
        static int onChipReadCount = 0;
        static long startTime = Stopwatch.GetTimestamp();
        static long endTime = 0;
        static string filePath = "your file path";
        static void Main(string[] args)
        {
            Reader r = Reader.Create("tmr://your m6 ip");
            r.Connect();

            byte[] mask = { Convert.ToByte("1F", 16) };
            Gen2.Select select = new Gen2.Select(false, Gen2.Bank.USER, 0xD0, 8, mask);
            TagOp onChipOP = new Gen2.ReadData(Gen2.Bank.RESERVED, 0xC, 2);
            SimpleReadPlan onchipReadPlan = new SimpleReadPlan(new int[] { 1 }, TagProtocol.GEN2, select, onChipOP, true, 0);
                
            r.ParamSet("/reader/read/plan", onchipReadPlan);
            r.ParamSet("/reader/radio/readPower", 3150);

            r.TagRead += delegate (object sender, TagReadDataEventArgs e)
            {

                System.DateTime currentTime = new System.DateTime();
                currentTime = System.DateTime.Now;
                int hour = currentTime.Hour;
                int minute = currentTime.Minute;
                int second = currentTime.Second;
                int millisecond = currentTime.Millisecond;
                int black = 0;

                String currentTimeStr;

                if (hour < 10) 
                {
                    currentTimeStr = black.ToString();
                    currentTimeStr += hour.ToString();
                }
                else
                {
                    currentTimeStr = hour.ToString();
                }
                if (minute < 10) 
                {
                    currentTimeStr += black.ToString();
                }
                currentTimeStr += minute.ToString();
                if (second < 10) 
                {
                    currentTimeStr += black.ToString();
                }
                currentTimeStr += second.ToString();

                if (millisecond < 10) 
                {
                    currentTimeStr += black.ToString();
                    currentTimeStr += black.ToString();
                }
                else if (millisecond >= 10 && millisecond < 100)
                {
                    currentTimeStr += black.ToString();
                }
                currentTimeStr += millisecond.ToString();


                endTime = Stopwatch.GetTimestamp();
                long es = endTime - startTime;
                double microseconds = es * (1.0 / Stopwatch.Frequency);
                currentTimeStr += " " + microseconds.ToString().Remove(0, 2);
                string EPC = e.TagReadData.EpcString;
                string frequency = e.TagReadData.Frequency.ToString();
                string result = ByteFormat.ToHex(e.TagReadData.Data).Substring(2);
                if(result.Length > 0)
                {
                    string sensorCode = result.Substring(0, 4);
                    string onChipRssi = result.Substring(4);
                    FileStream file = new FileStream(filePath, mode: FileMode.Append);
                    StreamWriter sw = new StreamWriter(file);
                    sw.WriteLine("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t", e.TagReadData.Phase, e.TagReadData.Rssi, frequency, EPC, sensorCode, onChipReadCount++, onChipRssi, currentTimeStr);
                    sw.Close();

                    Console.WriteLine("EPC:{0}", EPC);
                    //Console.WriteLine("PhaseAngleInRadians:" + result.Tag.PhaseAngleInRadians);
                    Console.WriteLine(" Phase:{0}", e.TagReadData.Phase);
                    //Console.WriteLine(" PeakRssiInDbm: " + result.Tag.PeakRssiInDbm);
                    Console.WriteLine(" RSSI:{0}", e.TagReadData.Rssi);
                    Console.WriteLine("Frequency: {0}", e.TagReadData.Frequency);
                    //Console.WriteLine(" RfDopplerFrequency: " + result.Tag.RfDopplerFrequency);

                    //Console.WriteLine(" Frequency (MHZ): " + frequency);
                    Console.WriteLine(" Sensor Code:{0} ", sensorCode);
                    Console.WriteLine("OnChipRssi:{0} ", onChipRssi);
                    // Console.WriteLine(" EPC" +(count1++)+" " +currentTime);
                    Console.WriteLine(" Count:{0}", onChipReadCount);
                }


            };
            r.StartReading();
            while (onChipReadCount < totalReadCount) ;
        }
    }
}