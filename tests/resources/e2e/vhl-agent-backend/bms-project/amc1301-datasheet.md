## AMC1301 Precision, ±250-mV Input, Reinforced Isolated Amplifier

## 1 Features

- • ±250-mV input voltage range optimized for current  measurements using shunt resistors - • Fixed gain: 8.2 V/V - • Low DC errors: - - Offset error: ±0.2 mV (max) - - Offset drift: ±3 µV/°C (max) - - Gain error: ±0.3% (max) - - Gain drift: ±50 ppm/°C (max) - - Nonlinearity: 0.03% (max) - • 3.3-V operation on high-side and low-side - • System-level diagnostic features - • Safety-related certifications: - - 7070-V PK reinforced isolation per DIN EN IEC  60747-17 (VDE 0884-17) - - 5000-V RMS isolation for 1 minute per UL1577 - • Fully specified over the extended industrial  temperature range: -40°C to +125°C

## 2 Applications

- • Shunt-resistor-based current sensing in: - - Motor drives - - Frequency inverters - - Uninterruptible power supplies

## 3 Description

The AMC1301 is a precision, isolated amplifier with an output separated from the input circuitry by an isolation barrier that is highly resistant to magnetic interference. This barrier is certified to provide reinforced isolation of up to 7070 V PEAK according to the DIN EN IEC 60747-17 (VDE 0884-17) and UL1577 standards, and supports a working voltage up to 1 kV RMS.

The isolation barrier separates parts of the system that operate on different common-mode voltage levels and protects the low-side from voltage levels that can cause electrical damage and are potentially harmful to an operator.

The input of the AMC1301 is optimized for direct connection to shunt resistors or other low voltage-level signal sources. The excellent DC accuracy and low temperature drift supports accurate current control in onboard chargers (OBC), DC/DC converters, frequency inverters, or other highvoltage applications. The integrated common-mode overvoltage and missing high-side supply voltage detection features of the AMC1301 simplify systemlevel design and diagnostics.

The AMC1301 is fully specified over the extended industrial temperature range of -40°C to +125°C and is available in a wide-body 8-pin SOIC (DWV) package. The AMC1301S is specified over the temperature range of -55°C to +125°C. **Package Information**

# PART NUMBER **PACKAGE** (1) **BODY SIZE (NOM)** AMC1301 DWV (SOIC, 8) 5.85 mm \times 7.50 mm

(1) For all available packages, see the orderable addendum at the end of the data sheet.

# VDD2 Low-side supply (3.3 V or 5 V)

# AMC1301 Reinforced Isolation

# OUTP

# OUTN

# GND2 GND1

# INP

# INN

# VDD1 ADC \pm2.05 V CMout

# RSHUNT

# I High-side supply (3.3 V or 5 V) +250 mV 0 V -250 mV **Simplified Schematic**

# AMC1301 SBAS667G - APRIL 2016 - REVISED APRIL 2023

An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications, intellectual property matters and other important disclaimers. PRODUCTION DATA.

## Table of Contents

**1 Features**............................................................................ 1 **2 Applications**..................................................................... 1 **3 Description**....................................................................... 1 **4 Revision History**.............................................................. 2 **5 Pin Configuration and Functions**................................... 4 **6 Specifications**.................................................................. 5

6.1 Absolute Maximum Ratings........................................ 5 6.2 ESD Ratings............................................................... 5 6.3 Recommended Operating Conditions......................... 5 6.4 Thermal Information.................................................... 6 6.5 Power Ratings............................................................. 6 6.6 Insulation Specifications............................................. 7 6.7 Safety-Related Certifications...................................... 8 6.8 Safety Limiting Values................................................. 8 6.9 Electrical Characteristics............................................. 9 6.10 Switching Characteristics........................................ 10 6.11 Timing Diagram....................................................... 10 6.12 Insulation Characteristics Curves............................ 11 6.13 Typical Characteristics............................................ 12 **7 Detailed Description**...................................................... 19

7.1 Overview................................................................... 19 7.2 Functional Block Diagram......................................... 19 7.3 Feature Description................................................... 19 7.4 Device Functional Modes.......................................... 21 **8 Application and Implementation**.................................. 22

8.1 Application Information............................................. 22 8.2 Typical Application.................................................... 22 8.3 Best Design Practices............................................... 25 8.4 Power Supply Recommendations............................. 25 8.5 Layout....................................................................... 26 **9 Device and Documentation Support**............................ 27

9.1 Documentation Support............................................ 27 9.2 Receiving Notification of Documentation Updates.... 27 9.3 Support Resources................................................... 27 9.4 Trademarks............................................................... 27 9.5 Electrostatic Discharge Caution................................ 27 9.6 Glossary.................................................................... 27 **10 Mechanical, Packaging, and Orderable **

**Information**.................................................................... 27

**4 Revision History** NOTE: Page numbers for previous revisions may differ from page numbers in the current version.

**Changes from March 14, 2023 to April 24, 2023 (from Revision F (April 2020) to Revision G ** **(April 2023))** **Page** - • Changed document title...................................................................................................................................... 1 - • Changed *Features* section: Changed, deleted, and reorganized bullets............................................................ 1 - • Changed isolation standard from DIN VDE V 0884-11 (VDE V 0884-10) to DIN EN IEC 60747-17 (VDE  0884-17) and updated the *Insulation Specifications* and *Safety-Related Certifications* tables accordingly....... 1 - • Deleted last bullet from *Applications* section...................................................................................................... 1 - • Changed *Description* section to include common-mode decoupling capacitors as a known best practice........ 1 - • Changed pin names VINP to INP, VINN to INN, VOUTP to OUTP, and VOUTN to OUTN throughout  document............................................................................................................................................................ 4 - • Changed *Description* column and added footnotes to *Pin Functions* table........................................................ 4 - • Changed CDM ESD standard from JESD22-C101 to JDEC JS-002................................................................. 5 - • Changed PD from 81.4 mW to 99 mW............................................................................................................... 6 - • Changed PD1 (VDD1 = 3.3 V) from  24.85 mW to 31 mW................................................................................. 6 - • Changed PD1 (VDD1 = 5.5 V) from  45.65 mW to 54 mW................................................................................. 6 - • Changed PD2 (VDD2 = 3.3 V) from 20.16 mW to 26 mW.................................................................................. 6 - • Changed PD2 (VDD2 = 5.5 V) from 35.75 mW to 45 mW.................................................................................. 6 - • Changed DTI from ≥0.027 mm to ≥0.021 mm in *Insulation Specifications* table................................................ 7 - • Changed IDD1 (3.0 V ≤ VDD1 ≤ 3.6 V) from 5.0 mA (typ) / 6.9 mA (max) to 6.3 mA (typ) / 8.5 mA (max)........ 9 - • Changed IDD1 (4.5 V ≤ VDD1 ≤ 5.5 V) from 5.9 mA (typ) / 8.3 mA (max) to 7.2 mA (typ) / 9.8 mA (max)........ 9 - • Changed IDD2 (3.0 V ≤ VDD2 ≤ 3.6 V) from 4.4 mA (typ) / 5.6 mA (max) to 5.3 mA (typ) / 7.2 mA (max)........ 9 - • Changed IDD2 (4.5 V ≤ VDD2 ≤ 5.5 V) from 4.8 mA (typ) / 6.5 mA (max) to 5.9 mA (typ) / 8.1 mA (max)........ 9 - • Changed *Timing Diagram* section.................................................................................................................... 10 - • Changed *Overview* section............................................................................................................................... 19 - • Changed *Functional Block Diagram* image...................................................................................................... 19 - • Changed the *Analog Input* section.................................................................................................................... 19 - • Added the *Isolation Channel Signal Transmission* section............................................................................... 20 - • Added *Analog Output* section, deleted *Fail-Safe Output* section...................................................................... 21 - • Changed *Device Functional Modes* section..................................................................................................... 21

# AMC1301

SBAS667G - APRIL 2016 - REVISED APRIL 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated Product Folder Links: *AMC1301*

- • Changed *Application Information* section......................................................................................................... 22 - • Changed *Typical Application* section................................................................................................................ 22 - • Changed *Best Design Practices* section........................................................................................................... 25 - • Changed *Power Supply Recommendations* section......................................................................................... 25 - • Changed the *Recommended Layout of the AMC1301* figure........................................................................... 26 - • Added a link to the *Isolated Voltage-Measurement Circuit* in the *Related Documentation* section.................. 27

