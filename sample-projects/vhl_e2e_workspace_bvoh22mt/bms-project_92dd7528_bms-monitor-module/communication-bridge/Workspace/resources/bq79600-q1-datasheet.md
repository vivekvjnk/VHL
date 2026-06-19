## BQ79600-Q1 Automotive SPI/UART Communication Interface Functional-Safety **Compliant With Automatic Host Wakeup**

## 1 Features

- • Qualified for automotive applications - • AEC-Q100 Qualified with the following results: - - Device temperature grade 1: -40°C to +125°C ambient operating temperature range - - Device HBM ESD classification level 2 - - Device CDM ESD classification level C4B - • Functional Safety-Compliant - - Developed for functional safety applications - - Documentation available to aid ISO 26262 system design - • Safety Manual - • Functional Safety Analysis Report - - Systematic capability up to ASIL-D - - Hardware capability up to ASIL-D - • Automatic wake up of BMS/BMU system when fault is detected in ring architecture - • Support supply from 4.75-V to 40-V - • UART/SPI Host interface - • Compatible with 3.3-V/5-V logic - • Isolated differential daisy chain - - Support ring architecture with one device - - Support transformer/ capacitor isolation - • Designed for BCI/EMI/EMC robustness - • Supports BQ7961X-Q1 family, BQ7965X, BQ7963X and future products

## 2 Applications

- • Battery management system (BMS) - • Other HEV/EV - • Fuel cell - • Energy storage

## 3 Description

The BQ79600-Q1 is a communication (bridge) IC designed to interface between a microcontroller (MCU) and TI battery monitoring ICs, for example the BQ7961X-Q1. The information from the MCU is translated by the device to signals recognized by TI's battery management daisy chain protocol, and transmitted out. And signals from daisy chain are decoded to bit stream and then sent back to MCU.

When the MCU and PMIC are in SHUTDOWN/ SLEEP, the BQ79600-Q1 can wake them up if any unmasked fault is detected when using ring architecture. **Device Information**

# PART NUMBER (1) **PACKAGE** **BODY SIZE (NOM)**

BQ79600-Q1 TSSOP (16-pin) 6.6 mm \times 5.1 mm

(1) For all available packages, see the orderable addendum at the end of the data sheet.

# BQ796XX-Q1

# COML COMH

# BQ796XX-Q1 BQ796XX-Q1 BQ79600-Q1 UART /SPI

Balance and Filter Components Balance and Filter Components

# CAP

| COML | COMH |
|:--- |:--- |
| COML | COMH | **Transformer** **CAP or ** **Transfomer** Low Voltage Boundary

# VIO BAT 12V Battery

# INH Battery Battery

# NFAULT **Transformer** **CAP** **CAP or ** **Transfomer** **CAP or ** **Transfomer** **CAP or ** **Transfomer** BMU CMU CMU BMU isolation uC

# SBC (PMIC)

# EN

Optional: Ring Enables Fault and Reverse Wakeup Feature Battery Battery

Balance and Filter Components Balance and Filter Components

# BQ796XX-Q1

| COML | COMH |
|:--- |:--- |
| COML | COMH | **Simplified System Diagram** **<https://www.ti.com**>

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback*

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications, intellectual property matters and other important disclaimers. PRODUCTION DATA.

## Table of Contents

**1 Features**............................................................................ 1 **2 Applications**..................................................................... 1 **3 Description**....................................................................... 1 **4 Revision History**.............................................................. 2 **5 Pin Configuration and Functions**................................... 3

Pin Functions.................................................................... 3 **6 Specifications**.................................................................. 4

6.1 Absolute Maximum Ratings....................................... 4 6.2 ESD Ratings.............................................................. 4 6.3 Recommended Operating Conditions........................ 4 6.4 Thermal Information................................................... 4 6.5 Electrical Characteristics............................................ 5 6.6 Timing Requirements................................................. 6 6.7 Typical Characteristics................................................ 9 **7 Detailed Description**...................................................... 10

7.1 Overview................................................................... 10 7.2 Functional Block Diagram......................................... 10 7.3 Feature Description................................................... 10 7.4 Device Functional Modes.......................................... 36

7.5 Register Maps........................................................... 37 **8 Application and Implementation**.................................. 55

8.1 Application Information............................................. 55 8.2 Typical Applications.................................................. 55 **9 Power Supply Recommendations**................................ 59 **10 Layout**........................................................................... 60

10.1 Layout Guidelines................................................... 60 10.2 Layout Example...................................................... 60 **11 Device and Documentation Support**.......................... 63

11.1 Device Support........................................................ 63 11.2 Third-Party Products Disclaimer............................. 63 11.3 Receiving Notification of Documentation Updates.. 63 11.4 Support Resources................................................. 63 11.5 Trademarks............................................................. 63 11.6 Electrostatic Discharge Caution.............................. 63 11.7 Glossary.................................................................. 63 **12 Mechanical, Packaging, and Orderable** **Information**.................................................................... 64

## 4 Revision History

**Changes from Revision \* (November 2019) to Revision A (June 2020)** **Page** - • Changed from Advance Information to Production Data.................................................................................... 1

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2020 Texas Instruments Incorporated

## 5 Pin Configuration and Functions

# BAT

# COMLN

# COMHP

# COMLP

# NFAULT

# VIO CVDD

# nUART/SPI (SPI\_RDY)

# 16-TSSOP nCS

# MOSI/RX MISO/TX 5.1x6.6x1.2(mm) No thermal pad

# DVDD INH

# GND

# SCLK

# COMHN

## Figure 5-1. PW Package 16-Pin TSSOP Top View

## Pin Functions

# PIN

# TYPE (1) **DESCRIPTION** **NAME** **NO.**

VIO P Power supply input for UART/SPI input/output pins. Decouple with a 0.1μF capacitor to GND. VIO should be powered before SCLK, nCS, RX/MOSI, TX/MISO, NFAULT, nUART/SPI (SPI\_RDY) is driven.

| SCLK | DI | SPI clock input. If SPI interface is used, this pin is connected to SPI master controller. Connect | to GND with a 10-100kohm pull-down resistor. If not used, connect to GND. |
|:--- |:--- |:--- |:--- |
| nCS | DI | Active low chip select pin for SPI interface. Connect to VIO with 10-100kohm pull-up resistor in | SPI mode. Cannot hardwire to GND in SPI mode. Connect to GND in UART mode. |
| RX/MOSI | DI | UART receiver input or SPI master out slave in. Connect to VIO with a 10-100kohm pull-up | resistor. Don't leave it unconnected. |

nCS DI Active low chip select pin for SPI interface. Connect to VIO with 10-100kohm pull-up resistor in SPI mode. Cannot hardwire to GND in SPI mode. Connect to GND in UART mode.

RX/MOSI DI UART receiver input or SPI master out slave in. Connect to VIO with a 10-100kohm pull-up resistor. Don't leave it unconnected.

TX/MISO DO UART transmitter output or SPI master in slave out. Pull up to VIO with a 10-100kohm pull-up resistor at MCU side. MISO pin drives high in SPI idle mode, cannot directly support SPI multidrop, if multidrop is needed, add a tri-state buffer between BQ79600-Q1 and MCU.

NFAULT DO Fault indication output. Open drain active low. Pull up to VIO with 100kohm resistor. Connect NFAULT to host MCU GPIO. If not used, connect to GND.

# nUART/SPI (SPI\_RDY)

DI/O If used as UART mode, connect this pin to GND. If used as SPI mode, connect to VIO through 10-100kohm pull up resistor and connect this pin to MCU GPIO. This pin is used as an input pin to select SPI or UART interface before device finishes wakeup/reset initialization (SPI communication is ready). If SPI mode is selected, SPI\_RDY has to be used by host to decide if read/write can be initiated or needing further wait. Refer to Section 7.3.2.1.2.2.1 details.

DVDD P 1.8V regulated output. DVDD supplies the internal digital circuits. Bypass DVDD with a 0.22μF (recommended) or a 0.47μF capacitor to GND. GND P Ground.

CVDD P Dedicated 5V supply used for the daisy chain communications. Decouple with a 0.22μF (recommended) or a 0.47μF to GND.

COMHN AC-I/O This is an AC coupled bi-directional I/O pin for daisy chain (VIF) communication. Do not apply external DC voltage to this pin. Shall connect to COMLN/P of adjacent device through proper isolation, see Section 7.3.2.1.1. Leave unconnected if (Ring Architecture) not used. COMHP AC-I/O

COMLN AC-I/O This is an AC coupled bi-directional I/O pin for daisy chain (VIF) communication. Do not apply external DC voltage to this pin. Shall connect to COMHN/P of adjacent device through proper isolation, see Section 7.3.2.1.1. Leave unconnected if (Ring Architecture) not used. COMLP AC-I/O

INH HV-O Inhibit pin (PMOS open drain) to control system voltage regulators, connect 100kohm resistor to GND. If reverse wake up feature is not used, connect this pin to BAT pin. Don't leave this pin floating.

BAT HV-P Battery supply Input. Supply internal LDOs and wakeup circuit. Connect to external supply through 10ohm resistor. Bypass to GND with 0.1μF.

(1) DI = digital input, DO = digital output, HV = high voltage **<https://www.ti.com**>

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback*

## 6 Specifications

**6.1 Absolute Maximum Ratings** over operating free-air temperature range (unless otherwise noted) (1)

# MIN **MAX** **UNIT** Input Voltage

# BAT to GND -0.3 V INH to GND (INH is lower than BAT) -0.3 V

# VIO, CVDD to GND -0.3 5.5 V

# DVDD to GND -0.3 1.98 V

# MISO/TX, MOSI/RX, nCS, SCLK, NFAULT, nUART/SPI(SPI\_RDY) to GND -0.3 VIO+0.3 V

# COMHP, COMHN, COMLP, COMLN to GND V

# COMHP to COMHN, COMLP to COMLN -6.5 6.5 V INH current mA

I/O current MISO/TX current (100pF load, VIO=5V, 10ns transition-time) mA

| TA | Ambient temperature | -40 | °C |
|:--- |:--- |:--- |:--- |
| TJ | Junction temperature | -40 | °C |
| Tstg | Storage temperature | -65 | °C | T J Junction temperature °C T stg Storage temperature °C

(1) Stresses beyond those listed under Absolute Maximum Rating may caµse permanent damage to the device. These are stress ratings only, which do not imply functional operation of the device at these or any other conditions beyond those indicated under Recommended Operating Condition. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability.

## 6.2 ESD Ratings

| VALUE | UNIT |
|:--- |:--- |
| V(ESD) | Electrostatic discharge |
| Human body model (HBM), per AEC Q100-002(1) | ±2000 | V (ESD) Electrostatic discharge

Human body model (HBM), per AEC Q100-002 (1) \pm2000

V Charged device model (CDM), per AEC Q100-011 Corner pins (1, 8, 9 and 16) \pm750 Other pins \pm500

(1) AEC Q100-002 indicates that HBM stressing shall be in accordance with the ANSI/ESDA/JEDEC JS-001 specification.

## 6.3 Recommended Operating Conditions

over operating free-air temperature range (unless otherwise noted)

# MIN **TYP** **MAX** **UNIT**

V BAT, INH BAT, INH (INH is equal to or lower than BAT) (Powered by 12V Battery) 5.5 V

# V VIO\_RANGE VIO input (applies to nCS, MOSI/RX, MISO/TX, SLCK, nUART/SPI (SPI\_RDY), NFAULT) 3.135 5.25 V I MISO/TX MISO/TX current mA I INH INH output current mA T A Operation temperature °C

## 6.4 Thermal Information

# THERMAL METRIC (1)

# BQ79600-Q1

# UNIT **PW(TSSOP)**

# 16 PINS

R\thetaJA Junction-to-ambient thermal resistance °C/W

R\thetaJC(top) Junction-to-case (top) thermal resistance 28.9 °C/W

| RθJB | Junction-to-board thermal resistance | °C/W |
|:--- |:--- |:--- |
| ΨJT | Junction-to-top characterization parameter | °C/W |
| BQ79600-Q1 | SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 | www.ti.com |

\PsiJT Junction-to-top characterization parameter °C/W

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2020 Texas Instruments Incorporated

# THERMAL METRIC (1)

# BQ79600-Q1

# UNIT **PW(TSSOP)**

# 16 PINS

\PsiJB Junction-to-board characterization parameter 48.2 °C/W

