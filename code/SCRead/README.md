# SCRead

This code can be used to read the sensorCode and onChip values of the tag through the EPC protocol. It is only valid for Magnus s3.Other tags cannot be read normally because they do not have SC and OCRSS flags in user memory.

## Hardware

A Impinj reader which support Mercury API.

## How to run

* Use the official program to connect to the M6 and select the fast-read option to perform a round of reading first
* Disconnect the official program from M6, set the IP address and file path
* OCRSS can be adjusted by adjusting the size of readpower

## The difference of two floder

***SCAndOnChipOPT*** is an automated version of SCAndOnChip. The rest of the operations are the same. Target is the target value that OCRSS needs to adjust to, so you dont need to change read power by yourself.