**Changes from Revision E (March 2018) to Revision F (April 2020)** **Page** - • Changed safety-related certifications details as per ISO standard.................................................................... 1 - • Changed *IEC 60950-1 and IEC60065* to *IEC 62368-1*...................................................................................... 1 - • Changed *VDE V 0884-10* to *VDE V 0884-11* in *Description* section.................................................................. 1 - • Changed T A parameter from *specified* to *operating* in *Device Comparison Table*............................................. 4 - • Changed CLR and CPG values from 9 mm to 8.5 mm....................................................................................... 7 - • Changed *Insulation Specifications* table per ISO standard................................................................................ 7 - • Changed *Safety-Related Certifications* table per ISO standard......................................................................... 8 - • Changed *Safety Limiting Values* description as per ISO standard..................................................................... 8 - • Changed *Rise and Fall Time Test Waveforms* figure....................................................................................... 10 - • Changed *Delay Time Test Waveforms* figure................................................................................................... 10 - • Changed *Functional Block Diagram* figure....................................................................................................... 19 **<https://www.ti.com**>

# AMC1301 SBAS667G - APRIL 2016 - REVISED APRIL 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* Product Folder Links: *AMC1301*

## Device Comparison Table

| PARAMETER | AMC1301S | AMC1301 |
|:--- |:--- |:--- |
| Operating ambient temperature, TA | -55°C to +125°C | -40°C to +125°C |
| Input offset drift, TCVOS | ±4 µV/°C (max) | ±3 µV/°C (max) |
| Gain error drift, TCEG | ±60 ppm/°C (max) | ±50 ppm/°C (max) |

Operating ambient temperature, T A -55°C to +125°C -40°C to +125°C

Input offset drift, TCV OS \pm4 µV/°C (max) \pm3 µV/°C (max)

Gain error drift, TCE G \pm60 ppm/°C (max) \pm50 ppm/°C (max)

## 5 Pin Configuration and Functions

# VDD1

# INP

# INN

# GND1

# VDD2

# OUTP

# GND2

# OUTN Not to scale

## Figure 5-1. DWV Package, 8-Pin SOIC (Top View)

## Table 5-1. Pin Functions

# PIN

# TYPE **DESCRIPTION** **NO.** **NAME**

VDD1 High-side power High-side power supply. (1)

INP Analog input Noninverting analog input. Either INP or INN must have a DC current path to GND1 to define the common-mode input voltage. (2)

INN Analog input Inverting analog input. Either INP or INN must have a DC current path to GND1 to define the common-mode input voltage. (2)

| GND1 | High-side ground | High-side analog ground. |
|:--- |:--- |:--- |
| GND2 | Low-side ground | Low-side analog ground. |
| OUTN | Analog output | Inverting analog output. |
| OUTP | Analog output | Noninverting analog output. |
| VDD2 | Low-side power | Low-side power supply.(1) | GND2 Low-side ground Low-side analog ground. OUTN Analog output Inverting analog output.

OUTP Analog output Noninverting analog output.

VDD2 Low-side power Low-side power supply. (1)

(1) See the *Power Supply Recommendations* section for power-supply decoupling recommendations. (2) See the *Layout* section for details.

# AMC1301

SBAS667G - APRIL 2016 - REVISED APRIL 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated Product Folder Links: *AMC1301*

## 6 Specifications **6.1 Absolute Maximum Ratings** see (1)

# MIN **MAX** **UNIT** Power-supply voltage High-side VDD1 to GND1 -0.3 V Low-side VDD2 to GND2 -0.3

Analog input voltage INP, INN GND1 - 6 VDD1 + 0.5 V

Input current Continuous, any pin except power-supply pins mA Temperature Junction, T J °C Storage, T stg

(1) Operation outside the *Absolute Maximum Ratings* may cause permanent device damage. *Absolute Maximum Ratings* do not imply functional operation of the device at these or any other conditions beyond those listed under *Recommended Operating Conditions*. If used outside the Recommended Operating Conditions but within the Absolute Maximum Ratings, the device may not be fully functional, and this may affect device reliability, functionality, performance, and shorten the device lifetime

## 6.2 ESD Ratings

| VALUE | UNIT |
|:--- |:--- |
| V(ESD) | Electrostatic discharge |
| Human-body model (HBM), per ANSI/ESDA/JEDEC JS-001(1) | ±2000 | V (ESD) Electrostatic discharge

Human-body model (HBM), per ANSI/ESDA/JEDEC JS-001 (1) \pm2000

V Charged-device model (CDM), per ANSI/ESDA/JEDEC JS-002 ((2)) \pm1000