(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application report.

## 6.5 Electrical Characteristics

VIO = 3.3V, over operating free-air temperature range (unless otherwise noted)

# PARAMETER

**TEST CONDITIONS** **MIN** **TYP** **MAX** **UNIT**

# OPERATION VOLTAGE

V BAT When reverse wakeup feature is used, BAT pin is powered by "12V battery" 5.5 V

# V BAT

When reverse wakeup feature is not used, BAT/CVDD are powered by regulated 5V

# 4.75 5.25 V

# THERMAL SHUTDOWN

T SHUT\_R Thermal shutdown (rising direction) DieTemp sensor °C

T SHUT\_F Thermal shutdown (falling direction) DieTemp sensor °C

# SUPPLY CURRENTS

# I SHDN\_1

Supply current in SHUTDOWN mode device powered by regulated 5V supply

VBAT shorted to CVDD, both equal to 5V, measured through GND pin µA

# I SHDN\_2

Supply current in SHUTDOWN mode powered by "12V" battery directly

VBAT= 17V, CVDD self powered, measured through GND pin µA

I VALIDATE Supply current in VALIDATE mode Current on BAT pin µA

I SLP(IDLE) Baseline supply current in SLEEP mode Current on BAT pin, no fault, COMH and COML RX disabled, no HB TX µA

# I SLP\_RX\_O

# N

Additional supply current to SLEEP mode base line When COML OR COMH RX is on µA

# I SLP\_TX\_O

# N

Additional supply current to SLEEP mode base line

When COML or COMH tone transmiter is on (HB tone) µA

I ACT(IDLE) Baseline supply current in ACTIVE mode Current on BAT pin,  no fault, no communication, Tone RX/TX is off mA

I COMT Additional average current for one of BQ79600 daisy chain transmitters is on

Average current into VBAT when BQ79600 transmits 14 bytes of data (brdcast write 8 bytes of 0x00 into address 0X1B) mA

**Supplies (AVAO\_REF, always on internal supply)**

# V AVAORE

# G AVAOREG voltage VBAT \> min VBAT 2.45 V

# V AVDDREF

# \_OV

AVDDREF OV threshold VBAT \> min VBAT, hys = 130mV 2.8 3.1 V **Supplies (CVDD)**

V CVDD CVDD output voltage No external load, C SUPPLIES = 0.22µF, ACTIVE mode 4.9 5.1 V

# V CVDD\_O

# V

CVDD OV rising threshold $$ Hys = 140mV $$ 5.3 5.5 5.65 V

# V CVDD\_U

# V\_F CVDD UV falling threshold 4.35 4.5 4.65 V

# V CVDD\_U

# V\_R CVDD UV rising threshold 4.45 4.6 4.75 V

# V CVDD\_ILI

# MIT CVDD current limit mA

C CVDD Capacitance range on CVDD pin Not capacitor value 0.1 0.8 µF **<https://www.ti.com**>

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback*

## VIO = 3.3V, over operating free-air temperature range (unless otherwise noted)

# PARAMETER

**TEST CONDITIONS** **MIN** **TYP** **MAX** **UNIT** **Supplies (DVDD)**

V DVDD DVDD output voltage No external load, C SUPPLIES = 0.22µF, ACTIVE mode 1.75 1.8 1.85 V

# V DVDD\_O

V DVDD OV rising threshold Hys = 65mV 1.9 2.1 V

# V DVDD\_U V\_F DVDD UV falling threshold 1.63 1.69 V

# V DVDD\_U V\_R DVDD UV rising threshold 1.68 1.75 V

# V DVDD\_ILI MIT DVDD current limit mA

D DVDD Load capacitance on DVDD pin Not capacitor value 0.1 0.8 µF

# SNIFF DETECTOR

# V VAL\_THR

# \_P

Sniffer detector threshold,  rising swing on COMHP has to be larger than value

Sniffer is enabled, and device is in SHUTDOWN mode 3.2 3.6 V **INH Driver**

# V DROP\_IN

# H

When INH is pulled up, voltage drop from BAT to INH IINH = -0.5mA 0.5 V

V INH\_DET Threshold to set \[INH\_STAT\] to '1' 2.2 V **Reference Voltages** **Digital I/Os (TX, RX, NFAULT)**

# V VIO\_UV\_ R VIO UV rising $$ Hys = 200mV $$ 2.5 3.1 V

V OH Output as logic level high (TX) FET pull up, Iout=1mA, VIO = 3.3V or 5V V VIO -0.1 V

V OL Output as logic level low (TX) FET pull down, Iout=1mA, VIO = 3.3V or 5V 0.1 V

# V IH

Input as logic level high (RX), requirement for user VIO = 3.3V or 5V 0.75 x V VIO V

# V IL

Input as logic level low (RX), requirement for user VIO = 3.3V or 5V 0.25 x V VIO V

R NFAULT NFAULT pull down impedance Use 100kohm external pull up \Omega **Daisy-chain Communication Bus**

# V DCCM\_1

Common mode voltage (COML and COMH) ACTIVE mode 2.2 V

# V DCCM\_2

Common mode voltage (COML and COMH) SLEEP or VALIDATE mode V

# V COMM\_D

# ATA

COMM port data receiver threshold range (V COMP -V COMN ) 1.04 1.75 V

# V COMM\_T

# ONE

COMM port HB/FAULT tone receiver threshold range (V COMP -V COMN ) 1.13 1.94 V

## 6.6 Timing Requirements

over operating free-air temperature range (unless otherwise noted)

# PARAMETER

**TEST CONDITIONS** **MIN** **TYP** **MAX** **UNIT**

# POWER STATE TIMING

# t POR2COM

# M

From V BAT (rising) \> V POR to device ready to receive WAKE ping, ramp up VBAT and VIO in 10µs ms

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2020 Texas Instruments Incorporated

## over operating free-air temperature range (unless otherwise noted)

# PARAMETER

**TEST CONDITIONS** **MIN** **TYP** **MAX** **UNIT**

# t SU(WAKE\_

# SHUT) Startup from SHUTDOWN/VALIDATE to ACTIVE mode

From receiving WAKE ping (RX ping going low-to-high) to device in ACTIVE mode (ready to do µART /SPI communication) (CVDD= 0.22µF capacitor DVDD = 0.22µF capacitor) 3.5 ms

# t SU(SLP2A

# CT)

Startup from SLEEP to ACTIVE mode (with Sleep2active ping)

From receiving SLP2ACT ping (RX ping going low-to-high) to device in ACTIVE mode (ready to do UART / SPIcommunication) µs

# t SU(WAKE\_

# SLP)

Startup from SLEEP to ACTIVE mode (with WAKE ping)

From receiving WAKE ping (RX ping going low-to-high) to device in ACTIVE mode (ready to do UART / SPIcommunication) µs

# t RST Reset time from ACTIVE mode to ACTIVE mode

From receiving WAKE ping (RX ping going low-to-high) or CONTROL1\[SOFT\_RESET\]=1 to device in ACTIVE mode (ready to do UART /SPI communication) µs

t SLP From ACTIVE to SLEEP mode From receiving SLEEP entry condition to enter in SLEEP mode µs

# t SHTDN From ACTIVE/SLEEP/VALIDATE to SHUTDOWN mode

From receiving SHUTDOWN entry condition to enter in SHUTDOWN mode (CVDD<1.2V) ms

# t VALID\_EN

TRY From SHUTDOWN to VALIDATE From fault tone toggling on COM port to DVDD hit above 1.75V ms

# t VALID\_TIM

# EOUT

time to validate fault tone before transition to SHUTDOWN state Start from DVDD out of reset ms **INH Driver TIMING**

# t INH\_DLY

After device enters VALIDATE, from first couplet of fault tone to INH pulled high µs

# PING SIGNAL TIMING

# t HLD\_WAK

# E

From user perspective, WAKE ping low time on MOSI/RX pin

VBAT \> VPOR, RX pin (low-pulse width) VIO = 3.3 or 5V 2.5 ms

# t HLD\_SD

From user perspective, SHUTDOWN ping low time on MOSI/RX pin

VBAT \> VPOR, RX pin (low-pulse width) VIO = 3.3 or 5V 12.5 ms t StA

From user perspective, SLEEPtoACTIVE ping low time on MOSI/RX pin VBAT \> VPOR µs **Daisy-chain Communication Bus TIMING**

# t PW\_DC

COMM data Pulse width of data (half bit time) for communiction ns

# t COMTONE

Time between pulses within a comm tone (HFO based).

Transmit. From the beginning of a pulse until the beginning of the next pulse. 10.67 11.33 µs

# t COMTONE

# \_PLS

Comm tone pulse width(HFO based) Transmit 0.97 1.03 µs

# t FLTTONE

Time between pulses within a fault tone (LFO based).

Only transmit HB tone, not FAULT tone. From the beginning of a pulse until the beginning of the next pulse. 10.3 11.5 12.7 µs

# t FLTTONE\_

# PLS

Fault tone or HB tone pulse width (analog delay based) µs

# n HBDET

HEARTBEAT: Number of pulses to detect as a valid tone (dig counter) Detect pulses

# n FTONEDE

# T

FAULT TONE: Number of pulses to detect as a valid tone  (dig counter) Detect pulses **<https://www.ti.com**>

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback*

## over operating free-air temperature range (unless otherwise noted)

# PARAMETER

**TEST CONDITIONS** **MIN** **TYP** **MAX** **UNIT**

# t HB\_PERIO

# D

HEARTBEAT: Period between HEARTBEAT Burst (from the beginning of a HEARTBEAT to the beginning of the next HEARTBEAT) ms

# t HB\_TIMEO

# UT

HEARTBEAT: Timeout to considered as not receving HEARTBEAT 0.9 1.1 s

# t HB\_FAST

HEARTBEAT: If HEARTBEAT is received within this time, it is considered receving HEARTBEAT too fast ms

# t FTONE\_PE

# RIOD

Defined by BQ7961X, FAULT TONE: Period between FAULT TONE Burst

From the beginning of a FAULT TONE to the beginning of the next FAULT TONE ms

# t FT\_LATEN

CY Fault Tone latency in Base Device From the time device receives the tone to the time asserts NFAULT µs

# I/O TIMING (TX, RX, NFAULT)

t RISE\_TX Rise Time CLOAD = 100pF, VIO=3.3V or 5V ns

t FALL\_TX Fall Time CLOAD = 100pF, VIO=3.3V or 5V ns

# t FALL/ RISE\_RX RX pin rise/fall time ns

# UART TIMING

# UARTER R\_BAUD

UART TX/RX baud rate (either 250K or 1Mbps) error -1.5 1.5 %

# t UART(CLR ) UART Comm Clear low time 20 bit period

# t UART(RX\_

# HIGH)

UART high time after Comm Clear, before sending Clear or Reset bit period

# SPI TIMING SCLK SPI clock freq MHz n SPI(CLR) SPI Comm Clear low time bit t SPI\_R SPI clock rising edge 25% to 75% ns t SPI\_F SPI clock falling edge 25% to 75% ns t SPI\_CLKH SPI clock high time ns t SPI\_CLKL SPI clock low time ns t 8

Max SPI\_RDY service interval. This time doesn't apply if total response bytes (payload + overhead) is less than 256 bytes

| Read SCLK = 6MHz, with 30% SPI BUS | idle time | ms |
|:--- |:--- |:--- |
| t9 | From nCS (25%) to SCLK rising (75%) | ns |
| t10 | From SCLK falling (25%) to nCS (75%) | ns | t 9 From nCS (25%) to SCLK rising (75%) ns t 10 From SCLK falling (25%) to nCS (75%) ns t 11

From nCS rising(75%) to nCS falling(25%) Don't drop nCS while SPI\_RDY is low µs t 12

From nCS falling (25%) to stable MISO(L:20% H:80%)

Timing is defined at device pins, exclude propergation delay of PCB traces (from device perspective) ns t 13

From SCLK falling (25%) to stable MISO(L:20% H:80%)

Timing is defined at device pins, exclude propergation delay of PCB traces (from device perspective) ns t 14

From nCS rising (75%) to MISO drive to '1' (80%)

Timing is defined at device pins, exclude propergation delay of PCB traces (from device perspective) ns

t SU Setup time, refer to 75% of SCLK rising ns t H Hold time, refer to 75% of SCLK rising ns

# SNIFF DETECTOR

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2020 Texas Instruments Incorporated

## over operating free-air temperature range (unless otherwise noted)

# PARAMETER

**TEST CONDITIONS** **MIN** **TYP** **MAX** **UNIT**

# n VALIDATE

Number of pulses needed (digital counter) to transition to validate mode

Sniffer is enabled, and device is in SHUTDOWN mode pulses

t SNIFFIDLE Timer length. Once timer expired, it resets the 64 counter

Sniffer is enabled, and device is in SHUTDOWN mode µs

# OSCILLATOR

| fHFO | HFO frequency | 31.52 | 32.48 | MHz |
|:--- |:--- |:--- |:--- |:--- |
| tHFOWDG | HFO watchdog time | Reset digital if HFO is stuck or period is \> | than the watchdog timer | µs |
| fLFO | LFO frequency | 235.8 | 288.2 | kHz |
| tLFOWDG | LFO watchdog time | Reset digital if LFO is stuck or period is \> | than the watchdog timer | µs |

t HFOWDG HFO watchdog time Reset digital if HFO is stuck or period is \> than the watchdog timer µs f LFO LFO frequency 235.8 288.2 kHz

t LFOWDG LFO watchdog time Reset digital if LFO is stuck or period is \> than the watchdog timer µs

## 6.7 Typical Characteristics

## Figure 6-1. Typical COMHN and COMHP characteristic **<https://www.ti.com**>

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback*

## 7 Detailed Description **7.1 Overview**

The BQ79600-Q1 is a bridge IC designed to interface between microcontroller (MCU) and TI battery monitoring ICs (BQ7961X-Q1 family). It translates between daisy chain interface and SPI/UART interface. It is fully compatible with BQ7961X-Q1 family. When working with BQ7961X-Q1 family, BQ79600-Q1 supports automatic host wakeup through INH pin when unmask fault is detected in high voltage battery pack. Details can be found in Section 7.3.5 and Section 7.3.4. For convenience of traceability, each device is marked by DIE IDs and PARTID which could be found in Section 7.5 Register Summary Table. **7.2 Functional Block Diagram**

# DVDD **Digital** **Core**

# COMHP **COMHN** **COMLP**

# GND **Ping ** **Detect**

# COMLN **REFSYS/** **Powermode ** **Control**

# BAT **Daisy Chain  **

# INH

# CVDD

# nUART/SPI (SPI\_RDY)

# NFAULT

# VIO

# MISO/TX **MOSI/RX**

# SCLK **nCS**

# DVDD **Push-Pull GPIOs**

# VIO

# OSC **32MHz** **262KHz**

# AVAOREF

# AVDDREF

# CVDD

# TX

# RX

# TX

# DVDD

# RX **Figure 7-1. Functional Block Diagram** **7.3 Feature Description**

**7.3.1 Functional Modes and Power Supply** ***7.3.1.1 Power Mode***

The device has four power modes plus an Complete Off state. The functions supported under each power modes are summarized in Table 7-1 and the power state diagram is shown in Figure 7-2.

- **• COMPLETE OFF**: The voltage at the BAT pin is less than V BAT min, and all circuits are powered off. - **• SHUTDOWN**: The lowest power mode. Without VIO, device can only transition to VALIDATE. (If Sniffer used) - **• SLEEP**: A low power mode. Transition to ACTIVE is much faster compared to SHUTDOWN. - **• ACTIVE**: Full power mode. Device can communicate between MCU and daisy chain. - **• VALIDATE**: This state is to validate if there is real fault tone from stack devices. If fault tone is validated, drive INH pin towards VBAT (INH pin is latched until cleared by user). Device goes back to SHUTDOWN if t VALID\_TIMEOUT or sleep timer expires. (t VALID\_TIMEOUT timer is reset if fault tone is detected, detecting Heartbeat tone doesn't reset timer.) This state is bypassed if Section 7.3.5 is disabled (by default). Once entered this state, a status bit \[VALIDATE\_DET\] is set in next ACTIVE such that host knows what happened. Without VIO, device can only transition to SHUTDOWN. NFAULT pin is low in this mode.

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2020 Texas Instruments Incorporated

## Table 7-1. Functions Summary

# FUNCTIONAL BLOCK (1)

**SHUTDOWN** **VALIDATE** **(3)** **SLEEP** **ACTIVE** Data Communication RX/TX If VIO_UV_R = 1

Time out Sleep Timeout Sleep Timeout Comm Timeout

| Tone RX (HB/Fault) | √ | Depends on \[DIR\_SEL\] and \[TONE\_RX\_EN\] |
|:--- |:--- |:--- |
| Tone TX (WAKE/ SLP2ACT/ | SHUTDOWN/ HWRST) (5) | √ |
| Tone TX (HB) | Depends on \[DIR\_SEL\] | and \[HB\_TX\_EN\] |

# Tone TX (WAKE/ SLP2ACT/ SHUTDOWN/ HWRST) (5) √

Tone TX (HB) Depends on \[DIR\_SEL\] and \[HB\_TX\_EN\] COM embedded fault $$ [FCOMM_EN] =1 $$

Sniff detector on COM\* If host enables this feature (2)

Wake/Shutdown Ping If VIO_UV_R = 1 If VIO_UV_R = 1 If VIO_UV_R = 1 If VIO_UV_R = 1

# SLP2ACT Ping √ NFAULT Driver √ √ √

# LFO √ √ √

# HFO √

INH Driver Holds State √ $$ INH_DIS[1:0]!= 2'b11 $$ $$ INH_DIS[1:0]!= 2'b11(4) $$

# CVDD/DVDD √ √ √ Thermal Shutdown √ √ √

(1) Once device in SLEEP/ACTIVE, losing VIO doesn't directly cause change of state, it causes loss of data communication to MCU. (2) If host writes \[SNIFDET\_EN\] =1 & \[SNIFDET\_DIS\] = 0 in ACTIVE mode, even device shuts down, enable signal is still valid. Sniff detector is enabled or disabled by a latch powered by always on power supply. (3) This mode is bypassed if sniff detector is not enabled, see register DEV\_CONF1. (4) INH can only be triggered by \[INH\_SET\_GO\] bit in ACTIVE. (5) Device does not recognize WAKE/ SLP2ACT/ SHUTDOWN/ HWRST tone sent by stack devices.

# ACTIVE MODE

# SLEEP MODE

# SHUTDOWN MODE

1. Set * CONTROL1\[GOTO\_SLEEP\]* = 1, OR 2. Long comm timeout occurs w/  COMM_TIMEOUT[CTL_ACT] = 0

1. Thermal shutdown, OR 2. Long comm timeout occurs w/  *COMM\_TIMEOUT\[CTL\_ACT\] * = 1, OR 3. Receive SHUTDOWN Ping, OR 4. Set * CONTROL1\[GOTO\_SHTUTDOWN\]* = 1 Device reset

1. Receive WAKE Ping, OR 2. Set CONTROL1[SOFT_RESET] = 1

1. SleeptoActive Ping, OR 2. Receive WAKE Ping Wake Ping **VALIDATE MODE** **(bypassed by default)** SNIFF Det = 1 if enabled

1. Thermal shutdown, OR 2. SHUTDOWN Ping, OR 3. Sleep timer expires

# COMPLETE OFF Wake Ping

# BAT \> Min V BAT BAT \< Min V BAT

# BAT \< Min V BAT 1. Thermal shutdown, OR 2. SHUTDOWN Ping, OR

3. t VALID\_TIMEOUT expires, OR 4. Sleep timer expires

## Figure 7-2. Power State Diagram **<https://www.ti.com**>

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback*

## 7.3.1.2 Pings

## A "ping" is a specific signal pattern to change power mode of BQ79600-Q1. There are total of 3 different pings

# HLD\_WAKE

# RX

# HLD\_SD StA 1us: 1Mbps(default) 4us: 250Kbps **UART mode** Hardwired to GND **WAKE Ping ** **high-low-high **

# HLD\_WAKE

# MOSI **SHUTDOWN Ping ** **high-low-high **

# HLD\_SD **SLEEPtoACTIVE Ping  ** **high-low** StA nCS timing follows SPI physical layer requirement

**SPI mode (see notes below for SCLK control)** nCS

# RX

# RX

# MOSI

# MOSI

## Figure 7-3. Communication Pings

## • • In SPI mode, ping can be sent without SCLK toggling or host can treat sending a ping like sending a series of

logic '0' (drive nCS and SCLK properly, refer to SPI physical layer requirement, Section 7.3.2.1.2.2 ). - • Device does not transmit any tones to stack devices due to the receiving of pings. - • After sending in SHUTDOWN ping, host has to wait t SHTDN before sending another ping. - • If nCS = '1', all of the pings above are ignored by the device.

## Note

## If device is shut down through SHUTDOWN ping (COMH RX and COML RX are disabled at next

wake up), host needs to send 1 st WAKE ping, wait t SU(WAKE\_SHUT), and then send 2 nd WAKE ping.

## Table 7-2. Device Behavior when SLP2ACT Ping is Sent

# UART

**SPI WITH SCLK TOGGLING** **SPI WITHOUT SCLK TOGGLING**

# ACTIVE

[COMMCLR_DET]=1, [STOP_DET] =1 [COMCLR_ERR]=1, [COMMCLR_DET]=0

# \[FMT\_ERR\]=1, \[COMCLR\_ERR\]=0, [COMMCLR_DET]=0

| SLEEP | \[COMMCLR\_DET\]=1, \[STOP\_DET\] =0, | transitions to active mode |
|:--- |:--- |:--- |
| \[COMCLR\_ERR\]=0, | \[COMMCLR\_DET\]=0, transitions to | active mode |
| \[FMT\_ERR\]=0, \[COMCLR\_ERR\]=0, | \[COMMCLR\_DET\]=0, transitions to active | mode |

[COMCLR_ERR]=0, \[COMMCLR\_DET\]=0, transitions to active mode

[FMT_ERR]=0, [COMCLR_ERR]=0, \[COMMCLR\_DET\]=0, transitions to active mode

## 7.3.1.3 SPI/UART Selection

## The SPI or UART interface is selected through hardware: connect pin nUART/SPI to VIO through resistor for SPI

or connect to GND for UART. Device determines UART or SPI mode every time it transitions from SHUTDOWN to ACTIVE mode. Before transitioning to ACTIVE, the mode selected is locked in. VIO has to be above V VIO\_UV\_R. nUART/SPI pin is used as output indication of SPI\_RDY once in ACTIVE mode. See Section 7.3.2.1.2.2.1 for more information.

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2020 Texas Instruments Incorporated

## 7.3.1.4 Digital Reset

## Digital reset is when digital core of the device in reset mode. It is not a power mode. Once device comes out of

digital reset, \[DRST\] bit is set to '1', registers that are not included in NVM are set to RESET VALUE, registers included in NVM would be NVM program value. There are several conditions in which the device will go through a digital reset: - • A WAKE ping is received. - • The CONTROL1 \[SOFT\_RESET\] = 1 command is sent in ACTIVE mode. - • Power supply faults. DVDD UV or CVDD UV is detected. - • A HFO or LFO watchdog fault will reset the digital.

## 7.3.1.5 Power Mode in BMS System

## It is recommended to follow the power state combinations below to save system level power.

## Table 7-3. Power Mode Combination Summary

| STACK MONITORING IC | BQ79600-Q1 | COMMENT |
|:--- |:--- |:--- |
| ACTIVE | ACTIVE | Recommended |
| SLEEP | SLEEP | Recommended |
| SLEEP | SHUTDOWN | Recommended |
| SHUTDOWN | SHUTDOWN | Recommended | ACTIVE ACTIVE Recommended SLEEP SLEEP Recommended SLEEP SHUTDOWN Recommended SHUTDOWN SHUTDOWN Recommended Other combinations Not recommended

## 7.3.1.6 Power Supply

## This section provides an overview of each supplies for both user cases: without using Reverse Wakeup and with

using Reverse Wakeup. See the Section 7.3.6 for diagnostic control and fault detection on the power supplies block.

## Table 7-4. Power Supply Summary

# NAME

**W/O REVERSE WAKEUP USER CASE** **W/ REVERSE WAKEUP USER CASE**

VIO This supply is powered by regulated 3.3V or 5V from SBC (PMIC), it powers UART/SPI interface pins.

| BAT | This supply is powered by regulated 5V from SBC (PMIC). | This supply is powered by unregulated 12V battery. |
|:--- |:--- |:--- |
| AVAOREF | This supply is generated from VBAT. It is always on if VBAT exists. It powers REFSYS and Power mode control | block. |
| AVDDREF | This supply is derived from AVAOREF. AVDDREF and AVAOREF are connected by a switch, the switch is open in | SHUTDOWN mode. |
| DVDD | This supply is generated by the internal DVDD LDO. It is the supply for the digital circuits. It takes the input voltage | from CVDD and generates a nominal 1.8V. It will not be used to power any external circuit. |
| CVDD | This supply is powered by regulated 5V from SBC(PMIC). It | is the supply for daisy chain interface. |

AVAOREF This supply is generated from VBAT. It is always on if VBAT exists. It powers REFSYS and Power mode control block.

AVDDREF This supply is derived from AVAOREF. AVDDREF and AVAOREF are connected by a switch, the switch is open in SHUTDOWN mode.

DVDD This supply is generated by the internal DVDD LDO. It is the supply for the digital circuits. It takes the input voltage from CVDD and generates a nominal 1.8V. It will not be used to power any external circuit.

CVDD This supply is powered by regulated 5V from SBC(PMIC). It is the supply for daisy chain interface.

This supply is generated by the internal CVDD LDO. It is the supply for the daisy chain interface (or vertical interface, VIF). It takes the input voltage from VBAT and generates a nominal 5V. It will not be used to power any external circuit.

## 7.3.1.7 Shutdown

## Power Mode Transition Example **<https://www.ti.com**>

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback*

# BAT

# AVAOREF

# VIO

# CVDD

# DVDD

# Min V BAT

# SHUTDOWN **ACTIVE ** **Received WAKE ping** **Communication ** **Ready** **time**

# POR2COMM

# SU(WAKE\_SHUT) **Transition**

# SU(SLP2ACT)/ **SU(WAKE\_SLP)** **Transition to Sleep mode**

# AVDDREF **Sleep** **ACTIVE ** **Transition to Active mode**

# SLP **Transition** **Transition** **Complete Off** **Transition**

# VIO\_UVZ

**VIO ramp time is system dependent and not specified**

## Figure 7-4. Shutdown -\> Active -\> Sleep -\> Active

# BAT

# AVAOREF

# VIO

# CVDD

# DVDD

# Min V BAT

# SHUTDOWN **VALIDATE** **Transition Detected ** **on COMM PORT** **time**

# POR2COMM

# VALID\_ENTRY **Transition** **Received WAKE Ping**

# AVDDREF **Transition** **Complete Off** **Transition**

# ACTIVE

# INH\_DLY **INH enables PMIC ** **which enables VIO** **Depend on system**

# INH **SNIF\_DET** **(internal signal)**

**Transition to Active then to Validate ** **as a status bit indicates device wakes ** **up due to SNIF\_DET** **SPI(UART) communication ** **Ready**

**FTONE\_PERIOD** **Fault tones from ** **stack device** **on COMM\* pins**

# FTONE\_PERIOD

## Figure 7-5. Shutdown -\> Validate -\> Active

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2020 Texas Instruments Incorporated

## 7.3.2 Communication

## This device is used as a bridge (base) device in daisy chain configuration, as showed in figure below. It

communicates with MCU through UART or SPI and communicates with stack devices through daisy chain (proprietary interface). MCU always initiates communication with a Command frame. In the system, BQ devices would never send data back to MCU before MCU requests. And MCU needs to wait all expected response frames before sending next command frame. Thus, communication scenarios can be put into 2 categories: - • MCU sends Write Command frames to BQ devices. Write Command frames don't incur Response frame. - • MCU sends one Read Command frame to BQ devices and waits till all Response frames are received. Command Frame Response Frame

Both Command and Response Frames shall follow the ** Transaction Frame Structure** Half-duplex **SPI or UART** BQ79600 (Base Device) MCU

# MOSI/RX MISO/TX COM Command Frame Response Frame BQ796XX monitoring IC (Stack 1) COM

Half-duplex (Asynchronous proprietary protocol ) SCLK zCS BQ796XX monitoring IC (Stack N) COM Command Frame Response Frame

# COM

Half-duplex (Asynchronous proprietary protocol )

# SPI\_RDY

## Address N Address 1 Address 0

## Figure 7-6. System Communication Diagram

## Rest of the section talks about how data and tone are communicated among host, bridge, and stack devices

Section 7.3.2.1 ( Section 7.3.2.1.1 and Section 7.3.2.1.2 protocol), Section 7.3.2.2. It also talks about Section 7.3.2.3 and Section 7.3.2.4.

## 7.3.2.1 Data Communication Protocol

## 7.3.2.1.1 Frame Layer

## The communication frame is defined in figure below. It is made up of 5 types of information: initialization

character (INIT), device address characters, register address character, data character(s) and CRC characters. Each character is transmitted at UART/ SPI/ Daisy Chain physical level, whose format is defined in following Section 7.3.2.1.2 section. There are 3 types of transaction frames: **Read Command Frames**, **Write Command** **Frames** and **Response Frames**. They follow the structure in the figure below.

# INIT \[7:0\]

**DEV ADR \[7:0\] ** **REG ADR \[15:0\] ** **DATA byte(s) ** **CRC \[15:0\] **

## Frames

**INIT ** **DEV ADR REG ADR ** **DATA ** **CRC ** Read Command Frame

Single Device Read Always 0x80 Y Y # of byte requested (max value 127, meaning 128)

# Y

Stack Read Always 0xA0 N Y Y Broadcast Read Always 0xC0 N Y Y Write Command Frame

Single Device Write Y Y Y Actual payload (1-8 bytes) Y Stack Write Y N Y Y Broadcast Write Y N Y Y Broadcast Write Reverse (5)

# Y (5) N Y (5) Y (5) Y

## Response Frame Y Y Y Actual payload (1-128 bytes) Y

## Figure 7-7. Command/Response Frame Structure

## Notes

- • When BQ79600-Q1 is used as bridge device, to read BQ devices information, host **SHALL NOT** use Broadcast Read command but only Single Device Read or Stack Read. The reason is BQ79600-Q1 register address does not overlap with stack devices, it would only return 0x00 to Broadcast Read command. - • For Stack Read command, the response is broken into individual response frames from each device addressed. Each device (address N) in the stack waits until the device above it (address N+1) responds before device N sends its own data back. - • After a read command frame is transmitted, the host must wait for all expected responses to return (or timeout: t WAIT\_READ\_MAX ) before initiating a new command frame. - • A response frame is not mandatary. A response frame is only received after a read command frame.

## www.ti.com

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

## Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback*

# • • Broadcast Write Reverse command frame should only be used to config \[DIR\_SEL\] bit, not for any other

purposes. INIT byte is 0xE0, Reg address byte is 0x309 (BQ7961X-Q1), data byte is 0x80. - • Bytes received on COMH/COML are NOT propagated up to the stack; while bytes received on the SPI/UART are propagated to COMH or COML depending on \[DIR\_SEL\]. - • Even if there is a byte error, data is still forwarded from VIF to SPI (buffer)/UART; if there is a byte error, data doesn't forward from SPI/UART to VIF. ** ** ** ** ** ** **Command/Response Frame ** ** ** **Bit ** **Bit Name ** **Description **

# DEV

# ADR

RSVD 6KRXOG DOZD\\VZULWH³´ RSVD 6KRXOG DOZD\\VZULWH³´ 5:0 Device Address Set the device address range from 0x00 to 0x3F ** ** ** ** ** ** **Command/Response Frame ** ** ** **Bit ** **Bit Name ** **Description **

# REG\_

# ADR 7:0 Register Address (MSB)

Target or beginning of the register address 7:0 Register Address (LSB) Target or beginning of the register address ** ** **Bit ** **Bit Name ** **Description **

# DATA 7:0 Data Byte\[0\] Data Byte\[0\] « «« «« 7:0 Data Byte \[n\] Data Byte\[n\]

** ** ** ** ** ** **Command Frame ** ** ** **Response Frame **

** ** **Bit ** **Bit Name ** **Description ** **Bit Name ** **Description **

# INIT

FRAME\_TYPE 1 =  Command Frame FRAME\_TYPE 0 = Response Frame REQ\_TYPE 000 = Single Device Read 001 = Single Device Write 010 = Stack Read 011 = Stack Write 100 = Broadcast Read 101 = Broadcast Write 110 = Broadcast Write Reverse $$ 111 = RSVD (1) $$

RESPONSE\_BYTE Number of the data bytes $$ 0x00 = 1 byte $$ $$ 0x01 = 2 bytes $$: $$ 0x7F = 128 bytes $$

RSVD RSVD. This bit is ignored DATA\_SIZE Number of data bytes, excluding device address, register address or CRC $$ 000 = 1 byte $$ $$ 001 = 2 bytes $$: $$ 111 = 8 bytes $$ ** ** ** ** ** ** **Command/Response Frame ** ** ** **Bit ** **Bit Name ** **Description **

# CRC

7:0 CRC (MSB) CRC-16-IBM polynomial (x 16 + x 15 + x 2 + 1 or 11000000000000101.  with 0xFFFF initialization 7:0 CRC (LSB) CRC-16-IBM polynomial (x 16 + x 15 + x 2 + 1 or 11000000000000101.  with 0xFFFF initialization

# Figure 7-8. Frame Byte Definition

# Notes

- • INIT character: (1) No function to this selection, but this selection sets the \[RC\_IERR\] error flag. - • Device Address character: Bit 6 and 7 are reserved; 0x4F to 0xFF is decoded as 0x3F by device. - • Register Address characters: Register addresses are two bytes in length. They indicate the targeted register address on a single byte read/write, or the beginning of the register address on a multi-byte read/write. If an invalid register address is set on a write command, the command will be ignored. If an invalid register address is set on a read command, a 0x00 will be returned as response. - • Data characters can be: - - Single data byte, it represents number of registers requested in Read Command Frame. The BQ79600Q1 supports up to 128 byte reads. The valid data byte for read command frame is 0b0000000 0b1111111. The MSB of the data byte is ignored for read command frames. For example, 0b10011001 is read as 0b00011001 and returns data from 26 registers. - - Actual payload in Write Command Frame (max 8 byte) or Response Frame (max 128 byte). - • CRC characters: - - The CRC value is checked as the first step (assume no physical layer error, no \[RC\_IERR\], no \[RC\_SOF\], no \[RC\_BYTE\_ERR\]) after receiving the communication frame. If the CRC is incorrect, the entire frame is discarded and not processed. Any additional frame errors are not checked. - - The frame with CRC error is still transferred up/down the stack. Every device processing this frame will also detect a CRC error. Hence, it is possible to have multiple devices indicating CRC fault on the same communication frame. If a CRC error occurs in the response frame from address N+1, device N does NOT append its own message and an invalid CRC fault is generated. For example, if device 15 finds response frame from device 16 has invalid CRC, device 15 doesn't send its own response frame.

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

## Submit Document Feedback

Copyright © 2020 Texas Instruments Incorporated

## The device uses a CRC (cyclic redundancy check) to protect data integrity during transmission. The

device uses the CRC-16-IBM polynomial (x 16 + x 15 + x 2 + 1 ) with 0xFFFF initialization. ***7.3.2.1.1.1 Calculating Frame CRC Value***

## The CRC calculation by the transmitter is in bit-stream order across the entire transmission frame (except for the

CRC). When determining bit-stream order for implementing the CRC algorithm, it is important to note that protocol bytes transmit serially, least-significant bit first. Figure 7-9 illustrates the bit-stream order concept.

## Figure 7-9. Bit-Stream Order Explanation

## The CRC (0x0000) is appended to the end of the bit-stream. This bit-stream is then initialized by XOR'ing with

0xFFFF to catch any leading 0 errors. This new bit-stream is then divided by the polynomial (0xC002) until only the 2-byte CRC remains. During this process, the most significant 17 bits of the bit stream are XOR'd with the polynomial. The leading zeroes of the result are removed and that result is XOR'd with the polynomial once again. The process is repeated until only the 2-byte CRC remains. For example:

## Example 1: CRC Calculation Using Polynomial Division

$$ Command Frame = 0x80 00 02 0F 0B (0b1000 0000 0000 0000 0000 0010 0000 1111 0000 1011) $$ $$ Command Frame in bit stream order = 0x01 00 40 F0 D0 (0b0000 0001 0000 0000 0100 0000 1111 0000 1101 $$ 0000.  $$ After Initialization (XOR with 0xFFFF) = 0b1111 1110 1111 1111 0100 0000 1111 0000 1101 0000 $$ 1111 1110 1111 1111 0100 0000 1111 0000 1101 0000 0000 0000 0000 0000 #append 0x0000 for CRC 1100 0000 0000 0010 1 #XOR with polynomial 0011 1110 1111 1101 1100 0000 1111 0000 1101 0000 0000 0000 0000 0000 11 1110 1111 1101 1100 0000 1111 0000 1101 0000 0000 0000 0000 0000 #delete leading zeros from previous result 11 0000 0000 0000 101 #XOR with polynomial 00 1110 1111 1101 0110 0000 1111 0000 1101 0000.................. 1100 0110 0000 0001 0000 0000 1100 0000 0000 0010 1 #XOR with polynomial 0000 0110 0000 0011 1000 0000 110 0000 0011 1000 0000 110 0000 0000 0001 01 #XOR with polynomial 000 0000 0011 1001 0100 0000 0011 1001 0100 #CRC result in bit stream order 1100 0000 0010 1001 #final CRC result in normal order CRC final 0xC029 ***7.3.2.1.1.2 Verifying Frame CRC***

## There are several methods for checking the CRC of a frame. One method is to simply calculate the CRC for the

transmitted command except the last two bytes (CRC bytes) using the method described in the previous section, and then compare that result with the transmitted CRC bytes. A more simple option is to run the entire transmission through the CRC algorithm. If the CRC is correct, the result is 0000. In this case, the initial zero padding of the bit-stream with 16 zeroes is not necessary. Using the previous result and running through the algorithm produces the following results:

## Example 1: CRC Verification Using Polynomial Division

$$ Command Frame = 0x80 00 02 0F 0B (0b1000 0000 0000 0000 0000 0010 0000 1111 0000 1011) $$ CRC to Check = 0xC029 $$ Command Frame w/ CRC in bit stream order = 0x80 00 02 0F 0B C0 29 (0b1000 0000 0000 0000 0000 0010 $$ **<https://www.ti.com**>

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback*

0000 1111 0000 1011 0000 0011 1001 0100) $$ After Initialization (XOR with 0xFFFF) = 0b0 1111 1110 1111 1111 0100 0000 1111 0000 1101 0000 0000 $$ 0011 1001 0100 1111 1110 1111 1111 0100 0000 1111 0000 1101 0000 0000 0011 1001 010 #delete leading zeros from previous result 1100 0000 0000 0010 1 #XOR with polynomial 0011 1110 1111 1101 1100 0000 1111 0000 1101 0000 0000 0011 1001 0100 11 1110 1111 1101 1100 0000 1111 0000 1101 0000 0000 0011 1001 0100 #delete leading zeros from previous result 11 0000 0000 0000 101 #XOR with polynomial 00 1110 1111 1101 0110 0000 1111 0000 1101 0000 0000 0011 1001 0100.................. 1100 0110 0000 0010 1001 0100 1100 0000 0000 0010 1 #XOR with polynomial 0000 0110 0000 0000 0001 0100 1 1000 0000 0000 0101 00 1 1000 0000 0000 0101 #XOR with polynomial 0 0000 0000 0000 0000 00 0x0000 #verfiy that CRC checks out valid **Note**

The result of '0b0000 0000 0000 0000' for the CRC indicates a successful check. **7.3.2.1.2 Physical Layer**

# 7.3.2.1.2.1 UART

Communication between host and BQ79600-Q1 can be configured to UART mode, refer to Section 7.3.1.3. The UART interface baud rate is default to 1Mbps at power up or digital reset. The UART interface follows the standard serial protocol of 8-N-1 (see Figure 7-10 ), where it sends information as a START bit, followed by eight data bits, and then one STOP bit. The STOP bit indicates the end of the byte. The protocol also supports two STOP bits. When the device is configured as 2 stop bits (\[TWO\_STOP\_EN\] = 1, stack devices should also be set as two stop bits), the UART response frame from the device to MCU will always return with 2 stop bits.

The UART sends data on the TX pin and receives data on the RX pin. When idle, the TX and RX are high. TX is always pulled to VIO internally while in ACTIVE or SLEEP mode, whether enabled or disabled.

The UART interface is strictly a half-duplex interface. While transmitting, any attempted communication on RX is ignored. The only exception is Section 7.3.2.1.2.1.2.

bit0 bit1 bit2 bit3 bit4 bit5 bit6 bit7 START **... ** bit period = 1/ baud rate LSB Stop is oÁÇ•  Z 1 \[

# MSB

| STOP |... |
|:--- |:--- |
| 1 or 2 bit | period |
| Start  is | oÁÇ•Z0\[ | 1 or 2 bit period Start  is oÁÇ•  Z 0 \[ **Figure 7-10. UART Character Definition**

Note: User can change baud rate using register bit \[UART\_VIF\_BAUD\] for debug purpose.

# 7.3.2.1.2.1.1 TX HOLD OFF

UART transmitter is configurable to wait a specified number of bit periods after the last bit reception of Single Device read command frame from host before starting transmitting Response Frame using the TX\_HOLD\_OFF register, as showed in Figure 7-11. This provides time for the host to switch the bus direction at the end of its transmission. **Note**

Host does not need to configure register TX\_HOLD\_OFF in BQ79600-Q1 if Stack Read command is used. Host shall not use Broadcast Read Command.

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2020 Texas Instruments Incorporated

Single Device Read Command frame Response frame

**Last bit of the command ** **received at RX pin**

**1** **st** ** bit of the response ** **frame sent on TX pin** **Time**

# TX\_HOLD\_OFF **Figure 7-11. TX HOLD OFF Timing Diagram**

# 7.3.2.1.2.1.2 UART COMM CLEAR **Note**

Comm Clear concept only applies to bridge device not stack device.

Comm Clear command is used to clear the receiver and instruct it to look for a new start of frame. (Resync up with host) The next byte following the Comm Clear is considered a "start of frame" byte. The digital receiver continuously monitors the RX line for Comm Clear condition which is RX pin is held low for tUART (CLR) bit periods, showed in Figure 7-12.

When Comm Clear is detected, FAULT\_COMM1 \[COMMCLR\_DET\] and FAULT\_COMM1 \[STOP\_DET\] are set. \[STOP\_DET\] flag is set because the Comm Clear timing violates the typical byte timing and the STOP bit is seen as '0'. The only exception to this is when a COMM CLEAR is sent while BQ79600-Q1 is in sleep. If this is the case, there is no STOP error flag. RX pin 1 bit period Command frame t UART(RX\_HIGH) t UART(CLR) **Figure 7-12. Comm Clear Timing**

# 7.3.2.1.2.2 SPI **Note**

To facilitate the communication between daisy chain (asynchronous protocol) and SPI (synchronous protocol), BQ79600-Q1 requires the use of Section 7.3.2.1.2.2.1.

Communication between host and BQ79600-Q1 can be configured to SPI mode, refer to Section 7.3.1.3. The host is always a SPI master while BQ79600-Q1 is always a slave. At physical layer, SPI is a five pin interface including 4 common pins (nCS, SCLK, MOSI, MISO) plus SPI\_RDY. At SPI interface, each bit is captured on low to high clock transitions and propagated on high to low clock transition and byte includes 8 bits as shown in Figure 7-13. Please note, MISO is driven high in idle mode. If MCU talks to multiple slaves, please add a tri-state buffer between BQ79600 MISO and MCU. **<https://www.ti.com**>

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback*

# SCLK

## nCS

# MOSI

# MISO

# SPI\_RDY

SPI\_RDY high indicates host can read/write **predefined ** **number of bytes**

| MSB\_n | LSB\_n |
|:--- |:--- |
| SPI\_CLKH | SPI\_CLKL |
| SU | H |

# SPI\_CLKH SPI\_CLKL

# SU H

# SPI\_CLK t>0

# MSB\_n+1 MSB\_n LSB\_n

# H Bit 7 Bit 0

# MSB LSB

## One Byte Bit 0 bit period = t SPI\_CLK Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 7 xxx xxx xxxx xxxx Hi or Low Hi or Low

SPI\_RDY may go low (and it is ok) before finish read/write this batch

**Figure 7-13. SPI Timing and Byte Definition** **Note**

Although SPI interface is full duplex at physical layer, at frame layer, it is effectively half duplex because daisy chain only supports half duplex. It means, at the given time, only a command frame OR a response frame is transmitted between MCU and the device. - • When command is being sent from MCU to the device, BQ79600 TX FIFO (2 buffers) should be empty, 0xFF is sent to MCU (except in FIFO diagnostic mode) - • When response is being sent from device to MCU, MCU shall clock in 0xFF

- • Host shall provide SPI clock in the range between 2MHz and 6MHz. This range is set by the predefined size of FIFO. Even SPI can run at 6MHz, it does not increase the throughput of total system as daisy chain speed still limit the throughput. - • To avoid collisions on the daisy chain interface, the MCU must wait until all expected response frames are received (or waiting timer expires) before sending another command frame to bq79600. Refer to flow chart in Figure 7-16. - • Master shall always drive MOSI to '1' when not sending command frame into device. - **• Host Read mode**: from host perspective, read mode is between first byte of a valid read command and last expected number of byte received. - **• Device Read mode**: start from first byte of a valid read command, device exists read mode when TX FIFO times out and FIFO is empty. Device read mode is subset of host read mode. (concept used for understanding of communication fault registers 0x2301, 0x2302 ) - • Other than Comm Clear, device rejects any data from MOSI before exiting Device Read mode. - • SPI module rejects any data from daisy chain (stack device) or from itself after TX FIFO timeout List item. until it enters Device Read mode again.

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2020 Texas Instruments Incorporated

- • For command frame, device uses falling edge of nCS as indication of start of frame, and rising edge as end of frame. MCU needs to toggle and keep nCS low for the entire frame (up to 14 characters), toggle nCS back high at the end of this frame. It is legitimate to freeze SCLK while nCS is low. Pulsing nCS in the middle of a command frame is not supported. - • For response frame, nCS is not required to remain low throughout, although it can just like sending command frame. Host can toggle nCS high, stop SPI reading in the middle of the frame (at byte boundary). IDLE Data ** ** **frame A** IDLE **frame C** IDLE

## nCS

IDLE Data **1** **st** ** half of frame A** IDLE **2** **nd** ** half of frame A** IDLE Supported in command frame and response frame Only Supported in response frame

## nCS IDLE **frame B**

**Figure 7-14. nCS Behavior when Sending Frames**

# 7.3.2.1.2.2.1 SPI\_RDY and SPI FIFOs

SPI\_RDY is a output signal indicating to host that data is ready to communicate. SPI FIFOs Figure 7-15 are buffers in the device for temporary storage of incoming/outgoing data. They are required for the following reasons: - • Daisy chain baud rate is approximately 1Mbps by default, once host requests large amount of data, e.g. 400 bytes, device daisy chain receiver would try to send it back to host, but since device does not own the SCLK, it cannot control when the data would be read out. Thus when host is not reading, device need to store the incoming data in the TX FIFO. And even when host is reading, FIFOs are still needed to handle the baud rate difference between SPI and daisy chain. - • SPI\_RDY is required because there is limited depth of TX FIFOs. If host requests more than 256 bytes, and host does not service (read data out) device in time, data overflow would happen. SPI\_RDY indicates to host that certain amount of data is ready to be read or written, e.g. If host request 129 bytes, first time SPI\_RDY flags 128 bytes is ready, second time SPI\_RDY flags 1byte is ready. For details refer to Table 7-5 **<https://www.ti.com**>

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback* **32 bytes** **RX FIFO**

# BQ79600-Q1 **Ping Buffer** **128 bytes** **Daisy Chain Transceiver ** **Pong Buffer** **128 bytes**

# TX FIFO

# MOSI **MISO** **Aprox. 1Mbps** **Asynchronous **

# COMH/COML Pins

**Aprox. 1Mbps** **Asynchronous ** **Aprox. 1Mbps** **Asynchronous **

For simplicity, the drawing only shows dataflow from/to stack devices, it \} •v \[ š  •Z\}Á  šZ  š(o\}Á  \}(  Œ   (Œ\}u / write to BQ79600 itself.

# SCLK: 2MHz 6MHz

## Figure 7-15. SPI FIFO Simplified Diagram

## TX FIFO consists of two 128 bytes buffers (working together as Ping-Pong buffer).

1. When Ping buffer is filled up, Pong buffer should be empty, to store incoming data. 2. While Pong buffer is being filled, Ping buffer is being read. Each byte in buffer is reset to 0xFF once being read. Ping buffer shall be empty (read out) before Pong buffer is full. 3. After Pong buffer is filled up, Ping buffer catches up. 4. Device goes through this loop (step 1 to 3) till all response data are received. 5. Host has to read TX FIFO fast enough such that Ping (Pong) buffer is read out and ready to store data from daisy chain before Pong (Ping) buffer is full.

## Table 7-5. SPI\_RDY Behavior Summary

# CASE **#** **HI-\>LOW WHEN** **LO-\>HI WHEN** a b

Host Writes In 2μs when RX FIFO has \>= 16 bytes. After event a1, in 2μs when RX FIFO has \< 8 bytes. Host Reads

In 5μs after device receives 1st byte of read command frame. In 1us after ping (pong) buffer is full.

TX buffer being read becomes empty (before transmitting out last bit of last byte in the buffer) Note: once going low, SPI\_RDY remains low for 2μs no matter what.

TX FIFO time out happened Note: TX FIFO timeout could happen while SPY\_RDY is high (while host is reading TX FIFO), in this case, after event a3, SPI\_RDY goes how for approximately 2μs, then come back high.

## Notes

- • SPI\_RDY sets flag only, doesn't gate data flow into or out of device. - • Once devices enters Device Read mode, device rejects any data from host other than COMM CLEAR. a1, b1 doesn't apply anymore. - • TX FIFO Timeout: after SPI module receives one byte of data from either daisy chain or BQ79600-Q1 local, a timer starts; this timer expires if there is no data received for 30μs.

## 7.3.2.1.2.2.2 Flow to Read/Write BQ79600-Q1

## User shall follow flow chart Figure 7-16 to do read from device and Figure 7-17 to do write to device activities.

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2020 Texas Instruments Incorporated

# SPI\_RDY = Z1\[?

# NO NO Wait $$ t<= t8 $$

Drop nCS, Send one **Single Device Read** or **Stack Read** Command frame, raise nCS @2-6Mbps; M = expected total Response bytes, $$ i = int(M/128), K = M- i*128; $$

Drop nCS, Read 128 bytes then stop (stop SCLK, raise nCS high), $$ i = i -1; $$ Total wait time \> t WAIT\_READ\_MAX?

# NO YES Comm Clear, Reread i > 0?

# YES Drop nCS, Read K bytes, raise nCS

# YES Host reads expected # of valid data

# YES

# NO Comm Clear Finish Reading

# SPI\_RDY = Z1\[?

# YES

# NO delay Start Device Initialization

## Figure 7-16. Flow Chart to Read from Device

## Note

## MCU shall check SPI\_RDY pin at least every t8 (max service interval). t8 = 1ms at SCLK = 6MHz /

890μs at SCLK = 4MHz /550μs at SCLK = 2MHz assuming host starts to read TX FIFO right after detecting SPI\_RDY = '1 and SPI bus has 30% idle time in the process of reading 128 bytes.

## • • For response frame, nCS has to be toggled high after reading the last byte of data in the current buffer.

- • t WAIT\_READ\_MAX - - stack read/single device read from stack devices, with n stack devices, request m bytes in total (payload + overheads, from all stack devices), wait time: (n-1)*3\mus*2 + m*10\mus + 100μs. - - single device read from BQ79600-Q1, request m bytes, wait time: 100μs + m\*10μs. **<https://www.ti.com**>

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback*

# SPI\_RDY = Z1\[?

# YES

# NO Wait t

Toggle nCS low, Send 1 Write Command frame (up to 14 bytes) @SCLK 2Mhz-6MHz, toggle nCS high Total wait time \> 250us?

# NO

# NO Comm Clear Start More Write cmd to send?

# NO End YES

# YES

# SPI\_RDY = Z1\[?

# YES

## Figure 7-17. Flow Chart to Send Write Command Frame to Device

## Notes

## • • Since write command frame doesn't incur response frames, host shall discard data from MISO pin.

- • If host sends partial data, the device would keep waiting the rest of command data till communication time out happens. Refer to Section 7.3.2.4 for details.

# 7.3.2.1.2.2.3 SPI COMM CLEAR

## Note

## SPI Comm Clear, applied only to bridge device, is used to clear the FIFOs and reset SPI module.

## It stops BQ79600-Q1 sending response; it cannot stop stack devices sending response data back to BQ79600

Q1. If host still couldn't communicate to device, host can ultimately use SHUTDOWN ping followed by WAKE ping to reboot device. Device only responses to Comm Clear in ACTIVE. Use the SPI Comm Clear command when: - • SPI\_RDY being low exceeds expected time, either t SPI\_RD\_WAIT\_MAX in READ mode in Figure 7-16 or when 220μs while sending write command frame into device. Don't send Comm Clear before this wait time has elapsed. - • Data read back by host has CRC error. - • Host cannot communicate to the device.

## MOSI pin

# COMM CLEAR

## nCS

# SCLK

## 8 clk cycles

# SU H xx xx Hi or Low xx xx Hi or Low

## Figure 7-18. SPI Comm Clear

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2020 Texas Instruments Incorporated

## SPI Comm Clear is strictly defined as nCS toggling low, 8 bits of '0', nCS toggling high like shown in Figure 7-18.

nCS must remain low while sending the Comm Clear. If additional data is detected on MOSI pin before nCS going high, \[COMCLR\_ERR\] bit is set, device ignores malformed Comm Clear. A correctly formed Comm Clear will only trigger \[COMMCLR\_DET\]. If Comm Clear is used, it can trigger DEBUG\_SPI\_FRAME \[TR\_SOF\] (while transmitting local data), \[RC\_SOF\](receiving partial data) and \[TS\_WAIT\] (while transmitting daisy chain data). ***7.3.2.1.2.3 Daisy Chain***

## Daisy chain is the interface (COMH/COML) communicating to stack devices. It is bi-directional and half duplex,

and, therefore, has a transmitter (TX) and receiver (RX) on both COMH and COML interfaces, Figure 7-1. Signal going in and out of daisy chain port is taken care by the device. To use the device, host does not need to know daisy chain physical layer protocol (bit definition, byte definition and byte transferring). Host just needs to control SPI or UART port properly. Still, for user's information, daisy chain physical layer protocol is described below.

## Daisy chain bit is transmitted between COM\*P and COM\*N in fully differential fashion, see Figure 7-19.

## Daisy chain byte uses an asynchronous 13-bit byte-transfer protocol. The definition of each bit in the byte is

defined in Table 7-6. Byte to byte transmission is captured in Figure 7-20.

# PW\_DC 2 x t PW\_DC

# COM\*P t COMP\*N

# COM\*P COM\*N

# Z 1 \[ Z 0 \[

# PW\_DC

# PW\_DC

## Figure 7-19. Daisy Chain Bit Definition +1 Preamble (half-bit)

# SYNC \[1:0\] 6.5us nominal 1.375us of bus idle 0.5us of bus short

# DATA\[7:0\] Byte Error (1bit) Postamble (half-bit) Start-Of-Frame (1bit)

# COM\*P t COMP\*N

# D0 D1 D7 D6 D5 D2 D3 D4 $$ SYNC = 2'b00 $$ Byte Up to 8.375us for a byte Byte 10.875us at 1Mbps, 40.6us at 250Kbps Up to 8.375us for a byte

## Daisy Chain Byte Definition

## Daisy Chain Byte Transfer

# LSB

# MSB

## Figure 7-20. Daisy Chain Byte/ Byte Transfer Definition **<https://www.ti.com**>

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback*

## Table 7-6. Daisy Chain Byte Definition

# BIT NAME **DESCRIPTION**

| Preamble (half-bit) | Indicates a start of byte transaction, signaling the receiver to start sampling. This half-bit and the following 2 | SYNC bits are used for extra timing information. |
|:--- |:--- |:--- |
| SYNC\[1:0\] | Always 0b00. The SYNC bits are used for the digital to assess the timing and noise level on the byte, improving | the detection of a '1' and '0' in a noisy environment. |
| Start-Of-Frame (1-bit) | The Start-Of-Frame (SOF) bit defines the byte as the INIT byte (initialization byte) in the frame, refer to Figure | 7-8. Stack device needs this information in order to process the communication. |

SYNC\[1:0\] Always 0b00. The SYNC bits are used for the digital to assess the timing and noise level on the byte, improving the detection of a '1' and '0' in a noisy environment.

Start-Of-Frame (1-bit) The Start-Of-Frame (SOF) bit defines the byte as the INIT byte (initialization byte) in the frame, refer to Figure 7-8. Stack device needs this information in order to process the communication. Data\[7:0\] The actual 8-bit payload.

Byte Error BERR (1-bit) For BQ79600-Q1, BERR is always '0' in command frames sent to stack device. While in received response frames, if it is '1', it indicates last device DEBUG\_COM\*\_PHY\[PERR\] = 1.

Postamble (half-bit) Indicates the end of byte transaction.

## 7.3.2.2 Tone Communication Protocol

## Other than data, certain information is transmitted using tone: signals to change power state of stack device

(SLP2ACT tone, WAKE tone, SHUTDOWN tone, HWRST tone), signals related to faults (FAULT tone and HEARTBEAT tone). The definition of each tone is defined in Figure 7-22 and Figure 7-21.

## Device can transmit and receive tones in summary below

## Table 7-7. Available Tones to BQ79600-Q1

| DIRECTION | NAME |
|:--- |:--- |
| Receive | FAULT tone and HEARTBEAT tone |
| Transmit | SLP2ACT tone, WAKE tone, SHUTDOWN tone, HWRST tone, HEARTBEAT tone | Receive FAULT tone and HEARTBEAT tone

Transmit SLP2ACT tone, WAKE tone, SHUTDOWN tone, HWRST tone, HEARTBEAT tone

## Note

- • Device does not transmit Fault Tone as it uses Section 7.3.3.2.1 to signal fault if enabled. - • SLP2ACT/WAKE/SHUTDOWN/HWRST tone transmitting is on demand when corresponding bit in register CONTROL1 and CONTROL2 is set. - • When bridge device in SHUTDOWN, wakeup bridge device doesn't change power mode of stack devices. - • Receiving threshold value is defined as n HBDET, n FTONEDET in section 6.6. - • Transmitting number is predefined by device in Table 7-8.

## Table 7-8. Transmitting Tones Summary Table

# SLP2ACT

**WAKE** **SHUTDOWN** **HWRST** **HEARTBEAT (SLEEP only)** N of Couplets Transmitted in Single Burst Burst Period NA NA NA NA 400ms

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2020 Texas Instruments Incorporated

# V DCCM

# COM\*P t COMP\*N

# COM\*P COM\*N

# FLTTONE\_PLS

# FLTTONE

# FLTTONE\_PLS

## A pulse

## One Burst (N of couplets)

## One Burst (N of couplets)

# HB\_PERIOD or t FTONE\_PERIOD

## Figure 7-21. FAULT Tone and HEARTBEAT Tone Definition

# V DCCM

# COM\*P t COMP\*N

# COM\*P COM\*N

# COMTONE\_PLS

# COMTONE

# COMTONE\_PLS (N of couplets)

# V DCCM

# COM\*P t COMP\*N

# COM\*P COM\*N

# COMTONE\_PLS

# COMTONE (N of couplets)

# COMTONE\_PLS

# WAKE, SLP2ACT Tone

**SHUTDOWN**, **HEARTBEAT**, **HWRST ** Tone **  **

## Figure 7-22. SHUTDOWN, HEARTBEAT, HWRST, SLP2ACT Tone Definition

## 7.3.2.3 Device Auto Addressing / Ring Communication

## Note

## The host starts communication at least 100µs after changing the \[DIR\_SEL\] setting to ensure the

device finishes the COMH/COML reconfiguration.

## 7.3.2.3.1 Auto-Addressing

## To properly communicate to every device in daisy chain, host has to assign a unique device address to every

device. This process is called Auto-addressing. This step is required every time devices come out of SHUTDOWN or digital reset. Table 7-9 describes a procedure to bring up a system of 1 bridge device and 3 stack devices from SHUTDOWN to a state ready to do read/write communication.

## • • All device addresses must be sequential

## Table 7-9. Auto-Addressing with Figure 7-22(a), assume all devices are in SHUTDOWN

# STEP **WORK WITH BQ7961X-Q1** send WAKE ping on RX (wakeup BQ79600-Q1)

single device write to BQ79600-Q1 CONTROL1 \[SEND\_WAKE\] = 1 (wake up stack devices)

dummy stack write data 0x00 to register 0x343 to 0x34A (sync up internal DLL). These are 8 separate write commands.

brdcast write 0x01 to address 0x309 (enable auto addressing) **<https://www.ti.com**>

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback*

## Table 7-9. Auto-Addressing with Figure 7-22(a), assume all devices are in SHUTDOWN (continued)

# STEP **WORK WITH BQ7961X-Q1**

brdcast write consecutively to 0x306 = 0,1,2,3 (address 1-3 assigned to BQ7961X-Q1, 0 assigned to BQ79600-Q1)

brdcast write 0x02 to address 0x308 (set BQ7961X-Q1 as stack device )

single device write to device 3: data 0x03 to address 0x308 (set 3rd BQ7961X-Q1 as top of stack, BQ79600-Q1 is default to base)

dummy stack read registers 0x343 to 0x34A (sync up internal DLL). These are 8 separate read commands.

stack read address 0x306 (read back to verify address are correct for stack devices)

single device read to BQ79600-Q1, verify 0x2001 = 0x14 finish initialization

## 7.3.2.3.2 Ring Communication (optional)

## A ring communication (optional) allows the system to establish communication from either direction. This allows

the system to continue communicating to all stack devices even if one piece of daisy chain cable is broken.

## Table 7-10 describes a procedure auto address Figure 7-23 (b): to bring up a system of 1 bridge device and 3

stack devices from SHUTDOWN to a state ready to do read/write communication in **reverse direction**.

## To change communication direction from Figure 7-23 (a) to Figure 7-23 (b), follow the steps 2, 4-14. (Assuming all

devices in (a) are already in ACTIVE and auto addressed as described in Table 7-9 )

# MCU bq Monitoring IC (S1)

# COML

# COMH bq Monitoring IC (S2)

# COML

# COMH bq79600 (Base, B0)

# COMH

# COML bq Monitoring IC (Top Of Stack)

# COML

# COMH

*a). \[DIR\_SEL\]* = 0: Command from COMH -> COML) Command Response bq Monitoring IC (Top of Stack)

# COML

# COMH bq Monitoring IC (S2)

# COML

# COMH bq79600 (Base, B0)

# COMH

# COML bq Monitoring IC (S1)

# COML

# COMH Command Response

*b). \[DIR\_SEL\]* = 1: Command from COML -> COMH)

