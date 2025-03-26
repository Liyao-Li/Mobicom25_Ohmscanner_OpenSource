# SCRead
This code can be used to read the sensorCode and onChip values of the tag through the EPC protocol. 

## Hardware

A ThingMagic M6 reader 

##software
Visio studio 2020, Mercury API.

## How to run

* Use the official program to connect to the reader and select the fast-read option to perform a round of reading first
* Disconnect the official program from reader, set the IP address and file path
* OCRSS can be adjusted by adjusting the size of readpower

## The difference of two floder

***SCAndOnChipOPT*** is an automated version of ***SCAndOnChip***. The remaining operations follow the same procedure. The target value represents the desired OCRSS level to be achieved, and the program automatically adjusts the reader’s power to reach this target level.