(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process. (2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.

## 6.3 Recommended Operating Conditions

over operating ambient temperature range (unless otherwise noted)

# MIN **NOM** **MAX** **UNIT**

# POWER SUPPLY High-side power supply VDD1 to GND1 5.5 V Low-side power supply VDD2 to GND2 3.3 5.5 V

# ANALOG INPUT

| VClipping | Differential input voltage before clipping output | VIN = VINP - VINN | ±302.7 | mV |
|:--- |:--- |:--- |:--- |:--- |
| VFSR | Specified linear differential full-scale voltage | VIN = VINP - VINN | -250 | mV |
| Absolute common-mode input voltage(1) | (VINP + VINN) / 2 to GND1 | -2 | VDD1 | V |
| VCM | Operating common-mode input voltage | (VINP + VINN) / 2 to GND1 | -0.16               VDD1 - 2.1 | V |

V FSR Specified linear differential full-scale voltage V IN = V INP - V INN mV

Absolute common-mode input voltage (1) (V INP + V INN ) / 2 to GND1 VDD1 V

V CM Operating common-mode input voltage (V INP + V INN ) / 2 to GND1 -0.16               VDD1 - 2.1 V

# TEMPERATURE RANGE T A Specified ambient temperature

# AMC1301

# °C AMC1301S

(1) Steady-state voltage supported by the device in case of a system failure. See specified common-mode input voltage V CM for normal operation. Observe analog input voltage range as specified in *Absolute Maximum Ratings* table. **<https://www.ti.com**>

# AMC1301 SBAS667G - APRIL 2016 - REVISED APRIL 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* Product Folder Links: *AMC1301*

## 6.4 Thermal Information

# THERMAL METRIC (1) **DWV (SOIC)**

# UNIT **8 PINS**

| RθJA | Junction-to-ambient thermal resistance | 110.1 | °C/W |
|:--- |:--- | ---: |:--- |
| RθJC(top) | Junction-to-case (top) thermal resistance | 51.7 | °C/W |
| RθJB | Junction-to-board thermal resistance | 66.4 | °C/W |
| ΨJT | Junction-to-top characterization parameter | 16.0 | °C/W |
| ΨJB | Junction-to-board characterization parameter | 64.5 | °C/W |
| RθJC(bot) | Junction-to-case (bottom) thermal resistance | N/A | °C/W |

R\thetaJC(top) Junction-to-case (top) thermal resistance 51.7 °C/W

R\thetaJB Junction-to-board thermal resistance 66.4 °C/W

\PsiJT Junction-to-top characterization parameter 16.0 °C/W

\PsiJB Junction-to-board characterization parameter 64.5 °C/W

R\thetaJC(bot) Junction-to-case (bottom) thermal resistance N/A °C/W

(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application report.

## 6.5 Power Ratings

# PARAMETER **TEST CONDITIONS** **VALUE** **UNIT**

P D Maximum power dissipation (both sides) $$ VDD1 = VDD2 = 5.5 V $$ mW P D1 Maximum power dissipation (high-side)

# VDD1 = 3.6 V

# mW $$ VDD1 = 5.5 V $$ P D2 Maximum power dissipation (low-side)

# VDD2 = 3.6 V

# mW $$ VDD2 = 5.5 V $$

# AMC1301

SBAS667G - APRIL 2016 - REVISED APRIL 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated Product Folder Links: *AMC1301*

## 6.6 Insulation Specifications

over operating ambient temperature range (unless otherwise noted)

# PARAMETER **TEST CONDITIONS** **VALUE** **UNIT**

# GENERAL

CLR External clearance (1) Shortest pin-to-pin distance through air $$ \geq 8.5 $$ mm

CPG External creepage (1) Shortest pin-to-pin distance across the package surface $$ \geq 8.5 $$ mm

DTI Distance through insulation Minimum internal gap (internal clearance) of the double insulation $$ \geq 0.021 $$ mm

CTI Comparative tracking index DIN EN 60112 (VDE 0303-11); IEC 60112 $$ \geq 600 $$ V Material group According to IEC 60664-1 I Overvoltage category per IEC 60664-1 Rated mains voltage ≤ 600 V RMS I-IV Rated mains voltage ≤ 1000 V RMS I-III

# DIN EN IEC 60747-17 (VDE 0884-17) (2)

V IORM Maximum repetitive peak isolation voltage At AC voltage V PK

V IOWM Maximum-rated isolation working voltage At AC voltage (sine wave) V RMS At DC voltage V DC V IOTM Maximum transient isolation voltage

V TEST = V IOTM, t = 60 s (qualification test), VTEST = 1.2 × VIOTM, t = 1 s (100% production test) V PK

V IMP Maximum impulse voltage (2) Tested in air, 1.2/50-µs waveform per IEC 62368-1 V PK V IOSM Maximum surge isolation voltage (3)

Tested in oil (qualification test), 1.2/50-µs waveform per IEC 62368-1 V PK q pd Apparent charge ((5))

Method a, after input/output safety test subgroups 2 and 3, Vpd(ini) = VIOTM, tini = 60 s, Vpd(m) = 1.2 \times VIORM, tm = 10 s $$ \leq 5 $$ pC

| Method a, after environmental tests subgroup 1, | Vpd(ini) = VIOTM, tini = 60 s, Vpd(m) = 1.6 × VIORM, tm = 10 s | ≤ 5 |
|:--- |:--- |:--- |
| Method b1, at preconditioning (type test) and routine test, | Vpd(ini) = 1.2 x VIOTM, tini = 1 s, Vpd(m) = 1.875 × VIORM, tm = 1 s | ≤ 5 |
| Method b2, at routine test (100% production)((7)), | Vpd(ini) = Vpd(m) = 1.2 x VIOTM, tini =  tm = 1 s | ≤ 5 |

Method b1, at preconditioning (type test) and routine test, Vpd(ini) = 1.2 x VIOTM, tini = 1 s, Vpd(m) = 1.875 \times VIORM, tm = 1 s $$ \leq 5 $$

Method b2, at routine test (100% production) ((7)), Vpd(ini) = Vpd(m) = 1.2 x VIOTM, tini =  tm = 1 s $$ \leq 5 $$

C IO Barrier capacitance, input to output (5) VIO = 0.5 VPP at 1 MHz ~1.2 pF

R IO Insulation resistance, input to output (5)

# VIO = 500 V at TA = 25°C > 1012

\Omega $$ VIO = 500 V at 100°C \leq TA \leq 125°C $$ > 1011

# VIO = 500 V at TS = 150°C > 109 Pollution degree Climatic category

# AMC1301 40/125/21

# AMC1301S 55/125/21

# UL1577

V ISO Withstand isolation voltage V TEST = V ISO, t = 60 s (qualification test), VTEST = 1.2 × VISO, t = 1 s (100% production test) V RMS

(1) Apply creepage and clearance requirements according to the specific equipment isolation standards of an application. Care must be taken to maintain the creepage and clearance distance of a board design to ensure that the mounting pads of the isolator on the printed circuit board (PCB) do not reduce this distance. Creepage and clearance on a PCB become equal in certain cases. Techniques such as inserting grooves, ribs, or both on a PCB are used to help increase these specifications. (2) Testing is carried out in air to determine the surge immunity of the package. (3) Testing is carried in oil to determine the intrinsic surge immunity of the isolation barrier. (4) Apparent charge is electrical discharge caused by a partial discharge (pd). (5) All pins on each side of the barrier are tied together, creating a two-pin device. (6) Either method b1 or b2 is used in production. **<https://www.ti.com**>

# AMC1301 SBAS667G - APRIL 2016 - REVISED APRIL 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* Product Folder Links: *AMC1301*

## 6.7 Safety-Related Certifications

# VDE **UL**

# DIN EN IEC 60747-17 (VDE 0884-17),

EN IEC 60747-17, DIN EN IEC 62368-1 (VDE 0868-1), EN IEC 62368-1, IEC 62368-1 Clause: 5.4.3; 5.4.4.4; 5.4.9

Recognized under 1577 component recognition program Reinforced insulation Single protection

Certificate number: 40040142 File number: E181974

**6.8 Safety Limiting Values** Safety limiting (1) intends to minimize potential damage to the isolation barrier upon failure of input or output circuitry. A failure of the I/O can allow low resistance to ground or the supply and, without current limiting, dissipate sufficient power to over-heat the die and damage the isolation barrier potentially leading to secondary system failures.

# PARAMETER

**TEST CONDITIONS** **MIN** **TYP** **MAX** **UNIT**

I S Safety input, output, or supply current $$ R\thetaJA = 110.1°C/W, VDDx = 5.5 V, $$ $$ TJ = 150°C, TA = 25°C $$ mA

I S Safety input, output, or supply current $$ R\thetaJA = 110.1°C/W, VDDx = 3.6 V, $$ $$ TJ = 150°C, TA = 25°C $$ mA

P S Safety input, output, or total power $$ R\thetaJA = 110.1°C/W, TJ = 150°C, TA = 25°C $$ mW T S Maximum safety temperature °C

(1) The maximum safety temperature, T S, has the same value as the maximum junction temperature, T J, specified for the device. The I S and P S parameters represent the safety current and safety power, respectively. Do not exceed the maximum limits of I S and P S. These limits vary with the ambient temperature, T A. The junction-to-air thermal resistance, R θJA, in the Thermal Information table is that of a device installed on a high-K test board for leaded surface-mount packages. Use these equations to calculate the value for each parameter: T J = T A + R θJA × P, where P is the power dissipated in the device. T J(max) = T S = T A + R θJA × P S, where T J(max) is the maximum junction temperature. P S = I S × VDD max, where VDD max is the maximum supply voltage for high-side and low-side.

# AMC1301

SBAS667G - APRIL 2016 - REVISED APRIL 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated Product Folder Links: *AMC1301*

## 6.9 Electrical Characteristics

minimum and maximum specifications apply from T A = -40°C to +125°C (for AMC1301S: T A = -55°C to +125°C), VDD1 = 3.0 V to 5.5 V, VDD2 = 3.0 V to 5.5 V, INP = -250 mV to +250 mV, and INN = GND1; typical specifications are at TA = 25°C, VDD1 = 5 V, and VDD2 = 3.3 V (unless otherwise noted)

# PARAMETER

**TEST CONDITIONS** **MIN** **TYP** **MAX** **UNIT**

# ANALOG INPUT V CMov

Common-mode overvoltage detection level (V INP + V INN ) / 2 to GND1 VDD1 - 2 V

Hysteresis of common-mode overvoltage detection level mV

V OS Input offset voltage (1) Initial, at T A = 25°C, INP = INN = GND1 -0.2 \pm0.05 0.2 mV

TCV OS Input offset drift (1) (4) AMC1301 \pm1 µV/°C AMC1301S \pm1 CMRR Common-mode rejection ratio f IN = 0 Hz, V CM min ≤ V CM ≤ V CM max dB f IN = 10 kHz, V CM min ≤ V CM ≤ V CM max

R IN Single-ended input resistance INN = GND1 k\Omega R IND Differential input resistance k\Omega

I IB Input bias current INP = INN = GND1; IIB = (IIBP + IIBN) / 2 µA TCI IB Input bias current drift nA/°C C IND Differential input capacitance pF

# ANALOG OUTPUT Nominal gain 8.2 V/V

E G Gain error (1) at TA = 25°C -0.3% \pm0.05% 0.3% TCE G Gain drift (1) (5) AMC1301 \pm15 ppm/°C AMC1301S \pm15 Nonlinearity (1) -0.03% \pm0.01% 0.03% Nonlinearity drift \pm1 ppm/°C

THD Total harmonic distortion (3) fIN = 10 kHz dB

Output noise INP = INN = GND1, f IN = 0 Hz, BW = 100 kHz brickwall filter µV RMS SNR Signal-to-noise ratio fIN = 1 kHz, BW = 10 kHz

| dB | fIN = 10 kHz, BW = 100 kHz |
|:--- |:--- |
| PSRR | Power-supply rejection ratio(2) |
| PSRR vs VDD1, at DC | -94 | PSRR Power-supply rejection ratio (2) PSRR vs VDD1, at DC dB PSRR vs VDD1, 100-mV and 10-kHz ripple PSRR vs VDD2, at DC PSRR vs VDD2, 100-mV and 10-kHz ripple

V CMout Common-mode output voltage 1.39 1.44 1.49 V

V CLIPout Clipping differential output voltage V OUT = (V OUTP - V OUTN ); \|V IN \| = \|V INP - V INN \| \> \|V Clipping \| -2.52 \pm2.49 2.52 V

V Failsafe Failsafe differential output voltage V CM ≥ V CMov, or VDD1 missing -2.563 -2.545 V BW Output bandwidth kHz

R OUT Output resistance On OUTP or OUTN < 0.2 \Omega Output short-circuit current

On OUTP or OUTN, sourcing or sinking, INN = INP = GND1, outputs shorted to either GND2 or VDD2 mA

CMTI Common-mode transient immunity |GND1 - GND2| = 1 kV kV/µs **<https://www.ti.com**>

# AMC1301 SBAS667G - APRIL 2016 - REVISED APRIL 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* Product Folder Links: *AMC1301*

## 6.9 Electrical Characteristics (continued)

minimum and maximum specifications apply from T A = -40°C to +125°C (for AMC1301S: T A = -55°C to +125°C), VDD1 = 3.0 V to 5.5 V, VDD2 = 3.0 V to 5.5 V, INP = -250 mV to +250 mV, and INN = GND1; typical specifications are at TA = 25°C, VDD1 = 5 V, and VDD2 = 3.3 V (unless otherwise noted)

# PARAMETER

**TEST CONDITIONS** **MIN** **TYP** **MAX** **UNIT**

# POWER SUPPLY IDD1 High-side supply current $$ 3.0 V \leq VDD1 \leq 3.6 V $$ 6.3 8.5 mA $$ 4.5 V \leq VDD1 \leq 5.5 V $$ 7.2 9.8 IDD2 Low-side supply current $$ 3.0 V \leq VDD2 \leq 3.6 V $$ 5.3 7.2 mA $$ 4.5 V \leq VDD2 \leq 5.5 V $$ 5.9 8.1

(1) The typical value includes one standard deviation ( *sigma* ) at nominal operating conditions. (2) This parameter is input referred. (3) THD is the ratio of the rms sum of the amplitues of first five higher harmonics to the amplitude of the fundamental. (4) Offset error temperature drift is calculated using the box method, as described by the following equation: *TCV* *OS* * = (V* *OS,MAX* * - V* *OS,MIN* *) / TempRange* where V OS,MAX and V OS,MIN refer to the maximum and minimum V OS values measured within the temperature range (-40 to 125 ℃ ). (5) Gain error temperature drift is calculated using the box method, as described by the following equation: *TCE* *G* * (ppm) = ((E* *G,MAX* * - E* *G,MIN* *) / TempRange) x 10* *4* * * where E G,MAX and E G,MIN refer to the maximum and minimum E G values (in %) measured within the temperature range (-40 to 125 ℃ ).

## 6.10 Switching Characteristics

over operating ambient temperature range (unless otherwise noted)

# PARAMETER

**TEST CONDITIONS** **MIN** **TYP** **MAX** **UNIT** t r Output signal rise time 2.0 µs t f Output signal fall time 2.0 µs

V INx to V OUTx signal delay (50% - 10%) Unfiltered output 0.7 2.0 µs

V INx to V OUTx signal delay (50% - 50%) Unfiltered output 1.6 2.6 µs

V INx to V OUTx signal delay (50% - 90%) Unfiltered output 2.5 µs

## 6.11 Timing Diagram

# INP - INN

# OUTN 50% - 10% f 50% - 50% 50% - 90%

# OUTP r 250 mV 250 mV CMout

## Figure 6-1. Rise, Fall, and Delay Time Definition

# AMC1301

SBAS667G - APRIL 2016 - REVISED APRIL 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated Product Folder Links: *AMC1301*

# 6.12 Insulation Characteristics Curves

# T A (°C)

# I S (mA)

# D043

# VDD1 = VDD2 = 3.6 V $$ VDD1 = VDD2 = 5.5 V $$

## Figure 6-2. Thermal Derating Curve for Safety-Limiting Current

## per VDE

# T A (°C)

# P S (mW)

# D044

## Figure 6-3. Thermal Derating Curve for Safety-Limiting Power

## per VDE

## T A up to 150°C, stress voltage frequency = 60 Hz

## Figure 6-4. Reinforced Isolation Capacitor Lifetime Projection

## www.ti.com

# AMC1301 SBAS667G - APRIL 2016 - REVISED APRIL 2023

## Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## Product Folder Links: AMC1301

## 6.13 Typical Characteristics

## at VDD1 = 5 V, VDD2 = 3.3 V, INP = -250 mV to 250 mV, INN = 0 V, and fIN = 10 kHz (unless otherwise noted)

# VDD1 (V) V CMov (V) 3.25 3.5 3.75 4.25 4.5 4.75 5.25 5.5 1.4 1.8 2.2 2.6 3.4 3.8

# D001

**Figure 6-5. Common-Mode Overvoltage Detection Level vs ** **High-Side Supply Voltage** Temperature (°C) V CMov (V) 110 125 1.4 1.8 2.2 2.6 3.4 3.8

D002 -55°C \leq TA < 40°C valid for the AMC1301S only

**Figure 6-6. Common-Mode Overvoltage Detection Level vs ** **Temperature**

# V OS ( P V) Devices (%)

# D003

# VDD1 = 3.3 V

**Figure 6-7. Input Offset Voltage Histogram**

# V OS ( P V) Devices (%)

# D004

# VDD1 = 5 V

**Figure 6-8. Input Offset Voltage Histogram**

# VDDx (V)

# V OS ( P V) 3.25 3.5 3.75 4.25 4.5 4.75 5.25 5.5

# D005 vs VDD1 vs VDD2

**Figure 6-9. Input Offset Voltage vs Supply Voltage** Temperature (°C)

# V OS ( P V) 110 125

# D006 Device 1 Device 2 Device 3

-55°C \leq TA < 40°C valid for the AMC1301S only

**Figure 6-10. Input Offset Voltage vs Temperature**

# AMC1301

SBAS667G - APRIL 2016 - REVISED APRIL 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated Product Folder Links: *AMC1301*

## 6.13 Typical Characteristics (continued)

## at VDD1 = 5 V, VDD2 = 3.3 V, INP = -250 mV to 250 mV, INN = 0 V, and fIN = 10 kHz (unless otherwise noted)

# TCV OS ( P V/ q C) Devices (%) -2.5 -1.5 -0.5 0.5 1.5 2.5

# D007

# VDD1 = 3.3 V **Figure 6-11. Input Offset Drift Histogram**

# TCV OS ( P V/ q C) Devices (%) -2.5 -1.5 -0.5 0.5 1.5 2.5

# D008

# VDD1 = 5 V **Figure 6-12. Input Offset Drift Histogram** f IN (kHz)

# CMRR (dB) 0.001 0.01 0.1 0.5 2 3 5 10 20

# D009

**Figure 6-13. Common-Mode Rejection Ratio vs Input Frequency** Temperature (°C)

# CMRR (dB) 110 125

D011 -55°C \leq TA < 40°C valid for the AMC1301S only

**Figure 6-14. Common-Mode Rejection Ratio vs Temperature**

# V CM (V)

# I IB ( P A) -0.5 0.5 1.5 2.5

# D012

**Figure 6-15. Input Bias Current vs Common-Mode Input Voltage**

# VDD1 (V)

# I IB ( P A) 3.25 3.5 3.75 4.25 4.5 4.75 5.25 5.5

# D013

**Figure 6-16. Input Bias Current vs High-Side Supply Voltage** **<https://www.ti.com**>

# AMC1301 SBAS667G - APRIL 2016 - REVISED APRIL 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* Product Folder Links: *AMC1301*

# 6.13 Typical Characteristics (continued)

## at VDD1 = 5 V, VDD2 = 3.3 V, INP = -250 mV to 250 mV, INN = 0 V, and fIN = 10 kHz (unless otherwise noted) Temperature (°C)

# I IB ( P A) 110 125

D014 -55°C \leq TA < 40°C valid for the AMC1301S only

## Figure 6-17. Input Bias Current vs Temperature Input Signal Frequency (kHz) Normalized Gain (dB) 0.01 0.1

# D015

## Figure 6-18. Normalized Gain vs Input Frequency

# E G (%) Devices (%) -0.3 -0.25 -0.2 -0.15 -0.1 -0.05 0.05 0.1 0.15 0.2 0.25 0.3

# D016

# VDD1 = 3.3 V

## Figure 6-19. Gain Error Histogram

# E G (%) Devices (%) -0.3 -0.25 -0.2 -0.15 -0.1 -0.05 0.05 0.1 0.15 0.2 0.25 0.3

# D017

# VDD1 = 5 V

## Figure 6-20. Gain Error Histogram

# VDDx (V)

# E G (%) 3.25 3.5 3.75 4.25 4.5 4.75 5.25 5.5 -0.3 -0.25 -0.2 -0.15 -0.1 -0.05 0.05 0.1 0.15 0.2 0.25 0.3

# D018 vs VDD1 vs VDD2

## Figure 6-21. Gain Error vs Supply Voltage Temperature (°C)

# E G (%) 110 125 -0.3 -0.25 -0.2 -0.15 -0.1 -0.05 0.05 0.1 0.15 0.2 0.25 0.3

# D019 Device 1 Device 2 Device 3

## 55°C \\leq TA \< 40°C valid for the AMC1301S only

## Figure 6-22. Gain Error vs Temperature

# AMC1301

SBAS667G - APRIL 2016 - REVISED APRIL 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## Product Folder Links: AMC1301

# 6.13 Typical Characteristics (continued)

## at VDD1 = 5 V, VDD2 = 3.3 V, INP = -250 mV to 250 mV, INN = 0 V, and fIN = 10 kHz (unless otherwise noted) TCE G (ppm/ q C) Devices (%)

# D020

# VDD1 = 3.3 V

## Figure 6-23. Gain Error Drift Histogram TCE G (ppm/ q C) Devices (%)

# D021

# VDD1 = 5 V

## Figure 6-24. Gain Error Drift Histogram Differential Input Voltage (mV)

# V OUT (V) 0.5 1.5 2.5 3.5 4.5

# D022

# V OUTN V OUTP

## Figure 6-25. Output Voltage vs Input Voltage Differential Input Voltage (mV) Nonlinearity (%) -250 -200 -150 -100 -0.03 -0.025 -0.02 -0.015 -0.01 -0.005 0.005 0.01 0.015 0.02 0.025 0.03

# D024

## Figure 6-26. Nonlinearity vs Input Voltage

# VDDx (V) Nonlinearity (%) 3.25 3.5 3.75 4.25 4.5 4.75 5.25 5.5 -0.03 -0.025 -0.02 -0.015 -0.01 -0.005 0.005 0.01 0.015 0.02 0.025 0.03

# D025 vs VDD1 vs VDD2

## Figure 6-27. Nonlinearity vs Supply Voltage Temperature (°C) Nonlinearity (%) 110 125 -0.03 -0.025 -0.02 -0.015 -0.01 -0.005 0.005 0.01 0.015 0.02 0.025 0.03

# D026 Device 1 Device 2 Device 3

## 55°C \\leq TA \< 40°C valid for the AMC1301S only

## Figure 6-28. Nonlinearity vs Temperature

## www.ti.com

# AMC1301 SBAS667G - APRIL 2016 - REVISED APRIL 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## Product Folder Links: AMC1301

## 6.13 Typical Characteristics (continued)

## at VDD1 = 5 V, VDD2 = 3.3 V, INP = -250 mV to 250 mV, INN = 0 V, and fIN = 10 kHz (unless otherwise noted)

# VDDx (V)

# THD (dB) 3.25 3.5 3.75 4.25 4.5 4.75 5.25 5.5

# D027 vs VDD1 vs VDD2

## Figure 6-29. Total Harmonic Distortion vs Supply Voltage Temperature (°C)

# THD (dB) 110 125

# D028 Device 1 Device 2 Device 3

## 55°C \\leq TA \< 40°C valid for the AMC1301S only

## Figure 6-30. Total Harmonic Distortion vs Temperature

# \|VINP - VINN\| (mV)

# SNR (dB)

# D029

## Figure 6-31. Signal-to-Noise Ratio vs Input Voltage

# VDDx (V)

# SNR (dB) 3.25 3.5 3.75 4.25 4.5 4.75 5.25 5.5 62.5 67.5 72.5 77.5

# D030 vs VDD1 vs VDD2

## Figure 6-32. Signal-to-Noise Ratio vs Supply Voltage Temperature (°C)

# SNR (dB) 110 125 62.5 67.5 72.5 77.5

# D031 Device 1 Device 2 Device 3

## 55°C \\leq TA \< 40°C valid for the AMC1301S only

## Figure 6-33. Signal-to-Noise Ratio vs Temperature Frequency (kHz) Input Referred Noise Density (nV/ - Hz) 0.01 0.1

# D032

## Figure 6-34. Input-Referred Noise Density vs Frequency

# AMC1301

SBAS667G - APRIL 2016 - REVISED APRIL 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## Product Folder Links: AMC1301

## 6.13 Typical Characteristics (continued)

## at VDD1 = 5 V, VDD2 = 3.3 V, INP = -250 mV to 250 mV, INN = 0 V, and fIN = 10 kHz (unless otherwise noted) Ripple Frequency (kHz)

# PSRR (dB) 0.001 0.01 0.1 D033 vs VDD1

## Figure 6-35. Power-Supply Rejection Ratio vs Ripple Frequency Ripple Frequency (kHz)

# PSRR (dB) 0.001 0.01 0.1 D042 vs VDD2

## Figure 6-36. Power-Supply Rejection Ratio vs Ripple Frequency Temperature (°C) Rise/Fall Time ( P s) 110 125 0.5 1.5 2.5 3.5

D034 -55°C \leq TA < 40°C valid for the AMC1301S only

## Figure 6-37. Output Rise and Fall Time vs Temperature

# VDD2 (V) Signal Delay ( P s) 3.25 3.5 3.75 4.25 4.5 4.75 5.25 5.5 0.2 0.6 1.4 1.8 2.2 2.6 3.4 3.8

# D035 50% - 10% 50% - 50% 50% - 90%

## Figure 6-38. V IN to V OUT Signal Delay vs Low-Side

## Supply Voltage Temperature (°C) Signal Delay ( P s) 110 125 0.2 0.6 1.4 1.8 2.2 2.6 3.4 3.8

# D036 50% - 10% 50% - 50% 50% - 90%

## 55°C \\leq TA \< 40°C valid for the AMC1301S only

## Figure 6-39. V IN to V OUT Signal Delay vs Temperature

# VDD2 (V) Output Common-Mode Voltage (V) 3.25 3.5 3.75 4.25 4.5 4.75 5.25 5.5 1.39 1.4 1.41 1.42 1.43 1.44 1.45 1.46 1.47 1.48 1.49

# D010

## Figure 6-40. Output Common-Mode Voltage vs Low-Side

## Supply Voltage

## www.ti.com

# AMC1301 SBAS667G - APRIL 2016 - REVISED APRIL 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## Product Folder Links: AMC1301

## 6.13 Typical Characteristics (continued)

## at VDD1 = 5 V, VDD2 = 3.3 V, INP = -250 mV to 250 mV, INN = 0 V, and fIN = 10 kHz (unless otherwise noted) Temperature (°C) V CMout (V) 110 125 1.39 1.4 1.41 1.42 1.43 1.44 1.45 1.46 1.47 1.48 1.49

D037 -55°C \leq TA < 40°C valid for the AMC1301S only

**Figure 6-41. Output Common-Mode Voltage vs Temperature**

# VDD2 (V) BW (kHz) 3.25 3.5 3.75 4.25 4.5 4.75 5.25 5.5

# D038

**Figure 6-42. Output Bandwidth vs Low-Side Supply Voltage** Temperature (°C) BW (kHz) 110 125

D039 -55°C \leq TA < 40°C valid for the AMC1301S only

**Figure 6-43. Output Bandwidth vs Temperature**

# VDDx (V) I DDx (mA) 3.25 3.5 3.75 4.25 4.5 4.75 5.25 5.5 3.5 4.5 5.5 6.5 7.5 8.5

# D040

# I DD1 vs VDD1 I DD2 vs VDD2

**Figure 6-44. Supply Current vs Supply Voltage** Temperature (°C) I DDx (mA) 110 125 3.5 4.5 5.5 6.5 7.5 8.5

# D041

# I DD1 I DD2

-55°C \leq TA < 40°C valid for the AMC1301S only

**Figure 6-45. Supply Current vs Temperature**

# AMC1301

SBAS667G - APRIL 2016 - REVISED APRIL 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated Product Folder Links: *AMC1301*

## 7 Detailed Description **7.1 Overview**

The AMC1301 is a fully differential, precision, isolated amplifier. The input stage of the device consists of a fully differential amplifier that drives a second-order, delta-sigma (ΔΣ) modulator. The modulator converts the analog input signal into a digital bitstream that is transferred across the isolation barrier that separates the high-side from the low-side. On the low-side, the received bitstream is processed by a fourth-order analog filter that outputs a differential signal at the OUTP and OUTN pins that is proportional to the input signal.

The SiO 2 -based, capacitive isolation barrier supports a high level of magnetic field immunity, as described in the *ISO72x Digital Isolator Magnetic-Field Immunity* application note. The digital modulation used in the AMC1301 to transmit data across the isolation barrier, and the isolation barrier characteristics, result in high reliability and common-mode transient immunity. **7.2 Functional Block Diagram**

# AMC1301 ΔΣ Modulator

# RX / TX

Isolation                                   Barrier

# GND1

# INP

# INN

# VDD1 Diagnostics

# VDD2

# OUTP

# OUTN

# GND2

# TX / RX Analog Filter **7.3 Feature Description** **7.3.1 Analog Input**

The differential amplifier input stage of the AMC1301 feeds a second-order, switched-capacitor, feed-forward ΔΣ modulator. The gain of the differential amplifier is set by internal precision resistors with a differential input impedance of R IND. The modulator converts the analog input signal into a bitstream that is transferred across the isolation barrier, as described in the *Isolation Channel Signal Transmission* section.

There are two restrictions on the analog input signals (INP and INN). First, if the input voltages V INP or V INN exceed the range specified in the *Absolute Maximum Ratings* table, the input currents must be limited to the absolute maximum value, because the electrostatic discharge (ESD) protection turns on. In addition, the linearity and parametric performance of the device are ensured only when the analog input voltage remains within the linear full-scale range (V FSR ) and within the common-mode input voltage range (V CM ), as specified in the *Recommended Operating Conditions* table. **<https://www.ti.com**>

# AMC1301 SBAS667G - APRIL 2016 - REVISED APRIL 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* Product Folder Links: *AMC1301*

**7.3.2 Isolation Channel Signal Transmission**

The AMC1301 uses an on-off keying (OOK) modulation scheme, as shown in Figure 7-1, to transmit the modulator output bitstream across the SiO 2 -based isolation barrier. The transmit driver (TX) shown in the *Functional Block Diagram* transmits an internally generated, high-frequency carrier across the isolation barrier to represent a digital *one* and does not send a signal to represent a digital *zero*. The nominal frequency of the carrier used inside the AMC1301 is 480 MHz.

The receiver (RX) on the other side of the isolation barrier recovers and demodulates the signal and provides the input to the fourth-order analog filter. The AMC1301 transmission channel is optimized to achieve the highest level of common-mode transient immunity (CMTI) and lowest level of radiated emissions caused by the high-frequency carrier and RX/TX buffer switching. Modulator Bitstream on High-side Internal Clock Signal Across Isolation Barrier Recovered Sigal on Low-side **Figure 7-1. OOK-Based Modulation Scheme**

# AMC1301

SBAS667G - APRIL 2016 - REVISED APRIL 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated Product Folder Links: *AMC1301* **7.3.3 Analog Output**

The AMC1301 offers a differential analog output comprised of the OUTP and OUTN pins. For differential input voltages (V INP - V INN ) in the range from -250 mV to 250 mV, the device provides a linear response with a nominal gain of 8.2. For example, for a differential input voltage of 250 mV, the differential output voltage (V OUTP - V OUTN ) is 2.05 V. At zero input (INP shorted to INN), both pins output the same common-mode output voltage  V CMout, as specified in the *Electrical Characteristics* table. For absolute differential input voltages greater than 250 mV but less than 320 mV, the differential output voltage continues to increase in magnitude but with reduced linearity performance. The outputs saturate at a differential output voltage of V CLIPout, as shown in Figure 7-2, if the differential input voltage exceeds the V Clipping value. Linear input range (V FSR )

Maximum input range before clipping (V Clipping ) 320 mV 320 mV 250 mV 250 mV

# OUTP

# OUTN Differential Input Voltage (V INP ± V INN ) CMout \pm \pm CLIPout

# FAILSAFE

**Figure 7-2. Output Behavior of the AMC1301 **

The AMC1301 offers a fail-safe feature that simplifies diagnostics on a system level. Figure 7-2 shows the fail-safe mode, in which the AMC1301 outputs a negative differential output voltage that does not occur under normal operating conditions. The fail-safe output is active in two cases: - • When the high-side supply is missing or below the VDD1 UV threshold - • When the common-mode input voltage, that is V CM = (V INP + V INN ) / 2, exceeds the common-mode  overvoltage detection level V CMov

Use the maximum V FAILSAFE voltage specified in the *Electrical Characteristics* table as a reference value for fail-safe detection on a system level. **7.4 Device Functional Modes**

The AMC1301 assumes normal operation as soon as VDD1, VDD2, and the input common-mode voltage (V CM ) are within the operational ranges, as specified in *Electrical Characteristics* table. In this mode, the output voltage is proportional to the input voltage.

The AMC1301 enters fail-safe mode whenever the high-side supply (VDD1) is missing or the input commonmode voltage (V CM ) exceeds the specified input-overvoltage detection level V CMov. In this mode, the differential output voltage is a fixed, negative value (V FAILSAFE ). See the *Analog Output* section for details. **<https://www.ti.com**>

# AMC1301 SBAS667G - APRIL 2016 - REVISED APRIL 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* Product Folder Links: *AMC1301*

# 8 Application and Implementation

## Note

## Information in the following applications sections is not part of the TI component specification,

and TI does not warrant its accuracy or completeness. TI's customers are responsible for determining suitability of components for their purposes, as well as validating and testing their design implementation to confirm system functionality.

# 8.1 Application Information

## With a low analog input voltage range, high DC accuracy, and low temperature drift, the AMC1301 is designed

for precision, shunt-based current sensing in applications requiring high voltage isolation.

# 8.2 Typical Application

## Figure 8-1 shows the AMC1301 in a typical application of an AC motor drive. The load current flowing through

an external shunt resistor RSHUNT produces a voltage drop that is sensed by the AMC1301. The AMC1301 digitizes the analog input signal on the high-side, transfers the data across the isolation barrier to the low-side, reconstructs the analog signal, and presents that signal as a differential voltage on the output pins.

## The differential input, differential output, and the high common-mode transient immunity (CMTI) of the AMC1301

provide reliable and accurate operation even in high-noise environments. 10   

# RSHUNT 1 uF 100 nF

# R4 Floating Gate Driver Supply + DC Link - DC Link

## Load

# 5 V

# D1 10 nF 1 nF 1 nF

# VDD1

# GND1

# INP

# INN

# AMC1301

# VDD2

# OUTP

# OUTN

# GND2 1 uF 100 nF 10   Low-side supply (3.3 V or 5 V)

# ADC 10 nF

## Figure 8-1. Using the AMC1301 for Current Sensing in a Typical Application

# AMC1301

SBAS667G - APRIL 2016 - REVISED APRIL 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## Product Folder Links: AMC1301 **8.2.1 Design Requirements**

Table 8-1 lists the parameters for this typical application. **Table 8-1. Design Requirements**

| PARAMETER | VALUE |
|:--- |:--- |
| High-side supply voltage | 3.3 V or 5 V |
| Low-side supply voltage | 3.3 V or 5 V |
| Voltage drop across RSHUNT for a linear response | ±250 mV (maximum) |
| Signal delay (50% VIN to 90% OUTP, OUTN) | 3 µs (maximum) | High-side supply voltage 3.3 V or 5 V Low-side supply voltage 3.3 V or 5 V

Voltage drop across RSHUNT for a linear response \pm250 mV (maximum)

Signal delay (50% V IN to 90% OUTP, OUTN) 3 µs (maximum) **8.2.2 Detailed Design Procedure**

In Figure 8-1, the high-side power supply (VDD1) for the AMC1301 is derived from the floating power supply of the upper gate driver.

The floating ground reference (GND1) is derived from the end of the shunt resistor that is connected to the negative input of the AMC1301 (INN). If a four-pin shunt is used, the inputs of the AMC1301 are connected to the inner leads and GND1 is connected to the outer lead on the INN-side of the shunt. To minimize offset and improve accuracy, route the ground connection as a separate trace that connects directly to the shunt resistor rather than shorting GND1 to INN directly at the input to the device. See the *Layout* section for more details. ***8.2.2.1 Shunt Resistor Sizing***

Use Ohm's Law to calculate the voltage drop across the shunt resistor (V SHUNT ) for the desired measured current: V SHUNT = I × RSHUNT.

Consider the following two restrictions when selecting the value of the shunt resistor, RSHUNT:

| voltage range for a linear response: | VSHUNT | ≤ | VFSR |
|:--- |:--- |:--- |:--- |
| a clipping output: | VSHUNT | ≤ | VClipping | ***8.2.2.2 Input Filter Design***

Place a differential RC filter (R1, R2, C5) in front of the isolated amplifier to improve signal-to-noise performance of the signal path. Design the input filter such that:

- • The cutoff frequency of the filter is at least one order of magnitude lower than the sampling frequency of the  ΔΣ modulator (20 MHz) - • The input bias current does not generate significant voltage drop across the DC impedances (R1, R2) of the  input filter - • The impedances measured from the analog inputs are equal (R1 equals R2)

Capacitors C6 and C7 are optional and improve common-mode rejection at high frequencies (\>1 MHz). For best performance, C6 must match the value of C7 and both capacitors must be 10 to 20 times lower in value than C5. For most applications, the structure shown in Figure 8-2 achieves excellent performance.

# VDD1

# GND1

# INP

# INN

# AMC1301

# VDD2

# OUTP

# OUTN

# GND2

# R2 10 

# R1 10   C5 10 nF

# RSHUNT C6 1 nF C7 1 nF **Figure 8-2. Differential Input Filter** **<https://www.ti.com**>

# AMC1301 SBAS667G - APRIL 2016 - REVISED APRIL 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* Product Folder Links: *AMC1301*

***8.2.2.3 Differential to Single-Ended Output Conversion***

Figure 8-3 shows an example of a TLV900x -based signal conversion and filter circuit for systems using singleended input ADCs to convert the analog output voltage into digital. For R1 = R3 and R2 = R4, the output voltage equals (R2 / R1) × (V OUTP - V OUTN ) + V REF. Tailor the bandwidth of this filter stage to the bandwidth requirement of the system and use NP0-type capacitors for best performance. For most applications, R1 = R2 = R3 = R4 = 3.3 kΩ and C1 = C2 = 330 pF yields good performance.

# VDD1

# GND1

# INP

# INN

# AMC1301

# VDD2

# OUTP

# OUTN

# GND2 +

# R4

# R3

# R1

# R2

# REF

# ADC To MCU

# C1

# C2 **TLV9001**

**Figure 8-3. Connecting the AMC1301 Output to a Single-Ended Input ADC**

For more information on the general procedure to design the filtering and driving stages of SAR ADCs, see the *18-Bit, 1MSPS Data Acquisition Block (DAQ) Optimized for Lowest Distortion and Noise* and *18-Bit Data * *Acquisition Block (DAQ) Optimized for Lowest Power* reference guides, available for download at <https://www.ti.com>. **8.2.3 Application Curve**

One important aspect of power-stage design is the effective detection of an overcurrent condition to protect the switching devices and passive components from damage. To power off the system quickly in the event of an overcurrent condition, a low delay caused by the isolated amplifier is required. Figure 8-4 shows the typical full-scale step response of the AMC1301.

# VIN VOUTP VOUTN **Figure 8-4. Step Response of the AMC1301 **

# AMC1301

SBAS667G - APRIL 2016 - REVISED APRIL 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated Product Folder Links: *AMC1301*

## 8.3 Best Design Practices

## Do not leave the inputs of the AMC1301 unconnected (floating) when the device is powered up. If the device

inputs are left floating, the input bias current can possibly drive the inputs to a positive value that exceeds the operating common-mode input voltage, thus causing the device to output the fail-safe voltage as described in the *Analog Output* section.

## Connect the high-side ground (GND1) to INN, either by a hard short or through a resistive path. A DC current

path between INN and GND1 is required to define the input common-mode voltage. Take care not to exceed the input common-mode range as specified in the *Recommended Operating Conditions* table. For best accuracy, route the ground connection as a separate trace that connects directly to the shunt resistor rather than shorting GND1 to INN directly at the input to the device. See the *Layout* section for more details.

## 8.4 Power Supply Recommendations

## The AMC1301 does not require any specific power-up sequencing. The high-side power supply (AVDD) is

decoupled with a low-ESR, 100-nF capacitor (C1) parallel to a low-ESR, 1-µF capacitor (C2). The low-side power supply (DVDD) is equally decoupled with a low-ESR, 100-nF capacitor (C3) parallel to a low-ESR, 1-µF capacitor (C4). Place all four capacitors (C1, C2, C3, and C4) as close to the device as possible.

## The ground reference for the high-side (AGND) is derived from the end of the shunt resistor that is connected

to the negative input (INN) of the device. For best DC accuracy, use a separate trace to make this connection instead of shorting AGND to INN directly at the device input. If a four-terminal shunt is used, the device inputs are connected to the inner leads and AGND is connected to the outer lead on the INN side of the shunt. Figure 8-5 shows a decoupling diagram of the AMC1301.

# R2 10 

# R1 10   C5 10 nF

# RSHUNT

# VDD1

# I

# VDD2 INP C2 1 µF C1 100 nF C4 1 µF C3 100 nF C6 1 nF C7 1 nF to RC filter / ADC to RC filter / ADC

# VDD1

# GND1

# INP

# INN

# AMC1301

# VDD2

# OUTP

# OUTN

# GND2

## Figure 8-5. Decoupling of the AMC1301 **<https://www.ti.com**>

# AMC1301 SBAS667G - APRIL 2016 - REVISED APRIL 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* Product Folder Links: *AMC1301*

## 8.5 Layout

## 8.5.1 Layout Guidelines

## Figure 8-6 shows a layout recommendation with the critical placement of the decoupling capacitors (as close as

possible to the AMC1301 supply pins) and placement of the other components required by the device. For best performance, place the shunt resistor close to the INP and INN inputs of the AMC1301 and keep the layout of both connections symmetrical.

## 8.5.2 Layout Example

# C2

# C1

# AMC1301

Clearance area, to be kept free of any conductive materials. Top Metal Inner or Bottom Layer Metal Via

# C5

# R1

# R2

# RSHUNT

# INP

# INN

# GND1

# VDD1

# C6

# C7

# VDD2

# GND2 to RC filter / ADC to RC filter / ADC

# C4

# C3

## Figure 8-6. Recommended Layout of the AMC1301

# AMC1301

SBAS667G - APRIL 2016 - REVISED APRIL 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated Product Folder Links: *AMC1301*

## 9 Device and Documentation Support **9.1 Documentation Support** **9.1.1 Related Documentation** For related documentation, see the following:

- • Texas Instruments, *Isolation Glossary* application note - • Texas Instruments, *Semiconductor and IC Package Thermal Metrics* application note - • Texas Instruments, *ISO72x Digital Isolator Magnetic-Field Immunity* application note - • Texas Instruments, *TLV900x Low-Power, RRIO, 1-MHz Operational Amplifier for Cost-Sensitive Systems * data sheet - • Texas Instruments, *18-Bit, 1-MSPS Data Acquisition Block (DAQ) Optimized for Lowest Distortion and Noise * reference guide - • Texas Instruments, *18-Bit, 1-MSPS Data Acquisition Block (DAQ) Optimized for Lowest Power* reference  guide - • Texas Instruments, *Isolated Amplifier Voltage Sensing Excel Calculator * design tool - • Texas Instruments, *Best in Class Radiated Emissions EMI Performance with the AMC1300B-Q1 Isolated * *Amplifier* technical white paper - • Texas Instruments, *Isolated Voltage-Measurement Circuit With ±250-mV Input and Differential Output * application note

**9.2 Receiving Notification of Documentation Updates**

To receive notification of documentation updates, navigate to the device product folder on ti.com. Click on *Subscribe to updates* to register and receive a weekly digest of any product information that has changed. For change details, review the revision history included in any revised document. **9.3 Support Resources**

TI E2E ™ support forums are an engineer's go-to source for fast, verified answers and design help - straight from the experts. Search existing answers or ask your own question to get the quick design help you need.

Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do not necessarily reflect TI's views; see TI's Terms of Use.

**9.4 Trademarks** TI E2E ™ is a trademark of Texas Instruments. All trademarks are the property of their respective owners. **9.5 Electrostatic Discharge Caution**

This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.

ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may be more susceptible to damage because very small parametric changes could cause the device not to meet its published specifications. **9.6 Glossary**

TI Glossary This glossary lists and explains terms, acronyms, and definitions.

## 10 Mechanical, Packaging, and Orderable Information

The following pages include mechanical, packaging, and orderable information. This information is the most current data available for the designated devices. This data is subject to change without notice and revision of this document. For browser-based versions of this data sheet, refer to the left-hand navigation. **<https://www.ti.com**>

# AMC1301 SBAS667G - APRIL 2016 - REVISED APRIL 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* Product Folder Links: *AMC1301*

# PACKAGE OPTION ADDENDUM <https://www.ti.com> 6-Feb-2026

# PACKAGING INFORMATION **Orderable part number** **Status** (1) **Material type** (2)

**Package \| Pins** **Package qty \| Carrier** **RoHS** (3) **Lead finish/** **Ball material** (4) **MSL rating/** **Peak reflow** (5) **Op temp (°C)** **Part marking** (6)

AMC1301DWV Active Production SOIC (DWV) \| 8 64 \| TUBE Yes NIPDAU Level-3-260C-168 HR -40 to 125 AMC1301

AMC1301DWVR Active Production SOIC (DWV) \| 8 1000 \| LARGE T&R Yes NIPDAU Level-3-260C-168 HR -40 to 125 AMC1301

AMC1301DWVRG4 Active Production SOIC (DWV) \| 8 1000 \| LARGE T&R Yes NIPDAU Level-3-260C-168 HR -55 to 125 AMC1301

AMC1301SDWV Active Production SOIC (DWV) \| 8 64 \| TUBE Yes NIPDAU Level-3-260C-168 HR -55 to 125 AMC1301S

AMC1301SDWVR Active Production SOIC (DWV) \| 8 1000 \| LARGE T&R Yes NIPDAU Level-3-260C-168 HR -55 to 125 AMC1301S

AMC1301SDWVRG4 Active Production SOIC (DWV) \| 8 1000 \| LARGE T&R Yes NIPDAU Level-3-260C-168 HR -55 to 125 AMC1301S **(1)** ** Status: ** For more details on status, see our product life cycle.

**(2)** ** Material type: ** When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance, reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind.

**(3)** ** RoHS values: ** Yes, No, RoHS Exempt. See the TI RoHS Statement for additional information and value definition.

**(4)** ** Lead finish/Ball material: ** Parts may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two lines if the finish value exceeds the maximum column width.

**(5)** ** MSL rating/Peak reflow: ** The moisture sensitivity level ratings and peak solder (reflow) temperatures. In the event that a part has multiple moisture sensitivity ratings, only the lowest level per JEDEC standards is shown. Refer to the shipping label for the actual reflow temperature that will be used to mount the part to the printed circuit board.

**(6)** ** Part marking: ** There may be an additional marking, which relates to the logo, the lot trace code information, or the environmental category of the part. Multiple part markings will be inside parentheses. Only one part marking contained in parentheses and separated by a "~" will appear on a part. If a line is indented then it is a continuation of the previous line and the two combined represent the entire part marking for that device. **Important Information and Disclaimer:** The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release. In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis. Addendum-Page 1

# PACKAGE OPTION ADDENDUM <https://www.ti.com> 6-Feb-2026

# OTHER QUALIFIED VERSIONS OF AMC1301 - Automotive: AMC1301-Q1

## NOTE: Qualified Version Definitions

- Automotive - Q100 devices qualified for high-reliability automotive applications targeting zero defects Addendum-Page 2

# PACKAGE MATERIALS INFORMATION <https://www.ti.com> 5-Dec-2025

# TAPE AND REEL INFORMATION Reel Width (W1)

# REEL DIMENSIONS

# A0 B0 K0

# W

Dimension designed to accommodate the component length Dimension designed to accommodate the component thickness Overall width of the carrier tape Pitch between successive cavity centers

Dimension designed to accommodate the component width

# TAPE DIMENSIONS

# K0 P1

# B0 W A0 Cavity

# QUADRANT ASSIGNMENTS FOR PIN 1 ORIENTATION IN TAPE Pocket Quadrants Sprocket Holes

# Q1 Q1 Q2 Q2 Q3 Q3 Q4 Q4 User Direction of Feed

# P1 Reel Diameter \*All dimensions are nominal **Device** **Package** **Type** **Package** **Drawing**

**Pins** **SPQ** **Reel** **Diameter** **(mm)** **Reel** **Width** **W1 (mm)**

| A0 | (mm) |
|:--- |:--- |
| B0 | (mm) |
| K0 | (mm) |
| P1 | (mm) |
| W | (mm) |
| Pin1 | Quadrant | **B0** **(mm)** **K0** **(mm)** **P1** **(mm)** **W** **(mm)** **Pin1** **Quadrant**

# AMC1301DWVR

SOIC DWV 330.0 16.4 12.15 6.2 3.05 16.0 16.0 Q1

# AMC1301DWVRG4

SOIC DWV 330.0 16.4 12.15 6.2 3.05 16.0 16.0 Q1

# AMC1301SDWVR

SOIC DWV 330.0 16.4 12.15 6.2 3.05 16.0 16.0 Q1

# AMC1301SDWVRG4

SOIC DWV 330.0 16.4 12.15 6.2 3.05 16.0 16.0 Q1 Pack Materials-Page 1

# PACKAGE MATERIALS INFORMATION <https://www.ti.com> 5-Dec-2025

# TAPE AND REEL BOX DIMENSIONS ***Width (mm)***

# W

# L

# H \*All dimensions are nominal

**Device** **Package Type** **Package Drawing** **Pins** **SPQ** **Length (mm)** **Width (mm)** **Height (mm)**

| AMC1301DWVR | SOIC | DWV | 353.0 | 353.0 | 32.0 |
|:--- |:--- |:--- | ---: | ---: | ---: |
| AMC1301DWVRG4 | SOIC | DWV | 353.0 | 353.0 | 32.0 |
| AMC1301SDWVR | SOIC | DWV | 353.0 | 353.0 | 32.0 |
| AMC1301SDWVRG4 | SOIC | DWV | 353.0 | 353.0 | 32.0 |

# AMC1301DWVRG4 SOIC DWV 353.0 353.0 32.0

# AMC1301SDWVR SOIC DWV 353.0 353.0 32.0

# AMC1301SDWVRG4 SOIC DWV 353.0 353.0 32.0 Pack Materials-Page 2

# PACKAGE MATERIALS INFORMATION <https://www.ti.com> 5-Dec-2025

# TUBE

## L - Tube length **T - Tube  **

## height

## W - Tube

## width

## B - Alignment groove width \*All dimensions are nominal

**Device** **Package Name** **Package Type** **Pins** **SPQ** **L (mm)** **W (mm)** **T (µm)** **B (mm)**

# AMC1301DWV DWV SOIC 505.46 13.94 6.6

# AMC1301SDWV DWV SOIC 505.46 13.94 6.6 Pack Materials-Page 3 <https://www.ti.com>

# PACKAGE OUTLINE

# C

# TYP 11.5 0.25

# 2.8 MAX

# TYP 0.33 0.13 0 -8

# 6X 1.27

# 8X 0.51 0.31

# 2X 3.81 0.46 0.36 1.0 0.5

# 0.25 GAGE PLANE

# A

# NOTE 3 5.95 5.75

# B

# NOTE 4 7.6 7.4 (2.286) (2)

# 4218796/A 09/2013

# SOIC - 2.8 mm max height DWV0008A

# SOIC

NOTES: 1. All linear dimensions are in millimeters. Dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M. 2. This drawing is subject to change without notice.  3. This dimension does not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not exceed 0.15 mm, per side. 4. This dimension does not include interlead flash. Interlead flash shall not exceed 0.25 mm, per side.

# 0.25 C A B

# AREA PIN 1 ID

# SEATING PLANE

# 0.1 C

# SEE DETAIL A

# DETAIL A TYPICAL

# SCALE 2.000 <https://www.ti.com>

# EXAMPLE BOARD LAYOUT (10.9)

# 0.07 MAX ALL AROUND 0.07 MIN ALL AROUND

# 8X (1.8)

# 8X (0.6)

# 6X (1.27)

# 4218796/A 09/2013

# SOIC - 2.8 mm max height DWV0008A

# SOIC

# SYMM

# SYMM

# SEE DETAILS

# LAND PATTERN EXAMPLE 9.1 mm NOMINAL CLEARANCE/CREEPAGE SCALE:6X

NOTES: (continued) 5. Publication IPC-7351 may have alternate designs.  6. Solder mask tolerances between and around signal pads can vary based on board fabrication site.

# METAL SOLDER MASK OPENING

# NON SOLDER MASK DEFINED

# SOLDER MASK DETAILS

# OPENING SOLDER MASK METAL

# SOLDER MASK DEFINED <https://www.ti.com>

# EXAMPLE STENCIL DESIGN

# 8X (1.8)

# 8X (0.6)

# 6X (1.27) (10.9)

# 4218796/A 09/2013

# SOIC - 2.8 mm max height DWV0008A

# SOIC

NOTES: (continued) 7. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate design recommendations. 8. Board assembly site may have different recommendations for stencil design.

# SOLDER PASTE EXAMPLE BASED ON 0.125 mm THICK STENCIL SCALE:6X

# SYMM

# SYMM

# IMPORTANT NOTICE AND DISCLAIMER

# TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATASHEETS), DESIGN RESOURCES (INCLUDING REFERENCE

DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES "AS IS" AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.

These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, regulatory or other requirements.

These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you fully indemnify TI and its representatives against any claims, damages, costs, losses, and liabilities arising out of your use of these resources.

TI's products are provided subject to TI's Terms of Sale, TI's General Quality Guidelines, or other applicable terms available either on ti.com or provided in conjunction with such TI products. TI's provision of these resources does not expand or otherwise alter TI's applicable warranties or warranty disclaimers for TI products. Unless TI explicitly designates a product as custom or customer-specified, TI products are standard, catalog, general purpose devices.

TI objects to and rejects any additional or different terms you may propose.

# IMPORTANT NOTICE

Copyright © 2026, Texas Instruments Incorporated

Last updated 10/2025