# MCU

## Figure 7-23. Example to Change Communication Direction in Daisy Chain

## Table 7-10. Auto-Addressing Figure 7-22(b), assume all devices are in SHUTDOWN

# STEP **WORK WITH BQ7961X-Q1** send WAKE ping on RX (wakeup BQ79600-Q1)

single device write to BQ79600-Q1 control 1 [DIR_SEL] = 1 (change BQ79600-Q1 direction)

single device write to BQ79600-Q1 CONTROL1 \[SEND\_WAKE\] = 1 (wake up stack devices)

dummy stack write data 0x00 to registers 0x343 to 0x34A (sync up internal DLL). These are 8 separate write commands.

**brdcast write reverse** 0x80 to address 0x309 (change stack devices direction DIR\_SEL =1) brdcast Write 0x02 to address 0x308 (1)

brdcast Write 0x81 to address 0x309 (enable BQ7961X-Q1 auto addressing)

brdcast Write consecutively to address 0x307 = 0,1,2,3 (address 1-3 assigned to BQ7961X-Q1, 0 assigned to BQ79600-Q1)

brdcast write 0x02 to address 0x308 (set BQ7961X-Q1 as stack device )

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2020 Texas Instruments Incorporated

**Table 7-10. Auto-Addressing Figure 7-22(b), assume all devices are in SHUTDOWN (continued)**

