# simulate

## Platform

ANSYS Elcectronics Desktop 2018.2
We also tested it on ANSYS Elcectronics Desktop 2023.

## Description

Our core goal is to achieve impedance variation by influencing the antenna. In this article, we present three different methods for affecting antenna impedance.

* button.adet: OhmScan-Based Keystub-Equivalent Button Board. This design changes the antenna’s impedance by altering its closed-loop configuration.
* capAntenna.adet: Used for Liquid Concentration Sensing, Pressure Sensing, and Temperature Sensing. In this design, the antenna’s impedance is modified by connecting external impedance elements.
* roateAntenna.adet: Used for UV Light Sensing. The impedance of the antenna is changed by physically altering its shape.

By running impedance.m, you can intuitively observe the impact of the aforementioned factors on antenna impedance. In each .adet project, the source sub-project represents the initial (baseline) impedance state. The remaining sub-projects demonstrate how various factors influence the initial impedance, and are used to adjust the antenna's impedance accordingly in the experiments.
