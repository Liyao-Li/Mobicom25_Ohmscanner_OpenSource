using System;
using System.Collections.Generic;
using System.Text;
using System.Linq;
using ThingMagic;
using System.Diagnostics;
using System.IO;


namespace ReadAsync
{
    class Program
    {
        static int onChipReadCount = 0;
        static long startTime = Stopwatch.GetTimestamp();
        static long endTime = 0;
        static string filePath = "your file path";
        static int tartet = 13; 
        static int readPower = 3150;
        static int lowPower = 1537;
        static int highPower = 3150;
        static SimpleReadPlan onchipReadPlan;
        static void Main(string[] args)
        {
            Reader r = Reader.Create("tmr://your m6 ip");
            r.Connect();

            byte[] mask = { Convert.ToByte("1F", 16) };
            Gen2.Select select = new Gen2.Select(false, Gen2.Bank.USER, 0xD0, 8, mask);
            TagOp onChipOP = new Gen2.ReadData(Gen2.Bank.RESERVED, 0xC, 2);
            onchipReadPlan = new SimpleReadPlan(new int[] { 1 }, TagProtocol.GEN2, select, onChipOP, true, 0);

            r.ParamSet("/reader/read/plan", onchipReadPlan);
            r.ParamSet("/reader/radio/readPower", readPower);

            optOnChipRssi(r, tartet);

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
                //Console.WriteLine(" RfDopplerFrequency: " + result.Tag.RfDopplerFrequency);

                //Console.WriteLine(" Frequency (MHZ): " + frequency);
                Console.WriteLine(" Sensor Code:{0} ", sensorCode);
                Console.WriteLine(" OnChipRssi:{0} ", onChipRssi);
                // Console.WriteLine(" EPC" +(count1++)+" " +currentTime);
                Console.WriteLine(" Count:{0}", onChipReadCount);
                }

            };
            r.StartReading();
            while (onChipReadCount < 400) ;
        }

        static int increaseRadio(Reader r)
        {
            int temp = lowPower;
            lowPower = readPower;
            readPower = (lowPower + highPower) / 2;
            Console.WriteLine("highPower: " + highPower + "     lowPower: " + lowPower + "     readPower: "+readPower);
            Console.WriteLine("add readPower to" + readPower/100 + "dB");
            //r.Destroy();
            //r = Reader.Create("tmr://169.254.247.84");
            //r.Connect();
            //r.ParamSet("/reader/read/plan", onchipReadPlan);
            r.ParamSet("/reader/radio/readPower", readPower);
            return readPower;
        }
        static int reduceRadio(Reader r)
        {
            int temp = highPower;
            highPower = readPower;
            readPower = (highPower + lowPower) / 2;
            Console.WriteLine("highPower: " + highPower + "     lowPower: " + lowPower + "     readPower: " + readPower);
            Console.WriteLine("sub readPower to" + readPower / 100 + "dB");
            //r.Destroy();
            //r = Reader.Create("tmr://169.254.247.84");
            //r.Connect();
            //r.ParamSet("/reader/read/plan", onchipReadPlan);
            r.ParamSet("/reader/radio/readPower", readPower);
            return readPower;
        }
        static double readData(Reader r)
        {
            int onChipRssiSum = 0;
            int notZeroDataLength = 0;
            int readTimes = 0;
            DateTime startTime = DateTime.Now;
            r.TagRead += delegate (object sender, TagReadDataEventArgs e)
            {
                if(0 < e.TagReadData.Data.Length)
                {
                    int onChipRssi = int.Parse(ByteFormat.ToHex(e.TagReadData.Data).Substring(6), System.Globalization.NumberStyles.HexNumber);
                    if (onChipRssi != 0)
                    {
                        Console.WriteLine("Onchip: " + onChipRssi);
                        onChipRssiSum += onChipRssi;
                        notZeroDataLength++;
                    }
                    readTimes++;
                }
            };
            r.StartReading();
            DateTime nextOutputTime = DateTime.Now.AddSeconds(2);
            while (readTimes < 10 && notZeroDataLength <= 5 && DateTime.Now - startTime < TimeSpan.FromSeconds(10))
            {
                if (DateTime.Now >= nextOutputTime)
                {
                    Console.WriteLine("The remaining time for Onchip to read data is adjusted to " + (10 - (DateTime.Now - startTime).TotalSeconds));

                }
                nextOutputTime = DateTime.Now.AddSeconds(2);
            }
            r.StopReading();
            Console.WriteLine("finish read");
            if(notZeroDataLength == 0)
            {
                return -1;
            }
            return onChipRssiSum / notZeroDataLength;

        }
        static void optOnChipRssi(Reader r, int target)
        {
            int adjustTimes = 0;
            readPower = reduceRadio(r);
            while (true)
            {
                adjustTimes++;
                double data = readData(r);

                if (Math.Abs(data - target) < 1 || adjustTimes == 10)
                {
                    Console.WriteLine("Adjustment completed");
                    break;
                }

                if (data == -1 || data <=¡¡target - 1)
                {
                    increaseRadio(r);
                }
                else if (data >= target + 1)
                {
                    reduceRadio(r);
                }

            }
        }
    }
}