# STEP **WORK WITH BQ7961X-Q1**

single device write to device 3: data 0x03 to address 0x308 (set 3rd BQ7961X-Q1 as top of stack, BQ79600-Q1 is default to base)

dummy stack read registers 0x343 to 0x34A (sync up internal DLL). These are 8 separate read commands.

stack read address 0x307 (read back to verify address are correct for stack device)

single device read to BQ79600-Q1, verify 0x2001 = 0x14 finish initialization

(1) Clear the previous TOP\_STACK flag after communication direction is changed because top of stack device cannot be reached if one cable is broken ***7.3.2.4 Communication Timeout***

In ACTIVE, there are two programmable communication timeout timers, **comm timeout short** (once expires, flag fault) and **comm timeout long** (once expired, transition to SLEEP or SHUTDOWN). They monitor the absence of a valid frame from either UART/SPI or daisy chain communications. A valid frame is defined as any frame (response or command) that does NOT contain any errors that prevent the frame from being processed.

In SHUTDOWN, the timers are disabled and reset. In SLEEP, the last timer values are held frozen. The timer is reset every time a valid response or command frame is received.

How to set the timer, timer expiration action are described in COMM\_TIMEOUT. In order to avoid entering SHUTDOWN mode before a communications timeout fault, ensure the COMM\_TIMEOUT \[CTS\_TIME\] is shorter than the COMM\_TIMEOUT \[CTL\_TIME\]. ***7.3.2.5 Communication Debug Mode***

The device provides a communication debug mode to ease the initial development phase. Enter/exit debug is controlled by setting of register DEBUG\_CTRL\_UNLOCK. Once device is in debug mode, user is able to control the UART/daisy chain baud rate and on/off of COMH/COML RX/TX. Please refer to register DEBUG\_COMM\_CTRL. User can always read DEBUG\_COMM\_STAT register for comm status disregard the setting/mode of device.

In addition to that, device provides communication low level faults (physical and frame layer)to facilitate debug. Refer to registers from address 0x2301 - 0x2307. **<https://www.ti.com**>

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback*

# 7.3.3 Fault Handling

***7.3.3.1 Fault Status Hierarchy/Reset/Mask***

# 7.3.3.1.1 Fault Status Hierarchy

# BQ79600-Q1 reports faults in hierarchy, as shown in Figure 7-24

- • Level 1 is FAULT\_SUMMARY register in which each bit represents an OR function of all the bits in its own hierarchy captured in level 2. - • Level 2 bit is the OR function of level 3 bits in its own hierarchy. - • Level 3 contains debug register bits meant to inform host frame and physical layer fault. Level 3 fault is useful in firmware development. - • Any bit triggered in lower level would trigger higher level bit in its hierarchy, e.g. if \[TXFIFO\_OV\] is set, \[SPI\_PHY\], \[FAULT\_COMM\] would also be set.

# Note

# Host system can periodically poll the FAULT\_SUMMARY to check the fault status and only read the lower level fault registers if needed.

# 7.3.3.1.2 Fault Reset and Mask

# Once fault is detected, the fault status bit is latched until cleared using the reset bit.

# When a specific fault reset bit is set, the same color coded bits in level 1 to level 3 are cleared if the fault

condition is gone. If the fault condition persists and the reset bit is written, the fault status bit is not reset. For example, if \[TXFIFO\_OV\], \[DVDD\_OV\] bits are set, \[SPI\_PHY\], \[FAULT\_COMM\] and \[FAULT\_PWR\] are set, if fault conditions are eliminated and write '1' to \[RST\_UART\_SPI\] and \[RST\_PWR\], 5 faults bits would be '0'.

# When a specific fault mask bit is set, the same color coded bits would be masked, meaning the fault bits will still

be set, but the faults will not be reflected in level 1, FAULT\_SUMMARY register. For example, if \[MSK\_UART\_SPI\] = 1, any bits being set marked green in level 2 and 3 won't set \[FAULT\_COMM\] bit.

# When fault is masked, it will also prevent the device from asserting the NFAULT pin when the masked faults occur. See Section 7.3.3.2 for details.

# MASK/RST

# Mask

Bit **MSK\_REG** **MSK\_SYS** **MSK\_PWR** Reset Bit **RST\_REG** **RST\_SYS** **RST\_PWR**

**Fault Status** **Level 1** **Fault Summary** Bit FAULT\_REG FAULT\_SYS FAULT\_PWR

# Level 2

# Detailed Fault

**Register ** **FAULT\_COMM1** **FAULT\_COMM2** **FAULT\_REG** **FAULT\_SYS** **FAULT\_PWR**

| FCOMM\_DET | SPI\_FRAME | CONF\_MON\_ERR | VALIDATE\_DET | CVDD\_UV\_DRST |
|:--- |:--- |:--- |:--- |:--- |
| FTONE\_DET | SPI\_PHY | FACTLDERR | LFO | CVDD\_OV |
| HB\_FAIL | COML\_FRAME | FACT\_CRC | SHUTDOWN\_REC | DVDD\_OV |

# FTONE\_DET SPI\_PHY FACTLDERR LFO CVDD\_OV

# HB\_FAIL COML\_FRAME FACT\_CRC SHUTDOWN\_REC DVDD\_OV

# HB\_FAST COML\_PHY DRST AVDDREF\_OV

# UART\_FRAME COMH\_FRAME CTL AVAO\_SW\_FAIL

# COMMCLR\_DET COMH\_PHY CTS

# STOP\_DET TSHUT

# INH

# Level 3

# Debug Info

**Register ** **DEBUG\_UART\_FRAME** **DEBUG\_SPI\_FRAME** **DEBUG\_SPI\_PHY** ** ** **DEBUG\_COML\_FRAME** **DEBUG\_COML\_PHY** **DEBUG\_COMH\_FRAME** **DEBUG\_COMH\_PHY**

# TR\_SOF TR\_SOF FMT\_ERR RR\_IERR PERR RR\_IERR PERR

# TR\_WAIT

TR\_WAIT COMCLR\_ERR RR\_SOF BERR\_TAG RR\_SOF BERR\_TAG

# RC\_IERR

RC\_IERR TXDATA\_UNEXP RR\_BYTE\_ERR SYNC2 RR\_BYTE\_ERR SYNC2

# RC\_SOF

RC\_SOF RXDATA\_UNEXP RR\_UNEXP SYNC1 RR\_UNEXP SYNC1

# RC\_BYTE\_ERR

RC\_BYTE\_ERR TXFIFO\_OF RR\_CRC BIT RR\_CRC BIT

# RC\_CRC RC\_CRC TXFIFO\_UF

# RXFIFO\_OF

# FAULT\_COMM

## Bit Bit

# MSK\_COML\_H MSK\_UART\_SPI MSK\_FCOMM\_DET MSK\_FTONE\_DET MSK\_HB

# RST\_COML\_H RST\_UART\_SPI

**RST\_FCOMM\_DET** **RST\_FTONE\_DET** **RST\_HB**

# Figure 7-24. Fault Status Hierarchy, Mask and Reset

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

# Submit Document Feedback

Copyright © 2020 Texas Instruments Incorporated ***7.3.3.2 Fault Interface***

Host can acquire the fault status with the following two methods: - • Host ignores NFAULT pin, constantly polls the FAULT\_SUMMARY register of each device. If FAULT\_SUMMARY is non-zero, read the low level fault status registers to obtain more information. - • Host monitors NFAULT pin status. Enable fault status to pass down the daisy chain to bridge device. Enable bridge device's NFAULT pin to be asserted when the FAULT\_SUMMARY is non-zero. When NFAULT is triggered, host polls fault information to diagnose further.

# 7.3.3.2.1 NFAULT

Device integrates an NMOS open-drain output (NFAULT) to signal the MCU that a fault has occurred in the system (either fault from BQ79600-Q1 or from monitoring IC). The NFAULT driver is enabled when \[NFAULT\_EN\] = 1. When BQ79600-Q1 detects an unmasked fault, NFAULT asserts low. When NFAULT is disabled, the device will set the corresponding flag in *FAULT\_SUMMARY* register but will not assert NFAULT.

If the fault information of stack devices are not transmitted to bridge device through Section 7.3.3.2.2, NFAULT output only indicates faults in BQ79600-Q1. **7.3.3.2.2 Daisy Chain (COMH and COML)**

When using BQ79600-Q1 NFAULT pin to signal the host under a fault detection, the stack devices have to transfer their fault status information to the base device. The information is transmitted through COMH/L interface through the same communication cables:

- • In ACTIVE, BQ79600-Q1 detects embedded fault info in response frame from stack device. - • In SLEEP, stack device sends Heartbeat and Fault tone to BQ79600-Q1. - • In SHUTDOWN, use Sniff Detector of BQ79600-Q1 monitors stack device Fault tone.

***7.3.3.2.2.1 Fault Transmitting when BQ79600-Q1 in ACTIVE***

In ACTIVE mode, stack devices can embed their fault status in their response frames (refer to Figure 7-7 ) that are sent to BQ79600-Q1. The BQ79600-Q1 can detect their embedded fault info and sets \[FTONE\_DET\] bit once criteria in Figure 7-25 is met. Please refer to BQ7961X-Q1 on how to use embeded fault feature.

To pass on the fault status of the stack devices, the host sends a stack read which will result with response frame pass through every device in the daisy chain, giving each device an opportunity to embed their fault status to response frame.

# INIT\[7:0\]

Dev ADR\[7:0\] REG ADR\[15:8\] REG ADR\[7:0\] DATA MSB\[7:0\] CRC\[7:0\] +1 Preamble

# SYNC \[1:0\] Start-Of-Frame

# SYNC = 2'b00 +1 Preamble

# SYNC \[1:0\] Start-Of-Frame

# SYNC = 2'b00 +1 Preamble

# SYNC \[1:0\] Start-Of-Frame

# SYNC = 2'b00 +1 Preamble

# SYNC \[1:0\] Start-Of-Frame

# SYNC = 2'b00

# SOF = 1

SOF bit of DEV ADR SOF bit of REG ADR\[15:8\] SOF bit of REG ADR\[7:0\] Fault Status x x x x x x [FCOMM_EN] = '0' x x x [FCOMM_DET] = '0'

# \[FCOMM\_DET\] = '1'

# \[FCOMM\_DET\] = '0'

# \[FCOMM\_EN\] = '1'

**Figure 7-25. Embed Fault Detection in Response Frame**

***7.3.3.2.2.2 Fault Transmitting when BQ79600-Q1 in SLEEP***

Because data communication is not available in SLEEP mode, the device provides following options to transmitting fault information: - • Transmit the Heartbeat tone (enabled by \[HB\_TX\_EN\], used to check integrity of cable between bridge and first stack device). Device does not transmitted fault tone as it has NFAULT. **<https://www.ti.com**>

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback*

# • • Detect Heartbeat and Fault tone, enabled, by \[TONE\_RX\_EN\].

# These tones are transmitted in the same direction as a communication command frame, which is based on the

CONTROL1\[DIR\_SEL\] setting. For the tone signal to return back to BQ79600-Q1 (so NFAULT can be triggered if needed), a Ring architecture must be used to support transmitting fault status in SLEEP mode. B0 (base device) Non-bq79606 S1

1)B0 detects HB tone from S2, B0 itself has no fault, send HB tone to S1 (optional) **Scenario1: No Fault ** 2. S1 has no fault, send HB tone to S2 3. S1 has no fault, send HB tone to B0

# MCU Non-bq79606 (Top of Stack) S2

**Scenario2: HB Stop** **Scenario3: Fault Detected** Sleep Sleep Sleep Shutdown

# IHN B0 (base device) Non-bq79606 S1

# MCU Non-bq79606 (Top of Stack) S2 Sleep Sleep Sleep Shutdown

# IHN B0 (base device) Non-bq79606 S1

2. Receive S1 Fault tone, S2 sends  Fault tone to B0.

# MCU Non-bq79606 (Top of Stack) S2 Sleep Sleep Sleep Shutdown

# IHN

3)B0 receivers fault tone from S2, set \[FTONE\_DET\], drive INH pin high, NFAULT pin low Fault Detected

