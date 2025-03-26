# Gen2 UHF RFID Reader

## Notice

This code is forked form https://github.com/nkargas/Gen2-UHF-RFID-Reader

### Implemented GNU Radio Blocks:

- Gate : Responsible for reader command detection.  
- Tag decoder : Responsible for frame synchronization, channel estimation, symbol period estimation and detection.  
- Reader : Create/send reader commands.

## Requirements

- gcc7.5,g++7.5

- cmake >= 2.6

- uhd

- gnuradio (must be 3.7)

- swig

  ```shell
  sudo apt intstall gcc
  sudo apt intstall g++
  sudo apt intstall cmake
  sudo add-apt-repository ppa:ettusresearch/uhd
  sudo apt-get update
  sudo apt-get install libuhd-dev libuhd4.1.0 uhd-host
  sudo apt install gnuradio
  sudo apt install swig
  ```

## Installation

```shell
cd rfid-usrp-outband\gr-rfid
mkdir build  
cd build/  
cmake ../ (logging and swig should be enabled)  
make && sudo make install  
sudo ldconfig
```

## Configuration

- set ip of outband and inband usrp;
- You should first adjust decim, ampl, rx_gian and gx_gian to ensure that the tag can be read correctly;
- Adjust the frequency of outband signal by changing outband_Start_freq and outband_End_freq

## How to run

```shell
cd rfid-usrp-outband/gr-rfid/apps/    
sudo GR_SCHEDULER=STS nice -n -20 python ./reader.py
```

## Hardware

- usrp N210 and usrp 2922
- CDA-2990
- LNA
- two band-pass filter

![Outband Device Connection Diagram](../../../pictures/outband_device_connect.jpg)

*This picture just shows you how to connect each device, so we did not connect the transmit and receive antennas.*