3)B0 receivers fault tone from S2, set \[FTONE\_DET\], drive INH pin high, NFAULT pin low

1. S1 receives HB tone from B0 as  expected, S1 has no fault, send HB tone to S2

2. S2 \} •v \[ š  Œ  \]À Œ , š\}v  •  expected, set fault, send Fault tone to B0

1. S1 receives HB tone from B0 as  expected, S1 has fault, send Fault tone to S2

# Figure 7-26. Heartbeat and Fault Tone Examples

# Both the Heartbeat and Fault Tone are a type of tone similar to the communication. One main difference is a

communication tone only transmits with a single burst of couplets, while Heartbeat and Fault Tones are sent with a burst of couplets periodically. See Figure 7-21 for details.

# 7.3.3.2.2.3 Fault Transmitting (Automatic Host Wakeup/Reverse Wakeup) when BQ79600-Q1 in SHUTDOWN

# Note

# This feature (Auto Host Wakeup/Reverse Wakeup) is only available if Section 7.3.5 is enabled.

# The purpose of this user case is to keep BQ79600-Q1 in lowest power mode while still being able to detect fault

information from stack devices. In this case, fault information transmittion is similar to that of SLEEP: top of stack device sends HB or Fault tone to BQ79600-Q1. The difference lies in the detection of those tones in BQ79600Q1. In SHUTDOWN, TONE RX is off, only low power Section 7.3.5 is available. Once sniffer detects FAULT tone, it puts device into VALIDATE mode in which full power TONE RX is available, device would validate if true Fault tone exists or not. If yes, it triggers INH. See Figure 7-27 for different case.

# PMIC

| B0 | (base device) |
|:--- |:--- |
| Non-bq79606 | S1 |
| 3)B0 \}
•v\[šŒ

\]À
&µošš\}v
(Œ\}u | S2, No Action | Non-bq79606 S1

3)B0 \} •v \[ š  Œ  \]À & µoš  š\}v  (Œ\}u  S2, No Action **Scenario1: No Fault **

1. Mask HB Tone RX fault from B0. S1  has no fault, send HB tone to S2.

2. Receive S1 HB tone as expected,  S2 has no fault, \}v \[ š  • v & µoš  š\}v  to B0.

# MCU Non-bq79606 (Top of Stack) S2

**Scenario2: HB Stop** **Scenario3: Fault Detected** Shutdown Sleep Sleep Shutdown

# INH B0 (base device) Non-bq79606 S1

3)B0 receives Fault tone from S2, transition to Fault Validate, validate Fault tone from S2, drive INH pin high

1. Mask HB Tone RX fault from B0. S1  has no fault, send HB tone to S2.

2.  \}  •v \[ š  Œ  \]À ^ 1 HB tone as expected, S2 sends Fault tone to B0. Non-bq79606 (Top of Stack) S2 Shutdown Sleep Sleep B0 (base device) Non-bq79606 S1

1. Mask HB Tone RX fault from B0. S1  has no fault, send HB tone to S2.

2. Receive S1 Fault tone, S2 sends  Fault tone to B0. Non-bq79606 (Top of Stack) S2 Shutdown Sleep Sleep

3)B0 receives Fault tone from S2, transition to Fault Validate, validate Fault tone from S2, drive INH pin high Fault Detected

# INH PMIC

# MCU Shutdown

# INH INH PMIC

# MCU Shutdown

# INH Shutdown Shutdown Shutdown

# Figure 7-27. Reverse Wakeup User Case

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

# Submit Document Feedback

Copyright © 2020 Texas Instruments Incorporated **7.3.4 INH/ Reverse Wakeup** **Note**

INH pin is used if Reverse Wakeup feature is used. If this feature is not used, connect this pin to BAT pin, refer to schematic in Figure 8-1.

Reverse wakeup feature is a mechanism where BQ79600-Q1 can wakeup the host, through INH pin, on faulty status from either BQ79600-Q1 or stack devices like BQ7961X-Q1. MCU and its supply (PMIC/SBC) are in SHUTDOWN for power saving on low voltage battery side.

The INH pin is a high voltage output pin that provides voltage from the BAT minus V DROP\_INH to enable an external high voltage regulators (SBC, PMIC). These regulators are usually used to support the microprocessor and VIO pin. When INH PMOS pullup is not activated, INH pin goes to a high Z state, it relies on external circuit to define the pin voltage (in application circuit, 100kohm resistor to GND is used.) INH PMOS pullup can be triggered:

- • In SLEEP mode or VALIDATE mode if following faults are detected regardless of setting of register FAULT\_MSK: \[FTONE\_DET\], \[HB\_FAIL\], \[HB\_FAST\], \[AVAO\_SW\_FAIL\], \[FACT\_CRC\], \[CONF\_MON\_ERR\]. - • In ACTIVE, INH can only be triggered by setting \[INH\_SET\_GO\] =1.

Once INH triggered, it remains latched in all modes as long as VBAT is not removed.

INH function described above can be disabled by configuring INH\_DIS\[1:0\] = 2'b11.

Every time INH PMOS is activated, fault bit \[INH\] is set. To clear the fault, set INH\_DIS\[1:0\] = 2'b11 (disarm INH driver), then write \[RST\_SYS\] = 1. After this, to use INH feature, set INH\_DIS\[1:0\] = 2'b00.

As part of safety diagnostic (SM202 in Safety Manual), host can trigger INH in ACTIVE and check if pin voltage is set properly: If INH pin voltage is higher than V INH\_DET, \[INH\_STAT\] = 1. **Note**

INH pin should be considered a "high voltage logic" terminal, thus should be used to drive the EN terminal of the system's power management device. It should be not used as a switch for power management supply itself. This terminal is not reverse battery protected and thus should not be connected outside of the system module. **<https://www.ti.com**>

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback* **7.3.5 Sniff Detector** **Note**

Sniff detector is only used if reverse wakeup feature is used.

Sniff detector, powered by AVAOREF, is used to detect fault tone from stack device on COMH\* or COML\*. This detector would trigger if it detects/counts no less than nVALIDATE of continuous couplets (either "-" or "+") with amplitude larger than V VAL\_THR. If any couplet timing interval is larger than t SNIFFIDLE, detector/counter is reset.

This sniff detector rejects HB tone since nVALIDATE is more than 30, both HB/Fault tone are "-" tone; detector doesn't expect "+" tone. **Note**

The usage assumption of this detector is when system is in idle mode, BQ79600-Q1 in SHUTDOWN.

Sniff detector is only effective in SHUTDOWN. Once detector is triggered, device transitions from SHUTDOWN to VALIDATE. The sniff detector is by default disabled when first transition from COMPLETE OFF to SHUTDOWN. To enable the feature, host has to keep \[SNIFDET\_EN\] = '1' & \[SNIFDET\_DIS\] = '0' before transitioning to SHUTDOWN. After enabling the detector, if device doesn't transition to COMPLETE OFF, the only way to disable the detector is to keep \[SNIFDET\_DIS\] = '1'. (Disable bit has higher priority so don't care about the setting of \[SNIFDET\_EN\]) before transitioning to SHUTDOWN.)

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2020 Texas Instruments Incorporated **7.3.6 Device Diagnostic**

The product is developed as a safety element out of context (SEooC), with a target safety goal of ASIL-D for communication. The following sub-sections describe the diagnostic control and fault status that can be used as part of the safety mechanisms.

The Safety Manual and FMEDA for BQ79600-Q1 are available separately from Texas Instruments. Contact TI Sales Associate or Applications Engineer for further information. ***7.3.6.1 Power Supplies Check*** **7.3.6.1.1 Power Supply Diagnostic Check**

The internal power supply circuits have overvoltage, undervoltage, and/or current limit checks. The table below summarizes the diagnostics that apply for each power supply and the corresponding action when failure is detected.

**Table 7-11. Power Supply Diagnostic Summary**

# SUPPLY **OV CHECK** **UV CHECK** **CURRENT LIMIT**

DVDD If fails, set \[DVDD\_OV\] If fails, digital reset Limit current to EC table current limit specification

CVDD If fails, set \[CVDD\_OV\] If fails, digital reset, set \[CVDD\_UV\_DRST\]

Limit current to EC table current limit specification

AVAOREF If fails, set \[AVDDREF\_OV\] (AVAOREF supplies AVDDREF) If fails, device shuts down

AVDDREF If fails, set \[AVDDREF\_OV\] If fails, set \[AVAO\_SW\_FAIL\] or digital reset

VIO If fails, device losses data communication and Ping function **7.3.6.1.2 Power Supply BIST**

The device implemented a power supply BIST (Built-In Self-Test) function to test CVDD, DVDD, AVDDREF OV detection comparator integrity. It is a command base function initiated by host. Steps below explains how it works, and further details can be found in Safety Manual (SM017). 1. Host shall read the register FAULT\_PWR to verify \[CVDD\_OV\], \[DVDD\_OV\], \[AVDDREF\_OV\] are low. 2. Host shall write \[PWR\_DIAG\_GO\] = 1. 3. After 1.7ms, host shall read if \[PWR\_DIAG\_RDY\] = 1, else shall, keep waiting, reread. 4. If yes, host shall read FAULT\_PWR register, \[CVDD\_OV\], \[DVDD\_OV\], \[AVDDREF\_OV\] to verify the bits are asserted. 5. Host shall reset faults above. ***7.3.6.2 Thermal Shutdown***

Thermal shutdown (TSHUT) event occurs when the Thermal Shutdown sensor value exceeds the thermal shutdown temperature threshold. The sensor operates without interaction and is separated from the ADC measured die sensor. The thermal shutdown function has a register-status indicator flag ( *FAULT\_SYS\[TSHUT\]* ) that is saved during the shutdown event and can be read after the device is waken back up. When a TSHUT fault occurs, the device immediately enters the SHUTDOWN mode. Any pending transactions on UART or daisy chain are discarded. There is no fault signaling when a thermal shutdown event occurs, as the device immediately shuts down.

To awaken the device, host shall ensure the ambient temperature is below T SD\_FALL and sends a WAKE ping to the base device. Host shall not attempt to wake the device if the ambient temperature is still above T SD\_FALL.

Upon waking up, the *FAULT\_SYS\[TSHUT\]* bit is set. The *FAULT\_SYS\[SHUTDOWN\_REC\]* = 1 indicating the prior shutdown was caused by abnormal event. See Section 7.5.17 for more details. If the system faults are unmasked, *FAULT\_MSK1\[MSK\_SYS\]* = 0, the thermal shutdown will be reflected as FAULT and will be indicated in the *FAULT\_SUMMARY* register and the assertion of the NFAULT pin. **<https://www.ti.com**>

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback* ***7.3.6.3 Oscillators Watchdog***

The oscillators are monitored by watchdog circuits. There are two oscillators in the device, the HFO and the LFO. If these oscillators are not functioning, the device does not operate. If the HFO or LFO does not transition within the expected time, the watchdog circuits trigger Digital Reset.

When such unexpected reset occurs, it is recommended for the host to send a SHUTDOWN ping/tone to the problem device and follow up a WAKE ping to reset the daisy chain. If the oscillators are truly damaged, the device will not restart and must be replaced.

In addition to the watchdog, the LFO frequency is monitored to ensure it stays within acceptable limits. If the LFO frequency falls outside of the expected range, the *FAULT\_SYS\_FAULT\[LFO\]* bit is set. ***7.3.6.4 Register Bit Flip Monitor***

This bit flip checker monitors 2 configuration registers: DEV\_CONF1, FAULT\_MSK. It is always running when device is out of SHUTDOWN. Whenever user changes those 2 register settings or any of the register bit flips, fault bit \[CONF\_MON\_ERR\] is set.

Once user changes the setting, user shall write \[CONF\_MON\_GO\]=1 (resample 2 register values), write \[RST\_REG\] =1 to clear the \[CONF\_MON\_ERR\] fault, after this point, if any bit flips among those 2 registers, \[CONF\_MON\_ERR\] is set. After device resets (receive WAKE ping or \[SOFT\_RESET\] = 1), \[CONF\_MON\_ERR\] $$ = 0. $$

This device does not have customer register CRC check and the register bit flip monitor provides the protection for the above mentioned customer registers. ***7.3.6.5 SPI FIFO Diagnostic***

The FIFO diagnostic mode provides a method for host to exercise the RX/TX FIFOs. Please refer to safety manual for detailed FIFO diagnostic safety mechanism implementation (SM132). **7.4 Device Functional Modes** See Section 7.3.1

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2020 Texas Instruments Incorporated

# 7.5 Register Maps

**Addr** ** ** **R/W Type** **Reset Value** **Data**

**Hex** **Bit7** **Bit6** **Bit5** **Bit4** **Bit3** **Bit2** **Bit1** **Bit0**

# DIR0\_ADDR

R/W "0000 0000" RSVD RSVD ADDRESS\[5\] ADDRESS\[4\] ADDRESS\[3\] ADDRESS\[2\] ADDRESS\[1\] ADDRESS\[0\] **DIR1\_ADDR** R/W "0000 0000" RSVD RSVD ADDRESS\[5\] ADDRESS\[4\] ADDRESS\[3\] ADDRESS\[2\] ADDRESS\[1\] ADDRESS\[0\] **CONTROL1** R/W-AC "0000 0000" DIR\_SEL SEND\_SHUTDOWN SEND\_WAKE SEND\_SLPTOACT GOTO\_SHUTDOWN GOTO\_SLEEP SOFT\_RESET ADDR\_WR

# CONTROL2

30A R/W-AC "0000 0000" RSVD RSVD RSVD RSVD RSVD RSVD SEND\_HW\_RESET RSVD

# DIAG\_CTRL

2000 R/W-AC "0000 0000" RSVD RSVD CONF\_MON\_GO PWR\_DIAG\_GO SPI\_FIFO\_DIAG\_GO FLIP\_FACT\_CRC FLIP\_TR\_CRC INH\_SET\_GO **DEV\_CONF1** 2001 R/W **"0001 0100"** SNIFDET\_EN SNIFDET\_DIS TONE\_RX\_EN FCOMM\_EN TWO\_STOP\_EN NFAULT\_EN RESERVED HB\_TX\_EN

# DEV\_CONF2

2002 R/W "0000 0000" RSVD RSVD RSVD RSVD RSVD RSVD INH\_DIS\[1\] INH\_DIS\[0\] **TX\_HOLD\_OFF** 2003 R/W "0000 0000" DLY\[7\] DLY\[6\] DLY\[5\] DLY\[4\] DLY\[3\] DLY\[2\] DLY\[1\] DLY\[0\]

# SLP\_TIMEOUT

2004 R/W **"0000 0011"** RSVD RSVD RSVD RSVD RSVD SLP\_TIME\[2\] SLP\_TIME\[1\] SLP\_TIME\[0\]

# COMM\_TIMEOUT

2005 R/W **"0011 0100"** RSVD CTS\_TIME\[2\] CTS\_TIME\[1\] CTS\_TIME\[0\] CTL\_ACT CTL\_TIME\[2\] CTL\_TIME\[1\] CTL\_TIME\[0\]

# SPI\_FIFO\_UNLOCK

2010 R/W "0000 0000" RSVD RSVD RSVD RSVD CODE\[3\] CODE\[2\] CODE\[1\] CODE\[0\]

# FAULT\_MSK

2020 R/W "0000 0000" MSK\_COML\_H MSK\_UART\_SPI MSK\_FCOMM\_DET MSK\_FTONE\_DET MSK\_HB MSK\_REG MSK\_SYS MSK\_PWR

# FAULT\_RST

2030 R/W-AC "0000 0000" RST\_COML\_H RST\_UART\_SPI RST\_FCOMM\_DET RST\_FTONE\_DET RST\_HB RST\_REG RST\_SYS RST\_PWR

# FAULT\_SUMMARY

2100 R "0000 0000" RSVD RSVD RSVD RSVD FAULT\_COMM FAULT\_REG FAULT\_SYS FAULT\_PWR

# FAULT\_REG

2101 R "0000 0000" RSVD RSVD RSVD RSVD RSVD CONF\_MON\_ERR FACTLDERR FACT\_CRC

# FAULT\_SYS

2102 R "0000 0000" VALIDATE\_DET LFO SHUTDOWN\_REC DRST CTL CTS TSHUT INH

# FAULT\_PWR

2103 R "0000 0000" RSVD RSVD RSVD CVDD\_UV\_DRST CVDD\_OV DVDD\_OV AVDDREF\_OV AVAO\_SW\_FAIL

# FAULT\_COMM1

2104 R "0000 0000" RSVD FCOMM\_DET FTONE\_DET HB\_FAIL HB\_FAST UART\_FRAME COMMCLR\_DET STOP\_DET

# FAULT\_COMM2

2105 R "0000 0000" RSVD RSVD SPI\_FRAME SPI\_PHY COML\_FRAME COML\_PHY COMH\_FRAME COMH\_PHY

# DEV\_DIAG\_STAT

2110 R "0000 0000" RSVD RSVD RSVD RSVD RSVD RSVD PWR\_DIAG\_RDY INH\_STAT

# PARTID

2120 R "0000 0000" REV\[7\] REV\[6\] REV\[5\] REV\[4\] REV\[3\] REV\[2\] REV\[1\] REV\[0\]

# DIE\_ID1

2121 R "0000 0000" ID\[7\] ID\[6\] ID\[5\] ID\[4\] ID\[3\] ID\[2\] ID\[1\] ID\[0\]

# DIE\_ID2

2122 R "0000 0000" ID\[7\] ID\[6\] ID\[5\] ID\[4\] ID\[3\] ID\[2\] ID\[1\] ID\[0\]

# DIE\_ID3

2123 R "0000 0000" ID\[7\] ID\[6\] ID\[5\] ID\[4\] ID\[3\] ID\[2\] ID\[1\] ID\[0\]

# DIE\_ID4

2124 R "0000 0000" ID\[7\] ID\[6\] ID\[5\] ID\[4\] ID\[3\] ID\[2\] ID\[1\] ID\[0\]

# DIE\_ID5

2125 R "0000 0000" ID\[7\] ID\[6\] ID\[5\] ID\[4\] ID\[3\] ID\[2\] ID\[1\] ID\[0\]

# DIE\_ID6

2126 R "0000 0000" ID\[7\] ID\[6\] ID\[5\] ID\[4\] ID\[3\] ID\[2\] ID\[1\] ID\[0\]

# DIE\_ID7

2127 R "0000 0000" ID\[7\] ID\[6\] ID\[5\] ID\[4\] ID\[3\] ID\[2\] ID\[1\] ID\[0\]

# DIE\_ID8

2128 R "0000 0000" ID\[7\] ID\[6\] ID\[5\] ID\[4\] ID\[3\] ID\[2\] ID\[1\] ID\[0\]

# DIE\_ID9

2129 R "0000 0000" ID\[7\] ID\[6\] ID\[5\] ID\[4\] ID\[3\] ID\[2\] ID\[1\] ID\[0\]

# DEBUG\_CTRL\_UNLOCK 2200 R/W

"0000 0000" CODE\[7\] CODE\[6\] CODE\[5\] CODE\[4\] CODE\[3\] CODE\[2\] CODE\[1\] CODE\[0\]

# DEBUG\_COMM\_CTRL

2201 R/W **"0111 1000"** RSVD COML\_TX\_EN COML\_RX\_EN COMH\_TX\_EN COMH\_RX\_EN UART\_VIF\_BAUD USER\_UART\_EN USER\_DAISY\_EN

# DEBUG\_COMM\_STAT

2300 R **"0001 0011"** RSVD RSVD RSVD HW\_DAISY\_DRV COML\_TX\_ON COML\_RX\_ON COMH\_TX\_ON COMH\_RX\_ON

# DEBUG\_SPI\_PHY

2301 R "0000 0000" RSVD FMT\_ERR COMCLR\_ERR TXDATA\_UNEXP RXDATA\_UNEXP TXFIFO\_OF TXFIFO\_UF RXFIFO\_OF

# DEBUG\_SPI\_FRAME

2302 R "0000 0000" RSVD RSVD TR\_SOF TR\_WAIT RC\_IERR RC\_SOF RC\_BYTE\_ERR RC\_CRC

# DEBUG\_UART\_FRAME 2303 R

"0000 0000" RSVD RSVD TR\_SOF TR\_WAIT RC\_IERR RC\_SOF RC\_BYTE\_ERR RC\_CRC

# DEBUG\_COMH\_PHY

2304 R "0000 0000" RSVD RSVD RSVD PERR BERR\_TAG SYNC2 SYNC1 BIT

# DEBUG\_COMH\_FRAME 2305 R

"0000 0000" RSVD RSVD RSVD RR\_IERR RR\_SOF RR\_BYTE\_ERR RR\_UNEXP RR\_CRC

# DEBUG\_COML\_PHY

2306 R "0000 0000" RSVD RSVD RSVD PERR BERR\_TAG SYNC2 SYNC1 BIT

# DEBUG\_COML\_FRAME 2307 R

"0000 0000" RSVD RSVD RSVD RR\_IERR RR\_SOF RR\_BYTE\_ERR RR\_UNEXP RR\_CRC

# Figure 7-28. Register Summary

# www.ti.com

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

# Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback*

## 7.5.1 Register Summary Table

# ADDRESS

REGISTER DESCRIPTION R/W MODE RESET VALUE NVM VALUES INCLUDED IN NVM?

0x306 DIR0\_ADDR Device Address North Direction R/W 0x00 n/a no

0x307 DIR1\_ADDR Device Address South Direction R/W 0x00 n/a no 0x309 CONTROL1 Control1 R/W 0x00 n/a no 0x30A CONTROL2 Control2 R/W 0x00 n/a no

0x2000 DIAG\_CTRL Diagnostic Control R/W 0x00 n/a no

0x2001 DEV\_CONF1 Device Configure1 R/W 0x14 n/a no

0x2002 DEV\_CONF2 Device Configure2 R/W 0x00 n/a no

0x2003 TX\_HOLD\_OFF Transmitter Hold off Control R/W 0x00 n/a no

0x2004 SLP\_TIMEOUT Sleep Timer R/W 0x03 n/a no

0x2005 COMM\_TIMEOUT Communication Timeout Control R/W 0x34 n/a no

0x2010 SPI\_FIFO\_UNLOCK FIFO Diagnostic Unlock R/W 0x00 n/a no 0x2020 FAULT\_MSK Fault Mask R/W 0x00 n/a no 0x2030 FAULT\_RST Fault Reset R/W 0x00 n/a no

0x2100 FAULT\_SUMMARY Fault Summary R 0x00 n/a no

0x2101 FAULT\_REG Register Fault R 0x00 n/a no 0x2102 FAULT\_SYS System Fault R 0x00 n/a no 0x2103 FAULT\_PWR Power Fault R 0x00 n/a no

0x2104 FAULT\_COMM1 Communication Fault1 R 0x00 n/a no

0x2105 FAULT\_COMM2 Communication Fault2 R 0x00 n/a no

0x2110 DEV\_DIAG\_STAT Diagnostic Status R 0x00 n/a no 0x2120 PARTID Part ID R 0x00 various yes 0x2121 DIE\_ID1 Die ID1 R 0x00 various yes 0x2122 DIE\_ID2 Die ID2 R 0x00 various yes 0x2123 DIE\_ID3 Die ID3 R 0x00 various yes 0x2124 DIE\_ID4 Die ID4 R 0x00 various yes 0x2125 DIE\_ID5 Die ID5 R 0x00 various yes 0x2126 DIE\_ID6 Die ID6 R 0x00 various yes 0x2127 DIE\_ID7 Die ID7 R 0x00 various yes 0x2128 DIE\_ID8 Die ID8 R 0x00 various yes 0x2129 DIE\_ID9 Die ID9 R 0x00 various yes

0x2200 DEBUG\_CTRL\_UNLOCK Debug Control Unlock R/W 0x00 n/a no

0x2201 DEBUG\_COMM\_CTRL Debug Communication Control R/W 0x78 n/a no

0x2300 DEBUG\_COMM\_STAT Debug Communication Status R 0x13 n/a no

0x2301 DEBUG\_SPI\_PHY SPI Physical Layer Error R 0x00 n/a no

0x2302 DEBUG\_SPI\_FRAME SPI Frame Layer Error R 0x00 n/a no

0x2303 DEBUG\_UART\_FRAME UART Frame Layer Error R 0x00 n/a no

0x2304 DEBUG\_COMH\_PHY COMH Physical Layer Error R 0x00 n/a no

0x2305 DEBUG\_COMH\_FRAME COMH Frame Layer Error R 0x00 n/a no

0x2306 DEBUG\_COML\_PHY COML Physical Layer Error R 0x00 n/a no

0x2307 DEBUG\_COML\_FRAME COML Frame Layer Error R 0x00 n/a no

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2020 Texas Instruments Incorporated

## 7.5.2 Register: DIR0\_ADDR Address: 0x306

# B7 B6 B5 B4 B3 B2 B1 B0

# RSVD ADDRESS\[5:0\]

# RW RW RW RW RW RW RW RW

ADDRESS \[5:0\] Follow steps in section "Device Addressing" to config this register. Always shows the current Device Address used by the device when $$ [DIR_SEL] = 0. $$ Default to 0x00 when digital core out of digital reset. MCU can re-address the device by writing a different device address to this register, and the device will take on the new address immediately.

## 7.5.3 Register: DIR1\_ADDR Address: 0x307

# B7 B6 B5 B4 B3 B2 B1 B0

# RSVD ADDRESS\[5:0\]

# RW RW RW RW RW RW RW RW

ADDRESS \[5:0\] Follow steps in section "Device Addressing" to config this register. Always shows the current Device Address used by the device when $$ [DIR_SEL] = 1. $$ Default to 0x00 when digital core out of digital reset. MCU can re-address the device by writing a different device address to this register, and the device will take on the new address immediately.

## 7.5.4 Register: CONTROL1 Address: 0x0309

# B7 B6 B5 B4 B3 B2 B1 B0

# DIR\_SEL SEND\_SHUTDO WN

# SEND\_WAKE SEND\_SLPTOAC T

# GOTO\_SHUTDO WN

# GOTO\_SLEEP SOFT\_RESET ADDR\_WR

# RW RW RW RW RW RW RW RW

DIR\_SEL Select daisy chain comm direction. Not self-clear bit. 0: In a device, command frame travels from MCU to COMH 1: In a device, command frame travels from MCU to COML

# SEND\_SHUTDO WN

Sends SHUTDOWN tone to next device up the stack. The device receiving this bit is unaffected. Self-clear bit. 0: Ready 1: Send SHUTDWON tone up the stack

SEND\_WAKE Send WAKE tone up the stack. Self-clear bit. 0: Ready 1: Send WAKE tone up the stack, then reset its own

# SEND\_SLPTOAC T

Send SLEEPtoWAKE tone up the stack. Self-clear bit. 0: Ready 1: Send SLEEPtoWAKE tone up the stack

# GOTO\_SHUTDO WN

Transition device to SHUTDOWN mode. Self-clear bit. 0: Ready 1: Enter SHUTDOWN mode

| GOTO\_SLEEP | Transition device to SLEEP mode. Self-clear bit. | 0: Ready | 1: Enter SLEEP mode |
|:--- |:--- |:--- |:--- |
| SOFT\_RESET | Reset the digital to OTP default. Self-clear bit. | 0: Ready | 1: Reset device |
| ADDR\_WR | Enable device to start auto-addressing. See auto-addressing chapter for detail. Self cleared. | 0: Not performing auto-address. Device forwards communication transaction as normal | 1: Device is being auto-addressed; the 1st communication transaction it received will not be forwarded. |

SOFT\_RESET Reset the digital to OTP default. Self-clear bit. 0: Ready 1: Reset device

ADDR\_WR Enable device to start auto-addressing. See auto-addressing chapter for detail. Self cleared. 0: Not performing auto-address. Device forwards communication transaction as normal 1: Device is being auto-addressed; the 1st communication transaction it received will not be forwarded. **<https://www.ti.com**>

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback*

## 7.5.5 Register: CONTROL2 Address: 0x30A

# B7 B6 B5 B4 B3 B2 B1 B0

# RSVD SEND\_HW\_RESE T

# SPARE

# RW RW RW RW RW RW RW RW

# SEND\_HW\_RESE T

Send HW\_RESET tone up the stack. Self-clear bit. 0: Ready 1: Send HW\_RESET tone to next stack device up

## 7.5.6 Register: DIAG\_CTRL Address: 0x2000

# B7 B6 B5 B4 B3 B2 B1 B0

# RSVD

CONF\_MON\_GO PWR\_DIAG\_GO SPI\_FIFO\_DIAG\_ GO

# FLIP\_FACT\_CRC FLIP\_TR\_CRC INH\_SET\_GO

# RW RW RW RW RW RW RW RW

CONF\_MON\_GO Resample the 2 registers (DEV\_CONF1, FAULT\_MSK) setting that bit flip monitor checks against. self-clear bit. For usage, refer to paragraph: Register Bit Flip Monitor 0: No action 1: Resample 2 registers setting

PWR\_DIAG\_GO Indicates a power supply BIST diagnostic is initiated, self-clear bit. 0: No action 1: Initiate power BIST diagnostic

# SPI\_FIFO\_DIAG\_ GO

| Write the unlock code 0x0A to SPI\_FIFO\_UNLOCK and followed by writing \[SPI\_FIFO\_DIAG\_GO\] = 1 to do FIFO diagnostic. For detailed | steps of FIFO diagnostic, refer to safety manual. This bit is self-cleared. | 0: No action | 1: Initiate SPI FIFO diagnostic |
|:--- |:--- |:--- |:--- |
| FLIP\_FACT\_CRC | An enable bit to flip the factory CRC expected value. This is for factory CRC diagnostic. | 0: No action | 1: flip the CRC expected value. This will cause a factory CRC fault, FAULT\_REG\[FACT\_CRC\] |
| FLIP\_TR\_CRC | Sends a purposely incorrect communication (during transmitting response) CRC by inverting all of the calculated CRC bits | 0: Send CRC as calculated | 1: Send inverted CRC |
| INH\_SET\_GO | This bits intentionally activates INH PMOS pull up, sets \[INH\] and \[INH\_STAT\] to 1. (self-cleared) | 0: mission mode | 1: Trigger INH PMOS pull up |

FLIP\_FACT\_CRC An enable bit to flip the factory CRC expected value. This is for factory CRC diagnostic. 0: No action 1: flip the CRC expected value. This will cause a factory CRC fault, FAULT\_REG\[FACT\_CRC\]

FLIP\_TR\_CRC Sends a purposely incorrect communication (during transmitting response) CRC by inverting all of the calculated CRC bits 0: Send CRC as calculated 1: Send inverted CRC

INH\_SET\_GO This bits intentionally activates INH PMOS pull up, sets \[INH\] and \[INH\_STAT\] to 1. (self-cleared) 0: mission mode 1: Trigger INH PMOS pull up

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2020 Texas Instruments Incorporated

## 7.5.7 Register: DEV\_CONF1 Address: 0x2001

# B7 B6 B5 B4 B3 B2 B1 B0

# SNIFDET\_EN

SNIFDET\_DIS TONE\_RX\_EN FCOMM\_EN TWO\_STOP\_EN NFAULT\_EN RESERVED HB\_TX\_EN

# RW RW RW RW RW RW RW RW

SNIFDET\_EN Enable the Sniff detector on COM\* port, this bit is latched into AVAOREF domain, once latched in, this bit is still effective in SHUTDOWN 0: no effect 1: SNIF DET is enabled in SHUTDOWN

SNIFDET\_DIS Enable the Sniff detector on COM\* port, this bit is latched into AVAOREF domain, once latched in, this bit is still effective in SHUTDOWN 0: no effect 1: SNIF DET is disabled in SHUTDOWN, if both SNIFDET\_EN and SNIFDET\_DIS are '1', SNIFDET\_DIS takes priority.

TONE\_RX\_EN Enable the Tone receiver, depends on \[DIR\_SEL\], one of the COML/COMH tone recover is enabled. COMH/COML tone receivers are enabled in VALIDATE disregarding setting of this bit. 0: Disable 1: Enable

| FCOMM\_EN | Enable the fault state detection through communication in ACTIVE mode | 0: Disable | 1: Enable |
|:--- |:--- |:--- |:--- |
| TWO\_STOP\_EN | Enables two stop bits for the UART in case of severe oscillator error in both the host and device | 0: One STOP bit | 1: Two STOP bit |
| NFAULT\_EN | Enables the NFAULT function | 0: NFAULT driver is disabled | 1: NFAULT pulls low to indicate an unmasked fault is detected |

TWO\_STOP\_EN Enables two stop bits for the UART in case of severe oscillator error in both the host and device 0: One STOP bit 1: Two STOP bit

NFAULT\_EN Enables the NFAULT function 0: NFAULT driver is disabled 1: NFAULT pulls low to indicate an unmasked fault is detected

RESERVED Reserved. Default value is 0. Please don't alter.

HB\_TX\_EN Enable HEARTBEAT transmitter when device is in SLEEP mode 0: Disable 1: Enable

## 7.5.8 Register: DEV\_CONF2 Address: 0x2002

# B7 B6 B5 B4 B3 B2 B1 B0

# RSVD INH\_DIS\[1:0\]

# RW RW RW RW RW RW RW RW

INH\_DIS\[1:0\] Disable INH driver (PMOS pull up). In all modes, this bit overwrites \[INH\_SET\_GO\] and fault tone detection event 00: INH function is enabled 01: INH function is enabled 10: INH function is enabled 11: INH function is DISABLED

## 7.5.9 Register: TX\_HOLD\_OFF Address: 0x2003

# B7 B6 B5 B4 B3 B2 B1 B0

# DLY\[7:0\]

# RW RW RW RW RW RW RW RW

DLY\[7:0\] Set the number of bit period delay from 0 to 255, after receiving the STOP bit of a command frame and before transmitting the 1st bit of response frame **<https://www.ti.com**>

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback*

## 7.5.10 Register: SLP\_TIMEOUT Address: 0x2004

# B7 B6 B5 B4 B3 B2 B1 B0

# RSVD SLP\_TME\[2:0\]

# RW RW RW RW RW RW RW RW

SLP\_TME\[2:0\] This timer starts counting when device enters SLEEP or VALIDATE. When the timer expires, the device enters SHUTDOWN. The timer reset if device wakes up to ACTIVE. 000: no timeout. Device remains in SLEEP 001: 5s 010: 10s 011: 1min 100: 10mins 101: 30mins 110: 1hour 111: 2hours

## 7.5.11 Register: COMM\_TIMEOUT Address: 0x2005

# B7 B6 B5 B4 B3 B2 B1 B0

# RSVD CTS\_TIME\[2:0\] CTL\_ACT CTL\_TIME\[2:0\]

# RW RW RW RW RW RW RW RW

CTS\_TIME\[2:0\] Set the short communication timeout. When this timer expires, the device set the FAULT\_SYS \[CTS\] bit. This can be used as an alert to the system to prevent a long communication timeout. 000: disable short communication timeout 001: 100ms 010: 2s 011: 10s (default) 100: 1min 101: 10mins 110: 30min 111: 1hour

CTL\_ACT Configure the device action when long communication timeout timer expires 0: set FAULT\_SYS\[CTL\] and send device to SLEEP mode (default at reset) 1: Send the device to SHUTDOWN. FAULT\_SYS\[CTL\] bit will not be set

CTL\_TIME\[2:0\] Set the long communication timeout. When this timer expires, the device takes the action configured by the \[CTL\_ACT\] bit. 000: disable long communication timeout 001: 100ms 010: 2s 011: 10s 100: 1min (default) 101: 10mins 110: 30min 111: 1hour

## 7.5.12 Register: SPI\_FIFO\_UNLOCK Address: 0x2010

# B7 B6 B5 B4 B3 B2 B1 B0

# RSVD CODE\[3:0\]

# RW RW RW RW RW RW RW RW

CODE\[3:0\] In UART mode - write has no impact and read always returns 0 In SPI mode - Write the unlock code 0x0A to SPI\_FIFO\_UNLOCK (MSB 4 bits are don't care, e.g. 0x2A would also unlock) and followed by writing \[SPI\_FIFO\_DIAG\_GO\] = 1 to do FIFO diagnostic. For detailed steps of FIFO diagnostic, refer to safety manual. After these bits are written, read cmd doesn't affect them while any write cmd clears them.

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2020 Texas Instruments Incorporated

## 7.5.13 Register: FAULT\_MSK Address: 0x2020

# B7 B6 B5 B4 B3 B2 B1 B0

# MSK\_COML\_H MSK\_UART\_SPI MSK\_FCOMM\_D ET

# MSK\_FTONE\_DE T

# MSK\_HB MSK\_REG MSK\_SYS MSK\_PWR

# RW RW RW RW RW RW RW RW

MSK\_COML\_H If this bit is set, \[FAULT\_COMM\] bit in FAULT\_SUMMARY register is not set (NFAULT won't toggle) due to bits: \[COML\_FRAME\], \[COMH\_FRAME\], \[COML\_PHY\], \[COMH\_PHY\] and registers: DEBUG\_COMH\_PHY, DEBUG\_COMH\_FRAME, DEBUG\_COML\_PHY, DEBUG\_COML\_FRAME 0: Assert NFAULT and set \[FAULT\_COMM\] if fault above is detected 1: No NFAULT action, \[FAULT\_COMM\] not set due to faults above

MSK\_UART\_SPI If this bit is set, \[FAULT\_COMM\] bit in FAULT\_SUMMARY register is not set (NFAULT won't toggle) due to \[STOP\_DET\], \[COMMCLR\_DET\], \[UART\_FRAME\], \[SPI\_FRAME\], \[SPI\_PHY\] bits and DEBUG\_UART\_FRAME, DEBUG\_SPI\_PHY, DEBUG\_SPI\_FRAME registers 0: Assert NFAULT and set \[FAULT\_COMM\] if fault above is detected 1: No NFAULT action, \[FAULT\_COMM\] not set due to faults above

# MSK\_FCOMM\_D ET

If this bit is set, \[FAULT\_COMM\] bit in FAULT\_SUMMARY register is not set (NFAULT won't toggle) due to \[FCOMM\_DET\] 0: Assert NFAULT and set \[FAULT\_COMM\] if fault above is detected 1: No NFAULT action, \[FAULT\_COMM\] not set due to faults above

# MSK\_FTONE\_DE T

If this bit is set, \[FAULT\_COMM\] bit in FAULT\_SUMMARY register is not set (NFAULT won't toggle) due to \[FTONE\_DET\] 0: Assert NFAULT and set \[FAULT\_COMM\] if fault above is detected 1: No NFAULT action, \[FAULT\_COMM\] not set due to faults above

MSK\_HB If this bit is set, \[FAULT\_COMM\] bit in FAULT\_SUMMARY register is not set (NFAULT won't toggle) due to \[HB\_FAIL\] and \[HB\_FAST\] 0: Assert NFAULT and set \[FAULT\_COMM\] if fault above is detected 1: No NFAULT action, \[FAULT\_COMM\] not set due to faults above

| MSK\_REG | If this bit is set, \[FAULT\_REG\] bit in FAULT\_SUMMARY register is not set and NFAULT won't toggle due to OTP fault. It doesn't affect | FAULT\_REG register. | 0: Mask disabled | 1: Mask enabled to prevent fault signaling |
|:--- |:--- |:--- |:--- |:--- |
| MSK\_SYS | If this bit is set, \[FAULT\_SYS\] bit in FAULT\_SUMMARY register is not set and NFAULT won't toggle due to SYS fault. It doesn't affect | FAULT\_SYS register. | 0: Assert NFAULT if any bit from FAULT\_SYS is set to '1' | 1: No NFAULT action regardless of FAULT\_SYS status |
| MSK\_PWR | If this bit is set, \[FAULT\_PWR\] bit in FAULT\_SUMMARY register is not set and NFAULT won't toggle due to PWR fault. It doesn't affect | FAULT\_PWR register. | 0: Mask disabled | 1: Mask enabled to prevent fault signaling |

MSK\_SYS If this bit is set, \[FAULT\_SYS\] bit in FAULT\_SUMMARY register is not set and NFAULT won't toggle due to SYS fault. It doesn't affect FAULT\_SYS register. 0: Assert NFAULT if any bit from FAULT\_SYS is set to '1' 1: No NFAULT action regardless of FAULT\_SYS status

MSK\_PWR If this bit is set, \[FAULT\_PWR\] bit in FAULT\_SUMMARY register is not set and NFAULT won't toggle due to PWR fault. It doesn't affect FAULT\_PWR register. 0: Mask disabled 1: Mask enabled to prevent fault signaling **<https://www.ti.com**>

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback*

## 7.5.14 Register: FAULT\_RST Address: 0x2030

# B7 B6 B5 B4 B3 B2 B1 B0

# RST\_COML\_H RST\_UART\_SPI RST\_FCOMM\_DE T

# RST\_FTONE\_DE T

# RST\_HB RST\_REG RST\_SYS RST\_PWR

# RW RW RW RW RW RW RW RW

RST\_COML\_H Reset bits: COML\_FRAME, COMH\_FRAME, COML\_PHY, COMH\_PHY and registers: DEBUG\_COMH\_PHY, DEBUG\_COMH\_FRAME, DEBUG\_COML\_PHY, DEBUG\_COML\_FRAME. self-cleared bit. 0: Do not reset 1: Reset to 0x00

RST\_UART\_SPI Reset STOP\_DET, COMMCLR\_DET, UART\_FRAME, SPI\_FRAME, SPI\_PHY bits and DEBUG\_UART\_FRAME, DEBUG\_SPI\_PHY, DEBUG\_SPI\_FRAME registers. self-cleared bit. 0: Do not reset 1: Reset to 0x00

# RST\_FCOMM\_DE T

Reset FCOMM\_DET bit, self-cleared bit. 0: Do not reset 1: Reset to '0'

# RST\_FTONE\_DE T

Reset FTONE\_DET bit, self-cleared bit. 0: Do not reset 1: Reset to '0'

| RST\_HB | Reset HB\_FAIL and HB\_FAST bit, self-cleared bit. | 0: Do not reset | 1: Reset to '0' |
|:--- |:--- |:--- |:--- |
| RST\_REG | Resets FAULT\_SUMMARY \[FAULT\_REG\] to '0', self-cleared bit. | 0: Do not reset | 1: Reset to '0' |
| RST\_SYS | This bit is self-clear to 0 after writing to 1. | 0: Do not reset | 1: Reset register FAULT\_SYS and \[FAULT\_SYS\] to 0x00 and '0' |
| RST\_PWR | Resets FAULT\_SUMMARY \[FAULT\_PWR\] to '0' and register FAULT\_PWR, self-cleared bit. | 0: Do not reset | 1: Reset |

RST\_REG Resets FAULT\_SUMMARY \[FAULT\_REG\] to '0', self-cleared bit. 0: Do not reset 1: Reset to '0'

RST\_SYS This bit is self-clear to 0 after writing to 1. 0: Do not reset 1: Reset register FAULT\_SYS and \[FAULT\_SYS\] to 0x00 and '0'

RST\_PWR Resets FAULT\_SUMMARY \[FAULT\_PWR\] to '0' and register FAULT\_PWR, self-cleared bit. 0: Do not reset 1: Reset

## 7.5.15 Register: FAULT\_SUMMARY Address: 0x2100

# B7 B6 B5 B4 B3 B2 B1 B0

# RSVD FAULT\_COMM FAULT\_REG FAULT\_SYS FAULT\_PWR

# R R R R R R R R

| FAULT\_COMM | Indicate communication related fault is detected (any bits in register FAULT\_COMM1, FAULT\_COMM2 is set) | 0: No fault | 1: Fault |
|:--- |:--- |:--- |:--- |
| FAULT\_REG | Indicate registers related fault is detected | 0: No fault | 1: Fault |
| FAULT\_SYS | Indicates system fault is detected (any bits in register FAULT\_SYS). | 0: No fault | 1: Fault |
| FAULT\_PWR | Indicates a power supply fault is detected (any bits in register FAULT\_PWR) | 0: No fault | 1: Fault |

FAULT\_REG Indicate registers related fault is detected 0: No fault 1: Fault

FAULT\_SYS Indicates system fault is detected (any bits in register FAULT\_SYS). 0: No fault 1: Fault

FAULT\_PWR Indicates a power supply fault is detected (any bits in register FAULT\_PWR) 0: No fault 1: Fault

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2020 Texas Instruments Incorporated

## 7.5.16 Register: FAULT\_REG Address: 0x2101

# B7 B6 B5 B4 B3 B2 B1 B0

# RSVD CONF\_MON\_ERR FACTLDERR FACT\_CRC

# R R R R R R R R

# CONF\_MON\_ER R

| Indicates monitored 2 registers (DEV\_CONF1, FAULT\_MSK) have at least one bit flip. For usage, refer to paragraph: Register Bit Flip | Monitor. | 0: No fault | 1: Fault |
|:--- |:--- |:--- |:--- |
| FACTLDERR | Indicates the factory NVM registers could not be loaded from OTP. | 0: No fault | 1: Fault |
| FACT\_CRC | Indicates a CRC error has occurred in the factory register space. | 0: No fault | 1: Fault |

FACTLDERR Indicates the factory NVM registers could not be loaded from OTP. 0: No fault 1: Fault

FACT\_CRC Indicates a CRC error has occurred in the factory register space. 0: No fault 1: Fault

## 7.5.17 Register: FAULT\_SYS Address: 0x2102

# B7 B6 B5 B4 B3 B2 B1 B0

# VALIDATE\_DET LFO SHUTDOWN\_REC DRST CTL CTS TSHUT INH

# R R R R R R R R

VALIDATE\_DET Indicates device transitioned to VALIDATE mode 0: no transitioned to VALIDATE MODE 1: transitioned to VALIDATE MODE

LFO Indicated LFO frequency is off by +/-25% 0: no fault 1: fault

# SHUTDOWN\_RE C

Indicates the device was shut down using SHUTDOWN ping. If this bit is set, the COML and COMH RX are both disabled at wake up as a way to isolate itself from the stack. Send another wake ping or \[SOFT\_RESET\] to re-enable COMH/L RX. 0: The previous SHUTDOWN was normal 1: The previous SHUTDOWN was caused by ping, which is not a usual SHUTDOWN method, indicating potential communication issue with the device

DRST Indicates a digital reset has occurred. 0: no digital reset 1: digital reset has occurred

CTL Indicates a long communication timeout occurred. Device action is configured by \[CTL\_ACT\]. This bit is not observable if the action is set to device shutdown. 0: No fault 1: long communication timeout occurs. Observable if long timeout action is set to SLEEP

CTS Indicates a short communication timeout occurred. No action from the device. This can be served as an alert to system before reaching long communication timeout. 0: No fault 1: short communication timeout occurs

TSHUT Indicates the previous shutdown was due to thermal shutdown 0: die temp is \< thermal shutdown threshold 1: the previous shutdown was to due thermal shutdown

INH Indicates INH PMOS is enabled 0: INH driver is off 1: INH driver enabled, pulls pin up to BAT **<https://www.ti.com**>

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback*

## 7.5.18 Register: FAULT\_PWR Address: 0x2103

# B7 B6 B5 B4 B3 B2 B1 B0

# RSVD

CVDD\_UV\_DRST CVDD\_OV DVDD\_OV AVDDREF\_OV AVAO\_SW\_FAIL

# R R R R R R R R

| CVDD\_UV\_DRST | Indicates CVDDUV fault caused DRST. Shutdown/power up event shall not trigger this fault. | 0: no fault | 1: fault |
|:--- |:--- |:--- |:--- |
| CVDD\_OV | Indicates an over voltage fault on the CVDD pin | 0: no fault | 1: fault |
| DVDD\_OV | Indicates an over voltage fault on the DVDD pin | 0: no fault | 1: fault |
| AVDDREF\_OV | Indicates an over voltage fault on the AVDD\_REF internal supply | 0: no fault | 1: fault |
| AVAO\_SW\_FAIL | Indicates a fault is detected on the AVAO\_REF switch. | 0: no fault | 1: fault |

CVDD\_OV Indicates an over voltage fault on the CVDD pin 0: no fault 1: fault

DVDD\_OV Indicates an over voltage fault on the DVDD pin 0: no fault 1: fault

AVDDREF\_OV Indicates an over voltage fault on the AVDD\_REF internal supply 0: no fault 1: fault

AVAO\_SW\_FAIL Indicates a fault is detected on the AVAO\_REF switch. 0: no fault 1: fault

## 7.5.19 Register: FAULT\_COMM1 Address: 0x2104

# B7 B6 B5 B4 B3 B2 B1 B0

# RSVD

FCOMM\_DET FTONE\_DET HB\_FAIL HB\_FAST UART\_FRAME COMMCLR\_DET STOP\_DET

# R R R R R R R R

| FCOMM\_DET | Indicates the fault status bit in comm frame is set by stack devices. At least a fault in stack devices happened. Only apply to non-bq79606 | family | 0: no fault | 1: fault |
|:--- |:--- |:--- |:--- |:--- |
| FTONE\_DET | Indicates the fault tone is detected, COM Port in sleep mode if work with non-bq79606 (Detection is monitoring the COML side if \[DIR\_SEL\] | = 0 and vice versa.) | 0: no fault | 1: fault |
| HB\_FAIL | Indicates HB tone is NOT detected within tHB\_PERIOD, not supported with BQ79606A-Q1 ( Detection is monitoring the COML side if | \[DIR\_SEL\] = 0 and vice versa.) | 0: no fault, HB tone detected as expected | 1: fault |

FTONE\_DET Indicates the fault tone is detected, COM Port in sleep mode if work with non-bq79606 (Detection is monitoring the COML side if \[DIR\_SEL\] = 0 and vice versa.) 0: no fault 1: fault

HB\_FAIL Indicates HB tone is NOT detected within tHB\_PERIOD, not supported with BQ79606A-Q1 ( Detection is monitoring the COML side if \[DIR\_SEL\] = 0 and vice versa.) 0: no fault, HB tone detected as expected 1: fault

HB\_FAST Indicates HB tone is detected within tHB\_FAST (too frequent), not supported with BQ79606A-Q1 ( Detection is monitoring the COML side if \[DIR\_SEL\] = 0 and vice versa.) This bit could also be set when \[FTONE\_DET\]=1 depends on how soon the Fault Tone is detected from previous Heartbeat tone. 0: no fault 1: fault

UART\_FRAME Indicates a UART FAULT detected when receiving command or transmitting response frames Further detail of the fault information is available in the DEBUG\_UART\_FRAME register 0: no fault 1: fault

COMMCLR\_DET A UART/SPI communication clear signal is detected. This bit is set when Sleep2active ping is sent in UART mode. While in SPI mode, it is not set when sleep2active ping is sent. 0: no UART/SPI Comm Clear 1: UART/SPI Comm Clear detected

STOP\_DET Indicates and unexpected STOP condition is received. Apply to UART mode. This bit is set when Sleep2active ping is sent in ACTIVE. 0: no fault 1: fault

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2020 Texas Instruments Incorporated

## 7.5.20 Register: FAULT\_COMM2 Address: 0x2105

# B7 B6 B5 B4 B3 B2 B1 B0

# RSVD

SPI\_FRAME SPI\_PHY COML\_FRAME COML\_PHY COMH\_FRAME COMH\_PHY

# R R R R R R R R

| SPI\_FRAME | Indicates a SPI frame level FAULT detected when receiving command or transmitting response frames. Further detail of the fault | information is available in the DEBUG\_SPI\_FRAME register | 0: no fault | 1: fault |
|:--- |:--- |:--- |:--- |:--- |
| SPI\_PHY | Indicates a SPI bit level FAULT detected when receiving command or transmitting response frames. Further detail of the fault information is | available in the DEBUG\_SPI\_PHY register | 0: no fault | 1: fault |
| COML\_FRAME | Indicate a COML byte level fault detected when receiving response frames. Further details of the fault information is available in | DEBUG\_COML\_FRAME | 0: no fault | 1: fault |
| COML\_PHY | Indicate a COML bit level fault detected, which would cause at least a byte level (RC\_RR) fault. Further details of the fault information are | available in DEBUG\_COML\_PHY register. | 0: no fault | 1: fault |
| COMH\_FRAME | Indicate a COMH byte level fault detected when receiving response frames. Further details of the fault information is available in | DEBUG\_COMH\_FRAME | 0: no fault | 1: fault |
| COMH\_PHY | Indicate a COMH bit level fault detected, which would cause at least a byte level (RC\_RR) fault. Further details of the fault information are | available in DEBUG\_COMH\_PHY register. | 0: no fault | 1: fault |

SPI\_PHY Indicates a SPI bit level FAULT detected when receiving command or transmitting response frames. Further detail of the fault information is available in the DEBUG\_SPI\_PHY register 0: no fault 1: fault

COML\_FRAME Indicate a COML byte level fault detected when receiving response frames. Further details of the fault information is available in DEBUG\_COML\_FRAME 0: no fault 1: fault

COML\_PHY Indicate a COML bit level fault detected, which would cause at least a byte level (RC\_RR) fault. Further details of the fault information are available in DEBUG\_COML\_PHY register. 0: no fault 1: fault

COMH\_FRAME Indicate a COMH byte level fault detected when receiving response frames. Further details of the fault information is available in DEBUG\_COMH\_FRAME 0: no fault 1: fault

COMH\_PHY Indicate a COMH bit level fault detected, which would cause at least a byte level (RC\_RR) fault. Further details of the fault information are available in DEBUG\_COMH\_PHY register. 0: no fault 1: fault

## 7.5.21 Register: DEV\_DIAG\_STAT Address: 0x2110

# B7 B6 B5 B4 B3 B2 B1 B0

# RSVD PWR\_DIAG\_RDY INH\_STAT

# R R R R R R R R

PWR\_DIAG\_RDY Indicates a power supply BIST test is done. It is cleared when \[PWR\_DIAG\_GO\] bit is set. 0: BIST is not done 1: BIST is done

INH\_STAT Indicates INH Pin see VINH\_DET, this bit reflects real time value of pin INH 0: Voltage not detected 1: Voltage detected

## 7.5.22 Register: PARTID Address: 0x2120

# B7 B6 B5 B4 B3 B2 B1 B0

# REV\[7:0\]

# R R R R R R R R

REV\[7:0\] Device revision 0x00 = A0, 0x01 = A1, 0x02 = A2, etc. **<https://www.ti.com**>

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback*

## 7.5.23 Register: DIE\_ID1 Address: 0x2121

# B7 B6 B5 B4 B3 B2 B1 B0

# ID\[7:0\]

# R R R R R R R R

ID\[7:0\] Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM.

## 7.5.24 Register: DIE\_ID2 Address: 0x2122

# B7 B6 B5 B4 B3 B2 B1 B0

# ID\[7:0\]

# R R R R R R R R

ID\[7:0\] Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM.

## 7.5.25 Register: DIE\_ID3 Address: 0x2123

# B7 B6 B5 B4 B3 B2 B1 B0

# ID\[7:0\]

# R R R R R R R R

ID\[7:0\] Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM.

## 7.5.26 Register: DIE\_ID4 Address: 0x2124

# B7 B6 B5 B4 B3 B2 B1 B0

# R R R R R R R R

ID\[7:0\] Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM.

## 7.5.27 Register: DIE\_ID5 Address: 0x2125

# B7 B6 B5 B4 B3 B2 B1 B0

# ID\[7:0\]

# R R R R R R R R

ID\[7:0\] Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM.

## 7.5.28 Register: DIE\_ID6 Address: 0x2126

# B7 B6 B5 B4 B3 B2 B1 B0

# ID\[7:0\]

# R R R R R R R R

ID\[7:0\] Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM.

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2020 Texas Instruments Incorporated

## 7.5.29 Register: DIE\_ID7 Address: 0x2127

# B7 B6 B5 B4 B3 B2 B1 B0

# ID\[7:0\]

# R R R R R R R R

ID\[7:0\] Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM.

## 7.5.30 Register: DIE\_ID8 Address: 0x2128

# B7 B6 B5 B4 B3 B2 B1 B0

# ID\[7:0\]

# R R R R R R R R

ID\[7:0\] Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM.

## 7.5.31 Register: DIE\_ID9 Address: 0x2129

# B7 B6 B5 B4 B3 B2 B1 B0

# ID\[7:0\]

# R R R R R R R R

ID\[7:0\] Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM.

## 7.5.32 Register: DEBUG\_CTRL\_UNLOCK Address: 0x2200

# B7 B6 B5 B4 B3 B2 B1 B0

# CODE\[7:0\]

# RW RW RW RW RW RW RW RW

CODE\[7:0\] Write the unlock code (0xA5) to this register to activate the setting in the DEBUG\_COMM\_CTRL register. Any other value than the unlock code will deactivate any effect in the DEBUG\_COMM\_CTRL setting and return to the device's normal setting. This register doesn't affect DEBUG\_COMM\_STAT register. **<https://www.ti.com**>

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback*

## 7.5.33 Register: DEBUG\_COMM\_CTRL Address: 0x2201

# B7 B6 B5 B4 B3 B2 B1 B0

# RSVD

COML\_TX\_EN COML\_RX\_EN COMH\_TX\_EN COMH\_RX\_EN UART\_VIF\_BAUD USER\_UART\_E N

# USER\_DAISY\_EN

# RW RW RW RW RW RW RW RW

| COML\_TX\_EN | Enable COML transmitter | 0: disable | 1: enable |
|:--- |:--- |:--- |:--- |
| COML\_RX\_EN | Enable COML receiver | 0: disable | 1: enable |
| COMH\_TX\_EN | Enable COMH transmitter | 0: disable | 1: enable |
| COMH\_RX\_EN | Enable COMH receiver | 0: disable | 1: enable |

COML\_RX\_EN Enable COML receiver 0: disable 1: enable

COMH\_TX\_EN Enable COMH transmitter 0: disable 1: enable

COMH\_RX\_EN Enable COMH receiver 0: disable 1: enable

UART\_VIF\_BAUD This bit changes the baud rate of UART and Daisy Chain (Also called VIF) to 250kb/s. Useful on Daisy Chain debug. When system set all the daisy chain devices to the 250kb/s baud rate, it slows down the response byte through the Daisy Chain to increase the robustness of the Daisy Chain for debug purpose. 0: 1Mbps 1: 250kbps

USER\_UART\_EN This bit enables \[UART\_VIF\_BAUD\] setting 0: disable 1: enable

# USER\_DAISY\_E N

This bit enables the setting of bits \[6:3\] in this register 0: the setting of bits \[6:3 \] of current register has no effect 1: the device will configure the COML and COMH per current register setting

## 7.5.34 Register: DEBUG\_COMM\_STAT Address: 0x2300

# B7 B6 B5 B4 B3 B2 B1 B0

# RSVD

HW\_DAISY\_DRV COML\_TX\_ON COML\_RX\_ON COMH\_TX\_ON COMH\_RX\_ON

# R R R R R R R R

HW\_DAISY\_DRV Indicates the COML and COMH are controlled by the device itself or by MCU control 0: the DEBUG\_COMM\_CTRL \[USER\_DAISY\_EN\] = 1. COML and COMH are under manual control through DEBUG\_COMM\_CTRL register 1: COML and COMH are controlled by the device

| COML\_TX\_ON | Show the current COML transmitter status | 0: Disabled | 1: Enabled |
|:--- |:--- |:--- |:--- |
| COML\_RX\_ON | Show the current COML receiver status | 0: Disables | 1: Enables |
| COMH\_TX\_ON | Show the current COMH transmitter status | 0: Disabled | 1: Enabled |
| COMH\_RX\_ON | Show the current COMH receiver status | 0: Disabled | 1: Enabled |

COML\_RX\_ON Show the current COML receiver status 0: Disables 1: Enables

COMH\_TX\_ON Show the current COMH transmitter status 0: Disabled 1: Enabled

COMH\_RX\_ON Show the current COMH receiver status 0: Disabled 1: Enabled

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2020 Texas Instruments Incorporated

## 7.5.35 Register: DEBUG\_SPI\_PHY Address: 0x2301

# B7 B6 B5 B4 B3 B2 B1 B0

# RSVD

FMT\_ERR COMCLR\_ERR TXDATA\_UNEXP RXDATA\_UNEXP TXFIFO\_OF TXFIFO\_UF RXFIFO\_OF

# R R R R R R R R

FMT\_ERR When not in Host Read mode (after sending a write cmd frame), indicates malformed cmd is received: 1. first byte of data after nCS falling edge is 0xFF 2. devices receives not multiple of 8bit. 3. In ACTIVE, nCS pulses low without SCLK toggling (send SLP2ACT ping) Comm clear doesn't trigger this fault. This fault doesn't lock down SPI interface. 0: No fault 1: Fault

COMCLR\_ERR More than 8 SCLK pulses are received during a comm clear. Once this fault is detected, device ignores the malformed comm clear. This fault doesn't affect SPI\_RDY nor data storing into RX/TX FIFO. 0: No fault 1: Fault

TXDATA\_UNEXP This fault occurs when: 1. device receives unexpected data from itself or daisy chain after a Comm clr OR 2. device receives unexpected data from daisy chain(or from bq79600) after a TX FIFO timeout. Once this fault is detected, device doesn't store any new data into RX/TX FIFO. Device sends out 0xFF on MISO after current byte finished transmission(FIFO data mask happens at byte boundary). SPI\_RDY held low till Comm Clear detected. Comm Clear needed for recovery. 0: No fault 1: Fault

RXDATA\_UNEXP Host sends data other than 0xFF during Device Read mode OR initiates SPI communication when SPI\_RDY = 0 (e.g. While FIFO2 is being filled up, host continues reading FIFO2 right after FIFO1 is read out. SPI\_DRY is low at this point) Once this fault is detected, device doesn't store any new data into RX/TX FIFO. Device would sends out 0xFF on MISO after current byte finished transmission(FIFO data mask happens at byte boundary). SPI\_RDY held low till Comm Clear detected. Comm Clear needed for recovery. 0: No fault 1: Fault

TXFIFO\_OF If SPI module receives data (from itself or daisy chain) when current FIFO is full and 2nd FIFO is not empty (host hasn't complete reading the 2nd FIFO). Once this fault is detected, device doesn't store any new data into RX/TX FIFO. Device sends out 0xFF on MISO after current byte finished transmission(FIFO data mask happens at byte boundary). SPI\_RDY held low till Comm Clear detected. Comm Clear needed for recovery. 0: No fault 1: Fault

TXFIFO\_UF In Host Read mode, when both FIFOs are empty and the host continues to send clocks for more read data (send 0xFF through MOSI). SPI Slave sets this fault flag and continues to send 0xFF on MISO when host requests data. Once this fault is detected, device doesn't store any new data into RX/TX FIFO. Device sends out 0xFF on MISO after current byte finished transmission(FIFO data mask happens at byte boundary). SPI\_RDY held low till Comm Clear detected. Comm Clear needed for recovery. (FIFO 1 is read out, FIFO2 is still buffering, if reading happens, it is RXDATA\_UNEXP fault) Once FIFO is empty, device rejects any 0xFF until nCS going high. 0: No fault 1: Fault

RXFIFO\_OF While device is receiving command frame, more data is sent than device can accommodate in RX FIFO. Once this fault is detected, device doesn't store any new data into RX/TX FIFO. Device sends out 0xFF on MISO after current byte finished transmission(FIFO data mask happens at byte boundary). SPI\_RDY held low till Comm Clear detected. Comm Clear needed for recovery. Follow "Flow to send write cmd frame into bq79600" to avoid this fault. 0: No fault 1: Fault **<https://www.ti.com**>

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback*

## 7.5.36 Register: DEBUG\_SPI\_FRAME Address: 0x2302

# B7 B6 B5 B4 B3 B2 B1 B0

# RSVD

TR\_SOF TR\_WAIT RC\_IERR RC\_SOF RC\_BYTE\_ERR RC\_CRC

# R R R R R R R R

TR\_SOF Indicates that a SPI COMM CLEAR is received while there is data in output FIFO (SPI\_RDY is 0 or SPI\_RDY = 1 and receiving new data from VIF.) If SPI\_RDY = 1 and not receiving new data from VIF while receiving COMM CLEAR, it doesn't assert this bit. 0: No fault 1: Fault

TR\_WAIT Indicates that a SPI COMM CLEAR is received while there is no data in output FIFO regardless of SPI\_RDY. 0: No fault 1: Fault

RC\_IERR Detects initialization byte error in the received command frame. Example: • reserved command bits in the "INIT byte" is set, • expected to a cmd "INIT byte', but it is configured as response frame instead • extra data is sent other than one cmd frame during one nCS low All bytes that follow are discarded until a Comm Clear is received or a SOF due to a properly formed new command is received (nCS falling, etc). 0: No fault 1: Fault

RC\_SOF Detects a start-of-frame (SOF) error. Mostly, this is SPI COMM CLEAR is received on the SPI before the current frame is finished, e.g. partial cmd frame is sent 0: No fault 1: Fault

RC\_BYTE\_ERR Device receives data from the VIF that needs to go out on SPI, while host send data into device through SPI. (TXDATA\_UNEXP should also be set) CRC is not calculated and doesn't forward communication in daisy chain. All bytes that follow are ignored until a communication CLEAR is received. 0: No fault 1: Fault

RC\_CRC Detects CRC error in the received command frame from SPI. The frame will be considered as discarded frame. Frame CRC is calculated only if no physical level error, IERR, BERR, SOF error detected. 0: No fault 1: Fault

## 7.5.37 Register: DEBUG\_UART\_FRAME Address: 0x2303

# B7 B6 B5 B4 B3 B2 B1 B0

# RSVD

TR\_SOF TR\_WAIT RC\_IERR RC\_SOF RC\_BYTE\_ERR RC\_CRC

# R R R R R R R R

TR\_SOF Indicates that a UART COMM CLEAR is received while the device is still transmitting data to host. 0: No fault 1: Fault

TR\_WAIT The device is waiting for its turn to transfer a response out but the action is terminated because: 1. the device receives a UART COMM CLEAR signal, or 2. the device receives a new command This bit is valid when broadcast or stack read command has been issued. 0: No fault 1: Fault

RC\_IERR Detects initialization byte error in the received command frame. Example: • a STOP error is detected, • reserved command bits in the "INIT byte" is set, • expected a "INIT byte', but it is configured as response frame instead (e.g. 1st byte received after COMM CLEAR signal should but a "INIT byte") All bytes that follow are ignored until a communication CLEAR is received. 0: No fault 1: Fault

RC\_SOF Detects a start-of-frame (SOF) error. Mostly, this is UART COMM CLEAR is received on the UART before the current frame is finished. 0: No fault 1: Fault

RC\_BYTE\_ERR Other than INIT byte, if STOP error is detected in rest of byte in the frame or TX receives data while RX is using. CRC is not calculated and doesn't forward communication in daisy chain. All bytes that follow are ignored until a communication CLEAR is received. 0: No fault 1: Fault

RC\_CRC Detects CRC error in the received command frame from UART. The frame will be considered as discarded frame. Frame CRC is calculated only if no physical level error, IERR, BERR, SOF error detected 0: No fault 1: Fault

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2020 Texas Instruments Incorporated

## 7.5.38 Register: DEBUG\_COMH\_PHY Address: 0x2304

# B7 B6 B5 B4 B3 B2 B1 B0

# RSVD PERR BERR\_TAG SYNC2 SYNC1 BIT

# R R R R R R R R

PERR Pertain to received response frame from stack device only. PERR is a lump bit of all physical errors. Any error bit that is set in this register will also set the \[PERR\] bit. However, abnormality that isn't classified in the register can also trigger the \[PERR\] bit (e.g. detecting missing of data or wrong data order.) 0: no comm error detected 1: detected abnormality of the received comm frame. BERR is asserted to the forwarded communication.

BERR\_TAG Indicates BERR bit is set in at least one byte in received response frame from stack device 0: received response frame doesn't have BERR 1: received response frame has BERR

SYNC2 Timing information extracted from the demodulation of the preamble half-bit and the two full bits of synchronization is outside of the expected window, this bit is set and the byte is not processed. 0: No fault 1: Fault

SYNC1 If the demodulation of the preamble half-bit and the two full bits of synchronization data have errors and the timing is likely not correct, this bit is set and the byte is not processed. 0: No fault 1: Fault

BIT The device has detected a data bit, however, the detection samples is not enough to guarantee a strong '1' or '0'. 0: No fault 1: Fault

## 7.5.39 Register: DEBUG\_COMH\_FRAME Address: 0x2305

# B7 B6 B5 B4 B3 B2 B1 B0

# RSVD

RR\_IERR RR\_SOF RR\_BYTE\_ERR RR\_UNEXP RR\_CRC

# R R R R R R R R

RR\_IERR Detects initialization byte error in the received response frame. This may due to improper formatting of a byte such as a frame initialization byte is expected, but start-of-frame (SOF) bit is not set, or an invalid frame type is selected. All bytes from VIF that follows are ignored until a SOF bit is received (BQ79600 still forwards data from VIF to UART/SPI). 0: No fault 1: Fault

RR\_SOF Valid when \[DIR\_SEL\] = 0. Detects a start-of-frame (SOF) error on COMH. The SOF bit shall only be set in the initialization frame but the SOF bit is set in the current frame that is not expected. 0: No fault 1: Fault

RR\_BYTE\_ERR Valid when \[DIR\_SEL\] = 0. Detected any byte errors, other than the error in the initialization byte, in the received response frame. If the byte err is on the last byte of the CRC, it would check CRC in addition to discarding the frame. This error can be triggered by one or more error bit set in the DEBUG\_COMH\_PHY register. All bytes from VIF that follows are ignored until a SOF bit is received (BQ79600 still forwards data from VIF to UART/SPI). 0: No fault 1: Fault

RR\_UNEXP If \[DIR\_SEL\] = 1, but device received response frame from COMH which is an invalid condition and device will set this error bit. 0: No fault 1: Fault

RR\_CRC Indicates one or more COMH response frames being discarded due to CRC error. 0: No fault 1: Fault **<https://www.ti.com**>

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback*

## 7.5.40 Register: DEBUG\_COML\_PHY Address: 0x2306

# B7 B6 B5 B4 B3 B2 B1 B0

# RSVD PERR BERR\_TAG SYNC2 SYNC1 BIT

# R R R R R R R R

PERR Pertain to received response frame from stack device only. PERR is a lump bit of all physical errors. Any error bit that is set in this register will also set the \[PERR\] bit. However, abnormality that isn't classified in the register can also trigger the \[PERR\] bit (e.g. detecting missing of data or wrong data order.) 0: no comm error detected 1: detected abnormality of the received comm frame. BERR is asserted to the forwarded communication.

BERR\_TAG Indicates BERR bit is set in at least one byte in received response frame from stack device 0: received response frame doesn't have BERR 1: received response frame has BERR

SYNC2 Timing information extracted from the demodulation of the preamble half-bit and the two full bits of synchronization is outside of the expected window, this bit is set and the byte is not processed. 0: No fault 1: Fault

SYNC1 If the demodulation of the preamble half-bit and the two full bits of synchronization data have errors and the timing is likely not correct, this bit is set and the byte is not processed. 0: No fault 1: Fault

BIT The device has detected a data bit, however, the detection samples is not enough to guarantee a strong '1' or '0'. 0: No fault 1: Fault

## 7.5.41 Register: DEBUG\_COML\_FRAME Address: 0x2307

# B7 B6 B5 B4 B3 B2 B1 B0

# RSVD

RR\_IERR RR\_SOF RR\_BYTE\_ERR RR\_UNEXP RR\_CRC

# R R R R R R R R

RR\_IERR Detects initialization byte error in the received response frame. This may due to improper formatting of a byte such as a frame initialization byte is expected, but start-of-frame (SOF) bit is not set, or an invalid frame type is selected. All bytes from VIF that follows are ignored until a SOF bit is received (BQ79600 still forwards data from VIF to UART/SPI). 0: No fault 1: Fault

RR\_SOF Valid when \[DIR\_SEL\] = 1. Detects a start-of-frame (SOF) error on COML. The SOF bit shall only be set in the initialization frame but the SOF bit is set in the current frame that is not expected. 0: No fault 1: Fault

RR\_BYTE\_ERR Valid when \[DIR\_SEL\] = 1. Detected any byte errors, other than the error in the initialization byte, in the received response frame. If the byte err is on the last byte of the CRC, it would check CRC in addition to discarding the frame. This error can be triggered by one or more error bit set in the DEBUG\_COML\_PHY register. All bytes from VIF that follows are ignored until a SOF bit is received (BQ79600 still forwards data from VIF to UART/SPI). 0: No fault 1: Fault

RR\_UNEXP If \[DIR\_SEL\] = 0, but device received response frame from COML which is an invalid condition and device will set this error bit. 0: No fault 1: Fault

RR\_CRC Indicates one or more COML response frames being discarded due to CRC error. 0: No fault 1: Fault

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2020 Texas Instruments Incorporated

# 8 Application and Implementation

# Note

# Information in the following applications sections is not part of the TI component specification, and TI

does not warrant its accuracy or completeness. TI's customers are responsible for determining suitability of components for their purposes. Customers should validate and test their design implementation to confirm system functionality.

# 8.1 Application Information

# This section is concerned with the external operation, what external components are required to add to the

device to make it usable in a particular design, and how to calculate the values for those external components.

# 8.2 Typical Applications

# 8.2.1 Bridge With Reverse Wakeup in UART

# The following application circuit is used when user chooses to use UART interface and any of those features

reverse wakeup, ring architecture, fault/heartbeat tone.

# MCU GPIO2

# GPIO1

# VIO

# GND

# BQ79600-Q1

# VIO

# GND

# NFAULT

# SBC (PMIC) KEY ON

# 5.5V-40V 3.3V/5V Real Time Clock

# CAN\_WK AFE fault nCS

# nUART/SPI (SPI\_RDY)

# SCLK

# MOSI/RX

# MISO/TX

# GPIO3

# GPIO4

# GPIO5

# GPIO0 0.1uF

# 100K 12V Battery 0.22uF

# 10K 100K 10K

# DVDD

# GND

# CVDD

# COMHP

# COMHN

# COMLP

# COMLN

# BAT

# INH Low Voltage Domain How Voltage Domain

# GND 50V 0.1uF 0.22uF

## Twisted pair cabling 100pF 100pF

## 1K BQ battery monitor Cap/ Cap+choke/ XFMR Isolation

# 1K Cap/ Cap+choke/ XFMR Isolation

## BQ battery monitor 100pF 100pF 100pF 100pF

## Ratio:1 to 1

# PESD5V0L2BT

# PESD5V0L2BT

# Figure 8-1. Typical Bridge with Reverse Wakeup in UART Applications Circuit

# 8.2.1.1 Design Requirements

# Table 8-1 describes the design parameters.

# Table 8-1. Recommended Design Requirement

# PARAMETER **VALUE**

# UART speed 1Mbps

# 8.2.1.2 Detailed Design Procedure

# 8.2.1.2.1 MCU Interface (UART, NFAULT)

# To select UART interface, connect nCS, nUART/SPI and SCLK pins to GND. UART interface includes RX/TX

pins. They are pulled up through a 10-100kΩ resistor to VIO like figure above.

# NFAULT pin, if not used, connect to GND. Otherwise, pull it up wtih 100kΩ to VIO.

# 8.2.1.2.2 Daisy Chain Interface

# Given that galvanic isolation is expected between BQ79600-Q1 and stack BQ devices, transformer isolation is

recommended. Section 8.2.1 shows the interface components values.

# www.ti.com

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

# Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback* Contact TI for transformer recommendations. **8.2.1.2.3 INH Connection**

INH pin is connected to the power management IC (PMIC) enable pin such that when reverse wakeup is triggered, INH would be pulled towards BAT and enable PMIC. INH pin should always be lower than BAT pin. The 100kΩ connected to INH in Section 8.2.1 is to make sure INH pin potential is defined when INH driver is off. ***8.2.1.3 Application Performance Plot***

**Figure 8-2. Command and Response Frame for Read from 2 Stack Devices**

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2020 Texas Instruments Incorporated

# Figure 8-3. Zoomed View of Response Frame for 8 Registers Read from Stack Devices

# 8.2.2 Bridge Without Reverse Wakeup in SPI

# The following application circuit is used when user chooses to use SPI interface and none of those features

reverse wakeup, ring architecture, fault/heartbeat tone.

# MCU GPIO2

# GPIO1

# VIO

# GND

# BQ79600-Q1

# VIO

# GND

# NFAULT SBC (PMIC) KEY ON 3.3V/5V Real Time Clock

# CAN\_WK nCS

# nUART/SPI (SPI\_RDY)

# SCLK

# MOSI/RX

# MISO/TX

# GPIO3

# GPIO4

# GPIO5

# GPIO0 0.1uF 12V Battery 0.22uF

# 10K 100K 10K

# DVDD

# 100K 10K

# CVDD

# BAT

# INH Low Voltage Domain How Voltage Domain

# RED is optional 0.22uF

| Twisted pair | cabling |
|:--- |:--- |
| BQ battery | monitor |
| BQ battery | monitor |

## BQ battery monitor

## BQ battery monitor

# COMHP

# COMHN

# COMLP

# COMLN

# GND 100pF 100pF

# 1K

# 1K 100pF 100pF 100pF 100pF

## Ratio:1 to 1

# PESD5V0L2BT

# PESD5V0L2BT 10K

# 5V Cap/ Cap+choke/ XFMR Isolation Cap/ Cap+choke/ XFMR Isolation

# Figure 8-4. Typical Bridge without Reverse Wakeup in SPI Applications Circuit

# 8.2.2.1 Design Requirements

# Table 8-2 describes the design parameters.

# Table 8-2. Key Requirements

# PARAMETER **VALUE**

# SPI speed 2 - 6Mbps

# www.ti.com

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

# Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback* ***8.2.2.2 Detailed Design Procedure***

# 8.2.2.2.1 MCU Interface (SPI, SPI\_RDY, NFAULT)

To select SPI interface, connect MOSI, MISO, SCLK, nCS, nUART/SPI as figure above shows. Connect SPI\_RDY to MCU GPIO port for SPI flow control use, Section 7.3.2.1.2.2.1.

NFAULT pin, if not used, connect to GND. Otherwise, pull it up wtih 100KΩ to VIO. **8.2.2.2.2 Daisy Chain Interface** Refer to Section 8.2.1.2.2. ***8.2.2.3 Application Performance Plot***

See Application Performance Plot for application performanace curve.

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2020 Texas Instruments Incorporated

## 9 Power Supply Recommendations

## The BQ79600-Q1 can be powered by either directly from 12-V battery (nominal 9 - 16V) or regulated 5-V supply.

The design consideration for both options are described in the table below.

## Table 9-1. Supply Design Considerations

# 12-V BATTERY (nominal 9 - 16 V) **REGULATED 5-V SUPPLY**

VIO 3.125 - 5.25V, decouple 0.1-µF capacitor to gnd 3.125 - 5.25V, decouple 0.1-µF capacitor to gnd

BAT Put RC between supply battery and BAT pin, R = 10Ω, C = 0.1-µF capacitor. Make sure BAT pin sees no less than 5.5V and no larger than 40V.

4.75 - 5.25V, decouple 0.22-µF capacitor to gnd

CVDD Decouple 0.22-µF capacitor to gnd shorted to BAT

DVDD Decouple 0.22-µF capacitor to gnd Decouple 0.22-µF capacitor to gnd **<https://www.ti.com**>

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback*

## 10 Layout

The layout for this device must be designed carefully. Any design outside these guidelines can affect the communication robustness and EMI performance. Care must be taken in the layout of signals to and from the device to avoid coupling noise onto sensitive inputs. The layout of ground and power connections, as well as communication signals, should also be made carefully. **10.1 Layout Guidelines** **10.1.1 Ground Planes**

It is very important to establish a clean grounding scheme to ensure best performance of the device. There is one ground pin (GND) on the device. It is a good practice to use top and bottom PCB layers for signal routing, and use middle layers as ground planes. Even on a PCB layer that is mainly for signal routing, it is good practice to have a small island of ground pour if possible to provide a low-impedance ground, rather than simply a via through the ground trace to an lower ground plane. Create a keep-out area (no other traces and no ground plane) around the daisy chain components in all PCB layers.

There is a strong recommendation to have a minimum of 4 layers in the PCB, with one fully dedicated layer as an unbroken VSS plane (except thermal reliefs). Avoid placing tracks on this layer to maintain the unbroken integrity of the plane structure.

**10.1.2 Bypass Capacitors for Power Supplies**

The bypass capacitors of the following pins must be placed as close to the device pins as possible to ensure proper performance. - • BAT, VIO, CVDD, DVDD **10.1.3 UART/SPI communication**

The UART/SPI interface (MISO/TX, MOSI/RX, SCLK, nCS, nUART/SPI\_RDY) between MCU and BQ79600-Q1 shall be kept as short and straight as possible for optimized EMC performance. **10.1.4 Daisy Chain Communication**

It is important to have proper layout on the COMHP/N and COMLP/N circuits in order to have the best robust daisy chain communication. - • Keep differential traces as short as possible and as straight as possible. Minimize turns and avoid any looping on the traces. - • Keep the differential traces on the same layers. Run the trace in parallel with shielding and matching trace impedance. - • Place the isolation components close to the connectors. - • Create a keep-out area (no other traces and no ground plane) around the daisy chain components in all PCB layers. **10.2 Layout Example**

This section presents the BQ79600-Q1 Evaluation Module (EVM) design as a layout example. Given the EVM doesn't have an MCU, the example of UART/SPI connection layout is not optimized.

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2020 Texas Instruments Incorporated

## Figure 10-1. Top Layer Layout

## Figure 10-2. Signal 1 Layer Layout **<https://www.ti.com**>

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback*

## Figure 10-3. Signal 2 Layer Layout

## Figure 10-4. Bottom Layer Layout

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2020 Texas Instruments Incorporated

**11 Device and Documentation Support** **11.1 Device Support** **11.2 Third-Party Products Disclaimer**

# TI'S PUBLICATION OF INFORMATION REGARDING THIRD-PARTY PRODUCTS OR SERVICES DOES NOT

CONSTITUTE AN ENDORSEMENT REGARDING THE SUITABILITY OF SUCH PRODUCTS OR SERVICES OR A WARRANTY, REPRESENTATION OR ENDORSEMENT OF SUCH PRODUCTS OR SERVICES, EITHER ALONE OR IN COMBINATION WITH ANY TI PRODUCT OR SERVICE.

**11.3 Receiving Notification of Documentation Updates**

To receive notification of documentation updates, navigate to the device product folder on ti.com. Click on *Subscribe to updates* to register and receive a weekly digest of any product information that has changed. For change details, review the revision history included in any revised document. **11.4 Support Resources**

TI E2E ™ support forums are an engineer's go-to source for fast, verified answers and design help - straight from the experts. Search existing answers or ask your own question to get the quick design help you need.

Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do not necessarily reflect TI's views; see TI's Terms of Use.

**11.5 Trademarks** TI E2E ™ is a trademark of Texas Instruments. All other trademarks are the property of their respective owners. **11.6 Electrostatic Discharge Caution**

This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.

ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may be more susceptible to damage because very small parametric changes could cause the device not to meet its published specifications. **11.7 Glossary**

**TI Glossary** This glossary lists and explains terms, acronyms, and definitions. **<https://www.ti.com**>

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

Copyright © 2020 Texas Instruments Incorporated *Submit Document Feedback*

## 12 Mechanical, Packaging, and Orderable Information

The following pages include mechanical, packaging, and orderable information. This information is the most current data available for the designated devices. This data is subject to change without notice and revision of this document. For browser-based versions of this data sheet, refer to the left-hand navigation.

# BQ79600-Q1

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2020 Texas Instruments Incorporated

# PACKAGE OPTION ADDENDUM <https://www.ti.com> 9-Nov-2025

# PACKAGING INFORMATION **Orderable part number** **Status** (1) **Material type** (2)

**Package \| Pins** **Package qty \| Carrier** **RoHS** (3) **Lead finish/** **Ball material** (4) **MSL rating/** **Peak reflow** (5) **Op temp (°C)** **Part marking** (6)

BQ79600PWRQ1 Active Production TSSOP (PW) \| 16 2000 \| LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 BQ79600

BQ79600PWRQ1.A Active Production TSSOP (PW) \| 16 2000 \| LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 BQ79600 **(1)** ** Status: ** For more details on status, see our product life cycle.

**(2)** ** Material type: ** When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance, reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind.

**(3)** ** RoHS values: ** Yes, No, RoHS Exempt. See the TI RoHS Statement for additional information and value definition.

**(4)** ** Lead finish/Ball material: ** Parts may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two lines if the finish value exceeds the maximum column width.

**(5)** ** MSL rating/Peak reflow: ** The moisture sensitivity level ratings and peak solder (reflow) temperatures. In the event that a part has multiple moisture sensitivity ratings, only the lowest level per JEDEC standards is shown. Refer to the shipping label for the actual reflow temperature that will be used to mount the part to the printed circuit board.

**(6)** ** Part marking: ** There may be an additional marking, which relates to the logo, the lot trace code information, or the environmental category of the part. Multiple part markings will be inside parentheses. Only one part marking contained in parentheses and separated by a "~" will appear on a part. If a line is indented then it is a continuation of the previous line and the two combined represent the entire part marking for that device. **Important Information and Disclaimer:** The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release. In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis. Addendum-Page 1

# PACKAGE MATERIALS INFORMATION <https://www.ti.com> 24-Jul-2025

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

# BQ79600PWRQ1 TSSOP PW 330.0 12.4 6.9 5.6 1.6 8.0 12.0 Q1 Pack Materials-Page 1

# PACKAGE MATERIALS INFORMATION <https://www.ti.com> 24-Jul-2025

# TAPE AND REEL BOX DIMENSIONS ***Width (mm)***

# W

# L

# H \*All dimensions are nominal

**Device** **Package Type** **Package Drawing** **Pins** **SPQ** **Length (mm)** **Width (mm)** **Height (mm)**

# BQ79600PWRQ1 TSSOP PW 353.0 353.0 32.0 Pack Materials-Page 2 <https://www.ti.com>

# PACKAGE OUTLINE

# C

# 14X 0.65

# 2X 4.55

# 16X 0.30 0.17

# 6.6 6.2 TYP

# 1.2 MAX 0.15 0.05

# 0.25 GAGE PLANE 0 -8

# 4X (0 -12 )

# B 4.5 4.3 NOTE 4

# A

# 5.1 4.9 NOTE 3 0.75 0.50

# (0.15) TYP

# TSSOP - 1.2 mm max height **PW0016A**

# SMALL OUTLINE PACKAGE

# 4220204/B 12/2023

# 0.1 C A B

# PIN 1 INDEX AREA

# SEE DETAIL A

# 0.1 C

NOTES: 1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M. 2. This drawing is subject to change without notice.  3. This dimension does not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not exceed 0.15 mm per side. 4. This dimension does not include interlead flash. Interlead flash shall not exceed 0.25 mm per side. 5. Reference JEDEC registration MO-153.

# SEATING PLANE

# A 20 DETAIL A TYPICAL

# SCALE 2.500 <https://www.ti.com>

# EXAMPLE BOARD LAYOUT

# 0.05 MAX ALL AROUND

# 0.05 MIN ALL AROUND

# 16X (1.5)

# 16X (0.45)

# 14X (0.65) (5.8)

# (R0.05) TYP

# TSSOP - 1.2 mm max height **PW0016A**

# SMALL OUTLINE PACKAGE

# 4220204/B 12/2023

NOTES: (continued) 6. Publication IPC-7351 may have alternate designs.  7. Solder mask tolerances between and around signal pads can vary based on board fabrication site.

# LAND PATTERN EXAMPLE EXPOSED METAL SHOWN SCALE: 10X

# SYMM

# SYMM 15.000

# METAL SOLDER MASK OPENING

| METAL UNDER | SOLDER MASK |
|:--- |:--- |
| SOLDER MASK | OPENING |
| EXPOSED METAL | EXPOSED METAL |

# SOLDER MASK OPENING

# EXPOSED METAL EXPOSED METAL

# SOLDER MASK DETAILS

# NON-SOLDER MASK DEFINED (PREFERRED)

# SOLDER MASK DEFINED <https://www.ti.com>

# EXAMPLE STENCIL DESIGN

# 16X (1.5)

# 16X (0.45)

# 14X (0.65) (5.8)

# (R0.05) TYP

# TSSOP - 1.2 mm max height **PW0016A**

# SMALL OUTLINE PACKAGE

# 4220204/B 12/2023

NOTES: (continued) 8. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate design recommendations. 9. Board assembly site may have different recommendations for stencil design.

# SOLDER PASTE EXAMPLE BASED ON 0.125 mm THICK STENCIL SCALE: 10X

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

Copyright © 2025, Texas Instruments Incorporated

Last updated 10/2025