## BQ79616 16-Series Battery Monitor, Balancer, and Integrated Hardware Protector

## 1 Features

- • ±1.5-mV ADC accuracy - • Built-in redundancy path for voltage and  temperature diagnostics - • Highly accurate cell voltage measurements within  128 µs for all cell channels - • Integrated post-ADC configurable digital low-pass  filters - • Bus bar connection and measurement support - • Built-in host-controlled hardware reset to emulate  POR-like device reset - • Supports internal cell balancing - - Balancing current at 240 mA - - Built-in balancing thermal management with  automatic pause and resume control - • Isolated differential daisy chain communication  with optional ring architecture - • Embedded fault signal and heartbeat through  communication line - • UART/SPI host interface/communication bridge  device BQ79600 - • Built-in SPI controller

## 2 Applications

- • Battery Management System (BMS) in hybrid and  electric powertrain systems - • Energy storage battery packs with Battery  Management Systems

## 3 Description

The BQ79616 device provides high-accuracy cell voltage measurements in less than 200 μs for 16-series battery modules in high-voltage battery management systems in HEV/EV. The monitor offers different channel options in the same package type, providing pin-to-pin compatibility and supporting high reuse of the established software and hardware across any platform. The integrated front-end filters enable the system to implement with simple, low voltage rating, differential RC filters on the cell input channels. The integrated, post-ADC, low-pass filters enable filtered, DC-like, voltage measurements for better state of charge (SOC) calculation. This device supports autonomous internal cell balancing with temperature monitoring to auto-pause and resume balancing to avoid an overtemperature condition. **Device Information**

# PART NUMBER (1) **PACKAGE** **BODY SIZE (NOM)**

BQ79616 HTQFP (64-pin) 10.00 mm \times 10.00 mm

(1) For all available packages, see the orderable addendum at the end of the data sheet.

| Device | 16s | Cells |
|:--- |:--- |:--- |
| Device | 16s | Cells |
| Device | 16s | Cells | Device 16s Cells Device 16s Cells

# BAT+

# BAT Comms Device MCU Current/Temp **Simplified System Diagram**

# BQ79616 SLUSF21 - JUNE 2023

An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications, intellectual property matters and other important disclaimers. PRODUCTION DATA.

## Table of Contents

**1 Features**............................................................................ 1 **2 Applications**..................................................................... 1 **3 Description**....................................................................... 1 **4 Revision History**.............................................................. 2 **5 Description (continued)**.................................................. 3 **6 Pin Configuration and Functions**................................... 4 **7 Specifications**.................................................................. 7

7.1 Absolute Maximum Ratings....................................... 7 7.2 ESD Ratings.............................................................. 7 7.3 Recommended Operating Conditions........................ 7 7.4 Thermal Information................................................... 8 7.5 Electrical Characteristics............................................ 8 7.6 Timing Requirements............................................... 14 7.7 Typical Characteristics.............................................. 17 **8 Detailed Description**...................................................... 19

8.1 Overview................................................................... 19 8.2 Functional Block Diagram......................................... 20 8.3 Feature Description................................................... 21

8.4 Device Functional Modes........................................ 100 8.5 Register Maps......................................................... 109 **9 Application and Implementation**................................ 187

9.1 Application Information........................................... 187 9.2 Typical Applications................................................ 187 **10 Power Supply Recommendations**............................ 199 **11 Layout**......................................................................... 200

11.1 Layout Guidelines................................................. 200 11.2 Layout Example.................................................... 203 **12 Device and Documentation Support**........................ 207

12.1 Device Support..................................................... 207 12.2 Receiving Notification of Documentation Updates 207 12.3 Support Resources............................................... 207 12.4 Trademarks........................................................... 207 12.5 Electrostatic Discharge Caution............................ 207 12.6 Glossary................................................................ 207 **13 Mechanical, Packaging, and Orderable **

**Information**.................................................................. 208

## 4 Revision History

NOTE: Page numbers for previous revisions may differ from page numbers in the current version.

# DATE **REVISION** **NOTES** June 2023 \* Initial Release

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## 5 Description (continued)

The inclusion of the isolated, bidirectional, daisy chain ports supports both capacitor- and transformer-based isolation, allowing the use of the most effective components for centralized or distribution architectures commonly found in the Energy Storage System (ESS). This device also includes eight GPIOs or auxiliary inputs that can be used for external thermistor measurements.

Host communication to the BQ79616 device can be connected via the device's dedicated UART interface or through a communication bridge device, BQ79600. Additionally, an isolated, differential daisy-chain communication interface allows the host to communicate with the entire battery stack over a single interface. in the event of a communication line break, the daisy-chain communication interface is configurable to a ring architecture that allows the host to talk to devices at either end of the stack. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

# 6 Pin Configuration and Functions Device 64-HTQFP (PAP) 10 mm x 10 mm

# BAT

# CB16

# VC16

# CB15

# VC15

# CB14

# VC14

# CB13

# VC13

# CB12

# VC12

# CB11

# VC11

# CB10

# VC10

# CB9

# VC9

# CB8

# VC8

# CB7

# VC7

# CB6

# VC6

# CB5

# VC5

# CB4

# VC4

# CB3

# VC3

# CB2

# VC2

# CB1

# BBP

# BBN

# NFAULT

# GPIO1

# GPIO2

# GPIO3

# GPIO4

# GPIO5

# GPIO6

# GPIO7

# GPIO8

# TX

# RX

# TSREF

# DVSS

# DVDD

# BBP

# LDOIN

# CVSS

# CVDD

# NEG5V

# COMHP

# COMHN

# COMLN

# COMLP

# AVSS

# AVDD

# REFHP

# REFHM

# VC0

# CB0

# VC1

## Table 6-1. Pin Functions

# PIN

# TYPE **DESCRIPTION** **NAME**

# No. **BQ79616**

BAT P Power supply input and top of module measurement input. Connect to the top cell of the battery module.

NPN P Connect to the base of an external NPN transistor.

| LDOIN | P | 6-V preregulated analog power supply input/sense pin. Connect to the emitter of the external | NPN transistor and connect a 0.1-µF decoupling capacitor to CVSS. |
|:--- |:--- |:--- |:--- |
| AVDD | P | 5-V regulated output. AVDD supplies the internal analog circuits. Bypass AVDD with a | capacitor to AVSS. |
| AVSS | GND | Analog ground. Ground connection for internal analog circuits. Connect DVSS, CVSS, | REFHM, and AVSS externally. |
| NEG5V | P | Negative 5-V charge pump used for daisy chain and Main ADC. Connect with a capacitor to | CVSS. |
| DVDD | P | 1.8-V regulated output. DVDD supplies the internal digital circuits. Bypass DVDD with a | capacitor to DVSS. |
| DVSS | GND | Digital ground. Ground connection for internal digital logics. Connect DVSS, CVSS, REFHM, | and AVSS externally. |

AVDD P 5-V regulated output. AVDD supplies the internal analog circuits. Bypass AVDD with a capacitor to AVSS.

AVSS GND Analog ground. Ground connection for internal analog circuits. Connect DVSS, CVSS, REFHM, and AVSS externally.

NEG5V P Negative 5-V charge pump used for daisy chain and Main ADC. Connect with a capacitor to CVSS.

DVDD P 1.8-V regulated output. DVDD supplies the internal digital circuits. Bypass DVDD with a capacitor to DVSS.

DVSS GND Digital ground. Ground connection for internal digital logics. Connect DVSS, CVSS, REFHM, and AVSS externally.

CVDD P 5-V daisy chain communication and I/Os power supply. CVDD supplies the stack daisy chain communication transceiver circuit and the I/O pins. This power supply also supports an additional 10-mA external load in ACTIVE and SLEEP.

CVSS GND Daisy chain communication ground. Ground connection for internal daisy chain transceivers. Connect DVSS, CVSS, REFHM, and AVSS externally.

TSREF P 5-V bias voltage for NTC thermistor. Connect TSREF to the top of the NTC resistor divider network to the GPIOs when they are configured for NTC temperature monitoring. Bypass TSREF with a capacitor to CVSS.

REFHP P Precision reference output pin. Bypass with a capacitor to REFHM.

REFHM GND Precision reference ground. Ground connection for the internal precision reference. Connect DVSS, CVSS, REFHM, and AVSS externally.

VC16 I Cell voltage sense input. Connect to the positive terminal of cell 16. Connect a differential RC filter to VC15. Tie unused NC pins to BAT pin as explained in Cell Connections.

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## Table 6-1. Pin Functions (continued)

# PIN

# TYPE **DESCRIPTION** **NAME**

# No. **BQ79616**

| VC15 | I | Cell voltage sense input. Connect to the positive terminal of cell 15. Connect a differential | RC filter to VC14.Tie unused NC pins to BAT pin as explained in Cell Connections. |
|:--- |:--- |:--- |:--- |
| VC14 | I | Cell voltage sense input. Connect to the positive terminal of cell 14. Connect a differential | RC filter to VC13.Tie unused NC pins to BAT pin as explained in Cell Connections. |
| VC13 | I | Cell voltage sense input. Connect to the positive terminal of cell 13. Connect a differential | RC filter to VC12. Tie unused NC pins to BAT pin as explained in Cell Connections. |
| VC12 | I | Cell voltage sense input. Connect to the positive terminal of cell 12. Connect a differential | RC filter to VC11. |
| VC11 | I | Cell voltage sense input. Connect to the positive terminal of cell 11. Connect a differential | RC filter to VC10. |
| VC10 | I | Cell voltage sense input. Connect to the positive terminal of cell 10. Connect a differential | RC filter to VC9. |
| VC9 | I | Cell voltage sense input. Connect to the positive terminal of cell 9. Connect a differential RC | filter to VC8. |
| VC8 | I | Cell voltage sense input. Connect to the positive terminal of cell 8. Connect a differential RC | filter to VC7. |
| VC7 | I | Cell voltage sense input. Connect to the positive terminal of cell 7. Connect a differential RC | filter to VC6. |
| VC6 | I | Cell voltage sense input. Connect to the positive terminal of cell 6. Connect a differential RC | filter to VC5. |
| VC5 | I | Cell voltage sense input. Connect to the positive terminal of cell 5. Connect a differential RC | filter to VC4. |
| VC4 | I | Cell voltage sense input. Connect to the positive terminal of cell 4. Connect a differential RC | filter to VC3. |
| VC3 | I | Cell voltage sense input. Connect to the positive terminal of cell 3. Connect a differential RC | filter to VC2. |
| VC2 | I | Cell voltage sense input. Connect to the positive terminal of cell 2. Connect a differential RC | filter to VC1. |
| VC1 | I | Cell voltage sense input. Connect to the positive terminal of cell 1. Connect a differential RC | filter to VC0. |
| VC0 | I | Cell voltage sense input. Connect to the negative terminal of cell 1. Connect a differential | RC filter to AVSS. |

VC14 I Cell voltage sense input. Connect to the positive terminal of cell 14. Connect a differential RC filter to VC13.Tie unused NC pins to BAT pin as explained in Cell Connections.

VC13 I Cell voltage sense input. Connect to the positive terminal of cell 13. Connect a differential RC filter to VC12. Tie unused NC pins to BAT pin as explained in Cell Connections.

VC12 I Cell voltage sense input. Connect to the positive terminal of cell 12. Connect a differential RC filter to VC11.

VC11 I Cell voltage sense input. Connect to the positive terminal of cell 11. Connect a differential RC filter to VC10.

VC10 I Cell voltage sense input. Connect to the positive terminal of cell 10. Connect a differential RC filter to VC9.

VC9 I Cell voltage sense input. Connect to the positive terminal of cell 9. Connect a differential RC filter to VC8.

VC8 I Cell voltage sense input. Connect to the positive terminal of cell 8. Connect a differential RC filter to VC7.

VC7 I Cell voltage sense input. Connect to the positive terminal of cell 7. Connect a differential RC filter to VC6.

VC6 I Cell voltage sense input. Connect to the positive terminal of cell 6. Connect a differential RC filter to VC5.

VC5 I Cell voltage sense input. Connect to the positive terminal of cell 5. Connect a differential RC filter to VC4.

VC4 I Cell voltage sense input. Connect to the positive terminal of cell 4. Connect a differential RC filter to VC3.

VC3 I Cell voltage sense input. Connect to the positive terminal of cell 3. Connect a differential RC filter to VC2.

VC2 I Cell voltage sense input. Connect to the positive terminal of cell 2. Connect a differential RC filter to VC1.

VC1 I Cell voltage sense input. Connect to the positive terminal of cell 1. Connect a differential RC filter to VC0.

VC0 I Cell voltage sense input. Connect to the negative terminal of cell 1. Connect a differential RC filter to AVSS.

| CB16 | I/O | Cell balance connection. This pin is connected to the internal cell balancing FET. Connect | this pin to the positive terminal of cell 16 with a differential RC filter to CB15. The filter | resistor also sets the internal balance current. Tie unused CB16 pin via RC to BAT pin and | tie unused NC pins to BAT pin as explained in Cell Connections. |
|:--- |:--- |:--- |:--- |:--- |:--- |
| CB15 | I/O | Cell balance connection. This pin is connected to the internal cell balancing FET. Connect | this pin to the positive terminal of cell 15 with a differential RC filter to CB14. The filter | resistor also sets the internal balance current. Tie unused NC pins to BAT pin as explained | in Cell Connections. |
| CB14 | I/O | Cell balance connection. This pin is connected to the internal cell balancing FET. Connect | this pin to the positive terminal of cell 14 with a differential RC filter to CB13. The filter | resistor also sets the internal balance current. Tie unused NC pins to BAT pin as explained | in Cell Connections. |
| CB13 | I/O | Cell balance connection. This pin is connected to the internal cell balancing FET. Connect | this pin to the positive terminal of cell 13 with a differential RC filter to CB12. The filter | resistor also sets the internal balance current. Tie unused NC pins to BAT pin as explained | in Cell Connections. |

CB15 I/O Cell balance connection. This pin is connected to the internal cell balancing FET. Connect this pin to the positive terminal of cell 15 with a differential RC filter to CB14. The filter resistor also sets the internal balance current. Tie unused NC pins to BAT pin as explained in Cell Connections.

CB14 I/O Cell balance connection. This pin is connected to the internal cell balancing FET. Connect this pin to the positive terminal of cell 14 with a differential RC filter to CB13. The filter resistor also sets the internal balance current. Tie unused NC pins to BAT pin as explained in Cell Connections.

CB13 I/O Cell balance connection. This pin is connected to the internal cell balancing FET. Connect this pin to the positive terminal of cell 13 with a differential RC filter to CB12. The filter resistor also sets the internal balance current. Tie unused NC pins to BAT pin as explained in Cell Connections.

| CB12 | I/O | Cell balance connection. This pin is connected to the internal cell balancing FET. Connect | this pin to the positive terminal of cell 12 with a differential RC filter to CB11. The filter | resistor also sets the internal balance current. |
|:--- |:--- |:--- |:--- |:--- |
| CB11 | I/O | Cell balance connection. This pin is connected to the internal cell balancing FET. Connect | this pin to the positive terminal of cell 11 with a differential RC filter to CB10. The filter | resistor also sets the internal balance current. |
| CB10 | I/O | Cell balance connection. This pin is connected to the internal cell balancing FET. Connect | this pin to the positive terminal of cell 10 with a differential RC filter to CB9. The filter resistor | also sets the internal balance current. |
| CB9 | I/O | Cell balance connection. This pin is connected to the internal cell balancing FET. Connect | this pin to the positive terminal of cell 9 with a differential RC filter to CB8. The filter resistor | also sets the internal balance current. |

CB11 I/O Cell balance connection. This pin is connected to the internal cell balancing FET. Connect this pin to the positive terminal of cell 11 with a differential RC filter to CB10. The filter resistor also sets the internal balance current.

CB10 I/O Cell balance connection. This pin is connected to the internal cell balancing FET. Connect this pin to the positive terminal of cell 10 with a differential RC filter to CB9. The filter resistor also sets the internal balance current.

CB9 I/O Cell balance connection. This pin is connected to the internal cell balancing FET. Connect this pin to the positive terminal of cell 9 with a differential RC filter to CB8. The filter resistor also sets the internal balance current. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## Table 6-1. Pin Functions (continued)

# PIN

# TYPE **DESCRIPTION** **NAME**

# No. **BQ79616**

| CB8 | I/O | Cell balance connection. This pin is connected to the internal cell balancing FET. Connect | this pin to the positive terminal of cell 8 with a differential RC filter to CB7. The filter resistor | also sets the internal balance current. |
|:--- |:--- |:--- |:--- |:--- |
| CB7 | I/O | Cell balance connection. This pin is connected to the internal cell balancing FET. Connect | this pin to the positive terminal of cell 7 with a differential RC filter to CB6. The filter resistor | also sets the internal balance current. |
| CB6 | I/O | Cell balance connection. This pin is connected to the internal cell balancing FET. Connect | this pin to the positive terminal of cell 6 with a differential RC filter to CB5. The filter resistor | also sets the internal balance current. |
| CB5 | I/O | Cell balance connection. This pin is connected to the internal cell balancing FET. Connect | this pin to the positive terminal of cell 5 with a differential RC filter to CB4. The filter resistor | also sets the internal balance current. |
| CB4 | I/O | Cell balance connection. This pin is connected to the internal cell balancing FET. Connect | this pin to the positive terminal of cell 4 with a differential RC filter to CB3. The filter resistor | also sets the internal balance current. |
| CB3 | I/O | Cell balance connection. This pin is connected to the internal cell balancing FET. Connect | this pin to the positive terminal of cell 3 with a differential RC filter to CB2. The filter resistor | also sets the internal balance current. |
| CB2 | I/O | Cell balance connection. This pin is connected to the internal cell balancing FET. Connect | this pin to the positive terminal of cell 2 with a differential RC filter to CB1. The filter resistor | also sets the internal balance current. |
| CB1 | I/O | Cell balance connection. This pin is connected to the internal cell balancing FET. Connect | this pin to the positive terminal of cell 1 with a differential RC filter to CB0. The filter resistor | also sets the internal balance current. |
| CB0 | I/O | Cell balance connection. This pin is connected to the internal cell balancing FET. Connect to | the negative terminal of cell 1 with differential RC filter to AVSS. The filter resistor also sets | the internal balance current. |

CB7 I/O Cell balance connection. This pin is connected to the internal cell balancing FET. Connect this pin to the positive terminal of cell 7 with a differential RC filter to CB6. The filter resistor also sets the internal balance current.

CB6 I/O Cell balance connection. This pin is connected to the internal cell balancing FET. Connect this pin to the positive terminal of cell 6 with a differential RC filter to CB5. The filter resistor also sets the internal balance current.

CB5 I/O Cell balance connection. This pin is connected to the internal cell balancing FET. Connect this pin to the positive terminal of cell 5 with a differential RC filter to CB4. The filter resistor also sets the internal balance current.

CB4 I/O Cell balance connection. This pin is connected to the internal cell balancing FET. Connect this pin to the positive terminal of cell 4 with a differential RC filter to CB3. The filter resistor also sets the internal balance current.

CB3 I/O Cell balance connection. This pin is connected to the internal cell balancing FET. Connect this pin to the positive terminal of cell 3 with a differential RC filter to CB2. The filter resistor also sets the internal balance current.

CB2 I/O Cell balance connection. This pin is connected to the internal cell balancing FET. Connect this pin to the positive terminal of cell 2 with a differential RC filter to CB1. The filter resistor also sets the internal balance current.

CB1 I/O Cell balance connection. This pin is connected to the internal cell balancing FET. Connect this pin to the positive terminal of cell 1 with a differential RC filter to CB0. The filter resistor also sets the internal balance current.

CB0 I/O Cell balance connection. This pin is connected to the internal cell balancing FET. Connect to the negative terminal of cell 1 with differential RC filter to AVSS. The filter resistor also sets the internal balance current.

BBP I Bus bar connection. With BBP and BBN connecting to each end of a bus bar, this channel provides a differential input to the ADC measurement with a 5x gain.

BBN I Bus bar connection. With BBP and BBN connecting to each end of a bus bar, this channel provides a differential input to the ADC measurement with a 5x gain.

RX I UART receiver input. Pull up to CVDD with an external resistor and connect the device RX to the TX output of the host MCU. If unused (for example, for stack devices), connect RX to CVDD.

TX O UART transmitter output. Connect device TX to RX input of the host MCU and will be pulled up from the host side. If unused (for example, for stack devices), leave it floating.

COMHP I/O Vertical bidirectional communication interface for daisy chain connection. High side (north side) differential I/O. Will connect to the low side (south side) COMLP and COMLN of the lower adjacent device in the daisy chain configuration. If unused, connect COMHP and COMHN with a 1-kΩ resistor.

# COMHN I/O

COMLP I/O Vertical bidirectional communication interface for daisy chain connection. Low side (south side) differential I/O. Will connect to the high side (north side) COMHP and COMHN of the upper adjacent device in the daisy chain configuration. If unused, connect COMLP and COMLN with a 1-kΩ resistor.

# COMLN I/O

NFAULT O Fault indication output. Active low. If used on the base device, pull up NFAULT to CVDD with a pullup resistor and connect NFAULT to host MCU GPIO. If unused, leave it unconnected.

GPIO1 I/O General purpose input/output, configuration options are:

- • For external NTC thermistor connection, connect NTC thermistor to the pin and pull up

to TSREF. Used as input to ADC and OT and UT hardware comparators

- • For external DC voltage measurement, configured as input to ADC - • Generic digital input/output - • Use as I/O for SPI controller.

| GPIO2 | I/O |
|:--- |:--- |
| GPIO3 | I/O |
| GPIO4 | I/O |
| GPIO5 | I/O |
| GPIO6 | I/O |
| GPIO7 | I/O |
| GPIO8 | I/O |

# GPIO3 I/O

# GPIO4 I/O

# GPIO5 I/O

# GPIO6 I/O

# GPIO7 I/O

# GPIO8 I/O

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## 7 Specifications **7.1 Absolute Maximum Ratings **

over operating free-air temperature range (unless otherwise noted) (1)

# MIN **MAX** **UNIT** Input Voltage

BAT, VC\* (except VC0), CB\* (except CB0), NFAULT, BBP, BBN to AVSS (2) (3) -0.3 V

# CB0, VC0 to AVSS -0.3 5.5 V

| VCn to VCn-1, n = 1 to 16 (2) | -80 | V |
|:--- |:--- |:--- |
| CBn to CBn-1, n = 1 to 16 (3) | -0.3 | V |
| BBP to BBN | -80 | V |
| LDOIN to AVSS | -0.3 | V |
| NPNB to AVSS | -0.3 | V | $$ CBn to CBn-1, n = 1 to 16 (3) $$ -0.3 V

# BBP to BBN V

# LDOIN to AVSS -0.3 V

# NPNB to AVSS -0.3 V

# AVDD to AVSS -0.3 5.5 V

# DVDD to DVSS -0.3 1.98 V

# CVDD to CVSS -0.3 V

# TSREF to AVSS -0.3 5.5 V

# REFHP to REFHM -0.3 5.5 V

| NEG5V to AVSS | -5.5 | V |
|:--- |:--- |:--- |
| TX, RX to AVSS | -0.3 | V |
| COMHP, COMHN, COMLP, COMLN to CVSS | -20 | V |

# TX, RX to AVSS -0.3 V

# COMHP, COMHN, COMLP, COMLN to CVSS V

# COMHP to COMHN, COMLP to COMLN -5.5 5.5 V

# GPIO\* to AVSS -0.3 5.5 V

CB\* current Max of 8 cell in balancing at 75 o C ambient mA I/O current GPIO\*, RX, TX current mA

| TOTP\_PROG | Device will not start OTP programming above | this temperature | °C |
|:--- |:--- |:--- |:--- |
| TA | Ambient temperature | -40 | °C |
| TJ | Junction temperature | -40 | °C |
| Tstg | Storage temperature | -65 | °C | T A Ambient temperature °C T J Junction temperature °C T stg Storage temperature °C

(1) Stresses beyond those listed under *Absolute Maximum Ratings* may cause permanent damage to the device. These are stress ratings only, which do not imply functional operation of the device at these or any other conditions beyond those indicated under *Recommended Operating Condition*. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability. (2) VC pin voltage has to meet criteria of both VCn to AVSS as well as VCn to VCn-1. (3) CB pin voltage has to meet criteria of both CBn to AVSS as well as CBn to CBn-1.

## 7.2 ESD Ratings

# VALUE **UNIT**

# V (ESD)

| Electrostatic | discharge |
|:--- |:--- |
| Human body model (HBM) | ±2000 |
| V | Charged device model (CDM) |
| All Pins | ±500 |
| Other pins (1, 16, 17, 32, 33, 48, 49, 64) | ±750 | Human body model (HBM) \pm2000 V Charged device model (CDM) All Pins \pm500

Other pins (1, 16, 17, 32, 33, 48, 49, 64) \pm750

## 7.3 Recommended Operating Conditions

over operating free-air temperature range (unless otherwise noted)

# MIN **NOM** **MAX** **UNIT**

# V BAT\_RANG

E Total module voltage, full functionality, no OTP programming V

# V BAT\_OTP\_R

ANGE Total module voltage, full functionality, OTP programming allow V **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## 7.3 Recommended Operating Conditions (continued)

over operating free-air temperature range (unless otherwise noted)

# MIN **NOM** **MAX** **UNIT**

# V CELL\_RAN GE VCn - VCn-1, where n = 2 to 16 V

# VC1 - VC0 V

# VC0, CB0 to AVSS -0.3 V

# VC1, VC2, CB1, CB2 to AVSS -0.3 V VCn, CBn to AVSS, where n = 3 to 16 V

# V BB\_RANGE V BBP - V BBN mV V CB\_RANGE CBn - CBn-1, where n = 1 to 16 V

# V IO\_RANGE RX, TX, NFAULT CVDD V

# V GPIO\_RAN

# GE GPIO n input, where n = 1 to 8 0.2 4.8 V I IO GPIO n, RX, TX, where n = 1 to 8 mA T A Operation temperature °C

## 7.4 Thermal Information

# THERMAL METRIC

# BQ79616

# UNIT **PAP (HTQFP)**

# 64 PINS

| RθJA | Junction-to-ambient thermal resistance | 21.6 | °C/W |
|:--- |:--- | ---: |:--- |
| RθJC(top) | Junction-to-case (top) thermal resistance | 8.7 | °C/W |
| RθJB | Junction-to-board thermal resistance | 7.9 | °C/W |
| ψJT | Junction-to-top characterization parameter | 0.1 | °C/W |
| ψJB | Junction-to-board characterization parameter | 7.8 | °C/W |
| RθJC(bot) | Junction-to-case (bottom) thermal resistance | 2.1 | °C/W |

R\thetaJC(top) Junction-to-case (top) thermal resistance 8.7 °C/W

R\thetaJB Junction-to-board thermal resistance 7.9 °C/W

\psiJT Junction-to-top characterization parameter 0.1 °C/W

\psiJB Junction-to-board characterization parameter 7.8 °C/W

R\thetaJC(bot) Junction-to-case (bottom) thermal resistance 2.1 °C/W

## 7.5 Electrical Characteristics

over operating -40 ℃ to 125 ℃ free-air temperature range, VBAT = 9 V to 80 V (unless otherwise noted)

# PARAMETER

**TEST CONDITIONS** **MIN** **TYP** **MAX** **UNIT**

# THERMAL SHUTDOWN

# T SHUT Thermal shutdown (rising direction) °C

# T SHUT\_FALL Thermal shutdown (falling direction) °C

# T SHUT\_HYS

Thermal shutdown (rising - falling direction) °C

# T WARN\_RANGE

Thermal warning Threshold (rising direction) °C

# T WARN\_HYS

Thermal warning hysteresis (falling direction) °C T WARN\_ACC Thermal warning accuracy (±) °C

# SUPPLY CURRENTS

# I SHDN

Supply current in SHUTDOWN mode Sum of both I BAT and I LDOIN µA

# I SLP(IDLE)

Baseline supply current in SLEEP mode. No fault, no protector comparator, no cell balancing

| Sum of both IBAT and ILDOIN | TA = -20℃ to 65℃ | µA |
|:--- |:--- |:--- |
| Sum of both IBAT and ILDOIN | TA = -40℃ to 125℃ | µA |
| BQ79616 | SLUSF21 - JUNE 2023 | www.ti.com |

Sum of both I BAT and I LDOIN $$ TA = -40℃ to 125℃ $$ µA

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## 7.5 Electrical Characteristics (continued)

over operating -40 ℃ to 125 ℃ free-air temperature range, VBAT = 9 V to 80 V (unless otherwise noted)

# PARAMETER

**TEST CONDITIONS** **MIN** **TYP** **MAX** **UNIT**

I ACT(IDLE) Baseline supply current in ACTIVE mode

Sum of both I BAT and I LDOIN No fault, no communication, no protector comparator, no cell balancing 10.4 11.6 mA

# I CB\_EN

Additional supply current when cell balancing is on

At least 1 cell balancing FET is on, OT CB is enabled. Other functions are inactive 1.5 mA

# I PROTCOMP

Additional supply current when protector comparator is on

Either OV/UV/OT/UT protector is enabled. Other functions are inactive µA

| IADC | Additional supply current when | ADC is enabled |
|:--- |:--- |:--- |
| One ADC on, and conversion is | in progress. Other functions are | inactive. |
| 0.4 | 0.6 | mA |
| 2 ADCs on, and conversion is | in progress. Other functions are | inactive. |
| 0.6 | 0.9 | mA |

One ADC on, and conversion is in progress. Other functions are inactive. 0.4 0.6 mA

2 ADCs on, and conversion is in progress. Other functions are inactive. 0.6 0.9 mA

| IBAT | Supply current goes into BAT pin |
|:--- |:--- |
| ACTIVE mode | µA |
| SLEEP mode | µA |
| SHUTDOWN mode | µA | ACTIVE mode µA SLEEP mode µA SHUTDOWN mode µA

# I COMT

Additional supply current during daisy-chain broadcast read of 128-byte data

Use transformer isolation for daisy-chain interface. mA

# I COMC

Additional supply current during daisy-chain broadcast read of 128-byte data

Use capacitor or capacitor and choke isolation for daisy-chain interface. mA

# I OW\_SINK

Sink current for open wire test, applies to VC1 to VC16 and CB1 to CB 16 µA

I OW\_SOURCE Source current for open wire test, applies to VC0 and CB0 µA

I LEAK Leakage current on VC, CB pins VC, CB pins with ADC off. 0.1 µA **Supplies (LDOIN)** V LDOIN LDOIN voltage No OTP programming 5.9 6.1 V OTP programming 7.9 8.1 V **Supplies (CVDD)** V CVDD CVDD output voltage ACTIVE and SLEEP mode 4.9 5.1 V SHUTDOWN mode, no external Iload 3.95 V

SHUTDOWN mode, max external Iload = 5mA 3.4 5.5 V

V CVDD\_LDRG CVDD load regulation ACTIVE/SLEEP mode, max external Iload = 10mA mV

V CVDD\_OV CVDD OV threshold ACTIVE/SLEEP mode, max external Iload = 10mA 5.3 5.5 5.7 V

V CVDD\_OVHYS CVDD OV Hysteresis ACTIVE/SLEEP mode, max external Iload = 10 mA mV V CVDD\_UV CVDD UV threshold SHUTDOWN mode 3.5 V

ACTIVE/SLEEP mode, max external Iload = 10mA 4.3 4.45 4.65 V V CVDD\_UVHYS CVDD UV Hysteresis mV

V CVDD\_ILIMIT CVDD current limit ACTIVE, SLEEP mA **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## 7.5 Electrical Characteristics (continued)

over operating -40 ℃ to 125 ℃ free-air temperature range, VBAT = 9 V to 80 V (unless otherwise noted)

# PARAMETER

**TEST CONDITIONS** **MIN** **TYP** **MAX** **UNIT** **Supplies (AVDD)**

V AVDD AVDD output voltage C SUPPLIES = 1 µF, ACTIVE mode 4.85 5.21 V

V AVDD\_OV AVDD OV threshold C SUPPLIES = 1 µF, ACTIVE mode 5.25 5.5 5.7 V

V AVDD\_OVHYS AVDD OV Hysteresis C SUPPLIES = 1 µF, ACTIVE mode mV

V AVDD\_UV AVDD UV threshold C SUPPLIES = 1 µF, ACTIVE mode 4.25 4.45 4.6 V

V AVDD\_UVHYS AVDD UV Hysteresis C SUPPLIES = 1 µF, ACTIVE mode mV

V AVDD\_ILIMIT AVDD current limit C SUPPLIES = 1 µF mA **Supplies (DVDD)**

V DVDD DVDD output voltage C SUPPLIES = 1 µF, ACTIVE mode 1.65 1.8 1.95 V

V DVDD\_OV DVDD OV threshold C SUPPLIES = 1 µF, ACTIVE mode 1.95 2.1 2.3 V

V DVDD\_OVHYS DVDD OV Hysteresis C SUPPLIES = 1 µF, ACTIVE mode mV

V DVDD\_UV DVDD UV threshold C SUPPLIES = 1 µF, ACTIVE mode 1.623 1.65 1.71 V

V DVDD\_UVHYS DVDD UV Hysteresis C SUPPLIES = 1 µF, ACTIVE mode mV V DVDD\_ILIMIT DVDD current limit mA **Supplies (TSREF)**

V TSREF TSREF output voltage C SUPPLIES = 1 µF, ACTIVE mode 4.975 5.025 V

V TSREF\_LDRG TSREF load regulation I load = 4 mA, C SUPPLIES = 1 µF, ACTIVE mode mV

V TSREF\_OV TSREF OV threshold I load = 4 mA, C SUPPLIES = 1 µF, ACTIVE mode 5.2 5.6 5.8 V

V TSREF\_OVHYS TSREF OV Hysteresis I load = 4 mA, C SUPPLIES = 1 µF, ACTIVE mode mV

V TSREF\_UV TSREF UV threshold I load = 4 mA, C SUPPLIES = 1 µF, ACTIVE mode 4.0 4.2 4.4 V

V TSREF\_UVHYS TSREF UV Hysteresis I load = 4 mA, C SUPPLIES = 1 µF, ACTIVE mode mV

V TSREF\_ILIMIT TSREF current limit Device in ACTIVE Mode mA **Negative Charge Pump (NEG5V)**

V NEG5V NEG5V pin voltage CNEG5V = 0.1 µF -5.3 -4.6 -4.0 V

V NEG5V\_UV NEG5V UV threshold (rising) CNEG5V = 0.1 µF -4.1 -3.5 -3.0 V

# V NEG5V\_UVRECOV

NEG5V UV Recovery CNEG5V = 0.1 µF -4.3 -3.8 -3.3 V

# CELL BALANCE

R DSON Internal cell balance FET Rdson VCn > 2.8 V, where n = 1 to 16; -40oC<TA < 125oC 1.45 4.6 \Omega

# V CB\_DONE

VCB\_DONE detection threshold setting range (not accuracy) Step of 25 mV 2.45 V

# V MB\_DONE

VMB\_DONE detection threshold setting range (not accuracy) Step of 1 V V

# T OTCB

OTCB threshold setting range (not accuracy) Step of 2% %

# T COOLOFF

COOLOFF threshold setting range (not accuracy) Step of 2% % T CB\_WARN CB TWARN threshold o C T CB\_WARN\_HYS CB TWARN hysteresis o C **ADC Resolution**

# ENOB MAIN Main ADC Effective number of bits bits

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## 7.5 Electrical Characteristics (continued)

over operating -40 ℃ to 125 ℃ free-air temperature range, VBAT = 9 V to 80 V (unless otherwise noted)

# PARAMETER

**TEST CONDITIONS** **MIN** **TYP** **MAX** **UNIT**

# ENOB AUX AUX ADC Effective number of bits bits

# V LSB\_ADC

Main and AUX ADC Resolution for VCELL measurement 190.73 µV/LSB

# V LSB\_BB

Main and AUX ADC Resolution for (BBP-BBN) measurement 30.52 µV/LSB

| VLSB\_MAIN\_DIETEMP1 | DieTemp1 resolution (Main ADC) | ADC measurement is centered | with 0x000 = 0oC | 0.025 | °C/LSB |
|:--- |:--- |:--- |:--- | ---: |:--- |
| VLSB\_AUX\_DIETEMP2 | DieTemp2 resolution (AUX ADC) | ADC measurement is centered | with 0x000 = 0oC | 0.025 | °C/LSB |
| VLSB\_AUX\_BAT | BAT resolution (AUX ADC) | Applies to BAT voltage | measurement from AUX ADC | 3.05 | mV/LSB |

V LSB\_AUX\_DIETEMP2 DieTemp2 resolution (AUX ADC) ADC measurement is centered $$ with 0x000 = 0oC $$ 0.025 °C/LSB

V LSB\_AUX\_BAT BAT resolution (AUX ADC) Applies to BAT voltage measurement from AUX ADC 3.05 mV/LSB

V LSB\_GPIO GPIO resolution (Main and AUX ADC) 152.59 µV/LSB

V LSB\_TSREF TSREF resolution (Main ADC) 169.54 µV/LSB

# V LSB\_DIAG Diagnostic measurements resolution

REFL, VBG2, LPBG5, VCM, AVAO\_REF, AVDD\_REF, all the HW protector DAC

# 152.59 µV/LSB **ADC Accuracy**

I VC\_DELTA VCn to VCn-1 input current delta (when Main ADC is on) TA = -20oC to 65oC 1.8 µA $$ TA = -40oC to 105oC $$ µA

I VC VCn input current (when Main ADC is on) µA

R CB\_INPUT CB pin input impedance (when AUX ADC is on) MΩ

# V ACC\_MAIN\_CELL

Total channel accuracy for main ADC VCELL measurement, LPF\_VCELL\[2:0\] = 0x03 setting;

# 2 V\< VCELL\< 4.5 V; TA=25oC -2.2 1.5 mV

| 2 V \< VCELL \< 4.5 V; -20oC\<TA \< | 65oC | -3.0 | 2.4 | mV |
|:--- |:--- |:--- | ---: |:--- |
| 2 V\<VCELL\< 4.5 V; -40oC\<TA \< | 105oC | -3.5 | 2.6 | mV |
| 2 V\<VCELL\< 4.5 V; - | 40oC\<TA\<125oC | -3.5 | 2.6 | mV |

# 2 V\<VCELL\< 4.5 V; -40oC\<TA \< 105 o C -3.5 2.6 mV

# 2 V\<VCELL\< 4.5 V; 40oC<TA<125oC -3.5 2.6 mV

# 1 V\<VCELL\< 5 V; -40oC\<TA\<125oC -3.7 2.8 mV

# 2 V\<VCELL\< 5 V; 40oC<TA<125oC -4.5 3.2 mV

# V ACC\_AUX\_CELL

Total channel accuracy for AUX ADC measurement (excluding BAT and GPIO accuracy);

# 2 V\<VCELL\<4.5 V; TA=25oC -7.5 5.4 mV

| 2 V \< VCELL\<4.5 V; - | 20oC\<TA\<65oC | -8.0 | 6.3 | mV |
|:--- |:--- |:--- | ---: |:--- |
| 2 V\<VCELL\< 4.5 V; - | 40oC\<TA\<105oC | -9.0 | 6.3 | mV |
| 2 V\<VCELL\<4.5 V; - | 40oC\<TA\<125oC | -9.0 | 6.5 | mV |

# 2 V\<VCELL\< 4.5 V; 40oC<TA<105oC -9.0 6.3 mV

# 2 V\<VCELL\<4.5 V; 40oC<TA<125oC -9.0 6.5 mV

# 1 V\<VCELL\< 5 V; -40oC\<TA\<125oC -9.0 6.6 mV

# 0 V \< VCELL\< 5 V; -40oC \< TA<125oC -9.0 6.6 mV **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## 7.5 Electrical Characteristics (continued)

over operating -40 ℃ to 125 ℃ free-air temperature range, VBAT = 9 V to 80 V (unless otherwise noted)

# PARAMETER

**TEST CONDITIONS** **MIN** **TYP** **MAX** **UNIT**

# V (MAIN-AUX)

| Main - AUX measurement during | VCELL and OVDAC Reference | diagnostic. Same input voltage to | both ADC under same TA |
|:--- |:--- | ---: |:--- |
| 2 V \< VCELL\<4.5 V; TA= 25oC | -7.1 | 6.1 | mV |
| 2 V\<VCELL\<4.5 V; -20oC\<TA\<65oC | -7.8 | 6.6 | mV |

# 2 V \< VCELL\<4.5 V; TA= 25oC -7.1 6.1 mV

# 2 V\<VCELL\<4.5 V; -20oC\<TA\<65oC -7.8 6.6 mV

# 2 V\<VCELL\<4.5 V; 40oC<TA<105oC -7.8 6.6 mV

# 2 V\<VCELL\<4.5 V; 40oC<TA<125oC -7.8 6.7 mV

# 1 V\<VCELL\< 5 V; -40oC\<TA\<125oC -7.9 6.9 mV

# 0 V\<VCELL\< 5 V; -40oC\<TA\<125oC -7.9 6.9 mV

# V ACC\_MAIN\_GPIO\_RATIO

Measured GPIO from Main ADC/ measured TSREF from Main ADC

| 0.08 V\<VIN\<0.2 V, | 85oC\<TA\<125oC | -0.20 | 0.20 | % |
|:--- |:--- |:--- | ---: |:--- |
| 0.2 V\<VIN\<4.6 V, -40oC \< | TA\<105oC | -0.20 | 0.20 | % |
| 4.6 V \< VIN\<4.8 V, -40oC\<TA \< - | 20oC | -0.30 | 0.30 | % |

# 0.2 V\<VIN\<4.6 V, -40oC \< TA<105oC -0.20 0.20 %

# 4.6 V \< VIN\<4.8 V, -40oC\<TA \< 20 o C -0.30 0.30 %

# V ACC\_AUX\_GPIO\_RATIO

Measured GPIO from AUX ADC/ measured TSREF from AUX ADC

| 0.08 V\<VIN\<0.2 V, | 85oC\<TA\<125oC | -0.20 | 0.20 | % |
|:--- |:--- |:--- | ---: |:--- |
| 0.2 V\<VIN\<4.6 V, -40oC \< | TA\<105oC | -0.20 | 0.20 | % |
| 4.6 V\<VIN\<4.8 V, -40oC \< TA\< - | 20oC | -0.30 | 0.30 | % |

# 0.2 V\<VIN\<4.6 V, -40oC \< TA<105oC -0.20 0.20 %

# 4.6 V\<VIN\<4.8 V, -40oC \< TA\< 20 o C -0.30 0.30 %

V ACC\_MAIN\_GPIO\_ABS Total channel accuracy for GPIO measurement (Main ADC)

| 0.08 V \< VIN\<0.2 V, 85oC \< | TA\<125oC | -4.00 | 4.00 | mV |
|:--- |:--- |:--- | ---: |:--- |
| 0.2 V\<VIN\<4.6 V, -40oC \< | TA\<105oC | -5.00 | 3.00 | mV |
| 4.6 V \< VIN\<4.8 V, -40oC\<TA \< - | 20oC | -4.00 | 4.00 | mV |

# 0.2 V\<VIN\<4.6 V, -40oC \< TA<105oC -5.00 3.00 mV

# 4.6 V \< VIN\<4.8 V, -40oC\<TA \< 20 o C -4.00 4.00 mV

V ACC\_AUX\_GPIO\_ABS Accuracy from AUX ADC on GPIO

| 0.08 V \< VIN\<0.2 V, 85oC \< TA \< | 125°C | -6.00 | 6.00 | mV |
|:--- |:--- |:--- | ---: |:--- |
| 0.2 V \< VIN\<4.6 V, -40°C \< | TA\<105°C | -6.00 | 6.00 | mV |
| 4.6 V \< VIN\< 4.8 V, -40°C \<TA \< | -20°C | -6.00 | 6.00 | mV |

# 0.2 V \< VIN\<4.6 V, -40°C \< TA<105°C -6.00 6.00 mV

# 4.6 V \< VIN\< 4.8 V, -40°C \<TA \< -20°C -6.00 6.00 mV

V ACC\_MAIN\_BB Total channel accuracy for (BBPBBN) from Main ADC $$ LPF_BB[2:0] = 0x00 $$ -1.1 1.1 mV

# V ACC\_AUX\_BB

Total channel accuracy for (BBPBBN) from AUXADC mV

# V ACC\_AUX\_BAT AUX ADC measurement accuracy for BAT pin

Vbat pack range: 32 V to 72 V, T A $$ = -40oC to 125oC $$ mV

| VACC\_AUX\_REFL | AUX ADC measurement result | 1.092 | 1.1 | 1.106 | V |
|:--- |:--- | ---: | ---: | ---: |:--- |
| VACC\_AUX\_VBG2 | AUX ADC measurement result | 1.092 | 1.1 | 1.106 | V |
| VACC\_AUX\_VCM | AUX ADC measurement result | 2.400 | 2.5 | 2.550 | V |
| VACC\_AUX\_AVAO\_REF | AUX ADC measurement result | 2.400 | 2.47 | 2.550 | V |
| VACC\_AUX\_AVDD\_REF | AUX ADC measurement result | 2.400 | 2.47 | 2.550 | V |

V ACC\_AUX\_VBG2 AUX ADC measurement result 1.092 1.1 1.106 V

V ACC\_AUX\_VCM AUX ADC measurement result 2.400 2.5 2.550 V

V ACC\_AUX\_AVAO\_REF AUX ADC measurement result 2.400 2.47 2.550 V

V ACC\_AUX\_AVDD\_REF AUX ADC measurement result 2.400 2.47 2.550 V

V ACC\_AUX\_OVDAC AUX ADC measurement result Setting at 4.475 V; TA = -20°C to 65 o C 4.450 4.500 V

V ACC\_AUX\_OVDAC AUX ADC measurement result Setting at 4.475 V; TA = -40°C to 105°C 4.445 4.500 V

V ACC\_AUX\_OVDAC AUX ADC measurement result Setting at 4.475 V; TA = -40°C to 125 o C 4.445 4.500 V

V ACC\_AUX\_OVDAC AUX ADC measurement result Setting at 3.8 V 3.770 3.825 V

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## 7.5 Electrical Characteristics (continued)

over operating -40 ℃ to 125 ℃ free-air temperature range, VBAT = 9 V to 80 V (unless otherwise noted)

# PARAMETER

**TEST CONDITIONS** **MIN** **TYP** **MAX** **UNIT**

V ACC\_AUX\_OVDAC AUX ADC measurement result Setting at 3 V 2.970 3.030 V

V ACC\_AUX\_UVDAC AUX ADC measurement result Setting at 3.1 V 3.095 3.1 3.150 V

V ACC\_AUX\_VCBDONEDAC AUX ADC measurement result Setting at 4 V 3.950 4.050 V

V ACC\_AUX\_OTDAC AUX ADC measurement result Setting at 39% 1.900 1.95 2.000 V

V ACC\_AUX\_UTDAC AUX ADC measurement result Setting at 80% 3.950 4.050 V

V ACC\_MAIN\_TSREF Main ADC measurement result 4.975 5.025 V

# V ACC\_MAIN\_\_DIETEMP

Total channel accuracy for Die Temp1 measurement (±) ℃

# V ACC\_AUX\_DIETEMP

Total channel accuracy for Die Temp2 measurement (±) ℃ **Reference Voltages** V REFH REFHP to REFHM voltage 4.975 5.025 V

**HW Voltage Comparator/Protector (CELL OV/UV)**

# V OV\_COMP\_RANGE

OV comparator detection threshold setting range (not accuracy)

| Step of 25 mV | mV |
|:--- |:--- |
| Step of 25 mV | mV |
| Step of 25 mV | mV | Step of 25 mV mV Step of 25 mV mV

V OV\_COMP\_HYS OV comparator hysteresis after detection mV V OV\_COMP\_ACC OV comparator accuracy TA = -20oC to 65oC mV $$ TA = -40oC to 105oC $$ mV

# V UV\_COMP\_RANGE

UV comparator detection threshold  setting range (not accuracy) Step of 50 mV mV

V UV\_COMP\_HYS UV comparator hysteresis after detection mV V UV\_COMP\_ACC UV comparator accuracy TA = -20oC to 65oC mV $$ TA = -40oC to 105oC $$ mV

**HW Temperature Comparator/Protector (NTC OT/UT)**

# V OT\_COMP\_RANGE

OT comparator detection threshold setting range (not accuracy)

Step of 1%, ratiometric with respect to TSREF %

V OT\_COMP\_HYS OT comparator hysteresis after detection %

V OT\_COMP\_ACC OT comparator accuracy -0.5 0.5 %

# V UT\_COMP\_RANGE UT comparator detection threshold  range

Step of 2%, ratiometric with respect to TSREF %

# V UT\_COMP\_HYS UT comparator hysteresis after detection %

V UT\_COMP\_ACC UT comparator accuracy -0.5 0.5 %

**Digital I/Os (TX, RX, GPIO, SPI controller)**

# V OH

Output as logic level high (TX, GPIO as output)

GPIO is configured as output. I OUT $$ = 1 mA $$

# V CVDD 0.3 V

# V OL

Output as logic level low (TX, NFAULT, GPIO as output)

GPIO is configured as output. I OUT $$ = 1 mA $$ 0.3 V

# V IH

Input as logic level high (RX, GPIO as fault input)

GPIO is configured as input. I OUT $$ = 1 mA $$ 0.75 \times V CVDD V

# V IL

Input as logic level low (RX, GPIO as fault input)

GPIO is configured as input. I OUT $$ = 1 mA $$ 0.25 \times V CVDD V R WK\_PU GPIO weak pullup resistance KΩ **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## 7.5 Electrical Characteristics (continued)

over operating -40 ℃ to 125 ℃ free-air temperature range, VBAT = 9 V to 80 V (unless otherwise noted)

# PARAMETER

**TEST CONDITIONS** **MIN** **TYP** **MAX** **UNIT** R WK\_PD GPIO weak pulldown resistance KΩ

# COML and COMH

# R DCTX

Transmitter output impedance (COML and COMH) Ω

# R DCCM Common mode impedance (COML and COMH) kΩ

# V DCCM

Common mode voltage  (COML and COMH) 2.21 2.5 2.76 V

# V COMM\_DATA1

Receiver threshold range (V COMP - V COML ) form communication CODE:0 0.4 1.2 V

# V COMM\_TONE1

Receiver threshold range (V COMP - V COML ) form Tone CODE:0 0.4 1.2 V

## 7.6 Timing Requirements

over operating -40 ℃ to 125 ℃ free-air temperature range, VBAT = 9V to 80V (unless otherwise noted)

# PARAMETER

**TEST CONDITIONS** **MIN** **NOM** **MAX** **UNIT**

# POWER STATE TIMING

t SU(WAKE\_SHUT) Startup from SHUTDOWN to ACTIVE mode

Base device: From the end of WAKE ping to the start of a forwarding WAKE tone ms

Stack device: From the end of a received WAKE tone to the start of a forwarding WAKE tone ms

t SU(SLP2ACT) Startup from SLEEP to ACTIVE mode (with SLEEP2ACTIVE ping/tone)

Base device: From the end of  SLEEP2ACTIVE ping to the start of the forwarding SLEEP2ACTIVE tone µs

Stack device: From the end of  SLEEP2ACTIVE tone to the start of the forwarding SLEEP2ACTIVE tone µs

t SU(WAKE\_SLP) Startup from SLEEP to ACTIVE mode (with WAKE ping/tone)

Base device: From the end of WAKE ping to the start of a forwarding WAKE tone ms

Stack device: From the end of a received WAKE tone to the start of a forwarding WAKE tone ms

t SLP From ACTIVE to SLEEP mode From receiving SLEEP entry condition to enter in SLEEP mode µs t SHTDN From ACTIVE to SLHUTDOWN mode

From receiving SHUTDOWN entry condition to enter in SHUTDOWN mode (all LDOs in 10% of their nominal value) ms

t RST Reset time during ACTIVE mode CONTROL1\[SOFT\_RST\] = 1 is sent to a completion of the digital reset ms

# t HWRST

The time device will be in HW reset, after HW reset ping/tone issued ms

# SUPPLIES TIMING

t TSREF\_ON TSREF ramp up time (10%-90%) C TSREF = 1 µF ms

t TSREF\_OFF TSREF ramp down time (90%-10%) C TSREF = 1 µF ms

# PING SIGNAL TIMING

# t HLD\_WAKE

WAKE ping low time on RX pin; no external load on CVDD 2.5 ms

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## 7.6 Timing Requirements (continued)

over operating -40 ℃ to 125 ℃ free-air temperature range, VBAT = 9V to 80V (unless otherwise noted)

# PARAMETER

**TEST CONDITIONS** **MIN** **NOM** **MAX** **UNIT**

# t HLD\_SD

SHUTDOWN ping low time on RX pin; no external load on CVDD ms

# t UART(StA) SLEEPtoACTIVE ping low time on RX pin µs

t HLD\_HWRST HW\_RESET ping low time on RX pin ms

# COML and COMH (PULSE and TONE TIMING)

# t PW\_DC

COMM: Pulse width of data (half bit time) for communication ns

# t RECLK\_DC

COMM: data reclocking delay per device from COMH to COML or vice versa µs

# t COMTONE

Time between pulses of comm tones (HFO based). Comm Tones are WAKE, SLEEPtoACTIVE, SHUTDOWN, HWRST tones µs

t COMMTONE\_HI The HIGH time of each comms pulse (HFO base) 0.92 1.08 µs

t COMMTONE\_LO The LOW time of each comms pulse (HFO base) 0.92 1.08 µs

# t FLTTONE

Time between pulses of FAULT Tone (LFO based). Applies to FAULT Tone and HEARTBEAT 11.5 µs

| tFLTTONE\_HI | The HIGH time of each pulse of the | tone couplet | µs |
|:--- |:--- |:--- |:--- |
| tFLTTONE\_LO | The LOW time of each pulse of the | tone couplet | µs |
| nWAKEDET | Number of pulses to detect as a | WAKE tone | pulses |
| nWAKE | Number of pulses to transit for a | WAKE tone | pulses |
| nSHDNDET | Number of pulses to detect as a | SHUTDOWN tone | pulses |
| nSHDN | Number of pulses to transit for a | SHUTDOWN tone | pulses |

t FLTTONE\_LO The LOW time of each pulse of the tone couplet µs

n WAKEDET Number of pulses to detect as a WAKE tone pulses

n WAKE Number of pulses to transit for a WAKE tone pulses

n SHDNDET Number of pulses to detect as a SHUTDOWN tone pulses

n SHDN Number of pulses to transit for a SHUTDOWN tone pulses

# n SLPtoACTDET

Number of pulses to detect as a SLEEPtoACTIVE tone pulses n SLPtoACT

Number of pulses to transit for a SLEEPtoACTIVE tone pulses

# n HWRSTDET

Number of pulses to detect as a HW\_RESET tone pulses

# n HWRST

Number of pulses to transit for a HW\_RESET tone pulses

# n HBDET

HEARTBEAT: Number of pulses to detect as a valid tone pulses n HB

HEARTBEAT: Number of pulses to transit for a tone pulses

# t HB\_PERIOD

HEARTBEAT: Period between HEARTBEAT  burst (from the beginning of a HEARTBEAT to the beginning of the next HEARTBEAT) ms

# t HB\_TIMEOUT

HEARTBEAT: Timeout to considered as not receiving HEARTBEAT 0.9 1.1 s **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## 7.6 Timing Requirements (continued)

over operating -40 ℃ to 125 ℃ free-air temperature range, VBAT = 9V to 80V (unless otherwise noted)

# PARAMETER

**TEST CONDITIONS** **MIN** **NOM** **MAX** **UNIT**

# t HB\_FAST

HEARTBEAT: If HEARTBEAT is received within this time, it is considered receiving HEARTBEAT too fast ms

# n FTONEDET

FAULT TONE: Number of pulses  to detect as a valid tone pulses

# n FTONE

FAULT TONE: Number of pulses to transit for a tone pulses

# t FTONE\_PERIOD

FAULT TONE: Period between FAULT TONE Burst (from the beginning of a FAULT TONE to the beginning of the next FAULT TONE) ms

t FTS\_LATENCY Fault tone latency in stack device

From time a device receive the tone to the time the same device detects and generate its fault tone µs

t FTB\_LATENCY Fault tone latency in base device

From the time a device receive the tone to the time the same device detects and asserts NFAULT µs

# MAIN and AUX ADC TIMING

t SAR\_CONV Single conversion time (both Main and AUX ADCs) µs

t MAIN\_ADC\_CYCLE Single round robin cycle (Main ADC) µs

t AUX\_ADC\_CYCLE Single round robin cycle (AUX ADC) µs

# t AFE\_SETTLE

Analog front end (level shifters) settling time whenever device enter ACTIVE mode from SLEEP or SHUTDOWN ms

t ADC\_ACC This includes mux round robin, ADC conversions, and digital filters. -1.5 1.5 %

# BALANCING TIMING t BAL\_ACC Balancing timer accuracy %

# HW COMPARATORS/PROTECTORS TIMING t OV\_CYCLE OV round robin cycle ms t UV\_CYCLE UV round robin cycle ms

t OVUV\_BIST\_CYCLE OV and UV BIST cycle 21.8 24.2 ms t OT\_CYCLE OT round robin cycle ms t UT\_CYCLE UT round robin cycle ms

# t PWR\_BIST\_CYCLE

Time needed for the power supply BIST to complete after the power BIST go command 10.9 11.5 12.1 ms t OTUT\_BIST\_CYCLE OT and UT BIST cycle ms

# t HW\_COMP\_ACC OV,UV,OT,UT comparators timing accuracy %

# I/O TIMING (TX, RX, GPIO, NFAULT)

| tRISE | Rise Time | VCVDD  \> MIN VCVDD, CLOAD = 150 pF, | GPIO in output mode | ns |
|:--- |:--- |:--- |:--- |:--- |
| tFALL | Fall Time (exclude NFAULT) | VCVDD  \> MIN VCVDD, CLOAD = 150 pF, | GPIO in output mode | ns |
| tFALL\_NFAULT | Fall Time on NFAULT | VCVDD  \> MIN VCVDD, CLOAD = 150 pF, | RPULLUP = 10 kΩ | ns |

t FALL Fall Time (exclude NFAULT) V CVDD  \> MIN V CVDD, C LOAD = 150 pF, GPIO in output mode ns

# t FALL\_NFAULT

Fall Time on NFAULT V CVDD  \> MIN V CVDD, C LOAD = 150 pF, RPULLUP = 10 kΩ ns

# UART TIMING

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## 7.6 Timing Requirements (continued)

over operating -40 ℃ to 125 ℃ free-air temperature range, VBAT = 9V to 80V (unless otherwise noted)

# PARAMETER

**TEST CONDITIONS** **MIN** **NOM** **MAX** **UNIT** UART BAUD UART TX/RX Baud Rate Mbps

# UART ERR\_BAUD(RX)

| UART RX baud rate error - | requirement on the external host | -1 | % |
|:--- |:--- |:--- |:--- |
| UARTERR\_BAUD(TX) UART TX baud rate error | -1.5 | 1.5 | % |
| tUART(CLR) | UART Clear low time | bit | period |

UART ERR\_BAUD(TX) UART TX baud rate error -1.5 1.5 % t UART(CLR) UART Clear low time bit period

# t UART(RX\_HIGH)

After COMM CLEAR, wait this time before sending new frame bit period

# OTP NVM TIMING

# t CRC\_CUST

Time to complete a single cycle of CRC check on the customer OTP space µs

t CRC\_FACT Time to complete a single cycle of CRC check on the factory OTP space 1.6 ms

# SPI CONTROLLER TIMING f SCLK SCLK frequency kHz t HIGH, t LOW SCLK duty cycle %

t SS(HIGH) SS HIGH latency time. Time from register write high to SS pin high µs

t SS(LOW) SS LOW latency time. Time from register write low to SS pin low µs

t SU(MISO) MISO input data setup timerequirement for target device MISO stable before SCLK transition ns

t HD(MISO) MISO input data hold time MISO stable after SCLK transition ns

# OSCILLATOR

f HFO High frequency oscillator 31.52 32.48 MHz

f LFO Low frequency oscillator 248.9 275.1 kHz

## 7.7 Typical Characteristics Temperature ( q C)

# ISLP(IDLE) ( P A)

## Figure 7-1. ISLP (IDLE) vs Temperature Temperature ( q C)

# IACT(IDLE) (mA) 9.9 10.1 10.3 10.5 10.7 10.9 11.1

## Figure 7-2. IACT (IDLE) vs Temperature **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* Temperature ( q C)

# RDSON (: ) 1.7 1.9 2.1 2.3 2.5 2.7 2.9 3.1 3.3 3.5

## Figure 7-3. CBFET RDSON vs Temperature Frequency (Hz) Gain (dB)

# LPF 6.5Hz

LPF 13Hz LPF 26Hz LPF 53Hz LPF 111Hz LPF 240Hz

## Figure 7-4. Digital Low Pass Filter Frequency (Hz) Gain (dB) AAF 1.6kHz

## Figure 7-5. MAIN ADC Filter Frequency (Hz) Gain (dB) AAF 0.7kHz AAF 1.4kHz AAF 2.9kHz

## Figure 7-6. AUX ADC Filter

## BQ79616 SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## 8 Detailed Description **8.1 Overview**

The BQ79616 device is a stackable battery monitor that measures cell voltages and temperature. The device supports 6-series to 16-series connected (6S to 16S) battery cells. It allows up to three bus bar connections and measurements using cell sensing input channels or a dedicated bus bar channel maximizing the device flexibility to support various battery module sizes.

Multiple devices can be connected in a daisy chain. Each device has a pair of high (north) and low (south) vertical differential communication ports, requiring only one twisted pair cable. The device supports either capacitive only, capacitive and choke, or transformer isolation. Communication is reclocked on each daisychained device, ensuring communication integrity for long distances. An optional RING connection is supported to reverse the daisy chain communication direction in case of cable failure. Each device includes a SPI controller configured through the GPIOs.

The ADCs in the daisy-chained devices can be configured to align the start of cell voltage measurements and all cell voltages can be measured within 128 μs. Each cell sensing channel includes with a post-ADC digital low-pass filter (LPF) for noise reduction, as well as provides moving average measurement results. The device has eight GPIOs, all of which are configurable for NTC thermistor connections or use as general purpose I/O. All eight GPIOs can be measured within 1.6 ms.

The device supports passive balancing through an internal cell balancing MOSFET (CBFET) for each cell. The balancing function runs autonomously without microcontroller (MCU) interaction. The BQ79616 includes an option to pause and then resume balancing based on a programmable threshold detected by the external thermistor or if the die temperature is too high (greater than 105°C). Once balancing starts, the device tracks the balancing time on each cell. MCU can read out the remaining balancing time at any time.

The device includes a hardware OVUV comparator and an OTUT comparator with user configurable thresholds. These can be used as a second-level protector for cell over- and undervoltage and thermistor over- and undertemperature detections independent of ADC measurements.

The device provides an option to embed fault status information to the communication frame. When a device in the daisy chain detects a fault condition, this information is embedded and travels along the communication response frame to the bottom device which can be configured to trigger an NFAULT pin as an interrupt signal to the system. This provides a way to reduce communication overhead without adding an additional twisted pair cable and isolation for faster fault detection.

The device has SLEEP and SHUTDOWN modes for lower power consumption. All functions work in ACTIVE mode, and balancing and hardware comparators for OVUV and OTUT also work in SLEEP mode. While in SHUTDOWN, all active functions are turned off. A HW reset function is available and can be activated by the host MCU. The HW reset provides a POR-like event to the device without actual battery removal. This provides a reliable, low cost, and recoverable option to improve overall system robustness. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

# 8.2 Functional Block Diagram

# COMM/FAULT VIF Pre-reg AVDD DVDD

# AVAO

# TSREF

# I/O COM VIF North

# COM VIF SOUTH Digital

# OV, UV, VCBDONE

# Main ADC (SAR)

# GPIO8::

# GPIO1

# SAR ADC LPF LPF LPF Digital Registers OTP

# POR CB Control

# CB16

# CB15

# CB16

# CB1

#: CB1

# CB0:: Charge Pump

# TWARN Cell Balance

# VC16

# VC15

# VC14

# VC13

# VC12

# VC11

# VC10

# VC9

# VC8

# VC7

# VC6

# VC5

# VC4

# VC3

# VC2

# VC1

# VC0

# BBP

# BBN

# CB16

# CB15

# CB14

# CB13

# CB12

# CB11

# CB10

# CB9

# CB8

# CB7

# CB6

# CB5

# CB4

# CB3

# CB2

# CB1

# CB0

# NEG5V

# GPIO8

# GPIO7

# GPIO1

# GPIO2

# GPIO3

# GPIO4

# GPIO5

# GPIO6

# NFAULT

# RX

# TX

# COMHP

# COMHN

# COMLP

# COMLN

# BAT

# NPNB

# LDOIN

# AVDD

# AVSS

# DVDD

# DVSS

# CVDD

# CVSS

# TSREF

# REFHP

# REFHM

# GPIO MUX GPIO8::

# GPIO1

# CB16:

# CB0 Diag ch1 Diag ch 12

# SAR ADC:: Digtial

# AUX ADC (SAR) Filters (BCI & AAF), LS

# VC\[0:16\]:: BBP

# BBN Die Temp1 Voltage Comp MUX

# VC16::

# VC0 LS Digital Temp Comp MUX

# GPIO8::

# GPIO1 LS Digital

# OT, UT, OTCB Protectors Die Temp2 HW RESET Detection

# CVDD Tone/Ping Detection

# REF Osc

# MUX

# MUX

# MUX

# CB MUX

# BBP/BBN

## BQ79616 SLUSF21 - JUNE 2023 **<https://www.ti.com**>

## Submit Document Feedback

Copyright © 2023 Texas Instruments Incorporated **8.3 Feature Description** **8.3.1 Power Supplies**

The device generates directly from the battery stack all required supplies for its operation. The following subsections provide an overview of each internal supply block. See Section 9 for the recommended component connection. See Section 8.3.6.4 for diagnostic control and fault detection on the power supplies block.

# 8.3.1.1 AVAO\_REF and AVDD\_REF

The AVAO\_REF block (analog voltage always on) is powered from the BAT pin. It powers the always-on low-current circuits that are required for all power modes. This block also generates a preregulated reference, AVAO\_REF. The AVAO\_REF voltage passes through a load switch controlled by the SHUTDOWN mode. The reference voltage after the load switch is AVDD\_REF. Preregulation

# AVAO\_REF Shutdown Logic Switch AVDD\_REF Always-On (AVAO) Block

# BAT Reference Systems **Figure 8-1. AVAO Block**

# 8.3.1.2 LDOIN

The device is powered from the battery module in which the current draw for each cell is the same. From the top of the battery module, the device generates a 6-V regulated voltage (nominal) on the LDOIN pin through the internal linear regulator and an external NPN transistor. The NPNB pin controls the external NPN transistor of the regulator. The LDOIN output is the preregulated input to the rest of the internal low-dropout regulators (LDOs). During OTP (One-Time Programmable) memory programming, the LDOIN pin will be regulated to 8 V (nominal) to supply the programming voltage internally to the OTP programming. The LDOIN is turned off only during HW reset or a POR event.

# 8.3.1.3 AVDD

The AVDD LDO is the supply for the analog circuits. It takes the input voltage from LDOIN and generates a nominal 5 V. It will not be used to power any external circuit. This LDO is powered down in SHUTDOWN mode, during HW reset, or a POR event.

# 8.3.1.4 DVDD

The DVDD LDO is the supply for the digital circuits. It takes the input voltage from LDOIN and generates a nominal 1.8 V. It will not be used to power any external circuit. This LDO is powered down in SHUTDOWN mode, during HW reset, or a POR event.

# 8.3.1.5 CVDD and NEG5V

The CVDD LDO is the supply for the daisy chain interface (or vertical interface, VIF) and the I/O pins (RX, TX, NFAULT, and GPIOs). It takes the input voltage from LDOIN and generates a nominal 5V. Besides providing power for internal usage, this LDO can support an extra 10mA external load in ACTIVE and SLEEP mode, whereas extra 5mA external load in SHUTDOWN mode.

There is a -5V charge pump used for the daisy chain interface (or vertical interface, VIF) and Main ADC blocks. The NEG5V pin has a -4.6V output (nominal). It will be in a low-power burst mode when the device is in SLEEP or SHUTDOWN mode.

# 8.3.1.6 TSREF

The TSREF is a 5-V buffered reference that can bias the external thermistor circuits, allowing the ADCs to measure temperature and the OTUT protector to detect temperature faults. This reference is measurable by **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

the Main ADC. Both TSREF and GPIO measured by the Main ADC give a ratiometric measurement for best temperature measurement.

The TSREF is capable of supplying up to I TSREF\_ILMIT and will not be used to power any external circuit other than the thermistor bias. The TSREF is off by default and can be enabled or disabled through the *CONTROL2\[TSREF\_EN\]* bit. The startup time of TSREF is determined by the external capacitance. The MCU ensures TSREF is stable before making any GPIO measurement or OTUT protector detection. After enabling TSREF LDO, user shall wait 1.35ms before sending the next command. **8.3.2 Measurement System**

There are two SAR ADCs in the device, a 16-bit Main ADC and a 14-bit AUX ADC; both use a precision reference (REFH) for high-accuracy measurement. Each ADC has its own independent control and can be enabled or disabled separately. The Main ADC is the main measurement for cell voltages (VCELL) and temperature through thermistors connecting to the GPIOs. It also provides TSREF and die temperature measurements. The AUX ADC is mainly used during diagnostic procedures such as providing measurements on internal reference voltages or DAC output of the OVUV and OTUT comparators. It serves as a redundancy measurement for cell voltage inputs and thermistor temperature input through the GPIOs.

The subsections below provide an overview of the Main and AUX ADCs measurement paths. See Section 9 for the recommended external component connection. See Section 8.3.6.4 for the diagnostic control function and status of this block. ***8.3.2.1 Main ADC***

There are total of 24 inputs (slots) multiplexed to the Main ADC ( Figure 8-2 ). All inputs are measured in round robin fashion ( Figure 8-3 ). Each input takes 8 μs (nominal) to measure and a single round robin cycle completes in 192 μs (nominal). The inputs to the Main ADC are: - • Die temperature 1 - • TSREF - • Cell1 to Cell16 voltages through differential VC n-1 to VC n, where n = 1 to 16 - • Bus bar input through differential BBP-BBN pins - • Multiplexed GPIO1 through GPIO8 - • Spares (RSVD)

All measurements are reported in 16-bit hexadecimal in 2s complement. Results are reported to the corresponding *\*\_HI* (high-byte) and *\*\_LO* (low-byte) registers. First, convert the hexadecimal results to decimal values. Follow the equations in Table 8-1 to translate the result to μV or °C.

When the Main ADC is enabled, all Main ADC-related result registers shown in Table 8-1 are reset to the default value 0x8000. The measured result is populated to the result registers as the main ADC makes its conversion along the round robin cycle. When MCU reads the *\*\_HI* register, the device will pause the data refresh to the associated *\*\_LO* register until that *\*\_LO* register is read.

**Table 8-1. Main ADC Measurement Conversion Equations**

**Main ADC Inputs** **Result Registers** **Conversion Equations**

Die Temperature 1 *DIETEMP1\_HI/LO* Result in °C = V LSB\_MAIN\_DIETEMP1 \* Result in decimal 0x0000h is centered to 0°C.

| TSREF | TSREF\_HI/LO | Result in μV = VLSB\_TSREF \* Result in decimal |
|:--- |:--- |:--- |
| Cell1 to Cell16 | VCELL\*\_HI/LO, where \* = 1 to 16 | Result in μV = VLSB\_ADC \* Result in decimal |
| Bus Bar | BUSBAR\_HI/LO | Result in μV = VLSB\_BB \* Result in decimal |
| GPIO1 to GPIO8 | GPIO\*\_HI/LO, where \* = 1 to 8 | Result in μV = VLSB\_GPIO \* Result in decimal |
| BQ79616 | SLUSF21 - JUNE 2023 | www.ti.com |

Cell1 to Cell16 VCELL*_HI/LO, where * = 1 to 16 Result in μV = V LSB\_ADC \* Result in decimal

Bus Bar *BUSBAR\_HI/LO* Result in μV = V LSB\_BB \* Result in decimal

GPIO1 to GPIO8 GPIO*_HI/LO, where * = 1 to 8 Result in μV = V LSB\_GPIO \* Result in decimal

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated BCI filter BCI filter **BCI ** **filter** Level shifter Level shifter **Level ** **shifter** AAF AAF **AAF**

# MUX

# VC16

# VC0 **:**

# BBP **BBN** DieTemp1

# TSREF

# GPIO MUX GPIO8

# GPIO1 **:** **:** **:** **:**

# SAR **ADC**

# De-MUX Die Temp1 register GPIO1..8 registers Digital LPF **VCELL1...16 registers** **Busbar register** If LFP is disabled If LFP is disabled TSREF register Digital LPF **Digital ** **LPF**

## Figure 8-2. Main ADC Measurement Path **... **

# MAIN ADC Cell16 Cell1 Busbar

# GPIO8

# GPIO1 Busbar **... ** Cell16 Cell1 **Round robin 1** **Round robin 8** **... ** **... ** Typ 192 µs DieTemp1 DieTemp1 Spare Spare Spare Spare

# TSREF

# TSREF **... ** Spare **... ** Spare **... ** **Round robin N** *Typ 8 µs*

## Figure 8-3. Main ADC Round Robin Measurements

## 8.3.2.1.1 Cell Voltage Measurements

## 8.3.2.1.1.1 Analog Front End

## The cell voltage measurements of the Main ADC are taken from the VC0 through VC16 pins. The device allows

a minimum of 6 cells to a maximum of 16 cells to be measured. The VC0 through VC16 pins are connected to the analog front end which consists of a BCI filter, level shifter, and an anti-aliasing filter (AAF) on each VC input channel. The BCI filter has a cutoff frequency (f cutoff ) of 100 kHz and the AAF has f cutoff of 1.6 kHz. This filters out high-frequency noise on the VC input before going to the high-voltage multiplexer and measured by the Main ADC. The level shifter block is turned off to save power in SLEEP and SHUTDOWN modes.

## 8.3.2.1.1.2 VC Channel Measurements

## The VC pins are the input channels for cell voltage measurements from the Main ADC measured in the Cell1

to Cell16 slots of the round robin. The round robin timing is always the same even if fewer than 16 cells are connected to the device ( Figure 8-4 ). That is, for the inactive (or unused) VC channel, the device ignores the respective cell slot, but it does not remove the slot from the round robin cycle. This keeps a consistent measurement timing regardless of the cell number configuration. It also provides a consistent sampling time to the post-ADC digital LPF input.

## To determine the number of active VCELL channels for ADC measurement, the ACTIVE\_CELL\[NUM\_CELL3:0\]

parameter sets the highest active channel number. The device assumes any VC channel below the setting is also active. For example, when a 14S is connected to the device, the MCU sets the *\[NUM\_CELL3:0\]* to 14S, the Main ADC ignores channel 15 and channel 16 measurements and takes measurements on channels 1 through 14.

## The measurement results are reported in the corresponding VCELL\*\_HI (high-byte) and VCELL\*\_LO (low-byte)

registers, where \* = 1 to 16. If the digital LPFs are disabled, the result registers are reported with the single ADC

## www.ti.com

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

conversion values; otherwise, the result registers are reported with filtered measurement values. For an inactive VC channel, the respective *\_HI* and *\_LO* registers remain with the default value 0x8000.

**... ** Cell16 Cell1 **... ** Cell15 Cell14 **... ** DieTemp1 Spare Typ 192 µs

# MAIN ADC

# ACTIVE\_CELL\[NUM\_CELL3:0\] = 14S,,QGLFDWLQJ ³&HOO 15 ´ DQG³&HOO 16 ´ DUH * * **Inactive channels**

Inactive slots remain in the round robin, but device does not make the measurement

**Figure 8-4. Same Round Robin Timing for 6S Through 16S** ***8.3.2.1.1.3 Post-ADC Digital LPF***

Each differential VC channel measurement is equipped with a post-ADC LPF. The LPFs have much lower cutoff frequency (f cutoff ). There are 7 f cutoff options: 6.5 Hz, 13 Hz, 26 Hz, 53 Hz, 111 Hz, 240 Hz, and 600 Hz, configurable through the *ADC\_CONF1\[LPF\_VCELL2:0\]* setting. Once an f cutoff value is selected and the LPFs are enabled by setting *ADC\_CTRL1\[LPF\_VCELL\_EN\]* = 1, the same f cutoff setting applies to all VC channel measurements.

The digital LPF is implemented as single-pole filter which responds very similarly as an analog RC circuit. This means the Main ADC will be running in continuous mode for the digital LPFs to produce effective filtered results.

The MCU should take into account the digital filter settling time when there is a step change in the input DC voltage level. Equation below gives a typical estimate of digital filter settling time to hit settling accuracy threshold for a step in VC voltage.

Digital Filter Settling Time ~ \[ (\{log10 (Settling Accuracy Threshold \[mV\] / Voltage Step in Input Voltage \[mV\])\} / \{log10(1 - Filter Coefficient)\}) - 1\] x 0.192 ms **Fcutoff (Hz)** **6.5**

Filter Coefficient 0.5 0.25 0.125 0.0625 0.03125 0.015625 0.007813

For example: If VC step by 15mV, and user has to accommodate ~27ms settling time to within 1 LSB of input step for 26Hz LPF setting.

When the LPF starts, from disabled to enabled state, it jumps to its first input value and starts the filtering from that point. As compared to starting from 0 V or some mid-level voltage, this implementation allows a fast settling time for Main ADC and LFP is just starting. ***8.3.2.1.1.4 BBP and BBN Measurements***

The BBP and BBN pins are the inputs for bus bar measurement from the Main ADC. The intent of the BB channel is to enable the system to share a bus bar with a cell to a single VC channel, as the example shows in Figure 8-5. Hence, similar to the VC inputs, the BBP/N inputs also have the BCI, Level-Shifters, and AAF filters in the front end. The differential BB channel measurement also has an option to pass-through a post-ADC digital LPF. With the same f cutoff option as for the VC channel by using different configuration and enable control, *ADC\_CONF1\[LPF\_BB2:0\]* and *ADC\_CTRL1\[LPF\_BB\_EN\]*.

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

# CELL6 + BusBar

# VC6

# CB6

# BBP

# BBN

# VC5

# CB5 + +

**Figure 8-5. Simplified BBP and BBN Connections**

The BB channel measurement is reported in the *BUSBAR\_HI* (high-byte) and *BUSBAR\_LO* (low-byte) registers. If the digital LPF is disabled, the result registers are reported with the single ADC conversion value; otherwise, the result is reported in the filtered measurement value. In Figure 8-5, to obtain the actual Cell6 measurement, the MCU takes the difference of ( *VCELL6\_HI/LO* measurement - *BUSBAR\_HI/LO* measurement). If the BBP and BBN pins are not used (floating), the *BUSBAR\_HI/LO* register values are meaningless. The MCU will ignore these register values. **8.3.2.1.2 Temperature Measurements** ***8.3.2.1.2.1 DieTemp1 Measurement***

There are 2 die temperature sensors, DieTemp1 and DieTemp2. The DieTemp1 is routed to the Main ADC and it is also used for the Main ADC gain and offset correction internally. The measurement is reported in the *DIETEMP1\_HI* (high-byte) and *DIETEMP1\_LO* (low-byte) registers. The 0°C measurement is centered to hex value 0x0000h, so a positive value represents a positive temperature and a negative value represents a negative temperature. The measurement is also capped off to +200°C and -100°C.

***8.3.2.1.2.2 GPIOs and TSREF Measurements***

There are eight GPIOs. All GPIO inputs are available to be used for thermistor connections for temperature measurements and be used as a simple, single-ended, voltage input measurement.

# NTC

# TSREF

# GPIO1 Device filter (optional) 1 µF

# (OPTIONAL) filter (optional) **Figure 8-6. Thermistor Connection** **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

Figure 8-6 shows the thermistor circuit when GPIO is enabled for thermistor measurements. MCU ensures TSREF is enabled by setting *CONTROL2\[TSREF\_EN\]* = 1 and settled before taking the measurement value.

The GPIOs are multiplexed to one of the Main ADC MUX inputs. That is, in a single round robin cycle, only one GPIO is measured. To complete all eight GPIO measurements, it takes eight round robin cycles.

To enable the GPIO for ADC measurement, the corresponding *GPIO\_CONFn\[GPIO\*2:0\]* (where n = 1 to 4, \* = 1 to 8 for the corresponding GPIO) register is configured to ADC input or ADC and OTUT input. For example, to enable GPIO1 for ADC measurement only, set *GPIO\_CONF1\[GPIO12:0\]* to ADC input. See Section 8.3.5 for more details. If a GPIO is not configured for any ADC measurement, the device will ignore the corresponding GPIO slot but does not remove the slot from the round robin cycle. See Figure 8-7 for an example when GPIO2 is configured for non-ADC measurement.

**... ** DieTemp1 GPIO1 Spare **Round robin 1** **... ** DieTemp1 GPIO2 Spare **... ** DieTemp1 GPIO3 Spare **... ** **... ** DieTemp1 GPIO8 Spare **Round robin 2** **... ** **... ** **... ** **... ** **... ** DieTemp1 GPIO1 Spare **... ** **... ** **Round robin 3** **Round robin 8** **Round robin 9**

**... ** DieTemp1 GPIO2 Spare **Round robin 10** **... ** **... **

# MAIN ADC

GPIO2 is inactive.  ADC measurement is ignored in this slot

**Figure 8-7. GPIO2 Not Configured for ADC Measurement**

The measurements are reported in the corresponding *GPIO\*\_HI* (high-byte) and *GPIO\*\_LO* (low-byte) registers, where \* = 1 to 8. The measurement result is in μV. To achieve better temperature accuracy, the MCU can use a ratiometric measurement by using both TSREF and GPIO measurement with the following formula: (GPIO\_ADC/ TSREF_ADC) = RNTC/(RNTC + R1), where

- • GPIO\_ADC = ADC measurement on GPIO - • TSREF\_ADC = ADC measurement on TSREF - • RNTC = NTC thermistor resistance - *• ACTIVE\_CELL* register: Determine the inactive VC channel(s) and keep the result registers to default value  0x8000. - • R1 is the pull-up resistor as shown in Figure 8-6 with the assumption the R2 is not used

For an inactive GPIO channel, the respective *\_HI* and *\_LO* registers remain with the default value 0x8000. **8.3.2.1.3 Main ADC Operation Control** ***8.3.2.1.3.1 Operation Modes and Status***

To start the Main ADC, the host MCU sets *ADC\_CTRL1\[MAIN\_GO\]* = 1. When the device receives the GO command, it first samples the following settings to determine Main ADC configuration and then operates the

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

Main ADC accordingly. Any change of the settings below requires the MCU to resend another GO command to implement the new settings. - *• ADC\_CTRL1\[MAIN\_MODE1:0\]*: three run modes. See Table 8-2 for details. - *• ADC\_CTRL1\[LPF\_VCELL\_EN\]*: LPF for VC channels. Set to *ADC\_CONF1\[LFP\_VCELL2:0\]* f cutoff if enabled. - *• ADC\_CTRL1\[LPF\_BB\_EN\]*: LPF for BB channel. Set to *ADC\_CONF1\[LFP\_BB2:0\]* f cutoff if enabled. - *• ADC\_CONF2\[ADC\_DLY5:0\]*: Delay the start of the Main ADC. Use to align the ADC start time among the  daisy-chained devices. - *• ACTIVE\_CELL* register: Determine the inactive VC channel(s) and keep the result registers to default value  0x8000. - *• GPIO\_CONF1* to *GPIO\_CONF4*: Determine the inactive GPIO channel(s) and keep the result registers to  default value 0x8000. - • MAIN\_ADC\_CAL1, MAIN\_ADC\_CAL2, CS\_ADC\_CAL1, CS\_ADC\_CAL2, ADC\_CTRL1\[CS\_DR\] register **Note**

When using the MAIN ADC with the LPF Filter enabled and an ADC reset is desired, it is important that the LPF\_VCELL\_EN bit, LPF\_BB\_EN bit and MAIN\_GO bit is set to 0 and again set to 1 before running the MAIN ADC again, due to needed re-initialization of the internal LPF buffer. If this procedure is omitted then an LPF\_FAIL status bit can occur on the following MAIN ADC activation.

There are two status bits to indicate the Main ADC status: - *• DEV\_STAT\[MAIN\_RUN\]*: indicates if the Main ADC is running or not. - *• ADC\_STAT1\[DRDY\_MAIN\_ADC\]*: set when at least eight round robin cycles have completed indicating all  active GPIO channels and all other Main ADC inputs have at least one measurement completed. **Table 8-2. Summary of Main ADC Run Modes**

| \[MAIN\_MODE1:0\] | Run Mode | Description |
|:--- |:--- |:--- |
| 0b00 | Stop Main ADC | Stop the Main ADC |
| 0b01 | 8 RR Run (eight round | robin cycles) | 0b00 Stop Main ADC Stop the Main ADC 0b01 8 RR Run (eight round robin cycles)

Main ADC runs for eight round robin cycles then stops. This gives a single measurement on all cell voltages and all GPIO inputs to the system. Filtered measurements are not effective under run mode. For example, use as a quick burst read when MCU is periodically awake during system idle state. 0b10 Continuous Run

Main ADC runs in continuous mode and stops if *\[MAIN\_MODE1:0\]* = 0b00 and a GO is sent. For example, must use this mode if LPF is enabled. Also use in diagnostic operation.

The level shifter is enabled for the number of channels specified in the *ACTIVE\_CELL\[NUM\_CELL3:0\]* when device enters ACTIVE mode. MCU shall wait for t AFE\_SETTLE time before starting the Main ADC whenever the device enters ACTIVE mode or when *\[NUM\_CELL3:0\]* setting is changed.

The Main ADC operates in ACTIVE mode only. If the ADC is running while the device goes into SLEEP, the Main ADC will be "frozen" (that is, ADC is stopped but device still remembers the operational state). When the device returns to ACTIVE mode without any digital reset event, the Main ADC will restart and continues from its "pre-frozen" state. In this condition, the cell voltage measurements are off during the t AFE\_SETTLE time because input voltage to the ADC is not settled yet. MCU can ignore these measurements or send a new GO command to restart the Main ADC after t AFE\_SETTLE.

# 8.3.2.2 AUX ADC

There are a total of 24 inputs (slots) multiplexed to the AUX ADC ( Figure 8-8 ). All inputs are measured in round robin fashion ( Figure 8-9 ). Each input takes 8 μs (nominal) to measure and a single round robin cycle completes in 192 μs (nominal). The inputs to AUX ADC are: - • Die temperature 2 - • Multiplexed differential CB n-1 to CB n (AUXCELL1 to AUXCELL16), where n = 1 to 16 and differential bus bar  input through the BBP to BBN pins. - • MISC measurements: - - BAT pin **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## REFL, internal reference

- - VBG2, internal bandgap - - VCM, common voltage on Main ADC - - AVAO\_REF, always-on block reference - - AVDD\_REF - - OV DAC from OV protector - - UV DAC from UV protector - - VCBDONE DAC from UV protector - - OT or OTCB DAC from OT protector - - UT DAC from UT protector - • Multiplexed GPIO1 to GPIO8 - • Spares (RSVD)

## All measurements are reported in 16-bit hexadecimal in 2s complement. Results are reported to the

corresponding *\*\_HI* (high-byte) and *\*\_LO* (low-byte) registers. It first converts the hexadecimal results to decimal values. Follow the equations in Table 8-3 to translate the result to μV or °C.

## When the AUX ADC is enabled, all AUX ADC related result registers shown in Table 8-3 are reset to the default

value 0x8000. The measured result is populated to the result registers as the AUX ADC makes its conversion along the round robin cycle. When MCU reads the *\*\_HI* register, the device will pause the data refresh to the associated *\*\_LO* register until that *\*\_LO* register is read.

## Table 8-3. AUX ADC Measurement Conversion Equations

**AUX ADC inputs** **Result Registers** **Conversion Equations**

Die Temperature 2 *DIETEMP2\_HI/LO* Result in °C = V LSB\_AUX\_DIETEMP2 \* Result in decimal Note: 0x0000h is centered to 0°C.

Multiplexed AUXCELL1 to AUXCELL16 and BB channel

*AUX\_CELL\_HI/LO*, when CB MUX is locked to a single channel Result in μV = V LSB\_ADC \* Result in decimal

BAT *AUX\_BAT\_HI/LO* Result in μV = V LSB\_AUX\_BAT \* Result in decimal

# REFL *AUX\_REFL\_HI/LO*

Result in μV = V LSB\_AUX\_DIAG \* Result in decimal

# VBG2 *AUX\_VBG2\_HI/LO*

# VCM *AUX\_VCM\_HI/LO*

# AVAO\_REF *AUX\_AVAO\_REF\_HI/LO*

# AVDD\_REF *AUX\_AVDD\_REF\_HI/LO*

# OV DAC *AUX\_OV\_DAC\_HI/LO*

# UV\_DAC *AUX\_UV\_DAC\_HI/LO*

# VCBDONE DAC *AUX\_VCBDONE\_DAC\_HI/LO*

# OT or OTCD DAC *AUX\_OT\_OTCD\_DAC\_HI/LO*

# UT DAC *AUX\_UT\_DAC\_HI/LO*

Multiplexed GPIO1 to GPIO8 *AUX\_GPIO\_HI/LO* Result in μV = V LSB\_GPIO \* Result in decimal

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated BCI filter Level shifter AAF

# AUX ADC MUX

# CB16

# CB0:

# BBP BBN DieTemp2

| GPIO MUX | GPIO8 |
|:--- |:--- |
| GPIO1 |: |
| SAR | ADC |

# GPIO1:

# SAR ADC

# De-MUX AUX\_GPIO register AUX\_CELL register Die Temp2 register

# CB MUX

MISC1 to MISC12 inputs:: MISC1 to MISC12 registers AUX\_SETTLE options

## Figure 8-8. AUX ADC Measurement Path

CB MUX output DieTemp2 **... ** MISC 12 MISC 1

# AUX ADC Typ 192 µs

# GPIO1 **... ** Round robin 1 Round robin n **... **

# ADC\_CONF1\[AUX\_SETTLE1:0\] 3 Spare slots

CB MUX output DieTemp2 **... ** MISC 12 MISC 1 GPIOn 3 Spare slots

# AUXCB\_SETTLE

Configured through *\[AUX\_CELL\_SEL4:0\]* bits 0x00 = cycle through the active cells 0x01 = lock to Busbar (BBP-BBN) 0x02 = lock to AUXCELL 1 0x03 = lock to AUXCELL 2: 0x11 = lock to AUXCELL 16

The MISC channels are: MISC1 = BAT MISC2 = REFL MISC3 = VBG2 MISC4 = Spare MISC5 = VCM MISC6 = AVAO\_REF MISC7 = AVDD\_REF MISC8 = OV DAC (HW protector) MISC9 = UV DAC (HW protector) MISC10 = VCBDONE DAC (HW protector) MISC11 = OT or OTCB DAC (HW protector) MISC12 = UT DAC (HW protector) 6 Spare slots 6 Spare slots Round robin 8

CB MUX output DieTemp2 **... ** MISC 12 MISC 1 GPIO8 3 Spare slots 6 Spare slots **... ** **... ** **... ** **... ** Typ 8 µs

## Figure 8-9. AUX ADC Round Robin Measurements

## 8.3.2.2.1 AUX Cell Voltage Measurements

## 8.3.2.2.1.1 AUX Analog Front End

## The AUX ADC path serves as a redundancy path to the Main ADC measurement on cell voltage measurements

and bus bar measurements. It also has the front end filters of a BCI filter and an AAF filter in the AUX ADC path. The AUXCELL channel and differential BB channel (taken from BBP and BBN pins) in the AUX path are multiplexed (shown as the CB MUX in Figure 8-8 ) to share a single BCI filter and AAF filter. The CB MUX output after the front end filters is then going into one of the AUX ADC MUX and to the AUX ADC for measurement.

## Because the front end filters are shared, the device has to wait for the AAF filter to settle before making any

valid CB channel (AUXCELL) or BBP and BBN channel measurement. The default AAF f cutoff is 1.6 kHz as in

## www.ti.com

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

the Main ADC path, which translates to additional 4.3ms settling time to complete a single CB or BB channel measurement. The device provides 3 AAF settling time options, 4.3ms (default), 2.3ms, and 1.3ms, configured by the *ADC\_CONF1\[AUX\_SETTLE1:0\]* bits. The BCI filter f cutoff is 100 kHz as in the Main ADC path. **Note**

In order to achieve best measurement accuracy through the AUX ADC it is recommended to reset the ADC every time a new CB channel is locked through the AUX\_CELL\_SEL bits. This will ensure that the common mode error calibration routine is re-run and the measured result is compensated for common mode error.

***8.3.2.2.1.2 CB and BB Channel Measurements***

One slot, the CB MUX output slot, is assigned in the AUX ADC round robin cycle for the CB channels (differential CB n-1 - CB n, where n = 1 to 16) and BB (differential BBP - BBN) channel measurement because these channels are multiplexed to a single input to the AUX ADC multiplexer. For a single CB or BB channel measurement, it takes multiple round robin cycles because the device has to wait for the AAF settling time as well.

Because of the need to wait for the AAF to settle, the AUX ADC would only measure CB and BB channels that are active and are selected by the MCU; inactive or unselected channels are skipped.

| Active CB channels are determined by the ACTIVE\_CELL\[NUM\_CELL3:0\] setting. These bits set the | highest active channel number. For example, when a 14S is connected to the device, the MCU sets the | ACTIVE\_CELL\[NUM\_CELL3:0\] to 14S, the device assumes CB channels 1 through 14 are active; CB channels | 15 and 16 are inactive and will be skipped by the AUX ADC. |
|:--- |:--- |:--- |:--- |
| MCU can control which CB and BB channels to be measured through the AUX ADC. The | ADC\_CTRL2\[AUX\_CELL\_SEL4:0\] gives the options to run through all the active CB channel and BB channels | or to lock to a single CB channels or lock to the BB channel. Figure 8-10 shows the example of how the | AUXCELL slot is implemented with different \[AUX\_CELL\_SEL4:0\] setting. |
| It is recommended to run AUX ADC in continuous mode and all AUX ADC to measure through all the active | CB channel once. This enables the device to reduce the common mode error in AUX ADC measurement. MCU | shall perform this procedure before running ADC comparison related diagnostic or locking to a single CB or BB | channel measurement. |

MCU can control which CB and BB channels to be measured through the AUX ADC. The *ADC\_CTRL2\[AUX\_CELL\_SEL4:0\]* gives the options to run through all the active CB channel and BB channels or to lock to a single CB channels or lock to the BB channel. Figure 8-10 shows the example of how the AUXCELL slot is implemented with different *\[AUX\_CELL\_SEL4:0\]* setting.

It is recommended to run AUX ADC in continuous mode and all AUX ADC to measure through all the active CB channel once. This enables the device to reduce the common mode error in AUX ADC measurement. MCU shall perform this procedure before running ADC comparison related diagnostic or locking to a single CB or BB channel measurement.

There is no post-ADC LPF in the AUX ADC path. When the AUX ADC measurements are used during diagnostics, the AUX CELL (CB channel) measurements are compared against the Main ADC prefiltered measurements. While the device performs VCELL (from Main ADC) to AUX CELL (from AUX ADC) measurement comparison internally, the AUX BB comparison is performed by the host instead. See Section 8.3.6.4 for more details.

The device makes the CB or BB channel measurement available to read only when the *\[AUX\_CELL\_SEL4:0\] * bits are set to lock on a single CB (must be active) or BB channel. The measurement is reported in the *AUX\_CELL\_HI* (high-byte) and *AUX\_CELL\_LO* (low-byte) registers. The result registers will be updated after the AAF settling time is passed. For any other conditions, including lock to an inactive CB channel, the result registers remain with the default value 0x8000.

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

# AUXCELL1......

# AUXCELL1.........

# AUXCELL1......

| Round | robin 1 |
|:--- |:--- |
| Round | robin 2 |
| Round | robin n | Round robin 2 Round robin n AUXCELL1...... **Round ** **robin n+1**

# AUX ADC AAF settling *ADC\_CONF1\[AUX\_SELLTE1:0\]* AUXCELL2...... Round robin n+2... AUXCELL2...... Round robin m AUXCELL2...... **Round ** **robin m+1**

# AUX ADC AAF settling *ADC\_CONF1\[AUX\_SELLTE1:0\]*...

**Looping through all the active AUXCELL** **(CB channels) until AUX ADC stop/restart ** **with a different selection**

CB MUX stays at the selected channel for the AUX ADC AAF settling time, but the measurement during this time is discarded

AUX ADC makes the measurement after AAF is settled CB MUX switches to next active channel

# AUXCELL5......

# AUXCELL5.........

# AUXCELL5......

| Round | robin 1 |
|:--- |:--- |
| Round | robin 2 |
| Round | robin n | Round robin 2 Round robin n AUXCELL5...... **Round ** **robin n+1**

# AUX ADC AAF settling *ADC\_CONF1\[AUX\_SELLTE1:0\]* AUXCELL5...... **Round ** **robin n+2** AUXCELL5...... **Round ** **robin n+3**...

**Lock at the selected active channel until ** **AUX ADC stop/restart with a different ** **selection**

(a) \[AUX\_CELL\_SEL4:0\] = loop through all active CB channels (b) [AUX_CELL_SEL4:0] = Lock to CB channel 5 (AUXCELL5) Start valid AUX ADC measurement

## Figure 8-10. CB MUX Output Slot with Different \[AUX\_CELL\_SEL4:0\] Setting

## 8.3.2.2.2 AUX Temperature Measurements

## 8.3.2.2.2.1 DieTemp2 Measurement

## There are 2 die temperature sensors, DieTemp1 and DieTemp2. The DieTemp2 is routed to the AUX ADC

and is also used for the AUX ADC gain and offset correction internally. The measurement is reported in the *DIETEMP2\_HI* (high-byte) and *DIETEMP2\_LO* (low-byte) registers. The 0°C measurement is centered to hex value 0x00, so a positive value represents positive temperature and a negative value represents negative temperature. The measurement is also capped off to +200°C and -100°C.

## 8.3.2.2.2.2 AUX GPIO Measurements

## The AUX GPIO path is the same as the main GPIO path. All eight GPIOs are multiplexed to a single AUX

ADC MUX input. There is only one GPIO slot in the AUX ADC round robin cycle. That is, in a single AUX ADC round robin cycle, only one GPIO will be measured. To complete all eight GPIO measurements, it takes eight round robin cycles. If GPIO is connected to the thermistor network, the MCU enables TSREF by setting *CONTROL2\[TSREF\_EN\]* = 1 and ensures TSREF is stable before starting the AUX ADC measurement.

## When AUX ADC is enabled, the GPIO slot in the 1st round robin cycle is GPIO1, 2nd round robin cycle is

GPIO3, and so on. For the AUX ADC to make a measurement on a GPIO, the GPIO must be configured as ADC input or ADC and OTUT input in the corresponding *GPIO\_CONFn\[GPIO\*2:0\]* bits, where n = 1 to 4, \* = 1 to 8 for the respective GPIO channel. See Section 8.3.5 for more details. If the GPIO is inactive for the ADC measurement, the device ignores the corresponding GPIO slot but does not remove the slot from the AUX ADC round robin cycle.

## By default, the AUX ADC loops through all GPIO channels and the measurements do not report out to

the result registers. However, if MCU locks to a single GPIO channel, the locked GPIO measurement is reported to the *AUX\_GPIO\*\_HI* (high-byte) and *AUX\_GPIO\*\_LO* (low-byte) registers. This channel lock can **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

be set by the *ADC\_CTRL3\[AUX\_GPIO\_SEL3:0\]* bits. The result registers will report a GPIO measurement if *\[AUX\_GPIO\_SEL3:0\]* is locked to single GPIO channel, any other condition will show default value 0x8000.

| GPIO1 |... |... | Round robin 1 |
|:--- |:--- |:--- |:--- |
| GPIO2 |... |... | Round robin 2 |
| GPIO8 |... |... | Round robin 8 | GPIO2...... Round robin 2 GPIO8...... Round robin 8... GPIO1...... Round robin 9... Looping through all the GPIO channels

| GPIO3 |... |... | Round robin 1 |
|:--- |:--- |:--- |:--- |
| GPIO3 |... |... | Round robin 2 |
| GPIO3 |... |... | Round robin 8 | GPIO3...... Round robin 2 GPIO3...... Round robin 8... GPIO3...... Round robin 9... Lock at the selected GPIO channel

**(a) \[AUX\_GPIO\_SEL3:0\] = loop through all GPIO channels** (b) [AUX_GPIO_SEL3:0] = Lock to GPIO3

**Figure 8-11. GPIO Slot with Different ** ***\[AUX\_GPIO\_SEL3:0\]*** ** Setting** **8.3.2.2.3 MISC Measurements**

There are 12 MISC measurements listed at the beginning of the AUX ADC section. When the AUX ADC is enabled, these inputs are measured in every round robin cycle. Table 8-3 shows the corresponding result registers.

The DAC inputs of the OVUV and OTUT protectors reflect the real-time DAC values of the device which shows the OVUV and OTUT detection or recovery threshold currently in use in the protectors. It is normal to observe a change of the DAC measurements if there are unused channels or if any cell or GPIO channels detect a fault. See Section 8.3.4 for description of the protector architecture and see Section 8.3.6.4 for the protector DAC measurement configuration. **8.3.2.2.4 AUX ADC Operation Control**

To start the AUX ADC, the host MCU sets *ADC\_CTRL3\[AUX\_GO\]* = 1. When the device receives the GO command, it first samples the following settings to determine the AUX ADC configuration, then operates the AUX ADC accordingly. Any change to the settings below requires the MCU to send another GO command to implement the new settings. - *• ADC\_CTRL3\[AUX\_MODE1:0\]*: Four run modes. See Table 8-4 for details. - *• ADC\_CTRL2\[AUX\_CELL\_SEL4:0\]*: Selects which CB channels are measured by AUX ADC. - *• ADC\_CONF1\[AUX\_SETTLE1:0\]*: Configures the AUX ADC AAF settling time. - *• ADC\_CTRL3\[AUX\_GPIO\_SEL3:0\]*: Selects which GPIO channels are measured by AUX ADC. - *• ACTIVE\_CELL* register: Determines the inactive CB channel(s). - *• GPIO\_CONF1* to *GPIO\_CONF4*: Determines the inactive GPIO channel(s).

There are four status bits to indicate the AUX ADC status: - *• DEV\_STAT\[AUX\_RUN\]*: indicates if the AUX ADC is running or not. - *• ADC\_STAT1\[DRDY\_AUX\_MISC\]*: set when all MISC inputs are measured at least once. - *• ADC\_STAT1\[DRDY\_AUX\_CELL\]*: set when the CB or BB channels selected by *\[AUX\_CELL\_SEL4:0\]* are  measured at least once. - *• ADC\_STAT1\[DRDY\_AUX\_GPIO\]*: set when all GPIO channels (active or inactive) have been measured once.  Inactive channel measurements will be ignored by the device.

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## Table 8-4. Summary of AUX ADC Run Modes

| \[AUX\_MODE1:0\] | Run Mode | Description |
|:--- |:--- |:--- |
| 0b00 | Stop AUX ADC | Stop the AUX ADC |
| 0b01 | Single Run (1 round robin | cycle) |
| AUX ADC runs for one round robin cycle then stops. This gives a single | measurement on all MISC inputs. For example, use as a quick burst read for just | the MISC inputs without the need to issue a stop command to the AUX ADC. | 0b00 Stop AUX ADC Stop the AUX ADC 0b01 Single Run (1 round robin cycle)

AUX ADC runs for one round robin cycle then stops. This gives a single measurement on all MISC inputs. For example, use as a quick burst read for just the MISC inputs without the need to issue a stop command to the AUX ADC. 0b10 Continuous Run

AUX ADC runs in continuous mode and stops if *\[AUX\_MODE1:0\]* = 0b00 and a GO command is sent. For example, must use this mode when ADC diagnostic comparison operation is used. See Section 8.3.6.4 for details. 0b11 8 RR Run (eight round robin cycles)

AUX ADC runs for eight round robin cycles then stops. This gives a single measurement on all active GPIO inputs.

## The AUX ADC operates in ACTIVE mode only. If the ADC is running while the device goes into SLEEP mode,

the AUX ADC will be "frozen"; that is, the ADC stops but the device still remembers the operational state. When the device returns to ACTIVE mode without any digital reset event, the AUX ADC will restart and continue from its "pre-frozen" state.

## 8.3.2.3 Synchronization Between MAIN and AUX ADC Measurements

## When AUX\_CELL\_ALIGN = 0x0 in the ADC\_CTRL2 register, the device aligns AUX Cell Measurement (CB

MUX - Slot 5) with the target VC channel slot on MAIN cell. DieTemp2 starts without any delay, and AUX cell CB MUX slot #5 moves dynamically to match the selected MAIN cell, and the remaining AUX ADC slots adjust accordingly. This ensures that there is no time skew between MAIN VC and AUX CB ADCs sampling.

## When AUX\_CELL\_ALIGN = 0x1, then the dynamic alignment is disabled and the AUX Cell Measurement (CB

MUX Slot #5) is always aligned to Main ADC Cell 8 Measurement (MAIN ADC Slot #12). **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* **... **

# MAIN ADC Cell16 \[slot20\] Cell1 \[slot5\] Busbar \[slot21\] GPIO1 \[slot22\] Typ 192 µs DieTemp1 \[slot1\]

Spare \[slot24\] Spare \[slot23\] TSREF \[slot4\] **... ** Spare \[slot2\] *Typ 8 µs*

| Spare | \[slot3\] |
|:--- |:--- |
| Cell2 | \[slot6\] |
| Cell3 | \[slot7\] | Cell2 \[slot6\] Cell3 \[slot7\] **... **

# AUX ADC Spare \[slot20\] CB MUX \[slot5\] Spare \[slot21\] Spare \[slot22\] DieTemp2 \[slot1\]

Spare \[slot24\] Spare \[slot23\] Spare \[slot4\] **... ** Spare \[slot2\] *Typ 8 µs*

| Spare | \[slot3\] |
|:--- |:--- |
| Diag1 | \[slot6\] |
| Diag2 | \[slot7\] | Diag1 \[slot6\] Diag2 \[slot7\]

# a) \[AUX\_CELL\_SEL\] = 00h t Running all active cell channels set by ACTIVE\_CELL\_CONF register. Ch1 conversion. **... **

# MAIN ADC Cell16 \[slot20\] Cell1 \[slot5\] Busbar \[slot21\] GPIO1 \[slot22\] Typ 192 µs DieTemp1 \[slot1\]

Spare \[slot24\] Spare \[slot23\] TSREF \[slot4\] **... ** Spare \[slot2\] *Typ 8 µs*

| Spare | \[slot3\] |
|:--- |:--- |
| Cell2 | \[slot6\] |
| Cell3 | \[slot7\] | Cell2 \[slot6\] Cell3 \[slot7\] **... **

# AUX ADC Spare \[slot20\] Diag1 \[slot6\] Spare \[slot21\] Spare \[slot22\] DieTemp2 \[slot1\]

Spare \[slot24\] Spare \[slot23\] Spare \[slot4\] **... ** Spare \[slot2\] *Typ 8 µs*

| Spare | \[slot3\] |
|:--- |:--- |
| CB MUX | \[slot5\] |
| Diag2 | \[slot7\] | CB MUX \[slot5\] Diag2 \[slot7\]

# b) \[AUX\_CELL\_SEL\] = 00h t Running all active cell channels set by ACTIVE\_CELL\_CONF register. Ch2 conversion. **... **

# MAIN ADC Cell16 \[slot20\] Cell1 \[slot5\] Busbar \[slot21\] GPIO1 \[slot22\] Typ 192 µs DieTemp1 \[slot1\]

Spare \[slot24\] Spare \[slot23\] TSREF \[slot4\] **... ** Spare \[slot2\] *Typ 8 µs*

| Spare | \[slot3\] |
|:--- |:--- |
| Cell2 | \[slot6\] |
| Cell3 | \[slot7\] | Cell2 \[slot6\] Cell3 \[slot7\] **... **

# AUX ADC Spare \[slot20\] Diag1 \[slot6\] Spare \[slot21\] Spare \[slot22\] DieTemp2 \[slot1\]

Spare \[slot24\] Spare \[slot23\] Spare \[slot4\] **... ** Spare \[slot2\] *Typ 8 µs*

| Spare | \[slot3\] |
|:--- |:--- |
| Diag2 | \[slot7\] |
| CB MUX | \[slot5\] | Diag2 \[slot7\] CB MUX \[slot5\]

# c) \[AUX\_CELL\_SEL\] = 04h t Lock to AUX CELL 3. Ch3 conversion.

# Figure 8-12. Synchronization Between MAIN and AUX ADC Sampling

# 8.3.3 Cell Balancing

# The device integrates internal cell balancing MOSFET (CBFET) across each CB channel to enable passive cell

balancing. The balancing current is determined by the cell voltage, the external resistor in series with the CB pin, and the internal CBFET Rdson, R DSON parameter. The following equations calculate the effective balancing current with or without adjacent CBFETs being on. Cell balancing can run in ACTIVE or SLEEP mode. - • Balancing with no consecutive CBFET on ( Figure 8-13 (a)): I CB = VCell / ((2 × R CB ) + Rdson QCB ) - • Balancing with two consecutive CBFETs on ( Figure 8-13 (b)): I CB = (Sum of two VCELL) / ((2 × R CB ) +  Rdson QCBn + Rdson( QCBn-1 ) )

## BQ79616 SLUSF21 - JUNE 2023 **<https://www.ti.com**>

## Submit Document Feedback

Copyright © 2023 Texas Instruments Incorporated

(a) Cell balancing with internal CBFET (b) Cell balancing with 2 consecutive CBFETs on

# CB

# CB

# VC

# VC

# VC

# CB CB Control VCELL ADC signal path VCELL ADC signal path Device CBn CB n CBn-1 Cn

# CB CB n-1 VC n-1

# CB

# CB

# VC

# VC

# VC

# CB CB Control VCELL ADC signal path VCELL ADC signal path Device CBn CB n CBn-1 Cn

# CB CB n-1

# CB CB n-2 VC n-1 VC n VC n-1 + + + +

## Figure 8-13. Internal Cell Balancing and the Flow of Balancing Current

## 8.3.3.1 Set Up Cell Balancing

## There are three steps to set up cell balancing. Each step is described in detail in the following subsections. The

host MCU follows the steps to configure the balancing control before starting cell balancing. Balancing starts by setting *BAL\_CTRL2\[BAL\_GO\]* = 1. The *BAL\_STAT\[CB\_RUN\]* = 1 indicates the cell balancing is actively running. Note that channels not selected by ACTIVE\_CELL\[NUM\_CELL3:0\] are bypassed during cell balancing. 1. Determine which channel to enable for cell balancing. 2. Select the cell balancing control methods, auto or manual balancing control. 3. Decide the additional control configuration: a. Will the thermal management based on thermistor measurement be enabled? b. Is cell balancing stop based on cell voltage? c. Will cell balancing terminate if any unmasked fault is detected?

## 8.3.3.1.1 Step 1: Determine Balancing Channels

## The device provides an individual balancing timer for each channel. The balancing timer is the primary control

setting to start and stop the cell balancing on a channel. The balancing timer is configured by *CB\_CELL\*\_CTRL * registers, where \* = 1 to 16 corresponding to CBFET 1 (CB channel 1) to CBFET 16 (CB channel 16). A non-zero value in these registers sets up the corresponding channels for balancing, but the CBFETs will not turn on until MCU issues the *BAL\_CTRL2\[BAL\_GO\]* = 1. When a channel balancing timer expires, cell balancing on that channel stops. Cell balancing can also stop with other conditions, like cell voltage below a certain threshold, unmasked fault is detected, or a forced stop by the host. Section 8.3.3.3 summarizes the cell balancing stop conditions.

## 8.3.3.1.2 Step 2: Select Balancing Control Methods

## The cell balancing runs autonomously once it is configured. The cell balancing control can be configured in two

ways using the *BAL\_CTRL2\[AUTO\_BAL\]* bit. - • Auto balancing control ( *\[AUTO\_BAL\]* = 1): With this method, host MCU can enable balancing on any channel.  Once the host sends a *\[BAL\_GO\]* = 1, balancing starts and the device will automatically duty cycle all enabled CBFETs in an odd and even manner. The duty cycle is configured by *BAL\_CTRL1\[DUTY2:0\]* bits. - - Example 1: MCU sets up all 16 channels for cell balancing. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* Odd CBFETs Even CBFETs

# CB\_DUTY By *\[DUTY2:0\]*

# CB\_DUTY By *\[DUTY2:0\]* Odd CBFETs Even CBFETs **... **

# Start CB [AUTO_BAL] = 1, AND $$ [BAL_GO] = 1 $$ time

Cycle continues until any stop condition is met

**Example: Both odd and even CB\_CELL\*\_CTRL registers have non-zero setting  **

**Figure 8-14. Auto Balancing Control, Example 1** - - Example 2: MCU sets up odd or even channels only for cell balancing. The *BAL\_CTRL1\[DUTY2:0\]* bits  setting is ineffective because the device is not switched between odd or even channels. Odd CBFETs Odd CBFETs

# CB\_DUTY By *\[DUTY2:0\]*

# CB\_DUTY By *\[DUTY2:0\]* Odd CBFETs Odd CBFETs **... ** **Start CB** [AUTO_BAL] = 1, AND time

Cycle continues until any stop condition is met

**Example: Odd CB\_CELL\*\_CTRL registers have non-zero value ** **                  Even CB\_CELL\*\_CTRL registers are all zero    **

**Figure 8-15. Auto Balancing Control, Example 2** - • Manual balancing control ( *\[AUTO\_BAL\]* = 0): With this method, the device will turn on the CBFETs that  have non-zero balancing timer settings once *\[BAL\_GO\]* = 1 is received. There is no odd and even channel switching during the cell balancing and the *BAL\_CTRL1\[DUTY2:0\]* setting does not apply under this control. Host MCU can enable two consecutive CBFETs with this method and a maximum of eight CBFETs can be enabled. When two consecutive CBFETs are enabled with both channels connected to battery cells, the balancing current is significantly different compared to no adjacent CBFET being on ( Figure 8-13 ). The *DEV\_CONF\[NO\_ADJ\_CB\]* bit is provided to avoid inadvertent enabling of an adjacent CBFET for a system that is not intended to have an adjacent channel on for balancing. In this control method, the device is relying on the MCU to enable the proper channels. If the MCU sends *\[BAL\_GO\]* = 1 but the CBFETs are enabled with an invalid condition, the device will not start balancing and will set *BAL\_STAT\[INVALID\_CBCONF\]* = 1. Invalid configurations are either: - - More than eight channels are enabled for balancing (that is, more than eight *CB\_CELL\*\_CTRL* registers  have non-zero settings), - *- DEV\_CONF\[NO\_ADJ\_CB\]* = 1, but adjacent channels are enabled for balancing, - *- DEV\_CONF\[NO\_ADJ\_CB\]* = 0, but more than two consecutive channels are enabled for balancing: - • Example: Enabling CBFET 1, 2, 4, 5, 7, 10, 12, and 14 is valid. - • Example: Enabling CBFET 1, 2, and 3 is invalid.

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated **... ** time

CBFETs with non-zero value in the CB\_CELL\*\_CTRL timer * * registers are on

# Start CB [AUTO_BAL] = 0, AND $$ [BAL_GO] = 1 $$

Cycle continues until any stop condition is met **Figure 8-16. Manual Balancing Control**

**8.3.3.1.3 Step 3a: Balancing Thermal Management**

With passive balancing, heat is generated through the internal CBFETs and the external balancing resistors. This creates two hotspots on the PCB, the device, and the balancing resistors area. The device is designed to support up to 240 mA at 75°C ambient. Higher balancing current can be supported with lower ambient temperature.

The device provides two thermal management functions to avoid overheating the die as well as managing the PCB temperature. Both functions monitor temperature, either die temperature or thermistor temperature, to automatically pause balancing if temperature exceeds a pause threshold. When temperature falls below a recovery threshold, balancing resumes automatically. In the cell balancing pause state, all balancing timers and balancing settings are "frozen", balancing will resume with the same configuration when the device is out of the pause state. - • CB TWARN Balancing Pause: There are die temperature sensors built near the internal CBFETs. When  *\[BAL\_GO\]* = 1 is sent, these temperature sensors are enabled. If any of the sensors detect a die temperature \> than the T CB\_TWARN threshold (105°C nominal), balancing on all channels is paused. The device sets the *BAL\_STAT\[CB\_INPAUSE\]* = 1 and *BAL\_STAT\[OT\_PAUSE\_DET\]* = 1. When all sensors detect die temperature \< (T CB\_TWARN - T CB\_HYS ), cell balancing will resume on the balancing enabled channels. - • Thermistor OTCB Balancing Pause: To manage thermal increases due to external balancing resistors, the  device has an option to pause cell balancing on all channels if any of the active thermistors connected to GPIOs detects a temperature greater than a threshold set by *OTCB\_THRESH\[OTCB\_THR3:0\]*. Once a OTCB detection is triggered, the *BAL\_STAT\[CB\_INPAUSE\]* = 1 and *BAL\_STAT\[OT\_PAUSE\_DET\]* = 1. The balancing on all enabled channels will resume once all active thermistors detect a temperature less than a recovery threshold set by ( *OTCB\_THRESH\[OTCB\_THR3:0\]* + *OTCB\_THRESH\[COOLOFF2:0\]* ). The OTCB detection is performed through the integrated OT protector. The protector must be turned on and running in round robin mode before cell balancing starts. See Section 8.3.4 for the protector control details. To use the OTCB function, MCU follows the setup sequence state below: - - Before enabling OT protector: - • GPIO used for this function will be configured to ADC and OTUT inputs. - *• \[OTCB\_THR3:0\]* and *\[COOLOFF2:0\]* are configured. - - Enable the OT protector in round robin mode. - - Set *\[OTCB\_EN\]* and *\[BAL\_GO\]* to 1.

Failure to do so may result in no OTCB pausing action or pausing at the wrong temperature. If a different OTCB or COOLOFF threshold is needed, MCU configures the new threshold values and then re-starts the OT protector to latch in the new setting. It is not required to resend the *\[BAL\_GO\]* = 1. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

Check OT & OTCB Check OT & OTCB Check OT & OTCB

# BAL OFF BAL ON Check OT & OTCB Check OT & OTCB

# BAL OFF BAL ON BAL OFF Check OT & OTCB **System enables OTUT Protector** **... **

**System enables OTCB & ** **start balancing**

Balancing block takes OTCB result from OT comparator to its control logic **... ** Check OT & OTCB **... ** Detected OTCB Detected COOLOFF **Balancing completed** Check OT and COOLOFF hysteresis Check OT & COOLOFF hysteresis Check OT & OTCB **... **

OT comparator starts checking on COOLOFF hysteresis

# PAUSE PERIOD OT comparator Cell Balancing function time

OTCB result is not used by the device Balancing block OTCB result is not used by the device Balancing block

Balancing block no longer looking at OTCB result from OT comparator

**Figure 8-17. Cell Balancing Pause and Resume by OTCB Detection**

**8.3.3.1.4 Step 3b: Option to Stop On Cell Voltage Threshold**

Besides the balancing timers, cell balancing can stop if the channel voltage is less than a threshold set by the *VCB\_DONE\_THRESH* register with a non-zero value. This stop voltage threshold applies to all channels. When this stop option is used, a channel will stop its balancing either if its balancing timer expires or its voltage level is less than *VCB\_DONE\_THRESH* setting.

The detection of the *VCB\_DONE\_THRESH* setting is performed by the integrated UV protector. The protector must be turned on and running in round robin mode before cell balancing starts. See Section 8.3.4 for the protector control details.

When using the VCB\_DONE detection function, the MCU follows the setup sequence state below:

- • Configure the *VCB\_DONE\_THRESH* register - • Enable the UV protector in round robin mode - • Send *\[BAL\_GO\]* to 1

Failure to do so may result in no VCB\_DONE detection or cell balancing stops at a wrong channel voltage.

If different *VCB\_DONE* thresholds are needed, MCU configures the new threshold values and then re-starts the UV protector to latch in the new setting. It is not required to resend the *\[BAL\_GO\]* = 1.

**8.3.3.1.5 Step 3c: Option to Stop at Fault**

The device provides an option to abort cell balancing if an unmasked fault is detected. To enable this option, MCU sets *BAL\_CTRL2\[FLTSTOP\_EN\]* = 1 before starting cell balancing. If cell balancing is aborted under this condition, the *BAL\_STAT\[ABORTFLT\]* = 1. ***8.3.3.2 Cell Balancing in SLEEP Mode***

Cell balancing can be operated in both ACTIVE and SLEEP modes. To run cell balancing in SLEEP mode, simply configure and start cell balancing in ACTIVE mode first. Once cell balancing is running, put the device in SLEEP mode. Cell balancing will continue autonomously in SLEEP mode. See Section 8.4 for description of putting device in SLEEP mode.

When cell balancing is completed with *BAL\_STAT\[CB\_DONE\]* = 1, there is an option to put the device in a different power mode by using the *BAL\_CTRL2\[BAL\_ACT1:0\]*. For example, setting *\[BAL\_ACT1:0\]* to 0b10 (SHUTDOWN mode) and start cell balancing, When cell balancing is completed in all balancing enabled channels, the device will automatically enter SHUTDOWN mode without MCU interaction. When multiple devices are connected in daisy chain structure, one device may complete its balancing but another may not. Using this option can result with devices in different power states for some period of time. See Section 8.3.3.3 for details about the *BAL\_STAT\[CB\_DONE\]* bit set conditions. ***8.3.3.3 Pause and Stop Cell Balancing*** **8.3.3.3.1 Cell Balancing Pause**

Cell balancing can be paused by one of three methods:

- • If die temperature during balancing \> T CB\_TWARN.

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

- • If *\[OTCB\_EN\]* = 1 when any thermistor detects a temperature greater than OTCB\_THR. - • MCU sets *BAL\_CTRL2\[CB\_PAUSE\]* = 1.

The first two conditions are described in Section 8.3.3.1.3. The third pause condition is a MCU-controlled pause action usually used during a diagnostic check that involves the CB path. MCU can pause cell balancing through the *\[CB\_PAUSE\]* bit at any given time once balancing starts.

When the cell balancing is paused due to any of the pause methods, the pause activity is the same:

- • Turn off CBFETs on all channels. - • All balancing timers are in hold or "freeze" state. - *• BAL\_STAT\[CB\_INPAUSE\]* = 1. - • Any unmasked fault detected during the pause state does not terminate cell balancing. This is because the  pause event can be used during diagnostic and fault insertion can be part of the diagnostic.

Once the device exits the cell balancing pause state, the cell balancing resumes. Cell balancing timers will continue the count down. CB channels with non-zero values in their timers will continue with the balancing. **8.3.3.3.2 Cell Balancing Stop**

Cell balancing stops in one of three conditions summarized in Table 8-5. **Table 8-5. Cell Balancing Stop Conditions**

**Stop Condition** **Apply to Individual Channel?** Set BAL_STAT[CB_DONE] = 1?

Cell balancing timer expires Yes, this stop condition is monitored per channel Yes, when all channels meet either stop condition 1 or stop condition 2. CB channel voltage \< *VCB\_DONE\_THRESH* register value

Yes, this stop condition is monitored per channel

*\[FLTSTOP\_EN\]* = 1 and unmasked fault is detected

No, this stops cell balancing on all channels No, instead set *BAL\_STAT\[ABORTFLT\]* = 1

Additionally, MCU can also force stop cell balancing on any particular channel or on all channels by either: - • Zeroing out the balancing timer setting and issuing *\[BAL\_GO\]* = 1. - • Setting a voltage greater than the CB channel voltage in the *VCB\_DONE\_THRESH* register and issuing  $$ [BAL_GO] = 1. $$

Because the cell balancing timer is the primary control to start cell balancing, if the MCU resets all balancing timers to 0 with *\[BAL\_GO\]* = 1, the device does not start balancing and *BAL\_STAT\[CB\_DONE\]* remains 0.

On the other hand, if any of the cell balancing timers is non-zero but the *VCB\_DONE\_THRESH* register is set to a threshold greater than all CB channel voltages with *\[BAL\_GO\]* = 1, the device starts cell balancing because of non-zero values on the balancing timers, but immediately stops because of the *VCB\_DONE\_THRESH* stop condition. The *BAL\_STAT\[CB\_DONE\]* is set to 1 for this condition. **8.3.3.3.3 Remaining CB Time**

Each channel has a balancing timer, when balancing starts, the timers start counting down from the configured balancing time set by *CB\_CELLn\_CTRL* registers, where n= 1 to 16. When balancing is pause, these timers are paused.

To read the remaining CB time, MCU set *\[BAL\_TIME\_SEL3:0\]* to select a single channel, then issue *\[BAL\_TIME\_GO\]* = 1 which latch the remaining CB time of the selected channel to *BAL\_TIME* register. Repeat the steps to read other remaining CB time on other channels. This timer information is only valid if CB is running, in pause state or in a valid CB stop condition.

If *BAL\_TIME* register reports 0x7F or 0xFF, which is not a valid value. This indicates the balancing configuration is keeping the balancing in a stop state, such as *\[BAL\_GO\]* = 1 with all balancing timer set to 0, or MCU never issue [BAL_GO] = 1. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* **Table 8-6. BAL\_TIME Register Status**

**CB Stop Condition** ***BAL\_TIME*** ** Register**

Cell balancing timer expires The selected CB channel reports 0-s

CB channel voltage \< *VCB\_DONE\_THRESH* register value The selected CB channel reports the remaining CB time *\[FLTSTOP\_EN\]* = 1 and unmasked fault is detected ***8.3.3.4 Module Balancing***

A small current can sink through GPIO as a way to balance the module voltage. The host can connect a loading resistor on the GPIO and configure the GPIO as digital output high which then loading current through CVDD that is regulated from the module stack. Such control can be turned on or off manually by the host.

Alternatively, the device can control this loading path through a function called module balancing (MB). The concept remains the same as depleting module voltage through a loading resistor connected to a GPIO (MB takes over GPIO3 for this function). However, host can set a module balancing timer and a stop threshold to automatically turn off the loading path through the module balancing function.

# LOAD

# GND

# GPIO3

Stack\_N-1 Sink current is limited by the max GPIO output current limit

# LOAD

# GPIO3 Stack\_N-1

Host set non-zero to MB\_TIMER\_CTRL Register, device configures GPIO3 as Output High and will be enable module timer And monitor BAR voltage for the balancing Daisy Chain Comm **Figure 8-18. Module Balancing** **8.3.3.4.1 Start Module Balancing**

1. Set a non-zero value to the *MB\_TIMER\_CTRL* register. 2. Configure the stop MB voltage threshold in the *VMB\_DONE\_THRESH* register. 3. The stack module monitoring is performed through AUX ADC. So host starts AUX ADC in continuous. 4. Send BAL_CTRL2[BAL_GO] = 1. 5. GPIO3 will be taken over for this function and is set to digital output port and starts sinking current through a loading resistor. *BAL\_STAT\[MB\_RUN\]* = 1 **8.3.3.4.2 Stop Module Balancing**

Once started, MB stops if one of the following occurs: - • Balancing timer reaches *MB\_TIMER\_CTRL* setting, device will set *BAL\_STAT\[MB\_DONE\]* = 1.

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

- • BAT voltage is less than *VMB\_DONE\_THRESH* setting (AUX ADC must be on), device will set  BAL_STAT[MB_DONE] = 1. - • Host stops the balancing by setting *MB\_TIMER\_CTRL* = 0 and sends *BAL\_CTRL2\[BAL\_GO\]* = 1.  BAL_STAT[MB_DONE] = 0. - • If *BAL\_CTRL\[FLTSTOP\_EN\]* = 1 and an unmasked fault is detected, *BAL\_STAT\[MB\_DONE\]* = 0

**Note** - • There is no pause control (manual pause or thermal pause) to module balancing. - • If AUX ADC stops (either stopped by the host or device enters SLEEP mode) during module  balancing, the device will not stop module balancing based on BAT voltage. Module balancing will stop by the MB timer expiration condition. - *• BAL\_CTRL2\[BAL\_ACT1:0\]* setting applies to the module balancing function as well. When the  *\[MB\_DONE\]* = 1 (and *\[CB\_DONE\]* = 1 if CB is enabled), device can enter the power mode set by the *\[BAL\_ACT1:0\]* setting. **8.3.4 Integrated Hardware Protectors**

The device integrates cell OV and UV protectors and thermistor OT and UT protectors with programmable thresholds independent of the ADC functionality or the ADC measurements path. The OVUV and OTUT protectors can operate in ACTIVE or SLEEP mode. The subsections below provide an overview of the protectors. See Section 8.3.6.4 for diagnostic control function and status of this block. ***8.3.4.1 OVUV Protectors***

A set window comparator provides cell voltage monitoring for all VC channels. This comparator function is entirely separate from the ADC function and as such, even if the ADC function fails, the analog comparators still flag the crossing of the overvoltage (OV) and undervoltage (UV) comparator thresholds. The programmed thresholds are translated through DACs to the comparators. BCI filters

# MAINAD CMUX

# VC16 **:** **:** Main ADC Digital FAULT\_OV and FAULT\_UV registers

# AAF + LS **:** **:**

# OVUV MUX **:** **:**

# VC0 **:** OV Comp UV Comp **Figure 8-19. OV and UV Protectors**

The OV and UV thresholds set by *OV\_THRESH* and *UV\_THRESH* registers are the same for all VC channels. The active channels are defined by the *ACTIVE\_CELL\[NUM\_CELL3:0\]* bits. These bits set the highest active channel number and the device assumes any lower channels are also active.

The *UV\_DISABLE1* and *UV\_DISABLE2* registers setting disable any individual channel for UV detection, such as channel is connected to bus bar.

Otherwise, the OV protector detects an OV fault on a particular channel if the VC channel voltage is greater than the OV\_THRESH setting. The UV protector detects a UV fault on a particular channel if the VC channel voltage is less than the UV\_THRESH setting. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* **8.3.4.1.1 OVUV Operation Modes**

## The OV and UV protectors have several operation modes controlled by OVUV\_CTRL\[OVUV\_MODE1:0\] and is

summarized in Table 8-7. To start the OVUV protectors, MCU sets *OVUV\_CTRL\[OVUV\_GO\]* = 1.

## Table 8-7. OVUV Protector Operation Modes

***\[OVUV\_MOD1:0\]*** **Operation Mode** **Description**

0b00 Stop OV and UV protectors Stop OV and UV protectors

0b01 Round robin run The OV and UV protectors are looping through all VC inputs. The active channels are checked against the OV and UV thresholds ( Figure 8-19 ). The round robin cycle timing is always the same regardless of the number of the active channels. For the inactive VC channels, the digital logic simply ignores the detection outcome. The UV protector detects both *UV\_THRESH* and *VCB\_DONE\_THRESH*.

0b10 OV and UV BIST run (diagnostic use, see Section 8.3.6.4 for details)

A BIST (built-in self-test) cycle on the OV and UV comparators and the detection paths. VCELL (VC channels) ADC measurement from the Main ADC and the OV and UV detections through the OVUV protectors are not available during this run. MCU shall stop ADC measurement when performing OVUV BIST.

0b11 Single channel run (diagnostic use, see Section 8.3.6.4 for details)

Use for checking the OV and UV DACs. The OV and UV comparator is locked to a single VC input channel in this mode. Channel is locked by *OVUV\_CTRL\[OVUV\_LOCK3:0\]*.

## If OVUV BIST run is in progress, but MCU start ADC, the ADC result registers will be held at 0x8000. ADC

measurements will resume once OVUV BIST is completed and after t AFE\_SETTLE time pass.

## If ADC is running, but MCU start OVUV BIST, the ADC result registers will be held at its last measurement. ADC

measurement update resumes once OVUV BIST is completed and after t AFE\_SETTLE time pass

# OV

CELL1 **... ** OV CELL16 OV CELL1 **... ** OV Round robin

# OV\_CYCLE

**Note: The round robin cycle time is always the same regardless the number of active channel **

# UV CELL1 **... ** UV CELL16

# VCB\_DONE\_THRESH

CELL1 **... ** UV and VCB\_DONE Round robin *UV\_CYCLE*

# VCB\_DONE\_THRESH CELL16

# UV CELL1 **... **

# UV\_CYCLE

# Stop if \[OVUV\_MODE1:0\] = 0b00, AND $$ [OVUV_GO] = 1 $$

# Stop if \[OVUV\_MODE1:0\] = 0b00, AND $$ [OVUV_GO] = 1 $$ Time

# Set \[OVUV\_MODE1:0\] = 0b01, AND Set [OVUV_GO] = 1

## Figure 8-20. OV and UV Round Robin Mode **8.3.4.1.2 OVUV Control and Status** ***8.3.4.1.2.1 OVUV Control***

## To start the OV and UV protectors, MCU sets OVUV\_CTRL\[OVUV\_GO\] = 1. When the device receives the

GO command, it samples the following register settings and then starts the OVUV protectors accordingly. Any change of the settings below requires the MCU to resend another GO command to implement the new settings. - *• OV\_THRESH* register: Sets the OV threshold for all VC channels - *• UV\_THRESH* register: Sets the UV threshold for all VC channels

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

- *• VCB\_DONE\_THRESH* register: Sets the VCB\_DONE threshold for cell balancing stop condition (if enabled) - *• OVUV\_CTRL\[OVUV\_MODE1:0\]*: OVUV operation mode selection - *• ACTIVE\_CELL* register: Determines the inactive VC channel(s) and ignores the detection result accordingly - *• UV\_DISABLE1* and *UV\_DISABLE2* registers: Determines the inactive VC channel(s) and ignores the  detection result accordingly.

The OVUV protectors can also operate in SLEEP mode. MCU first starts the protector in ACTIVE mode, then puts the device in SLEEP mode. The OVUV protectors will continue the operation until the MCU commands to stop or if the device shuts down. ***8.3.4.1.2.2 OVUV Status***

The *DEV\_STAT\[OVUV\_RUN\]* = 1 indicates the OVUV protectors are running. The OV detection result is reflected in the *FAULT\_OV1* and *FAULT\_OV2* registers; the UV detection result is reflected in the *FAULT\_UV1 * and *FAULT\_UV2* registers.

The VCB\_DONE detection is not a fault but a cell balancing stop condition. The result is reflected in a particular channel stopping cell balancing. See Section 8.3.3 for details. ***8.3.4.2 OTUT Protector***

A set window comparator provides temperature monitoring for all GPIO inputs with the external thermistor network pulled up to TSREF. This comparator function is entirely separate from the ADC function and, as such, even if the ADC function fails, the analog comparators still flag the crossing of the overtemperature (OT) and undertemperature (UT) comparator thresholds. The programmed thresholds are translated through DACs to the comparators.

# AUX ADC MUX

# GPIO MUX

# GPIO\[1:8\]

# To AUX ADC Digital FAULT\_OT and FAULT\_UT registers

# Main ADC MUX

| To Main | ADC |
|:--- |:--- |
| UT | Comp |
| OT | Comp | UT Comp OT Comp **Figure 8-21. OT and UT Protectors**

The OT and UT thresholds set by *OTUT\_THRESH\[OT\_THR4:0\]* and *OTUT\_THRESH\[UT\_THR2:0\]* bits are the same for all active GPIO inputs. The active GPIO inputs are defined by the *GPIO\_CONFn\[GPIO\*2:0\]* (where n = 1 to 4, \* = 1 to 8 for the corresponding GPIO input). The GPIO has to be configured as ADC and OTUT inputs to be considered as active GPIO inputs for the OTUT protectors.

The OTUT comparators use TSREF as reference, and so the detection is in ratiometric form. The OT protector detects an OT fault on a particular GPIO if the (GPIO voltage/TSREF) is less than the *OTUT\_THRESH\[OT\_THR4:0\]* setting. The UT protector detects a UT fault on a particular GPIO if the (GPIO **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## voltage/TSREF) is more than the OTUT\_THRESH\[UT\_THR2:0\] setting. The OTUT protectors assume the NTC

thermistor is used for temperature monitoring.

## MCU ensures TSREF is enabled before starting the OTUT protectors. Failing to do so, the OTUT protectors will

flag all OT and UT faults on all GPIO inputs as an indication of abnormal detection. **8.3.4.2.1 OTUT Operation Modes**

## The OT and UT protectors have several operation modes controlled by OTUT\_CTRL\[OTUT\_MODE1:0\] and are

summarized in Table 8-8. To start the OTUT protectors, the MCU sets *OTUT\_CTRL\[OTUT\_GO\]* = 1.

## Table 8-8. OTUT Protector Operation Modes

***\[OTUT\_MOD1:0\]*** **Operation Mode** **Description**

0b00 Stop OT and UT protectors Stop OT and UT protectors

0b01 Round robin run The OT and UT protectors are looping through all GPIO inputs. The active GPIO inputs are checked against the OT and UT thresholds ( Figure 8-22 ). The round robin cycle timing is always the same regardless of the number of the active GPIOs. For the inactive GPIO inputs, the digital logic simply ignores the detection outcome. The OT protector detects both OT threshold and OTCB threshold.

0b10 OT and UT BIST run (diagnostic use, see Section 8.3.6.4 for details)

A BIST (built-in self-test) cycle on the OT and UT comparators and the detection paths. Temperature (GPIO channels) ADC measurement from the main or AUX ADC and the OT and UT detections through the OTUT protectors are not available during this run.

0b11 Single channel run (diagnostic use, see Section 8.3.6.4 for details)

Used for checking the OT and UT DACs. The OT and UT comparator is locked to a single GPIO input channel in this mode. Channel is locked by *OTUT\_CTRL\[OTUT\_LOCK2:0\]*.

# UT GPIO1 **... ** UT GPIO8 **... ** UT Round robin

# UT\_CYCLE

**Note**: The round robin cycle time is always the same regardless of the number of active GPIO inputs

# UT GPIO1 **... **

# UT GPIO8

# OT GPIO1 **... ** OT GPIO8 **... ** OT and OTCB Round robin

# OT\_CYCLE

# OTCB GPIO1 **... **

# OTCB GPIO8

# OT\_CYCLE

# Time

Set [OTUT_MODE1:0] = 0b01, AND Set [OTUT_GO] = 1

# Stop if \[OTUT\_MODE1:0\] = 0b00, AND $$ [OTUT_GO] = 1 $$

# Stop if \[OTUT\_MODE1:0\] = 0b00, AND $$ [OTUT_GO] = 1 $$

## Figure 8-22. OT and UT Round Robin Modes **8.3.4.2.2 OTUT Control and Status** ***8.3.4.2.2.1 OTUT Control***

## Ensure TSREF is enabled. To start the OT and UT protectors, host MCU sets OTUT\_CTRL\[OTUT\_GO\] = 1.

When the device receives the GO command, it samples the following register settings and then starts the OTUT protectors accordingly. Any change of the settings below requires the MCU to send another GO command to implement the new settings. - *• OTUT\_THRESH\[OT\_THR4:0\]*: Sets the OT threshold for all active GPIO inputs - *• OTUT\_THRESH\[UT\_THR2:0\]*: Sets the UT threshold for all active GPIO inputs

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## • • OTCB\_THRESH register: Sets the OTCB threshold and COOLOFF hysteresis (if enabled)

- *• OTUT\_CTRL\[OTUT\_MODE1:0\]*: OTUT operation mode selection - *• GPIO\_CONF1* to *GPIO\_CONF4*: Determines the inactive GPIO channel(s) and ignores the detection result.

## The OTUT protectors can also operate in SLEEP mode. MCU first starts the protector in ACTIVE mode, then

puts the device in SLEEP mode. The OTUT protectors will continue the operation until the MCU commands them to stop or if device shuts down. ***8.3.4.2.2.2 OTUT Status***

## The DEV\_STAT\[OTUT\_RUN\] = 1 indicates the OTUT protectors are running. The OT detection result is reflected

in the *FAULT\_OT* register; the UT detection result is reflected in the *FAULT\_UT* register.

## The OTCB detection is not a fault but a cell balancing pause condition. The result is reflected in a particular

channel pausing cell balancing. See Section 8.3.3 for details.

## 8.3.5 GPIO Configuration

## The device has eight GPIOs. Each GPIO can be programmed to be one of the configurations below through the *GPIO\_CONF1* to *GPIO\_CONF4* registers.

# GPIO

# DISAB

**LE** **INPUT** **OUTPUT** **WEAK PULL-UP/** **DOWN** **SPECIAL** **High-Z** ** ** **Digita** **l**

# ADC & **OTUT** **ADC ** **Only** **High** **Low** **ADC & ** **weak ** **pull-up** **ADC & ** **weak ** **pull-down** **Module Balancing** ***MB\_TIMER\_CTRL *** **is not 0x00** **SPI Controller**

# \[SPI\_EN\] = 1 **Fault Input** [FAULT_IN_ EN] =

# GPIO1 √ √ √ √ √ √ √ √

# GPIO2 √ √ √ √ √ √ √ √ GPIO3 √ √ √ √ √ √ √ √ √ (output, HIGH)

# GPIO4 √ √ √ √ √ √ √ √ √ (SS)

# GPIO5 √ √ √ √ √ √ √ √ √ (MISO)

# GPIO6 √ √ √ √ √ √ √ √ √ (MOSI)

# GPIO7 √ √ √ √ √ √ √ √ √ (SCLK) GPIO8 √ √ √ √ √ √ √ √ √ (input, active low) **GPIO Configuration** **Description**

DISABLE High-Z This is the default GPIO configuration at reset if OTP is not programmed

# INPUT

Digital When GPIO is configured as Digital Input, the device detects the input voltage level to determine a 1 or 0 with respect to its V IL and V IH levels. The result is shown in the *GPIO\_STAT* register.

ADC and OTUT The GPIO is configured to be measurable by the ADC (both main and AUX ADCs) and also as the input to the OTUT protectors. Example: use this selection for GPIO used for thermistor connection.

ADC only The GPIO is configured to be measurable by the ADC (both main and AUX ADCs) only. Example: use this selection to measurement voltage on GPIO.

# OUTPUT

High The GPIO is configured as digital output high (internally pull up to CVDD). The logic state is also shown in the *GPIO\_STAT* register.

| Low | The GPIO is configured as digital output low. The logic state is also shown in the GPIO\_STAT register. |
|:--- |:--- |
| WEAK PULL- | UP/DOWN |
| ADC and Weak | Pull-up |

# WEAK PULL UP/DOWN ADC and Weak Pull-up

The GPIO is pull up internally and is configured to be measured by the ADC (both main and AUX ADCs) ADC and Weak Pull-down

The GPIO is pull down internally and is configured to be measured by the ADC (both main and AUX ADCs) **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* **GPIO Configuration** **Description**

# SPECIAL Module Balancing

When the *MB\_TIMER\_CTRL* register is non-zero, GPIO3 will be taken over to be used in the module balancing control. This configuration has higher priority over any of the INPUT/OUTPUT configurations on GPIO3. SPI Controller

When *GPIO\_CONF1\[SPI\_EN\]* = 1, GPIO4 to GPIO7 are taken over as the SPI controller communication lines. This configuration has higher priority over any of the INPUT/OUTPUT configurations on GPIO4 to GPIO7.

Fault Input When *GPIO\_CONF1\[FAULT\_IN\_EN\]* = 1, GPIO8 is taken over as an input that if the GPIO was asserted (active low), will set *FAULT\_SYS\[GPIO\]* = 1 and assert NFAULT (if enabled).

## 8.3.6 Communication, OTP, Diagnostic Control ***8.3.6.1 Communication***

## The device can operate as a standalone device in a multidrop configuration ( DEV\_CONF\[MULTIDROP\_EN\] =

1. or as a base/stack device in a daisy chain configuration ( *DEV\_CONF\[MULTIDROP\_EN\]* = 0). In multidrop  configuration, the daisy chain communication is disabled and the host communicates only with a single device through UART interface. This document will focus on the daisy chain communication.

## In daisy chain configuration, each device is identified by a 6-bit device address; hence, up to 64 devices can

be connected in the daisy chain. In this configuration, a device is either defined to a base (interface with host through UART) or a stack (interface through the daisy chain ports COMH/COML to the base device). The base description in this document assumes the use of BQ79616 as base device. If a communication extender (also known as bridge device) is used as a base, user must refer to the bridge device's datasheet for details.

## 8.3.6.1.1 Serial Interface

## The device has a serial interface which uses UART protocol as the physical layer to communicate between base

device and host. The communication is specified in a proprietary frame structure. **UART Protocol:**

bit0 bit1 bit2 bit3 bit4 bit5 bit6 bit7 START STOP **... ** **... ** bit period

bit period bit period = 1/ baud rate ½ bit period

# INIT\[7:0\]

**Transaction Frame Structure (to/from system MCU to the base device):** A transaction frame consists of 5 types of information as shown above. Data are all sent in byte, and each byte is sent through UART protocol.

# DEV ADR\[7:0\]

REG ADR\[15:8\] REG ADR\[7:0\] DATA MSB\[7:0\]... DATA LSB\[7:0\] CRC\[15:8\] CRC\[7:0\] Base device RX

# TX

# MCU TX

# RX Command Frame Response Frame

Both Command and Response Frames shall follow the ** Transaction Frame Structure**

**Each frame is sent through the UART Protocol ** Half-duplex

## Figure 8-23. UART Communication to Host

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated ***8.3.6.1.1.1 UART Physical Layer***

The UART interface follows the standard serial protocol of 8-N-1, where it sends information as a START bit, followed by eight data bits, and then one STOP bit. The STOP bit indicates the end of the byte. If a byte is received that does not have the STOP bit set, the *FAULT\_COMM1\[STOP\_DET\]* bit is set, indicating there may be a baud rate issue between the host and the device. The device supports 1-Mbps baud rate. Additionally, during development, a slower baud rate is needed to debug the communication, an optional 250-kbps baud rate can be enabled under communication debug mode.

The UART sends data on the TX pin and receives data on the RX pin. When idle, the TX and RX pins are high. The UART interface requires that RX is pulled up to CVDD through a resistor on the base device. The RX is pulled up on the device side. Do not leave RX unconnected. Ensure RX is connected directly to CVDD for stack devices.

The TX pin is disabled in stack devices, but must be pulled high through a resistor on the host side on base device to prevent triggering an invalid communications frame when the communication cable is not attached, or during power-off or SHUTDOWN state when TX is high impedance. TX is always pulled to CVDD internally while in ACTIVE or SLEEP mode, whether enabled or disabled. Leave TX unconnected if not used in stack devices.

The UART interface is strictly a half-duplex interface. While transmitting, any attempted communication on RX is ignored. The only exception is COMM CLEAR signal on RX pin, which immediately terminates the communication. See Section 8.3.6.1.1.1.3 for details. Using two STOP bits in UART:

The device can be set up with two stop bits ( *DEV\_CONF\[TWO\_STOP\_EN\]* = 1), the UART response frame transmits from device to host will always return with two STOP bits as shown below. Host is not required to send the command frame to the device with two STOP bits. The device is able to receive one or more stop bits with or without this function enabled.

bit0 bit1 bit2 bit3 bit4 bit5 bit6 bit7 START STOP **...** **... **

bit period bit period bit period = 1/ baud rate ½ bit period 2-bit period

**Figure 8-24. UART Response Frame with Two STOP Bits**

Potential use of the two stop bits may be to: - • The host to gain extra time to process the data before receiving next data frame. - • The clock tolerance between device and host might cause the data detection out of sync. Having two STOP  bits allows re-synchronization of the communication; hence, improving communication robustness.

Although UART is only used by the base device, if the *\[TWO\_STOP\_EN\]* = 1, the stack devices also set the *\[TWO\_STOP\_EN\]* = 1 even though UART is not used in stacks. It is because the stack devices will use the bit setting to determine the proper gap applying between two communication frames. ***8.3.6.1.1.1.1 UART Transmitter***

The transmitter is configured to wait a specified number of bit periods after the last bit reception before starting transmissions using the *TX\_HOLD\_OFF* register. This provides time for the host to switch the bus direction at the end of its transmission. The UART transmitter is disabled by default in the stack devices. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* Command frame Response frame

# TX\_HOLD\_OFF

Last bit of the command frame received by device

Start sending the 1 st bit of the response frame

Device is ready to return the response but is holding off by the TX\_HOLD\_OFF register

# To MCU **Time** device RX device TX data direction data direction

# Figure 8-25. UART TX\_HOLD\_OFF ***8.3.6.1.1.1.2 UART Receiver***

While the device is transmitting data on TX, RX is ignored except when receiving a COMM CLEAR. To avoid collisions during data transmission up the daisy-chain interface, the host must wait until all bytes of a communication transmission are received from the device before attempting additional communication to the device. If the host starts a transmitting without waiting to receive the preceding transaction's response, the communication is not considered reliable and the host must send a COMM CLEAR to restore normal communications to the base device.

# 8.3.6.1.1.1.3 COMM CLEAR

A COMM CLEAR is sent on the RX pin of the base device. It does not send to the stack devices. RX cannot be disabled and a COMM CLEAR can be sent at any time regardless of the TX status. Ensure that the COMM CLEAR does not exceed the maximum value of t UART(CLR) bit periods, as this may result in recognition of other communication pings.

# UART(CLR) RX pin 1 bit period

# UART(StA)

# COMM CLEAR SLEEPtoACTIVE ping 1 bit period

Wait 1-bit period to start the next communication

# Figure 8-26. UART COMM CLEAR

Use the COMM CLEAR command to clear the receiver and instruct the UART engine to look for a new start of frame. The next byte following the COMM CLEAR is always considered a start-of-frame byte. When detected, a COMM CLEAR sets the *FAULT\_COMM1\[COMMCLR\_DET\]* flag. The host must wait at least t UART(RXMIN) after the COMM CLEAR to start sending a new frame. It should be noted that in addition to the *\[COMMCLR\_DET\] * flag, the *FAULT\_COMM1\[STOP\_DET\]* flag is also set because the COMM CLEAR timing violates the typical byte timing and the STOP bit is seen as 0.

A SLEEPtoACTIVE ping/tone also clears the UART receiver. This ping/tone sets the *\[COMMCLR\_DET\] * flag when transiting from SLEEP to ACTIVE mode. If this ping/tone is sent during ACTIVE mode, the *\[COMMCLR\_DET\]* and *\[STOP\_DET\]* flags are set.

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

**COMM CLEAR sent during daisy chain communication:**

When a read command is sent, but the response has not yet completely returned to the host, if a COMM CLEAR is received in the base device at this condition, the device response is discarded. In addition, the stack devices do not see the COMM CLEAR and continue to send their responses which are forwarded to the host, resulting in host receiving unexpected response frames. Hence, host should avoid this condition by waiting until all responses are received from the stack before sending a COMM CLEAR.

If the above condition occurs, the base device low-level communication debug register *DEBUG\_UART\_RR\_TR\[TR\_WAIT\]* (indicating device is waiting to transmit response) or *DEBUG\_UART\_RR\_TR\[TR\_SOF\]* (indicating a COMM CLEAR is received while device is transmitting data) bits can be set depending on the timing in receiving the COMM CLEAR signal.

When using the multidrop configuration, a COMM CLEAR signal must be used before every frame to ensure consistent communication.

***8.3.6.1.1.2 Command and Response Protocol***

The host initiates every transaction between the host and device. The device never transmits data without first receiving a command frame from the host. A command frame is a communication frame sent from host to the device; a response frame is a response (to a read command) from device to host. After a command frame is transmitted, the host must wait for all expected responses to be returned (or a timeout in case of error) before initiating a new command frame. The commands supported by the device are listed in Table 8-9. **Table 8-9. Commands**

| Command | Description |
|:--- |:--- |
| Single Device Read | To read a register(s) from a single device (base or stack) |
| Single Device Write | To write a register(s) to a single device (base or stack) |

Single Device Read To read a register(s) from a single device (base or stack)

Single Device Write To write a register(s) to a single device (base or stack)

Stack Read To read a register(s) from the stack devices only. The device must be configured as a stack device with *COMM\_CTRL\[STACK\_DEV\]* = 1 to respond to Stack Read commands..

Stack Write To write a register(s) for only the stack devices. The device must be configured as a stack device with *COMM\_CTRL\[STACK\_DEV\]* = 1 to respond to Stack Write commands.

Broadcast Read To read a register(s) for all of the devices in the daisy chain, including base device.

Broadcast Read To write a register(s) for all of the devices in the daisy chain, including base device. Broadcast Write Reverse Direction

To send a broadcast write in the reverse direction set by *CONTROL1\[DIR\_SEL\]* bit. This command is intended to be used for switching the communication direction with the RING interface.

***8.3.6.1.1.2.1 Transaction Frame Structure***

The protocol layer is made up of transaction frames. There are two basic types of transaction frames: command frames (transactions from host) and response frames (transactions from device). The transaction frames are made up of the following five field types: - • Frame initialization (INIT, 1-byte) - • Device address (DEV ADR, 1-byte) - • Register address (REG ADR, 2-byte) - • Data (DATA, various byte length) - • Cyclic redundancy check (CRC, 2-byte)

***8.3.6.1.1.2.1.1 Frame Initialization Byte***

The frame initialization byte is used in both command and response frames. It is always the first byte of the frame. The frame initialization byte performs two functions. First, it defines the frame as either a command frame (host) or a response frame (device). Second, it defines the length of the frame that follows after the frame initialization byte. This provides the receiver an exact number of bytes to expect for a complete command or response. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## Table 8-10. Command Frame Initialization Byte Definition **Command Frame** **Response Frame**

**Bit** **Bit Name** **Description** **Bit Name** **Description**

**INIT** FRAME\_TYPE 1 = Define Command Frame FRAME\_TYPE 0 = Defines Response Frame

REQ\_TYPE 000 = Single Device Read 001 = Single Device Write 010 = Stack Read 011 = Stack Write 100 = Broadcast Read 101 = Broadcast Write 110 = Broadcast Write Reverse $$ 111 = RSVD(1) $$

RESPONSE\_BYTE Number of the data bytes $$ 0x00 = 1 byte $$ $$ 0x01 = 2 bytes $$: $$ 0x7F = 128 bytes $$ RSVD Reserved. This bit is ignored

DATA\_SIZE Number of data bytes of the command frame, excluding device address, register address or CRC $$ 000 = 1 byte $$ $$ 001 = 2 bytes $$: $$ 111 = 8 bytes $$

(1) No function to this selection, however, selecting this setting will set the *DEBUG\_COMMH\[RC\_IERR\]* or *DEBUG\_COMMH\[RC\_IERR\] * flag depends on which daisy chain interface receives the command frame. ***8.3.6.1.1.2.1.2 Device Address Byte***

## The device address byte identifies the device targeted by the single device read/write command. This byte is

omitted for broadcast, stack, and broadcast reverse direction command frames. All response frames contain the device address byte. In single device read/write commands, the device that contains a matching value in the *DIR0\_ADDR* (used for communication direction with *CONTROL1\[DIR\_SEL\]* = 0) or in *DIR1\_ADDR* (used for communication direction with *CONTROL1\[DIR\_SEL\]* = 1) responds to the command. If multiple devices have matching values, all of those devices will respond and cause collision.

## Table 8-11. Device Address Byte Definition **Command Frame** **Response Frame**

**Bit** **Bit Name** **Description** **Bit Name** **Description**

**DEV ADR** RSVD Should always write 0 RSVD Should always write 0

RSVD Should always write 0 RSVD Should always write 0

5 to 0 Device Address Set the device address range from 0x00 to 0x3F

Device Address Set the device address range from 0x00 to 0x3F ***8.3.6.1.1.2.1.3 Register Address Bytes***

## Register addresses are two bytes in length. Any write command to an invalid register address is ignored. Any

read from an invalid register returns a 0x00 response. This is true for command frames sent to an individual register with invalid address, or as part of command sent to multiple registers with invalid addresses. When read/write addresses a block of registers with only some invalid addresses, the valid addresses respond as normal, while the invalid addresses respond as previously described.

## Table 8-12. Register Address Byte Definition **Command Frame** **Response Frame**

**Bit** **Bit Name** **Description** **Bit Name** **Description**

# REG\_ADR 7 to 0 Register Address (MSB)

| Target or beginning of the register | address |
|:--- |:--- |
| Register Address | (MSB) |
| Target or beginning of the register | address | Register Address (MSB) Target or beginning of the register address 7 to 0 Register Address (LSB)

| Target or beginning of the register | address |
|:--- |:--- |
| Register Address | (LSB) |
| Target or beginning of the register | address | Register Address (LSB) Target or beginning of the register address

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated ***8.3.6.1.1.2.1.4 Data Bytes***

## The number of data bytes and the relevant information they convey is determined by the type of command frame

sent and the target register specified in that command frame. When part of a command frame, the data bytes contain the values to be written to the registers. When part of a response frame, the data bytes contain the values returned from the registers.

## Table 8-13. Data Bytes Definition **Command Frame** **Response Frame**

**Bit** **Bit Name** **Description** **Bit Name** **Description**

# DATA Data Byte\[0\]

For Write command: Data value to be written to the register(s) is specified in the REG\_ADR frame For Read command: Specify the number of bytes need to be returned by the read command. $$ 0x00 = 1 byte $$ $$ 0x01 = 2 bytes $$: $$ 0x7F = 128 bytes $$ Data Byte\[0\]

Data value return from the register(s) is specified in the REG\_ADR frame........................... Data Byte \[n\]

For Write command: Data value to be written to the register(s) is specified in the REG\_ADR frame Data Byte \[n\]

Data value return from the register(s) is specified in the REG\_ADR frame ***8.3.6.1.1.2.1.5 CRC Bytes***

## The device uses a CRC (cyclic redundancy check) to protect data integrity during transmission. The CRC

represents the remainder of a process analogous to polynomial long division, where the frame being checked is divided by the generator. The CRC appended to the frame is the remainder. Because of this process, when the device receives a frame, the CRC calculated by the receiver across the entire frame including the transmitted CRC will be zero, indicating a correct transmission and reception. A non-zero result indicates a communication error. Specifically, the device uses the CRC-16-IBM polynomial (x 16 + x 15 + x 2 + 1 ) with 0xFFFF initialization.

## The CRC value is checked as the first step after receiving the communication frame. If the CRC is incorrect, the

entire frame is discarded and not processed. Any additional frame errors are not checked and any errors are not indicated other than CRC error. The bytes are still transferred up or down the stack, thus every device that processed the frame will indicate a CRC error. This results in multiple devices indicating CRC faults on the same communication frame.

***8.3.6.1.1.2.1.6 Calculating Frame CRC Value***

## The CRC calculation by the transmitter is in bit-stream order across the entire transmission frame (except for

the CRC). When determining bit-stream order for implementing the CRC algorithm, it is important to note that protocol bytes transmit serially, least-significant bit first. Figure 8-27 illustrates the bit-stream order concept. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## Figure 8-27. Bit-Stream Order Explanation

## The CRC (0x0000) is appended to the end of the bit-stream. This bit-stream is then initialized by XOR'ing with

0xFFFF to catch any leading 0 errors. This new bit-stream is then divided by the polynomial (0xC002) until only the 2-byte CRC remains. During this process, the most significant 17 bits of the bit stream are XOR'd with the polynomial. The leading zeroes of the result are removed and that result is XOR'd with the polynomial once again. The process is repeated until only the 2-byte CRC remains. For example:

## Example 1: CRC Calculation Using Polynomial Division

$$ Command Frame = 0x80 00 02 0F 0B (0b1000 0000 0000 0000 0000 0010 0000 1111 0000 1011) $$ $$ Command Frame in bit stream order = 0x01 00 40 F0 D0 (0b0000 0001 0000 0000 0100 0000 1111 0000 $$ 1101 0000) $$ After Initialization (XOR with 0xFFFF) = 0b1111 1110 1111 1111 0100 0000 1111 0000 1101 0000 $$ 1111 1110 1111 1111 0100 0000 1111 0000 1101 0000 0000 0000 0000 0000 #append 0x0000 for CRC 1100 0000 0000 0010 1 #XOR with polynomial 0011 1110 1111 1101 1100 0000 1111 0000 1101 0000 0000 0000 0000 0000 11 1110 1111 1101 1100 0000 1111 0000 1101 0000 0000 0000 0000 0000 #delete leading zeros from previous result 11 0000 0000 0000 101 #XOR with polynomial 00 1110 1111 1101 0110 0000 1111 0000 1101 0000.................. 1100 0110 0000 0001 0000 0000 1100 0000 0000 0010 1 #XOR with polynomial 0000 0110 0000 0011 1000 0000 110 0000 0011 1000 0000 110 0000 0000 0001 01 #XOR with polynomial 000 0000 0011 1001 0100 0000 0011 1001 0100 #CRC result in bit stream order 1100 0000 0010 1001 #final CRC result in normal order CRC final 0xC029 ***8.3.6.1.1.2.1.7 Verifying Frame CRC***

## There are several methods for checking the CRC of a frame. One method is to simply calculate the CRC for

the transmitted command except the last two bytes (CRC bytes) using the method described in the previous section, and then compare that result with the transmitted CRC bytes. A more simple option is to run the entire transmission through the CRC algorithm. If the CRC is correct, the result is 0000. In this case, the initial zero padding of the bit-stream with 16 zeroes is not necessary. Using the previous result and running through the algorithm produces the following results:

## Example 1: CRC Verification Using Polynomial Division

$$ Command Frame = 0x80 00 02 0F 0B (0b1000 0000 0000 0000 0000 0010 0000 1111 0000 1011) $$ CRC to Check = 0xC029 $$ Command Frame w/ CRC in bit stream order = 0x80 00 02 0F 0B C0 29 (0b1000 0000 0000 0000 0000 0010 $$ 0000 1111 0000 1011 0000 0011 1001 0100) $$ After Initialization (XOR with 0xFFFF) = 0b0 1111 1110 1111 1111 0100 0000 1111 0000 1101 0000 0000 $$ 0011 1001 0100 1111 1110 1111 1111 0100 0000 1111 0000 1101 0000 0000 0011 1001 010 #delete leading zeros from previous result 1100 0000 0000 0010 1 #XOR with polynomial 0011 1110 1111 1101 1100 0000 1111 0000 1101 0000 0000 0011 1001 0100 11 1110 1111 1101 1100 0000 1111 0000 1101 0000 0000 0011 1001 0100 #delete leading zeros from

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

previous result 11 0000 0000 0000 101 #XOR with polynomial 00 1110 1111 1101 0110 0000 1111 0000 1101 0000 0000 0011 1001 0100.................. 1100 0110 0000 0010 1001 0100 1100 0000 0000 0010 1 #XOR with polynomial 0000 0110 0000 0000 0001 0100 1 1000 0000 0000 0101 00 1 1000 0000 0000 0101 #XOR with polynomial 0 0000 0000 0000 0000 00 0x0000 #verfiy that CRC checks out valid **Note**

The result of '0b0000 0000 0000 0000' for the CRC indicates a successful check.

***8.3.6.1.1.2.2 Transaction Frame Examples***

Transaction frames are created using the frame structure discussed in the previous sections. This section outlines how the command and response frames are passing through the daisy chain. The CRC values in the examples are correct and can be used to verify the customer CRC algorithm. The CRC is verified by the device with every received command frame and the command is not executed unless the CRC is valid.

***8.3.6.1.1.2.2.1 Single Device Read/Write*** **Single Device Read**:

Device address must be set up before using this command. A single device read generates a response frame whose length depends on the requested number of register bytes read. The command frame send by host must contain the register address to start at (address field) and the number of bytes to return (number of registers to read). The DATA\_SIZE field in the initialization byte for the single device read command is always 0b000.

The command frame travels to all devices in the daisy chain, but only the device that matches the command frame's device address field will respond to the single device read command. The corresponding device will respond with returned data request by the single device read, following the response frame format. **Single Device Write**:

Device address must be set up before using this command. A write command for a single device enables the customer to update up to eight consecutive registers with one command. The single device write command frame must contain the register address to start at (address field) and the data bytes to write to the registers. The DATA\_SIZE field in the initialization byte for the single device write command is the number of registers to update.

The command frame travels to all devices in the daisy chain, but only the device that matches the command frame's device address field will execute the single device write command. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

# S1

# COML

# COMH

# S2

# COML

# COMH

# B0 RX

# TX

# COMH

# COML

# S3

# COML

# COMH

# \[DIR0\_ADDR\] = 0

# \[DIR0\_ADDR\] = 1

# \[DIR0\_ADDR\] = 2

# \[DIR0\_ADDR\] = 3 [TOP_STACK] = 1

# MCU TX RX

**Host sends Single Read ** **command (addressing to S2)**

**Single Read command being forward ** **through the stack**

**Only the addressed ** **device responds after ** **receiving the command**

# S1

# COML

# COMH

# S2

# COML

# COMH

# B0 RX

# TX

# COMH

# COML

# S3

# COML

# COMH

# \[DIR0\_ADDR\] = 0

# \[DIR0\_ADDR\] = 1

# \[DIR0\_ADDR\] = 2

# \[DIR0\_ADDR\] = 3 [TOP_STACK] = 1

# MCU TX RX

**Host sends Single Write command** **(addressing to S2)**

**Single Write command being forward ** **through the stack**

**Only the addressed device ** **executes the command**

**(a) Single Read Command to S2** **(b) Single Write Command to S2**

## Figure 8-28. Single Device Read/Write

## Table 8-14. Single Device Read/Write

**Single Read Command Sent by Host** **Single Write Command Sent by Host**

**Example** **Read 16 Cell Voltages from S2** **Write OTP Unlock Code to OTP\_PROG\_UNLOCK1A to 1D ** **Registers**

**Frame Field** **Data** **Comments** **Data** **Comments** Initialization Byte

0x80 Always 0x80 FRAME_TYPE = 1 REQ_TYPE = 0b000 = Single Read $$ DATA_SIZE = 0b000 $$

0x93 0x90 for 1 byte data read, 0x91 for 2 bytes data read, 0x92 for 3 bytes data read, and so on. For this example: FRAME_TYPE = 1 REQ_TYPE = 0b001= Single Write DATA_SIZE = 0b11 = 4 bytes Device Address

0x02 Device address 0x02 (S2) in this example 0x02 Device address 0x02 (B0) in this example Register Address

0x0568 Start address of the register block to read (address of VCELL16\_HI in this example)

0x0300 Start address of the register block to write (address of OTP\_PROG\_UNLOCK1A in this example)

Data 0x1F Instruct the target device to return 32 bytes of data (that is, from address 0x0568 to 0x0587), assuming each VCELLn_HI = 0x80, VCELLn_LO = 0x00, where n = 1 to 16.

0x02B7 78BC The unlock value to OTP\_PROG\_UNLOCK1A to OTP\_PROG\_UNLOCK1D

# CRC 0x5A6F 0xB8AE ***8.3.6.1.1.2.2.2 Stack Read/Write***

## Stack Read

## The device address, COMM\_CTRL\[STACK\_DEV\] bit and \[TOP\_STACK\] bit must be configured before using this

command. A stack read command generates a number of response frames depending on the number of devices in the stack (that is, device with *COMM\_CTRL\[STACK\_DEV\]* = 1), whose length depends on the requested number of register bytes read. The stack read command frame must contain the register address to start at (address field) and the number of bytes to return (number of registers to read). The DATA\_SIZE field in the initialization byte for the read command is always 0b000.

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

# The

command frame travels to all devices in the daisy chain, but only the device with *COMM\_CTRL\[STACK\_DEV\]* = 1 will respond. During the response, the device with *COMM\_CTRL\[TOP\_STACK\] * = 1 will return the response frame first. Each device (address N) in the stack waits until the device above (address N+1) responds before appending its response frame. The CRC is validated while receiving the responses. If a CRC error occurs in the response frame from address N+1, device N does not append its message and an invalid CRC fault is generated.

# Use Figure 8-29 with the example of using reading 16 cell voltages from S1 to S3. The response to this

command is 3 separate response frames (one response frame per device), each frame with a total length of 38 bytes (32 data bytes + 6 protocol bytes). Although the stack read command does not contain the device address field, each response frame will contain the corresponding device address field associating the data to a particular device. The host will receive a response frame from S3 first (ToS), following with a response frame from S2, and finally the response frame from S1.

# Stack Write

# The COMM\_CTRL\[STACK\_DEV\] must be configured before using this command. A stack write command

enables the host to update up to eight consecutive registers for the stack devices (that is, device with *COMM\_CTRL\[STACK\_DEV\]* = 1) with one command. The command frame must contain the register address to start at (address field) and the data bytes to write to the registers. The DATA\_SIZE field in the initialization frame is the number of registers to update.

# The

command frame travels to all devices in the daisy chain, but only the device with *COMM\_CTRL\[STACK\_DEV\]* = 1 will execute the command.

# S1

# COML

# COMH

# S2

# COML

# COMH

# B0 RX

# TX

# COMH

# COML

# S3

# COML

# COMH

# \[DIR0\_ADDR\] = 0

# \[DIR0\_ADDR\] = 1

# \[DIR0\_ADDR\] = 2

# \[DIR0\_ADDR\] = 3 [TOP_STACK] = 1

# MCU TX RX

| Host sends broadcast Read | command |
|:--- |:--- |
| Stack Read command being forward | through the stack |
| Device in top of stack | responds first |

**Stack Read command being forward ** **through the stack**

**Device in top of stack ** **responds first**

# S1

# COML

# COMH

# S2

# COML

# COMH

# B0 RX

# TX

# COMH

# COML

# S3

# COML

# COMH

# \[DIR0\_ADDR\] = 0

# \[DIR0\_ADDR\] = 1

# \[DIR0\_ADDR\] = 2

# \[DIR0\_ADDR\] = 3 [TOP_STACK] = 1

# MCU TX RX

**Host sends Single Write ** **command (addressing to S1)**

**Stack Write command being forward ** **through the stack**

**All the devices identified as ** **³VWDFN´** **H\[HFXWHWKHFRPPDQG** **except B0 (as it is identified as ** **³EDVH´** **)**

**(a) Stack Read Command** **(b) Stack Write Command**

**After S2 receives ** **response from S3, S2 ** **also responds and ** **process continues for ** **the rest of the device.**

**B0 (identified as base ** **device) only forward the ** **response and does not ** **return its own data **

# Figure 8-29. Stack Read/Write

## www.ti.com

# BQ79616 SLUSF21 - JUNE 2023

## Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## Table 8-15. Stack Read/Write

**Stack Read Command Sent by Host** **Stack Write Command Sent by Host**

**Example** **Read 16 Cell Voltages from S1 to S3** **Write OTP Unlock Code to OTP\_PROG\_UNLOCK1A to 1D ** **Registers to S1, S2, and S3**

**Frame Field** **Data** **Comments** **Data** **Comments** Initialization Byte

0xA0 Always 0xA0 FRAME_TYPE = 1 REQ_TYPE = 0b010 = Stack Read $$ DATA_SIZE = 0b000 $$

0xB3 0xB0 for 1 byte data read, 0xB1 for 2 bytes data read, 0xB2 for 3 bytes data read, and so on. For this example: FRAME_TYPE = 1 REQ_TYPE = 0b011= Stack Write DATA_SIZE = 0b011 = 4 bytes Device Address

N/A No need to include the device address byte in command frame

N/A No need to include the device address byte in command frame Register Address

0x0568 Start address of the register block to read (address of VCELL16\_HI in this example)

0x0300 Start address of the register block to write (address of OTP\_PROG\_UNLOCK1A in this example)

Data 0x1F Instruct each device to return 32 bytes of data (that is, from address 0x0568 to 0x0587), assuming each VCELLn_HI = 0x80, VCELLn_LO = 0x00, where n = 1 to 16.

0x02B7 78BC The unlock value to OTP\_PROG\_UNLOCK1A to OTP\_PROG\_UNLOCK1D

# CRC 0x5C2D 0x0BD7 ***8.3.6.1.1.2.2.3 Broadcast Read/Write***

## Broadcast Read

## The device address and \[TOP\_STACK\] bit must be configured before using this command. A broadcast read

command generates a number of response frames depending on the number of devices in the daisy chain (both stack and base devices), whose length depends on the requested number of register bytes read. The broadcast read command frame must contain the register address to start at (address field) and the number of bytes to return (number of registers to read). The DATA\_SIZE field in the initialization byte for the read command is always 0b000.

## The command frame travels to all devices in the daisy chain, every device will respond. During the response,

the device with *COMM\_CTRL\[TOP\_STACK\]* = 1 will return the response frame first, each device (address N) in the stack waits until the device above (address N+1) responds before appending its response frame. The CRC is validated while receiving the responses. If a CRC error occurs in the response frame from address N+1, device N does not append its message and an invalid CRC fault is generated.

## Use Table 8-16 with the example of reading 16 cell voltages from B0 to S3. The response to this command is 4

separate response frames (one response frame per device), each frame with a total length of 38 bytes (32 data bytes + 6 protocol bytes). Although the broadcast read command does not contain the device address field, each response frame will contain the corresponding device address field, associated the data to a particular device. The host will receive the response frame from S3 first (ToS), following with the response frame from S2, then S1, and finally the response frame from B0.

## Broadcast Write

## This command can be used without auto-addressing. A broadcast write command enables the host to update

up to eight consecutive registers for all devices in the daisy chain with one command. The command frame must contain the register address to start at (address field) and the data bytes to write to the registers. The DATA\_SIZE field in the initialization frame is the number of registers to update.

## The command frame travels to all the devices in the daisy chain, and every device in the daisy chain will execute the command.

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

# S1

# COML

# COMH

# S2

# COML

# COMH

# B0 RX

# TX

# COMH

# COML

# S3

# COML

# COMH

# \[DIR0\_ADDR\] = 0

# \[DIR0\_ADDR\] = 1

# \[DIR0\_ADDR\] = 2

# \[DIR0\_ADDR\] = 3 [TOP_STACK] = 1

# MCU TX

# RX

| Host sends broadcast Read | command |
|:--- |:--- |
| Broadcast Read command being | forward through the stack |
| Device in top of stack | responds first |

**Broadcast Read command being ** **forward through the stack**

**Device in top of stack ** **responds first**

# S1

# COML

# COMH

# S2

# COML

# COMH

# B0 RX

# TX

# COMH

# COML

# S3

# COML

# COMH

# \[DIR0\_ADDR\] = 0

# \[DIR0\_ADDR\] = 1

# \[DIR0\_ADDR\] = 2

# \[DIR0\_ADDR\] = 3 [TOP_STACK] = 1

# MCU TX RX

**Host sends Single Write command** **(addressing to S1)**

**Broadcast Write command being forward ** **through the stack** **All the devices execute the ** **command**

**(a) Broadcast Read Command** **(b) Broadcast Write Command**

**After S2 receives ** **response from S3, S2 ** **also responds.**

**Process continues until ** **all devices send their ** **response**

## Figure 8-30. Broadcast Read/Write

## Table 8-16. Broadcast Read/Write

**Broadcast Read Command Sent by Host** **Broadcast Write Command Sent by Host**

**Example** **Read 16 Cell Voltages from B0 to S3** **Write OTP Unlock Code to OTP\_PROG\_UNLOCK1A to 1D ** **Registers to B0, S1, S2, and S3**

**Frame Field** **Data** **Comments** **Data** **Comments** Initialization Byte

0xC0 Always 0xC0 FRAME_TYPE = 1 REQ_TYPE = 0b100 = Broadcast Read $$ DATA_SIZE = 0b000 $$

0xD3 0xD0 for 1 byte data read, 0xD1 for 2 bytes data read, 0xD2 for 3 bytes data read, and so on. For this example: FRAME_TYPE = 1 REQ\_TYPE = 0b101= Broadcast Write DATA_SIZE = 0b011 = 4 bytes Device Address

N/A No need to include the device address byte in command frame

N/A No need to include the device address byte in command frame Register Address

0x0568 Start address of the register block to read (address of VCELL16\_HI in this example)

0x0300 Start address of the register block to write (address of OTP\_PROG\_UNLOCK1A in this example)

Data 0x1F Instruct each device to return 32-bytes of data (that is, from address 0x0568 to 0x0587), assuming each VCELLn_HI = 0x80, VCELLn_LO = 0x00, where n = 1 to 16.

0x02B7 78BC The unlock value to OTP\_PROG\_UNLOCK1A to OTP\_PROG\_UNLOCK1D

# CRC 0x422D 0x6BD1

***8.3.6.1.1.2.2.4 Broadcast Write Reverse Direction***

## Usually, device is expecting to receive communication based on the \[DIR\_SEL\] setting. If a device receives

communication frame opposite to the *\[DIR\_SEL\]* setting, such as receiving command frame from COMH while *\[DIR\_SEL\]* = 0, it will flag the communication as error. The broadcast write reverse direction is a command used to change flip the *\[DIR\_SEL\]* setting when host needs to switch the daisy chain communication direction. This command is expected to receive from an opposite direction than the \[DIR\_SEL\] setting during reverse communication direction procedure. See Section 8.3.6.1.3.4 for details. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## Although the broadcast write reverse direction is allowed to write any register value to the device, it is not

recommended to write any other register setting other than the *CONTROL1\[DIR\_SEL\]* to avoid communication collisions. Communication collisions are not detected and result in corrupted communication on the stack interface.

# S1

# COML

# COMH

# S2

# COML

# COMH

# B0 RX

# TX

# COMH

# COML

# S3

# COML

# COMH

# \[DIR0\_ADDR\] = 0

# \[DIR0\_ADDR\] = 1

# \[DIR0\_ADDR\] = 2

# \[DIR0\_ADDR\] = 3 [TOP_STACK] = 0

# MCU TX RX

**Host sends Single Write command to change** **B0 communication direction** **Reverse Broadcast Write Command**

**Host sends Reverse Broadcast Write ** **command to change stack devices ** **communication direction**

## Figure 8-31. Broadcast Write Reverse Direction

## Table 8-17. Broadcast Write Reverse Direction

**Broadcast Write Reverse Direction Command Sent by Host**

**Example** **Set the ** ***\[DIR\_SEL\]*** ** = 1 on All Devices in the Daisy Chain** **Frame Field** **Data** **Comments**

Initialization Byte 0xE0 Always 0xE0 FRAME_TYPE = 1 REQ\_TYPE = 0b110 = Broadcast Write Reverse Direction $$ DATA_SIZE = 0b000 $$

| Device Address | N/A | No need to include the device address byte in command frame |
|:--- |:--- |:--- |
| Register Address | 0x0309 | Address of CONTROL1 register |
| Data | 0x80 | Set CONTROL1\[DIR\_SEL\] = 1 |

Register Address 0x0309 Address of *CONTROL1* register

# Data 0x80 Set CONTROL1[DIR_SEL] = 1

# CRC 0xC014

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated **8.3.6.1.2 Daisy Chain Interface**

The daisy chain communication is created using differential signaling to minimize Electro-Magnetic Susceptibility (EMS) and Bulk Current Injection (BCI) immunity. The differential communication transmits true and complement data on the COM\*P and COM\*N pins, respectively. In a multiple device stack, there are configurations where the devices are physically located on the same board or located in entirely separate packs connected with twisted-pair wiring.

The device supports the use of transformers or capacitors to electrically isolate the signals between devices in the stack. For applications that have multiple devices on the same PCB, a single level-shifting capacitor is connected between the COMH/L pins of the devices. For extremely noisy environments, additional filtering may be necessary. For devices that are separated by cabling, additional isolation components are used. See Section 9 for specific details on selecting components.

***8.3.6.1.2.1 Daisy Chain Transmitter and Receiver Functionality***

The daisy chain is bidirectional and half duplex, and, therefore, has a transmitter (TX) and receiver (RX) on the COMH and COML interfaces. The TX and RX functions are controlled automatically by the hardware based on the device's base/stack detection. When a WAKE ping/tone is received, the communication direction is set by *CONTROL1\[DIR\_SEL\]* and the *COMM\_CTRL\[TOP\_STACK\]* configurations. See Section 8.3.6.1.3 for details. Additionally, a user overwrites to take over the complete control of the COMH and COML is available under communication debug mode using the *DEBUG\_CTRL\_UNLOCK*, *DEBUG\_COMM\_CTRL1*, and *DEBUG\_COMM\_CTRL2* registers. See Section 8.5.4.14 for details. ***8.3.6.1.2.2 Daisy Chain Protocol***

The differential daisy chain (vertical) interface uses an asynchronous 13-bit byte-transfer protocol. Data is transferred LSB first and every bit is duplicated (with a complement) to ensure the transmission has no DC content.

# PW\_DC 2 x t PW\_DC

# CVSS

# COM\*P \\pm COMP\*N

# COM\*P

# COM\*N

# CVDD µ 1 ¶ µ 0 ¶

# PW\_DC

# PW\_DC **Figure 8-32. Daisy Chain Bit Definition**

A byte starts with a Preamble, followed by two SYNC bits, a start-of-frame bit, eight data bits starting from the LSB D0 to MSB D7 (D0 is transmitted just after State-Of-Frame and D7 comes last before the Byte Error and Postamble).

The device extracts timing information using the Preamble and SYNC bits to decode the rest of the bit value in the byte. If any of the following errors is detected, the byte is not processed and register error bit is set. - • The Preamble and SYNC bits are known values, if the decoded value has error, the *DEBUG\_COMH/* *L\_BIT\[SYNC1\]* = 1 depends on which COM port receives this data. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

# • • If timing extracted from the Preamble and SYNC bits is outside of the expected range, the DEBUG\_COMH/ $$ L_BIT[SYNC2] = 1. $$

# Once the two valid SYNC bits are received, the additional bits are decoded and sent to the command processor.

The device continues to detect any error on this byte, and if error is detected, the Byte Error (BERR) bit will be set in this byte. The *DEBUG\_COMH/L\_BIT\[PERR\]* = 1 depends on which COM port detects the error. The following condition will set the BERR bit in the byte. - • Not sufficient samples to indicate the logic level of a bit. That is, a bit is decoded as not a strong 1 or strong 0.  The *DEBUG\_COMH/L\_BIT\[BIT\]* = 1 depends on which COM port detects the error.

# In the meantime, each bit is still being retransmitted to the next device. If the device is unable to decode a

1 or a 0 for the bit, it will retransmit with 0 with the BERR bit set in the byte. When the new device detects the BERR bit is set to 1 in the receiving byte, it will ignore the questionable byte and set the *DEBUG\_COMH/* *L\_BIT\[BERR\_TAG\]* = 1, indicating a byte is received with BERR. The questionable byte being ignored is likely to cause other communication errors and is likely to trigger the *DEBUG\_COMH/L\_BIT\[PERR\]* = 1 being set in the new device as well. The questionable byte continues to be retransmitted up the daisy chain with BERR set and the process continues.

# INIT\[7:0\] DEV ADR\[7:0\] +1 Preamble (half-bit)

# SYNC \[1:0\]

# DATA\[7:0\] Byte Error (1bit) Postamble (half-bit)

# COM\*P \\pm COMP\*N

# D0 D1 D7 D6 D5 D2 D3 D4 $$ SYNC = 2'b00 $$ +1 Preamble (half-bit)

# SYNC \[1:0\] 6.5us nominal 1.375 us of bus idle 0.5 us of bus short

# DATA\[7:0\] Byte Error (1bit) Postamble (half-bit)

# COM\*P \\pm COMP\*N

# D0 D1 D7 D6 D5 D2 D3 D4 $$ SYNC = 2'b00 $$ **Communication transmits ** **from UART** Start-Of-Frame (1bit) **Byte in daisy chain ** **transmission**

**Additional bits used for daisy chain transmission**

# Figure 8-33. Daisy Chain Byte Definition

# Table 8-18. Daisy Chain Byte Definition

## Bit Field **Description**

## Preamble (half-bit) Indicates a start of transaction, signaling the receiver to start sampling. This half-bit and the following two SYNC bits are used to extra timing information.

## SYNC\[1:0\]

Always 0b00. The SYNC bits are used for the digital to assess the timing and noise level on the byte, improving the detection of a 1 and 0 in a noisy environment.

## BQ79616 SLUSF21 - JUNE 2023 **<https://www.ti.com**>

## Submit Document Feedback

Copyright © 2023 Texas Instruments Incorporated

## Table 8-18. Daisy Chain Byte Definition (continued) **Bit Field** **Description** Start-Of-Frame (1bit)

The Start-Of-Frame (SOF) bit indicates the follow-on data byte is the initialization byte, a start of a communication transaction frame. Stack device needs this information to process the communication. For command frame transaction, the base device is responsible to set the SOF bit as it translates the UART communication to the daisy chain communication. The initialization byte contains data size information. Based on the data size information, the base device would count the number of bytes received and set the next SOF bit accordingly. The UART COMM CLEAR signal resets the UART receiver which includes the frame handling of the logic. Hence, the next byte after COMM CLEAR must have SOF set to 1 because the COMM CLEAR indicates the system clears UART and re-starts the communication.

Data\[7:0\] The actual byte of the communication transaction frame Byte Error BERR (1-bit)

Indicates an error detected in this byte. When a device receives a byte with BERR set by the lower device, it will retransmit the byte also with *BERR* = 1. Because each data bit is re-clocked from one device to the next, the next device may not detect a communication error. However, the tag of the *\[BERR\]* bit would indicate this communication frame has an error during its previous transaction. Postamble (halfbit) Indicates the end of transaction

## Each byte is transmitted at 2 MHz (250 ns per pulse or 500 ns per couplet). The time between each byte

depends on the UART baud rate (1 Mbps in normal operation), but the byte time is always the same. The communication frame is defined with idle time between byte. In some rare cases, communication signal may not terminate cleanly, leaving ringing at the end of a byte. In such case, increasing the byte to byte gap can improve the communication robustness. The device allows additional byte gap insert between bytes in the response frame through *STACK\_RESPONSE* register setting. Byte Up to 8.375 µs for a byte Byte

10.875 µs at 1Mbps 40.6us at 250Kbps (if comm debug is enable) Nominal Response byte to byte delay is fixed by the UART baud rate Up to 8.375 µs for a byte

**Apply to response frame only:** Additional byte gap configured by STACK\_RESPONSE delay

## Figure 8-34. Daisy Chain Byte Transfer **8.3.6.1.3 Start Communication**

## From SHUTDOWN or after device reset, host follows the following steps to bring up the devices for

communication. - • Host sends a WAKE ping to reset or bring the devices to ACTIVE mode. In this process, the devices in the  daisy chain will configure their own COMH and COML ports based on their position in the daisy chain (base device or stack device) - - After this step, the broadcast write is supported. - • Host performs auto-addressing to assign a device address to each device - - After this step, the broadcast read/write and single device read/write are supported. - • Host configures the *COMM\_CTRL\[STACK\_DEV\]* and *\[TOP\_STACK\]* bits. The Top of Stack (ToS) device will  disable its transmitter of the COMH (or COML based on communication direction) - - After this step, all commands, broadcast read/write, single device read/write, and stack read/write are  supported. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* **Host: ** Perform auto addressing ** ** **(b) Perform auto addressing**

# MCU TX RX WAKE ping

# WAKE TONE

# S1

# COML

# COMH

# S2

# COML

# COMH

# B0 RX

# TX

# COMH

# COML

# S3

# COML

# COMH

# UART

**B0: ** Receive WAKE ping. Identified itself as base. ** ** [DIR_SEL =0] (default): COML (both TX and RX) is disable $$ [DIR_SEL] = 0 $$

# \[DIR\_SEL\] = 0

# \[DIR\_SEL\] = 0

# \[DIR\_SEL\] = 0

**S1 to S3: ** Receive WAKE tone. Identified itself as stack. Both COML and COMH are enabled ** ** **(a) Waking up device using WAKE ping/tone**

# MCU TX RX

# S1

# COML

# COMH

# S2

# COML

# COMH

# B0 RX

# TX

# COMH

# COML

# S3

# COML

# COMH

# UART

# \[DIR\_SEL\] = 0

# \[DIR\_SEL\] = 0

# \[DIR\_SEL\] = 0

# \[DIR\_SEL\] = 0

# \[DIR0\_ADDR\] = 0

# \[DIR0\_ADDR\] = 1

# \[DIR0\_ADDR\] = 2

# \[DIR0\_ADDR\] = 3

**S3**: Based on *\[TOP\_STACK\]* & *\[DIR\_SEL\] * setting, S3, in this example, disables its COMH TX

# MCU TX RX

# S1

# COML

# COMH

# S2

# COML

# COMH

# B0 RX

# TX

# COMH

# COML

# S3

# COML

# COMH RX   TX

# UART

# \[DIR\_SEL\] = 0

# \[DIR\_SEL\] = 0

# \[DIR\_SEL\] = 0

# \[DIR\_SEL\] = 0

# \[DIR0\_ADDR\] = 0

# \[DIR0\_ADDR\] = 1

# \[DIR0\_ADDR\] = 2

# \[DIR0\_ADDR\] = 3

# \[STACK\_DEV\] = 0 [TOP_STACK] = 0

# \[STACK\_DEV\] = 1 [TOP_STACK] = 0

# \[STACK\_DEV\] = 1 [TOP_STACK] = 0

# \[STACK\_DEV\] = 1 [TOP_STACK] = 1

**Host: ** Configure *COMM\_CTRL\[STACK\_DEV\]* & *\[TOP\_STACK\]* bits to each device

# (c) Set the \[STACK\_DEV\] & \[TOP\_STACK\]

# Figure 8-35. Configure Device for Communication

# 8.3.6.1.3.1 Identify Base and Stack

# A WAKE ping/tone is used for the device to identify its position in the daisy chain.

- • Base device: a device interfaces with host through UART - • Stack device: a device interfaces with the base device through COMH and COML

# A base device will be woke up by a WAKE ping through RX pin, while a stack device will be woke up by WAKE

tone via the COMH/COML port. Hence, a device is using a WAKE ping or WAKE tone to identify itself as base or stack. This information is stored in the AVAO\_REF block which is available in all power modes and is refreshed whenever a WAKE ping/tone is received.

# Using the CONTROL1\[DIR\_SEL\] setting, a base device will disable the unused daisy chain ports (transmitter

and receiver). If host changes the *CONTROL1\[DIR\_SEL\]* setting, the base device will reconfigure its COMH/ COML.

# Note

# The host starts communication at least 100 µs after changing the \[DIR\_SEL\] setting to ensure the

device finishes the COMH/COML reconfiguration.

# 8.3.6.1.3.2 Auto-Addressing

# Every device must have a unique device address for the read protocol to work. If, for any reason, two devices

are assigned with the same device address, it is likely that broadcast and stack reads do not work. Additionally, single device read to the doubled address results in destroyed communication.

# The default device address, assuming the device address in OTP is not programmed, is 0x00. For a host to talk

to a standalone device (that is, a stack consisting with only one device), host can simply use the default 0x00 device address. Otherwise, device address follows the rules below: - • Base device address can start with any value, it is not necessary for it to be 0x00 - • All device addresses must be sequential. That is, if base is 0x00, the next device must be 0x01, and next  must be 0x02, and so on.

# Before starting the auto-addressing procedure, all devices must be in ACTIVE mode. In this state, the device

will only be able to process broadcast write command, which will be the command used for the auto-addressing procedure. Based on the *CONTROL1\[DIR\_SEL\]* setting, the auto-addressing procedure sets up the device address to either *DIR0\_ADDR* register (when *\[DIR\_SEL\]* = 0) or *DIR1\_ADDR* register (when *\[DIR\_SEL\]* = 1).

# BQ79616 SLUSF21 - JUNE 2023 **<https://www.ti.com**>

# Submit Document Feedback

Copyright © 2023 Texas Instruments Incorporated

***8.3.6.1.3.2.1 Setting Up the Device Addresses***

## The CONTROL1\[ADDR\_WR\] bit enables the auto-addressing mode. In this mode, the device turns off its

COMH/COML (depends on the *\[DIR\_SEL\]* setting) transmitter for one communication frame (following the autoaddressing procedure, that will be its own device's address), clear the *CONTROL1\[ADDR\_WR\]* = 0. When the next communication is received (following the auto-addressing procedure, it will be the next device's address), the device will forward the communication to the next device.

# MCU TX

# RX

# S1

# COML

# COMH

# B0 RX

# TX

# COMH

# COML UART

# \[DIR\_SEL\] = 0 $$ [ADDR_WR] = 1 $$

# \[ADDR\_WR\] = 1

# S2

# COML

# COMH

# \[ADDR\_WR\] = 1

**Host sending: ** DIR_ADDR = 0x00, DIR_ADDR = 0x01, DIR_ADDR = 0x02

# \[DIR\_SEL\] = 0

# \[DIR\_SEL\] = 0

# B0 RX

# TX

# COMH

# COML

**B0 receives: ** DIR_ADDR = 0x00, DIR_ADDR = 0x01, DIR_ADDR = 0x02

# \[DIR0\_ADDR\] = 0

# S1

# COML

# COMH

**B0 retransmits: ** DIR_ADDR = 0x01, DIR_ADDR = 0x02

# S1

# COML

# COMH

**S1 receives: ** DIR_ADDR = 0x01, DIR_ADDR = 0x02

# \[DIR0\_ADDR\] = 1

# S2

# COML

# COMH **S1 transmits: ** DIR\_ADDR = 0x02

# \[ADDR\_WR\] = 0

# \[ADDR\_WR\] = 1 $$ [ADDR_WR] = 0 $$

# \[ADDR\_WR\] = 1

**(a) Set ** ***\[ADDR\_WR\] *** **= 1 to all the devices and start sending in the ** **device addresses ** **(b)B0 takes the 1** **st** ** device address sent by host, clear \[ADDR\_WR\] ** **and retransmit the rest ** **(c)S1 takes the 2** **nd** ** device address sent by host, clear \[ADDR\_WR\]** **and retransmit the rest **

## Figure 8-36. Auto-Addressing

# 8.3.6.1.3.2.2 Setting Up COMM\_CTRL\[STACK\_DEV\] and \[TOP\_STACK\]

## The last procedure in the auto-addressing is to configure the COMM\_CTRL\[STACK\_DEV\] and \[TOP\_STACK\]

settings. These bits need to be configured for the broadcast read and stack read/write to work properly. - • Base device: *\[STACK\_DEV\]* = 0 and *\[TOP\_STACK\]* = 0 - • Stack devices (except ToS device): *\[STACK\_DEV\]* = 1 and *\[TOP\_STACK\]* = 0 - • ToS device: *\[STACK\_DEV\]* = 1 and *\[TOP\_STACK\]* = 1

## Table 8-19 shows the auto-addressing steps, assuming CONTROL1\[DIR\_SEL\] = 0 (that is, each device will be

set up to transmit command frame sent by host from its COML to COMH).

## Table 8-19. Auto-Addressing **Step** **Procedure**

This step is required if a device reset has occurred before performing the auto-addressing procedure. Dummy Write to synchronize all daisy chain devices DLL (delay-locked loop) ramp in write direction. Host sends broadcast write to write 0x00 to *ECC\_DATA1* to *ECC\_DATA8* registers.

Enable auto-addressing procedure. Host sends broadcast write to set *CONTROL1\[ADDR\_WR\]* = 1.

Sending in the device addresses. Host sends broadcast write to set the consecutive addresses to *DIR0\_ADDR\[ADDRESS5:0\]*. With an example of a total of three devices in a daisy chain:

1. Send broadcast write to *DIR0\_ADDR* register with data 0x00. 2. Send broadcast write to *DIR0\_ADDR* register with data 0x01. 3. Send broadcast write to *DIR0\_ADDR* register with data 0x02. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* **Table 8-19. Auto-Addressing (continued)** **Step** **Procedure**

Set up the *COMM\_CTRL\[STACK\_DEV\]* and *\[TOP\_STACK\]* bits for each device. Option 1: Host sends single device write to each device to set the proper *\[STACK\_DEV\]* and *\[TOP\_STACK\]* values. Option 2 (less communication steps):

1. Host sends broadcast write to set *\[STACK\_DEV\]* = 1 and *\[TOP\_STACK\]* = 0. 2. Host sends single device write to base device (device address 0x00 in this example) with *\[STACK\_DEV\]* = 0. 3. Host send single device write to the ToS device address 0x02 in this example) with *\[TOP\_STACK\]* = 1.

This step is required if a device reset has occurred before performing the auto-addressing procedure. Dummy read to synchronize all daisy chain devices DLL ramp in read direction. Host sends broadcast read to read *ECC\_DATA1* to *ECC\_DATA8* registers. Host may not receive all of the data as this step synchronizes the DLL.

Recommended as good practice. Use broadcast read to read *DIR0\_ADDR* registers to read back all device addresses to ensure all devices are addressed properly.

If the dummy write and dummy read steps are performed to synchronize the DLL, it is normal if communication fault is triggered. Clear the fault registers if that is the case.

***8.3.6.1.3.2.3 Storing Device Address to OTP***

The device uses *DIR0\_ADDR* (used with *\[DIR\_SEL\]* = 0) and *DIR1\_ADDR* (used with *\[DIR\_SEL\]* = 1) registers for its device address. In the auto-addressing procedure, device address is written to one of these registers and the new device address takes effect immediately.

The host has an option to program the device addresses for the *\[DIR\_SEL\]* = 0 and 1 directions to the OTP, allowing the programmed addresses to be loaded whenever the device is reset. To program the device address to OTP, host writes the desired address to the OTP shadow registers, *DIR0\_ADDR\_OTP* (used when *\[DIR\_SEL\] * = 0) and *DIR1\_ADDR\_OTP* (used when *\[DIR\_SEL\]* = 1) and performs OTP programming. These two shadow registers only reflect the value programmed in OTP or use for the host to program the desired value to OTP. These two shadow registers are not the device address setting during communication. See Section 8.3.6.3.2 for programming details. ***8.3.6.1.3.3 Synchronize Daisy Chain DLL***

When the device is reset or enters ACTIVE from SLEEP, the MCU performs a dummy write and read to synchronize the DLL on the daisy chain devices.

In the device reset case, if device address is not programmed in OTP. MCU must perform an auto-address. The DLL synchronization is part of the step. If device address is programmed in OTP, auto-address is not required after device reset. However, MCU should perform a dummy write and dummy read steps shown in Table 8-19, step1 and step5 to synchronize the DLL.

When the device goes from SLEEP to ACTIVE using SLEEPtoACTIVE signal, the device is not reset. However, it is recommend to do a 1-data-byte dummy write and read to ensure robustness. Follow the similar dummy write and read steps in Table 21, but only write and read to *OTP\_ECC\_DATAIN1*. ***8.3.6.1.3.4 Ring Communication***

The daisy chain communication for the device uses a Ring architecture. In this architecture, a cable break between two devices does not prevent communication to all upstream devices as in a normal non-Ring scheme. When the host detects a broken communication, the device allows the host to switch the communication direction to communicate with devices on both sides of the break. This allows for safe operation until the break in the lines is repaired.

The *CONTROL1\[DIR\_SEL\]* controls the communication direction. The devices will reconfigure the COMH and COML ports depending on the *\[DIR\_SEL\]* and the *\[TOP\_STACK\]* settings. Auto-addressing procedure is needed to re-address the device address for the reverse communication direction.

Example to change the communication direction to *\[DIR\_SEL\]* = 1 to the entire daisy chain: 1. Host sends Single Device Write to change the base device *\[DIR\_SEL\]* = 1. The base device will disable its COMH and enable its COML.

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

# 2.

Host sends Broadcast Write Reverse Direction to clear the *COMM\_CTRL* register settings on all devices. 3. Host sends Broadcast Write Reverse Direction to change the rest of the devices' *\[DIR\_SEL\]* = 1. In this step, the entire daisy chain set up to transmitting communication in the *\[DIR\_SEL\]* = 1 direction (that is, each device set up to transmit command frames sent by host from its COMH to its COML). 4. Host performs auto-addressing procedure to set up device address in the *DIR1\_ADDR* register. Unless the devices have been reset, host can skip the dummy read/write steps to synchronize the DLL in the auto-addressing procedure. 5. Host sets up the new Top of Stack device and the new ToS device will disable its COML transmitter.

# MCU TX

# RX

# S1

# COML

# COMH

# S2

# COML

# COMH

# B0 RX

# TX

# COMH

# COML

# S3

# COML

# COMH RX   TX

# UART

# \[DIR\_SEL\] = 1

# \[DIR\_SEL\] = 0

# \[DIR\_SEL\] = 0

# \[DIR\_SEL\] = 0

# \[DIR0\_ADDR\] = 0

# \[DIR0\_ADDR\] = 1

# \[DIR0\_ADDR\] = 2

# \[DIR0\_ADDR\] = 3

**Host: ** Sing device write to change [DIR_SEL] = 1 ***Ring***

# MCU TX

# RX

# S1

# COML

# COMH

# S2

# COML

# COMH

# B0 RX

# TX

# COMH

# COML

# S3

# COML

# COMH RX   TX

# UART

# \[DIR\_SEL\] = 1

# \[DIR\_SEL\] = 1

# \[DIR\_SEL\] = 1

# \[DIR\_SEL\] = 1

# \[DIR0\_ADDR\] = 0

# \[DIR0\_ADDR\] = 1

# \[DIR0\_ADDR\] = 2

# \[DIR0\_ADDR\] = 3

**Host: ** Broadcast write reverse direction to change the rest of the devices \[DIR\_SEL\] = 1 ***Ring***

**(a) Change the communication direction on the base device** **(b) Clear Top of Stack and change the communication ** **direction to the stack devices**

# S1

# COMH RX   TX

# COMH

# S2

# COML

# COMH

# B0 RX

# TX

# COMH

# COML

# S3

# COML

# COMH RX   TX

# \[DIR\_SEL\] = 1

# \[DIR\_SEL\] = 1

# \[DIR\_SEL\] = 1

# \[DIR\_SEL\] = 1

# \[DIR0\_ADDR\] = 0

# \[DIR0\_ADDR\] = 1

# \[DIR0\_ADDR\] = 2

# \[DIR0\_ADDR\] = 3

# \[DIR1\_ADDR\] = 0

# \[DIR1\_ADDR\] = 3

# \[DIR1\_ADDR\] = 2

# \[DIR1\_ADDR\] = 1

# \[TOP\_STACK\] = 1

**(c) re-address the device addresses for the reverse ** **communication direction, and set the new Top of Stack**

# \[TOP\_STACK\] = 0 [TOP_STACK] = 0 [TOP_STACK] = 1

# Figure 8-37. Example to Change Communication Direction in Daisy Chain

# Once the device address in both communication directions is set up, host can skip auto-address step when switching communication direction.

# In a broken cable case, host follows the same procedure to change the communication direction. To access

all devices in the daisy chain, host will have to communicate with *\[DIR\_SEL\]* = 0 on some devices and communicate with *\[DIR\_SEL\]* = 1 on other devices in the daisy chain. The chain will also have two ToS devices, one for each communication direction.

# www.ti.com

# BQ79616 SLUSF21 - JUNE 2023

# Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

# S1

# COMH RX   TX

# COMH

# S2

# COML

# COMH

# B0 RX

# TX

# COMH

# COML

# S3

# COML

# COMH RX   TX

# \[DIR\_SEL\] = 0

# \[DIR\_SEL\] = 0

# \[DIR0\_ADDR\] = 0

# \[DIR0\_ADDR\] = 1

# \[TOP\_STACK\] = 1

# S1

# COMH RX   TX

# COMH

# S2

# COML

# COMH

# B0 RX

# TX

# COMH

# COML

# S3

# COML

# COMH RX   TX

# \[DIR\_SEL\] = 1

# \[DIR\_SEL\] = 1

# \[DIR\_SEL\] = 1

# \[DIR1\_ADDR\] = 0

# \[DIR1\_ADDR\] = 2

# \[DIR1\_ADDR\] = 1

# \[TOP\_STACK\] = 1

# \[TOP\_STACK\] = 1

**(a) Use \[DIR\_SEL\] = 0 direction to communicate to S1** **(a) Use \[DIR\_SEL\] = 1 direction to communicate to S3 and S2**

## Figure 8-38. Using Ring Architecture to Access All Devices in a Broken Cable Case

## 8.3.6.1.4 Communication Timeout

## There are two programmable communication timeout thresholds, CTS timer and CTL timer, that monitor the

absence of a valid frame from either UART or daisy chain communication. A valid frame is defined as any frame (response or command) that does NOT contain any errors that prevent the frame from being processed. The communication timeouts are only actively counting while in ACTIVE mode. The counters are disabled and reset during SHUTDOWN mode. In SLEEP mode, the last counter values are held frozen.

## 8.3.6.1.4.1 Short Communication Timeout

## The short communication timeout acts like an alert to the host when triggered. The timeout period is

programmable through the *COMM\_TIMEOUT\_CONF\[CTS\_TIME2:0\]* bits. If enabled, the timer is reset every time a valid response or command frame is received. If the timer expires, the *FAULT\_SYS\[CTS\]* bit is set.

## 8.3.6.1.4.2 Long Communication Timeout

## The long communication timeout allows the host to put the device in SLEEP or SHUTDOWN mode for power

saving. The timeout period is programmable through *COMM\_TIMEOUT\_CONF\[CTL\_TIME2:0\]* bits. If enabled, the timer is reset every time a valid response or command frame is received. If the timer expires, host can choose one of the following actions through *COMM\_TIMEOUT\_CONF\[CTL\_ACT\]* bit.

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

- • Set *FAULT\_SYS\[CTL\]* = 1 and enter SLEEP mode. - • Enter SHUTDOWN mode. **8.3.6.1.5 Communication Debug Mode**

The device provides a communication debug mode to ease the initial development phase. To enter this debug mode, host writes an unlock code 0xA5 to register *DEBUG\_CTRL\_UNLOCK*. Once the debug mode is unlocked, the settings in *DEBUG\_COMM\_CTRL1* and *DEBUG\_COMM\_CTRL2* become effective.

To exit the debug mode simply write any value but 0xA5 (for example, writing 0x00) to the *DEBUG\_CTRL\_UNLOCK*. The COMH, COML, and UART will return to their normal operation status regardless of the settings in the *DEBUG\_COMM\_CTRL1* and *DEBUG\_COMM\_CTRL2* registers.

Once the communication debug mode is entered, the host gains control of the following:

**Table 8-20. Communication Debug Mode Functions**

**Control Function** **Enable Bit** **Description** Full COMH/L transmitter and receiver control

*\[USER\_DAISY\_EN\]* If *\[USER\_DAISY\_EN\]* = 1, device will enable or disable its COMH/L transmitter and receiver based on the *DEBUG\_COMM\_CTRL2* register setting. If *\[USER\_DAISY\_EN\]* = 0, COMH/L will be in its normal operation status even under communication debug mode. Mirror out the data in daisy chain onto UART

*\[USER\_UART\_EN\]* If *\[USER\_UART\_EN\]* = 1, host can set *\[UART\_MIRROR\_EN\]* = 1 to instruct the device to translate the daisy chain onto the UART, allowing host to read the data being received or forwarded in the daisy chain from the UART interface. Data will be presented in UART communication frame format. For stack devices, the UART TX is disabled by default. To use this feature, host also sets [UART_TX_EN] = 1. If *\[USER\_UART\_EN\]* = 0, any UART related debug functions are disabled. The UART will be in its normal operation status regardless of the *\[UART\_MIRROR\_EN\] * and *\[UART\_TX\_EN\]* settings. Slow down UART baud rate to 250 kbps

*\[USER\_UART\_EN\]* If *\[USER\_UART\_EN\]* = 1, host can set *\[UART\_BAUD\]* = 1 to change the UART baud rate to 250 kbps. This will result in slow throughput rate on the daisy chain. If *\[USER\_UART\_EN\]* = 0, UART baud rate will stay on 1 Mbps regardless of the *\[UART\_BAUD\]* setting.

The *DEBUG\_COMM\_STAT* register has status bits indicating if UART and COMH/L are under user or hardware (device) control. The register also indicates the status of the COMH/L transmitter and receiver. This debug status register is updated per device status and is readable with or without the communication debug mode enabled.

In fact, the read-only debug registers are all readable in ACTIVE mode without communication debug mode enabled. Most of them are lower level communication fault status registers to provide extra information in a communication failure event like the *DEBUG\_UART\**, *DEBUG\_COMH\**, and *DEBUG\_COML\** registers. See Section 8.3.6.2 and Section 8.5.4 for more details. **8.3.6.1.6 Multidrop Configuration**

A multidrop configuration is a configuration of multiple devices in a system communicating through UART to the host system. There is no daisy chain communication between devices. When *\[MULTIDROP\]* = 1, the device COMH and COML ports are disabled. All the communication protocols, single device read/write, broadcast read/write, stack read/write, and a reverse broadcast write are still supported as in daisy chain configuration (that is, *\[MULTIDROP\]* = 0). However, in a multidrop configuration, it is unlikely to have a use of the stack and reverse broadcast commands. If broadcast command is used, it is still required to set up the devices with sequential device address and set the *\[TOP\_STACK\]* bit on the device with highest device address. The device with *\[TOP\_STACK\]* = 1 initiates the data return when a broadcast read command is received, and the device with one lower device address will respond next, as in a daisy chain communication. Additionally, a COMM\_CLR must be used before every frame to ensure consistent communication in multidrop configuration. **8.3.6.1.7 SPI Controller**

The GPIO4 thru GPIO7 are configurable as a SPI controller interface when *GPIO\_CONF1\[SPI\_EN\]* = 1. The SPI controller includes four I/Os: - • SCLK: SPI clock, generated by the device and is used for synchronization **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## • • MOSI: Controller data output, driven by the device to output data to target

- • MISO: Controller data input, detecting data from target - • SS: target select, driven by the device during SPI communication.

# MCU TX

# RX Device (S1)

# COML

# COMH Device (S2)

# COML

# COMH Device (Base, B0) RX

# TX

# COMH

# COML Device (ToS, S3)

# COML

# COMH

| SPI based | EEPROM |
|:--- |:--- |
| GPIO7 | GPIO6 |
| GPIO5 | GPIO4 |

# GPIO7 GPIO6

# GPIO5 GPIO4

# CLK SDI SDO

# CS

| SPI based | EEPROM |
|:--- |:--- |
| SPI based | EEPROM |
| SPI based | EEPROM | SPI based EEPROM SPI based EEPROM

Host talks to the device SPI control registers to perform read/write operation to an external SPI based slave device

| Device read/write to the external SPI based slave via | GPIO4...7 based on MCU's operation instruction |
|:--- |:--- |
| GPIO7 | GPIO6 |
| GPIO5 | GPIO4 |

# GPIO7 GPIO6

# GPIO5 GPIO4

# CLK SDI SDO

# CS

# GPIO7 GPIO6

# GPIO5 GPIO4

# CLK SDI SDO

# CS

# GPIO7 GPIO6

# GPIO5 GPIO4

# CLK SDI SDO

# CS

## Figure 8-39. SPI Controller Stack Configuration

## The SPI\_CONF\[CPOL\] (clock polarity) and \[CPHA\] (clock phase) define the SPI clock format. The \[CPOL\]

is defined if the SPI clock is inverted or non-inverted. The *\[CPHA\]* is defined if the MISO and MOSI are sampled on the leading (first) clock edge or on the trailing (second) clock edge, regardless of whether that clock edge is rising or falling. The *SPI\_CONF\[NUMBIT4:0\]* defines how many bits the transaction is (1-bit to 24-bit transaction).

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

# IDLE IDLE

# SCLK

# SS

# MOSI

# MISO Data Clocked

# IDLE IDLE

# CPOL = 0 CPHA = 0

# IDLE IDLE

# SCLK

# SS

# MOSI

# MISO Data Clocked

# IDLE IDLE

# IDLE IDLE

# SCLK

# SS

# MOSI

# MISO Data Clocked

# IDLE IDLE IDLE IDLE

# SCLK

# SS

# MOSI

# MISO Data Clocked

# IDLE IDLE

# CPOL = 0 CPHA = 1

# CPOL = 1 CPHA = 0 CPOL = 1 CPHA = 1 **Legend** Data on MISO and MOSI is sampled at this time Data on MISO and MOSI is change at this time

# Figure 8-40. SPI Controller CPOL and CPHA

# IDLE

# IDLE

# IDLE

# SCLK $$ (CPOL=0) $$

# SS

# MOSI

# MISO

# HIGH:tLOW MSB in DATA in

# HD,MISO SU,MISO LSB in IDLE MSB out DATA out LSB out

# VALID,MOSI VALID,MOSI MOSI,DIS

# SS,LOW Command SS Low Command SS High

# SS,HI

# CPHA=0

# SCLK

# HIGH:tLOW

# SCLK

# SCLK $$ (CPOL=1) $$

# IDLE

# IDLE

# IDLE

# SCLK $$ (CPOL=0) $$

# SS

# MOSI

# MISO

# HIGH:tLOW MSB in DATA in

# HD,MISO SU,MISO LSB in IDLE MSB out DATA out LSB out

# VALID,MOSI MOSI,DIS

# SS,LOW Command SS Low Command SS High

# SS,HI

# CPHA=1

# SCLK

# HIGH:tLOW

# SCLK

# SCLK $$ (CPOL=1) $$

# Figure 8-41. SPI Controller Timing Diagram

# www.ti.com

# BQ79616 SLUSF21 - JUNE 2023

# Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## Table 8-21. Write to External SPI Target **Step** **Description**

Configure the SPI clock polarity, clock phase, number of bit transactions: - Write to *SPI\_CONF* register to configure SPI communication

Write the data (from 1 to 24 bits, specified in the *SPI\_CONF\[NUMBIT4:0\]* setting): - Set up the data to send to SPI target to the *SPI\_TX1* to *SPI\_TX3* registers - *SPI\_TX1* is the LSByte and *SPI\_TX3* is MSByte

Select the target (assuming active low) and execute the SPI write action: - Send SPI_EXE register = 0x01 (that is, [SS_CTRL] = 0 and [SPI_GO] = 1) Wait for the SPI communication to complete

Deselect the SS port (assuming active low, so deselecting means pull the SS pin high): - Send SPI_EXE register = 0x02 (that is, [SS_CTRL] = 1 and [SPI_GO] = 0)

## Table 8-22. Read from External SPI Target **Step** **Description**

Configure the SPI clock polarity, clock phase, number of bit transactions: - Write to *SPI\_CONF* register to configure SPI communication

Select the target and execute the SPI communication: - Send SPI_EXE register = 0x01 (that is, [SS_CTRL] = 0 and [SPI_GO] = 1) Wait for the data transaction to complete

Read the data (from 1 to 24 bits, specified in the *SPI\_CONF\[NUMBIT4:0\]* setting): - Read data from SPI target from the *SPI\_RX1* to *SPI\_RX3* registers - *SPI\_TX1* is the LSByte and *SPI\_TX3* is MSByte

Deselect the SS port (assuming active low, so deselecting means pull the SS pin high): - Send SPI_EXE register = 0x02 (that is, [SS_CTRL] = 1 and [SPI_GO] = 0) **8.3.6.1.8 SPI Loopback**

## The SPI controller has a loopback function that is enabled using the DIAG\_COMM\_CTRL\[SPI\_LOOPBACK\] bit.

When enabled, the byte in the *SPI\_TX\** registers are clocked directly to the MISO pin of the SPI controller to verify the SPI controller functionality. This is performed internally, so no external connection is needed to run this test. This verifies that the SPI function is working correctly. The *SPI\_CFG*, *SPI\_TX\**, and *SPI\_EXE* registers are written as a normal SPI transaction, but the external pins do not toggle during this mode. That is, the external pins stay static in their last state and do not change state during the loopback operation.

## The expected result of the test is that the byte in the SPI\_TX\* register is read into the SPI\_RX\* register. The

SS pin is latched to the setting in *SPI\_EXE\[SS\_CTRL\]* that existed when the LOOPBACK mode was enabled. The CPHA and CPOL parameters must be set before entering LOOPBACK mode to ensure proper operation. Changing the CPOL or CPHA parameters while in LOOPBACK mode may result in errant pulses on the SPI outputs and is not recommended.

## 8.3.6.2 Fault Handling **8.3.6.2.1 Fault Status Hierarchy**

## The device monitors multiple types of faults such as

- • Battery cell monitoring through the hardware protector, like cell OV/UV, cell OT/UT, and so on - • System operation driven like device reset, communication timeout, thermal warning, and so on - • Command-based diagnostic check related like the various comparison through the main and AUX ADCs,  BIST run, and so on - • Automatic diagnostic check running in the background like the internal power supplies, OTP CRC, and so on - • Communication fault.

## Each bit in the FAULT\_SUMMARY register represents a group of faults which are stored in one or more

lower level fault registers. The *FAULT\_SUMMARY* register represents the highest hierarchy level of fault status detected by the device. Host system can periodically poll the *FAULT\_SUMMARY* register to check the fault status and only read the lower level fault registers if needed (for example, if *FAULT\_SUMMARY\[FAULT\_OVUV\] * = 1, host can read *FAULT\_OV1/2* and *FAULT\_UV1/2* registers to determine which cell channel triggered the fault).

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## Table 8-23 shows which lower level register corresponds to the FAULT\_SUMMARY register bit. The description

of the register is covered in the Section 8.5.

## Table 8-23. Low-Level Fault Registers

# FAULT\_SUMMA

**RY Bit Name** **FAULT\_PROT** **FAULT\_COMP\_ADC** **FAULT\_OTP** **FAULT\_COMM** **FAULT\_OTUT** **FAULT\_OVUV** **FAULT\_SYS** **FAULT\_PWR** **Lower level ** **register name**

# FAULT\_PROT

# FAULT\_COMP\_GPIO *FAULT\_OTP* (1) *FAULT\_ COMM1 * (1)

# FAULT\_OT *FAULT\_OV1* *FAULT\_SYS* *FAULT\_PWR1*

# FAULT\_PROT

# FAULT\_COMP\_VCCB1 *FAULT\_ COMM2 * (1)

# FAULT\_UT *FAULT\_OV2* *FAULT\_PWR2*

# FAULT\_COMP\_VCCB2 *FAULT\_ COMM3* *FAULT\_UV1* *FAULT\_PWR3*

# FAULT\_COMP\_VCOW1 *FAULT\_UV2*

# FAULT\_COMP\_VCOW2

# FAULT\_COMP\_CBOW1

# FAULT\_COMP\_CBOW2

# FAULT\_COMP\_CBFET1

# FAULT\_COMP\_CBFET2

# FAULT\_COMP\_MISC

(1) Some of the bits in the *FAULT\_COMM1/2* and *FAULT\_OTP* registers have a lower level of fault information than shown in the *DEBUG\_COMM\** and *DEBUG\_OTP* registers. ***8.3.6.2.1.1 Debug Registers***

## The DEBUG\_COMM\* and DEBUG\_OTP registers are a form of fault status showing lower hierarchy level of fault

information for some of the bits in *FAULT\_COMM1*, *FAULT\_COMM2*, and *FAULT\_OTP*.

## Table 8-24 shows the hierarchy relationship. See Section 8.5 for the register description details.

## Table 8-24. Debug Registers

**Low-level Fault Register** **Low-level Register Bit** **Associated DEBUG Registers**

# FAULT\_COMM1

*\[UART\_RC\]* Fault related to received command frame from UART *DEBUG\_UART\_RC*

# \[UART\_RR\] *\[UART\_TR\]*

Fault related to received or transmitted response frame from UART

# DEBUG\_UART\_RR\_TR

# FAULT\_COMM2

*\[COMH\_BIT\]* Fault related to error in a byte from COMH *DEBUG\_COMH\_BIT*

*\[COMH\_RC\]* Fault related to received command frame from COMH *DEBUG\_COMH\_RC*

# \[COMH\_RR\] *\[COMH\_TR\]*

Fault related to received or transmitted response frame from COMH

# DEBUG\_COMH\_RR\_TR

*\[COML\_BIT\]* Fault related to error in a byte from COML *DEBUG\_COML\_BIT*

*\[COML\_RC\]* Fault related to received command frame from COML *DEBUG\_COML\_RC*

# \[COML\_RR\] *\[COML\_TR\]*

Fault related to received or transmitted response frame from COML

# DEBUG\_COML\_RR\_TR

# FAULT\_OTP

*\[SEC\_DET\]* Single error correction in OTP *DEBUG\_OTP\_SEC\_BLK*

*\[DED\_DET\]* Double error correction in OTP *DEBUG\_OTP\_DED\_BLK* **8.3.6.2.2 Fault Masking and Reset** ***8.3.6.2.2.1 Fault Masking***

## When a device detects a fault, the corresponding low-level register bit, including the one in the related bit

in the *DEBUG\_\** registers is set. Based on the fault hierarchy relationship, the fault will be reflected in the *FAULT\_SUMMARY* register.

## A group of faults can be masked, which the related low-level register flag will still be set, but the fault will not be

reflected to the corresponding *FAULT\_SUMMARY* register. The faults can be masked through the *FAULT\_MSK1 * and *FAULT\_MSK2* registers.

## For example, to mask the FAULT\_SUMMARY\[FAULT\_OTUT\] being set, host sets FAULT\_MSK1\[MSK\_OT\] = 1 and [MSK_UT] = 1.

## When fault is masked, it will also prevent the device from asserting the NFAULT pin when the masked fault

occurs. See Section 8.3.6.2.3 for details on NFAULT signal. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## Table 8-25. Fault Masking

**Masking Bit Name** **Related Low-level Register(s) Affected** **FAULT\_SUMMARY Register Bit That ** **Will Be Masked**

# FAULT\_MSK1

# \[MSK\_PROT\] *FAULT\_PROT\** *\[FAULT\_PROT\]*

# \[MSK\_UT\] *FAULT\_UT*

# \[FAULT\_OTUT\] *\[MSK\_OT\]* *FAULT\_OT*

# \[MSK\_UV\] *FAULT\_UV\**

| \[FAULT\_OVUV\] | \[MSK\_OV\] | FAULT\_OV\* |
|:--- |:--- |:--- |
| \[MSK\_COMP\] | FAULT\_COMP\_\* | \[FAULT\_COMP\] |
| \[MSK\_SYS\] | FAULT\_SYS | \[FAULT\_SYS\] |
| \[MSK\_PWR\] | FAULT\_PWR\* | \[FAULT\_PWR\] |

# \[MSK\_COMP\] *FAULT\_COMP\_\** *\[FAULT\_COMP\]*

# \[MSK\_SYS\] *FAULT\_SYS* *\[FAULT\_SYS\]*

# \[MSK\_PWR\] *FAULT\_PWR\** *\[FAULT\_PWR\]*

# FAULT\_MSK2

# \[MSK\_OTP\_CRC\] *FAULT\_OTP\[CUST\_CRC\]\[FACT\_CRC\]*

# \[FAULT\_OTP\]

*\[MSK\_OTP\_DATA\]* All non-CRC bits in *FAULT\_OTP*,

# DEBUG\_OTP\_\*

# \[MSK\_COMM3\_FCOMM\] *FAULT\_COMM3\[FCOMM\_DET\]*

# \[FAULT\_COMM3\]

*\[MSK\_COMM3\_FTONE\]* *FAULT\_COMM3\[FTONE\_DET\]*

# \[MSK\_COMM3\_HB\] *FAULT\_COMM3\[HB\_FAIL\]\[HB\_FAST\]*

# \[MSK\_COMM2\] *FAULT\_COMM2*, *DEBUG\_COMH\_\*, *

# DEBUG\_COML\_\* *\[FAULT\_COMM2\]*

# \[MSK\_COMM1\]

*FAULT\_COMM1*, *DEBUG\_UART\_\** *\[FAULT\_COMM1\]* ***8.3.6.2.2.2 Fault Reset***

## Once fault is detected, the fault status bit is latched until cleared using the reset bit. Similar to fault masking,

when the specific fault reset bit is set, the associated low-level fault registers, including the *DEBUG\_\** registers are cleared. The corresponding bit in the *FAULT\_SUMMARY* register will clear if all its associated low-level registers are cleared. If the fault condition persists and the reset bit is written, the fault status bit is not reset. The fault indicator cannot be reset until the underlying fault condition is eliminated.

## The fault is reset through the FAULT\_RST1 and FAULT\_RST2 registers; the fault reset bits are structured in the

same corresponding fault status registers as the fault masking bits. **8.3.6.2.3 Fault Signaling**

## Host can acquire the fault status with the following methods

- • Constantly polling the *FAULT\_SUMMARY* status on each device in the daisy chain. If *FAULT\_SUMMARY* is  non-zero, read the low-level fault status registers to obtain more information. - • Enable fault status to pass down the daisy chain to the base device. Enable base device's NFAULT pin to  be asserted when the *FAULT\_SUMMARY* is non-zero in any of the devices in the daisy chain. Host monitors NFAULT. When NFAULT is triggered, host does a broadcast read on the *FAULT\_SUMMARY* to determine which device(s) is at fault.

## When using the NFAULT pin in the base device to signal the host under a fault detection, the stack devices

have to transfer their fault status information to the base device. The information is transmitted through COMH/L through the same communication cables. In ACTIVE mode, each device embeds the fault status to the communication when a response frame is forwarded. In SLEEP mode, or using Heartbeat and Fault Tone in SLEEP mode.

## The NFAULT pin can be masked by configuring DEV\_CONF\[NFAULT\_EN\] = 0. When NFAULT is disabled, the

device will set the corresponding flag in *FAULT\_SUMMARY* register but will not assert NFAULT.

***8.3.6.2.3.1 Fault Status Transmitting in ACTIVE Mode***

## In ACTIVE mode, stack devices can embed their fault status before retransmitting a response frame if

*DEV\_CONF\[FCOMM\_EN\]* = 1. When the *\[FCOMM\_EN\]* = 1, the stack devices repurpose the SOF bit in the response frame's device address byte, register address bytes (both high and low address bytes) to a fault status bit instead. See Figure 8-42. This will be referred to as fault status bits in the rest of this section.

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated +1 Preamble

# SYNC \[1:0\] Start-Of-Frame

# SYNC = 2'b00

# INIT\[7:0\] +1 Preamble

# SYNC \[1:0\] Start-Of-Frame

# SYNC = 2'b00 Dev ADR\[7:0\] +1 Preamble

# SYNC \[1:0\] Start-Of-Frame

# SYNC = 2'b00

# REG ADR\[15:8\] +1 Preamble

# SYNC \[1:0\] Start-Of-Frame

# SYNC = 2'b00

# REG ADR\[7:0\]

| SOF | = 1 |
|:--- |:--- |
| SOF | = 0 |
| SOF | = 0 |
| SOF | = 0 |

**(a) Response frame if ** ***\[FCOMM\_EN\]*** ** = 0** +1 Preamble

# SYNC \[1:0\]

# SYNC = 2'b00

# INIT\[7:0\] +1 Preamble

# SYNC \[1:0\] Fault Status

# SYNC = 2'b00 Dev ADR\[7:0\] +1 Preamble

# SYNC \[1:0\] Fault Status

# SYNC = 2'b00

# REG ADR\[15:8\] +1 Preamble

# SYNC \[1:0\] Fault Status

# SYNC = 2'b00

# REG ADR\[7:0\]

# SOF = 1

**(b) Response frame if ** ***\[FCOMM\_EN\]*** ** = 1**

Fault Status = 0: no fault Fault Status = 1: fault Fault Status = 0: no fault Fault Status = 1: fault Fault Status = 0: no fault Fault Status = 1: fault Start-Of-Frame

# Figure 8-42. Embed Fault Status in Communication Response Frame

# To pass on the fault status of the stack devices, the host sends a broadcast read or sends a single device read

to the ToS device. Both types of reads will result in response frames passing through every device in the daisy chain, giving each device an opportunity to OR their fault status to the fault status bits in the response frame.

# An example of a response frame going through a daisy chain from a single device read command to the top device is shown in Figure 8-43.

## www.ti.com

# BQ79616 SLUSF21 - JUNE 2023

## Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

# MCU TX

# RX

# S1

# COML

# COMH

# S2

# COML

# COMH

# B0 RX

# TX

# COMH

# COML

# S3

# COML

# COMH RX   TX

# \[DIR\_SEL\] = 0

# \[DIR\_SEL\] = 0

# \[DIR\_SEL\] = 0

# \[DIR\_SEL\] = 0

# NFAULT INT ***AT Fault***

| (1) S3 is NOT at fault, returns its | response frame (fault status bit is | 0b000) & transmits to S2 |
|:--- |:--- |:--- |
| (2) S2 is at fault, VRLW³25´0b111 to | the Fault Status bits of the response | frame and transmits to S1 |
| (3) S1 is not at fault, VRLW³25´0b000 to the Fault | Status bits (resulting with 0b111) of the response frame | and transmits to B0 |

**(2) S2 is at fault, ** **VR** **LW³25´** **0b111** ** to ** **the Fault Status bits of the response ** **frame and transmits to S1**

**(3) S1 is not at fault, ** **VR** **LW³25´** **0b000 to the Fault ** **Status bits (resulting with ** **0b111** **) of the response frame ** **and transmits to B0**

**S1 will set ** ***FAULT\_COMM3\[FCOMM\_DET\]*** ** = 1 indicating ** **a device in the stack is at fault**

**(4) B0 detects the response frame has fault status bits set to ** **0b111** **, it assert NFAULT to host. It will also set  ** FAULT_COMM3[FCOMM_DET] = 1

# S1

# COML

# COMH

# S2

# COML

# COMH

# B0 RX

# TX

# COMH

# COML

# S3

# COML

# COMH RX   TX

# \[DIR\_SEL\] = 0

# \[DIR\_SEL\] = 0

# \[DIR\_SEL\] = 0

# \[DIR\_SEL\] = 0

# NFAULT ***AT Fault*** ***AT Fault*** ***AT Fault***

**(5) If FAULT\_COMM3\[FCOMM\_DET\] is not ** **masked, S1 and B0 will also in fault state after** **transmitting the response frame**

# Figure 8-43. Transfer Fault Status in ACTIVE Mode (Respond to a Single Device Read)

# When a device has no fault, it will OR the fault status bits with 0b000; otherwise, it will OR the fault status bits

with 0b111. Hence, if a fault exists in any device in the daisy chain, the fault status bits will be 0b111. For the base device to assert the NFAULT pin, it requires at least two bits of the fault status bits to be 1.

# Additionally, when a device detects a response frame with at least two of the fault status bits being 1, the device

will also set the *FAULT\_COMM3\[FCOMM\_DET\]* = 1. If this fault is not masked, the device will be in fault state as well. Next time a response frame is transmitted, this device will OR the fault status bits with 0b111.

# Host performs a broadcast read to detect which device in the daisy chain is at fault and what type of fault.

## 8.3.6.2.3.2 Fault Status Transmitting in SLEEP Mode

# In SLEEP mode, the following fault detections are still active

- • Customer and Factory OTP shadow registers CRC check - • Device thermal warning - • Power supplies OV, UV, and oscillation detection - • If OVUV protectors are enabled, cell OV and UV detection. - • If OTUT protectors are enabled, thermistors OT and UT detection.

# Because communication is not available in SLEEP mode, the device provides an option to transmit the

fault status through Heartbeat (device in no fault state) and Fault (device in fault state) Tones. These tones are transmitted in the same direction as a communication command frame, which is based on the *CONTROL1\[DIR\_SEL\]* setting. For the tone signal to return back to the base device (so NFAULT can be triggered if needed), a Ring architecture must be used to support transmitting fault status in SLEEP mode.

## BQ79616 SLUSF21 - JUNE 2023 **<https://www.ti.com**>

## Submit Document Feedback

Copyright © 2023 Texas Instruments Incorporated B0 (base)

# S1

# S2

# S3 (ToS)

# \[DIR\_SEL\] = 0

# \[DIR\_SEL\] = 0

# \[DIR\_SEL\] = 0

# \[DIR\_SEL\] = 0

# MCU

# I/O NFAULT

**(a) Traveling direction with \[DIR\_SEL\] = 0**

| NFAULT is asserted if B0 | receives Fault Tone |
|:--- |:--- |
| B0 | (base) |
| S1 | (ToS) | B0 (base)

# S1 (ToS)

# S2

# S3

# \[DIR\_SEL\] = 1

# \[DIR\_SEL\] = 1

# \[DIR\_SEL\] = 1

# \[DIR\_SEL\] = 1

# MCU

# I/O NFAULT

**(b) Traveling direction with \[DIR\_SEL\] = 1**

**NFAULT is asserted if B0 ** **receives Fault Tone**

## Figure 8-44. Heartbeat or Fault Tone Traveling Direction

## Both the Heartbeat and Fault Tones are a type of tone similar to the communication tone. One main difference is

a communication tone only transmits with a single burst of couplets, but Heartbeat and Fault Tones are sent with a burst of couplets periodically. See Section 8.3.6.2.3.3 for details.

## 8.3.6.2.3.3 Heartbeat and Fault Tone

## The tones are enabled by setting DEV\_CONF\[HB\_EN\] = 1 and DEV\_CONF\[FTONE\_EN\] = 1 to enable the

Heartbeat and Fault Tone transmitters, respectively. The Heartbeat and Fault Tone receivers are always on in SLEEP mode regardless of the *\[HB\_EN\]* and *\[FTONE\_EN\]* settings. To avoid fault detection (asserting NFAULT or *FAULT\_SUMMARY* register) by a Heartbeat or Fault Tone fault, mask the fault by *\[MSK\_COMM3\_HB\]* = 1 or [MSK_COMM3_FTONE] = 1.

## The Heartbeat and Fault Tone are formed with couplets with "-" polarity. They are differentiated by the number

of couplets. Unlike communication tones, Heartbeat and Fault Tone are transmitted periodically. The period between tones is a burst period. The number of couplets transmitted is always greater than the number of couplets needed for detection. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* **Heartbeat or Fault Tone Detection**

**Heartbeat, Fault Tone Couplets (** **DOO** **³** **-** **³** **SXOVHV** **)  **

# CVDD

# CVSS

# COMTONE

# FLTTONE\_LO

# FLTONE\_HI

# COM\*P \\pm COMP\*N

# COM\*P

# COM\*N

# CVDD/2 Couplets detection by receiving device Heartbeat or Fault Tone COM\*P,COM\*N Tone detection (internal signal) Heartbeat or Fault Tone Burst period **Figure 8-45. Heartbeat and Fault Tone** ***8.3.6.3 Nonvolatile Memory***

There are memory locations that are programmable in nonvolatile memory (NVM) using OTP (One Time Programmable). The memory space is divided in two groups, factory space and customer space. The factory space stores the device configurations that are essential for normal operation. This space is not accessible by the host. The customer space contains the device default setting that host system can customize for their application configuration. This space is readable and programmable by the host.

When a device reset occurs, factory and customer OTP values are reloaded to their shadow registers. Error check and correction (ECC), single error correction (SEC) and double error detection (DED), are performed during the factory and customer space OTP load. The corresponding *FAULT\_OTP\[SEC\_DET\]* or *FAULT\_OTP\[DED\_DET\]* will be set if an error is detected.

Any load errors of the factory OTP space signal a fault using the *FAULT\_OTP\[FACTLDERR\]*. Any load errors of the customer OTP space signal a fault using the *FAULT\_OTP\[CUSTLDERR\]*. Additionally, the OTP space (factory and customer) are protected from data integrity problems using CRC. The corresponding *FAULT\_OTP\[FACT\_CRC\]* and *\[CUST\_CRC\]* bits will be set if a CRC error is detected.

If any overvoltage error conditions exist in the OTP pages space (factory and customer) during programming, the *OTP\_FAULT\[GBLOVERR\]* bit is set. Information received from the device with this error must not be considered reliable. **8.3.6.3.1 OTP Page Status**

There are two unused pages of OTP memory available for the customer to program. Each page status is held in the *OTP\_CUST1\_STAT* and *OTP\_CUST2\_STAT* registers. The registers provide information on the current status of the page such as:

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## • • Load status (if loaded, loaded with error, loaded but failed)

- • Programmed successfully or available to be programmed - • Programmed status

## When a reset occurs, the device evaluates the OTP page status and chooses the latest and valid OTP page to

load. Page 2 has priority over Page 1. If both pages have not been written, the factory OTP default are loaded. Section 8.5.1 shows all customer programmable OTP parameters. The register summary also shows the default values when Customer OTP Page 1 and Page 2 are not programmed. - • A valid page is one where the *OTP\_CUST\*\_STAT\[PROGOK\]* = 1. - • When the page is selected for loading, the *OTP\_CUST\*\_STAT1\[LOADED\]* = 1. - • If a single error occurs in the loading of the page, the page is loaded after the single error is corrected and the  OTP_CUST*_STAT1[LOADWRN] = 1. - - Additionally, the *DEBUG\_OTP\_SEC\_BLK* register is updated with the location of the error corrected block. - • If a double error occurs, the loading of that block is terminated and the hardware defaults of that block are  loaded (as indicated in Section 8.5.1 ). - - The overall page loading process is not terminated for a DED, only the affected block is terminated. - - When a DED occurs, the *OTP\_CUST\*\_STAT1\[LOADERR\]* = 1. Additionally, the *DEBUG\_OTP\_DED\_BLK * register is updated with the block where the double error occurred. **8.3.6.3.2 OTP Programming**

## Section 8.5.1 shows all parameters that can be programmed to the customer OTP page. There are two pages of OTP memory available for customer to use.

## Before programming the OTP, host ensures

- • All OTP shadow registers have the correct settings - • A customer OTP page is valid to be programmed. A valid page is one with *OTP\_CUST\*\_STAT1\[TRY\]* = 0 and  OTP_CUST*_STAT1[FMTERR] = 0.

## Table 8-26. Program the OTP **Step** **Procedure**

Unlock the OTP programming: - Write the following data to *OTP\_PROG\_UNLOCK1A* to *OTP\_PROG\_UNLOCK1D* registers.

# • • OTP\_PROG\_UNLOCK1A ≤ data 0x02

- *• OTP\_PROG\_UNLOCK1B* ≤ data 0xB7 - *• OTP\_PROG\_UNLOCK1C* ≤ data 0x78 - *• OTP\_PROG\_UNLOCK1D* ≤ data 0xBC

- Do another write with the following data to *OTP\_PROG\_UNLOCK2A* to *OTP\_PROG\_UNLOCK2D* registers.

# • • OTP\_PROG\_UNLOCK2A ≤ data 0x7E

- *• OTP\_PROG\_UNLOCK2B* ≤ data 0x12 - *• OTP\_PROG\_UNLOCK2C* ≤ data 0x08 - *• OTP\_PROG\_UNLOCK2D* ≤ data 0x6F

Each block of registers must be written in order (that is, A, B, C, then D) with no other writes or reads between. The best practice is to use the same Write command to update. Any attempt to update the registers out of sequence, or if another register is written or read between writes, the entire sequence must be redone.

Check to confirm the OTP unlock procedure is successful: - Read to confirm *OTP\_PROG\_STAT\[UNLOCK\]* = 1 Issuing a Read command after step 1 is ok, but issuing the *\[PROG\_GO\]* must be the next write command after the unlock procedures.

Select the proper OTP page and start the OTP programming: - To program page1, set *OTP\_PROG\_CTRL\[PAGESEL\]\[PROG\_GO\]* = 0x01, or - To program page2, set *OTP\_PROG\_CTRL\[PAGESEL\]\[PROG\_GO\]* = 0x03

Wait t PROG for the OTP programming to complete **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## Table 8-26. Program the OTP (continued) **Step** **Procedure**

Check to ensure there is no error during OTP programming. The following bits are expected to be 1 after a successful OTP programming: - *OTP\_PROG\_STAT\[DONE\]* = 1, OTP programming is done. No other bit will be set in this register. - If page 1 is programmed, *OTP\_CUST1\_STAT\[PROGOK\]*, *\[TRY\]*, *\[OVOK\]*, and *\[UVOK\]* bits are 1. Other bits are 0. - If page 2 is programmed, *OTP\_CUST2\_STAT\[LOADED\]*, *\[PROGOK\]*, *\[TRY\]*, *\[OVOK\]*, and *\[UVOK\]* bits are 1. Other bits  are 0.

Issue a digital reset to reload the registers with the updated OTP values: - CONTROL1[SOFT_RESET] = 1

## During programming, if a programming voltage OV or UV event occurs, the OTP\_CUST\*\_STAT\[UVOK\] or

*OTP\_CUST\_STAT2\[OVOK\]* bit is 0 to indicate the programming voltage under- or overvoltage condition is detected during the programing attempts. In addition, the *\[UVERR\]*, *\[OVERR\]*, *\[SUVERR\]*, and *\[SOVERR\]* bits in the *OTP\_PROG\_STAT* register indicate if there is programming voltage error during programming and stability test.

## Note

- • During the programming procedure, device performs a programming voltage stability test before  actually programming the OTP. If a programming voltage fails the stability test, the device will not set the *OTP\_CUST\*\_STAT\[TRY\]* bit, giving the customer another attempt to program the page again. - • If the host incorrectly selects a page for programming, the *OTP\_PROG\_STAT\[PROGERR\]* bit is  set. This indicates that the selected page was not available to be programmed. Select the correct page and retry the programming. - • Device will not start OTP programming above 55°C temperature. - • OTP programming time (from \[PROG\_GO\] = 1 to \[DONE\] =1) for LDOIN capacitor of 0.1 μF is 100  ms.

## 8.3.6.4 Diagnostic Control/Status

## The following subsections describe the diagnostic control and fault status that can be used as part of the safety mechanisms.

## The Safety Manual for BQ79616 and the BQ79606 FMEDA documents are available separately from Texas

Instruments. Contact TI Sales Associate or Applications Engineer for further information. **8.3.6.4.1 Power Supplies Check**

***8.3.6.4.1.1 Power Supply Diagnostic Check***

## The internal power supply circuits have overvoltage, undervoltage, oscillation detection, and/or current limit

checks. All these detections are continuously running in the background when the device is in ACTIVE or SLEEP mode. If a failure is detected, the corresponding flags in the *FAULT\_PWR\** registers will be set or in certain failure modes, the device will reset. Table 8-27 summarizes the diagnostics that apply for each power supply and the corresponding action when failure is detected.

## Table 8-27. Power Supply Diagnostic Checks

**Supply/ ** **Ground Pin** **OV Check** **UV Check** **OSC Check** **Current Limit** **Pin Open**

# LDOIN

AVDD If this fails, set *FAULT\_PWR1\[AVDD\_* *OV\]*

If this fails, disable DVDD and trigger a digital reset. After soft reset, device sets *\[AVDDUV\_DRST\] * to indicate a reset is caused by AVDD UV.

| If fails, set | FAULT\_PWR1\[AVDD\_ | OSC\] |
|:--- |:--- |:--- |
| Limit current to EC | table current limit | specification |
| BQ79616 | SLUSF21 - JUNE 2023 | www.ti.com |

Limit current to EC table current limit specification

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## Table 8-27. Power Supply Diagnostic Checks (continued)

**Supply/ ** **Ground Pin** **OV Check** **UV Check** **OSC Check** **Current Limit** **Pin Open**

DVDD If this fails, set *FAULT\_PWR1\[DVDD\_* *OV\]* If this fails, trigger a digital reset

Limit current to EC table current limit specification

CVDD If this fails, set *FAULT\_PWR1\[CVDD\_* *OV\]*

If this fails, set *FAULT\_PWR1\[CVDD\_* *UV\]*

Limit current to EC table current limit specification

TSREF If this fails, set *FAULT\_PWR2\[TSREF\_* *OV\]* and *FAULT\_OT * and *FAULT\_UT * registers to all 1s.

If this fails, set *FAULT\_PWR2\[TSREF\_* *UV\]* and *FAULT\_OT * and *FAULT\_UT * registers to all 1s.

If fails, set *FAULT\_PWR2\[TSREF\_* *OSC\]* and *FAULT\_OT * and *FAULT\_UT * registers to all 1s.

Limit current to EC table current limit specification

NEG5V If this fails, set *FAULT\_PWR2\[NEG5V\_* *UV\]*

# REFHP/REFHM

If REFHP fails, set *FAULT\_PWR2\[REFH\_* *OSC\]*

If REFHM opens, set the *FAULT\_PWR1 * *\[REFHM\_OPEN\]*

DVSS If this opens, set the *FAULT\_PWR1\[DVSS\_* *OPEN\]*

CVSS If this opens, set the *FAULT\_PWR1\[CVSS\_* *OPEN\]*

## Note

## Due to the detection logic implemented, when AVDD OV or UV is detected, the AVDD OSC fault can

also be triggered. Similarly, when TSREF OV or UV, the TSREF OSC fault can also be triggered. ***8.3.6.4.1.2 Power Supply BIST***

## The device implements a power supply BIST (Built-In Self-Test) function to test the primary power supply failure

diagnostic paths that cover the following detections: - *• FAULT\_PWR1\[AVDD\_OV\]*, *\[AVDD\_OSC\]*, *\[DVDD\_OV\]*, *\[CVDD\_OV\]*, *\[CVDD\_UV\]*, *\[REFHM\_OPEN\]*,  *\[DVSS\_OPEN\]*, and *\[CVSS\_OPEN\]* - *• FAULT\_PWR2\[TSREF\_OV\]*, *\[TSREF\_UV\]*, *\[TSREF\_OSC\]*, *\[NEG5V\_UV\]*, *\[REFHM\_OSC\]*, and  *\[PWRBIST\_FAIL\]*

## The power supply BIST is essentially a check on the checker and it is a command base function initiated by host.

## The power supply BIST, once started, will force a fault on failure detection path on each supply. Take AVDD OV

diagnostic path as an example, when the BIST engine tests the AVDD OV path, the following occur: 1. The BIST engine forces a fail to the AVDD OV comparator 2. The BIST engine then checks to ensure the signal to trigger *FAULT* register is asserted, and the signal to trigger NFAULT is also asserted 3. The BIST engine resets the *FAULT* register and NFAULT signal (that is, clears the *FAULT\_PWR1/2/3 * registers and deasserts NFAULT) 4. The BIST engine repeats step 1 to step 3 on the next power supply diagnostic path check (for example, AVDD OSC) until all intended diagnostic paths covered by BIST are tested. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

**Note** - • During the BIST run, the NFAULT pin will be toggled on and off. Host ignores the NFAULT pin  status or can disable the NFAULT pin output by setting *DEV\_CONF\[NFAULT\_EN\]* = 0. - • Among all internal power supplies, TSREF is one that can be enabled or disabled by host. To  ensure TSREF diagnostic paths are tested during BIST run, host enables TSREF before starting the power supply BIST. Otherwise, the BIST engine will ignore the TSREF diagnostic paths test result during the BIST run. - • Because other nonpower supply-related faults can also trigger NFAULT, it is recommended to  mask all nonpower supply-related faults through *FAULT\_MSK1/2* registers before the power supply BIST run. - • Host also ensures there are no power supply faults before starting the power supply BIST run.

Start power supply BIST by sending *DIAG\_PWR\_CTRL\[PWR\_BIST\_GO\]* = 1. The BIST run will not abort even if a failure is detected during the run. At the end of the BIST run, the result is indicated by the *FAULT\_PWR2\[PWRBIST\_FAIL\]* flag.

The power supply BIST forces a failure and ensures the diagnostic path triggers the fault accordingly. A failure on the BIST run indicates a diagnostic path is unable to trigger in a fault condition. To further examine which path is unable to indicate a failure, host can set the *DIAG\_PWR\_CTRL\[BIST\_NO\_RST\]* = 1. This bit disables the reset step during the BIST run. Re-start power supply BIST with this option enabled. At the end of the BIST run, examine the *FAULT\_PWR1* and *FAULT\_PWR2* registers. Any register flag that remains 0 indicates it is unable to flag a failure. AVDD OV diagnostic path

# MUX

# AVDD

# REF

Force a reference voltage that will cause a fail AVDD output OV comparator **... **

# To NFAULT Reset Reset

| Control to select | reference voltage |
|:--- |:--- |
| FAULT\_PWR | registers |
| AVDD OV diagnostic | path |
| DVDD OV | CVDD OV | FAULT\_PWR registers **AVDD OV diagnostic ** **path **

# DVDD OV CVDD OV

# AVDD OV **... **

# GND

# OR GATE **Figure 8-46. Power Supply BIST**

**8.3.6.4.2 Thermal Shutdown and Warning Check** ***8.3.6.4.2.1 Thermal Shutdown***

Thermal shutdown occurs when the thermal shutdown sensor senses an overtemperature condition of the device. The sensor operates without interaction and is separated from the ADC measured die sensor. The

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

thermal shutdown function has a register-status indicator flag ( *FAULT\_SYS\[TSHUT\]* ) that is saved during the shutdown event and can be read after the device is awaken back up. When a TSHUT fault occurs, the part immediately enters the SHUTDOWN mode. Any pending transactions on UART or daisy chain are discarded. There is no fault signaling performed when a thermal shutdown event occurs as the device immediately shuts down.

To awaken the device, host ensures the ambient temperature is below T SHUT\_FALL and sends a WAKE ping to the base device. Host will not attempt to wake the device if the ambient temperature is still above T SHUT\_FALL.

Upon waking up, the *FAULT\_SYS\[TSHUT\]* bit is set. See Section 8.4.1.1 for more details. If the system faults are unmasked, *FAULT\_MSK1\[MSK\_SYS\]* = 0, the thermal shutdown will be reflected as a fault and will be indicated in the *FAULT\_SUMMARY* register and the assertion of the NFAULT pin. ***8.3.6.4.2.2 Thermal Warning***

To warn the host of an impending thermal overload the device includes an overtemperature warning that signals a fault when the die temperature approaches thermal shutdown. The device detects the die temperature through the TWARN sensor against the thermal warning threshold. There are four threshold options configured by the *PWR\_TRANSIT\_CONF\[TWARN\_THR1:0\]* setting.

When the system fault is unmasked, and the temperature warning fault occurs, the *FAULT\_SYS\[TWARN\]* = 1. The host can take action to avoid a thermal shutdown. **8.3.6.4.3 Oscillators Watchdog**

The oscillators are monitored by watchdog circuits. There are two oscillators in the device, the HFO and the LFO. If these oscillators are not functioning, the device does not operate. If the HFO or LFO does not transition within the expected time, the watchdog circuits cause a digital reset.

When this unexpected reset occurs, it is recommended that the host sends a SHUTDOWN ping/tone to the problem device and then send a WAKE ping to reset the daisy chain. If the oscillators are truly damaged, the device will not restart and must be replaced.

In addition to the watchdog, the LFO frequency is monitored to ensure it stays within acceptable limits. If the LFO frequency falls outside of the expected range, the *FAULT\_SYS\_FAULT\[LFO\]* bit is set. **8.3.6.4.4 OTP Error Check** ***8.3.6.4.4.1 OTP CRC Test and Faults*** CRC Test:

The factory registers and customer OTP shadow registers are covered by a CRC check that constantly runs in the background. The *CUST\_CRC\_RSLT\_HI* and *CUST\_CRC\_RSLT\_LO* registers hold the current device's computed CRC value. This value is compared against the customer programmed value in the CRC registers, *CUST\_CRC\_HI* and *CUST\_CRC\_LO*. When updating any customer OTP shadow register covered in the CRC, the host must update a new CRC value to *CUST\_CRC\_HI* and *CUST\_CRC\_LO* registers. The CRC calculation is performed in the same manner (including the bit stream ordering) and with the same polynomial as described in Section 8.3.6.1.1.2.1.6. The CRC check and comparison for factory and customer spaces is performed periodically and the *DEV\_STAT\[CUST CRC\_DONE\]* and *\[FACT\_CRC\_DONE\]* bits are set after the check is complete. If the bit is already set, it remains set until cleared with a read. CRC Faults:

When *CUST\_CRC\_HI/LO* and *CUST\_CRC\_RSLT\_HI/LO* do not match, the *FAULT\_OTP\[CUST\_CRC\]* flag is set until the condition is corrected. Continuous monitoring of the factory NVM space occurs in a similar fashion, concurrently with the monitoring of the customer space. When a factory register change is detected, the *FAULT\_OTP\[FACT\_CRC\]* flag is set. When this fault occurs, the host should reset the fault flag to see if the fault persists. If the fault persists, the host must perform a reset of the part. If reset does not correct the issue, the device is corrupted and must not be used. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* ***8.3.6.4.4.2 OTP Margin Read***

The device provides OTP margin read test modes, with which host can set up to reload the OTP with margin 1 or margin 0. To start the margin read test, host selects the desired test mode through *DIAG\_OTP\_CTRL\[MARGIN\_MODE2:0\]* and sets *DIAG\_OTP\_CTRL\[MARGIN\_GO\]* = 1. The device will reload the OTP per the *\[MARGIN\_MODE2:0\]* setting. Any OTP related error will be flagged to the *FAULT\_OTP* register.

***8.3.6.4.4.3 Error Check and Correct (ECC) OTP***

# ECC

Register values for selected registers (0x0000 to 0x002F) are permanently stored in OTP. All registers also exist as volatile storage locations at the same addresses, referred to as shadow registers. The volatile registers are for reading, writing, and device control. For a list of registers included in the OTP, see Section 8.5.1.

During wakeup, the device first loads all shadow registers with hardware default values listed in Section 8.5.1. Then the device loads the registers conditionally with OTP contents from the results of the Error Check and Correct (ECC) evaluation of the OTP. The OTP is loaded to shadow registers in 64-bit blocks; each block has its own Error Check and Correct (ECC) value stored. The ECC detects a single-bit (Single-Error-Correction) or double-bit (Double-Error-Detection) changes in OTP stored data. The ECC is calculated for each block, individually.

Single-bit errors are corrected, double-bit errors are only detected, not corrected. A block with good ECC is loaded. A block with a single-bit error is corrected, and the *FAULT\_OTP\[SEC\_DET\]* bit is set to flag the corrected error event. Additionally, the *DEBUG\_OTP\_SEC\_BLK* register is updated with the location of the error corrected block. This enables the host to keep track of potentially damaged memory. The block is loaded to shadow registers after the single-bit error correction. Because the evaluation is on a block-by-block basis, it is possible for multiple blocks to have a single-correctable error and still be loaded correctly. Multiple-bit errors can exist with full correction, as long as they are limited to a single error per block.

A block with a bad ECC comparison (two-bit errors in one block) is not loaded and the *FAULT\_OTP\[DED\_DET\] * bit is set to flag the failed bit-error event. Additionally, the *DEBUG\_OTP\_DED\_BLK* register is updated with the block where the double error occurred. The hardware default value remains in the register. This allows some blocks to be loaded correctly (no fail or single-bit corrected value) and some blocks not to load. When the *FAULT\_OTP\[SEC\_DET\]* or *FAULT\_OTP\[DED\_DET\]* bit is set and the condition is not cleared by a device reset, the device is corrupted and must not be used.

The ECC engine uses the industry standard 72,64 SEC DEC ECC implementation. The OTP is protected by a (72, 64) Hamming code, providing single error correction, double error detection (SECDED). For each 64 bits of data stored in OTP, an additional 8 bits of parity information are stored. The parity bits are designated p0, p1, p2, p4, p8, p16, p32, and p64. Bit p0 covers the entire encoded 72-bit ECC block. The remaining seven parity bits are assigned according to the following rule: - • Parity bit p1 covers odd bit positions, that is, bit positions which have the least significant bit of the bit position  equal to 1 (1, 3, 5, and so on), including the p1 bit itself (bit 1). - • Parity bit p2 covers bit positions which have the second least significant bit of the bit position equal to 1 (2, 3,  6, 7, 10, 11, and so on), including the p2 bit itself (bit 2). - • The pattern continues for p4, p8, p16, p32, and p64. Table 8-28 specifies the complete encoding.

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## Table 8-28. (72, 64) Parity Encoding **Bit Position**

**Encoded Bits** **d63** **d62** **d61** **d60** **d59** **d58** **d57** **p64** **d56** **d55** **d54** **d53** **d52** **d51** **d50** **d49** **d48** **d47** **Parity Bit ** **Coverage** **p0** x x x x x x x x x x x x x x x x x x **p1** x x x x x x x x x **p2** x x x x x x x x x x **p4** x x x x x x x x x x **p8** x x x x x x x x **p16** x x x x x x x x x x **p32** x x x x x x x x x x **p64** x x x x x x x x **Bit Position**

**Encoded Bits** **d46** **d45** **d44** **d43** **d42** **d41** **d40** **d39** **d38** **d37** **d36** **d35** **d34** **d33** **d32** **d31** **d30** **d29** **Parity Bit ** **Coverage** **p0** x x x x x x x x x x x x x x x x x x **p1** x x x x x x x x x **p2** x x x x x x x x **p4** x x x x x x x x x x **p8** x x x x x x x x **p16** x x x x x x **p32** x x x x x x x x x x x x x x x x x x **p64** **Bit Position**

**Encoded Bits** **d28** **d27** **d26** **p32** **d25** **d24** **d23** **d22** **d21** **d20** **d19** **d18** **d17** **d16** **d15** **d14** **d13** **d12** **Parity Bit ** **Coverage** **p0** x x x x x x x x x x x x x x x x x x **p1** x x x x x x x x x **p2** x x x x x x x x x x **p4** x x x x x x x x **p8** x x x x x x x x **p16** x x x x x x x x x x x x x x **p32** x x x x **p64** **Bit Position**

**Encoded Bits** **d11** **p16** **d10** **d9** **d8** **d7** **d6** **d5** **d4** **p8** **d36** **d2** **d1** **p4** **d0** **p2** **p1** **p0** **Parity Bit ** **Coverage** **p0** x x x x x x x x x x x x x x x x x x **p1** x x x x x x x x x **p2** x x x x x x x x **p4** x x x x x x x x **p8** x x x x x x x x **p16** x x **p32** **p64** **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## Table 8-29. Encoder and Decoder Data IN and OUT Positioning

# ENCODER

| DATA IN | Encoded Bits | DATA OUT | Bit Positions |
|:--- |:--- |:--- |:--- |
| OTP\_ECC\_DATAIN 1 | d0 to d7 | OTP\_ECC\_DATAOUT 1 | 0 to 7 |
| OTP\_ECC\_DATAIN 2 | d8 to d15 | OTP\_ECC\_ DATAOUT 2 | 8 to 15 |
| OTP\_ECC\_DATAIN 3 | d16 to d23 | OTP\_ECC\_ DATAOUT 3 | 16 to 23 |
| OTP\_ECC\_DATAIN 4 | d24 to d31 | OTP\_ECC\_ DATAOUT 4 | 24 to 31 |
| OTP\_ECC\_DATAIN 5 | d32 to d39 | OTP\_ECC\_ DATAOUT 5 | 32 to 39 |
| OTP\_ECC\_DATAIN 6 | d40 to d47 | OTP\_ECC\_ DATAOUT 6 | 40 to 47 |
| OTP\_ECC\_DATAIN 7 | d48 to d55 | OTP\_ECC\_ DATAOUT 7 | 48 to 55 |
| OTP\_ECC\_DATAIN 8 | d56 to d63 | OTP\_ECC\_ DATAOUT 8 | 56 to 63 |

# OTP\_ECC\_DATAIN 1 d0 to d7 OTP\_ECC\_DATAOUT 1 0 to 7

# OTP\_ECC\_DATAIN 2 d8 to d15 OTP\_ECC\_ DATAOUT 2 8 to 15

# OTP\_ECC\_DATAIN 3 d16 to d23 OTP\_ECC\_ DATAOUT 3 16 to 23

# OTP\_ECC\_DATAIN 4 d24 to d31 OTP\_ECC\_ DATAOUT 4 24 to 31

# OTP\_ECC\_DATAIN 5 d32 to d39 OTP\_ECC\_ DATAOUT 5 32 to 39

# OTP\_ECC\_DATAIN 6 d40 to d47 OTP\_ECC\_ DATAOUT 6 40 to 47

# OTP\_ECC\_DATAIN 7 d48 to d55 OTP\_ECC\_ DATAOUT 7 48 to 55

# OTP\_ECC\_DATAIN 8 d56 to d63 OTP\_ECC\_ DATAOUT 8 56 to 63

# OTP\_ECC\_ DATAOUT 9 64 to 71

# DECODER

| DATA IN | Bit Positions | DATA IN | Encoded Bits |
|:--- |:--- |:--- |:--- |
| OTP\_ECC\_DATAIN 1 | 0 to 7 | OTP\_ECC\_DATAOUT 1 | d0 to d7 |
| OTP\_ECC\_DATAIN 2 | 8 to 15 | OTP\_ECC\_ DATAOUT 2 | d8 to d15 |
| OTP\_ECC\_DATAIN 3 | 16 to 23 | OTP\_ECC\_ DATAOUT 3 | d16 to d23 |
| OTP\_ECC\_DATAIN 4 | 24 to 31 | OTP\_ECC\_ DATAOUT 4 | d24 to d31 |
| OTP\_ECC\_DATAIN 5 | 32 to 39 | OTP\_ECC\_ DATAOUT 5 | d32 to d39 |
| OTP\_ECC\_DATAIN 6 | 40 to 47 | OTP\_ECC\_ DATAOUT 6 | d40 to d47 |
| OTP\_ECC\_DATAIN 7 | 48 to 55 | OTP\_ECC\_ DATAOUT 7 | d48 to d55 |
| OTP\_ECC\_DATAIN 8 | 56 to 63 | OTP\_ECC\_ DATAOUT 8 | d56 to d63 |

# OTP\_ECC\_DATAIN 1 0 to 7 OTP\_ECC\_DATAOUT 1 d0 to d7

# OTP\_ECC\_DATAIN 2 8 to 15 OTP\_ECC\_ DATAOUT 2 d8 to d15

# OTP\_ECC\_DATAIN 3 16 to 23 OTP\_ECC\_ DATAOUT 3 d16 to d23

# OTP\_ECC\_DATAIN 4 24 to 31 OTP\_ECC\_ DATAOUT 4 d24 to d31

# OTP\_ECC\_DATAIN 5 32 to 39 OTP\_ECC\_ DATAOUT 5 d32 to d39

# OTP\_ECC\_DATAIN 6 40 to 47 OTP\_ECC\_ DATAOUT 6 d40 to d47

# OTP\_ECC\_DATAIN 7 48 to 55 OTP\_ECC\_ DATAOUT 7 d48 to d55

# OTP\_ECC\_DATAIN 8 56 to 63 OTP\_ECC\_ DATAOUT 8 d56 to d63

# OTP\_ECC\_DATAIN 9 64 to 71

## ECC Diagnostic Test: The device provides a diagnostic tool to test the ECC function. There are two modes

that are available to run the diagnostic. The first, auto mode ( *OTP\_ECC\_TEST\[MANUAL\_AUTO\]* = 0), uses internal data to run the tests. In auto mode, the *OTP\_ECC\_TEST\[DED\_SEC\]* bit selects the type of test that is to be performed and the *OTP\_ECC\_TEST\[ENC\_DEC\]* bit determines if the encoder or decoder function is to be tested. The result of the ECC test is provided in the *OTP\_ECC\_DATAOUT\** registers within 1μs delay. The test steps and expected results from each test are shown below.

## Automatic Decoding steps

1. Set ECC Test to automatic *OTP\_ECC\_TEST\[MANUAL\_AUTO\]* = 0 2. Set decoder setting *OTP\_ECC\_TEST\[ENC\_DEC\]* = 0 3. Set decoder to single or double encoding setting with *OTP\_ECC\_TEST\[DED\_SEC\]* (1 for DED or 0 for SEC) 4. Clear all SEC/DED faults by *FAULT\_RST2\[RST\_OTP\_DATA\]* = 1 5. Enable ECC test *OTP\_ECC\_TEST\[ENABLE\]* = 1 6. Read *FAULT\_OTP\[SEC\_DET\]* flag for SEC or *FAULT\_OTP\[DED\_DET\]* flag for DED 7. Block read *OTP\_ECC\_DATAOUT1* to *OTP\_ECC\_DATAOUT8* to verify the decoder test results as in Table 8-30 8. Disable ECC test *OTP\_ECC\_TEST\[ENABLE\]* = 0

## Automatic Encoding steps

1. Set ECC TEST to automatic *OTP\_ECC\_TEST\[MANUAL\_AUTO\]* = 0 2. Set the encoder setting using *OTP\_ECC\_TEST\[ENC\_DEC\]* = 1 3. Enable the ECC test with *OTP\_ECC\_TEST\[ENABLE\]* = 1 4. Block read *OTP\_ECC\_DATAOUT1* to *OTP\_ECC\_DATAOUT9* to verify the encoder test results as in Table 8-30 5. Disable ECC test *OTP\_ECC\_TEST\[ENABLE\]* = 0

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

**Table 8-30. Decoder and Encoder Test Verification**

# \[DED\_SEC\]

***\[ENC\_DEC\]*** ***\[SEC\_DET\]*** ***\[DED\_DET\]*** ***OTP\_DATAOUT\****

0 (SEC test) 0 (Decoder test) 0x18C3 FF8A 68A9 8069

0 (SEC test) 1 (Encoder test) N/A N/A 0xCD 3968 C140 2EA5 ED6D

1 (DED test) 0 (Decoder test) 0x0000 0000 0000 0000

1 (DED test) 1 (Encoder test) N/A N/A 0xCD 3968 C140 2EA5 ED6D

**8.3.6.4.5 Integrated Hardware Protector Check** ***8.3.6.4.5.1 Parity Check***

When the OVUV and OTUT protectors are enabled, the register settings related to the OVUV and OTUT configurations are latched to protector blocks. The device will check periodically in the background to ensure the latched configurations remain the same throughout the protector operation.

The parity check covers the following latched setting. If a parity fault in the OVUV protector is detected, the device will set the *FAULT\_PROT1\[VPARITY\_FAIL\]* = 1. If a parity fault in the OTUT protector is detected, the device will set the *FAULT\_PROT1\[TPARITY\_FAIL\]* = 1.

**Table 8-31. Protector Parity Check Settings**

| OVUV Protector | OTUT Protector | Note |
|:--- |:--- |:--- |
| OV threshold, UV threshold | OT threshold, UT threshold | Ensure threshold settings remains the same during the operation |
| OVUV\_MODE setting | OTUT\_MODE setting | Ensure the protector doesn't switch to a different operation mode |
| NUM\_CELL setting | GPIO\_CONF1 to GPIO\_CONF4 | settings |

OV threshold, UV threshold OT threshold, UT threshold Ensure threshold settings remains the same during the operation

OVUV\_MODE setting OTUT\_MODE setting Ensure the protector doesn't switch to a different operation mode

NUM\_CELL setting *GPIO\_CONF1* to *GPIO\_CONF4 * settings

Ensure the active channel (either cell channels for OVUV or GPIO channel for OTUT) remains the same during operation ***8.3.6.4.5.2 OVUV and OTUT DAC Check***

The OV, UV, OT, and UT DAC values are multiplexed to the AUX ADC from which the host can read out the values as part of the diagnostic check on the protector threshold settings.

To measure the protector's DAC value, it is recommended to lock the OVUV or OTUT protectors to a single channel through *OVUV\_CTRL\[OVUV\_LOCK3:0\]* for OV and UV DAC measurement; and through *OTUT\_CTRL\[OTUT\_LOCK2:0\]* for OT and UT DAC measurement, and restart the OVUV protectors or OTUT protector to run in the single channel run mode. Host ensures the locked cell channel is not under OV or UV fault or the locked GPIO channel is not under OT or UT fault. Otherwise, the DAC measurement will not be reflecting the triggering threshold value. Note that the OV and UV DAC value is (0.8 x the threshold setting). ***8.3.6.4.5.3 OVUV Protector BIST***

The device implemented an OVUV BIST (Built-In-Self-Test) function to test the primary OVUV protector path. Host can start the BIST run by setting *\[OVUV\_MODE1:0\]* = 0b10 and *\[OVUV\_GO\]* = 1. The BIST run covers: 1. OV and UV comparators thresholds: a. A higher and lower than the set threshold are checked to ensure the comparator is triggered correctly. b. If failure is detected, the corresponding *FAULT\_PROT2\[OVCOMP\_FAIL\]* or *\[UVCOMP\_FAIL\]* bit will be set. 2. The path from the OVUV MUX to UV fault status bit and NFAULT pin: a. For each VC channel, a switch is open so that input to the OVUV MUX is open and will lead to a UV detection to the channel under test b. The BIST engine then checks the logic to assert corresponding *FAULT\_UV* register bit and the NFAULT is set properly. c. The BIST engine resets the corresponding *FAULT\_UV* bit and deasserts the NFAULT, then switches to test the next channel and repeats the process until all active channels are tested. d. If failure is detected, the corresponding *\[VPATH\_FAIL\]* bit is set. 3. OV fault bit and NFAULT path a. The BIST engine forces 1 to the *FAULT\_OV\** register, one bit at time, to ensure each *FAULT\_OV\* * register bit can be set and the NFAULT can be asserted, accordingly. b. If failure is detected, the corresponding *\[VPATH\_FAIL\]* bit will be set. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

If NFAULT is enabled, host observes NFAULT toggling during the BIST run. Upon completion of the BIST run, the OVUV comparators will be turned off. Host starts the regular OVUV round robin mode by sending [OVUV_GO] = 1 with [OVUV_MODE1:0] = 0b01 (round robin mode).

**Note** - • If a *\[OVUV\_GO\]* = 1 is sent during the OVUV BIST run, device will execute the new GO command  based on the *\[OVUV\_MODE1:0\]* setting. - • Before starting the OVUV Protector BIST, host masks out all the non-OVUV related faults, and  ensures there are no OV and UV faults on any cell channels (recommended all cell voltages to be at least 100 mV apart from the OV or UV threshold during the BIST run). Otherwise, the BIST result is not invalid. - • After BIST starts, if pre-existing fault is detected before starting step 2, the BIST engine will be  aborted and the *FAULT\_PROT2\[BIST\_ABORT\]* = 1. - • A no reset option, *DIAG\_PROT\_CTRL\[PROT\_BIST\_NO\_RST\]* = 1, is available to command the  BIST engine not to reset the fault status and NFAULT pin after testing each channel. If a BIST run fails, host can select this option and re-run BIST to detect which cell channel path is unable reflect a fault condition in the fault registers. ***8.3.6.4.5.4 OTUT Protector BIST***

The device implemented an OTUT BIST function to test the primary OTUT protector path. Host can start the BIST run by setting *\[OTUT\_MODE1:0\]* = 0b10 and *\[OTUT\_GO\]* = 1. The BIST run covers: 1. OT and UT comparator thresholds a. A higher and lower than the set threshold are checked to ensure the comparator is triggering correctly. b. If failure is detected, the corresponding *FAULT\_PROT2\[OTCOMP\_FAIL\]* or *\[UTCOMP\_FAIL\]* bit will be set. 2. The path from GPIO MUX to UT fault bit and NFAULT path a. For each GPIO channel, the GPIO is internally pulled up so the input to the OTUT MUX is high and will lead to a UT detection to the channel under test. b. The BIST cycle then checks the logic to assert the corresponding *FAULT\_UT* register bit and the NFAULT is set properly. c. The BIST engine resets the corresponding *FAULT\_UT* bit and deasserts the NFAULT, then switches to test the next channel. d. If failure is detected, the corresponding *\[TPATH\_FAIL\]* bit will be set. 3. OV fault bit and NFAULT path a. The BIST engine forces 1 to the *FAULT\_OT* register, one bit at time, to ensure each *FAULT\_OT* register bit can be set and the NFAULT can be asserted, accordingly. b. If failure is detected, the corresponding *\[TPATH\_FAIL\]* bit will be set.

If NFAULT is enabled, host observes NFAULT toggling during the BIST run. Upon completion of the BIST run, the OTUT comparators will be turned off. Host starts the regular OTUT round robin mode by sending [OTUT_GO] = 1 with [OTUT_MODE1:0] = 0b01 (round robin mode).

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

**Note** - • If a *\[OTUT\_GO\]* = 1 is sent during the OTUT BIST run, device will execute the new GO command  based on the *\[OVUV\_MODE1:0\]* setting. - • Before starting the OTUT Protector BIST, host masks out all non-OTUT related faults, and ensures  there are no OT and UT faults on any GPIO during the BIST run). Otherwise, the BIST result is not invalid. - • After BIST starts, if pre-existing fault is detected before starting step 2, the BIST engine will be  aborted and the *FAULT\_PROT2\[BIST\_ABORT\]* = 1. - • A no reset option, *DIAG\_PROT\_CTRL\[PROT\_BIST\_NO\_RST\]* = 1, is available to command the  BIST engine not to reset the fault status and NFAULT pin after testing each channel. If a BIST run fails, host can select this option and re-run BIST to detect which GPIO channel path is unable reflect a fault condition in the fault registers.

**8.3.6.4.6 Diagnostic Through ADC Comparison**

***8.3.6.4.6.1 Cell Voltage Measurement Check*** Cell voltage measurement path comparison:

The cell voltage measurement check is performed by comparing the prefiltered measurement result from Main ADC versus measurement result from AUX ADC. To read the compared value measured by Main ADC and AUX ADC, MCU has to set up this diagnostic check to lock on a single channel using *\[AUX\_CELL\_SEL\]* setting and the start this diagnostic check. In this configuration, the compared values from Main ADC and AUX ADC are reported to *DIAG\_MAIN\_HI/LO* registers and *DIAG\_AUX\_HI/LO* registers respectively.

Both Main and AUX ADC has the same front end filters. This diagnostic time is mostly spent on waiting for the AAF on the AUX ADC path to settle. The *\[AUX\_SETTLE\]* setting allows the MCU to make trade-off between diagnostic time and noise filter level. Additionally, when AUX ADC starts, by default, AUXCELL slot always align to the Main ADC Cell1 slot. The *\[AUX\_CELL\_ALIGN\]* setting allows MCU to change this alignment to Main ADC Cell8 slot, resulting with less sampling time delta between Main and AUX ADC on the higher channels.

|  | SAR |
|:--- |:--- |
|  | ADC |

# De MUX

To AUXCELL register If single channel lock is enabled

|  | SAR |
|:--- |:--- |
|  | ADC |

# De MUX To VCELL registers Comp To FAULT\_COMP\_VCCB register

Comparison threshold set by DIAG\_COMP\_CTRL1\[VCCB\_THR4:0\] Latest VCELL Unfiltered value AUXCELL value Main ADC Path Filters (BCI & AAF), LS

# MUX CB Filters BCI & AAF filters

# AUX ADC Path + Digital LPF

**Figure 8-47. Cell Voltage Measurement Diagnostic**

**Before starting the cell voltage measurement comparison, host ensures:** - • The desired AUXCELL channels to be tested are configured in the *ADC\_CTRL2\[AUX\_CELL\_SEL4:0\]* setting  and AUX ADC is enabled and in continuous mode. - • Allow AUX ADC to run through all AUXCELL channels for the devie to compensate for common mode error  before starting this diagnostic check. - • Main ADC must be enabled and is in continuous mode. - • Select the (VCELL - AUXCELL) comparison threshold through *DIAG\_COMP\_CTRL1\[VCCB\_THR4:0\] * setting. - • Select the desired settling time for the AUX CELL channel through *ADC\_CONF1\[AUX\_SETTLE1:0\].* **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

**To start the cell voltage measurement comparison: **

1. Set *DIAG\_COMP\_CTRL3\[COMP\_ADC\_SEL2:0\]* = cell voltage measurement check (that is, 0b001) and set [COMP_ADC_GO] = 1. 2. For each channel enabled by *\[AUX\_CELL\_SEL4:0\]*, the device will compare abs\[(VCELL - AUXCELL)\] \< *\[VCCB\_THR4:0\]*. 3. Wait for the comparison to be accomplished, roughly \[(number of channel) \* (AUXCELL settling time + one round robin cycle time)\]. 4. The cell voltage measurement comparison is completed when *ADC\_STAT2\[DRDY\_VCCB\]* = 1.

Host checks the *FAULT\_COMP\_VCCB1* and *FAULT\_COMP\_VCCB2* registers for the comparison result. **ADC comparison abort conditions:**

The device will not start the cell voltage measurement comparison under the invalid conditions listed below. When the comparison is aborted, the *FAULT\_COMP\_MISC\[COMP\_ADC\_ABORT\]* = 1, *\[DRDY\_AUX\_CEL\]* = 1, *\[DRDY\_VCCB\]* = 1, and *FAULT\_COMP\_VCCB1/2* registers = 0xFF. If *\[AUX\_CELL\_SEL4:0\]* is set to locked at a single channel, the *AUX\_CELL\_HI/LO* registers will be reset to default value 0x8000 if the comparison run is aborted.

Invalid conditions or settings which will prevent the start of the cell voltage measurement comparison: - • Invalid *\[AUX\_CELL\_SEL\]* setting: results in no AUX ADC measurement on the selected channel. The  *AUX\_CELL\_HI/LO* registers are kept in default value. - • Channel higher than the NUM\_CELL configuration is selected. - • Invalid BBVC\_POSN setting: - - Adjacent channels are enabled in the *BBVC\_POSN1/2* registers. - *- BBVC\_POSN2\[CELL1\]* is enabled. - - More than two channels are selected in *BBVC\_POSN1/2*. - *- \[AUX\_CELL\_SEL\]* is locked to any of the selected channels in *BBVC\_POSN1/2*. - • Main or AUX ADCs are off or not set in continuous mode. **Post-ADC digital LPF check:**

The digital LPF is checked continuous whenever the Main ADC is running. A duplicate diagnostic LPF is implemented to check against each LPF for each VC channel and the BBP/N channel. The check is performed with one LPF at a time.

Example, to test LPF1 for cell channel 1, the input (that is, ADC measurement result from cell 1) is fed to the LPF1 and the diagnostic LPF for a period of time. The output of the LPF1 and the diagnostic LPF are compared against each other. Several outputs from LPF1 and diagnostic LPF will be compared to ensure the operation of the LFP1 before moving to check the next LFP. If any of the LPFs fail the diagnostic check, FAULT_COMP_MISC[LPF_FAIL] = 1.

When the LPF for each active cell channels is tested once, *ADC\_STAT2\[DRDY\_LPF\]* = 1. This diagnostic check of the LPFs will continuously run in the background as long as the Main ADC is running.

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

# MUX DIAG LFP

# LPF BB

# LPF 16

# LPF BB

# MUX BIST Compare

**Pass/Fail** Indicates with \[LPF\_FAIL\] bit VCell 1 VCell 16 Busbar **Main ADC** **Conversion**

Inject Fault to check DIAG LFP by setting [LPF_FAULT_INJ] = 1

# MUX DIAG LFP

# LPF CS

# LPF 16

# LPF 1

# MUX BIST Compare

**Pass/Fail** Indicates with \[LPF\_FAIL\] bit VCell 1 VCell 16 Current **Main ADC** **Conversion**

Inject Fault to check DIAG LFP by setting [LPF_FAULT_INJ] = 1

## Figure 8-48. Post-ADC LPF Diagnostic (Blue Path as Example of Checking LPF1)

## Furthermore, the device also implements a check to verify the functionality of the diagnostic LPF itself. By setting

*DIAG\_COMP\_CTRL4\[LPF\_FAULT\_INJ\]* = 1 and restarting the Main ADC, the device will inject a fault into the diagnostic LPF, forcing a failure during the LPF diagnostic check which then sets the *\[LPF\_FAIL\]* = 1. When the test is completed, simply set the *\[LPF\_FAULT\_INJ\]* = 0.

## 8.3.6.4.6.2 Temperature Measurement Check

## Similar to the cell voltage measurement check, the device checks the thermistor temperature measurement by

comparing the Main ADC measurement to the AUX ADC measurement. To read the compared value measured by Main ADC and AUX ADC, MCU has lock on a single channel using *\[AUX\_GPIO\_SEL\]* setting and the start this diagnostic check. In this configuration, the compared values from Main ADC and AUX ADC are reported to *DIAG\_MAIN\_HI/LO* registers and *DIAG\_AUX\_HI/LO* registers respectively. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

# MUX GPIO MUX

|  | SAR |
|:--- |:--- |
|  | ADC |

DeMUX To AUX\_GPIO Registers if a single GPIO is locked

# MUX GPIO MUX

|  | SAR |
|:--- |:--- |
|  | ADC | DeMUX To GPIO Measurement registers Comp To FAULT\_COMP\_GPIO register

Comparison threshold set by DIAG\_COMP\_CTRL2\[GPIO\_THR2:0\] Main ADC Path

# AUX ADC Path GPIO Measurement GPIO Measurement

# GPIO1

# GPIO8

**Figure 8-49. Thermistor Temperature (GPIO) Measurement Diagnostic**

**Before starting the temperature measurement comparison, host ensures:** - • Main ADC must be enabled and is in continuous mode. - • The desired GPIO channels to be tested are configured in the *ADC\_CTRL3\[AUX\_GPIO\_SEL3:0\]* setting and  AUX ADC is enabled and in continuous mode. - • Select the comparison threshold through *DIAG\_COMP\_CTRL2\[GPIO\_THR2:0\]* setting.

**To start the cell voltage measurement comparison:**

1. Set *DIAG\_COMP\_CTRL3\[COMP\_ADC\_SEL2:0\]* = GPIO measurement check (that is, 0b101) and set [COMP_ADC_GO] = 1. 2. For each channel enabled by *\[AUX\_GPIO\_SEL4:0\]*, the device will compare abs\[(GPIO from Main - GPIO from AUX)] < [GPIO_THR2:0]. 3. Wait for the comparison to be accomplished which can take up to 64 ADC round robin times. 4. The GPIO measurement comparison is completed when *ADC\_STAT2\[DRDY\_GPIO\]* = 1.

Host checks the *FAULT\_COMP\_GPIO* register for the comparison result. **ADC comparison abort conditions:**

The device will not start the temperature measurement comparison under the invalid conditions listed below. When the comparison is aborted, the *FAULT\_COMP\_MISC\[COMP\_ADC\_ABORT\]* = 1, *\[DRDY\_GPIO\]* = 1, and *FAULT\_COMP\_GPIO* = 0xFF. If *\[AUX\_GPIO\_SEL3:0\]* is set to locked at a single channel, the *AUX\_GPIO\_HI/LO * registers will be reset to default value 0x8000 if the comparison run is aborted.

**Invalid conditions or settings which will prevent the start of the temperature measurement comparison: ** - • Invalid *\[AUX\_GPIO\_SEL\]* setting which the selected GPIO isn't configured for ADC measurement. The  *AUX\_GPIO\_HI/LO* registers are kept in default value. This also applies to the case if *\[AUX\_GPIO\_SEL\]* is selected for all GPIOs but none of the GPIOs are configured for ADC measurement. - • Main or AUX ADCs are off or not set in continuous mode. ***8.3.6.4.6.3 Cell Balancing FETs Check***

The cell balancing FET check is performed by turning on the balancing FET and comparing the voltage across the FET (through the AUX ADC path) versus the cell voltage (through the Main ADC path). To read the AUXCELL measurement used for the check, MCU has to set up this diagnostic check to lock on a single channel using *\[AUX\_CELL\_SEL\]* setting and the start this diagnostic check. The AUXCELL compared value will be reported to *DIAG\_AUX\_HI/LO* registers.

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

# CB

# VC

# VC

# CB Device CBn CB n Cn CB n-1 VC n-1 +

**AUXCELL, cell voltage measured by ** **AUX ADC from CB pin**

**VCELL, cell voltage ** **measured by Main ADC from ** **VC pin** comp To FAULT\_COMP\_CBFET\* registers

Comparison threshold is fixed to AUXCELL \< ½ of VCELL

**Figure 8-50. Cell Balancing FET Diagnostic**

**Before starting the cell balancing FET comparison, host ensures:** - • Main ADC is running in continuous mode. - • Configured in the *ADC\_CTRL2\[AUX\_CELL\_SEL4:0\]* to select the AUXCELL channels which the CB FETs  are tested. - • Select the desired settling time for the AUX CELL channel through *ADC\_CONF1\[AUX\_SETTLE1:0\]*. - • Pause CB if balancing is running. - • Configured which CBFET to be tested through *DIAG\_CBFET\_CTRL1* and *DIAG\_CBFET\_CTRL2* registers. - - The rules of maximum of eight CBFETs to be on and turn on no more than two consecutive CBFETs still  apply. - - Recommended to test in odd and even manner. **To start the CBFET comparison:**

1. Start AUX ADC in continuous mode. 2. Turn on the selected CBFET by setting *DIAG\_COMP\_CTRL3\[CBFET\_CTRL\_GO\]* = 1 and wait for appropriate dv/dt time. 3. Set DIAG_COMP_CTRL3[COMP_ADC_SEL2:0] = CBFET check (that is, 0b100) and set [COMP_ADC_GO] $$ = 1. $$ 4. The device turns on the CBFET configured in the above step and compares the AUXCELL measurement (through CB channel) \< half of the VCELL measurement (through VC channel). Only the CBFETs that are enabled are checked. 5. The CBFET comparison is completed when *ADC\_STAT2\[DRDY\_CBFET\]* = 1. 6. Repeat this procedure for other set of CBFET test. To turn off the CBFET enabled for this test, MCU clear the *DIAG\_CBFET1* and *DIAG\_CBFET2* registers then set the *\[CBFET\_CTRL\_GO\]* = 1. Otherwise, exiting from the CB pause state by sending *\[CB\_PAUSE\]* = 0 will resume the regular balancing which turns off the CBFETs enabled for this test and resume on the CBFETs that are set for balancing.

Host checks the *FAULT\_COMP\_CBFET1* and *FAULT\_COMP\_CBFET2* registers for the comparison result. Repeat the steps to compare the remaining CBFETs. **ADC comparison abort conditions:**

The device will not start the CBFET comparison under the invalid conditions listed below. When the comparison is aborted, the *FAULT\_COMP\_MISC\[COMP\_ADC\_ABORT\]* = 1, *\[DRDY\_AUX\_CEL\]* = 1, *\[DRDY\_CBFET\]* = 1, and *FAULT\_COMP\_CBFET1/2* = 0xFF. If *\[AUX\_CELL\_SEL4:0\]* is set to locked at a single channel, the *AUX\_CELL\_HI/LO* registers will be reset to default value 0x8000 if the comparison run is aborted.

Invalid conditions or settings which will prevent the start of the cell voltage measurement comparison: **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

- • Invalid *\[AUX\_CELL\_SEL\]* setting which results in no AUX ADC measurement on the selected channel. The  *AUX\_CELL\_HI/LO* registers are kept in default value. - • Channel higher than the NUM\_CELL configuration is selected. - • Invalid BBVC\_POSN setting: - - Adjacent channels are enabled in the *BBVC\_POSN1/2* registers. - *- BBVC\_POSN2\[CELL1\]* is enabled. - - More than two channels are selected in *BBVC\_POSN1/2*. - *- \[AUX\_CELL\_SEL\]* is locked to any of the selected channels in *BBVC\_POSN1/2*. - • Main or AUX ADCs are off or not set in continuous mode. - • CB is running and it is not in pause mode. - • More than eight CBFETs are enabled, or more than two consecutive CBFETs are enabled in  *DIAG\_CBFET\_CTRL1/2* registers. ***8.3.6.4.6.4 VC and CB Open Wire Check***

The device can detect an open wire connection on the VC and CB pins. A current sink is connected to each VC and CB pin, except VC0 and CB0 pins which are connected with a current source.

When the current sink (or current source) is enabled and if there is an open wire connection, the external differential capacitor will be depleted and the cell voltage measurement will drop to an abnormal level over time. Similar detection concept applies to the VC0 and CB0 pins with a current source. If there is an open wire connection, the VC0 or CB0 will be pulled up by the current source, resulting in a reduced cell voltage measurement over time.

When the diagnostic comparison is enabled, the device will compare the cell voltage measurement from Main ADC (for VC pins open wire detection) against a host-programmed threshold; or comparing the AUX CELL measurement from the AUX ADC (for CB pins open wire detection) against a host-programmed threshold.

If MCU lock to a single CB channel though *\[AUX\_CELL\_SEL\]* before starting the CB open wire check. The device will report the AUXCELL measurement used for the check comparison. The value is reported in *DIAG\_AUX\_HI/LO* registers. Since there is no single channel lock mechanism in Main ADC, VC channel measurement used for VC open wire will not be reported in *DIAG\_MAIN\_HI/LO* registers.

# VC

# VC

# VC Comp VC n VC n-1

+ VCELL, cell voltage measured by Main ADC from VC pin Cell to pcb wire OW current sink OW current sink Device

Comparison threshold set by DIAG\_COMP\_CTRL2\[OW\_THR3:0\] To FAULT\_COMP\_VCOW\* registers **Figure 8-51. Open Wire Detection**

**Before starting the open wire comparison, host ensures:** - • For VC open wire detection, Main ADC is running in continuous mode. - • For CB open wire detection, AUX ADC is running in continuous mode - - Configured in the *ADC\_CTRL2\[AUX\_CELL\_SEL4:0\]* to select the AUXCELL channels - - Select the desired settling time for the AUX CELL channel through *ADC\_CONF1\[AUX\_SETTLE1:0\].* - • Configure the open wire detection threshold through *DIAG\_COMP\_CTRL2\[OW\_THR3:0\]*.

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## To start the open wire comparison

1. Turn on the VC pins (or CB pins) current sink or source through *DIAG\_COMP\_CTRL3\[OW\_SNK1:0\]*. 2. Wait for dV/dt time of the external capacitor to deplete to the detection threshold if there is an open wire fault. 3. For VC open wire detection, select *DIAG\_COMP\_CTRL3\[COMP\_ADC\_SEL2:0\]* = OW VC check (that is, 0b010) and set *\[COMP\_ADC\_GO\]* = 1. Or for CB open wire detection, *\[COMP\_ADC\_SEL2:0\]* = OW CB check (that is, 0b011). 4. The device compares all active VCELL measurement (for VC open wire) or AUX CELL measurement (for CB open wire) against the *\[OW\_THR3:0\]* threshold setting. 5. When the comparison is completed, *ADC\_STAT2\[DRDY\_VCOW\]* = 1 for VC open wire (or *\[DRDY\_CBOW\]* = 1 for CB open wire). 6. Host then turns off all current sinks and sources through *DIAG\_COMP\_CTRL3\[OW\_SNK1:0\]*.

## Host checks the FAULT\_COMP\_VCOW1/2 or FAULT\_COMP\_CBOW1/2 registers for the comparison result.

## 8.3.7 Bus Bar Support

## The device supports bus bar measurement in two types of connections

- • Bus bar connected to a dedicated bus bar channel through BBP and BBN pins - • Bus bar connected to a VC channel

## A total of three bus bars can be connected to a single device, one through BBP/N pins and two through VC

channels. Table 8-32 shows the difference between the two connection methods. Details are described in the later subsections.

## Table 8-32. Bus Bar Connection Methods

**Supporting Feature/ ** **Limitation** **Bus Bar Connected Across BBP/BBN Pins** **Bus Bar Connected Individually Across VC Pins** Number of bus bar can be connected per device

Connection channel Can be connected to any channel but the bottom one

Can be connected to any channel but the bottom one

Bus bar measurement Yes, result is output to *BUSBAR\_HI/LO* registers Yes, result is output to *VCELLx\_HI/LO* registers, where x is the VC channel the bus bar is connected to Integrated filters to bus bar measurement

Yes, same front end filters as the regular cell channels and post ADC digital LPF. BBP/N channel is x5 gain with ±1-V input range. Dedicated digital LPF setting separated from the LPF setting used for cell voltage measurements.

Yes, same front end filters as the regular cell channels and post ADC digital LPF. Use the same cell voltage LPF setting for bus bar measurement.

Host requires to adjust cell measurement adjustment

Yes, a cell + bus bar are sharing a single VC channel using this method. Host needs to separate out the bus bar measurement to obtain the actual cell measurement on the shared channel.

No, cell and bus bar are connected to their own VC channels and measurements are reported separately

Cell balancing limitation No CB limitation, but host turns on adjacent CBFETs when balancing a cell above the bus bar connected channel

No CB limitation but require to float the upper CB pin on the bus bar connected channel

## The device supports bus bar measurement in a connection when a bus bar is connected to a VC channel. A total

of two bus bars can be connected to a single device through the VC channels. Table 8-33 shows the details as described in the later subsections.

## Table 8-33. Bus Bar Connection Methods

**Supporting Feature/ Limitation** **Bus Bar Connected Individually Across VC Pins** Number of bus bar can be connected per device

Connection channel Can be connected to any channel but the bottom one

Bus bar measurement Yes, result is output to *VCELLx\_HI/LO* registers, where x is the VC channel the bus bar is connected to **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

**Table 8-33. Bus Bar Connection Methods (continued)**

**Supporting Feature/ Limitation** **Bus Bar Connected Individually Across VC Pins**

Integrated filters to bus bar measurement Yes, same front end filters as the regular cell channels and post ADC digital LPF. Use the same cell voltage LPF setting for bus bar measurement.

Host requires to adjust cell measurement adjustment

No, cell and bus bar are connected to their own VC channels and measurements are reported separately

Cell balancing limitation No CB limitation but require to float the upper CB pin on the bus bar connected channel ***8.3.7.1 Bus Bar on BBP/BBN Pins***

The device provides a dedicated bus bar channel through BBP/BBN pins for bus bar connection and measurement. It is a floating channel, allowing the bus bar to be connected to any cell except the bottom cell of a module. Using the bus bar channel maximizes the use of cell channels in the device across different module sizes. **8.3.7.1.1 Typical Connection**

With the bus bar connected to BBP/BBN pins, it is intended to allow a single cell channel (VC channel) to be shared with a cell + a bus bar (see Figure 8-52 (a) connection). Usually, such connection introduced additional IR error to the cell measurement to the system. The dedicated bus bar channel through BBP/BBN pins supported in the device allows the host to measure the bus bar voltage to obtain the actual cell measurement.

Figure 8-52 (a) connection applies to bus bar connecting to any middle VC channel. That is, in a single device, there is a cell connected above and below the BBP/BBN channel. To support the hotplug on the bus bar channel, the device only requires a 400-Ω filter resistor each on the BBP/N pins and a 0.47-µF/16-V differential capacitor across the BBP/N pins.

If the bus bar connected to BBP/N is placed at the top of a module (see Figure 8-52 (b) connection), such connection is the exception in the BBP/N case that a cell channel is not being shared. In this connection, actual cell measurements are made through the VC channels and host does not require additional calculations.

Figure 8-52 (b) connection applies to bus bar connected to top of the module, where in a single device, no cell is connected above the bus bar. To support the hotplug on the bus bar channel, besides the 400-Ω filter resistor each on BBP/N pins and a 0.47-µF/16-V differential capacitor across BBP/N pins, and additional 0.47-µF/16-V differential capacitor is needed to connect from BBN to the top CB pins. This additional capacitor forms a complete capacitor ladder from all cells in the module to the bus bar, allowing high spike voltage during the hotplug to distributor across the capacitor ladder.

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

# VC

# CB

# 400 Ÿ 

# 400 Ÿ 

# 10 Ÿ 

# BAT

# BBN

# BBP

# VC16

# CB16

# VC

# CB

# VC15

# CB15

# AVSS Pcb connector **Device**

# VC0

# VC busbar **Device**

# 30 Ÿ 

# BAT

# VC16

# CB16

# VC

# CB

# VC14

# CB14

# AVSS **Device**

# VC0

# VC

# VC

# CB

# VC

# CB

# VC15

# CB15 busbar **Device**

# VC

# CB

# VC13

# CB13

# BBN

# BBP

# 400 Ÿ

# 400 Ÿ  Pcb connector

**A cell + ** **EXV** **EDU³VKDULQJ´DVLQJOH** **VC channel**

**A bus bar channel within, allowing host ** **to obtain the actual cell measurement by ** **subtracting the bus bar measuremement  **

**bus bar connected BBP/N ** **above the top of a module.**

**In such connection, the VC ** **FKDQQHO** **LVQRWEHLQJ³VKDUHG´**

**(a) BBP/N connection with bus bar connected in any middle VC channel** **(b) BBP/N connection with bus bar connected above the top of a module**

# VC

# CB 10 nF

# CB

# CB

# VC

# VC

# VC 0.47 µF + + + + + + +

# VC 22 nF 0.47 µF 0.47 µF

# CB

# VC

# Figure 8-52. Bus Bar Connected Across BBP and BBN Pins

# 8.3.7.1.2 Bus Bar Measurement

# The differential measurement across (BBP-BBN) is measured by the Main ADC and AUX ADC. See Section

8.3.2.1.1 and Section 8.3.2.2.1 for details. Use the *BBP\_LOC* register to indicate which VC channel is shared with the BBP/N connection. This information enables the device to better have better common mode correction for the final ADC measurement. Host will be aware that additional IR error is introduced to the shared VC channel. If OVUV protector is enabled, this shared channel may trigger earlier OV or UV detection due to the additional IR increase (during charge) or decrease (during discharge) to the shared channel measurement.

# 8.3.7.1.3 Cell Balancing Handling

# Because the bus bar is shared with a cell to a cell channel, there is no special handling on the cell balancing

control. Host will be aware that additional IR error is introduced to the VCB\_DONE detection (through VC channel) on the shared channel.

# www.ti.com

# BQ79616 SLUSF21 - JUNE 2023

# Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

# CB

# CB

# VC

# VC

# VC

# CB

## CB Control

## Device CBn

## CB n CBn-1 Cn

# CB

## CB n-1

## VC n-1

## +

## +

# Figure 8-53. Cell Balancing with Bus Bar (Through BBP/N) Sharing a Cell Channel

# 8.3.7.1.4 Cell Voltage Diagnostic Control

# The device still supports VC channel versus CB channel by looking at the sum of (cell + bus bar measurement)

comparison check on the shared channel. See Section 8.3.6.4.6.1. Additionally, bus bar measurement can be checked by comparing bus bar channel measurement from Main ADC and AUX ADC.

|  | SAR |
|:--- |:--- |
|  | ADC |

# De MUX

|  | SAR |
|:--- |:--- |
|  | ADC |

# De MUX Main ADC Path BusBar

| Digital | LPF |
|:--- |:--- |
| To BUSBAR\_HI/LO | registers |
| To AUXCELL register if \[AUX\_CELL\_SEL4:0\] | = 0x01 (busbar channel) | To BUSBAR\_HI/LO registers

To AUXCELL register if *\[AUX\_CELL\_SEL4:0\]* = 0x01 (busbar channel)

**Host to check the measurements** Bus bar channel from AUX ADC Filters (BCI & AAF), LS BCI & AAF filters 16:1 MUX CB Filters Aux ADC Path

# If ADC\_CTRL1\[LPF\_BB\_EN\]=0

# Figure 8-54. Bus Bar Through BBP/N Measurement Check

# The BBP/N pins have built-in current sink for open wire detection. The current sink is turned on when

*DIAG\_COMP\_CTRL3\[OW\_SNK1:0\]* = 0b11. When there is a current flow through the bus bar, the (BBP-BBN) measurement is non-zero. If there is an open wire on the BBP or BBN pin, the current sink changes the (BBP- BBN) measurement to an abnormal value.

# BQ79616 SLUSF21 - JUNE 2023 **<https://www.ti.com**>

## Submit Document Feedback

Copyright © 2023 Texas Instruments Incorporated

# VC

# VC

# VC

# VC

# VC Cn VC n-1 + +

# BBP

| OW current | sink |
|:--- |:--- |
| OW current | sink |
| Busbar to pcb | wire | OW current sink Busbar to pcb wire

# BBN Cell to pcb wire

Busbar measured by Main ADC across BBP/ BBN pins BusBar

**Figure 8-55. Current Sink for BBP/N Open Wire Detection**

***8.3.7.2 Bus Bar on Individual VC Channel***

Besides connecting bus bar through BBP/N, the device also supports bus bar connection to an individual VC channel. All VC channels, except the bottom channel (VC1-VC0), support -2V to 5V measurement.

The device supports bus bar connection to an individual VC channel. All VC channels, except the bottom channel (VC1-VC0), support -2V to 5V measurement.

When bus bar is connected to an individual VC channel, host indicates the bus bar position in the *BBVC\_POSN1 * and *BBVC\_POSN2* registers. The following configuration is not supported for bus bar connection through individual VC channel. Configuring *BBVC\_POSN1* register with such configuration can cause error in balancing, OVUV detection and cell voltage measurement comparison check. - • Bottom channel does not support bus bar connection. That is, *BBVC\_POSN1\[CELL1\]* must be 0. - • Maximum of two bus bars can be connected through this connection. That is, only two bits are set to 1 in the  *BBVC\_POSN1* registers. - • Bus bar cannot be connected to the adjacent channels. **8.3.7.2.1 Typical Connection**

With bus bar connected to a VC channel individually, the upper CB pin on that channel is left floating to avoid forward biasing the internal CBFET (see Figure 8-56 (a) connection). This connection applies to bus bar connecting to any middle VC channel individually. That is, in a single device, there is a cell connected above and below the VC channel with bus bar connected. To ensure hotplug performance, the CB channel where the bus bar is connected will still have the differential capacitor even if the upper CB pin is floating. This capacitor forms a complete capacitor ladder from all cells and the bus bar connected to the device, allowing high-voltage spike during hotplug to distribute across the capacitor ladder.

If bus bar is connected to above the top of a module to an individual VC channel (see Figure 8-56 (b) connection), the upper CB pin on that channel is left floating but the CB differential capacitor will still be connected. Additionally, an additional RC filter is connected from the top CB pin to the BAT pin. This additional RC filter (using the same RC values as the other RC filter on the CB pins) is to ensure a complete capacitor ladder is formed for the device to distribute the high voltage spike with the same RC constant as the reset of the CB pins during hotplug event. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

# 30 Ÿ 

# BAT

# VC16

# CB16

# VC

# CB

# VC14

# CB14

# AVSS **Device**

# VC0

# VC

# VC

# VC

# CB

# VC15

# CB15

# CB busbar **Device**

# 30 Ÿ 

# BAT

# VC16

# CB16

# VC

# CB

# VC14

# CB14

# VC

# VC

# CB

# VC15

# CB15 busbar **Device**

# VC

# CB

# VC13

# CB13

# CB Pcb connector Pcb connector

**(a) Bus bar connected any middle individual VC channel** **(b) Bus bar connected individual VC channel above the top of a module**

# CB

# CB

# VC

# VC

# VC

# CB 10 nF + + + 10 nF

# CB

# VC

# CB

# CB VC

# VC + +

# Figure 8-56. Bus Bar Connected to Individual VC Channel

# 8.3.7.2.2 Bus Bar Measurement

# Bus bar measurement is performed through Main ADC measurement as one of the VC channels. The result is

reported to *VCELLx\_HI/LO* register, where x is the channel connected with the bus bar. Digital LPF is enabled and applied as the rest of the VC channel measurement configuration.

# The VC channel indicated for bus bar connection (through BBVC\_POSN1/2 registers) will be skipped for

VCB\_DONE check during cell balancing, OV and UV detection when OVUV protectors are enabled, and will have special handling during cell voltage measurement comparison check.

# 8.3.7.2.3 Cell Balancing Handling

# Because the upper CB pin is open on the channel where bus bar is connected, to balance the cell connected

above bus bar, host turns on the adjacent CBFET and configures with the same timer setting.

# Host configures BBVC\_POSN1/2 register to indicate the bus bar connection. This information is used to avoid

the channel connected with bus bar to trigger a VCB\_DONE detection and turn off its CBFET, which disconnects the balancing path for the cell above the bus bar.

# The balancing of the cell above the bus bar is still terminated based on the timer and cell voltage threshold,

which its CBFET will be turned off when one of the stop conditions is met. The balancing path is disconnected even if the CBFET on the bus bar connected channel remains on.

# Note

# The CBFET on the bus bar connected channel will be on until the timer expired. This may lead to a

delayed flagging of the *\[CB\_DONE\]* = 1 even if the actual cell balancing is completed.

# BQ79616 SLUSF21 - JUNE 2023 **<https://www.ti.com**>

## Submit Document Feedback

Copyright © 2023 Texas Instruments Incorporated

# CB

# CB

# VC

# VC

# VC CB Control Device CBn CB n CBn-1 Cn

# CB CB n-1

# CB CB n-2 VC n-1 VC n VC n-2 + +

# CB

# VC VC VC n-2 Configure with same CB Timer setting

## Figure 8-57. Cell Balancing with Bus Bar Connected to Individual VC Channel

## 8.3.7.2.4 Cell Voltage Diagnostic Control

## The cell voltage comparison check is still performed by checking the Main ADC measurement versus the AUX

ADC measurement. Because the upper CB pin of the CB channel, where a bus bar is connected, is open, the device handles the comparison check by comparing a sum of (cell + bus bar) from Main ADC versus sum of (cell + bus bar) from AUX ADC instead. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

# CB CB n CB n-1 **Device**

# CB

# VC

# VC VC n VC n-1

# CB CB n-2 VC n VC n-2 BusBar VC n-2

# VC **AUX ADC Measurement**

**Main ADC Measurement** **Main ADC Measurement** **Sum** Comp

# CB

# CB VC

# VC + +

## Figure 8-58. Cell Measurement Check with Bus Bar Connected to Individual VC Channel

## 8.4 Device Functional Modes

## The device has three power modes plus an POR state.

- • POR: This is not a power mode. This is a condition in which the voltage at the BAT pin is less than VBAT min,  and all circuits including the AVAO\_REF block in the device are powered off. - • SHUTDOWN: This is the lowest power mode. AVDD, DVDD and CVDD supplies are off. Only a gross  regulation at LDOIN pin is maintained. CVDD pin is will have a similar voltage as the LDOIN pin through internal circuit in order to support WAKE detection. - • SLEEP: This is the low power operation mode. Only limited functions are available. - • ACTIVE: This is the full power operation mode. All functions are supported under this state.

## The various functions supported under different power modes are summarized in Table 8-34 and the power state diagram is shown in Figure 8-59.

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## Table 8-34. Active Functions Summary

**Functional Block** **SHUTDOWN** **SLEEP** **ACTIVE** **POR**

Main ADC √ This is not a power state. All circuits are off. A sufficient voltage on VBAT will POR the device and put it to SHUTDOWN mode

# AUX ADC √

| OV/UV protector | √(1) | √ |
|:--- |:--- |:--- |
| OT/UT protector | √(1) | √ |
| Cell Balancing | √(1) | √ |
| OTCB Detection | √(1) | √ | OT/UT protector √ (1) √ Cell Balancing √ (1) √ OTCB Detection √ (1) √

Module Balancing (via control through *MB\_TIMER\_CTRL* ) √

| UART | √ |
|:--- |:--- |
| Comm Vertical Communication | √ |
| Fault Status and NFAULT | Communication |
| √ | √ |
| Comm timeout | √ |
| SLEEP timeout | √ | Comm Vertical Communication √ Fault Status and NFAULT Communication √ √ Comm timeout √ SLEEP timeout √ Thermal Shutdown Detection √ √

| SPI Controller | √ |
|:--- |:--- |
| OTP programming | √ |
| Always-on block to detect POR of the | device | OTP programming √ Always-on block to detect POR of the device √ √ √

(1) To enable cell balancing, OV/UV or OT/UT protector(s) in SLEEP mode, host must enable the function(s) in ACTIVE mode first, then put the device to SLEEP. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

# ACTIVE MODE

# SLEEP MODE

# SHUTDOWN MODE

1. Set * CONTROL1\[GOTO\_SLEEP\]* = 1, OR 2. Long comm timeout occurs w/  *COMM\_TIMEOUT\[CTL\_ACT\] * = 0, OR 3. When cell and/or module balancing is done and  $$ [BAL_ACT1:0] = 01 $$ Receive SLEEPtoACTIVE signal Device reset Receive WAKE signal

1. Set * CONTROL1\[GOTO\_SHTUTDOWN\]* = 1, OR 2. Long comm timeout occurs w/ *COMM\_TIMEOUT\[CTL\_ACT\] * = 1, OR 3. Receive SHUTDOWN signal, OR 4. Thermal shutdown occurs 5. When cell and/or module balancing is done and $$ [BAL_ACT1:0] = 10 $$ Device reset Receive WAKE signal

1. Receive  SHUTDOWN  signal, OR 2. Thermal shutdown occurs, OR 3. SLEEP timeout Device reset

Receive WAKE signal, OR Set *CONTROL1\[SOFT\_RESET\]* = 1

# BAT \< Min V BAT

# BAT \< Min V BAT

# BAT \< Min V BAT

# BAT \> Min V BAT

# POR

## Figure 8-59. Power State Diagram

## 8.4.1 Power Modes ***8.4.1.1 SHUTDOWN Mode***

## This is the lowest power mode. In SHUTDOWN mode, most of the functions are off. The device remains idle

to simply monitor the WAKE ping/tone (see Section 8.4.3 for details) to wake up from this state. Only a gross regulation on LDOIN and CVDD pins are maintain for WAKE ping/tone detection.

## 8.4.1.1.1 Exit SHUTDOWN Mode

## Communication is not supported in SHUTDOWN mode, host must send a WAKE ping or WAKE tone to enter

ACTIVE mode. Once device transitions from SHUTDOWN mode to ACTIVE mode, the following table indicates the expected fault bits being set under such transition has occurred.

## BQ79616 SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## Table 8-35. Expected Fault Bit After Device Wake From SHUTDOWN

**Device Position In ** **The Daisy Chain** **Expected Fault Bits After Waking Up From SHUTDOWN** Base device

FAULT_SYS[DRST] = 1 Digital reset by the wake ping

*FAULT\_COMM3\[FCOMM\_DET\] * $$ = 1 $$ *\[DRST\]* = 1 from the upper device

*FAULT\_COMM1\[COMMCLR\_D* $$ ET] = 1 $$ UART engine is reset Stack device (except top of stack)

FAULT_SYS[DRST] = 1 Digital reset by the wake tone

*FAULT\_COMM3\[FCOMM\_DET\] * $$ = 1 $$ *\[DRST\]* = 1 from the upper device

Top of stack device FAULT_SYS[DRST] = 1 Digital reset by the wake tone **POR ** **(Transition)**

# BAT

# AVAO

# LDOIN

# CVDD

# AVDD

# DVDD

# Min V BAT

# Min V CVDDUV

# Min V AVDDUV

# SHUTDOWN Mode **ACTIVE Mode** **Received WAKE ** **ping/tone** **Ready to receive WAKE ** **ping/tone** **Comm** **time** **WAKE tone send to ** **next device**

# SU(WAKE\_SHUT) **Transition** Comm not available Comm available

# RST **Battery insertion**

## Figure 8-60. SHUTDOWN to ACTIVE Mode Transition **8.4.1.1.2 Enter SHUTDOWN Mode**

## During normal operation, host puts the device in SHUTDOWN mode through communication by sending

*CONTROL1\[GOTO\_SHUTDOWN\]* = 1. In a daisy chain configuration, using broadcast write to send this command will put all devices in the daisy chain in SHUTDOWN mode.

## The device can also enter SHUTDOWN mode by one of the following conditions **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## • • Communication timeout: automatically transitions from ACTIVE mode to SHUTDOWN mode if there

is no valid communication for the configured time. Host can enable this option through the *COMM\_TIMEOUT\_CONF* register. - • SLEEP mode timeout: automatically transitions from SLEEP mode to SHUTDOWN mode if  device is in SLEEP mode for the configured time. Host can enable this option through *PWR\_TRANSIT\_CONF\[SLP\_TIME2:0\]*. - • Upon balancing completion: automatically enter SHUTDOWN mode when all balancing of the devices is  completed. See Section 8.3.3 for details. This option can result with devices in different power modes for a period of time in a daisy chain configuration. - • Thermal shutdown: shuts down the device when the internal die temperature is greater than T SHUT - • SHUTDOWN or HW\_RESET ping/tone: These pings/tones are used as a recovery attempt on a loss  communication situation. A SHUTDOWN ping/tone puts the device into SHUTDOWN mode without using communication, forcing most of the circuits to be off. A more aggressive recovery attempt uses HW\_RESET ping/tone which turns off all circuits except a bandgap and restarts the device in SHUTDOWN mode.

## 8.4.1.2 SLEEP Mode

## This is the low power operation mode. In SLEEP mode, all internal power supplies are still on, but functions are

limited to cell balancing, OVUV and OTUT protectors, Heartbeat/Fault Tone/NFAULT transmission and detection. **8.4.1.2.1 Exit SLEEP Mode**

## Because host cannot communicate to the device, to exit SLEEP mode, host must send either a WAKE ping/tone

or SLEEPtoACTIVE ping/tone to transition to ACTIVE mode. A WAKE wakes up and resets the device, which host will need to reconfigure the device setting; a SLEEPtoACTIVE only wakes up the device. **8.4.1.2.2 Enter SLEEP Mode**

## The device can enter SLEEP mode from ACTIVE mode only. During normal operation, host puts the device

to SLEEP mode through communication by sending *CONTROL1\[GOTO\_SLEEP\]* = 1. In a daisy chain configuration, using broadcast write to send this command will put all devices into SLEEP mode.

## The device can also enter SLEEP mode in the following condition

- • Communication timeout: automatically transitions from ACTIVE mode to SLEEP mode if there is no valid  communication for the configured time. Host can enable this option through the *COMM\_TIMEOUT\_CONF * register.

# AVDD

# DVDD **Comm** **Received WAKE ping/tone**

**SLEEPtoACTIVE tone send to ** **next device** **SLEEP ** **Mode** **Start Device reset**

# ACTIVE Mode **time**

# SU(WAKE\_SLP) **Transition** Comm available Comm not available

# RST

# CVDD

# AVDD

# DVDD **Comm**

| Received SLEEPtoACTIVE | ping/tone |
|:--- |:--- |
| SLEEPtoACTIVE tone send to | next device |
| SLEEP | Mode |

**SLEEPtoACTIVE tone send to ** **next device** **SLEEP ** **Mode** **Start Device reset**

# ACTIVE Mode **time**

# SU(SLP2ACT) **Transition** Comm available Comm not available

# CVDD

**(a) Waking up with WAKE ping/tone** **(b) Waking up with SLEEPtoACTIVE ping/tone**

## Figure 8-61. SLEEP to ACTIVE Mode Transition

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

# 8.4.1.3 ACTIVE Mode

This is the operation mode with full functionality support. Host can communicate to the device with full control on various features as well as performance diagnostic in this mode. **8.4.1.3.1 Exit ACTIVE Mode**

From ACTIVE mode, device can enter SLEEP mode or SHUTDOWN mode through command, ping/tone, timer, or specific event. See Section 8.4.1.1 and Section 8.4.1.2 for details.

**8.4.1.3.2 Enter ACTIVE Mode from SHUTDOWN Mode**

The device can transition to ACTIVE mode from SHUTDOWN mode only through a WAKE ping/tone. Once in ACTIVE mode, the host clears some of the reset-related faults that are expected faults (see Section 8.4.1.1 for details), indicating a POR on certain blocks due to the transition from SHUTDOWN mode to ACTIVE mode. Registers are reset to default; the OTP shadow registers are reloaded with the OTP programmed values.

**8.4.1.3.3 Enter ACTIVE Mode from SLEEP Mode**

From SLEEP mode, either a WAKE or SLEEPtoACTIVE ping/tone can put the device in ACTIVE mode. A WAKE ping/tone generates a digital reset to the device. Because the LDO supplies remain on during SLEEP mode, only the *FAULT\_SYS\[DRST\]* = 1 is set, indicating a digital reset has occurred. Certain expected faults related to being reset are set. See SHUTDOWN mode for details. Registers are reset to default, the OTP shadow registers are reloaded with the OTP programmed values.

If a SLEEPtoACTIVE ping/tone is used to wake up the device from SLEEP mode to ACTIVE mode, the device enters ACTIVE mode without a digital reset, but the UART engine is reset; therefore, in the base device, the *FAULT\_COMM1\[COMMCLR\_DET\]* = 1 and the host clears it after entering ACTIVE mode. **8.4.2 Device Reset**

There are several conditions which the device will go through: a digital reset, putting the registers to their default settings and reloading the OTP. - • A WAKE ping/tone is sent to transition from SHUTDOWN mode or SLEEP mode to ACTIVE mode. - • A WAKE ping/tone is received in ACTIVE mode. - • The *CONTROL1\[SOFT\_RESET\]* = 1 command is sent in ACTIVE mode. - • A HW\_RESET ping/tone is sent under any power mode. This generates a POR-like event to the device.  Upon the detection of a HW\_RESET ping/tone, the device will turn off all internal blocks except a bandgap for t HWRST duration. Afterward, the device will restart in SHUTDOWN mode. - • Internal power supply faults. See Section 8.3.6.4 for details. - - AVDD UV, DVDD UV is detected. - • A HFO or LFP watchdog fault will reset the digital.

Apart from the full reset cases, the following conditions will only reset the UART engine. These conditions mainly affect the base device because UART is used to talk to the host MCU. In the base device, the *FAULT\_COMM1\[COMMCLR\_DET\]* = 1 will be set. These conditions do not affect the stack devices because UART is inactive in those devices. - • A SLEEPtoACTIVE ping is sent to transition from SLEEP mode to ACTIVE mode. - • The following conditions not only clear the UART engine and set the *\[COMMCLR\_DET\]* = 1, they also set  *FAULT\_COMM1\[STOP\_DET\]* = 1 as an indication that an unexpected UART STOP is detected. - - A SLEEPtoACTIVE ping is sent in ACTIVE mode. - - A COMM CLEAR signal is sent. This is a dedicated signal to clear the UART engine and instruct the  engine to look for a new start of communication frame. See Section 8.3.6.1.1.1 for more details. **8.4.3 Ping and Tone**

In the noncommunicable conditions, such as in SHUTDOWN or SLEEP mode, or in the loss of communication situations when host would send an instruction for a reset or power down as a communication recovery attempt, a Ping or Tone is a form of communication to the device for a specific action. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## Table 8-36. Supported Ping and Tone in Different Power Modes

**Ping/Tone Detection** **Detected Pin(s)** **SHUTDOWN** **SLEEP** **ACTIVE**

# SHUTDOWN ping RX √ √ SLEEPtoACTIVE ping RX √ √ WAKE ping RX √ √ √

| HW\_RESET ping | RX | √ | √ |
|:--- |:--- |:--- |:--- |
| SHUTDOWN tone | COMH/L | √ | √ |
| SLEEPtoACTIVE tone | COMH/L | √ | √ |

# SHUTDOWN tone COMH/L √ √

# SLEEPtoACTIVE tone COMH/L √ √ WAKE tone COMH/L √ √ √

# HW\_RESET tone COMH/L √ √

Fault tone COMH/L √ Only fault tone detection is available.

# HEARTBEAT COMH/L √

## 8.4.3.1 Ping

## A ping is a specific high-low-high signal to the RX pin of the device. Ping is used on the base device as only the

base device is connected to the host which the UART RX is accessible. The device detects different low times of the ping signal to differentiate the different ping signals.

## The communication pings are referring to the WAKE ping, SLEEPtoACTIVE ping, SHUTDOWN ping, and

HW\_RESET ping. These pings instruct the device to a specific power mode when normal communication is not available. By definition, a COMM CLEAR signal on the RX pin is a form of a ping. Because a COMM\_CLR is to clear the UART engine, this signal is covered in Section 8.3.6.1.1.1. RX High Ping duration

# SLEEPtoACTIVE

# WAKE

# SHUTDOWN

# HW\_RESET 5HWXUQ ³KLJK´IRUQH\[W operation

Host shall release the RX line after applying the HW\_RESET ping

# UART(StA)

# HLD\_WAKE

# HLD\_SD

# HLD\_HWRST

## Figure 8-62. Communication Pings

## 8.4.3.2 Tone

## A tone is a fixed number of couplets (pulses) with a specified polarity (all "+" or all "-") sent through the

differential vertical interface COMH and COML ports. Tone is used on stack devices as only the COMH/L ports are accessible. The number of couplets for transmission is always greater than the number of couplets needed for detection.

## There are four communication tones corresponding to the four communication pings. They are WAKE tone,

SLEEPtoACTIVE tone, SHUTDOWN tone, and HW\_RESET tone. In addition to the communication tones, there are two extra tones related to device fault status: Heartbeat tone and Fault tone. These two fault status tones are only available in SLEEP mode. See Section 8.3.6.2.3.3 for details.

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

Wake and SLEEP-to-ACTIVE Couplets ( DOO ³ + ´ SXOVHV )

# SHUTDOWN and HW\_RESET Couplets ( DOO ³ - ³ SXOVHV )

# CVDD/2

# CVDD

# CVSS

# CVDD

# CVSS

# COM\*P \\pm COMP\*N

# COM\*P

# COM\*N

# COM\*P \\pm COMP\*N

# COM\*P

# COM\*N

# COMMTONE

# WAKE TONE DETECTION

# n WAKE ³ + ´ 3XOVHV COM\*P,COM\*N WAKEUP\_DET (internal signal)

# n SLPtoACT ³ + ´ 3XOVHV

# SLEEP TO ACTIVE TONE DETECTION

# COMXP, COMXN

# SLP2ACT\_DET

# n SHDN ³ - ´ 3XOVHV

# SHUTDOWN TONE DETECTION

# COMXP, COMXN

# HWRST\_DET

# n HWRST ³ - ´ 3XOVHV

# HW\_RESET TONE DETECTION

# COMXP, COMXN

# HWRST\_DET n HWRSTDET Pulses n SHDNDET Pulses n SLPtoACTDET Pulses n WAKEDET Pulses

# COMTONE

# CVDD/2

# TONE\_HI

# TONE\_LO A pulse

# COMTONE\_LO

# COMTONE\_HI

# Figure 8-63. Communication Tones

# 8.4.3.3 Ping and Tone Propagation

# Propagates

# The WAKE and SLEEPtoACTIVE pings/tones are part of the normal operation to wake up the device; hence,

these two pings/tones can propagate to the next device in a daisy chain configuration. That is, when a device receives a WAKE ping/tone, it generates a WAKE tone and forwards it to the next device. Similar action applies to SLEEPtoACTIVE ping/tone.

# The direction of the tone forwarding follows the communication direction, which is set by the

*CONTROL1\[DIR\_SEL\]* bit. See Section 8.3.6.1 for more details. The detection of the tone is supported from the COMH and COML ports on stack devices regardless of the *\[DIR\_SEL\]* setting. This does not apply to base device because base device detects pings instead.

# During normal operation, host can simply send a WAKE or SLEEPtoACTIVE ping to the base device and the

corresponding tone will be generated to the rest of the stack devices. During system development, if there is a need to send WAKE or SLEEPtoACTIVE to only some of the devices in the daisy chain, host can use the *CONTROL1\[SEND\_WAKE\]* or *CONTROL1\[SEND\_SLPTOACT\]* bit. Device that receives this command will send the corresponding tone to the next device in the daisy chain. Because the WAKE and SLEEPtoACTIVE tones propagate, the rest of the daisy chain connected above also receives the corresponding tone.

# Does Not Propagate

# The SHUTDOWN and HW\_RESET pings/tones are mostly used as a communication recovery attempt. Hence

these pings/tones do not propagate. That is, when a device receives a SHUTDOWN ping/tone, it starts the shutdown process but the device does not generate another SHUTDOWN tone to the next device. Similar action applies to HW\_RESET ping/tone.

# For a base device, as RX pin is connected to the host, SHUTDOWN or HW\_RESET ping can be used on the

base device. For stack devices, it is required at least one stack device is connected to the problem device is communicable. Host has to talk to the neighboring device and sets the *CONTROL1\[SEND\_SHUTDOWN\]* = 1 or *CONTROL2\[SEND\_HW\_RESET\]* = 1 to instruct the neighboring device to issue the corresponding tone to the problem device. The detection of the tone is supported from the COMH and COML ports on stack devices

# www.ti.com

# BQ79616 SLUSF21 - JUNE 2023

# Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## regardless of the \[DIR\_SEL\] setting. This does not apply to a base device because a base device detects pings instead.

## Table 8-37. Ping and Tone Propagation Summary

| Ping/Tone | Propagable | Non-Propagable |
|:--- |:--- |:--- |
| WAKE | Receiving device will generate a WAKE tone to the | next device |
| SLEEPtoACTIVE | Receiving device will generate a SLEEPtoACTIVE | tone to the next device |

WAKE Receiving device will generate a WAKE tone to the next device

SLEEPtoACTIVE Receiving device will generate a SLEEPtoACTIVE tone to the next device

SHUTDOWN Receiving device will initialize the shutdown process

HW\_RESET Receiving device will initialize the HW reset process

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## 8.5 Register Maps

## This section has three register map summary tables with registers listed per the order of the register address

- • The NVM (OTP) shadow registers. These read/write-able shadow registers are reset with OTP values  programmed in the customer OTP space. To program the custom OTP space, host writes the desired values to these OTP shadow registers and follows the programming procedure. These registers are included in the OTP CRC check. If customer OTP space is not programmed. The shadow registers are loaded with factory configuration default value. If the OTP (either factory configuration default or value programmed in customer OTP space) is failing to load after a device reset, the shadow registers will be loaded with the hardware reset default value instead. The hardware reset default value and the factory configuration default values are the same for the majority of the OTP shadow registers. Only the *DIR0\_ADDR\_OTP, DIR1\_ADD\_OTP*, *PWR\_TRANSIT\_CONF*, *CUST\_CRC\_HI/LO* registers have a reset value versus factory default, and are specified in Section 8.5.1 and their register field descriptions. - • The Read/Write registers. These are registers that the host can read/write to during runtime. A device reset  will put these registers back to their reset value. - • The Read registers. These are registers that the host only has read access. A device reset will put these  registers back to their reset value.

## The register summary tables use the following key

- • Addr = Register address - • Hex = Hexidecimal value - • NVM = Non-volatile memory (OTP) shadow registers - • RSVD = Reserved. Reserved register addresses or bits are not implemented in the device. Any write to these  bits is ignored. Reads to these bits always return 0. - • OTP\_SPARE: These are spare OTP and shadow register bits that are implemented in the device. These  spare bits are included as part of the CRC calculation. These bits are read/write as normal, but do not perform any function or influence any device behaviors. - • OTP\_RSVDn = OTP and shadowed registers that are implemented but are reserved for device internal  usage, where n refers to the register address. MCU must keep these registers in their default value - • HW Reset default is the value loaded when digital resets (POR like event) whereas Factory Configuration  Default is the default value loaded into the OTP cell if customer doesn't program it themselves. Customer cannot read the HW Reset value.

## Section 8.5.4 describes the definition of each bit in the registers. The registers in this section are grouped per functional blocks.

## 8.5.1 OTP Shadow Register Summary

| Register | Name |
|:--- |:--- |
| Addr | Hex |
| RW | Type |
| Reset | Value | **Addr ** **Hex** **RW ** **Type** **Reset ** **Value** **Data**

**Bit7** **Bit6** **Bit5** **Bit4** **Bit3** **Bit2** **Bit1** **Bit0**

# DIR0\_ADDR \_OTP

NVM HW Reset Default = 0x00 Factory Configurati on Default $$ = 0x01 $$

# SPARE\[1:0\] ADDRESS\[5:0\]

# DIR1\_ADDR \_OTP

NVM HW Reset Default = 0x00 Factory Configurati on Default $$ = 0x01 $$

# SPARE\[1:0\] ADDRESS\[5:0\]

# DEV\_CONF NVM 0x54 RSVD NO\_ADJ \_CB

# MULTI DROP

# \_EN

# FCOMM \_EN

# TWO\_ STOP \_EN

# NFAULT \_EN

# FTONE

# \_EN

# HB\_EN **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

| Register | Name |
|:--- |:--- |
| Addr | Hex |
| RW | Type |
| Reset | Value | **Addr ** **Hex** **RW ** **Type** **Reset ** **Value** **Data**

**Bit7** **Bit6** **Bit5** **Bit4** **Bit3** **Bit2** **Bit1** **Bit0**

# ACTIVE\_CE LL

NVM HW Reset Default = 0x00 Factory Configurati on Default $$ = 0x0A $$

# SPARE\[3:0\] NUM\_CELL\[3:0\]

# OTP\_SPARE

# NVM 0x00 SPARE\[7:0\]

# BBVC\_POS N1

# NVM

0x00 CELL16 CELL15 CELL14 CELL13 CELL12 CELL11 CELL10 CELL9

# BBVC\_POS N2

# NVM

0x00 CELL8 CELL7 CELL6 CELL5 CELL4 CELL3 CELL2 CELL1

# ADC\_CONF

# NVM

0x00 AUX\_SETTLE\[1:0\] LPF\_BB\[2:0\] LPF\_VCELL\[2:0\]

# ADC\_CONF

# NVM 0x00 SPARE\[1:0\] ADC\_DLY\[5:0\]

# OV\_THRES H

# NVM 0x3F SPARE SPARE OV\_THR\[5:0\]

# UV\_THRES H

# A NVM 0x00 SPARE SPARE UV\_THR\[5:0\]

# OTUT\_THR ESH

# B NVM 0xE0 UT\_THR\[2:0\] OT\_THR\[4:0\]

# UV\_DISABL E1

# C

NVM 0x00 CELL16 CELL15 CELL14 CELL13 CELL12 CELL11 CELL10 CELL9

# UV\_DISABL E2

# D

NVM 0x00 CELL8 CELL7 CELL6 CELL5 CELL4 CELL3 CELL2 CELL1

# GPIO\_CONF

# E NVM 0x00 FAULT\_ IN\_EN

# SPI\_EN GPIO2\[2:0\] GPIO1\[2:0\]

# GPIO\_CONF

# F

NVM 0x00 SPARE SPARE GPIO4\[2:0\] GPIO3\[2:0\]

# GPIO\_CONF

# NVM 0x00 SPARE\[1:0\] GPIO6\[2:0\] GPIO5\[2:0\]

# GPIO\_CONF

# NVM 0x00 SPARE\[1:0\] GPIO8\[2:0\] GPIO7\[2:0\]

# OTP\_SPARE

# NVM 0x00 SPARE\[7:0\]

# OTP\_SPARE

# NVM 0x00 SPARE\[7:0\]

# OTP\_SPARE

# NVM 0x00 SPARE\[7:0\]

# OTP\_SPARE

# NVM 0x00 SPARE\[7:0\]

# FAULT\_MSK

# NVM

0x00 MSK\_ PROT MSK\_UT MSK\_OT MSK\_UV MSK\_OV MSK\_ COMP

# MSK\_ SYS

# MSK\_ PWR

# FAULT\_MSK

# NVM 0x00 SPARE\[1\] MSK\_ OTP\_ CRC

| MSK\_ | OTP\_ | DATA |
|:--- |:--- |:--- |
| MSK\_ | COMM3 | \_FCOMM |
| MSK\_ | COMM3 | \_FTONE |

# MSK\_ COMM3 \_FCOMM

# MSK\_ COMM3 \_FTONE

# MSK\_ COMM3

# \_HB

| MSK\_ | COMM2 |
|:--- |:--- |
| MSK\_ | COMM1 |
| PWR\_TRAN | SIT\_CONF |

# MSK\_ COMM1

# PWR\_TRAN SIT\_CONF

NVM HW Reset Default = 0x18 Factory Configurati on Default $$ = 0x10 $$

# SPARE\[2:0\] TWARN\_THR\[1:0\] SLP\_TIME\[2:0\]

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

| Register | Name |
|:--- |:--- |
| Addr | Hex |
| RW | Type |
| Reset | Value | **Addr ** **Hex** **RW ** **Type** **Reset ** **Value** **Data**

**Bit7** **Bit6** **Bit5** **Bit4** **Bit3** **Bit2** **Bit1** **Bit0**

# COMM\_TIM EOUT\_CON F

# NVM

0x00 SPARE CTS\_TIME\[2:0\] CTL\_ ACT CTL\_TIME\[2:0\]

# TX\_HOLD\_ OFF

# 1A NVM 0x00 DLY\[7:0\]

# MAIN\_ADC\_ CAL1

# 1B NVM 0x00 GAINL\[7:0\]

# MAIN\_ADC\_ CAL2

# 1C NVM 0x00 GAINH OFFSET\[6:0\]

# AUX\_ADC\_ CAL1

# 1D NVM 0x00 GAINL\[7:0\]

# AUX\_ADC\_ CAL2

# 1E NVM 0x00 GAINH OFFSET\[6:0\]

# OTP\_RSVD 1F

# 1F

NVM 0x00 INTERNAL USE. DO NOT WRITE TO THIS ADDRESS

# OTP\_RSVD

| NVM | 0x00 | INTERNAL USE. DO NOT WRITE TO THIS ADDRESS |
|:--- |:--- |:--- |
| CUST\_MISC | 1 through | CUST\_MISC |
| NVM | 0x00 | DATA\[7:0\] |
| NVM | 0x00 | DATA\[7:0\] |
| NVM | 0x00 | DATA\[7:0\] |
| NVM | 0x00 | DATA\[7:0\] |
| NVM | 0x00 | DATA\[7:0\] |
| NVM | 0x00 | DATA\[7:0\] |
| NVM | 0x00 | DATA\[7:0\] |
| NVM | 0x00 | DATA\[7:0\] | CUST\_MISC 1 through CUST\_MISC

# NVM 0x00 DATA\[7:0\]

# NVM 0x00 DATA\[7:0\]

# NVM 0x00 DATA\[7:0\]

# NVM 0x00 DATA\[7:0\]

# NVM 0x00 DATA\[7:0\]

# NVM 0x00 DATA\[7:0\]

# NVM 0x00 DATA\[7:0\]

# NVM 0x00 DATA\[7:0\]

# STACK\_RES PONSE

# NVM 0x00 SPARE\[1:0\] DELAY\[5:0\]

# BBP\_LOC 2A NVM 0x00 SPARE\[2:0\] LOC\[4:0\]

# OTP\_RSVD 2B

# 2B

NVM 0x00 INTERNAL USE. DO NOT WRITE TO THIS ADDRESS

# OTP\_SPARE

# 2C NVM 0x00 SPARE\[7:0\]

# OTP\_SPARE

# 2D NVM 0x00 SPARE\[7:0\]

# OTP\_SPARE

# 2E NVM 0x00 SPARE\[7:0\]

# OTP\_SPARE

# 2F NVM 0x00 SPARE\[7:0\]

# OTP\_SPARE

# NVM 0x00 SPARE\[7:0\]

# OTP\_SPARE

# NVM 0x00 SPARE\[7:0\]

# OTP\_SPARE

# NVM 0x00 SPARE\[7:0\]

# OTP\_SPARE

# NVM 0x00 SPARE\[7:0\]

# OTP\_SPARE

# NVM 0x00 SPARE\[7:0\]

# OTP\_SPARE

# NVM 0x00 SPARE\[7:0\] **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

| Register | Name |
|:--- |:--- |
| Addr | Hex |
| RW | Type |
| Reset | Value | **Addr ** **Hex** **RW ** **Type** **Reset ** **Value** **Data**

**Bit7** **Bit6** **Bit5** **Bit4** **Bit3** **Bit2** **Bit1** **Bit0**

# CUST\_CRC \_HI

NVM HW Reset Default = 0x57 Factory Configurati on Default $$ = 0x31 $$

# CRC\[7:0\]

# CUST\_CRC \_LO

NVM HW Reset Default = 0x89 Factory Configurati on Default $$ = 0xF3 $$

# CRC\[7:0\]

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## 8.5.2 Read/Write Register Summary **Register Name** **Addr ** **Hex** **RW ** **Type** **Reset ** **Value** **Data**

**Bit7** **Bit6** **Bit5** **Bit4** **Bit3** **Bit2** **Bit1** **Bit0**

# OTP\_PROG\_UNL OCK1A through OTP\_PROG\_UNL OCK1D

| RW | 0x00 | CODE\[7:0\] |
|:--- |:--- |:--- |
| RW | 0x00 | CODE\[7:0\] |
| RW | 0x00 | CODE\[7:0\] |
| RW | 0x00 | CODE\[7:0\] |

# RW 0x00 CODE\[7:0\]

# RW 0x00 CODE\[7:0\]

# RW 0x00 CODE\[7:0\]

| DIR0\_ADDR | RW | 0x00 | RSVD | ADDRESS\[5:0\] |
|:--- |:--- |:--- |:--- |:--- |
| DIR1\_ADDR | RW | 0x00 | RSVD | ADDRESS\[5:0\] |
| COMM\_CTRL | RW | 0x00 | RSVD | STACK\_ |

# DIR1\_ADDR RW 0x00 RSVD ADDRESS\[5:0\]

# COMM\_CTRL RW 0x00 RSVD STACK\_

# DEV

# TOP\_ STACK

# CONTROL1 RW 0x00 DIR\_SEL SEND\_ SHUT DOWN

# SEND\_ WAKE

# SEND\_ SLPTO ACT

# GOTO\_ SHUT DOWN

# GOTO\_ SLEEP

# SOFT\_ RESET

# ADDR\_

# WR

# CONTROL2 30A RW 0x00 RSVD SEND\_

| HW\_ | RESET |
|:--- |:--- |
| TSREF | \_EN |
| OTP\_PROG\_CTR | L |

# TSREF \_EN

# OTP\_PROG\_CTR L

# 30B RW 0x00 RSVD PAGE SEL

# PROG \_GO

# ADC\_CTRL1 30D RW 0x00 RSVD RSVD LPF\_BB

# \_EN

# LPF\_ VCELL\_ EN

# MAIN\_GO MAIN\_MODE\[1:0\]

# ADC\_CTRL2 30E RW 0x00 RSVD AUX\_CEL L\_ALIGN

# AUX\_CELL\_SEL\[4:0\]

# ADC\_CTRL3

30F RW 0x00 RSVD AUX\_GPIO\_SEL\[3:0\] AUX\_GO AUX\_MODE\[1:0\]

# REG\_INT\_RSVD

RW 0x00 INTERNAL USE. DO NOT WRITE TO THIS ADDRESS

# CB\_CELL16\_CTR L through CB\_CELL1\_CTRL

# RW 0x00 RSVD TIME\[4:0\]

# RW 0x00 RSVD TIME\[4:0\]

| 31A | RW | 0x00 | RSVD | TIME\[4:0\] |
|:--- |:--- |:--- |:--- |:--- |
| 31B | RW | 0x00 | RSVD | TIME\[4:0\] |
| 31C | RW | 0x00 | RSVD | TIME\[4:0\] |
| 31D | RW | 0x00 | RSVD | TIME\[4:0\] |
| 31E | RW | 0x00 | RSVD | TIME\[4:0\] |
| 31F | RW | 0x00 | RSVD | TIME\[4:0\] |

# 31B RW 0x00 RSVD TIME\[4:0\]

# 31C RW 0x00 RSVD TIME\[4:0\]

# 31D RW 0x00 RSVD TIME\[4:0\]

# 31E RW 0x00 RSVD TIME\[4:0\]

# 31F RW 0x00 RSVD TIME\[4:0\]

| RW | 0x00 | RSVD | TIME\[4:0\] |
|:--- |:--- |:--- |:--- |
| RW | 0x00 | RSVD | TIME\[4:0\] |
| RW | 0x00 | RSVD | TIME\[4:0\] |
| RW | 0x00 | RSVD | TIME\[4:0\] |
| RW | 0x00 | RSVD | TIME\[4:0\] |
| RW | 0x00 | RSVD | TIME\[4:0\] |
| RW | 0x00 | RSVD | TIME\[4:0\] |
| RW | 0x00 | RSVD | TIME\[4:0\] |

# RW 0x00 RSVD TIME\[4:0\]

# RW 0x00 RSVD TIME\[4:0\]

# RW 0x00 RSVD TIME\[4:0\]

# RW 0x00 RSVD TIME\[4:0\]

# RW 0x00 RSVD TIME\[4:0\]

# RW 0x00 RSVD TIME\[4:0\]

# RW 0x00 RSVD TIME\[4:0\]

# VMB\_DONE\_THR ESH

# RW 0x3F RSVD MB\_THR\[5:0\]

# MB\_TIMER\_CTRL RW 0x00 RSVD TIME\[4:0\]

# VCB\_DONE\_THR ESH

# 32A RW 0x00 RSVD CB\_THR\[5:0\]

# OTCB\_THRESH

32B RW 0x0F RSVD COOLOFF\[2:0\] OTCB\_THR\[3:0\] **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* **Register Name** **Addr ** **Hex** **RW ** **Type** **Reset ** **Value** **Data**

**Bit7** **Bit6** **Bit5** **Bit4** **Bit3** **Bit2** **Bit1** **Bit0**

# OVUV\_CTRL 32C RW 0x00 VCB DONE \_THR \_LOCK

# OVUV\_LOCK\[3:0\] OVUV \_GO

# OVUV\_MODE\[1:0\]

# OTUT\_CTRL 32D RW 0x00 RSVD OTCB\_ THR\_ LOCK

# OTUT\_LOCK\[2:0\] OTUT \_GO

# OTUT\_MODE\[1:0\]

# BAL\_CTRL1 32E RW 0x00 RSVD DUTY\[2:0\]

# BAL\_CTRL2 32F RW 0x00 RSVD CB\_ PAUSE

# FLTSTOP \_EN

# OTCB\_ EN

# BAL\_ACT\[1:0\] BAL\_GO AUTO\_ BAL

# BAL\_CTRL3

RW 0x00 RSVD BAL\_TIME\_SEL\[3:0\] BAL\_TIM E\_GO

# FAULT\_RST1 RW 0x00 RST\_ PROT

# RST\_UT RST\_OT RST\_UV RST\_OV RST\_ COMP

# RST\_SYS RST\_ PWR

# FAULT\_RST2 RW 0x00 RSVD RST\_OTP \_CRC

# RST\_OTP \_DATA

# RST\_ COMM3\_

# FCOMM

# RST\_ COMM3\_

# FTONE

# RST\_ COMM3\_

# HB

# RST\_ COMM2

# RST\_ COMM1

# DIAG\_OTP\_CTRL RW 0x00 RSVD FLIP\_ FACT\_ CRC

# MARGIN\_MODE\[2:0\] MARGIN \_GO

# DIAG\_COMM\_CT RL

# RW 0x00 RSVD SPI\_ LOOP BACK

# FLIP\_TR \_CRC

# DIAG\_PWR\_CTRL RW 0x00 RSVD BIST\_ NO\_RST

# PWR\_ BIST\_GO

# DIAG\_CBFET\_CT RL1

# RW

0x00 CBFET16 CBFET15 CBFET14 CBFET13 CBFET12 CBFET11 CBFET10 CBFET9

# DIAG\_CBFET\_CT RL2

# RW

0x00 CBFET8 CBFET7 CBFET6 CBFET5 CBFET4 CBFET3 CBFET2 CBFET1

# DIAG\_COMP\_CT RL1

# 33A RW 0x00 VCCB\_THR\[4:0\] BB\_THR\[2:0\]

# DIAG\_COMP\_CT RL2

# 33B RW 0x00 RSVD GPIO\_THR\[2:0\] OW\_THR\[3:0\]

# DIAG\_COMP\_CT RL3

# 33C RW 0x00 RSVD CBFET\_C TRL\_GO

# OW\_SNK\[1:0\] COMP\_ADC\_SEL\[2:0\] COMP\_ ADC\_GO

# DIAG\_COMP\_CT RL4

# 33D RW 0x00 RSVD COMP\_ FAULT \_INJ

# LPF\_ FAULT \_INJ

# DIAG\_PROT\_CTR L

# 33E RW 0x00 RSVD PROT\_ BIST\_ NO\_RST

# OTP\_ECC\_DATAI N1 through OTP\_ECC\_DATAI N9

| RW | 0x00 | DATA\[7:0\] |
|:--- |:--- |:--- |
| RW | 0x00 | DATA\[7:0\] |
| RW | 0x00 | DATA\[7:0\] |
| RW | 0x00 | DATA\[7:0\] |
| RW | 0x00 | DATA\[7:0\] |
| RW | 0x00 | DATA\[7:0\] |
| RW | 0x00 | DATA\[7:0\] |

# RW 0x00 DATA\[7:0\]

# RW 0x00 DATA\[7:0\]

# RW 0x00 DATA\[7:0\]

# RW 0x00 DATA\[7:0\]

# RW 0x00 DATA\[7:0\]

# RW 0x00 DATA\[7:0\]

# 34A RW 0x00 DATA\[7:0\]

# 34B RW 0x00 DATA\[7:0\]

# OTP\_ECC\_TEST 34C RW 0x00 RSVD DED\_ SEC

# MANUAL \_AUTO

# ENC\_ DEC

# ENABLE

# SPI\_CONF 34D RW 0x00 RSVD CPOL CPHA NUMBIT\[4:0\]

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated **Register Name** **Addr ** **Hex** **RW ** **Type** **Reset ** **Value** **Data**

**Bit7** **Bit6** **Bit5** **Bit4** **Bit3** **Bit2** **Bit1** **Bit0**

# SPI\_TX3, SPI\_TX2, and SPI\_TX1

# 34E RW 0x00 DATA\[7:0\]

# 34F RW 0x00 DATA\[7:0\]

# RW 0x00 DATA\[7:0\]

# SPI\_EXE RW 0x02 RSVD SS\_CTRL SPI\_GO

# OTP\_PROG\_UNL OCK2A through OTP\_PROG\_UNL OCK2D

| RW | 0x00 | CODE\[7:0\] |
|:--- |:--- |:--- |
| RW | 0x00 | CODE\[7:0\] |
| RW | 0x00 | CODE\[7:0\] |
| RW | 0x00 | CODE\[7:0\] |

# RW 0x00 CODE\[7:0\]

# RW 0x00 CODE\[7:0\]

# RW 0x00 CODE\[7:0\]

# DEBUG\_CTRL\_U NLOCK

# RW 0x00 CODE\[7:0\]

# DEBUG\_COMM\_ CTRL1

# RW 0x04 RSVD UART\_ BAUD

# UART\_ MIRROR \_EN

# UART\_ TX\_EN

# USER\_ UART\_ EN

# USER\_ DAISY \_EN

# DEBUG\_COMM\_ CTRL2

# RW 0x0F RSVD COML\_ TX\_EN

# COML\_ RX\_EN

# COMH\_ TX\_EN

# COMH\_ RX\_EN

## 8.5.3 Read-Only Register Summary **Register Name** **Addr ** **Hex** **RW ** **Type** **Reset ** **Value** **Data**

**Bit7** **Bit6** **Bit5** **Bit4** **Bit3** **Bit2** **Bit1** **Bit0**

# PARTID R 0x00 REV\[7:0\]

# DEV\_REVID E00 R 0x00 DEV\_REVID\[7:0\] DIE\_ID1 through DIE\_ID9

| R | 0x00 | ID\[7:0\] |
|:--- |:--- |:--- |
| R | 0x00 | ID\[7:0\] |
| R | 0x00 | ID\[7:0\] |
| R | 0x00 | ID\[7:0\] |
| R | 0x00 | ID\[7:0\] |
| R | 0x00 | ID\[7:0\] |
| R | 0x00 | ID\[7:0\] |
| R | 0x00 | ID\[7:0\] |
| R | 0x00 | ID\[7:0\] |

# R 0x00 ID\[7:0\]

# R 0x00 ID\[7:0\]

# R 0x00 ID\[7:0\]

# R 0x00 ID\[7:0\]

# R 0x00 ID\[7:0\]

# R 0x00 ID\[7:0\]

# R 0x00 ID\[7:0\]

# R 0x00 ID\[7:0\]

# CUST\_CRC\_RSLT \_HI

# 50C R 0x31 CRC\[7:0\]

# CUST\_CRC\_RSLT \_LO

# 50D R 0xF3 CRC\[7:0\]

# OTP\_ECC\_DATA OUT1 through OTP\_ECC\_DATA OUT9

| R | 0x00 | DATA\[7:0\] |
|:--- |:--- |:--- |
| R | 0x00 | DATA\[7:0\] |
| R | 0x00 | DATA\[7:0\] |
| R | 0x00 | DATA\[7:0\] |
| R | 0x00 | DATA\[7:0\] |
| R | 0x00 | DATA\[7:0\] |
| R | 0x00 | DATA\[7:0\] |
| R | 0x00 | DATA\[7:0\] |
| R | 0x00 | DATA\[7:0\] |

# R 0x00 DATA\[7:0\]

# R 0x00 DATA\[7:0\]

# R 0x00 DATA\[7:0\]

# R 0x00 DATA\[7:0\]

# R 0x00 DATA\[7:0\]

# R 0x00 DATA\[7:0\]

# R 0x00 DATA\[7:0\]

# R 0x00 DATA\[7:0\]

# OTP\_PROG\_STA T

# R

0x00 UNLOCK OTERR UVERR OVERR SUVERR SOVERR PROG ERR

# DONE

# OTP\_CUST1\_STA T

# 51A R 0x00 LOADED LOAD WRN

# LOAD ERR

# FMTERR PROGOK UVOK OVOK TRY **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* **Register Name** **Addr ** **Hex** **RW ** **Type** **Reset ** **Value** **Data**

**Bit7** **Bit6** **Bit5** **Bit4** **Bit3** **Bit2** **Bit1** **Bit0**

# OTP\_CUST2\_STA T

# 51B R 0x00 LOADED LOAD WRN

# LOAD ERR

# FMTERR PROGOK UVOK OVOK TRY

| SPI\_RX3, | SPI\_RX2, and | SPI\_RX1 |
|:--- |:--- |:--- |
| R | 0x00 | DATA\[7:0\] |
| R | 0x00 | DATA\[7:0\] |
| R | 0x00 | DATA\[7:0\] |

# R 0x00 DATA\[7:0\]

# R 0x00 DATA\[7:0\]

# R 0x00 DATA\[7:0\]

# DIAG\_STAT R 0x00 RSVD DRDY\_ OTUT

# DRDY\_ OVUV

| DRDY\_ | BIST\_ | OTUT |
|:--- |:--- |:--- |
| DRDY\_ | BIST\_ | OVUV |
| DRDY\_ | BIST\_ | PWR |

# DRDY\_ BIST\_ OVUV

# DRDY\_ BIST\_ PWR

# ADC\_STAT1 R 0x00 RSVD RSVD DRDY\_ AUX\_ GPIO

| DRDY\_ | AUX\_ | CELL |
|:--- |:--- |:--- |
| DRDY\_ | AUX\_ | MISC |
| DRDY\_ | MAIN\_ | ADC |

# DRDY\_ AUX\_ MISC

# DRDY\_ MAIN\_ ADC

# ADC\_STAT2 R 0x00 RSVD DRDY\_ LPF

| DRDY\_ | GPIO |
|:--- |:--- |
| DRDY\_ | VCOW |
| DRDY\_ | CBOW |
| DRDY\_ | CBFET |
| DRDY\_ | VCCB |

# DRDY\_ VCOW

# DRDY\_ CBOW

# DRDY\_ CBFET

# DRDY\_ VCCB

# GPIO\_STAT

52A R 0x00 GPIO8 GPIO7 GPIO6 GPIO5 GPIO4 GPIO3 GPIO2 GPIO1

# BAL\_STAT 52B R 0x00 INVALID\_ CBCONF

# OT\_ PAUSE\_ DET

# CB\_ INPAUSE

# MB\_RUN CB\_RUN ABORT FLT

# MB\_ DONE

# CB\_ DONE

# DEV\_STAT 52C R 0x00 RSVD FACT\_ CRC\_ DONE

# CUST\_ CRC\_ DONE

# OTUT\_ RUN

# OVUV\_ RUN

# RSVD AUX\_ RUN

# MAIN\_ RUN

# FAULT\_SUMMAR Y

# 52D R 0x00 FAULT\_ PROT

# FAULT\_ COMP\_ ADC

| FAULT\_ | OTP |
|:--- |:--- |
| FAULT\_ | COMM |
| FAULT\_ | OTUT |
| FAULT\_ | OVUV |
| FAULT\_ | SYS |
| FAULT\_ | PWR |

# FAULT\_ COMM

# FAULT\_ OTUT

# FAULT\_ OVUV

# FAULT\_ SYS

# FAULT\_ PWR

# FAULT\_COMM1 R 0x00 RSVD UART\_TR UART\_ RR

# UART\_ RC

# COMM CLR\_ DET

# STOP\_ DET

# FAULT\_COMM2 R 0x00 COML\_ TR

| COML\_ | RR |
|:--- |:--- |
| COML\_ | RC |
| COML\_ | BIT |
| COMH\_ | TR |
| COMH\_ | RR |
| COMH\_ | RC |
| COMH\_ | BIT |

# COML\_ RC

# COML\_ BIT

# COMH\_ TR

# COMH\_ RR

# COMH\_ RC

# COMH\_ BIT

# FAULT\_COMM3 R 0x00 RSVD FCOMM \_DET

# FTONE \_DET

# HB\_FAIL HB\_FAST

# FAULT\_OTP R 0x00 RSVD DED\_ DET

# SEC\_DET CUST\_ CRC

| FACT\_ | CRC |
|:--- |:--- |
| CUSTLD | ERR |
| FACTLD | ERR |
| GBLOV | ERR |

# CUSTLD ERR

# FACTLD ERR

# GBLOV ERR

# FAULT\_SYS R 0x00 LFO RSVD GPIO DRST CTL CTS TSHUT TWARN

# FAULT\_PROT1 53A R 0x00 RSVD TPARITY \_FAIL

# VPARITY \_FAIL

# FAULT\_PROT2 53B R 0x00 RSVD BIST\_ ABORT

| TPATH | \_FAIL |
|:--- |:--- |
| VPATH | \_FAIL |
| UTCOMP | \_FAIL |
| OTCOMP | \_FAIL |
| OVCOMP | \_FAIL |
| UVCOMP | \_FAIL |

# VPATH \_FAIL

# UTCOMP \_FAIL

# OTCOMP \_FAIL

# OVCOMP \_FAIL

# UVCOMP \_FAIL

# FAULT\_OV1 53C R 0x00 OV16\_ DET

| OV15\_ | DET |
|:--- |:--- |
| OV14\_ | DET |
| OV13\_ | DET |
| OV12\_ | DET |
| OV11\_ | DET |
| OV10\_ | DET |

# OV14\_ DET

# OV13\_ DET

# OV12\_ DET

# OV11\_ DET

# OV10\_ DET

# OV9\_DET

# FAULT\_OV2

53D R 0x00 OV8\_DET OV7\_DET OV6\_DET OV5\_DET OV4\_DET OV3\_DET OV2\_DET OV1\_DET

# FAULT\_UV1 53E R 0x00 UV16\_ DET

| UV15\_ | DET |
|:--- |:--- |
| UV14\_ | DET |
| UV13\_ | DET |
| UV12\_ | DET |
| UV11\_ | DET |
| UV10\_ | DET |

# UV14\_ DET

# UV13\_ DET

# UV12\_ DET

# UV11\_ DET

# UV10\_ DET

# UV9\_DET

# FAULT\_UV2

53F R 0x00 UV8\_DET UV7\_DET UV6\_DET UV5\_DET UV4\_DET UV3\_DET UV2\_DET UV1\_DET

# FAULT\_OT

R 0x00 OT8\_DET OT7\_DET OT6\_DET OT5\_DET OT4\_DET OT3\_DET OT2\_DET OT1\_DET

# FAULT\_UT

R 0x00 UT8\_DET UT7\_DET UT6\_DET UT5\_DET UT4\_DET UT3\_DET UT2\_DET UT1\_DET

# FAULT\_COMP\_G PIO

# R 0x00 GPIO8\_ FAIL

| GPIO7\_ | FAIL |
|:--- |:--- |
| GPIO6\_ | FAIL |
| GPIO5\_ | FAIL |
| GPIO4\_ | FAIL |
| GPIO3\_ | FAIL |
| GPIO2\_ | FAIL |
| GPIO1\_ | FAIL |
| FAULT\_COMP\_V | CCB1 |

# GPIO6\_ FAIL

# GPIO5\_ FAIL

# GPIO4\_ FAIL

# GPIO3\_ FAIL

# GPIO2\_ FAIL

# GPIO1\_ FAIL

# FAULT\_COMP\_V CCB1

# R 0x00 CELL16\_ FAIL

| CELL15\_ | FAIL |
|:--- |:--- |
| CELL14\_ | FAIL |
| CELL13\_ | FAIL |
| CELL12\_ | FAIL |
| CELL11\_ | FAIL |
| CELL10\_ | FAIL |
| CELL9\_ | FAIL |
| FAULT\_COMP\_V | CCB2 |

# CELL14\_ FAIL

# CELL13\_ FAIL

# CELL12\_ FAIL

# CELL11\_ FAIL

# CELL10\_ FAIL

# CELL9\_ FAIL

# FAULT\_COMP\_V CCB2

# R 0x00 CELL8\_ FAIL

| CELL7\_ | FAIL |
|:--- |:--- |
| CELL6\_ | FAIL |
| CELL5\_ | FAIL |
| CELL4\_ | FAIL |
| CELL3\_ | FAIL |
| CELL2\_ | FAIL |
| CELL1\_ | FAIL |
| FAULT\_COMP\_V | COW1 |

# CELL6\_ FAIL

# CELL5\_ FAIL

# CELL4\_ FAIL

# CELL3\_ FAIL

# CELL2\_ FAIL

# CELL1\_ FAIL

# FAULT\_COMP\_V COW1

# R 0x00 VCOW16 \_FAIL

| VCOW15 | \_FAIL |
|:--- |:--- |
| VCOW14 | \_FAIL |
| VCOW13 | \_FAIL |
| VCOW12 | \_FAIL |
| VCOW11 | \_FAIL |
| VCOW10 | \_FAIL |
| VCOW9 | \_FAIL |

# VCOW14 \_FAIL

# VCOW13 \_FAIL

# VCOW12 \_FAIL

# VCOW11 \_FAIL

# VCOW10 \_FAIL

# VCOW9 \_FAIL

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated **Register Name** **Addr ** **Hex** **RW ** **Type** **Reset ** **Value** **Data**

**Bit7** **Bit6** **Bit5** **Bit4** **Bit3** **Bit2** **Bit1** **Bit0**

# FAULT\_COMP\_V COW2

# R 0x00 VCOW8 \_FAIL

| VCOW7 | \_FAIL |
|:--- |:--- |
| VCOW6 | \_FAIL |
| VCOW5 | \_FAIL |
| VCOW4 | \_FAIL |
| VCOW3 | \_FAIL |
| VCOW2 | \_FAIL |
| VCOW1 | \_FAIL |
| FAULT\_COMP\_VB | OW1 |

# VCOW6 \_FAIL

# VCOW5 \_FAIL

# VCOW4 \_FAIL

# VCOW3 \_FAIL

# VCOW2 \_FAIL

# VCOW1 \_FAIL

# FAULT\_COMP\_VB OW1

# 54B R 0x00 CBOW16 \_FAIL

| CBOW15 | \_FAIL |
|:--- |:--- |
| CBOW14 | \_FAIL |
| CBOW13 | \_FAIL |
| CBOW12 | \_FAIL |
| CBOW11 | \_FAIL |
| CBOW10 | \_FAIL |
| CBOW9 | \_FAIL |
| FAULT\_COMP\_VB | OW2 |

# CBOW14 \_FAIL

# CBOW13 \_FAIL

# CBOW12 \_FAIL

# CBOW11 \_FAIL

# CBOW10 \_FAIL

# CBOW9 \_FAIL

# FAULT\_COMP\_VB OW2

# 54C R 0x00 CBOW8 \_FAIL

| CBOW7 | \_FAIL |
|:--- |:--- |
| CBOW6 | \_FAIL |
| CBOW5 | \_FAIL |
| CBOW4 | \_FAIL |
| CBOW3 | \_FAIL |
| CBOW2 | \_FAIL |
| CBOW1 | \_FAIL |
| FAULT\_COMP\_C | BFET1 |

# CBOW6 \_FAIL

# CBOW5 \_FAIL

# CBOW4 \_FAIL

# CBOW3 \_FAIL

# CBOW2 \_FAIL

# CBOW1 \_FAIL

# FAULT\_COMP\_C BFET1

# 54E R 0x00 CBFET16 \_FAIL

| CBFET15 | \_FAIL |
|:--- |:--- |
| CBFET14 | \_FAIL |
| CBFET13 | \_FAIL |
| CBFET12 | \_FAIL |
| CBFET11 | \_FAIL |
| CBFET10 | \_FAIL |
| CBFET9 | \_FAIL |
| FAULT\_COMP\_C | BFET2 |

# CBFET14 \_FAIL

# CBFET13 \_FAIL

# CBFET12 \_FAIL

# CBFET11 \_FAIL

# CBFET10 \_FAIL

# CBFET9 \_FAIL

# FAULT\_COMP\_C BFET2

# 54F R 0x00 CBFET8 \_FAIL

| CBFET7 | \_FAIL |
|:--- |:--- |
| CBFET6 | \_FAIL |
| CBFET5 | \_FAIL |
| CBFET4 | \_FAIL |
| CBFET3 | \_FAIL |
| CBFET2 | \_FAIL |
| CBFET1 | \_FAIL |
| FAULT\_COMP\_MI | SC |

# CBFET6 \_FAIL

# CBFET5 \_FAIL

# CBFET4 \_FAIL

# CBFET3 \_FAIL

# CBFET2 \_FAIL

# CBFET1 \_FAIL

# FAULT\_COMP\_MI SC

# R 0x00 RSVD COMP\_ ADC\_ ABORT

# LPF\_FAIL

# FAULT\_PWR1 R 0x00 CVSS\_ OPEN

| DVSS\_ | OPEN |
|:--- |:--- |
| REFHM\_ | OPEN |
| CVDD\_ | UV |
| CVDD\_ | OV |
| DVDD\_ | OV |
| AVDD\_ | OSC |
| AVDD\_ | OV |

# REFHM\_ OPEN

# CVDD\_ UV

# CVDD\_ OV

# DVDD\_ OV

# AVDD\_ OSC

# AVDD\_ OV

# FAULT\_PWR2 R 0x00 RSVD PWRBIST \_FAIL

# RSVD REFH\_ OSC

| NEG5V\_ | UV |
|:--- |:--- |
| TSREF\_ | OSC |
| TSREF\_ | UV |
| TSREF\_ | OV |

# TSREF\_ OSC

# TSREF\_ UV

# TSREF\_ OV

# FAULT\_PWR3 R RSVD RSVD RSVD RSVD AVDDUV \_DRST

# CB\_COMPLETE1 R 0x00 CELL16 \_DONE

| CELL15 | \_DONE |
|:--- |:--- |
| CELL14 | \_DONE |
| CELL13 | \_DONE |
| CELL12 | \_DONE |
| CELL11 | \_DONE |
| CELL10 | \_DONE |
| CELL9 | \_DONE |

# CELL14 \_DONE

# CELL13 \_DONE

# CELL12 \_DONE

# CELL11 \_DONE

# CELL10 \_DONE

# CELL9 \_DONE

# CB\_COMPLETE2 R 0x00 CELL8 \_DONE

| CELL7 | \_DONE |
|:--- |:--- |
| CELL6 | \_DONE |
| CELL5 | \_DONE |
| CELL4 | \_DONE |
| CELL3 | \_DONE |
| CELL2 | \_DONE |
| CELL1 | \_DONE |

# CELL6 \_DONE

# CELL5 \_DONE

# CELL4 \_DONE

# CELL3 \_DONE

# CELL2 \_DONE

# CELL1 \_DONE

# BAL\_TIME R 0x00 TIME\_UNI T

# TIME\[6:0\]

# VCELL16\_HI/LO R 0x80 RESULT\[7:0\]

# R 0x00 RESULT\[7:0\]

# VCELL15\_HI/LO 56A R 0x80 RESULT\[7:0\]

# 56B R 0x00 RESULT\[7:0\]

# VCELL14\_HI/LO 56C R 0x80 RESULT\[7:0\]

# 56D R 0x00 RESULT\[7:0\]

# VCELL13\_HI/LO 56E R 0x80 RESULT\[7:0\]

# 56F R 0x00 RESULT\[7:0\]

# VCELL12\_HI/LO R 0x80 RESULT\[7:0\]

# R 0x00 RESULT\[7:0\]

# VCELL11\_HI/LO R 0x80 RESULT\[7:0\]

# R 0x00 RESULT\[7:0\]

# VCELL10\_HI/LO R 0x80 RESULT\[7:0\]

# R 0x00 RESULT\[7:0\]

# VCELL9\_HI/LO R 0x80 RESULT\[7:0\]

# R 0x00 RESULT\[7:0\]

# VCELL8\_HI/LO R 0x80 RESULT\[7:0\]

# R 0x00 RESULT\[7:0\]

# VCELL7\_HI/LO 57A R 0x80 RESULT\[7:0\]

# 57B R 0x00 RESULT\[7:0\]

# VCELL6\_HI/LO 57C R 0x80 RESULT\[7:0\]

# 57D R 0x00 RESULT\[7:0\]

# VCELL5\_HI/LO 57E R 0x80 RESULT\[7:0\]

# 57F R 0x00 RESULT\[7:0\] **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* **Register Name** **Addr ** **Hex** **RW ** **Type** **Reset ** **Value** **Data**

**Bit7** **Bit6** **Bit5** **Bit4** **Bit3** **Bit2** **Bit1** **Bit0**

# VCELL4\_HI/LO R 0x80 RESULT\[7:0\]

# R 0x00 RESULT\[7:0\]

# VCELL3\_HI/LO R 0x80 RESULT\[7:0\]

# R 0x00 RESULT\[7:0\]

# VCELL2\_HI/LO R 0x80 RESULT\[7:0\]

# R 0x00 RESULT\[7:0\]

# VCELL1\_HI/LO R 0x80 RESULT\[7:0\]

# R 0x00 RESULT\[7:0\]

# BUSBAR\_HI/LO R 0x80 RESULT\[7:0\]

# R 0x00 RESULT\[7:0\]

# TSREF\_HI/LO 58C R 0x80 RESULT\[7:0\]

# 58D R 0x00 RESULT\[7:0\]

# GPIO1\_HI/LO 58E R 0x80 RESULT\[7:0\]

# 58F R 0x00 RESULT\[7:0\]

# GPIO2\_HI/LO R 0x80 RESULT\[7:0\]

# R 0x00 RESULT\[7:0\]

# GPIO3\_HI/LO R 0x80 RESULT\[7:0\]

# R 0x00 RESULT\[7:0\]

# GPIO4\_HI/LO R 0x80 RESULT\[7:0\]

# R 0x00 RESULT\[7:0\]

# GPIO5\_HI/LO R 0x80 RESULT\[7:0\]

# R 0x00 RESULT\[7:0\]

# GPIO6\_HI/LO R 0x80 RESULT\[7:0\]

# R 0x00 RESULT\[7:0\]

# GPIO7\_HI/LO 59A R 0x80 RESULT\[7:0\]

# 59B R 0x00 RESULT\[7:0\]

# GPIO8\_HI/LO 59C R 0x80 RESULT\[7:0\]

# 59D R 0x00 RESULT\[7:0\]

# DIETEMP1\_HI/LO 5AE R 0x80 RESULT\[7:0\]

# 5AF R 0x00 RESULT\[7:0\]

# DIETEMP2\_HI/LO 5B0 R 0x80 RESULT\[7:0\]

# 5B1 R 0x00 RESULT\[7:0\]

# AUX\_CELL\_HI/LO 5B2 R 0x80 RESULT\[7:0\]

# 5B3 R 0x00 RESULT\[7:0\]

# AUX\_GPIO\_HI/LO 5B4 R 0x80 RESULT\[7:0\]

# 5B5 R 0x00 RESULT\[7:0\]

# AUX\_BAT\_HI/LO 5B6 R 0x80 RESULT\[7:0\]

# 5B7 R 0x00 RESULT\[7:0\]

# AUX\_REFL\_HI/LO 5B8 R 0x80 RESULT\[7:0\]

# 5B9 R 0x00 RESULT\[7:0\]

# AUX\_VBG2\_HI/LO 5BA R 0x80 RESULT\[7:0\]

# 5BB R 0x00 RESULT\[7:0\]

# AUX\_AVAO\_REF\_ HI/LO

# 5BE R 0x80 RESULT\[7:0\]

# 5BF R 0x00 RESULT\[7:0\]

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated **Register Name** **Addr ** **Hex** **RW ** **Type** **Reset ** **Value** **Data**

**Bit7** **Bit6** **Bit5** **Bit4** **Bit3** **Bit2** **Bit1** **Bit0**

# AUX\_AVDD\_REF\_ HI/LO

# 5C0 R 0x80 RESULT\[7:0\]

# 5C1 R 0x00 RESULT\[7:0\]

# AUX\_OV\_DAC\_HI /LO

# 5C2 R 0x80 RESULT\[7:0\]

# 5C3 R 0x00 RESULT\[7:0\]

# AUX\_UV\_DAC\_HI/ LO

# 5C4 R 0x80 RESULT\[7:0\]

# 5C5 R 0x00 RESULT\[7:0\]

# AUX\_OT\_OTCB\_ DAC\_HI/LO

# 5C6 R 0x80 RESULT\[7:0\]

# 5C7 R 0x00 RESULT\[7:0\]

# AUX\_UT\_DAC\_HI/ LO

# 5C8 R 0x80 RESULT\[7:0\]

# 5C9 R 0x00 RESULT\[7:0\]

# AUX\_VCBDONE\_ DAC\_HI/LO

# 5CA R 0x80 RESULT\[7:0\]

# 5CB R 0x00 RESULT\[7:0\]

# AUX\_VCM\_HI/LO 5CC R 0x80 RESULT\[7:0\]

# 5CD R 0x00 RESULT\[7:0\]

# REFOVDAC\_HI/L O

# 5D0 R 0x00 RESULT\[7:0\]

# 5D1 R 0x00 RESULT\[7:0\]

# DIAG\_MAIN\_HI/L O

# 5D2 R 0x00 RESULT\[7:0\]

# 5D3 R 0x00 RESULT\[7:0\]

# DIAG\_AUX\_HI/LO 5D4 R 0x00 RESULT\[7:0\]

# 5D5 R 0x00 RESULT\[7:0\]

# DEBUG\_COMM\_S TAT R 0x33 for base 0x3F for stack

# RSVD HW\_ UART\_ DRV

# HW\_ DAISY\_ DRV

# COML\_ TX\_ON

# COML\_ RX\_ON

# COMH\_ TX\_ON

# COMH\_ RX\_ON

# DEBUG\_UART\_R C

# R 0x00 RSVD RC\_IERR RC\_ TXDIS

# RC\_SOF RC\_ BYTE\_ ERR

# RC\_ UNEXP

# RC\_CRC

# DEBUG\_UART\_R R\_TR

# R

0x00 RSVD TR\_SOF TR\_WAIT RR\_SOF RR\_ BYTE\_ ERR

# RR\_CRC

# T R 0x00 RSVD PERR BERR\_ TAG

# SYNC2 SYNC1 BIT

# DEBUG\_COMH\_R C

# R 0x00 RSVD RC\_IERR RC\_ TXDIS

# RC\_SOF RC\_ BYTE\_ ERR

# RC\_ UNEXP

# RC\_CRC

# DEBUG\_COMH\_R R\_TR

# R 0x00 RSVD TR\_WAIT RR\_ TXDIS

# RR\_SOF RR\_ BYTE\_ ERR

# RR\_ UNEXP

# RR\_CRC

# DEBUG\_COML\_BI T

# R 0x00 RSVD PERR BERR\_ TAG

# SYNC2 SYNC1 BIT

# DEBUG\_COML\_R C

# R 0x00 RSVD RC\_IERR RC\_ TXDIS

# RC\_SOF RC\_ BYTE\_ ERR

# RC\_ UNEXP

# RC\_CRC

# DEBUG\_COML\_R R\_TR

# R 0x00 RSVD TR\_WAIT RR\_ TXDIS

# RR\_SOF RR\_ BYTE\_ ERR

# RR\_ UNEXP

# RR\_CRC

# DEBUG\_UART\_DI SCARD

# R 0x00 COUNT\[7:0\]

# DEBUG\_COMH\_D ISCARD

# 78A R 0x00 COUNT\[7:0\] **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* **Register Name** **Addr ** **Hex** **RW ** **Type** **Reset ** **Value** **Data**

**Bit7** **Bit6** **Bit5** **Bit4** **Bit3** **Bit2** **Bit1** **Bit0**

# DEBUG\_COML\_D ISCARD

# 78B R 0x00 COUNT\[7:0\]

# DEBUG\_UART\_V ALID\_HI/LO

# 78C R 0x00 COUNT\[7:0\]

# 78D R 0x00 COUNT\[7:0\]

# DEBUG\_COMH\_V ALID\_HI/LO

# 78E R 0x00 COUNT\[7:0\]

# 78F R 0x00 COUNT\[7:0\]

# DEBUG\_COML\_V ALID\_HI/LO

# R 0x00 COUNT\[7:0\]

# R 0x00 COUNT\[7:0\]

# DEBUG\_OTP\_SE C\_BLK

# 7A0 R 0x00 BLOCK\[7:0\]

# DEBUG\_OTP\_DE D\_BLK

# 7A1 R 0x00 BLOCK\[7:0\]

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## 8.5.4 Register Field Descriptions ***8.5.4.1 Device Addressing Setup***

# 8.5.4.1.1 DIR0\_ADDR\_OTP **Address** **0x0000**

NVM **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name SPARE\[1:0\] ADDRESS\[5:0\] Reset SPARE[1:0] = Spare

ADDRESS\[5:0\] = This register shows the default device address used when *\[DIR\_SEL\]* = 0 and programmed in the OTP. Writing to this register won't change the device address actively in use. This register is used for the system to program the device address to OTP, which will be loaded to the *DIR0\_ADDR* register at POR. For programming, follow the OTP programming procedure.

# 8.5.4.1.2 DIR1\_ADDR\_OTP **Address** **0x0001**

NVM **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name SPARE\[1:0\] ADDRESS\[5:0\] Reset SPARE[1:0] = Spare

ADDRESS\[5:0\] = This register shows the default device address used when *\[DIR\_SEL\]* = 1 and programmed in the OTP. Writing to this register won't change the device address actively in use. This register is used for the system to program the device address to OTP, which will be loaded to the *DIR1\_ADDR* register at POR. For programming, follow the OTP programming procedure. **8.5.4.1.3 CUST\_MISC1 through CUST\_MISC8** **Address** **0x0021 to ** **0x0028**

NVM **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** Name DATA\[7:0\] Reset DATA\[7:0\] = Customer scratch pad

# 8.5.4.1.4 DIR0\_ADDR **Address** **0x0306**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD ADDRESS\[5:0\] Reset RSVD = Reserved

ADDRESS\[5:0\] = Always shows the current device address used by the device when *\[DIR\_SEL\]* = 0. At POR, this register is loaded from the device address value in the OTP (same OTP device address loaded to *DIR0\_ADDR\_OTP * register). Host can re-address the device by writing a different device address to this register, and the device will take on the new address immediately. Note: *CONTROL1\[ADDR\_WR\]* = 1 is required to write to this register. See Section 8.5.4.3.11 for details.

# 8.5.4.1.5 DIR1\_ADDR **Address** **0x0307**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD ADDRESS\[5:0\] Reset RSVD = Reserved **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

ADDRESS\[5:0\] = Always shows the current device address used by the device when *\[DIR\_SEL\]* = 1. At POR, this register is loaded from the device address value in the OTP (same OTP device address loaded to *DIR1\_ADDR\_OTP* register). Host can re-address the device by writing a different device address to this register, and the device will take on the new address immediately. Note: *CONTROL1\[ADDR\_WR\]* = 1 is required to write to this register. See Section 8.5.4.3.11 for details.

## 8.5.4.2 Device ID and Scratch Pad

# 8.5.4.2.1 PARTID **Address** **0x0500** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name PARTID\[7:0\] Reset

# PARTID\[7:0\] $$ = $$

Device Identification: $$ 0x21 = BQ79616 $$ All other codes = Reserved

# 8.5.4.2.2 DEV\_REVID Address 0xE00

Read Only **Bit7** **Bit6** **Bit5** **Bit4** **Bit3** **Bit2** **Bit1** **Bit0** Reset

A value of 0x00 indicates that the device is in normal operating mode. If a fault activates the Factory Testmode Detection, the value will be non-zero. Refer Safety Manual for details on SM426: Fact Testmode Detection. **8.5.4.2.3 DIE\_ID1 through DIE\_ID9** **Address** **0x0501** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** Name ID\[7:0\] Reset ID\[7:0\] = Device Revision

0x10 = Revision A0 0x11 = Revision A1 0x20 = Revision B0 0x21 = Revision B1 0x22 = Revision B2 All other codes = Reserved **Address** **0x0502 to ** **0x0509** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** Name ID\[7:0\] Reset ID\[7:0\] = Die ID for TI factory use

## 8.5.4.3 General Configuration and Control

# 8.5.4.3.1 DEV\_CONF **Address** **0x0002**

NVM **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD NO\_ADJ\_CB MULTIDROP

# \_EN

| FCOMM\_EN | TWO\_STOP | \_EN |
|:--- |:--- |:--- |
| NFAULT\_EN | FTONE\_EN | HB\_EN |
| BQ79616 | SLUSF21 - JUNE 2023 | www.ti.com |

# NFAULT\_EN FTONE\_EN HB\_EN

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated Reset RSVD = Reserved

NO\_ADJ\_CB = Indicates the device will not allow an adjacent CB FET to be turned on in manual CB control. If MCU has enabled an adjacent CB FET, device will not start CB even if host sends *\[BAL\_GO\]* = 1. 0 = Device will allow two adjacent CB FETs to be enabled. 1 = Device will not allow adjacent CB FET to be enabled.

MULTIDROP\_EN = Defines if the device is used in a multidrop or daisy chain configuration. The TX and RX for COML and COMH will be enabled or disabled based on the configuration. 0 = Daisy chain of base device 1 = Multidrop

FCOMM\_EN = Enables the fault state detection through communication in ACTIVE mode. 0 = Disable 1 = Enable

TWO\_STOP\_EN = Enables two stop bits for the UART in case of severe oscillator error in the host and device. 0 = One STOP bit 1 = Two STOP bits NFAULT\_EN = Enables the NFAULT function.

0 = NFAULT always pulled up 1 = NFAULT pulled low to indicate an unmasked fault is detected. Note: This bit setting does not affect the *FAULT\_SUMMARY* register.

FTONE\_EN = Enables FAULT TONE transmitter when device is in SLEEP mode. 0 = Disable 1 = Enable

HB\_EN = Enables HEARTBEAT transmitter when device is in SLEEP mode. 0 = Disable 1 = Enable

# 8.5.4.3.2 ACTIVE\_CELL **Address** **0x0003**

NVM **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name SPARE\[3:0\] NUM\_CELL\[3:0\] Reset Factory OTP Reset SPARE[3:0] = Spare

NUM\_CELL\[3:0\] = Configures the number of cells in series.

$$ 0x0 = 6S $$ $$ 0x1 = 7S $$ $$ 0x2 = 8S $$: $$ 0xA = 16S $$ Unused code defaults to *CHIP\_TYPE\[MAX\_CH1:0\]* setting (in factory trim).If the NUM\_CELL setting has more channels than the device offers, it would be capped to higest number of channel the device offers.

# 8.5.4.3.3 BBVC\_POSN1 **Address** **0x0005**

NVM **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name

CELL16 CELL15 CELL14 CELL13 CELL12 CELL11 CELL10 CELL9 Reset

CELL9 to CELL16 = This register specifies which channel is connected with a bus bar. The cell voltage measurement diagnostic comparison will handle those channel differently 0 = No special handling 1 = Special handling of the enabled channel(s). See Section 8.3.7 for details. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

# 8.5.4.3.4 BBVC\_POSN2 **Address** **0x0006**

NVM **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name

CELL8 CELL7 CELL6 CELL5 CELL4 CELL3 CELL2 CELL1 Reset

CELL1 to CELL8 = Among the active cells specified by the *ACTIVE\_CELL* register, this register indicates which active channel is excluded from the OV, UV and VCB\_DONE monitoring. This register information is also used for cell voltage measurement diagnostic comparison. 0 = No special handling of the functions mentioned above. 1 = Special handling of the functions mentioned above. See Section 8.3.7 for details.

# 8.5.4.3.5 PWR\_TRANSIT\_CONF **Address** **0x0018**

NVM **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name

SPARE\[2:0\] TWARN\_THR\[1:0\] SLP\_TIME\[2:0\] Reset Factory Configura tion default SPARE[2:0] = Spare TWARN\_THR\[1:0\] = Sets the TWARN threshold.

$$ 00 = 85°C $$ $$ 01 = 95°C $$ $$ 10 = 105°C (default) $$ $$ 11 = 115°C $$

SLP\_TIME\[2:0\] = A timeout in SLEEP mode. This timer starts counting when device enters SLEEP mode. When the timer expires, the device enters SHUTDOWN mode. The timer resets if device wakes up to ACTIVE mode. 000 = No timeout. Device remains in SLEEP mode (default at reset) $$ 001 = 5 s $$ $$ 010 = 10 s $$ $$ 011 = 1 min $$ $$ 100 = 10 min $$ $$ 101 = 30 min $$ $$ 110 = 1 hour $$ $$ 111 = 2 hour $$

# 8.5.4.3.6 COMM\_TIMEOUT\_CONF **Address** **0x0019**

NVM **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name

SPARE CTS\_TIME\[2:0\] CTL\_ACT CTL\_TIME\[2:0\] Reset SPARE = Spare

CTS\_TIME\[2:0\] = Sets the short communication timeout. When this timer expires, the device sets the *FAULT\_SYS\[CTL\]* bit. This can be used as an alert to the system to prevent a long communication timeout. 000 = Disables short communication timeout (default at reset) $$ 001 = 100 ms $$ $$ 010 = 2 s $$ $$ 011 = 10 s $$ $$ 100 = 1 min $$ $$ 101 = 10 min $$ $$ 110 = 30 min $$ $$ 111 = 1 hr $$

CTL\_ACT = Configures the device action when long communication timeout timer expires.

0 = Sets *FAULT\_SYS\[CTL\]* and sends device to SLEEP mode 1 = Sends the device to SHUTDOWN. *FAULT\_SYS\[CTL\]* bit will not be set.(default at reset)

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

CTL\_TIME\[2:0\] = Sets the long communication timeout. When this timer expires, the device takes the action configured by the

*\[CTL\_ACT\]* bit. 000 = Disables long communication timeout $$ 001 = 100 ms $$ $$ 010 = 2 s $$ $$ 011 = 10 s $$ 100 = 1 min (default at reset) $$ 101 = 10 min $$ $$ 110 = 30 min $$ $$ 111 = 1 hr $$

# 8.5.4.3.7 TX\_HOLD\_OFF **Address** **0x001A**

NVM **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** Name DLY\[7:0\] Reset

DLY\[7:0\] = Sets the number of bit periods from 0 to 255 to delay after receiving the STOP bit of a command frame and before transmitting the 1st bit of response frame.

# 8.5.4.3.8 STACK\_RESPONSE **Address** **0x0029**

NVM **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name SPARE\[1:0\] DELAY\[5:0\] Reset

# DELAY\[5:0\] $$ = $$

Add additional byte delay gap in daisy chain data response frame $$ 0x00 = 0-µs $$ $$ 0x01 to 0x3F = 0.25-µs to 15.75-µs in 0.25us step $$

# 8.5.4.3.9 BBP\_LOC **Address** **0x002A**

NVM **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name SPARE\[3:0\] LOC\[4:0\] Reset

LOC\[4:0\] = Indicate the BBP pin location and show which VC channel the BB channel is sharing with. This information is used for correcting the common mode error during BB channel ADC measurement 0x00 = BBP/N not in used 0x01 = BBP to negative side of Cell2, BBN to VC1 0x02 = BBP to negative side of Cell3, BBN to VC2 0x03 = BBP to negative side of Cell4, BBN to VC3: 0x0F = BBP to negative side of Cell16, BBN to VC15 0x10= BBP to VC16, BBN to positive side of Cell16

# 8.5.4.3.10 COMM\_CTRL **Address** **0x0308**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD STACK\_DEV TOP\_STACK Reset RSVD = Reserved

STACK\_DEV = Defines device as a base or stack device in daisy chain configuration. 0 = Base device 1 = Stack device **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

TOP\_STACK = Defines device as highest addressed device in the stack. 0 = Not the ToS device 1 = Is the ToS device

# 8.5.4.3.11 CONTROL1 **Address** **0x0309**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name DIR\_SEL SEND\_ SHUTDOWN

# SEND\_WAKE SEND\_ SLPTOACT

| GOTO\_ | SHUTDOWN |
|:--- |:--- |
| GOTO\_ | SLEEP |
| SOFT\_RESET | ADDR\_WR |

# GOTO\_ SLEEP

# SOFT\_RESET ADDR\_WR Reset

DIR\_SEL = Selects daisy chain communication direction.

0 = With two devices connected in daisy chain, command frame travels from COMH of the lower device to COML of the next device. 1 = With two devices connected in daisy chain, command frame travels from COML of the lower device to COMH of the next device.

SEND\_SHUTDOWN = Sends SHUTDOWN tone to next device up the stack. The device receiving this bit set is unaffected. Bit is cleared on read. 0 = Ready 1 = Send SHUTDOWN tone up the stack

SEND\_WAKE = Sends WAKE tone to next device up the stack. Bit is cleared on read.

0 = Ready 1 = Send WAKE tone to next device up the stack.

SEND\_SLPTOACT = Sends SLEEPtoACTIVE tone up the stack. Bit is cleared on read.

0 = Ready 1 = Send SLEEPtoACTIVE tone up the stack

GOTO\_SHUTDOWN = Transitions device to SHUTDOWN mode. Bit is cleared on read. 0 = Ready 1 = Enter SHUTDOWN mode

GOTO\_SLEEP = Transitions device to SLEEP mode. Bit is cleared on read. 0 = Ready 1 = Enter SLEEP mode

SOFT\_RESET = Resets the digital to OTP default. Bit is cleared on read. Setting this bit will cause the device to generate WAKE tone to the upper stack devices. 0 = Ready 1 = Reset device

ADDR\_WR = Enables device to start auto-addressing. When this bit is set, device will not forward the first transition it receives, allowing the device address to be written to a single device. See Section 8.3.6.1.3.2 for details. 0 = Not performing auto-address. Device forwards communication transaction as normal. 1 = Device is being auto-addressed; the first communication transaction it receives will not be forwarded.

# 8.5.4.3.12 CONTROL2 **Address** **0x030A**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD SEND\_HW\_ RESET

# TSREF\_EN Reset RSVD = Reserved

SEND\_HW\_RESET = Sends HW\_RESET tone up the stack. Bit is cleared on read.

0 = Ready 1 = Send HW\_RESET tone to next stack device up

TSREF\_EN = Enables TSREF LDO output. Used to bias NTC thermistor. 0 = Disabled 1 = Enabled

# 8.5.4.3.13 CUST\_CRC\_HI **Address** **0x0036**

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

NVM **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** Name CRC\[7:0\] Reset Factory Configura tion Reset

CRC\[7:0\] = High-byte of the host-calculated CRC for customer OTP space.

# 8.5.4.3.14 CUST\_CRC\_LO **Address** **0x0037**

NVM **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** Name CRC\[7:0\] Reset Factory Configura tion Reset

CRC\[7:0\] = Low-byte of the host-calculated CRC for customer OTP space.

# 8.5.4.3.15 CUST\_CRC\_RSLT\_HI **Address** **0x050C** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** Name CRC\[7:0\] Reset

CRC\[7:0\] = High-byte of the device-calculated CRC for customer OTP space.

# 8.5.4.3.16 CUST\_CRC\_RSLT\_LO **Address** **0x050D** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** Name CRC\[7:0\] Reset

CRC\[7:0\] = Low-byte of the device-calculated CRC for customer OTP space.

## 8.5.4.4 Operation Status

# 8.5.4.4.1 DIAG\_STAT **Address** **0x0526** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD DRDY\_OTUT DRDY\_OVUV DRDY\_BIST \_OTUT

# DRDY\_BIST \_OVUV

# DRDY\_BIST \_PWR Reset RSVD = Reserved

DRDY\_OTUT = Indicates the OTUT round robin has run at least once. This bit is cleared when *\[OTUT\_GO\]* = 1 with

*\[OTUT\_MODE1:0\]* = 01 (start the OTUT round robin run) and set when at least 1 cycle of round robin is completed. 0 = OTUT has not started or first round robin has not completed yet. 1 = At least 1 cycle of round robin has completed. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

DRDY\_OVUV = Indicates the OVUV round robin has at least run once. This bit is cleared when *\[OVUV\_GO\]* = 1 with

*\[OVUV\_MODE1:0\]* = 01 (start the OVUV round robin run) and set when at least 1 cycle of round robin is completed. 0 = OVUV has not started or first round robin has not completed yet. 1 = At least 1 cycle of round robin has completed.

DRDY\_BIST\_OTUT = Indicates the status of the OTUT protector diagnostic. This bit is cleared when *\[OTUT\_GO\]* = 1 with

*\[OTUT\_MODE1:0\]* = 10 (start the BIST run) and set when the BIST cycle is completed. 0 = Not started or still running. 1 = BIST cycle completed.

DRDY\_BIST\_OVUV = Indicates the status of the OVUV protector diagnostic. This bit is cleared when *\[OVUV\_GO\]* = 1 with

*\[OVUV\_MODE1:0\]* = 10 (start the BIST run) and set when the BIST cycle is completed. 0 = Not started or still running. 1 = BIST cycle completed.

DRDY\_BIST\_PWR = Indicates the status of the power supplies diagnostic. This bit is cleared when *\[PWR\_BIST\_GO\]* = 1 (start the BIST run) and set when the BIST cycle is completed. 0 = Not started or still running. 1 = BIST cycle completed.

# 8.5.4.4.2 ADC\_STAT1 **Address** **0x0527** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD RSVD DRDY\_AUX \_GPIO

# DRDY\_AUX \_CELL

# DRDY\_AUX \_MISC

# DRDY\_MAIN \_ADC Reset RSVD = Reserved

DRDY\_AUX\_GPIO = AUX ADC has completed at least a single measurement on all active GPIO channels configured for ADC measurement. This bit is cleared when *\[AUX\_GO\]* is changed from 0 to 1. 0 = Not ready 1 = All GPIO inputs have completed at least a single measurement by the AUX ADC

DRDY\_AUX\_CELL = Device has completed at least a single measurement on all AUXCELL channel(s) set by *\[AUX\_CELL\_SEL4:0\]. *

This bit is cleared when *\[AUX\_GO\]* is changed from 0 to 1. 0 = Not ready 1 = All *\[AUX\_CELL\_SEL4:0\]* configured channels have completed at least a single measurement

DRDY\_AUX\_MISC = Device has completed at least a single measurement on all AUX ADC MISC input channels (that is, completed a single round robin run). This bit is cleared when *\[AUX\_GO\]* is changed from 0 to 1. 0 = Not ready 1 = All AUX ADC MISC inputs have completed at least a single measurement

DRDY\_MAIN\_ADC = Device has completed at least a single measurement on all Main ADC input channels, including all GPIOs (that is, completed a single round robin run). This bit is cleared when *\[MAIN\_GO\]* is changed from 0 to 1. 0 = Not ready 1 = All Main ADC inputs have completed at least a single measurement

# 8.5.4.4.3 ADC\_STAT2 **Address** **0x0528** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name

RSVD DRDY\_LPF DRDY\_GPIO DRDY\_VCOW DRDY\_CBOW DRDY\_ CBFET

# DRDY\_VCCB Reset RSVD = Reserved

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

DRDY\_LPF = Device has finished at least 1 round of LPF checks on all active cell channels. The comparison continues in the background as long as the Main ADC is running. This bit is cleared when *\[MAIN\_GO\]* = 1. This data ready bit is also used when a fault is injected to test the DIAG\_LPF engine using the *\[LPF\_FLT\_INJ\] * bit. When *\[LPF\_FLT\_INJ\]* = 1, this bit is cleared to 0 and the device will restart the VC and BB and BB channel LPF checks from the beginning using the fault inject *\[DIAG\_LPF\]*. Once all channel LPFs are checked, the [DRDY_LPF] = 1. 0 = Not ready 1 = Diagnostic comparison finished

| DRDY\_GPIO = Device has finished the GPIO Main and AUX ADC diagnostic comparisons on all active channels and the | comparisons are stopped. This bit is cleared when \[COMP\_ADC\_GO\] = 1. | 0 = Not ready | 1 = Diagnostic comparison finished |
|:--- |:--- |:--- |:--- |
| DRDY\_VCOW = Device has finished VC OW diagnostic comparison on all active channels and the comparison is stopped. This bit | is cleared when \[COMP\_ADC\_GO\] = 1. | 0 = Not ready | 1 = Diagnostic comparison finished |
| DRDY\_CBOW = Device has finished CB OW diagnostic comparison on all active channels and the comparison is stopped. This bit | is cleared when \[COMP\_ADC\_GO\] = 1. | 0 = Not ready | 1 = Diagnostic comparison finished |
| DRDY\_CBFET = Device has finished CB FET diagnostic comparison on all active channels and the comparison is stopped. This bit | is cleared when \[COMP\_ADC\_GO\] = 1. | 0 = Not ready | 1 = Diagnostic comparison finished |

DRDY\_VCOW = Device has finished VC OW diagnostic comparison on all active channels and the comparison is stopped. This bit is cleared when *\[COMP\_ADC\_GO\]* = 1. 0 = Not ready 1 = Diagnostic comparison finished

DRDY\_CBOW = Device has finished CB OW diagnostic comparison on all active channels and the comparison is stopped. This bit is cleared when *\[COMP\_ADC\_GO\]* = 1. 0 = Not ready 1 = Diagnostic comparison finished

DRDY\_CBFET = Device has finished CB FET diagnostic comparison on all active channels and the comparison is stopped. This bit is cleared when *\[COMP\_ADC\_GO\]* = 1. 0 = Not ready 1 = Diagnostic comparison finished

DRDY\_VCCB = Device has finished VCELL vs. AUXCELL diagnostic comparison on all active channels. This bit is cleared when

[COMP_ADC_GO] = 1. 0 = Not ready 1 = Diagnostic comparison finished

# 8.5.4.4.4 GPIO\_STAT **Address** **0x052A**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name

GPIO8 GPIO7 GPIO6 GPIO5 GPIO4 GPIO3 GPIO2 GPIO1 Reset

GPIO1 through GPIO8 = When GPIO is configured as digital input or output, this register shows the GPIO status. $$ 0 = Low $$ 1 = High

# 8.5.4.4.5 BAL\_STAT **Address** **0x052B** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name INVALID\_ CBCONF

# OT\_PAUSE \_DET

# CB\_INPAUSE MB\_RUN CB\_RUN ABORTFLT MB\_DONE CB\_DONE Reset

# R R R R R R R R

INVALID\_CBCONF = Indicates CB is unable to start (after *\[BAL\_GO\]* = 1) due to improper CB control settings. Incorrect settings include:

- • More than eight cells are enabled for CB. - • More than two adjacent cells are enabled for CB if *DEVICE\_CONF\[NO\_ADJ\_CB\]* = 0. - • Any adjacent cells are enabled for CB if *DEVICE\_CONF\[NO\_ADJ\_CB\]* = 1.

This bit is updated every time *\[BAL\_GO\]* = 1. 0 = Valid CB setting 1 = Invalid CB setting **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

OT\_PAUSE\_DET = Indicates the OTCB is detected if *\[OTCB\_EN\]* = 1. The bit is also set if CB TWARN is detected, which will also pause CB. Valid only after *\[BAL\_GO\]* = 1 0 = No OTCB or CB TWARN is detected 1 = Any NTC thermistor measurement is greater than *OTCB\_THR\[3:0\]* setting, or die (CBFET) temperature is greater than CB TWARN

CB\_INPAUSE = Indicates the cell balancing pause status.

0 = CB is running or not started 1 = Paused (can be caused by OTCB detection, or host sets *\[CB\_PAUSE\]* = 1)

MB\_RUN = Indicates module balancing, controlled by the device, is running. Only valid if *MB\_TIMER\_CTRL* is not 0x00 and after *\[BAL\_GO\]* = 1. Does not indicate the cell balancing status. 0 = Completed or not started 1 = Module balancing, controlled by the device, is running

CB\_RUN = Indicates cell balancing is running. Only valid after *\[BAL\_GO\]* = 1. Does not indicate the module balancing status.

This bit remains as 1 even if CB is in pause state. 0 = Completed or not started 1 = At least 1 cell is in active cell balancing

ABORTFLT = Indicates cell balancing is aborted due to detection of unmasked fault. Cleared when *BAL\_CTRL1\[BAL\_GO\]* = 1. CB abort does not trigger if CB is in pause ( *\[CB\_INPAUSE\]* =1) even if an unmasked fault is detected. The abort at fault function will resume if CB is no longer in pause state. 0 = Not aborted or cell balancing not running 1 = Aborted

MB\_DONE = Indicates module balancing is completed. Cleared when *BAL\_CTRL1\[BAL\_GO\]* = 1.

0 = Module balancing is still running or has not started 1 = Module balancing completed

CB\_DONE = Indicates all cell balancing is completed. Cleared when *BAL\_CTRL1\[BAL\_GO\]* = 1.

0 = Cell balancing is still running or has not started 1 = All cell balancing is completed

# 8.5.4.4.6 DEV\_STAT **Address** **0x052C** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD FACT\_CRC \_DONE

# CUST\_CRC \_DONE

# OTUT\_RUN OVUV\_RUN RSVD AUX\_RUN MAIN\_RUN Reset RSVD = Reserved

FACT\_CRC\_DONE = Indicates the status of the factory CRC state machine. This bit is set when the factory CRC is calculated and verified internally at least once. A read from this register will clear this bit. 0 = Not complete 1 = Complete (cleared on read)

CUST\_CRC\_DONE = Indicates the status of the customer CRC state machine. This bit is set when the CRC is calculated and compared to the *CUST\_CRC\** registers at least once. A read from this register will clear this bit. 0 = Not complete 1 = Complete (cleared on read)

OTUT\_RUN = Shows the status of the OTUT protector comparators. This bit is set when OTUT BIST starts. When BIST is completed or aborted, the device will turn off the OT and UT comparators automatically, and then this bit will be cleared). 0 = off (that is, OTUT is not started or when *\[OTUT\_GO\]* = 1 and *\[OTUT\_MODE1:0\]* = 0) 1 = on (that is, when [OTUT_GO] = 1 and [OTUT_MODE1:0] is non-zero)

OVUV\_RUN = Shows the status of the OVUV protector comparators. This bit is set when OVUV BIST starts. When BIST is completed or aborted, the device will turn off the OV and UV comparators automatically, and then this bit will be cleared). 0 = off (that is, OVUV is not started or when *\[OVUV\_GO\]* = 1 and *\[OVUV\_MODE1:0\]* = 0) 1 = on (that is, when [OVUV_GO] = 1 and [OVUV_MODE1:0] is non-zero) AUX\_RUN = Shows the status of the AUX ADC. $$ 0 = off $$ $$ 1 = on $$

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated MAIN\_RUN = Shows the status of the Main ADC. $$ 0 = off $$ $$ 1 = on $$

## 8.5.4.5 ADC Configuration and Control

# 8.5.4.5.1 ADC\_CONF1 **Address** **0x0007**

NVM **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name

AUX\_SETTLE\[1:0\] LPF\_BB\[2:0\] LPF\_VCELL\[2:0\] Reset

AUX\_SETTLE\[1:0\] = The AUXCELL configures the AUX CELL settling time. Each AUXCELL has to wait for the anti-aliasing filter (AAF) settling time in order to consider as a valid measurement. These bits provide the option to use different AAF or bypass an AAF to trade for a fast measurement. $$ 00 = 4.3 ms $$ $$ 01 = 2.3 ms $$ $$ 10 = 1.3 ms $$ 11 = Reserved

LPF\_BB\[2:0\] = Configures the post main SAR ADC low-pass filter cut-off frequency for BBP/N measurement. Same options as the *LPF\_VCELL\[2:0\]*.

LPF\_VCELL\[2:0\] = Configures the post ADC low-pass filter cut-off frequency for VCELL measurement.

$$ 0x0 = 6.5 Hz (154 ms average) $$ $$ 0x1 = 13 Hz (77 ms average) $$ $$ 0x2 = 26 Hz (38 ms average) $$ $$ 0x3 = 53 Hz (19 ms average) $$ $$ 0x4 = 111 Hz (9 ms average) $$ $$ 0x5 = 240 Hz (4 ms average) $$ $$ 0x6 = 600 Hz (1.6 ms average) $$ $$ 0x7 = 240 Hz $$

# 8.5.4.5.2 ADC\_CONF2 **Address** **0x0008**

NVM **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name SPARE\[1:0\] ADC\_DLY\[5:0\] Reset SPARE[1:0] = Spare

ADC\_DLY\[5:0\] = If *\[MAIN\_GO\]* bit is written to 1, bit Main ADC is delayed for this setting time before being enabled to start the conversion. This setting synchronizes the start of Main ADC throughout the daisy-chained stack. The option ranges from 0 µs (no delay) to 200 µs in 5-µs steps. Undefined code = 0 µs (no delay)

# 8.5.4.5.3 MAIN\_ADC\_CAL1 **Address** **0x001B**

NVM **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** Name GAINL\[7:0\] Reset

GAINL\[7:0\] = Main ADC 25°C gain calibration result (lower 8-bit). If customer performs gain calibration during production flow, the gain result can be programmed to OTP and will be sent to this gain register at device reset. The device automatically applies this data during ADC correction step. Range from -0.78125% to 0.7782% in 0.0031% steps.

# 8.5.4.5.4 MAIN\_ADC\_CAL2 **Address** **0x001C**

NVM **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name GAINH OFFSET\[6:0\] **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* Reset

GAINH Main ADC 25°C gain calibration result (MS bit). If customer performs gain calibration during production flow, the gain result can be programmed to OTP and will be sent to this gain register at device reset. The device automatically applies this data during ADC correction step. Range from -0.78125% to 0.7782% in 0.0031% steps.

OFFSET\[6:0\] = Main ADC 25°C offset calibration result. If customer performs offset calibration during production flow, the offset result can be programmed to OTP and will be sent to this offset register at device reset. The device automatically applies this data during ADC correction step. Range from -12.20703-mV to 12.01630-mV in 0.19073-mV steps

# 8.5.4.5.5 AUX\_ADC\_CAL1 **Address** **0x001D**

NVM **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** Name GAINL\[7:0\] Reset

GAINL\[7:0\] = AUX ADC 25°C gain calibration result (lower 8-bit). If customer performs gain calibration during production flow, the gain result can be programmed to OTP and will be sent to this gain register at device reset. The device automatically applies this data during ADC correction step. Range from -0.78125% to 0.7782% in 0.0031% steps.

# 8.5.4.5.6 AUX\_ADC\_CAL2 **Address** **0x001E**

NVM **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name GAINH OFFSET\[6:0\] Reset

GAINH AUX ADC 25°C gain calibration result (MS bit). If customer performs gain calibration during production flow, the gain result can be programmed to OTP and will be sent to this gain register at device reset. The device automatically applies this data during ADC correction step. Range from -0.78125% to 0.7782% in 0.0031% steps.

OFFSET\[6:0\] = AUX ADC 25°C offset calibration result. If customer performs offset calibration during production flow, the offset result can be programmed to OTP and will be sent to this offset register at device reset. The device automatically applies this data during ADC correction step. Range from -12.20703-mV to 12.01630-mV in 0.19073-mV steps

# 8.5.4.5.7 ADC\_CTRL1 **Address** **0x030D**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD RSVD LPF\_BB\_EN LPF\_VCELL \_EN

# MAIN\_GO MAIN\_MODE\[1:0\] Reset RSVD = Reserved

LPF\_BB\_EN = Enables digital low-pass filter post-ADC conversion. LPF applies to BBP/N measurements only. The cut-off

frequency is configured by *ADC\_CONFIG1\[LPF\_BB\[2:0\]*.

LPF\_VCELL\_EN = Enables digital low-pass filter post-ADC conversion. LPF applies to VCELL measurements only. The cut-off frequency is configured by *ADC\_CONFIG1\[LPF\_VCELL\[2:0\]*.

MAIN\_GO = Starts main ADC conversion. When this bit is written to 1, all Main ADC inputs are sampled. Once the Main ADC is started, any change to the Main ADC control setting has no effect until this bit is written to 1 again. This bit is cleared to 0 in read. 0 = Ready. Writing 0 has no effect 1 = Start Main ADC

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

MAIN\_MODE\[1:0\] = Sets the Main ADC run mode. In continuous run, if user would like to stop ADC, user must read all the ADC

conversion results, then stop it. ADC results are not valid before ADC is reenabled next time. 00 = Main ADC not running 01 = Single run. Run the main ADC round robin 8 times and then stop 10 = Continuous run. Continuous running the Main ADC round robin until host sends command to stop 11 = Reserved

# 8.5.4.5.8 ADC\_CTRL2 **Address** **0x030E**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD RSVD AUX\_CELL\_A LIGN

# AUX\_CELL\_SEL\[4:0\] Reset RSVD = Reserved

AUX\_CELL\_ALIGN = Align the AUX ADC AUXCELL measurement to Main ADC CELL1 or CELL8

0 = Dynamic Alignment 1 = Align to Main ADC CELL8

AUX\_CELL\_SEL\[4:0\] = Selects which AUXCELL channel(s) will be multiplexed through the AUX ADC.

0x00 = Run all active cell channels set by *ACTIVE\_CELL\_CONF* register 0x01 = Lock to AUX Busbar (BBP-BBN) 0x02 = Lock to AUXCELL1 0x03 = Lock to AUXCELL2 0x04 = Lock to AUXCELL3: 0x11 = Lock to AUXCELL16 $$ 0x12 to 0x1F = RSVD $$ NOTE: If inactive channel or RSVD code is selected, device will not perform AUX ADC conversion on the AUXCELL slot and the *AUX\_CELL\_HI/LO* registers will be kept in reset value.

# 8.5.4.5.9 ADC\_CTRL3 **Address** **0x030F**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name

RSVD AUX\_GPIO\_SEL\[3:0\] AUX\_GO AUX\_MODE\[1:0\] Reset RSVD = Reserved

AUX\_GPIO\_SEL\[3:0\] = Selects which GPIO channel(s) will be multiplexed through the AUX ADC to use for temperature measurement diagnostic. If this selection is not set to 0x00, the AUX ADC will lock onto a single GPIO channel and the measurement result is output to the *AUX\_GPIO\_HI/LO* registers. 0x00 = AUX ADC cycles through all GPIO channel(s) that are configured as ADC only or ADC and OTUT. 0x01 = Lock to GPIO1 0x02 = Lock to GPIO2: 0x08 = Lock to GPIO8 All other codes are RSVD. NOTE: If GPIO is not configured for ADC measurement or RSVD codes are selected, device will not perform AUX ADC conversion on the GPIO slot and the *AUX\_GPIO\_HI/LO* registers will be kept in reset value.

AUX\_GO = Starts AUX ADC conversion. When this bit is written to 1, all AUX ADC inputs are sampled. Once the AUX ADC is started, any change to the AUX ADC control setting has no effect until this bit is written to 1 again. This bit is cleared to 0 in read. 0 = Ready. Writing 0 has no effect. 1 = Start AUX ADC

AUX\_MODE\[1:0\] = Sets the Main ADC run mode. In continuous run, if user would like to stop ADC, user must read all the ADC

conversion results, then stop it. ADC results are not valid before ADC is reenabled next time. 00 = AUX ADC not running 01 = Single run. Run the AUX ADC round robin once and then stop. 10 = Continuous run. Continually run the AUX ADC round robin until host sends command to stop. 11 = 8-round-robin run to measure all eight GPIOs once. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## 8.5.4.6 ADC Measurement Results

# 8.5.4.6.1 VCELL16\_HI/LO

# VCELL16\_HI **Address** **0x0568** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the high-byte of the Cell16 voltage in 2s complement. When host reads this register, the device locks the Cell16 voltage low-byte from updating until the high-byte and low-byte registers are read.

# VCELL16\_LO **Address** **0x0569** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the low-byte of the Cell16 voltage in 2s complement.

# 8.5.4.6.2 VCELL15\_HI/LO

# VCELL15\_HI **Address** **0x056A** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the high-byte of the Cell15 voltage in 2s complement. When host reads this register, the device locks the Cell15 voltage low-byte from updating until the high-byte and low-byte registers are read.

# VCELL15\_LO **Address** **0x056B** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the low-byte of the Cell15 voltage in 2s complement.

# 8.5.4.6.3 VCELL14\_HI/LO

# VCELL14\_HI **Address** **0x056C** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

RESULT\[7:0\] = The ADC measurement result of the high-byte of the Cell14 voltage in 2s complement. When host reads this register, the device locks the Cell14 voltage low-byte from updating until the high-byte and low-byte registers are read.

# VCELL14\_LO **Address** **0x056D** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the low-byte of the Cell14 voltage in 2s complement.

# 8.5.4.6.4 VCELL13\_HI/LO

# VCELL13\_HI **Address** **0x056E** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the high-byte of the Cell13 voltage in 2s complement. When host reads this register, the device locks the Cell13 voltage low-byte from updating until the high-byte and low-byte registers are read.

# VCELL13\_LO **Address** **0x056F** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the low-byte of the Cell13 voltage in 2s complement.

# 8.5.4.6.5 VCELL12\_HI/LO

# VCELL12\_HI **Address** **0x0570** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the high-byte of the Cell12 voltage in 2s complement. When host reads this register, the device locks the Cell12 voltage low-byte from updating until the high-byte and low-byte registers are read.

# VCELL12\_LO **Address** **0x0571** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

RESULT\[7:0\] = The ADC measurement result of the low-byte of the Cell12 voltage in 2s complement.

# 8.5.4.6.6 VCELL11\_HI/LO

# VCELL11\_HI **Address** **0x0572** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the high-byte of the Cell11 voltage in 2s complement. When host reads this register, the device locks the Cell11 voltage low-byte from updating until the high-byte and low-byte registers are read.

# VCELL11\_LO **Address** **0x0573** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the low-byte of the Cell11 voltage in 2s complement.

# 8.5.4.6.7 VCELL10\_HI/LO

# VCELL10\_HI **Address** **0x0574** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the high-byte of the Cell10 voltage in 2s complement. When host reads this register, the device locks the Cell10 voltage low-byte from updating until the high-byte and low-byte registers are read.

# VCELL10\_LO **Address** **0x0575** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the low-byte of the Cell10 voltage in 2s complement.

# 8.5.4.6.8 VCELL9\_HI/LO

# VCELL9\_HI **Address** **0x0576** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

RESULT\[7:0\] = The ADC measurement result of the high-byte of the Cell9 voltage in 2s complement. When host reads this register, the device locks the Cell9 voltage low-byte from updating until the high-byte and low-byte registers are read.

# VCELL9\_LO **Address** **0x0577** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the low-byte of the Cell9 voltage in 2s complement.

# 8.5.4.6.9 VCELL8\_HI/LO

# VCELL8\_HI **Address** **0x0578** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the high-byte of the Cell8 voltage in 2s complement. When host reads this register, the device locks the Cell8 voltage low-byte from updating until the high-byte and low-byte registers are read.

# VCELL8\_LO **Address** **0x0579** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the low-byte of the Cell8 voltage in 2s complement.

# 8.5.4.6.10 VCELL7\_HI/LO

# VCELL7\_HI **Address** **0x057A** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the high-byte of the Cell7 voltage in 2s complement. When host reads this register, the device locks the Cell7 voltage low-byte from updating until the high-byte and low-byte registers are read.

# VCELL7\_LO **Address** **0x057B** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the low-byte of the Cell7 voltage in 2s complement. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

# 8.5.4.6.11 VCELL6\_HI/LO

# VCELL6\_HI **Address** **0x057C** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the high-byte of the Cell6 voltage in 2s complement. When host reads this register, the device locks the Cell6 voltage low-byte from updating until the high-byte and low-byte registers are read.

# VCELL6\_LO **Address** **0x057D** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the low-byte of the Cell6 voltage in 2s complement.

# 8.5.4.6.12 VCELL5\_HI/LO

# VCELL5\_HI **Address** **0x057E** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the high-byte of the Cell5 voltage in 2s complement. When host reads this register, the device locks the Cell5 voltage low-byte from updating until the high-byte and low-byte registers are read.

# VCELL5\_LO **Address** **0x057F**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the low-byte of the Cell5 voltage in 2s complement.

# 8.5.4.6.13 VCELL4\_HI/LO

# VCELL4\_HI **Address** **0x0580** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the high-byte of the Cell4 voltage in 2s complement. When host reads this register, the device locks the Cell4 voltage low-byte from updating until the high-byte and low-byte registers are read.

# VCELL4\_LO **Address** **0x0581**

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the low-byte of the Cell4 voltage in 2s complement.

# 8.5.4.6.14 VCELL3\_HI/LO

# VCELL3\_HI **Address** **0x0582** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the high-byte of the Cell3 voltage in 2s complement. When host reads this register, the device locks the Cell3 voltage low-byte from updating until the high-byte and low-byte registers are read.

# VCELL3\_LO **Address** **0x0583** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the low-byte of the Cell3 voltage in 2s complement.

# 8.5.4.6.15 VCELL2\_HI/LO

# VCELL2\_HI **Address** **0x0584** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the high-byte of the Cell2 voltage in 2s complement. When host reads this register, the device locks the Cell2 voltage low-byte from updating until the high-byte and low-byte registers are read.

# VCELL2\_LO **Address** **0x0585** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the low-byte of the Cell2 voltage in 2s complement.

# 8.5.4.6.16 VCELL1\_HI/LO

# VCELL1\_HI **Address** **0x0586** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* Reset

RESULT\[7:0\] = The ADC measurement result of the high-byte of the Cell1 voltage in 2s complement. When host reads this register, the device locks the Cell1 voltage low-byte from updating until the high-byte and low-byte registers are read.

# VCELL1\_LO **Address** **0x0587** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the low-byte of the Cell1 Voltage in 2s complement.

# 8.5.4.6.17 BUSBAR\_HI/LO

# BUSBAR\_HI **Address** **0x0588** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the high-byte of the differential bus bar pins (BBP - BBN) in 2s complement. When host reads this register, the device locks the low-byte from updating until the high-byte and low-byte registers are read.

# BUSBAR\_LO **Address** **0x0589** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the low-byte of the differential bus bar pins (BBP - BBN) in 2s complement.

# 8.5.4.6.18 TSREF\_HI/LO

# TSREF\_HI **Address** **0x058C** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The TSREF high-byte result from Main ADC. When host reads this register, the device locks the TSREF low-byte from updating until the high-byte and low-byte registers are read.

# TSREF\_LO **Address** **0x058D** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The TSREF low-byte result from Main ADC

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

# 8.5.4.6.19 GPIO1\_HI/LO

# GPIO1\_HI **Address** **0x058E** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement high-byte result of the GPIO1. When host reads this register, the device locks the GPIO1 low-byte from updating until the high-byte and low-byte registers are read.

# GPIO1\_LO **Address** **0x058F** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement low-byte result of the GPIO1.

# 8.5.4.6.20 GPIO2\_HI/LO

# GPIO2\_HI **Address** **0x0590** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement high-byte result of the GPIO2. When host reads this register, the device locks the GPIO2 low-byte from updating until the high-byte and low-byte registers are read.

# GPIO2\_LO **Address** **0x0591** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement low-byte result of the GPIO2.

# 8.5.4.6.21 GPIO3\_HI/LO

# GPIO3\_HI **Address** **0x0592** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement high-byte result of the GPIO3. When host reads this register, the device locks the GPIO3 low-byte from updating until the high-byte and low-byte registers are read.

# GPIO3\_LO **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* **Address** **0x0593** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement low-byte result of the GPIO3.

# 8.5.4.6.22 GPIO4\_HI/LO

# GPIO4\_HI **Address** **0x0594** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement high-byte result of the GPIO4. When host reads this register, the device locks the GPIO4 low-byte from updating until the high-byte and low-byte registers are read.

# GPIO4\_LO **Address** **0x0595** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement low-byte result of the GPIO4.

# 8.5.4.6.23 GPIO5\_HI/LO

# GPIO5\_HI **Address** **0x0596**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement high-byte result of the GPIO5. When host reads this register, the device locks the GPIO5 low-byte from updating until the high-byte and low-byte registers are read.

# GPIO5\_LO **Address** **0x0597** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement low-byte result of the GPIO5.

# 8.5.4.6.24 GPIO6\_HI/LO

# GPIO6\_HI **Address** **0x0598** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\]

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated Reset

RESULT\[7:0\] = The ADC measurement high-byte result of the GPIO6. When host reads this register, the device locks the GPIO6 low-byte from updating until the high-byte and low-byte registers are read.

# GPIO6\_LO **Address** **0x0599** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement low-byte result of the GPIO6.

# 8.5.4.6.25 GPIO7\_HI/LO

# GPIO7\_HI **Address** **0x059A** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement high-byte result of the GPIO7. When host reads this register, the device locks the GPIO7 low-byte from updating until the high-byte and low-byte registers are read.

# GPIO7\_LO **Address** **0x059B** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement low-byte result of the GPIO7.

# 8.5.4.6.26 GPIO8\_HI/LO

# GPIO8\_HI **Address** **0x059C** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement high-byte result of the GPIO8. When host reads this register, the device locks the GPIO8 low-byte from updating until the high-byte and low-byte registers are read.

# GPIO8\_LO **Address** **0x059D** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement low-byte result of the GPIO8. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

# 8.5.4.6.27 DIETEMP1\_HI/LO

# DIETEMP1\_HI **Address** **0x05AE** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The DieTemp1 high-byte result from Main ADC. When host reads this register, the device locks the DIETEMP1 low-byte from updating until the high-byte and low-byte registers are read.

# DIETEMP1\_LO **Address** **0x05AF** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The DieTemp1 low-byte (temperature used for ADC correction) result from Main ADC.

# 8.5.4.6.28 DIETEMP2\_HI/LO

# DIETEMP2\_HI **Address** **0x05B0** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The DieTemp2 high-byte result from AUX ADC. When host reads this register, the device locks the DIETEMP2 low-byte from updating until the high-byte and low-byte registers are read.

# DIETEMP2\_LO **Address** **0x05B1** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The DieTemp2 low-byte (temperature used for ADC correction) result from AUX ADC

# 8.5.4.6.29 AUX\_CELL\_HI/LO

# AUX\_CELL\_HI **Address** **0x05B2** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the high-byte of the AUXCELL voltage in 2s complement. These *AUX\_CELL\_HI/LO* registers will only report AUXCELL voltage measurement if host configures *\[AUX\_CELL\_SEL4:0\]* to lock to a single AUXCELL channel. When host reads this register, the device locks the AUXCELL voltage low-byte from updating until the high-byte and low-byte registers are read.

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

# AUX\_CELL\_LO **Address** **0x05B3** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The ADC measurement result of the low-byte of the AUX cell voltage in 2s complement. These *AUX\_CELL\_HI/LO* registers will only report AUXCELL voltage measurement if host configures *\[AUX\_CELL\_SEL4:0\]* to lock to a single AUXCELL channel.

# 8.5.4.6.30 AUX\_GPIO\_HI/LO

# AUX\_GPIO\_HI **Address** **0x05B4** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The AUX ADC measurement high-byte result of the GPIO that is locked by the *\[AUXGPIO\_SEL3:0\]* bits. When host reads this register, the device locks the AUX\_GPIO low-byte from updating until the high-byte and low-byte registers are read.

# AUX\_GPIO\_LO **Address** **0x05B5** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The AUX ADC measurement low-byte result of the GPIO that is locked by the *\[AUXGPIO\_SEL3:0\]* bits.

# 8.5.4.6.31 AUX\_BAT\_HI/LO

# AUX\_BAT\_HI **Address** **0x05B6**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The high-byte result of the BAT pin measurement from AUX ADC. When host reads this register, the device locks the AUX\_BAT low-byte from updating until the high-byte and low-byte registers are read.

# AUX\_BAT\_LO **Address** **0x05B7** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The low-byte result of the BAT pin measurement from AUX ADC.

# 8.5.4.6.32 AUX\_REFL\_HI/LO

# AUX\_REFL\_HI **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* **Address** **0x05B8** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The high-byte result of the internal reference, REFL, measurement from AUX ADC. When host reads this register, the device locks the AUX\_REL low-byte from updating until the high-byte and low-byte registers are read.

# AUX\_REFL\_LO **Address** **0x05B9** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The low-byte result of the internal reference, REFL, measurement from AUX ADC.

# 8.5.4.6.33 AUX\_VBG2\_HI/LO

# AUX\_VBG2\_HI **Address** **0x05BA** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The high-byte result of the internal reference, VBG2, measurement from AUX ADC. When host reads this register, the device locks the AUX\_VBG2 low-byte from updating until the high-byte and low-byte registers are read.

# AUX\_VBG2\_LO **Address** **0x05BB**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The low-byte result of the internal reference, VBG2, measurement from AUX ADC.

# 8.5.4.6.34 AUX\_AVAO\_REF\_HI/LO

# AUX\_AVAO\_REF\_HI **Address** **0x05BE** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The high-byte result of the AVAO\_REF measurement from AUX ADC. When host reads this register, the device locks the AUX\_AVAO\_REF low-byte from updating until the high-byte and low-byte registers are read.

# AUX\_AVAO\_REF\_LO **Address** **0x05BF** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\]

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated Reset

RESULT\[7:0\] = The low-byte result of the AVAO\_REF measurement from AUX ADC.

# 8.5.4.6.35 AUX\_AVDD\_REF\_HI/LO

# AUX\_AVDD\_REF\_HI **Address** **0x05C0** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The high-byte result of the AVDD\_REF measurement from AUX ADC. When host reads this register, the device locks the AUX\_AVDD\_REF low-byte from updating until the high-byte and low-byte registers are read.

# AUX\_AVDD\_REF\_LO **Address** **0x05C1** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The low-byte result of the AVDD\_REF measurement from AUX ADC.

# 8.5.4.6.36 AUX\_OV\_DAC\_HI/LO

# AUX\_OV\_DAC\_HI **Address** **0x05C2**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The high-byte result of the OV comparator DAC measurement, which is (0.8 x OV threshold), from AUX ADC. When host reads this register, the device locks the AUX\_OV\_DAC low-byte from updating until the high-byte and low-byte registers are read.

# AUX\_OV\_DAC\_LO **Address** **0x05C3**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The low-byte result of the OV comparator DAC measurement, which is (0.8 x OV threshold), from AUX ADC.

# 8.5.4.6.37 AUX\_UV\_DAC\_HI/LO

# AUX\_UV\_DAC\_HI **Address** **0x05C4**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The high-byte result of the UV comparator DAC measurement, which is (0.8 x UV threshold), from AUX ADC. When host reads this register, the device locks the AUX\_UV\_DAC low-byte from updating until the high-byte and low-byte registers are read. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

# AUX\_UV\_DAC\_LO **Address** **0x05C5**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The low-byte result of the UV comparator DAC measurement, which is (0.8 x UV threshold), from AUX ADC.

# 8.5.4.6.38 AUX\_OT\_OTCB\_DAC\_HI/LO

# AUX\_OT\_OTCB\_DAC\_HI **Address** **0x05C6**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The high-byte result of the OT comparator (either OT or OTCB threshold based on *\[OTCB\_THR\_LOCK\]* setting) DAC measurement from AUX ADC. When host reads this register, the device locks the AUX\_OT\_OTCB\_DAC low-byte from updating until the high-byte and low-byte registers are read.

# AUX\_OT\_OTCB\_DAC\_LO **Address** **0x05C7**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The low-byte result of the OT comparator (either OT or OTCB threshold based on *\[OTCB\_THR\_LOCK\]* setting) DAC measurement from AUX ADC.

# 8.5.4.6.39 AUX\_UT\_DAC\_HI/LO

# AUX\_UT\_DAC\_HI **Address** **0x05C8**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The high-byte result of the UT comparator DAC measurement from AUX ADC. When host reads this register, the device locks the AUX\_UT\_DAC low-byte from updating until the high-byte and low-byte registers are read.

# AUX\_UT\_DAC\_LO **Address** **0x05C9**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The low-byte result of the UT comparator DAC measurement from AUX ADC.

# 8.5.4.6.40 AUX\_VCBDONE\_DAC\_HI/LO

# AUX\_VCBDONE\_DAC\_HI **Address** **0x05CA**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\]

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated Reset

RESULT\[7:0\] = The high-byte result of the UV comparator (VCBDONE Threshold) DAC measurement from AUX ADC. When host reads this register, the device locks the AUX\_VCBDONE\_DAC low-byte from updating until the high-byte and low-byte registers are read.

# AUX\_VCBDONE\_DAC\_LO **Address** **0x05CB**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The low-byte result of the UV comparator (VCBDONE Threshold) DAC measurement from AUX ADC.

# 8.5.4.6.41 AUX\_VCM\_HI/LO

# AUX\_VCM\_HI

**Address** **0x05CC** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The high-byte result of the VCM (common mode voltage on Main ADC) measurement from AUX ADC. When host reads this register, the device locks the AUX\_VCM low-byte from updating until the high-byte and low-byte registers are read.

# AUX\_VCM\_LO **Address** **0x05CD**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The low-byte result of the VCM (common mode voltage on Main ADC) measurement from AUX ADC.

# 8.5.4.6.42 REFOVDAC\_HI/LO

# REFOVDAC\_HI **Address** **0x05D0**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The high-byte result of the recorded OVDAC reference voltage trimmed at factory.

# REFOVDAC\_LO **Address** **0x05D1**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The low-byte result of the recorded OVDAC reference voltage trimmed at factory.

# 8.5.4.6.43 DIAG\_MAIN\_HI/LO

# DIAG\_MAIN\_HI **Address** **0x05D2** **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The high-byte result of reported Main ADC comparison value used in the diagnostic ADC comparison. Valid if the diagnostic ADC comparison is run when a single channel is locked

# DIAG\_MAIN\_LO **Address** **0x05D3**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The low-byte result of reported Main ADC comparison value used in the diagnostic ADC comparison. Valid if the diagnostic ADC comparison is run when a single channel is locked

# 8.5.4.6.44 DIAG\_AUX\_HI/LO

# DIAG\_AUX\_HI **Address** **0x05D4**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The high-byte result of reported AUX ADC comparison value used in the diagnostic ADC comparison. Valid if the diagnostic ADC comparison is run when a single channel is locked

# DIAG\_AUX\_LO **Address** **0x05D5**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RESULT\[7:0\] Reset

RESULT\[7:0\] = The low-byte result of reported AUX ADC comparison value used in the diagnostic ADC comparison. Valid if the diagnostic ADC comparison is run when a single channel is locked

## 8.5.4.7 Balancing Configuration, Control and Status

# 8.5.4.7.1 CB\_CELL16\_CTRL through CB\_CELL1\_CTRL **Address** **0x0318 to ** **0x0327**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD TIME\[4:0\] Reset RSVD = Reserved

TIME\[4:0\] = Sets the timer for cell\* balancing. The selection is sampled whenever *\[BAL\_GO\]* = 1 is set by the host MCU.

0x00 = 0 s = stop balancing $$ 0x01 = 10 s $$ $$ 0x02 = 30 s $$ $$ 0x03 = 60 s $$ $$ 0x04 = 300 s $$ 0x05 to 0x10 = range from 10 min to 120 min in 10-min steps 0x11 to 0x1F = range from 150 min to 540 min in 30-min steps and 600 min

# 8.5.4.7.2 VMB\_DONE\_THRESH **Address** **0x0328**

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD MB\_THR\[5:0\] Reset RSVD = Reserved

MB\_THR\[5:0\] = If *MB\_TIMER\_CTRL* is not 0x00 and BAT voltage is less than this threshold, the module balancing through GPIO3 stops. The selection is sampled whenever *\[AUX\_GO\]* = 1 is set by the host MCU. Note: To use this option, MCU enables the AUX ADC first before sending *\[BAL\_GO\]* = 1. A new threshold setting will take effect if MCU resends *\[AUX\_GO\]* = 1. It is not necessary to resend *\[BAL\_GO\]* = 1 as balancing is already running. Range from 18 V to 65 V with 1-V steps. Unused codes default to 65 V.

# 8.5.4.7.3 MB\_TIMER\_CTRL **Address** **0x0329**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD TIME\[4:0\] Reset RSVD = Reserved

TIME\[4:0\] = Sets the timer for module balancing. The selection is sampled whenever *\[BAL\_GO\]* = 1 is set by the host MCU.

0x00 = 0 s = stop balancing $$ 0x01 = 10 s $$ $$ 0x02 = 30 s $$ $$ 0x03 = 60 s $$ $$ 0x04 = 300 s $$ 0x05 to 0x10 = range from 10 min to 120 min in 10-min steps 0x11 to 0x1F = range from 150 min to 540 min in 30-min steps and 600 min

# 8.5.4.7.4 VCB\_DONE\_THRESH **Address** **0x032A**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD CB\_THR\[5:0\] Reset RSVD = Reserved

CB\_THR\[5:0\] = If a cell voltage is less than this threshold, the cell balancing on that cell stops. This threshold setting applies to all cells. The selection is sampled whenever *\[OVUV\_GO\]* = 1 is set by the host MCU. Note: To use the VCB\_DONE detection feature, host sets this threshold, then issues *\[OVUV\_GO\]* = 1 before starting CB (that is, sending *\[BAL\_GO\]* = 1). To change the VCB\_DONE threshold detection, set a new threshold then re-issue *\[OVUV\_GO\]* = 1 for the new threshold to take effect. It is not necessary to re-issue *\[BAL\_GO\]* = 1 to restart balancing in this case. Range from 2.45-V to 4-V with 25-mV steps, where 0x00 = Disables voltage based on CB\_DONE comparison 0x01 = threshold of 2.45-V 0x3F = threshold of 4-V

# 8.5.4.7.5 OTCB\_THRESH **Address** **0x032B**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD COOLOFF\[2:0\] OTCB\_THR\[3:0\] Reset RSVD = Reserved

COOLOFF\[2:0\] = Sets the COOLOFF hysteresis (resume temperature = OTCB\_THR - COOLOFF hysteresis) to resume CB when

*BAL\_CTRL1\[OTCB\_EN\]* = 1 and OTCB is detected. The MCU configures the corresponding GPIO(s) to the ADC and OTUT option. Range from 4% to 14% in steps of 2%. Unused code is set to 14%. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

OTCB\_THR\[3:0\] = Sets the OTCB threshold when *BAL\_CTRL1\[OTCB\_EN\]* = 1. The MCU configures the corresponding GPIO(s) to the ADC and OTUT option. Range from 10% to 24% in steps of 2%. Unused code is set to 24%.

# 8.5.4.7.6 BAL\_CTRL1 **Address** **0x032E**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD DUTY\[2:0\] Reset RSVD = Reserved

DUTY\[2:0\] = Selection is sampled whenever *\[BAL\_GO\]* = 1 is set by the host MCU.

$$ 0x0 = 5 s $$ $$ 0x1 = 10 s $$ $$ 0x2 = 30 s $$ $$ 0x3 = 60 s $$ $$ 0x4 = 5 min $$ $$ 0x5 = 10 min $$ $$ 0x6 = 20 min $$ $$ 0x7 = 30 min $$

# 8.5.4.7.7 BAL\_CTRL2 **Address** **0x032F**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name

RSVD CB\_PAUSE FLTSTOP\_EN OTCB\_EN BAL\_ACT\[1:0\] BAL\_GO AUTO\_BAL Reset RSVD = Reserved

CB\_PAUSE = Pauses cell balancing on all cells to allow diagnostics to run.

0 = Normal cell balancing operation 1 = Pause all cell balancing

FLTSTOP\_EN = Stops cell or module balancing if unmasked fault occurs. The selection is sampled whenever *\[BAL\_GO\]* = 1 is set by the host MCU. 0 = Balancing is continuous regardless of fault condition (excluding thermal shutdown) 1 = All CB balancing stops when any unmasked fault occurs

OTCB\_EN = Enables the OTCB detection during cell balancing. The selection is sampled whenever *\[BAL\_GO\]* = 1 is set by the host MCU. 0 = Disable OTCB detection 1 = Enable OTCB detection

BAL\_ACT\[1:0\] = Controls the device action when the MB and CB are completed. These bits are samples whenever *\[BAL\_GO\]* = 1 is set by the host MCU. The action is valid. 00 = No action 01 = Enters SLEEP 10 = Enters SHUTDOWN 11 = Reserved

BAL\_GO = Starts cell or module balancing. When written to 1, all balancing configuration registers are sampled. Any change to the configuration registers has no effect until this bit is written to 1 again. The bit is self-clearing. 0 = Ready 1 = Start balancing

AUTO\_BAL = Selects between auto or manual cell balance control. The selection is sampled whenever *\[BAL\_GO\]* = 1 is set by the host MCU. 0 = Manual cell balancing 1 = Auto cell balancing

# 8.5.4.7.8 BAL\_CTRL3 **Address** **0x0330**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

# Name RSVD BAL\_TIME\_SEL\[3:0\] BAL\_TIME\_G O Reset RSVD = Reserved

BAL\_TIME\_GO Instruct the device to report the selected CB channel (set by *\[BAL\_TIME\_SEL3:0\]* ) remaining balancing time to *BAL\_TIME* register

BAL\_TIME\_SEL\[3:0\] = Select a single CB channel to report its remaining balancing time

0x0 = CB Channel 1 0x1 = CB Channel 2: 0xF = CB Channel 16

# 8.5.4.7.9 CB\_COMPLETE1 **Address** **0x0556** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name CELL16\_ DONE

| CELL15\_ | DONE |
|:--- |:--- |
| CELL14\_ | DONE |
| CELL13\_ | DONE |
| CELL12\_ | DONE |
| CELL11\_ | DONE |
| CELL10\_ | DONE |

# CELL14\_ DONE

# CELL13\_ DONE

# CELL12\_ DONE

# CELL11\_ DONE

# CELL10\_ DONE

# CELL9\_ DONE Reset

# CELL9\_DONE to CELL16_DONE =

Cell balance completion for cell9 to cell16. This register is cleared when MCU sets *\[BAL\_GO\]* = 1. 0 = Balancing on the particular cell is still running or has not started 1 = Balancing completed on the particular cell

# 8.5.4.7.10 CB\_COMPLETE2 **Address** **0x0557**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name CELL8\_DO NE

# CELL7\_DONE CELL6\_DONE CELL5\_DONE CELL4\_DONE CELL3\_DONE CELL2\_DONE CELL1\_DONE Reset

# CELL1\_DONE to

# CELL8\_DONE =

Cell balance completion for cell1 to cell8. This register is cleared when MCU sets *\[BAL\_GO\]* = 1. 0 = Balancing on the particular cell is still running or has not started 1 = Balancing completed on the particular cell

# 8.5.4.7.11 BAL\_TIME **Address** **0x0558**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name TIME\_UNIT TIME\[6:0\] Reset

TIME\_UNIT = Indicates the unit reported by *\[TIME6:0\]* $$ 0 = sec $$ $$ 1 = min $$

TIME\[6:0\] = Report the selected CB channel remaining balancing time

If *\[TIME\_UNIT\]* = 0. Time report in sec with 5sec step If *\[TIME\_UNIT\]* = 1. Time report in min with 5min step

## 8.5.4.8 Protector Configuration and Control

# 8.5.4.8.1 OV\_THRESH **Address** **0x0009**

NVM **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name SPARE SPARE OV\_THR\[5:0\] Reset SPARE = Spare **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

OV\_THR\[5:0\] = Sets the overvoltage threshold for the OV comparator. Changes on these bits require host to send another

[OVUV_GO] = 1 command. All settings are at 25-mV steps. 0x02 to 0x0E: range from 2700 mV to 3000 mV 0x12 to 0x1E: range from 3500 mV to 3800 mV 0x22 to 0x2E: range from 4175 mV to 4475 mV All other settings will default to 2700 mV.

# 8.5.4.8.2 UV\_THRESH **Address** **0x000A**

NVM **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name SPARE SPARE UV\_THR\[5:0\] Reset SPARE = Spare

UV\_THR\[5:0\] = Sets the undervoltage threshold for the UV comparator. Changes on these bits require host to send another

[OVUV_GO] = 1 command. All settings are at 50-mV steps. 0x00 to 0x26: range from 1200 mV to 3100 mV All other settings will default to 3100 mV.

# 8.5.4.8.3 UV\_DISABLE1 **Address** **0x000C**

NVM **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name

CELL16 CELL15 CELL14 CELL13 CELL12 CELL11 CELL10 CELL9 Reset

# CELL9 to $$ CELL16 = $$

Indicate which channels shall be excluded from UV and VCB\_DONE detection 0 = UV and VCB\_DONE monitoring apply to the channel 1 = UV and VCB\_DOME monitoring are excluded from the channel

# 8.5.4.8.4 UV\_DISABLE2 **Address** **0x000D**

NVM **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name

CELL8 CELL7 CELL6 CELL5 CELL4 CELL3 CELL2 CELL1 Reset CELL8 to

# CELL1 =

Indicate which channels shall be excluded from UV and VCB\_DONE detection 0 = UV and VCB\_DONE monitoring apply to the channel 1 = UV and VCB\_DOME monitoring are excluded from the channel

# 8.5.4.8.5 OTUT\_THRESH **Address** **0x000B**

NVM **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name UT\_THR\[2:0\] OT\_THR\[4:0\] Reset

UT\_THR\[2:0\] = Sets the UT threshold for the UT comparator. Changes on these bits require host to send another *\[OTUT\_GO\]* = 1 command. The MCU configures the corresponding GPIO(s) to ADC and OTUT input. Range from 66% to 80% in steps of 2%

OT\_THR\[4:0\] = Sets the OT threshold for the OT comparator. Changes on these bits require host to send another *\[OTUT\_GO\]* = 1 command. The MCU configures the corresponding GPIO(s) to ADC and OTUT input. Range from 10% to 39% in steps of 1% Unused code defaults to 39%.

# 8.5.4.8.6 OVUV\_CTRL **Address** **0x032C**

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name VCBDONE\_ THR\_LOCK

# OVUV\_LOCK\[3:0\] OVUV\_GO OVUV\_MODE\[1:0\] Reset

VCBDONE\_THR\_LOCK = As the UV comparator is switching between UV threshold and VCBDONE threshold to measure the UV DAC or the VCBDONE DAC result for diagnostics, the UV comparator has to lock onto only one threshold before starting the AUX ADC measurement. This bit selects which threshold is locked to the UV comparator. The bit is sampled when *OVUV\_MODE\[1:0\]* is 0b11 which is locked to a single channel mode. 0 = UV threshold is selected 1 = VCBDONE threshold is selected

OVUV\_LOCK\[3:0\] = Configures a particular single channel as the OV and UV comparators input when *\[OVUV\_MOD1:0\]* = 0b11. Changes on these bits require host to send another *\[OVUV\_GO\]* = 1 command. 0x0 = Lock to Cell1 0x1 = Lock to Cell2 0x2 = Lock to Cell3: 0xF = Lock to Cell16

OVUV\_GO = Starts the OV and UV comparators. When written to 1, all OVUV configuration settings are sampled. This bit is self-clearing. 0 = Ready 1 = Start OV and UV comparators

OVUV\_MODE\[1:0\] = Sets the OV and UV comparators operation mode when *\[OVUV\_GO\]* = 1. Changes on these bits require host to send another *\[OVUV\_GO\]* = 1 command. 00 = Do not run OV and UV comparators 01 = Run the OV and UV round robin with all active cells 10 = Run the OV and UV BIST cycle. 11 = Lock OV and UV comparators to a single channel configured by *\[OVUV\_LOCK3:0\]* Note: Active cells are defined by the *ACTIVE\_CELL\[NUM\_CELL3:0\]* register.

# 8.5.4.8.7 OTUT\_CTRL **Address** **0x032D**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD OTCB\_THR\_ LOCK

# OTUT\_LOCK\[2:0\] OTUT\_GO OTUT\_MODE\[1:0\] Reset RSVD = Reserved

OTCB\_THR\_LOCK = As the OT comparator is switching between OT threshold and OTCB threshold to measure the OT or OTCB DAC threshold result for diagnostics, the OT comparator has to lock onto only one threshold before starting the AUX ADC measurement. This bit selects which threshold is locked to the OT comparator. The bit is sampled when *OTUT\_MODE\[1:0\]* = 0b11 which is locked to a single channel mode. 0 = OT threshold is selected 1 = OTCB threshold is selected

OTUT\_LOCK\[2:0\] = Configures a particular single channel as the OT and UT comparators input when *\[OTUT\_MOD1:0\]* = 0b11. Changes on these bits require host to send another *\[OTUT\_GO\]* = 1 command. 0x0 = Lock to GPIO1A 0x1 = Lock to GPIO2A: 0x7 = Lock to GPIO8A

OTUT\_GO = Starts the OT and UT comparators. When written to 1, all OTUT configuration settings are sampled. This bit is self-clearing. 0 = Ready 1 = Start OT and UT comparators

OTUT\_MODE\[1:0\] = Sets the OT and UT comparators operation mode when *\[OTUT\_GO\]* = 1. Changes on these bits require host to send another *\[OTUT\_GO\]* = 1 command. 00 = Do not run OT and UT comparators 01 = Run the OT and UT round robin with all active cells 10 = Run the OT and UT BIST cycle. 11 = Lock OT and UT comparators to a single channel configured by *\[OTUT\_LOCK3:0\]* **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## 8.5.4.9 GPIO Configuration

# 8.5.4.9.1 GPIO\_CONF1 **Address** **0x000E**

NVM **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name FAULT\_IN\_ EN

# SPI\_EN GPIO2\[2:0\] GPIO1\[2:0\] Reset

FAULT\_IN\_EN = Enables GPIO8 as an active-low input to trigger the NFAULT pin when the input signal is low.

0 = No fault input function. GPIO8 is configured based on *\[GPIO8\_CONF2:0\]* setting. 1 = GPIO8 is set as active-low input to trigger NFAULT pin, *\[GPIO8\_CONF2:0\]* setting is ignored.

SPI\_EN = Enables SPI controller on GPIO4, GPIO5 and GPIO6, GPIO7.

0 = SPI controller disabled. 1 = SPI controller enabled. Overwrite the *\[GPIO4\_CONF2:0\]*, *\[GPIO5\_CONF2:0\]*, *\[GPIO6\_CONF2:0\]*, and *\[GPIO7\_CONF2:0\]* settings. GPIO2[2:0] = Configures GPIO2.

000 = As disabled, high-Z 001 = As ADC and OTUT inputs 010 = As ADC only input 011 = As digital input 100 = As output high 101 = As output low 110 = As ADC input and weak pull-up enabled 111 = As ADC input and weak pull-down enabled GPIO1[2:0] = Configures GPIO1.

000 = As disabled, high-Z 001 = As ADC and OTUT inputs 010 = As ADC only input 011 = As digital input 100 = As output high 101 = As output low 110 = As ADC input and weak pull-up enabled 111 = As ADC input and weak pull-down enabled

# 8.5.4.9.2 GPIO\_CONF2 **Address** **0x000F**

NVM **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name SPARE RSVD GPIO4\[2:0\] GPIO3\[2:0\] Reset SPARE = Spare

GPIO4\[2:0\] = Configures GPIO4. If *\[SPI\_EN\]* = 1, these configuration bits are ignored and the pin is used as SS for SPI controller. See Section 8.3.6.1.7 for details. 000 = As disabled, high-Z 001 = As ADC and OTUT inputs 010 = As ADC only input 011 = As digital input 100 = As output high 101 = As output low 110 = As ADC input and weak pull-up enabled 111 = As ADC input and weak pull-down enabled

GPIO3\[2:0\] = Configures GPIO3. If *MB\_TIMER\_CTRL* is not 0x00, this configuration is ignored and the pin is configured for

module balancing. 000 = As disabled, high-Z 001 = As ADC and OTUT inputs 010 = As ADC only input 011 = As digital input 100 = As output high 101 = As output low 110 = As ADC input and weak pull-up enabled 111 = As ADC input and weak pull-down enabled

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

# 8.5.4.9.3 GPIO\_CONF3 **Address** **0x0010**

NVM **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name SPARE\[1:0\] GPIO6\[2:0\] GPIO5\[2:0\] Reset SPARE[1:0] = Spare

GPIO6\[2:0\] = Configures GPIO6. If *\[SPI\_EN\]* = 1, these configuration bits are ignored and the pin is used as MOSI for SPI controller. See Section 8.3.6.1.7 for details. 000 = As disabled, high-Z 001 = As ADC and OTUT inputs 010 = As ADC only input 011 = As digital input 100 = As output high 101 = As output low 110 = As ADC input and weak pull-up enabled 111 = As ADC input and weak pull-down enabled

GPIO5\[2:0\] = Configures GPIO5. If *\[SPI\_EN\]* = 1, these configuration bits are ignored and the pin is used as MISO for SPI controller. See Section 8.3.6.1.7 for details. 000 = As disabled, high-Z 001 = As ADC and OTUT inputs 010 = As ADC only input 011 = As digital input 100 = As output high 101 = As output low 110 = As ADC input and weak pull-up enabled 111 = As ADC input and weak pull-down enabled

# 8.5.4.9.4 GPIO\_CONF4 **Address** **0x0011**

NVM **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name SPARE\[1:0\] GPIO8\[2:0\] GPIO7\[2:0\] Reset SPARE[1:0] = Spare

GPIO8\[2:0\] = Configures GPIO8. If *\[FAULT\_IN\_EN\]* = 1, these configuration bits are ignored and the pin is used as an input such that an active low will trigger NFAULT. 000 = As disabled, high-Z 001 = As ADC and OTUT inputs 010 = As ADC only input 011 = As digital input 100 = As output high 101 = As output low 110 = As ADC input and weak pull-up enabled 111 = As ADC input and weak pull-down enabled

GPIO7\[2:0\] = Configures GPIO7. If *\[SPI\_EN\]* = 1, these configuration bits are ignored and the pin is used as SCLK for SPI controller. See Section 8.3.6.1.7 for details. 000 = As disabled, high-Z 001 = As ADC and OTUT inputs 010 = As ADC only input 011 = As digital input 100 = As output high 101 = As output low 110 = As ADC input and weak pull-up enabled 111 = As ADC input and weak pull-down enabled

## 8.5.4.10 SPI Controller

# 8.5.4.10.1 SPI\_CONF **Address** **0x034D**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

# Name RSVD CPOL CPHA NUMBIT\[4:0\] Reset RSVD = Reserved CPOL = Sets the SCLK polarity.

0 = Idles low and clocks high 1 = Idles high and clocks low

CPHA = Sets the edge of SCLK where data is sampled on MISO.

0 = Leading clock transition 1 = Trailing clock transition

NUMBIT\[4:0\] = SPI transaction length. Set the number of SPI bits to read/write.

$$ 00000 = 24-bit $$ $$ 00001 = 1-bit $$ $$ 00010 = 2-bit $$: $$ 10111 = 23-bit $$ All others = 23-bit

# 8.5.4.10.2 SPI\_EXE **Address** **0x0351**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD SS\_CTRL SPI\_GO Reset RSVD = Reserved SS\_CTRL = Programs the state of SS. 0 = Output low 1 = Output high

SPI\_GO = Executes the SPI transaction. This bit is self-clearing. 0 = Idle 1 = Execute the SPI

# 8.5.4.10.3 SPI\_TX3, SPI\_TX2, and SPI\_TX1 **Address** **0x034E to ** **0x0350**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** Name DATA\[7:0\] Reset

DATA\[7:0\] = Data to be used to write to SPI target device. The bits are programmed by using *SPI\_CONF\[NUMBIT4:0\]* and are clocked out of MOSI starting from the LSB *SPI\_TX1* -\> LSB *SPI\_TX2* -\> LSB *SPI\_TX3*.

# 8.5.4.10.4 SPI\_RX3, SPI\_RX2, and SPI\_RX1 **Address** **0x0520 to ** **0x522** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** Name DATA\[7:0\] Reset

# R R R R R R R R

DATA\[7:0\] = Data returned from a read during SPI transaction. Updated, starting with LSB *SPI\_RX1* -\> LSB *SPI\_RX2* -\> LSB

*SPI\_RX3*, with the number of bits set by *SPI\_CONF\[NUMBIT4:0\]* clocked in from MISO.

## 8.5.4.11 Diagnostic Control

# 8.5.4.11.1 DIAG\_OTP\_CTRL **Address** **0x0335**

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD FLIP\_FACT\_ CRC

# MARGIN\_MODE\[2:0\] MARGIN\_GO Reset RSVD = Reserved

FLIP\_FACT\_CRC = An enable bit to flip the factory CRC value. This is for factory CRC diagnostic.

0 = Normal operation. No modification of the factory CRC 1 = Flip the CRC value. This causes a factory CRC fault, *FAULT\_OTP\[FACT\_CRC\].*

MARGIN\_MODE\[2:0\] = Configures OTP Margin read mode:

0b000 = Normal Read 0b001 = Reserved 0b010 = Margin 1 Read $$ 0b011 to 0b111 = Reserved $$

MARGIN\_GO = Starts OTP Margin test set by the *\[MARGIN\_MOD\]* bit. This bit self-clears and always reads 0. 0 = Ready 1 = Start the test

# 8.5.4.11.2 DIAG\_COMM\_CTRL **Address** **0x0336**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD SPI\_ LOOPBACK

# FLIP\_TR\_ CRC Reset RSVD = Reserved

SPI\_LOOPBACK = Enables SPI loopback function to verify SPI functionality. See the Section 8.3.6.1.7 for more details. 0 = Disable 1 = Enable

FLIP\_TR\_CRC = Sends a purposely incorrect communication (during transmitting response) CRC by inverting all of the calculated CRC bits. 0 = Send CRC as calculated 1 = Send inverted CRC

# 8.5.4.11.3 DIAG\_PWR\_CTRL **Address** **0x0337**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD BIST\_NO\_ RST

# PWR\_BIST\_ GO Reset RSVD = Reserved

BIST\_NO\_RST = Use for further diagnostic if the power supply BIST detects a failure. When this bit is set to 1, and then BIST cycle is run using *\[PWR\_BIST\_GO\]*, the device will not clear the *FAULT\_PWR1* and *FAULT\_PWR2* register, and does not deassert the NFAULT signal at the end of BIST cycle. 0 = Cycle through BIST on the LDO comparators. The *FAULT\_PWR\** registers are reset to 0 and NFAULT is deasserted at the end of each LDO BIST run. 1 = Cycle through BIST on the LDO comparators. The *FAULT\_PWR\** registers are not reset to 0, and NFAULT remains asserted at the end of each LDO BIST run.

PWR\_BIST\_GO = When written to 1, the power supply BIST diagnostic will start. Any change in *\[BIST\_NO\_RST\]* has no effect until this bit is written to 1 again. The bit self-clears. 0 = Ready 1 = Start power supply BIST diagnostic.

# 8.5.4.11.4 DIAG\_CBFET\_CTRL1 **Address** **0x0338**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** Name CBFET16 to CBFET9 **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* Reset

CBFET16 to CBFET9 = Enables CBFET for CBFET diagnostic. This register is only sampled when *\[COMP\_ADC\_SEL2:0\]* = 0b100. 0 = CBFET off 1 = CBFET on

# 8.5.4.11.5 DIAG\_CBFET\_CTRL2 **Address** **0x0339**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** Name CBFET8 to CBFET1 Reset

CBFET8 to CBFET1 = Enables CBFET for CBFET diagnostic. This register is only sampled when *\[COMP\_ADC\_SEL2:0\]* = 0b100. 0 = CBFET off 1 = CBFET on

# 8.5.4.11.6 DIAG\_COMP\_CTRL1 **Address** **0x033A**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name VCCB\_THR\[4:0\] Reset

VCCB\_THR\[4:0\] = Configures the VCELL vs. AUXCELL delta. The VCELL vs. AUXCELL check is considered pass if the measured delta is less than this threshold. This threshold applies to the bus bar comparison from Main to AUX ADC as well. Range from 6 to 99mV in 3mV step

BB\_THR\[2:0\] = RSVD = Additional delta value added to the VCCB\_THR setting, used during VCELL vs. AUXCELL comparison when

comparing a cell connected above a bus bar (with the bus bar connected to a VC channel individually). Range is from 5 mV to 40 mV in 5-mV steps. Reserved

# 8.5.4.11.7 DIAG\_COMP\_CTRL2 **Address** **0x033B**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD GPIO\_THR\[2:0\] OW\_THR\[3:0\] Reset RSVD = Reserved

GPIO\_THR\[2:0\] = Configures the GPIO comparison delta threshold between Main and AUX ADC measurements. Range is from 4-mV to 32-mV in 4-mV steps

OW\_THR\[3:0\] = Configures the OW detection threshold for diagnostic comparison. This threshold applies to the CB OW and VC OW diagnostics. Range is from 500 mV to 5 V in 300-mV steps.

# 8.5.4.11.8 DIAG\_COMP\_CTRL3 **Address** **0x033C**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD CBFET\_CTRL \_GO

# OW\_SNK\[1:0\] COMP\_ADC\_SEL\[2:0\] COMP\_ADC \_GO Reset RSVD = Reserved

CBFET\_CTRL\_GO = When this GO bit = 1, device turns on the CBFET configured and turns off whichever CBFET is clear in DIAG\_CBFET\_CTRL1/2 regisetrs. This GO action is executed only if CB is not running or it's in pause, otherwise, CBFETs are controlled by regular CB control. If CBFET are turned on by this GO bit, once CB is started or resume, the CBFET controls returns to the regular CB control (and not by this GO bit action)

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

OW\_SNK\[1:0\] = Turns on current sink on VC pins, CB pins, or BBP/N pins. Changes to these bits take effect immediately. Host MCU is responsible to turn on the correct sink current before performing open wire (OW) test and to turn off the sink current after OW test is completed. 00 = All VC, BBP/N, CB pins current sink is off. 01 = Turn on current sink on all VC pins 10 = Turn on current sink on all CB pins 11 = Turn on current sink on BBP/N pins

COMP\_ADC\_SEL\[2:0\] = Enables the device diagnostic comparison through the ADC measurements. Host enables the corresponding ADCs in continuous mode before enabling this diagnostic. These bits are sampled when *\[COMP\_ADC\_GO\]* = 1. 000 = No ADC comparison is performed 001 = Cell voltage measurement check. Device compares the cell channels specified by *\[AUX\_CELL\_SEL4:0\]* against the following criteria: VCELL (from Main ADC) vs. AUXCELL (from AUX ADC) delta is less than *\[VCCB\_THR4:0\].* The *\[DRDY\_VCCB\]* = 1 when this comparison is completed. 010 = Open wire (OW) check on VC pins. MCU enables the current sink on all VC pins through the *\[OW\_SNK1:0\]* before enabling this comparison. Device compares corresponding VC pins specified by *ACTIVE\_CELL* register against the following criteria: VCELL (from Main ADC) is less than *DIAG\_COMP\_CTRL2 \[OW\_THR3:0\]*. The *\[DRDY\_VC\_OW\]* = 1 when the comparison is completed. 011 = Open wire (OW) check on CB pins MCU enables the current sink on all VC pins through the *\[OW\_SNK1:0\]* before enabling this comparison. Device compares corresponding CB pins specified by *\[AUX\_CELL\_SEL4:0\]* against the following criteria: AUXCELL (from AUX ADC) is less than *DIAG\_COMP\_CTRL2 \[OW\_THR3:0\]*. The *\[DRDY\_CBOW\]* = 1 when the comparison is completed. 100 = CBFET check. MCU preconfigures the following before starting this check:

- • Pause cell balancing if balancing is enabled. - • Enable the CBFET configured by *DIAG\_CBFET\_CTRL1/2* registers. - • Configure the *\[EXTD\_CBFET\]* to decide if all CBFET returns to pause state (that is, turn off all CBFET) or  remains their status as specified by *DIAG\_CBFET\_CTRL1/2* registers.

When this test starts, device will turn on CBFET specified by *DIAG\_CBFET\_CTRL1/2* registers and then compares the channel specified by *\[AUX\_CELL\_SEL4:0\]* with the following criteria: AUXCELL (from AUX ADC) \< 1/3 of VCELL (from Main ADC). *\[DRDY\_CBFET\]* = 1 when the comparison is completed. 101 = GPIO measurement check (applies to GPIO configured as ADC and OTUT inputs or ADC only input). Device compares main GPIO measurement vs. AUX GPIO measurements delta is less than *\[GPIO\_THR2:0\]*. The *\[DRDY\_GPIO\]* = 1 when the comparison is completed. Other codes: No ADC comparison is performed

COMP\_ADC\_GO = Device starts diagnostic test specified by *\[COMP\_ADC\_SEL2:0\]* setting. When this bit is written to 1, the selected

*\[COMP\_ADC\_SEL2:0\]* is sampled. Change of *\[COMP\_ADC\_SEL2:0\]* setting has no effect unless this GO bit is written to 1 again. This bit is cleared to 0 in read. 0 = Ready. Writing 0 has no effect 1 = Star diagnostic selected by *\[COMP\_ADC\_SEL2:0\]*

# 8.5.4.11.9 DIAG\_COMP\_CTRL4 **Address** **0x033D**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD COMP\_ FAULT\_INJ

# LPF\_FAULT \_INJ Reset RSVD = Reserved

COMP\_FAULT\_INJ = Injects fault to the ADC comparison logic. If any ADC comparison diagnostic is run with this bit set, the comparison result is expected to fail. 0 = Disable 1 = Enable

LPF\_FAULT\_INJ = Injects fault condition to the diagnostic LPF during LPF diagnostic. The *FAULT\_COMP\_MISC\[LPF\_FAIL\]* is expected to be set. 0 = Disable 1 = Enable **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

# 8.5.4.11.10 DIAG\_PROT\_CTRL **Address** **0x033E**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD PROT\_BIST \_NO\_RST Reset RSVD = Reserved

PROT\_BIST\_NO\_RST = Use for further diagnostic if the protector BIST detects a failure. When this bit is set to 1, the device will not clear the *FAULT\_OV1/2*, *FAULT\_UV1/2*, *FAULT\_OT*, and *FAULT\_UT* registers. The NFAULT signal will be latched once it is asserted. Note: Host ensures there is no fault before starting the BIST run with this bit set to 0. 0 = During BIST run, when the device asserts a fault to check the protector comparators and MUX and asserts the correct OV, UV, OT, and UT fault bits the NFAULT pin. When this bit is 0, the device clears the fault and deasserts NFAULT before switching to the next channel. 1 = During BIST run, the fault created during the test will not be cleared before switching to next cell or GPIO channel. The NFAULT pin is latched once it is asserted.

## 8.5.4.12 Fault Configuration and Reset

# 8.5.4.12.1 FAULT\_MSK1 **Address** **0x0016**

NVM **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name

MSK\_PROT MSK\_UT MSK\_OT MSK\_UV MSK\_OV MSK\_COMP MSK\_SYS MSK\_PWR Reset

MSK\_PROT = Masks the *FAULT\_PROT\** registers to trigger NFAULT.

0 = Assert NFAULT if any bit from *FAULT\_PROT\** is set to 1. 1 = No NFAULT action regardless of *FAULT\_PROT\** bit status.

MSK\_UT = Masks the *FAULT\_UT\** registers to trigger NFAULT.

0 = Assert NFAULT if any bit from *FAULT\_UT\** is set to 1. 1 = No NFAULT action regardless of *FAULT\_UT\** bit status.

MSK\_OT = Masks the *FAULT\_OT\** registers to trigger NFAULT.

0 = Assert NFAULT if any bit from *FAULT\_OT\** is set to 1. 1 = No NFAULT action regardless of *FAULT\_OT\** bit status.

MSK\_UV = Masks the *FAULT\_UV\** registers to trigger NFAULT.

0 = Assert NFAULT if any bit from *FAULT\_UV\** is set to 1. 1 = No NFAULT action regardless of *FAULT\_UV\** bit status.

MSK\_OV = Masks the *FAULT\_OV\** registers to trigger NFAULT.

0 = Assert NFAULT if any bit from *FAULT\_OV\** is set to 1. 1 = No NFAULT action regardless of *FAULT\_OV\** bit status.

MSK\_COMP = Masks the *FAULT\_COMP\_\** registers to trigger NFAULT.

0 = Assert NFAULT if any bit from *FAULT\_COMP\_\** is set to 1. 1 = No NFAULT action regardless of *FAULT\_COM\_\** bit status.

MSK\_SYS = To mask the NFAULT assertion from any *FAULT\_SYS* register bit.

0 = Assert NFAULT if any bit from *FAULT\_SYS* is set to 1. 1 = No NFAULT action regardless of *FAULT\_SYS* bit status.

MSK\_PWR = To mask the NFAULT assertion from any *FAULT\_PWR1* to *FAULT\_PWR3* register bit.

0 = Assert NFAULT if any bit from *FAULT\_PWR1* to *FAULT\_PWR3* is set to 1. 1 = No NFAULT action regardless of *FAULT\_PWR1* to *FAULT\_PWR3* bit status.

# 8.5.4.12.2 FAULT\_MSK2 **Address** **0x0017**

NVM **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name SPARE\[1\] MSK\_OTP\_ CRC

# MSK\_OTP\_ DATA

# MSK\_COMM3

# \_FCOMM

# MSK\_COMM3

# \_FTONE

# MSK\_COMM3

# \_HB

# MSK\_COMM2 MSK\_COMM1 Reset SPARE[1] = Spare

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

MSK\_OTP\_CRC = Masks the *FAULT\_OTP* register ( *\[CUST\_CRC\]* and *\[FACT\_CRC\]* only) on NFAULT triggering.

0 = Assert NFAULT if any bit described above is set to 1. 1 = No NFAULT action regardless of the status of the bits described above.

MSK\_OTP\_DATA = Masks the *FAULT\_OTP* register (all bits except *\[CUST\_CRC\]* and *\[FACT\_CRC\]* ) on NFAULT triggering.

0 = Assert NFAULT if any bit described above is set to 1. 1 = No NFAULT action regardless of the status of the bits described above.

# MSK\_COMM3\_FCOMM $$ = $$

Masks *FAULT\_COMM3\[FCOMM\_DET\]* fault on NFAULT triggering. 0 = Assert NFAULT if *FAULT\_COMM3\[FCOMM\_DET\]* is set to 1. 1 = No NFAULT action regardless of *FAULT\_COMM3\[FCOMM\_DET\]* status.

# MSK\_COMM3\_FTONE $$ = $$

Masks *FAULT\_COMM3\[FTONE\_DET\]* fault on NFAULT triggering. 0 = Assert NFAULT if *FAULT\_COMM3\[FTONE\_DET\]* is set to 1. 1 = No NFAULT action regardless of *FAULT\_COMM3\[FTONE\_DET\]* status.

MSK\_COMM3\_HB = Masks *FAULT\_COMM3\[HB\_FAST\]* or *\[HB\_FAIL\]* faults on NFAULT triggering.

0 = Assert NFAULT if *FAULT\_COMM3\[HB\_FAST\]* or *\[HB\_FAIL\]* is set to 1. 1 = No NFAULT action regardless of *FAULT\_COMM3\[HB\_FAST\]* or *\[HB\_FAIL\]* status.

MSK\_COMM2 = Masks *FAULT\_COMM2* register on NFAULT triggering.

0 = Assert NFAULT if any bit from *FAULT\_COMM2* register is set to 1. 1 = No NFAULT action regardless of *FAULT\_COMM2* register bit status.

MSK\_COMM1 = Masks *FAULT\_COMM1* register on NFAULT triggering.

0 = Assert NFAULT if any bit from *FAULT\_COMM1* register is set to 1. 1 = No NFAULT action regardless of *FAULT\_COMM1* register bit status.

# 8.5.4.12.3 FAULT\_RST1 **Address** **0x0331**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name

RST\_PROT RST\_UT RST\_OT RST\_UV RST\_OV RST\_COMP RST\_SYS RST\_PWR Reset

RST\_PROT = Resets the *FAULT\_PROT1* and *FAULT\_PROT2* registers to 0x00. 0 = No reset 1 = Reset registers to 0x00

RST\_UT = Resets all *FAULT\_UT* registers to 0x00. 0 = No reset 1 = Reset registers to 0x00

RST\_OT = Resets all *FAULT\_OT* registers to 0x00. 0 = No reset 1 = Reset registers to 0x00

RST\_UV = Resets all *FAULT\_UV\** registers to 0x00. 0 = No reset 1 = Reset registers to 0x00

RST\_OV = Resets all *FAULT\_OV\** registers to 0x00. 0 = No reset 1 = Reset registers to 0x00

RST\_COMP = Resets all *FAULT\_COMP\_\** registers to 0x00. 0 = No reset 1 = Reset registers to 0x00

RST\_SYS = To reset the *FAULT\_SYS* register to 0x00. This bit self-clears to 0 after writing to 1. 0 = Do not reset 1 = Reset to 0x00

RST\_PWR = To reset the *FAULT\_PWR1* to *FAULT\_PWR3* registers to 0x00. This bit self-clears to 0 after writing to 1. 0 = Do not reset 1 = Reset to 0x00

# 8.5.4.12.4 FAULT\_RST2 **Address** **0x0332**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD RST\_OTP \_CRC

# RST\_OTP\_ DATA

# RST\_COMM3

# \_FCOMM

# RST\_COMM3

# \_FTONE

# RST\_COMM3

# \_HB

# RST\_COMM2 RST\_COMM1 **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* Reset RSVD = Reserved

RST\_OTP\_CRC = Resets the *FAULT\_OTP* register ( *\[CUST\_CRC\]* and *\[FACT\_CRC\]* only). 0 = No reset 1 = Reset the register to 0x00

RST\_OTP\_DATA = Resets the *FAULT\_OTP* register ( *\[SEC\_DETECT\]* and *\[DED\_DETECT\]* only). 0 = No reset 1 = Reset the register to 0x00

# RST\_COMM3\_FCOMM $$ = $$

Resets *FAULT\_COMM3\[FCOMM\_DET\].* 0 = No reset 1 = Reset the related bit to 0

# RST\_COMM3\_FTONE $$ = $$

Resets *FAULT\_COMM3\[FTONE\_DET\]*. 0 = No reset 1 = Reset the related bit to 0

# RST\_COMM3\_HB = Resets FAULT\_COMM3\[HB\_FAST\] and \[HB\_FAIL\] bits. 0 = No reset 1 = Reset the related bits to 0

RST\_COMM2 = Resets *FAULT\_COMM2*, *DEBUG\_COML\**, and *DEBUG\_COMM\_COMH\** registers. 0 = No reset 1 = Reset registers to 0x00

RST\_COMM1 = Resets *FAULT\_COMM1* and *DEBUG\_COMM\_UART\** registers. 0 = No reset 1 = Reset registers to 0x00

## 8.5.4.13 Fault Status

# 8.5.4.13.1 FAULT\_SUMMARY

## This register is the soft version of the NFAULT. **Address** **0x052D** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name FAULT\_PRO T

# FAULT\_ COMP\_ADC

# FAULT\_OTP FAULT\_ COMM

# FAULT\_OTUT FAULT\_OVUV FAULT\_SYS FAULT\_PWR Reset

FAULT\_PROT = This bit is set if *\[MSK\_PROT\]* = 0 and any of the *FAULT\_PROT1* or *FAULT\_PROT2* register bits is set.

0 = No protector (OVUV, OTUT comparators) fault. 1 = Protector fault is detected

FAULT\_COMP\_ADC = This bit is set if *\[MSK\_COMP\]* = 0 and any of the following registers is set:

# • • FAULT\_COMP\_VCCB1/2

- *• FAULT\_COMP\_VCOW1/2* - *• FAULT\_COMP\_CBOW1/2* - *• FAULT\_COMP\_CBFET1/2* - *• FAULT\_COMP\_GPIO* - *• FAULT\_COMP\_MISC*

0 = No ADC comparison fault (that is, none of the *FAULT\_COMP\_\** registers are set). 1 = ADC comparison fault is detected.

FAULT\_OTP = This bit is set if *\[MSK\_OTP\]* = 0 and any of the *FAULT\_OTP* register bits is set.

0 = No OTP-related fault detected or OTP faults are masked. 1 = OTP-related fault is detected.

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

FAULT\_COMM = This bit is set if any of the following is true:

- *• \[MSK\_COMM1\]* = 0 and any of the *FAULT\_COMM1* register bits is set. - *• \[MSK\_COMM2\]* = 0 and any of the *FAULT\_COMM2* register bits is set. - *• \[MSK\_COMM3\_HB\]* = 0 and the *FAULT\_COMM3\[HB\_FAST\]* bit or *\[HB\_FAIL\]* bit is set. - *• \[MSK\_COMM3\_FTONE\]* = 0 and the *FAULT\_COMM3\[FTONE\_DET\]* is set. - *• \[MSK\_COMM3\_FCOMM\]* = 0 and if *FAULT\_COMM3\[FCOMM\_DET\]* is set.

0 = No UART, VIF, or FTONE fault is detected, or UART, VIF, and FTONE faults are masked. 1 = UART, VIF, or UT fault is detected.

FAULT\_OTUT = This bit is set if any of the following is true:

- *• \[MSK\_OT\]* = 0 and any of the *FAULT\_OT1* or *FAULT\_OT2* bits is set. - *• \[MSK\_UT\]* = 0 and any of the *FAULT\_UT1* or *FAULT\_UT2* bits is set.

0 = No OT or UT fault is detected, or OT and UT faults are masked. 1 = OT or UT fault is detected

FAULT\_OVUV = This bit is set if any of the following is true:

- *• \[MSK\_OV\]* = 0 and any of the *FAULT\_OV1* or *FAULT\_OV2* bits is set. - *• \[MSK\_UV\]* = 0 and any of the *FAULT\_UV1* or *FAULT\_UV2* bits is set.

0 = No OV or UV fault is detected, or OV and UV faults are masked. 1 = OV or UV fault is detected.

FAULT\_SYS = This bit is set if *\[MSK\_SYS\]* = 0 and any of the *FAULT\_SYS* register bits is set.

0 = No system related fault detected or system faults are masked. 1 = System related fault is detected.

FAULT\_PWR = This bit is set if *\[MSK\_PWR\]* = 0 and any of the *FAULT\_PWR1* to *FAULT\_PWR3* register bits is set.

0 = No power rail related fault is detected or power rail faults are masked. 1 = Power rail related fault is detected.

# 8.5.4.13.2 FAULT\_COMM1 **Address** **0x0530**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD UART\_TR UART\_RR UART\_RC COMMCLR \_DET

# STOP\_DET Reset RSVD = Reserved

| UART\_TR = Indicates a UART FAULT is detected when transmitting a response frame. Further details of the fault information | are available in the DEBUG\_UART\_RR\_TR register. | 0 = No fault | 1 = Fault |
|:--- |:--- |:--- |:--- |
| UART\_RR = Indicates a UART FAULT is detected when receiving a response frame. Further details of the fault information are | available in the DEBUG\_UART\_RR\_TR register. | 0 = No fault | 1 = Fault |
| UART\_RC = Indicates a UART FAULT is detected during receiving a command frame. Further details of the fault information | are available in the DEBUG\_UART\_RC register. | 0 = No fault | 1 = Fault |
| COMMCLR\_DET = A UART communication clear signal is detected. A detection of SLEEPtoACTIVE ping in ACTIVE or SLEEP mode | or detection of WAKE pin in ACTIVE mode will also set this bit. | 0 = No UART Clear | 1 = UART Clear detected |
| STOP\_DET = Indicates an unexpected STOP condition is received. A detection of SLEEPtoACTIVE signal in ACTIVE mode will | also set this bit. | 0 = No fault | 1 = Fault |

UART\_RR = Indicates a UART FAULT is detected when receiving a response frame. Further details of the fault information are available in the *DEBUG\_UART\_RR\_TR* register. 0 = No fault 1 = Fault

UART\_RC = Indicates a UART FAULT is detected during receiving a command frame. Further details of the fault information are available in the *DEBUG\_UART\_RC* register. 0 = No fault 1 = Fault

COMMCLR\_DET = A UART communication clear signal is detected. A detection of SLEEPtoACTIVE ping in ACTIVE or SLEEP mode or detection of WAKE pin in ACTIVE mode will also set this bit. 0 = No UART Clear 1 = UART Clear detected

STOP\_DET = Indicates an unexpected STOP condition is received. A detection of SLEEPtoACTIVE signal in ACTIVE mode will also set this bit. 0 = No fault 1 = Fault

# 8.5.4.13.3 FAULT\_COMM2 **Address** **0x0531** **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name

COML\_TR COML\_RR COML\_RC COML\_BIT COMH\_TR COMH\_RR COMH\_RC COMH\_BIT Reset

| COML\_TR = Indicates a COML byte level fault is detected when transmitting a response frame. Further details of the fault | information are available in the DEBUG\_COML\_RR\_TR register. | 0 = No fault | 1 = Fault |
|:--- |:--- |:--- |:--- |
| COML\_RR = Indicates a COML byte level fault is detected when receiving a response frame. Further details of the fault | information are available in the DEBUG\_COML\_RR\_TR register. | 0 = No fault | 1 = Fault |
| COML\_RC = Indicates a COML byte level fault is detected when receiving a command frame. Further details of the fault | information are available in the DEBUG\_COML\_RR\_RC register. | 0 = No fault | 1 = Fault |
| COML\_BIT = Indicates a COML bit level fault is detected which would cause at least one byte level fault. Further details of the | fault information are available in the DEBUG\_COML\_BIT register. | 0 = No fault | 1 = Fault |
| COMH\_TR = Indicates a COMH byte level fault is detected when transmitting a response frame. Further details of the fault | information are available in the DEBUG\_COMH\_RR\_TR register. | 0 = No fault | 1 = Fault |
| COMH\_RR = Indicates a COMH byte level fault is detected when receiving a response frame. Further details of the fault | information are available in the DEBUG\_COMH\_RR\_TR register. | 0 = No fault | 1 = Fault |
| COMH\_RC = Indicates a COMH byte level fault is detected when receiving a command frame. Further details of the fault | information are available in the DEBUG\_COMH\_RR\_RC register. | 0 = No fault | 1 = Fault |
| COMH\_BIT = Indicates a COMH bit level fault is detected which would cause at least one byte level fault. Further details of the | fault information are available in the DEBUG\_COMH\_BIT register. | 0 = No fault | 1 = Fault |

COML\_RR = Indicates a COML byte level fault is detected when receiving a response frame. Further details of the fault information are available in the *DEBUG\_COML\_RR\_TR* register. 0 = No fault 1 = Fault

COML\_RC = Indicates a COML byte level fault is detected when receiving a command frame. Further details of the fault information are available in the *DEBUG\_COML\_RR\_RC* register. 0 = No fault 1 = Fault

COML\_BIT = Indicates a COML bit level fault is detected which would cause at least one byte level fault. Further details of the fault information are available in the *DEBUG\_COML\_BIT* register. 0 = No fault 1 = Fault

COMH\_TR = Indicates a COMH byte level fault is detected when transmitting a response frame. Further details of the fault information are available in the *DEBUG\_COMH\_RR\_TR* register. 0 = No fault 1 = Fault

COMH\_RR = Indicates a COMH byte level fault is detected when receiving a response frame. Further details of the fault information are available in the *DEBUG\_COMH\_RR\_TR* register. 0 = No fault 1 = Fault

COMH\_RC = Indicates a COMH byte level fault is detected when receiving a command frame. Further details of the fault information are available in the *DEBUG\_COMH\_RR\_RC* register. 0 = No fault 1 = Fault

COMH\_BIT = Indicates a COMH bit level fault is detected which would cause at least one byte level fault. Further details of the fault information are available in the *DEBUG\_COMH\_BIT* register. 0 = No fault 1 = Fault

# 8.5.4.13.4 FAULT\_COMM3 **Address** **0x0532** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD FCOMM\_DET FTONE\_DET HB\_FAIL HB\_FAST Reset RSVD = Reserved

FCOMM\_DET = Received communication transaction with the Fault Status bits set by any of the upper stack device(s).

0 = Fault Status are clear, indicating no fault is detected from any of the upper stack device(s). 1 = Fault Status are set from the receiving communication transaction.

FTONE\_DET = Indicates a FAULT TONE is received. Detection is monitoring the COML side if *\[DIR\_SEL\]* = 0 and vice versa.

0 = No FAULT TONE detected 1 = FAULT TONE detected

HB\_FAIL = Indicates HEARTBEAT is not received within an expected time. Detection is monitoring the COML side if

*\[DIR\_SEL\]* = 0 and vice versa. 0 = No fault 1 = Fault

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

HB\_FAST = Indicates HEARTBEAT is received too frequently. Detection is monitoring the COML side if *\[DIR\_SEL\]* = 0 and vice versa. This bit may also be set when *\[FTONE\_DET\]* = 1 depends on how soon the FAULT TONE is detected from the previous HEATBEAT 0 = No fault 1 = Fault

# 8.5.4.13.5 FAULT\_OTP **Address** **0x0535** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name

RSVD DED\_DET SEC\_DET CUST\_CRC FACT\_CRC CUSTLDERR FACTLDERR GBLOVERR Reset RSVD = Reserved

DED\_DET = Indicates a DED error has occurred during the OTP load. (Unknown during encoding) 0 = No fault 1 = Fault

SEC\_DET = Indicates a SEC error has occurred during the OTP load. (Unknown during encoding) 0 = No fault 1 = Fault

CUST\_CRC = Indicates a CRC error has occurred in the customer register space. 0 = No fault 1 = Fault

FACT\_CRC = Indicates a CRC error has occurred in the factory register space. 0 = No fault 1 = Fault

CUSTLDERR = Indicates errors during the customer space OTP load process. Read *OTP\_CUST1\_STAT* and

*OTP\_CUST2\_STAT* registers for the specific error condition. This error bit is set if one of the following is true:

- • No Customer OTP page is programmed. - • The highest Customer OTP page has a *\[FMTERR\]*. - • The highest Customer OTP page has *\[TRY\]* = 1 and is not *\[PROGOK\]*. - • LOADERR happened on the selected Customer OTP page.

Information received from the device with this error must not be considered reliable. Writing *\[RST\_OTP\_DATA\]* = 1 does not reset this bit. To recheck this error, a device reset or HW\_RESET is needed. 0 = No fault 1 = Fault

FACTLDERR = Indicates errors during the factory space OTP load process. This error bit is set if one of the following is true:

- • No factory OTP page is programmed. - • The highest factory OTP page has a *\[FMTERR\].* - • The highest factory OTP page has *\[TRY\]* = 1 and is not *\[PROGOK\].* - • LOADERR happened on the selected factory OTP page.

Information received from the device with this error must not be considered reliable. Writing *\[RST\_OTP\_DATA\]* = 1 does not reset this bit. To recheck this error, a device reset or HW\_RESET is needed. 0 = No fault 1 = Fault

GBLOVERR = Indicates that on overvoltage error is detected on one of the OTP pages. Read *OTP\_CUST1\_STAT* and

*OTP\_CUST2\_STAT* registers to determine the specific page(s). Information received from the device with this error must not be considered reliable. Writing *\[RST\_OTP\_DATA\]* = 1 does not reset this bit. To clear this bit, a device reset or HW\_RESET is needed. Repeat the programming procedure on a different page (if available) will force the device to re-evaluate the condition. 0 = No fault 1 = Fault

# 8.5.4.13.6 FAULT\_SYS **Address** **0x0536** **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name LFO RSVD GPIO DRST CTL CTS TSHUT TWARN Reset

LFO = Indicated LFO frequency is outside an expected range 0 = No fault detected 1 = Fault detected RSVD = Reserved

GPIO = Indicates GPIO8 detects a FAULT input when *GPIO\_CONF1\[FAULT\_IN\_EN\]* = 1.

0 = No fault detected 1 = FAULT input detected

DRST = Indicates a digital reset has occurred.

0 = No digital reset 1 = Digital reset has occurred

| CTL = Indicates a long communication timeout occurred. Device action is configured by \[CTL\_ACT\]. This bit is not | observable if the action is set to device shutdown. | 0 = No fault | 1 = Long communication timeout occurs. Observable if long timeout action is set to SLEEP. |
|:--- |:--- |:--- |:--- |
| CTS = Indicates a short communication timeout occurred. No action from the device. This can be served as an alert to | system before reaching long communication timeout. | 0 = No fault | 1 = Short communication timeout occurs |
| TSHUT = Indicates the previous shutdown was a thermal shutdown, in which the die temperature (die temp 2) is higher than | the thermal shutdown threshold. | 0 = Die temperature is less than thermal shutdown threshold | 1 = The previous shutdown was a thermal shutdown |

CTS = Indicates a short communication timeout occurred. No action from the device. This can be served as an alert to system before reaching long communication timeout. 0 = No fault 1 = Short communication timeout occurs

TSHUT = Indicates the previous shutdown was a thermal shutdown, in which the die temperature (die temp 2) is higher than the thermal shutdown threshold. 0 = Die temperature is less than thermal shutdown threshold 1 = The previous shutdown was a thermal shutdown

TWARN = Indicates the die temperature (die temp 2) is higher than the *TWARN\_THR\[1:0\]* setting. No action is taken by the device at the moment yet. This serves as a warning signal that the die temperature is approaching thermal shutdown. 0 = Die temperature is less than *TWARN\_THR\[1:0\]* 1 = Die temperature is greater than *TWARN\_THR\[1:0\]*

# 8.5.4.13.7 FAULT\_PROT1 **Address** **0x053A** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD TPARITY\_ FAIL

# VPARITY\_ FAIL Reset RSVD = Reserved

TPARITY\_FAIL = Indicates a parity fault is detected on any of the following OTUT related configurations:

- • OT or UT threshold setting - *• \[OTUT\_MODE1:0\]* setting - *• GPIO\_CONF1...4* settings 0 = No fault 1 = Fault

VPARITY\_FAIL = Indicates a parity fault is detected on any of the following OVUV related configurations:

- • OV or UV threshold setting - *• \[OVUV\_MODE1:0\]* setting - *• \[NUM\_CELL3:0\]* setting 0 = No fault 1 = Fault

# 8.5.4.13.8 FAULT\_PROT2 **Address** **0x053B**

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name

RSVD BIST\_ABORT TPATH\_FAIL VPATH\_FAIL UTCOMP\_ FAIL

| OTCOMP\_ | FAIL |
|:--- |:--- |
| OVCOMP\_ | FAIL |
| UVCOMP\_ | FAIL |

# OVCOMP\_ FAIL

# UVCOMP\_ FAIL Reset RSVD = Reserved

BIST\_ABORT = Indicates either OVUV or OTUT BIST run is aborted. 0 = BIST runs to completion 1 = BIST abort

TPATH\_FAIL = Indicates a fault is detected along the OTUT signal path during BIST test. 0 = No fault 1 = Fault

VPATH\_FAIL = Indicates a fault is detected along the OVUV signal path during BIST test. 0 = No fault 1 = Fault

UTCOMP\_FAIL = Indicates the UT comparator fails during BIST test. 0 = No fault 1 = Fault

OTCOMP\_FAIL = Indicates the OT comparator fails during BIST test. 0 = No fault 1 = Fault

OVCOMP\_FAIL = Indicates the OV comparator fails during BIST test. 0 = No fault 1 = Fault

UVCOMP\_FAIL = Indicates the UV comparator fails during BIST test. 0 = No fault 1 = Fault

# 8.5.4.13.9 FAULT\_OV1 **Address** **0x053C** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name

OV16\_DET OV15\_DET OV14\_DET OV13\_DET OV12\_DET OV11\_DET OV10\_DET OV9\_DET Reset

# OV9\_DET to OV16\_DET $$ = $$

OV fault status for Cell9 to Cell16, results are from the OV comparator detection.

# 8.5.4.13.10 FAULT\_OV2 **Address** **0x053D** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name

OV8\_DET OV7\_DET OV6\_DET OV5\_DET OV4\_DET OV3\_DET OV2\_DET OV1\_DET Reset

OV1\_DET to OV8\_DET = OV fault status for Cell1 to Cell8, results are from the OV comparator detection.

# 8.5.4.13.11 FAULT\_UV1 **Address** **0x053E** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name

UV16\_DET UV15\_DET UV14\_DET UV13\_DET UV12\_DET UV11\_DET UV10\_DET UV9\_DET Reset

# UV9\_DET to UV16\_DET $$ = $$

UV fault status for Cell9 to Cell16, results are from the UV comparator detection. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

# 8.5.4.13.12 FAULT\_UV2 **Address** **0x053F** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name

UV8\_DET UV7\_DET UV6\_DET UV5\_DET UV4\_DET UV3\_DET UV2\_DET UV1\_DET Reset

UV1\_DET to UV8\_DET = UV fault status for Cell1 to Cell8, results are from the UV comparator detection.

# 8.5.4.13.13 FAULT\_OT **Address** **0x0540** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name

OT8\_DET OT7\_DET OT6\_DET OT5\_DET OT4\_DET OT3\_DET OT2\_DET OT1\_DET Reset

OT1\_DET to OT8\_DET = OT fault status for GPIO1 to GPIO8, results are from the OT comparator detection.

# 8.5.4.13.14 FAULT\_UT **Address** **0x0541** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name

UT8\_DET UT7\_DET UT6\_DET UT5\_DET UT4\_DET UT3\_DET UT2\_DET UT1\_DET Reset

UT1\_DET to UT8\_DET = UT fault status for GPIO1 to GPIO8, results are from the UT comparator detection.

# 8.5.4.13.15 FAULT\_COMP\_GPIO **Address** **0x0543** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name

GPIO8\_FAIL GPIO7\_FAIL GPIO6\_FAIL GPIO5\_FAIL GPIO4\_FAIL GPIO3\_FAIL GPIO2\_FAIL GPIO1\_FAIL Reset

# GPIO1\_FAIL to GPIO8_FAIL =

Indicates ADC vs. AUX ADC GPIO measurement diagnostic results for GPIO1 to GPIO8. 0 = Diagnostic pass 1 = Diagnostic fail. GPIO from Main ADC vs. AUX ADC measurement is greater than *\[GPIO\_THR2:0\]*

# 8.5.4.13.16 FAULT\_COMP\_VCCB1 **Address** **0x0545** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name CELL16\_FAI L

# CELL15\_FAIL

CELL14\_FAIL CELL13\_FAIL CELL12\_FAIL CELL11\_FAIL CELL10\_FAIL CELL9\_FAIL Reset

# CELL9\_FAIL to CELL16_FAIL =

Indicates voltage diagnostic results for cell9 to cell16. 0 = Diagnostic pass 1 = Diagnostic fail. VCELL vs. AUXCELL measurement is greater than *\[VCCB\_THR4:0\]*

# 8.5.4.13.17 FAULT\_COMP\_VCCB2 **Address** **0x0546**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name CELL8\_FAI L

# CELL7\_FAIL

CELL6\_FAIL CELL5\_FAIL CELL4\_FAIL CELL3\_FAIL CELL2\_FAIL CELL1\_FAIL

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated Reset

# CELL1\_FAIL to CELL8_FAIL =

Indicates voltage diagnostic results for cell1 to cell8. 0 = Diagnostic pass 1 = Diagnostic fail. VCELL vs. AUXCELL measurement is greater than *\[VCCB\_THR4:0\]*

# 8.5.4.13.18 FAULT\_COMP\_VCOW1 **Address** **0x0548** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name VCOW16 \_FAIL

| VCOW15 | \_FAIL |
|:--- |:--- |
| VCOW14 | \_FAIL |
| VCOW13 | \_FAIL |
| VCOW12 | \_FAIL |
| VCOW11 | \_FAIL |
| VCOW10 | \_FAIL |

# VCOW14 \_FAIL

# VCOW13 \_FAIL

# VCOW12 \_FAIL

# VCOW11 \_FAIL

# VCOW10 \_FAIL

# VCOW9\_FAIL Reset

# VCOW9\_FAIL to VCOW16_FAIL =

Indicates VC OW diagnostic results for cell9 to cell 16. 0 = Diagnostic pass 1 = Diagnostic fail. VCELL measurement is less than *\[OW\_THR3:0\]*

# 8.5.4.13.19 FAULT\_COMP\_VCOW2 **Address** **0x0549** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name VCOW8\_FA IL

# VCOW7\_FAIL

VCOW6\_FAIL VCOW5\_FAIL VCOW4\_FAIL VCOW3\_FAIL VCOW2\_FAIL VCOW1\_FAIL Reset

# VCOW1\_FAIL to VCOW8_FAIL =

Indicates VC OW diagnostic results for cell1 to cell 8. 0 = Diagnostic pass 1 = Diagnostic fail. VCELL measurement is less than *\[OW\_THR3:0\]*

# 8.5.4.13.20 FAULT\_COMP\_CBOW1 **Address** **0x054B** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name CBOW16\_ FAIL

| CBOW15\_ | FAIL |
|:--- |:--- |
| CBOW14\_ | FAIL |
| CBOW13\_ | FAIL |
| CBOW12\_ | FAIL |
| CBOW11\_ | FAIL |
| CBOW10\_ | FAIL |

# CBOW14\_ FAIL

# CBOW13\_ FAIL

# CBOW12\_ FAIL

# CBOW11\_ FAIL

# CBOW10\_ FAIL

# CBOW9\_FAIL Reset

# CBOW9\_FAIL to CBOW16_FAIL =

Results of the CB OW diagnostic for CB FET9 to CB FET16. 0 = Pass 1 = Fail

# 8.5.4.13.21 FAULT\_COMP\_CBOW2 **Address** **0x054C**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name CBOW8\_FA IL

# CBOW7\_FAIL

CBOW6\_FAIL CBOW5\_FAIL CBOW4\_FAIL CBOW3\_FAIL CBOW2\_FAIL CBOW1\_FAIL Reset

# CBOW1\_FAIL to CBOW8_FAIL =

Results of the CB OW diagnostic for CB FET1 to CB FET8. 0 = Pass 1 = Fail

# 8.5.4.13.22 FAULT\_COMP\_CBFET1 **Address** **0x054E** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

# Name CBFET16\_ FAIL

| CBFET15\_ | FAIL |
|:--- |:--- |
| CBFET14\_ | FAIL |
| CBFET13\_ | FAIL |
| CBFET12\_ | FAIL |
| CBFET11\_ | FAIL |
| CBFET10\_ | FAIL |

# CBFET14\_ FAIL

# CBFET13\_ FAIL

# CBFET12\_ FAIL

# CBFET11\_ FAIL

# CBFET10\_ FAIL

# CBFET9\_FAIL Reset

# CBFET9\_FAIL to CBFET16_FAIL =

Results of the CB FET diagnostic for CB FET9 to CB FET16. 0 = Pass 1 = Fail

# 8.5.4.13.23 FAULT\_COMP\_CBFET2 **Address** **0x054F** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name CBFET8\_FA IL

# CBFET7\_FAIL

CBFET6\_FAIL CBFET5\_FAIL CBFET4\_FAIL CBFET3\_FAIL CBFET2\_FAIL CBFET1\_FAIL Reset

# CBFET1\_FAIL to CBFET8_FAIL =

Results of the CB FET diagnostic for CB FET1 to CB FET8. 0 = Pass 1 = Fail

# 8.5.4.13.24 FAULT\_COMP\_MISC **Address** **0x0550** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD COMP\_ADC \_ABORT

# LPF\_FAIL Reset RSVD = Reserved

COMP\_ADC\_ABORT = Indicates the most recent ADC comparison diagnostic is aborted due to improper setting. Valid only if one of the ADC comparison diagnostics has started. 0 = ADC comparison diagnostic run to completion 1 = ADC comparison diagnostic is aborted LPF\_FAIL = Indicates LPF diagnostic result. 0 = Pass 1 = Fail

# 8.5.4.13.25 FAULT\_PWR1 **Address** **0x0552** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name CVSS\_OPE N

# DVSS\_OPEN REFHM\_ OPEN

# CVDD\_UV CVDD\_OV DVDD\_OV AVDD\_OSC AVDD\_OV Reset

CVSS\_OPEN = Indicates an open condition on CVSS pin. 0 = No fault 1 = Fault

DVSS\_OPEN = Indicates an open condition on DVSS pin. 0 = No fault 1 = Fault

REFHM\_OPEN = Indicates an open condition on REFHM pin. 0 = No fault 1 = Fault

CVDD\_UV = Indicates an undervoltage fault on the CVDD LDO. 0 = No fault 1 = Fault

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

CVDD\_OV = Indicates an overvoltage fault on the CVDD LDO. 0 = No fault 1 = Fault

DVDD\_OV = Indicates an overvoltage fault on the DVDD LDO. 0 = No fault 1 = Fault

AVDD\_OSC = Indicates AVDD is oscillating outside of acceptable limits.

0 = No fault 1 = Fault This fault could trigger when transitioning from SLEEP to ACTIVE mode. So, if this fault is set, please ignore it and reset the fault.

AVDD\_OV = Indicates an overvoltage fault on the AVDD LDO. 0 = No fault 1 = Fault

# 8.5.4.13.26 FAULT\_PWR2 **Address** **0x0553** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD PWRBIST\_ FAIL

# RSVD

REFH\_OSC NEG5V\_UV TSREF\_OSC TSREF\_UV TSREF\_OV Reset RSVD = Reserved

PWRBIST\_FAIL = Indicates a fail on the power supply BIST run. 0 = No fault 1 = Fault

REFH\_OSC = Indicates REGH reference is oscillating outside of an acceptable limit. 0 = No fault 1 = Fault

NEG5V\_UV = Indicates an undervoltage fault on the NEG5V charge pump. 0 = No fault 1 = Fault

TSREF\_OSC = Indicates TSREF is oscillating outside of an acceptable limit. 0 = No fault 1 = Fault

TSREF\_UV = Indicates an undervoltage fault on the TSREF LDO. 0 = No fault 1 = Fault

TSREF\_OV = Indicates an overvoltage fault on the TSREF LDO. 0 = No fault 1 = Fault

# 8.5.4.13.27 FAULT\_PWR3 **Address** **0x0554** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD RSVD RSVD AVDDUV\_ DRST Reset RSVD = Reserved

AVDDUV\_DRST = Indicates a digital reset occurred due to AVDD UV detected. This also applies when device wakes up after a SHUTDOWN or HW Reset event. 0 = No reset 1 = Digital reset occurred due to AVDD UV **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## 8.5.4.14 Debug Control and Status

# 8.5.4.14.1 DEBUG\_CTRL\_UNLOCK **Address** **0x0700**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** Name CODE\[7:0\] Reset

CODE\[7:0\] = Write the unlock code (0xA5) to this register to activate the setting in the *DEBUG\_COMM\_CTRL\** register.

Any other value than the unlock code will deactivate any effect in the *DEBUG\_COMM\_CTRL\** setting and return to the normal settings of the device.

# 8.5.4.14.2 DEBUG\_COMM\_CTRL1 **Address** **0x0701**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD UART\_BAUD UART\_ MIRROR\_EN

# UART\_TX\_EN USER\_ UART\_EN

# USER\_ DAISY\_EN Reset RSVD = Reserved

UART\_BAUD = This bit changes the UART baud rate to 250kb/s. Useful on VIF debug. When system sets all daisy chain devices to the 250kb/s baud rate, it slows down the response byte through the VIF to increase the robustness of the VIF for debug purposes. 0 = Default 1Mb/s $$ 1 = 250kb/s $$

UART\_MIRROR\_EN = This bit enables the stack VIF communication to mirror to UART. To use this debug function, the stack device's UART TX has to be enabled first by setting *\[UARTTX\_EN\]* = 1. 0 = Disable 1 = Enable

UART\_TX\_EN = Stack device, by default, has the UART TX disabled. This bit enables the UART TX to allow read/write via UART on the stack device. 0 = Disable 1 = Enable

USER\_UART\_EN = This bit enables the debug UART control bits, *\[UART\_TX\_EN\]* and *\[UART\_MIRROR\_EN\]*.

0 = The setting of the bits mentioned above has no effect. 1 = The device configures the UART per *\[UART\_TX\_EN\]* and *\[UART\_MIRROR\_EN\]* settings

USER\_DAISY\_EN = This bit enables the debug COML and COMH control bits in the *DEBUG\_COMM\_CTRL2* register

0 = The setting of *DEBUG\_COMM\_CTRL2* register has no effect. 1 = The device configures the COML and COMH per *DEBUG\_COMM\_CTRL2* register setting.

# 8.5.4.14.3 DEBUG\_COMM\_CTRL2 **Address** **0x0702**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD COML\_TX \_EN

# COML\_RX \_EN

# COMH\_TX \_EN

# COMH\_RX \_EN Reset RSVD = Reserved COML\_TX\_EN = Enables COML transmitter. 0 = Disable 1 = Enable COML\_RX\_EN = Enables COML receiver. 0 = Disable 1 = Enable COMH\_TX\_EN = Enables COMH transmitter. 0 = Disable 1 = Enable

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated COMH\_RX\_EN = Enables COMH receiver. 0 = Disable 1 = Enable

# 8.5.4.14.4 DEBUG\_COMM\_STAT **Address** **0x0780** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD HW\_UART \_DRV

| HW\_DAISY | \_DRV |
|:--- |:--- |
| COML\_TX | \_ON |
| COML\_RX | \_ON |
| COMH\_TX | \_ON |
| COMH\_RX | \_ON |
| Reset | (Base) |
| Reset | (Stack) |

# COML\_TX \_ON

# COML\_RX \_ON

# COMH\_TX \_ON

# COMH\_RX \_ON Reset (Base) Reset (Stack) RSVD = Reserved

HW\_UART\_DRV = Indicates the UART TX is controlled by the device itself or by MCU control. Applicable to the stack device in which the UART TX is disabled by default once a device is configured as 'STACK'. 0 = The *DEBUG\_COMM\_CTRL1\[USER\_UART\_EN\]* = 1. UART TX is under manual control through the *DEBUG\_COMM\_CTRL2* register. 1 = UART TX is controlled by the device

HW\_DAISY\_DRV = Indicates the COML and COMH are controlled by the device itself or by MCU control.

0 = The *DEBUG\_COMM\_CTRL1\[USER\_DAISY\_EN\]* = 1. COML and COMH are under manual control through the *DEBUG\_COMM\_CTRL2* register. 1 = COML and COMH are controlled by the device

COML\_TX\_ON = Shows the current COML transmitter status. $$ 0 = off $$ $$ 1 = on $$

COML\_RX\_ON = Shows the current COML receiver status. $$ 0 = off $$ $$ 1 = on $$

COMH\_TX\_ON = Shows the current COMH transmitter status. $$ 0 = off $$ $$ 1 = on $$

COMH\_RX\_ON = Shows the current COMH receiver status. $$ 0 = off $$ $$ 1 = on $$

# 8.5.4.14.5 DEBUG\_UART\_RC **Address** **0x0781** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name

RSVD RC\_IERR RC\_TXDIS RC\_SOF RC\_BYTE \_ERR

# RC\_UNEXP RC\_CRC Reset RSVD = Reserved

RC\_IERR = Detects initialization byte error in the received command frame. This may be due to the frame initialization byte has a stop error, incorrect frame type is set, or reserved command type bit is set. All bytes that follow are ignored until a communication CLEAR is received. When a communication frame is ignored, the device will not attempt to detect any communication error in the ignored frame nor counting it as valid/discard in the frame counters. 0 = No error 1 = Error detected

RC\_TXDIS = Detects if UART TX is disabled, but the host MCU has issued a command to read data from the device. 0 = No error 1 = Error detected **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

RC\_SOF = Detects a start-of-frame (SOF) error. That is, an UART CLEAR is received on the UART before the current frame is finished. 0 = No error 1 = Error detected

RC\_BYTE\_ERR = Detects any byte error, other than the error in the initialization byte, in the received command frame. All bytes that follow are ignored until a communication CLEAR is received. When a communication frame is ignored, the device will not attempt to detect any communication error in the ignored frame nor counting it as valid/discard in the frame counters. 0 = No error 1 = Error detected

RC\_UNEXP = In a stack device (that is, *\[STACK\_DEV\]* = 1 and *\[MULTIDROP\]* = 0), it is not expected to receive a stack or broadcast command through the UART interface. If so, this is detected as an error and this bit is set. If device is configured with *\[MULTIDROP\]* = 1, this bit will not be set. 0 = No error 1 = Error detected

RC\_CRC = Detects a CRC error in the received command frame from UART. The frame will be considered as discarded frame. 0 = No error 1 = Error detected

# 8.5.4.14.6 DEBUG\_UART\_RR\_TR **Address** **0x0782** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD TR\_SOF TR\_WAIT RR\_SOF RR\_BYTE \_ERR

# RR\_CRC Reset RSVD = Reserved

TR\_SOF = Indicates that a UART CLEAR is received while the device is still transmitting data. 0 = No error 1 = Error detected

TR\_WAIT = The device is waiting for its turn to transfer a response out but the action is terminated because either:

- • The device receives a UART CLEAR signal. - • The device receives a new command.

This bit is valid when broadcast or stack read command has been issued. 0 = No error 1 = Error detected

RR\_SOF = Indicates a UART CLEAR is received while receiving the response frame. Response frames on the UART only apply in multidrop mode. 0 = No error 1 = Error detected

RR\_BYTE\_ERR = Detects any byte error, other than the error in the initialization byte, in the received response frame. All bytes that follow are ignored until a communication CLEAR is received. When a communication frame is ignored, the device will not attempt to detect any communication error in the ignored frame nor counting it as valid/discard in the frame counters. 0 = No error 1 = Error detected

RR\_CRC = Detects are CRC error in the received response frame from UART. The frame will be considered as a discarded frame. 0 = No error 1 = Error detected

# 8.5.4.14.7 DEBUG\_COMH\_BIT **Address** **0x0783**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD PERR BERR\_TAG SYNC2 SYNC1 BIT Reset

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated RSVD = Reserved

PERR = Detects abnormality of the incoming communication frame and hence, the device will forward the communication frame with *\[BERR\]* bit set. Any error bit that is set in this register will also set the *\[PERR\]* bit. However, an abnormality that isn't classified in the register can also trigger the *\[PERR\]* bit (for example, detecting missing data or wrong data order). 0 = No communication error detected, the forwarded communication frame does not have the *\[BERR\]* inserted. 1 = Detected abnormality of the received communication frame. *\[BERR\]* is asserted to the forwarded communication.

BERR\_TAG = Set when the received communication is tagged with *\[BERR\]* = 1.

0 = Received communication frame has no *\[BERR\]* 1 = Received communication frame has *\[BERR\]*

SYNC2 = The Preamble half-bit and the *\[SYNC1:0\]* bits are detected. Device is using the timing information extracted from these bits but it is unable to detect valid data. 0 = No error 1 = Error detected

SYNC1 = Unable to detect the preamble half-bit or any of the *\[SYNC1:0\]* bits. It could be the bit is missing or the signal is too distorted to be detectable. 0 = No error 1 = Error detected

BIT = The device has detected a data bit; however, the detection samples are not enough to assure a strong 1 or 0. 0 = No error 1 = Error detected

# 8.5.4.14.8 DEBUG\_COMH\_RC **Address** **0x0784**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name

RSVD RC\_IERR RC\_TXDIS RC\_SOF RC\_BYTE \_ERR

# RC\_UNEXP RC\_CRC Reset RSVD = Reserved

RC\_IERR = Detects initialization byte error in the received command frame. This may due to improper formatting of a byte such as a frame initialization byte is expected, but start-of-frame (SOF) bit is not set, or an invalid frame type is selected. Because bytes received on the COMH/COML are propagated up the stack, it is likely devices in the upper stack will also detect this error. All bytes that follow are ignored until a SOF bit is set is received. When a communication frame is ignored, the device will not attempt to detect any communication error in the ignored frame nor counting it as valid/discard in the frame counters. 0 = No error 1 = Error detected

| RC\_TXDIS = Valid when \[DIR\_SEL\] = 1. Device detects the COMH TX is disabled but the device receives a command to read | data (that is, to transmit data out). The command frame will be counted as a discard frame. | 0 = No error | 1 = Error detected |
|:--- |:--- |:--- |:--- |
| RC\_SOF = Valid when \[DIR\_SEL\] = 1. Detects a start-of-frame (SOF) error on COMH. The SOF bit is set only in the | initialization frame but the SOF bit is set in the current frame that is not expected. | 0 = No error | 1 = Error detected |
| RC\_BYTE\_ERR = Valid when \[DIR\_SEL\] = 1. Detected any byte error, other than the error in the initialization byte, in the received | command frame. This error can trigger one or more error bit set in the DEBUG\_COMMH\_BIT register. | 0 = No error | 1 = Error detected |
| RC\_UNEXP = If \[DIR\_SEL\] = 0, but device receives command frame from COMH which is an invalid condition and device will | set this error bit. | 0 = No error | 1 = Error detected |
| RC\_CRC = Indicates a CRC error that resulted in one or more COMH command frames being discarded. Any other errors in | the frame are not indicated as the frame was discarded. | 0 = No error | 1 = Error detected |

RC\_SOF = Valid when *\[DIR\_SEL\]* = 1. Detects a start-of-frame (SOF) error on COMH. The SOF bit is set only in the initialization frame but the SOF bit is set in the current frame that is not expected. 0 = No error 1 = Error detected

RC\_BYTE\_ERR = Valid when *\[DIR\_SEL\]* = 1. Detected any byte error, other than the error in the initialization byte, in the received command frame. This error can trigger one or more error bit set in the *DEBUG\_COMMH\_BIT* register. 0 = No error 1 = Error detected

RC\_UNEXP = If *\[DIR\_SEL\]* = 0, but device receives command frame from COMH which is an invalid condition and device will set this error bit. 0 = No error 1 = Error detected

RC\_CRC = Indicates a CRC error that resulted in one or more COMH command frames being discarded. Any other errors in the frame are not indicated as the frame was discarded. 0 = No error 1 = Error detected **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

# 8.5.4.14.9 DEBUG\_COMH\_RR\_TR **Address** **0x0785**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name

RSVD TR\_WAIT RR\_TXDIS RR\_SOF RR\_BYTE \_ERR

# RR\_UNEXP RR\_CRC Reset RSVD = Reserved

TR\_WAIT = The device is waiting for its turn to transfer a response out but the action is terminated because the device receives a new command. This bit is valid when broadcast or stack read command has been issued. 0 = No error 1 = Error detected

| RR\_TXDIS = Valid when \[DIR\_SEL\] = 0, device receives a response but fails to transmit to the next device because the COMH | TX is disabled. The frame is counted as a discarded frame. | 0 = No error | 1 = Error detected |
|:--- |:--- |:--- |:--- |
| RR\_SOF = Valid when \[DIR\_SEL\] = 0. Detects a start-of-frame (SOF) error on COMH. The SOF bit is set only in the | initialization frame but the SOF bit is set in the current frame that is not expected. | 0 = No error | 1 = Error detected |
| RR\_BYTE\_ERR = Valid when \[DIR\_SEL\] = 0. Detects any byte error, other than the error in the initialization byte, in the received | response frame. This error can trigger one or more error bits set in the DEBUG\_COMMH\_BIT register. | 0 = No error | 1 = Error detected |
| RR\_UNEXP = If \[DIR\_SEL\] = 1, but device received response frame from COMH which is an invalid condition and device sets | this error bit. | 0 = No error | 1 = Error detected |

RR\_SOF = Valid when *\[DIR\_SEL\]* = 0. Detects a start-of-frame (SOF) error on COMH. The SOF bit is set only in the initialization frame but the SOF bit is set in the current frame that is not expected. 0 = No error 1 = Error detected

RR\_BYTE\_ERR = Valid when *\[DIR\_SEL\]* = 0. Detects any byte error, other than the error in the initialization byte, in the received response frame. This error can trigger one or more error bits set in the *DEBUG\_COMMH\_BIT* register. 0 = No error 1 = Error detected

RR\_UNEXP = If *\[DIR\_SEL\]* = 1, but device received response frame from COMH which is an invalid condition and device sets this error bit. 0 = No error 1 = Error detected

RR\_CRC = Indicates a CRC error that resulted in one or more COMH response frames being discarded. Most other errors in the frame are not indicated as the frame was discarded. If *\[RR\_BYTE\_ERR\]* is observed on the final byte of the CRC, both CRC and BERR will be indicated. 0 = No error 1 = Error detected

# 8.5.4.14.10 DEBUG\_COML\_BIT **Address** **0x0786**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD PERR BERR\_TAG SYNC2 SYNC1 BIT Reset RSVD = Reserved

PERR = Detect abnormality of the incoming communication frame and the outgoing communication frame will be set with BERR. Any error bit that is set in this register will also set the *\[PERR\]* bit. However, abnormality that isn't classified in the register can also trigger the *\[PERR\]* bit (for example, detecting missing data or wrong data order. 0 = No communication error detected, the forwarded communication frame does not have the BERR inserted 1 = Detected abnormality of the received communication frame. BERR is asserted to the forwarded communication.

BERR\_TAG = Set when the received communication is tagged with BERR.

0 = Received communication frame has no BERR 1 = Received communication frame has BERR

SYNC2 = The Preamble half-bit and the *\[SYNC1:0\]* bits are detected. Device is using the timing information that is extracted from these bits but it is unable to detect valid data. 0 = No error 1 = Error detected

SYNC1 = Unable to detect the preamble half-bit or any of the *\[SYNC1:0\]* bits. It could be the bit is missing or the signal is too distorted to be detectable. 0 = No error 1 = Error detected

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

BIT = The device has detected a data bit. However, the detection samples are not enough to assure a strong 1 or 0. 0 = No error 1 = Error detected

# 8.5.4.14.11 DEBUG\_COML\_RC **Address** **0x0787**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name

RSVD RC\_IERR RC\_TXDIS RC\_SOF RC\_BYTE \_ERR

# RC\_UNEXP RC\_CRC Reset RSVD = Reserved

RC\_IERR = Detected initialization byte error in the received command frame. This may due to improper formatting of a byte such as a frame initialization byte is expected, but start-of-frame (SOF) bit is not set, or an invalid frame type is selected. Because bytes received on the COMH/COML are propagated up the stack, it is likely devices in the upper stack will also detect this error. All bytes that follow are ignored until a SOF bit is received. When a communication frame is ignored, the device will not attempt to detect any communication error in the ignored frame nor counting it as valid/discard in the frame counters. 0 = Error not detected 1 = Error detected

| RC\_TXDIS = Valid when \[DIR\_SEL\] = 0. Device detects the COML TX is disabled but the device receives a command to read | data (that is, to transmit data out). The command frame will be counted as a discarded frame. | 0 = No error | 1 = Error detected |
|:--- |:--- |:--- |:--- |
| RC\_SOF = Valid when \[DIR\_SEL\] = 0. Detects a start-of-frame (SOF) error on COML. The SOF bit is set only in the | initialization frame but the SOF bit is set in the current frame that is not expected. | 0 = No error | 1 = Error detected |
| RC\_BYTE\_ERR = Valid when \[DIR\_SEL\] = 0. Detected any byte error, other than the error in the initialization byte, in the received | command frame. This error can trigger one or more error bits set in the DEBUG\_COMML\_BIT register. | 0 = No error | 1 = Error detected |
| RC\_UNEXP = If \[DIR\_SEL\] = 1, but device received command frame from COML which is an invalid condition and device will | set this error bit. | 0 = No error | 1 = Error detected |
| RC\_CRC = Indicates a CRC error that resulted in one or more COML command frames being discarded. Any other errors in | the frame are not indicated as the frame was discarded. | 0 = No error | 1 = Error detected |

RC\_SOF = Valid when *\[DIR\_SEL\]* = 0. Detects a start-of-frame (SOF) error on COML. The SOF bit is set only in the initialization frame but the SOF bit is set in the current frame that is not expected. 0 = No error 1 = Error detected

RC\_BYTE\_ERR = Valid when *\[DIR\_SEL\]* = 0. Detected any byte error, other than the error in the initialization byte, in the received command frame. This error can trigger one or more error bits set in the *DEBUG\_COMML\_BIT* register. 0 = No error 1 = Error detected

RC\_UNEXP = If *\[DIR\_SEL\]* = 1, but device received command frame from COML which is an invalid condition and device will set this error bit. 0 = No error 1 = Error detected

RC\_CRC = Indicates a CRC error that resulted in one or more COML command frames being discarded. Any other errors in the frame are not indicated as the frame was discarded. 0 = No error 1 = Error detected

# 8.5.4.14.12 DEBUG\_COML\_RR\_TR **Address** **0x0788** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name

RSVD TR\_WAIT RR\_TXDIS RR\_SOF RR\_BYTE \_ERR

# RR\_UNEXP RR\_CRC Reset RSVD = Reserved

TR\_WAIT = The device is waiting for its turn to transfer a response out but the action is terminated because the device receives a new command. This bit is valid when broadcast or stack read command has been issued. 0 = No error 1 = Error detected

RR\_TXDIS = Valid when *\[DIR\_SEL\]* = 1, device receives a response but fails to transmit to the next device because the COML TX is disabled. The frame is counted as a discarded frame. 0 = No error 1 = Error detected **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

| RR\_SOF = Valid when \[DIR\_SEL\] = 1. Detects a start-of-frame (SOF) error on COML. The SOF bit is set only in the | initialization frame but the SOF bit is set in the current frame that is not expected. | 0 = No error | 1 = Error detected |
|:--- |:--- |:--- |:--- |
| RR\_BYTE\_ERR = Valid when \[DIR\_SEL\] = 1. Detects any byte error, other than the error in the initialization byte, in the received | response frame. This error can trigger one or more error bits set in the DEBUG\_COMML\_BIT register. | 0 = No error | 1 = Error detected |
| RR\_UNEXP = If \[DIR\_SEL\] = 0, but device received a response frame from COML which is an invalid condition and device will | set this error bit. | 0 = No error | 1 = Error detected |

RR\_BYTE\_ERR = Valid when *\[DIR\_SEL\]* = 1. Detects any byte error, other than the error in the initialization byte, in the received response frame. This error can trigger one or more error bits set in the *DEBUG\_COMML\_BIT* register. 0 = No error 1 = Error detected

RR\_UNEXP = If *\[DIR\_SEL\]* = 0, but device received a response frame from COML which is an invalid condition and device will set this error bit. 0 = No error 1 = Error detected

RR\_CRC = Indicates a CRC error that resulted in one or more COML response frames being discarded. Most other errors in the frame are not indicated as the frame was discarded. If *\[RR\_BYTE\_ERR\]* is observed on the final byte of the CRC, both CRC and BERR are indicated. 0 = No error 1 = Error detected

# 8.5.4.14.13 DEBUG\_UART\_DISCARD **Address** **0x0789** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** Name COUNT\[7:0\] Reset

COUNT\[7:0\] = UART frame counter to track the number of discard frames received or transmitted. The registers of the

*DEBUG\_UART\_DISCARD* and *DEBUG\_UART\_VALID\** are latched and the related counters are reset when this register is read.

# 8.5.4.14.14 DEBUG\_COMH\_DISCARD **Address** **0x078A** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** Name COUNT\[7:0\] Reset

COUNT\[7:0\] = COMH frame counter to track the number of discard frames received or transmitted. The registers of the

*DEBUG\_COMH\_DISCARD* and *DEBUG\_COMH\_VALID\** are latched and the related counters are reset when this register is read.

# 8.5.4.14.15 DEBUG\_COML\_DISCARD **Address** **0x078B** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** Name COUNT\[7:0\] Reset

COUNT\[7:0\] = COML frame counter to track the number of discard frames received or transmitted. The registers of the

*DEBUG\_COML\_DISCARD* and *DEBUG\_COML\_VALID* \* are latched and the related counters are reset when this register is read.

# 8.5.4.14.16 DEBUG\_UART\_VALID\_HI/LO

# DEBUG\_UART\_VALID\_HI **Address** **0x078C** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** Name COUNT\[7:0\]

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated Reset

COUNT\[7:0\] = The high-byte of UART frame counter to track the number of valid frames received or transmitted. Counter saturates when both *DEBUG\_UART\_VALID\_HI/LO* is 0xFF. This register is latched and the related counter is reset when *DEBUG\_UART\_DISCARD* is read.

# DEBUG\_UART\_VALID\_LO **Address** **0x078D** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** Name COUNT\[7:0\] Reset

COUNT\[7:0\] = The low-byte of UART frame counter to track the number of valid frames received or transmitted. Counter saturates when both *DEBUG\_UART\_VALID\_HI/LO* is 0xFF. This register is latched and the related counter is reset when *DEBUG\_UART\_DISCARD* is read.

# 8.5.4.14.17 DEBUG\_COMH\_VALID\_HI/LO

# DEBUG\_COMH\_VALID\_HI **Address** **0x078E** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** Name COUNT\[7:0\] Reset

COUNT\[7:0\] = The high-byte of COMH frame counter to track the number of valid frames received or transmitted. Counter saturates when both *DEBUG\_COMH\_VALID\_HI/LO* is 0xFF. This register is latched and the related counter is reset when *DEBUG\_COMH\_DISCARD* is read.

# DEBUG\_COMH\_VALID\_LO **Address** **0x078F** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** Name COUNT\[7:0\] Reset

COUNT\[7:0\] = The low-byte of COMH frame counter to track the number of valid frames received or transmitted. Counter saturates when both *DEBUG\_COMH\_VALID\_HI/LO* is 0xFF. This register is latched and the related counter is reset when *DEBUG\_COMH\_DISCARD* is read.

# 8.5.4.14.18 DEBUG\_COML\_VALID\_HI/LO

# DEBUG\_COML\_VALID\_HI **Address** **0x0790** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** Name COUNT\[7:0\] Reset

COUNT\[7:0\] = The high-byte of COML frame counter to track the number of valid frames received or transmitted. Counter saturates when both *DEBUG\_COML\_VALID\_HI/LO* is 0xFF. This register is latched and the related counter is reset when *DEBUG\_COML\_DISCARD* is read.

# DEBUG\_COML\_VALID\_LO **Address** **0x0791** **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** Name COUNT\[7:0\] Reset

COUNT\[7:0\] = The low-byte of COML frame counter to track the number of valid frames received or transmitted. Counter saturates when both *DEBUG\_COML\_VALID\_HI/LO* is 0xFF. This register is latched and the related counter is reset when *DEBUG\_COML\_DISCARD* is read.

# 8.5.4.14.19 DEBUG\_OTP\_SEC\_BLK **Address** **0x07A0** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** Name BLOCK\[7:0\] Reset

BLOCK\[7:0\] = Holds last OTP block address where SEC occurred. Valid only when *FAULT\_OTP\[SEC\_DET\]* = 1.

# 8.5.4.14.20 DEBUG\_OTP\_DED\_BLK **Address** **0x07A1**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** Name BLOCK\[7:0\] Reset

BLOCK\[7:0\] = Holds last OTP block address where DED occurred. Valid only when *FAULT\_OTP\[DED\_DET\]* = 1.

## 8.5.4.15 OTP Programming Control and Status

# 8.5.4.15.1 OTP\_PROG\_UNLOCK1A through OTP\_PROG\_UNLOCK1D **Address** **0x0300 to ** **0x0303**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** Name CODE\[7:0\] Reset

CODE\[7:0\] = The first 32-bit OTP programming unlock code is required as part of the OTP programming unlock sequence before performing OTP programming. This 32-bit code is entered in the sequence from *OTP\_PROG\_UNLOCK1A * to *OTP\_PROG\_UNLOCK1D*. These registers always read back 0.

# 8.5.4.15.2 OTP\_PROG\_UNLOCK2A through OTP\_PROG\_UNLOCK2D **Address** **0x0352 to ** **0x0355**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** Name CODE\[7:0\] Reset

CODE\[7:0\] = The second 32-bit OTP programming unlock code, required as part of the OTP programming unlock sequence before performing OTP programming. This 32-bit code is entered in the sequence from *OTP\_PROG\_UNLOCK2A * to *OTP\_PROG\_UNLOCK2D*. These registers always read back 0.

# 8.5.4.15.3 OTP\_PROG\_CTRL **Address** **0x030B**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD PAGESEL PROG\_GO Reset RSVD = Reserved

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

PAGESEL = Selects which customer OTP page to be programmed. $$ 0 = page 1 $$ $$ 1 = page 2 $$

PROG\_GO = Enables programming for the OTP page selected by *OTP\_PROG\_CTRL\[PAGESEL\].* Requires

*OTP\_PROG\_UNLOCK1\** and *OTP\_PROG\_UNLOCK2\** registers are set to the correct codes. 0 = Ready 1 = Start OTP programming

# 8.5.4.15.4 OTP\_ECC\_TEST **Address** **0x034C**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name RSVD DED\_SEC MANUAL\_ AUTO

# ENC\_DEC ENABLE Reset RSVD = Reserved

DED\_SEC = Sets the decoder function (SEC or DED) to test. This bit is ignored during encoder testing.

0 = Test SEC functionality. Sets the *FAULT\_OTP\[SEC\_DETECT\]* flag and outputs test result to *OTP\_ECC\_DATAOUT\** registers. 1 = Test DED functionality. Sets the *FAULT\_OTP\[DED\_DETECT\]* flag and outputs test result *OTP\_ECC\_DATAOUT\**. Note: If SEC or DEC fault is detected, host sets *\[RST\_OTP\_DATA\]* = 1 to reset the corresponding fault. Switch to run SEC test does not clear DEC fault or vice versa.

MANUAL\_AUTO = Sets the location of the data to use for the ECC test.

0 = Auto mode. Use the internal data for test. 1 = Manual mode. Uses data in *ECC\_DATAIN\_n* registers for test. Use for MPF test.

ENC\_DEC = Sets the encoder/decoder test to run when *OTP\_ECC\_TEST\[ENABLE\]* = 1. 0 = Run decoder test 1 = Run encoder test

ENABLE = Executes the OTP ECC test configured by *\[ENC\_DEC\]* and *\[DED\_SEC\]* bits.

0 = Normal operation, ECC test disabled 1 = Initiate test

# 8.5.4.15.5 OTP\_ECC\_DATAIN1 through OTP\_ECC\_DATAIN9 **Address** **0x0343 to ** **0x034B**

RW **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** Name DATA\[7:0\] Reset

DATA\[7:0\] = When ECC is enabled in manual mode, *CUST\_ECC\_TEST\[MANUAL\_AUTO\]* = 1, *OTP\_ECC\_DATAIN1...9 *

registers are used to test the ECC encoder/decoder. If *CUST\_ECC\_TEST\[ENC\_DEC\]* = 1, *ECC\_DATAIN8* through *ECC\_DATAIN1* are fed to the encoder. If *CUST\_ECC\_TEST\[ENC\_DEC\]* = 0, *ECC\_DATAIN9* through *ECC\_DATAIN1* are fed to the decoder. The ECC\_DATAOUT0...8 bytes must be read back to verify functionality.

# 8.5.4.15.6 OTP\_ECC\_DATAOUT1 through OTP\_ECC\_DATAOUT9 **Address** **0x0510 to ** **0x0518** Read Only

**Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0** Name DATA\[7:0\] Reset **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

DATA\[7:0\] = * * *OTP\_ECC\_DATAOUT\** bytes output the results of the ECC decoder and encoder tests.

If *CUST\_ECC\_TEST\[ENC\_DEC\]* = 0, *ECC\_DATAOUT8* through *ECC\_DATAOUT1* are read to determine a successful decoder test. If *CUST\_ECC\_TEST\[ENC\_DEC\]* = 1, *ECC\_DATAOUT9* through *ECC\_DATAOUT1* are read to determine a successful encoder test. The correct result depends on the input to the test.

# 8.5.4.15.7 OTP\_PROG\_STAT **Address** **0x0519**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name

UNLOCK OTERR UVERR OVERR SUVERR SOVERR PROGERR DONE Reset

UNLOCK = Indicates the OTP programming function unlock status. After this bit is set (that is, OTP programming is enabled), the host writes to the *OTP\_PROG\_CTRL* register to start the OTP programming. Writing to any other register relocks the OTP programming function and clears this bit to 0. *\[PROG\_GO\]* = 1 also clears this bit to 0. 0 = OTP programming locked 1 = OTP programming is unlocked

OTERR = Indicates the die temperature is greater than T OTP\_PROG and device does not start OTP programming.

0 = No fault 1 = Detected die temperature is greater than T OTP\_PROG. Abort OTP programming.

| UVERR = Indicates an undervoltage error detected on the programming voltage during OTP programming. This bit is | cleared with \[PROG\_GO\] = 1. | 0 = No error | 1 = UV error detected |
|:--- |:--- |:--- |:--- |
| OVERR = Indicates an overvoltage error detected on the programming voltage during OTP programming. This bit is cleared | with \[PROG\_GO\] = 1. Information received from the device with this error must not be considered reliable. | 0 = No error | 1 = OV error detected |
| SUVERR = A programming voltage stability test is performed before starting the actual OTP programming. This bit indicates | an undervoltage error is detected during the voltage stability test. This bit is cleared with \[PROG\_GO\] = 1. | 0 = No error | 1 = UV error detected during OTP programming voltage stability test |
| SOVERR = A programming voltage stability test is performed before starting the actual OTP programming. This bit indicates | an overvoltage error is detected during the voltage stability test. This bit is cleared with \[PROG\_GO\] = 1. | 0 = No error | 1 = OV error detected during OTP programming voltage stability test |

OVERR = Indicates an overvoltage error detected on the programming voltage during OTP programming. This bit is cleared with *\[PROG\_GO\]* = 1. Information received from the device with this error must not be considered reliable. 0 = No error 1 = OV error detected

SUVERR = A programming voltage stability test is performed before starting the actual OTP programming. This bit indicates an undervoltage error is detected during the voltage stability test. This bit is cleared with *\[PROG\_GO\]* = 1. 0 = No error 1 = UV error detected during OTP programming voltage stability test

SOVERR = A programming voltage stability test is performed before starting the actual OTP programming. This bit indicates an overvoltage error is detected during the voltage stability test. This bit is cleared with *\[PROG\_GO\]* = 1. 0 = No error 1 = OV error detected during OTP programming voltage stability test

# PROGERR $$ = $$

Indicates when an error is detected due to incorrect page setting caused by any of the following:

- • Trying to program but OTP programming *\[UNLOCK\]* = 0. - • Trying to program a page that has *\[TRY\]* = 1. - • Trying to program a page which has *\[FMTERR\]* = 1.

This bit is cleared with *\[PROG\_GO\]* = 1. 0 = No error or programming not attempted 1 = Error detected

DONE = Indicates the status of the OTP programming for the selected page. This bit is cleared with *\[PROG\_GO\]* = 1.

0 = Not completed or programming not attempted 1 = Complete.

# 8.5.4.15.8 OTP\_CUST1\_STAT **Address** **0x051A**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name

LOADED LOADWRN LOADERR FMTERR PROGOK UVOK OVOK TRY Reset

LOADED = Indicates OTP page 1 has been selected for loading into the related registers. See *\[LOADERR\]* and *\[LOADWRN\] *

for error and warning status. 0 = Not selected for loading 1 = Page 1 selected and loaded

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

# LOADWRN $$ = $$

Indicates OTP page 1 was loaded but with one or more SEC warnings. 0 = No warning, or no load attempted 1 = Warning

LOADERR = Indicates an error while attempting to load OTP page 1; that is, DED is detected while loading the selected page.

0 = No error, or no load was attempted. 1 = Error detected

FMTERR = Indicates a formatting error in OTP page 1; that is, when *\[UVOK\]* or *\[OVOK\]* is set, but *\[TRY\]* = 0. Do not program if this bit is set. 0 = No error 1 = Error detected

PROGOK = Indicates the validity for loading for OTP page 1. A valid page indicates that successful programming occurred. 0 = Not valid 1 = Valid

UVOK = Indicates an OTP programming voltage undervoltage condition is detected during programming attempt for OTP page 1. The OV condition may also trigger the UV as part of the shutdown process. 0 = UV condition detected. Also reads as 0 if no programming attempt is performed. 1 = No UV condition detected

OVOK = Indicates an OTP programming voltage overvoltage condition is detected during programming attempt for OTP page 1. The OV condition will trigger the UV as part of the shutdown process. The device must be taken out of service. 0 = OV condition detected. Also reads as 0 if no programming attempt is performed. 1 = No OV condition detected

TRY = Indicates a first programming attempt for OTP page 1.

0 = No first attempt made 1 = First attempt made

# 8.5.4.15.9 OTP\_CUST2\_STAT **Address** **0x051B**

Read Only **Bit 7** **Bit 6** **Bit 5** **Bit 4** **Bit 3** **Bit 2** **Bit 1** **Bit 0**

# Name

LOADED LOADWRN LOADERR FMTERR PROGOK UVOK OVOK TRY Reset

LOADED = Indicates OTP page 2 has been selected for loading into the related registers. See *\[LOADERR\]* and *\[LOADWRN\] *

for error and warning status. 0 = Not selected for loading 1 = Page 2 selected and loaded

# LOADWRN $$ = $$

Indicates OTP page 2 was loaded but with one or more SEC warnings. 0 = No warning, or no load attempted 1 = Warning

# LOADERR $$ = $$

Indicates an error while attempting to load OTP page 2; that is, DED is detected while loading the selected page. 0 = No error, or no load was attempted. 1 = Error detected

FMTERR = Indicates a formatting error in OTP page 2; that is, when *\[UVOK\]* or *\[OVOK\]* is set, but *\[TRY\]* = 0. Do not program if this bit is set. 0 = No error 1 = Error detected

PROGOK = Indicates the validity for loading for OTP page 2. A valid page indicates that successful programming occurred. 0 = Not valid 1 = Valid

UVOK = Indicates an OTP programming voltage undervoltage condition is detected during programming attempt for OTP page 2. The OV condition may also trigger the UV as part of the shutdown process. 0 = UV condition detected. Also reads as 0 if no programming attempt is performed. 1 = No UV condition detected

OVOK = Indicates an OTP programming voltage overvoltage condition is detected during programming attempt for OTP page 2. The OV condition will trigger the UV as part of the shutdown process. The device must be taken out of service. 0 = OV condition detected. Also reads as 0 if no programming attempt is performed. 1 = No OV condition detected **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

TRY = Indicates a first programming attempt for OTP page 2.

0 = No first attempt made 1 = First attempt made

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

# 9 Application and Implementation

# Note

# Information in the following applications sections is not part of the TI component specification,

and TI does not warrant its accuracy or completeness. TI's customers are responsible for determining suitability of components for their purposes, as well as validating and testing their design implementation to confirm system functionality.

# 9.1 Application Information

# The BQ79616 device family provides high-accuracy, cell voltages and temperature measurements for 6-series to 16-series battery modules.

# 9.2 Typical Applications

# 9.2.1 Base Device Application Circuit

# The following application circuit (see Figure 9-1 ) is based on the BQ79616 device connecting to a 16S module.

# VCC

# TX

# RX

# INB

# INC

# OUTC INT

# MCU

# BAT

# LDOIN

# NPNB

# COMHP

# COMHN

# VC16

# VC0

# CB0

# REFHP

# AVDD

# REFHM

# DVDD

# DVSS

# CVSS

# CVDD Isolation Circuit

# GND1

# GND2 GND

# ISO774x

# COMLP

# COMLN

| To COMH of the | Top of Stack |
|:--- |:--- |
| Isolation | circuit |
| OPTIONAL: Only necessary for ring | architecture applications | Isolation circuit

**OPTIONAL**: Only necessary for ring architecture applications

# NEG5V

# AVSS

# RX

# NFAULT

# TX

# GPIO2

# TSREF

# GPIO1

# To CVDD

# 4.7 F

# N

# N

# N

# 1 F

# 1 F

# N

# N

# 1 F

# N

# N

# 0.1 F

# N 0.1 F

# N

# 0.22 F 10 nF

# N 0.47 uF

# CELL 16 + 0.47 uF +

# CELL 1 0.47 uF 1 µF 10 k 10 k

# CELL 16

# SYS

# OPTIONAL

# GPIO3

# GPIO4

# GPIO5

# GPIO6

# GPIO7

# GPIO8

# INA OUTB

# OUTA VCC1 100 k 100 k

# RX

# TX

# NFAULT

# COMLP

# COMLN Leave Unconnected For Base Device

# To CVDD optional HV to LV Isolation (Transformer)

# COMHP COMHN

# BAT

# RS

# TX

# TX

# RX

# NFAULT optional

# PMIC

# VCC

If communication device is used on the system side BQ79600 Communication Device (Base Device)

# MCU

If NO (system side) communication device is in use

# BBP BBN To COML of the North Device

# CELL 15 + 0.47 uF 0.47 uF

# VC1

# CELL 15 0.47 uF

# CELL 1

# CELL 1

# CB1

# CB15

# CB16

# VC15

# AVSS 0.47 uF

# Figure 9-1. Typical Base Device with Measurement Application Circuit

# 9.2.1.1 Design Requirements

# Table 9-1 below shows the design parameters.

# Table 9-1. Recommended Design Requirements

# PARAMETER **VALUE**

# Module Voltage Range (Voltage at the BAT pin) 9V to 80V

# Number of cells (single device)

6 to 16 cells (BQ79616), 6 to 14 cells (BQ79616), 6 to 12 cells (BQ79616)

# www.ti.com

# BQ79616 SLUSF21 - JUNE 2023

# Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## Table 9-1. Recommended Design Requirements (continued)

# PARAMETER **VALUE** Cell voltage range 0V to 5V

## 9.2.1.2 Detailed Design Procedure

**9.2.1.2.1 Cell Sensing and Balancing Inputs**

**Related Pins** **Components** **Value** **Description**

VC0 to VC16 Filter resistor 100 Ω Only differential RC filters are needed for VC channels. Besides serving for input signal filtering, these components are required to support hot-plug events during cell module insertion. Hence, it is highly recommended to use the component values as suggested. Filter capacitor 0.47 \muF/16 V or 1 \muF/16 V

CB0 to CB16 Filter resistor Depends on system's balancing current requirements

The filter resistor on CB pins sets the maximum balancing current. See Section 8.3.3 for details. Only differential RC filters are needed for CB channels. Besides serving for input signal filtering, these components are required to support hot-plug events during cell module insertion. Hence, it is highly recommended to use the component values as suggested. Filter capacitor 0.47 \muF/16 V or 1 \muF/16 V

## Cell Connections

## Populate the battery cells from the bottom channels (both VC and CB channels) and up, leaving upper channels

as unused channels if cell module size is smaller than the maximum channel size of the BQ79616 device. Unused channel(s) in the BQ79616 device are connected as shown in Figure 9-2. PCB Layout for open/NC pins should have minimum trace lengths and should not be connected to a wire or cable.

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

(c) One PCB for all channels applications ± For BQ79616: Configured for 15 VC and CB If floating the unused VC and CB pins, capacitors in black corresponding to CB pins  need to be populated, but capacitors and resistors in grey corresponding to VC and CB pins need to be unpopulated

# VC16

# VC15

#...

# CB16

# CB15

# CB14

#...

(b) One PCB for all channels applications ± For BQ79616: Configured for 16 VC and CB      

# BAT VCn

#...

#... +

# CELL n +

# CELL15 +

# CELL16 +

# CELL14

#...

# VC16

# VC15

#...

# CB16

# CB15

# CB14

#...      

# BAT VCn

#...

#... +

# CELL n +

# CELL15 +

# CELL16 +

# CELL14

#...

(d) One PCB for all channels applications ± For BQ79612: Configured for 12 VC and CB If floating the unused VC and CB pins, capacitors in black corresponding to CB pins  need to be populated, but capacitors and resistors in grey corresponding to VC and CB pins need to be unpopulated

# VC16/NC

# VC15/NC

#...

# CB16/NC

# CB15/NC

# CB14/NC

#...      

# BAT VCn

#...

#... +

# CELL n +

# CELL15 +

# CELL16 +

# CELL14

#...

# VC14

# VC14

# VC14/NC

# CB13/NC   +

# CELL13

# VC13/NC

# CB12   +

# CELL12

# VC12

(a) Customized PCB for certain channels applications - Short unused pins to BAT Pin VC16 (or NC in 14S/12S device) VCn+1 VCn

#...

#... CB16 (or NC in 14S/12S device) CBn+1

# CELL n +

# BAT

#...

#... VC15 (or NC in 14S/12S device) CB15 (or NC in 14S/12S device) CBn

#...

# Figure 9-2. Unused VC and CB Channels

## www.ti.com

# BQ79616 SLUSF21 - JUNE 2023

## Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* **9.2.1.2.2 BAT and External NPN**

**Related Pins** **Components** **Value** **Description**

BAT Filter resistor 30 Ω Single-ended RC filter, recommended values must be used for hot-plug performance. Filter capacitor 10 nF/100 V Can use lower voltage rating based on module size

NPNB NPN (Q1) Collector-emitter breakdown voltage 80 V to 100 V, but can use lower rating based on module size Power rating ≥ 1 W Gain \> 80 at the expected load current Current handling \>100 mA

The external NPN is used to form a preregulation circuit to provide a 6-V (typical) input to the LDOIN pin. The voltage rating of the NPN can be optimized by the following equation: **NPN voltage rating = Max VModule - Min VLDOIN + Margin** Where: Max VModule = maximum module voltage with fully charged cells Min VLDOIN = the minimum spec of the VLDOIN parameter Margin = system transient voltage + design margin per application requirement Resistor on external NPN collector (R NPN )

Various based on module voltage The resistor has a couple purposes: (a) For an RC filter for the NPN preregulation circuit (b) Share the thermal dissipation with the NPN Capacitor on external NPN collector

0.22 \muF/100 V Can use lower voltage rating based on module size

The capacitor forms the RC filter for the NPN preregulation circuit The capacitor rating is based on peak voltage spike seen on the module. For smaller module size, \< 100-V rated capacitor can be used. System designer selects the optimized voltage-rated capacitor per their system tolerance and requirements.

## To reduce the power rating needed for the external NPN (Q1), system designers can put power resistors on the

NPN collector to create an IR drop from the module voltage (VModule). Figure 9-3 shows the current paths to power the BQ79616 device.

## Typical I STARTUP current, that is, inrush startup current when the device enters from SHUTDOWN to ACTIVE, is

20 mA for TI recommended components. This current is the sum of IBAT + ILDOIN, and is dependent on PCB board components and layout. Designers must characterize this on their end. 0.22 µF Q1 0.1 µF

# NPN

# NPNB

# LDOIN 10 nF

# CELL 16 +

#...

#...

# BAT

# VC16

**Small current path ** **to BAT to power an ** **Always-On circuit in ** **the device ** **Main current path to power the device ** VModule VCollector

## Figure 9-3. Power Consumption Paths

## To ensure there is sufficient headroom to maintain 6 V (typical) regulated voltage on LDOIN pin, system designer

ensures VCollector has ≥ 8 V at any time with the assumption of about 2-V drop across the NPN.

## Therefore, maximum allowable R NPN value = ((Min VModule) - (VCollector)) / (Max peak current)

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## Where

## Min VModule: based on module size and minimum cell voltage per application

## VCollector: 8 V with the assumption of about 2-V drop across NPN

## Max peak current: highest operation current, which is the active current with all functions turned on. Note that

different communication isolation components (for example, capacitor isolation versus transformer, or the type of transformer) contribute different loading to the total power consumption.

## Powering the device separately from the top of the battery stack

## The device is designed to be powered by the battery stack. If there is a need to power the device from a

separate source such as in Figure 9-4, the following relationship between the voltage on the BAT pin and the highest VC pin voltage (with respected to ground) is BAT voltage ≥ (0.5 × highest VC voltage) + 2.

## For example, if the device is connected to a 14S module with max cell voltage of 4.2 V/cell, the highest VC pin is

VC14, and the highest VC14 voltage is (4.2 V × 14) = 58.8 V. If the BAT pin is powered separately, BAT voltage must be ≥ 31.4 V.

## Similarly, if BBP/N channel is connected above the highest cell stack, the BBP pin will has the highest

voltage (with respected to ground) than the VC pins. In this scenario, VBAT ≥ \[(VBBP-2.5) × 0.84\] + 4.5. The requirement applies when BAT is power separately and it is to ensure proper operation of the internal level shifter. Fail to maintain the voltage relationship will increase the ADC measurement error on the VC and BB channels. 0.22 µF Q1 0.1 µF

# NPN

# NPNB

# LDOIN 10 nF

# CELL 14 +

#...

#...

# BAT

# VC14 Top of stack module Separate Power source

## Figure 9-4. Separate Power Source to BAT **9.2.1.2.3 Power Supplies, Reference Input**

**Related Pins** **Components** **Value** **Description**

# AVDD, DVDD, TSREF

Bypass capacitor 1 \muF/10 V Bypass capacitor for the internal LDOs

CVDD Bypass capacitor 4.7 µF/10 V Bypass capacitor for CVDD

NEG5V Bypass capacitor 0.1 \muF/10 V Bypass capacitor for the negative charge pump **9.2.1.2.4 GPIO For Thermistor Inputs**

## When using external thermistor, for ADC measurement only, there is no limitation of what type of thermistors

(NTC or PTC) or the bias resistor (R1) value or whether the thermistor is placed on high side or low side with respected to the bias resistor.

## However, when using with the integrated OTUT comparators, the programmable OT and UT threshold ranges

are designed to work with a 103NTC (10 kΩ at 25°C) type of NTC thermistor, following the connection shown in Figure 9-5 with different options for the R1 and R2 resistors. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

- • Option 1: R 1 = 10 kΩ, and no R 2 - • Option 2: R 1 = 10 kΩ, and R 2 = 100 kΩ for better linearity at cold temperature - • Option 3: R 1 = 3.6 kΩ, and R 2 = 15 kΩ. This base option can be used for NTC used for the OTCB  feature assuming system designer allows the PCB temperature to be higher than the cell temperature during balancing. Because the device does not differentiate which NTC is used on the cells versus the PCB, NTC biasing with this option scales the NTC's hot temperature curve differently, allowing the threshold set for OT comparator to be triggered at a lower GPIO voltage. Thus, making the device to only trigger OTCB threshold on this NTC.

The device does not require external RC for temperature measurement. However, it is common for system designer to add an RC filter on the GPIO pin for the NTC circuit. System designer can select the RC values for the application need. Example: R GPIO = 1 kΩ, C GPIO = 0.1 μF to 1 μF.

Unused GPIO must be grounded to AVSS with a 10-kΩ resistor.

# 1... F

# GPIO (OPTIONAL)

# GPIO (OPTIONAL)

# (OPTIONAL) Device

# NTC

# TSREF

# GPIO1 **Figure 9-5. NTC Connection** **9.2.1.2.5 Internal Balancing Current**

When internal cell balancing is used, the max balancing current the device can support (before going into thermal pause) can vary based on the ambient temperature.

# 9.2.1.2.6 UART, NFAULT

If device is used as a base device, the UART interface requires the TX and RX pins are pulled up through a 10-kΩ to 100-kΩ resistor. Do not leave TX and RX unconnected. The TX must be pulled high to prevent triggering an invalid communications frame during the idle state. When using a serial cable to connect to the host controller, connect the TX pull-up on the host side and the RX pull-up to the CVDD on the device side.

If device is used as a stack device, the TX pin is disabled by default and is left floating. RX pin is shorted to CVDD.

NFAULT pin for base device, if not used, must be left floating. Otherwise, pull it up with 100-kΩ to CVDD. NFAULT pin on stack device is floating. **9.2.1.2.7 Daisy Chain Isolation**

The device works with multiple daisy chain isolation types: capacitor isolation, capacitor-choke isolation, and transformer isolation. For devices that are daisy-chained on the same PCB, capacitor isolation without ESD diode as shown in Figure 9-6 is sufficient. Unused COMLP/H or COMHP/N pins must be connected with 1-kΩ termination resistor.

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

***9.2.1.2.7.1 Devices Connected on the Same PCB***

## Table 9-2. Isolation Components for Devices Connected on the Same PCB

**Components** **Value** **Description (Capacitor Isolation on the Same PCB)** R TERM 1 kΩ Termination resistor

R SERIES 49 Ω Filter resistor and impedance matching resistor. The connection between devices must be ~120 Ω (~50 Ω on each end of the signal connection of the device plus 10-Ω internal resistance) C BYPASS 220 pF/50 V Bypass capacitor

C ISO 2.2 nF Isolation capacitor Voltage rating depends on application requirement. It is common to select 2x of module voltage rating to provide standoff margin in the event of a fault in the system.

| SERIES | 49 Ÿ |
|:--- |:--- |
| ISO | 2.2 nF |
| SERIES | 49 Ÿ |
| BYPASS | 220 pF |

# ISO 2.2 nF

# SERIES 49 Ÿ

# BYPASS 220 pF

# BYPASS 220 pF TERM 1 k

# TERM 1 k SERIES 49 Ÿ

| ISO | 2.2 nF |
|:--- |:--- |
| SERIES | 49 Ÿ |
| BYPASS | 220 pF |
| BYPASS | 220 pF |

# SERIES 49 Ÿ

# BYPASS 220 pF

# BYPASS 220 pF

# COMLP

# COMLN

# COMHP

# COMHN

Components Required for Cap Coupled Daisy Chain on the same PCB

## Figure 9-6. Capacitor Isolation with Devices on the Same PCB

***9.2.1.2.7.2 Devices Connected on Different PCBs***

## For devices that are daisy-chained to different PCBs through a pair of twisted cables, all three isolation types can

be used for daisy chain isolation, however it is not possible to use one type of isolation on one side of the daisy chain (for example, transformer isolation on COMLP/N to the Battery Management Unit) while using a different type of isolation for the other side of the daisy chain (for example, capacitor isolation on COMH/N to the Cell Module Unit).

## Option 1: Capacitor Isolation

## Table 9-3. Components for Capacitor Isolation on Different PCBs

**Components** **Value** **Description (Capacitor Isolation Between PCBs)** R TERM 1 kΩ Termination resistor

R SERIES 49 Ω Filter resistor and impedance matching resistor. The connection between devices must be ~120 Ω (~50 Ω on each end of the signal connection of the device plus 10-Ω internal resistance). C BYPASS 220 pF/50 V Bypass capacitor

C ISO 2.2 nF Isolation capacitor Voltage rating depends on application requirement. It is common to select 2x of module voltage rating to provide standoff margin in the event of a fault in the system.

ESD diode TVS diode The ESD protector should provide protection to the communication interface pins during hot-plug events and also for absorption of high-voltage transients during service disconnect or reconnect. Select the ESD diodes to limit the maximum voltage on the COM\* bus to below the maximum rating. A voltage rating close to the maximum voltage to provide the highest possible commonmode voltage range is recommended for best EMC performance. The capacitance must be low compared to the coupling capacitance (if using capacitor coupling). **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

| ISO | 2.2 nF |
|:--- |:--- |
| ISO | 2.2 nF |
| ISO | 2.2 nF |
| ISO | 2.2 nF |

# ISO 2.2 nF

# ISO 2.2 nF

# ISO 2.2 nF

| RSERIES | 
Ÿ | RSERIES | 
Ÿ |
|:--- |:--- |:--- |:--- |
| RSERIES | 
Ÿ | RSERIES | 
Ÿ |
| CBYPASS | 220 pF | CBYPASS | 220 pF |
| RTERM | 1 kŸ | RTERM | 1 kŸ |

# R SERIES  Ÿ R SERIES  Ÿ

# C BYPASS 220 pF C BYPASS 220 pF

# R TERM 1 k Ÿ R TERM 1 k Ÿ

# COMHP

# COMHN

# ESD

| ISO | 2.2 nF |
|:--- |:--- |
| ISO | 2.2 nF |
| ISO | 2.2 nF |
| ISO | 2.2 nF |

# ISO 2.2 nF

# ISO 2.2 nF

# ISO 2.2 nF

| RSERIES | 
Ÿ | RSERIES | 
Ÿ |
|:--- |:--- |:--- |:--- |
| RSERIES | 
Ÿ | RSERIES | 
Ÿ |
| BYPASS | 220 pF | BYPASS | 220 pF |
| CBYPASS | 220 pF | CBYPASS | 220 pF |
| RTERM | 1 kŸ | RTERM | 1 kŸ |

# R SERIES  Ÿ R SERIES  Ÿ

# BYPASS 220 pF BYPASS 220 pF

# C BYPASS 220 pF C BYPASS 220 pF

# R TERM 1 k Ÿ R TERM 1 k Ÿ

# COMLP

# COMLN

# ESD

| ISO | 2.2 nF |
|:--- |:--- |
| ISO | 2.2 nF |
| RSERIES | 
Ÿ |
| RSERIES | 
Ÿ |
| BYPASS | 220 pF |
| CBYPASS | 220 pF |
| RTERM | 1 kŸ |

# ISO 2.2 nF

# R SERIES  Ÿ

# R SERIES  Ÿ

# BYPASS 220 pF

# C BYPASS 220 pF

# R TERM 1 k Ÿ

# COMLP

# COMLN

# ESD Twisted pair cabling between modules

Components Required for Cap Coupled Daisy Chain on different pcb

# Figure 9-7. Capacitor Isolation on Different PCB

# Figure 9-7 shows the capacitor isolation circuit for devices connecting between PCBs. Similar to the capacitor

isolation on the same PCB case, the capacitor must be rated with a high enough voltage to provide standoff margin in the event of a fault in the system that exposes the device to a local hazardous voltage. The voltage is determined by the application requirement but it is common to select 2x of the module voltage.

# The capacitance on the daisy chain bus has a direct effect on performance. All parasitic capacitances from

the support components and cabling must be taken into consideration when designing for communication robustness to EMC. Capacitance from the cables, ESD diodes, bypass capacitance, and chokes form a capacitive divider with the isolation capacitors that may affect performance. Additionally, the amount of capacitance on the bus has a direct impact to the operating current during communication (the capacitor charging or discharging).

# Option 2: Capacitor Plus Common-Mode Choke Isolation

# Table 9-4. Components for Capacitor Plus Common-Mode Choke Isolation

# Components

**Value** **Description (Capacitor Plus Choke Isolation Between PCBs)**

# R TERM 1 kΩ Termination resistor

# R SERIES

49 Ω Filter resistor and impedance matching resistor. The connection between devices must be ~120 Ω (~50 Ω on each end of the signal connection of the device plus 10-Ω internal resistance)

# C BYPASS 220 pF/50 V Bypass capacitor

# C ISO

2.2 nF Isolation capacitor Voltage rating depends on application requirement. It is common to select 2x of module voltage rating to provide a standoff margin in the event of a fault in the system.

# Common-mode choke

# 100 μH to 500 μH Common-mode choke (The inductance range 100 μH to 500 μH is a general guidance value, not

# a guaranteed range, as there are many parameters affecting the performance of a common-mode choke.)

# ESD diode (optional)

# TVS diode

Optional ESD protection depends on pcb level ESD requirement (Adding this diode or not is subject to the user's system level ESD requirement)

# R SERIES  Ÿ R SERIES  Ÿ

# R SERIES  Ÿ R SERIES  Ÿ

| CISO | 2.2 nF |
|:--- |:--- |
| CISO | 2.2 nF |
| CISO | 2.2 nF |
| CISO | 2.2 nF |

# C ISO 2.2 nF

# C ISO 2.2 nF

# C ISO 2.2 nF

# BYPASS 220 pF BYPASS 220 pF

# R TERM 1 k Ÿ R TERM 1 k Ÿ

# COMLP

# COMLN Twisted pair cabling between modules

# R SERIES  Ÿ R SERIES  Ÿ

| CISO | 2.2 nF |
|:--- |:--- |
| CISO | 2.2 nF |
| ISO | 2.2 nF |
| ISO | 2.2 nF |

# C ISO 2.2 nF

# ISO 2.2 nF

# ISO 2.2 nF

# BYPASS 220 pF BYPASS 220 pF

# R TERM 1 k Ÿ R TERM 1 k Ÿ

# COMHP

# COMHN

# R SERIES  Ÿ R SERIES  Ÿ Common-mode Choke 470 µH Common-mode Choke 470 µH

## Components Required for cap-choke Daisy Chain with Cabling ESD (optional) ESD (optional)

# Figure 9-8. Capacitor Plus Choke Isolation

# Longer cable lengths, or abnormally noisy applications may require the use of a common-mode choke filter.

Capacitor plus choke isolation has better noise immunity than capacitor only. For these applications, use

# BQ79616 SLUSF21 - JUNE 2023 **<https://www.ti.com**>

# Submit Document Feedback

Copyright © 2023 Texas Instruments Incorporated

## an automotive grade from 100-μH to 500-μH common-mode filter minimum for proper operation. To achieve

the best performance in noisy environments, use dual common-mode filters (470 μH). The recommended impedance of the choke is at least 1 kΩ from 1 MHz to 100 MHz and above 300 Ω for higher frequencies.

## Option 3: Transformer Isolation

## Table 9-5. Components for Transformer Isolation

**Components** **Value** **Description (Capacitor Plus Choke Isolation Between PCBs)** R TERM 1 kΩ Termination resistor

R SERIES 49 Ω Filter resistor and impedance matching resistor. The connection between devices must be ~120 Ω (~50 Ω on each end of the signal connection of the device plus 10-Ω internal resistance) C BYPASS 220 pF/50 V Bypass capacitor Transformer Inductance: 150 μH to 1400 \muH

The inductance range 150 μH to 1400 μH is a general guidance value, not a guaranteed range as there are many parameters affecting the performance of transformer. When coming to specific recommended part, please refer to SLVAEP4 *BQ79616 Daisy Chain Communications * *Application Report*. User shall perform the through test in their environment. ESD diode (optional)

TVS diode Optional ESD protection depends on pcb level ESD requirement (Adding this diode or not is subject to the user's system level ESD requirement.)

## Transformer isolation is supported. Transformer Isolation shows how it can be implemented. For example,

transformer isolation can be used between the low-voltage and high-voltage boundary for galvanic isolation.

| Twisted pair cabling | between modules |
|:--- |:--- |
| SERIES |  |
| SERIES | 49   |
| BYPASS | 220 pF |
| BYPASS | 220 pF |
| TERM | 1 k |

# SERIES 

# SERIES 49  

# BYPASS 220 pF

# BYPASS 220 pF

# TERM 1 k 

# COMLP

# COMLN

| BYPASS2 | 100 pF |
|:--- |:--- |
| SERIES |  |
| BYPASS | 220 pF |
| BYPASS | 220 pF |
| TERM | 1 k |

# SERIES 

# BYPASS 220 pF

# BYPASS 220 pF

# TERM 1 k 

# COMHP

# COMHN

# SERIES 

# BYPASS2 100 pF Transformer Isolation Transformer Isolation ESD (optional) ESD (optional)

## Figure 9-9. Transformer Isolation **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* ***9.2.1.3 Application Curve***

**Figure 9-10. Response Frame for 8 Registers Read from Stack Devices** **9.2.2 Daisy Device Application Circuit**

The following application circuit (see Figure 9-11 ) is based on the BQ79616 device connecting to a 16S module.

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated Isolation circuit Bq79600 Communication Device

# VCC

# TX RX

# COMHP COMHM

# BAT

# TX RS

# MCU Leave unconnected for Base Device

# BAT

# LDOIN

# NPNB

# COMHP

# COMHN

# COMLP

# COMLN

# VC16

# VC0 **... **

# CB16

# CB0 **Stack-N Device**

# REFHP

# AVDD

# REFHM

# DVDD

# DVSS

# CVSS

# CVDD

# NFAULT GND

# COMLP

# COMLN To COMH of the Top of Stack Isolation circuit

**OPTIONAL**: Only necessary for ring architecture applications

# COMHP

# COMHN To COML of the Base Device Isolation circuit

**OPTIONAL**: Only necessary for ring architecture applications

**HV System ** **(Cell Module Control)** **LV System ** **(Battery Management Unit)** **Isolation**

# NEG5V

# AVSS

# RX

# NFAULT

# TX

# GPIO2

# TSREF

# GPIO1

# To CVDD

# 4.7 F

# N

# N

# N

# 1 F

# 1 F

# N

# N

# 1 F

# N

# N

# 0.1 F

# N 1 k

# 0.1 F

# N

# 0.22 F 10 nF

# N 0.47 µF

# CELL 16 +

# N 0.47 µF

# N

# + CELL 1 **... **

# N 0.47 uF 0.47 uF

# N **... ** 1 µF 10 k 10 k

# CELL 16

# CELL 1

# BAT

# LDOIN

# NPNB

# COMHP

# COMHN

# COMLP

# COMLN

# VC16

# VC0

# CB16

# CB0

# REFHP

# AVDD

# REFHM

# DVDD

# DVSS

# CVSS

# CVDD

# NEG5V

# AVSS

# GPIO2

# TSREF

# GPIO1

# 4.7 F

# N

# N

# N

# 1 F

# 1 F

# N

# N

# 1 F

# N

# N

# 0.1 F

# N 0.1 F

# N

# 0.22 F 10 nF

# N 0.47 µF

# CELL 16 +

# N 0.47 µF

# N

# + CELL 1

# N 0.47 µF 0.47 µF

# N

# CELL 16

# CELL 1 1 µF 10 k 10 k Leave unconnected for Top of Stack Device

# AVSS

# NFAULT

# TX

# RX

# CVDD

# PMIC HV to LV Isolation (Transformer) **Stack 1 Device** 0.47 µF 0.47 uF

# Figure 9-11. Daisy Device Application Circuit

# www.ti.com

# BQ79616 SLUSF21 - JUNE 2023

# Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* ***9.2.2.1 Design Requirements***

See Section 9.2.1.1 section for design requirements. ***9.2.2.2 Detailed Design Procedure***

See Section 9.2.1.2 section for detailed design procedure.

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

# 10 Power Supply Recommendations

## The device is powered by BAT pin and the LDOIN pin, with which the LDOIN pin is regulated by the pre

regulation circuit formed with an external NPN. The device can be powered by a battery module as low as 9 V (without OTP programming) on the BAT pin. However, system designers must scale the R NPN resistor accordingly to ensure there is sufficient headroom to have 6 V on the LDOIN pin after the IR drop across R NPN and the external NPN. For example, if BAT voltage is at 9 V, the R NPN reduces to 10 Ω to allow sufficient voltage at the LDOIN pin.

# 0.22 P F 0.1 µF

# NPN 10 nF

# BAT

# VC16

# NPNB

# LDOIN

#...

#...

# Q1

# CELL 16 +

Scale the value of RNPN according to the min module voltage.

Lower the min module voltage in application, smaller the RNPN value should be used

## Figure 10-1. Device Powering Path

## Multiple cell modules can be connected to the same device through the bus bar support of the BQ79616 family.

The same power will be drawn from each of the cell modules. 10 nF

# 0.1... F

# 0.22... F

# NPN cell module cell module

Small current path to BAT for an Always-on circuit

# Q1 Main current path to power the device

# BAT

# NPNB

# LDOIN

## Figure 10-2. Device Can Be Powered by Multiple Cell Modules in Stack **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## 11 Layout

The layout for this device must be designed carefully. Any design outside these guidelines can affect the ADC accuracy and EMI performance. Care must be taken in the layout of signals to and from the device to avoid coupling noise onto sensitive inputs. The layout of ground and power connections, as well as communication signals, should also be made carefully. **11.1 Layout Guidelines** **11.1.1 Ground Planes**

It is very important to establish a clean grounding scheme to ensure best performance of the device. There are three ground pins (AVSS, DVSS, CVSS) for the device's internal power supplies and one ground reference (REFHM) for the precision reference. There are noisy grounds and quiet grounds that must be separated in the layout initially and rejoined together in a lower PCB layer. The external components (for example, bypass capacitors) must be tied to the proper grounding group if possible to keep the separation of noisy and quiet grounds apart. - • AVSS ground: - - Bypass capacitor for these pins: BAT, VC0, CB0, and AVDD. - - Package power pad - • DVSS ground: - - Bypass capacitor for DVDD. - - GPIO filter capacitor (if used). It can also connect to AVSS ground plane, if needed. - • CVSS ground: - - Bypass capacitor for GPIOs, CVDD, TSREF, NEG5V, LDOIN, COMHP/N, and COMLP/N. - • REFHM ground: - - Bypass capacitor for REFHP. - - If possible, separate out REFHM from AVSS on the signal connection layer and reconnect REFHM to  AVSS ground plane in the lower layer.

Even on a PCB layer that is mainly for signal routing, it is good practice to have a small island of ground pour if possible to provide a low-impedance ground, rather than simply a via through the ground trace to an lower ground plane.

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

# REFHM

# REFHP

Small island of ground pour if possible to via down to lower layers

# AVSS **AVSS**

# REFHM

# CVDD

# CVSS

# NEG5V

# CVSS BAT

# DVDD

# DVSS

# DVSS

# AVSS

# DVSS

# CVSS

Create more solid ground planes as well as separating noisy and quiet grounds for better performance Connect REFHM to AVSS Connect all grounds together **Main Ground Plane** Layer1 Layer2 Layer3

## Figure 11-1. Grounding Layout Consideration

## If multiple devices are placed on the same PCB, each device must have its own ground plane with proper layout clearance. **Ground Plane 2** bq796xx Device 2 **Ground Plane 1** bq796xx Device 1

**Proper clearance is ** **required. Depends on ** **the number of cells ** **connects to each ** **device, the 2 grounds ** **can be \>50V apart  **

## Figure 11-2. Separate Ground Planes Per Device on the Same PCB **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

**11.1.2 Bypass Capacitors for Power Supplies and Reference**

The bypass capacitors of the following pins must be placed as close to the device pins as possible to ensure proper performance, especially for the REFHP capacitor. - • REFHP, BAT, LDOIN, AVDD, DVDD, CVDD, TSREF, and NEG5V **11.1.3 Cell Voltage Sensing**

Cell voltage sensing traces (VC pins and CB pins) must be placed in parallel with impedance matching. The balancing traces (CB pins) must be sized properly to carry the maximum balancing current and proper thermal performance for the application.

It is recommended to use separate cables, connect tabs, and PCB traces for the BAT pin and top VC pin connections. Same applies to AVSS and VC0 connections. This avoids the device current impact on the top and bottom cell voltage measurements.

If the same cable and connector tab is used for BAT/top VC pins connection and AVSS/VC0 pins connection, the PCB trace going to BAT/top VC pins and AVSS/VC0 pins must be separated at the connector tabs. Note the device current will still go through the cell to the PCB cable, which may introduce IR errors across the cable connection to the top and bottom cell measurements. **11.1.4 Daisy Chain Communication**

It is important to have proper layout on the COMHP/N and COMLP/N circuits in order to have the best robust daisy chain communication. - • Keep differential traces as short as possible and as straight as possible. Minimize turns and avoid any  looping on the traces. - • Keep the differential traces on the same layers. Run the trace in parallel with shielding and matching trace  impedance. - • Place the isolation components close to the connectors. - • When using capacitive isolation, place the high-voltage capacitor of the COMxP/N pair (where x = H or L)  close to each other along the parallel traces. - • Create a keep-out area (no other traces and no ground plane) around the daisy chain components in all PCB  layers.

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated **Main Ground Plane**

# CVDD

# CVSS

# CVSS

# NEG5V

# COMHN

# COMHP

# COMLN

# COMLP

# CVSS Shield COMH/L traces

Keep COMH/L trace straight and on the same layer Keep-out area: no other traces/ground plans Daisy chain communication circuits Layer1 Layer2 Layer3

| TERM | 1 kŸ | TERM | 1 kŸ |
|:--- |:--- |:--- |:--- |
| SERIES | 
Ÿ | SERIES | 
Ÿ |
| SERIES | 
Ÿ | SERIES | 
Ÿ |

# SERIES  Ÿ SERIES  Ÿ

# SERIES  Ÿ SERIES  Ÿ

| ISO | 2.2 nF |
|:--- |:--- |
| ISO | 2.2 nF |
| ISO | 2.2 nF |
| ISO | 2.2 nF |

# ISO 2.2 nF

# ISO 2.2 nF

# ISO 2.2 nF

| SERIES | 
Ÿ | SERIES | 
Ÿ |
|:--- |:--- |:--- |:--- |
| SERIES | 
Ÿ | SERIES | 
Ÿ |
| TERM | 1 kŸ | TERM | 1 kŸ |

# SERIES  Ÿ SERIES  Ÿ

# TERM 1 k Ÿ TERM 1 k Ÿ

| TERM | 1 kŸ |
|:--- |:--- |
| SERIES | 
Ÿ |
| SERIES | 
Ÿ |
| ISO | 2.2 nF |
| ISO | 2.2 nF |
| SERIES | 
Ÿ |
| SERIES | 
Ÿ |
| TERM | 1 kŸ |

# SERIES  Ÿ

# SERIES  Ÿ

# ISO 2.2 nF

# ISO 2.2 nF

# SERIES  Ÿ

# SERIES  Ÿ

# TERM 1 k Ÿ

# Figure 11-3. Daisy Chain Layout Consideration

# 11.2 Layout Example

# This section presents the BQ79616 Evaluation Module (EVM) design as a layout example.

## www.ti.com

# BQ79616 SLUSF21 - JUNE 2023

## Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## Figure 11-4. Top Signal Layer

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## Figure 11-5. Second Layer with Solid, Separate Ground Planes **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## Figure 11-6. ThIrd Layer with Single Ground Plane

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## 12 Device and Documentation Support **12.1 Device Support** **12.1.1 Third-Party Products Disclaimer**

# TI'S PUBLICATION OF INFORMATION REGARDING THIRD-PARTY PRODUCTS OR SERVICES DOES NOT

CONSTITUTE AN ENDORSEMENT REGARDING THE SUITABILITY OF SUCH PRODUCTS OR SERVICES OR A WARRANTY, REPRESENTATION OR ENDORSEMENT OF SUCH PRODUCTS OR SERVICES, EITHER ALONE OR IN COMBINATION WITH ANY TI PRODUCT OR SERVICE.

**12.2 Receiving Notification of Documentation Updates**

To receive notification of documentation updates, navigate to the device product folder on ti.com. Click on *Subscribe to updates* to register and receive a weekly digest of any product information that has changed. For change details, review the revision history included in any revised document. **12.3 Support Resources**

TI E2E ™ support forums are an engineer's go-to source for fast, verified answers and design help - straight from the experts. Search existing answers or ask your own question to get the quick design help you need.

Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do not necessarily reflect TI's views; see TI's Terms of Use.

**12.4 Trademarks** TI E2E ™ is a trademark of Texas Instruments. All trademarks are the property of their respective owners. **12.5 Electrostatic Discharge Caution**

This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.

ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may be more susceptible to damage because very small parametric changes could cause the device not to meet its published specifications. **12.6 Glossary**

TI Glossary This glossary lists and explains terms, acronyms, and definitions. **<https://www.ti.com**>

# BQ79616 SLUSF21 - JUNE 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## 13 Mechanical, Packaging, and Orderable Information

The following pages include mechanical, packaging, and orderable information. This information is the most current data available for the designated devices. This data is subject to change without notice and revision of this document. For browser-based versions of this data sheet, refer to the left-hand navigation.

**BQ79616** SLUSF21 - JUNE 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

# PACKAGE OPTION ADDENDUM <https://www.ti.com> 31-Oct-2025

# PACKAGING INFORMATION **Orderable part number** **Status** (1) **Material type** (2)

**Package \| Pins** **Package qty \| Carrier** **RoHS** (3) **Lead finish/** **Ball material** (4) **MSL rating/** **Peak reflow** (5) **Op temp (°C)** **Part marking** (6)

BQ79616PAPR Active Production HTQFP (PAP) \| 64 1000 \| LARGE T&R Yes NIPDAU Level-3-260C-168 HR -40 to 125 BQ75216

BQ79616PAPR.A Active Production HTQFP (PAP) \| 64 1000 \| LARGE T&R Yes NIPDAU Level-3-260C-168 HR -40 to 125 BQ75216 **(1)** ** Status: ** For more details on status, see our product life cycle.

**(2)** ** Material type: ** When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance, reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind.

**(3)** ** RoHS values: ** Yes, No, RoHS Exempt. See the TI RoHS Statement for additional information and value definition.

**(4)** ** Lead finish/Ball material: ** Parts may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two lines if the finish value exceeds the maximum column width.

**(5)** ** MSL rating/Peak reflow: ** The moisture sensitivity level ratings and peak solder (reflow) temperatures. In the event that a part has multiple moisture sensitivity ratings, only the lowest level per JEDEC standards is shown. Refer to the shipping label for the actual reflow temperature that will be used to mount the part to the printed circuit board.

**(6)** ** Part marking: ** There may be an additional marking, which relates to the logo, the lot trace code information, or the environmental category of the part. Multiple part markings will be inside parentheses. Only one part marking contained in parentheses and separated by a "~" will appear on a part. If a line is indented then it is a continuation of the previous line and the two combined represent the entire part marking for that device. **Important Information and Disclaimer:** The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release. In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis. **OTHER QUALIFIED VERSIONS OF BQ79616:** - Automotive: BQ79616-Q1 Addendum-Page 1

# PACKAGE OPTION ADDENDUM <https://www.ti.com> 31-Oct-2025

## NOTE: Qualified Version Definitions

- Automotive - Q100 devices qualified for high-reliability automotive applications targeting zero defects Addendum-Page 2

# PACKAGE MATERIALS INFORMATION <https://www.ti.com> 7-Jul-2023

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

# BQ79616PAPR

HTQFP PAP 330.0 24.4 13.0 13.0 1.5 16.0 24.0 Q2 Pack Materials-Page 1

# PACKAGE MATERIALS INFORMATION <https://www.ti.com> 7-Jul-2023

# TAPE AND REEL BOX DIMENSIONS ***Width (mm)***

# W

# L

# H \*All dimensions are nominal

**Device** **Package Type** **Package Drawing** **Pins** **SPQ** **Length (mm)** **Width (mm)** **Height (mm)**

# BQ79616PAPR HTQFP PAP 367.0 367.0 55.0 Pack Materials-Page 2 <https://www.ti.com>

# GENERIC PACKAGE VIEW

This image is a representation of the package family, actual package may vary. Refer to the product data sheet for package details.

## HTQFP - 1.2 mm max height **PAP 64** QUAD FLATPACK **10 x 10, 0.5 mm pitch**

# 4226442/A <https://www.ti.com>

# PACKAGE OUTLINE

# C

# 64X 0.27 0.17 60X 0.5

# PIN 1 ID

# (0.127) TYP 0.15 0.05 0 -7

# 4X 7.5

# 12.2 11.8 TYP

# B 10.2 9.8 NOTE 3

# A

# 10.2 9.8 NOTE 3 0.75 0.45

# 0.25 GAGE PLANE

# 1.2 MAX (1)

# PowerPAD TQFP - 1.2 mm max height **PAP0064F**

# PLASTIC QUAD FLATPACK

NOTES: 1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M. 2. This drawing is subject to change without notice. 3. This dimension does not include mold flash, protrusions, or gate burrs. 4. Strap features may not be present. 5. Reference JEDEC registration MS-026. PowerPAD is a trademark of Texas Instruments.

# TM

# 0.08 C A B

# SEE DETAIL A

# SEATING PLANE

# A 17 DETAIL  A TYPICAL

# 0.08 C

# SCALE 1.300

# PLASTIC QUAD FLATPACK

# 4226412/A 11/2020

| 6.5 | 5.3 |
|:--- |:--- |
| 8X (R0.091) | NOTE 4 |
| 20X (R0.137) | NOTE 4 |

# 8X (R0.091) NOTE 4

# 20X (R0.137) NOTE 4 <https://www.ti.com>

# EXAMPLE BOARD LAYOUT

# 0.05 MAX ALL AROUND 0.05 MIN ALL AROUND (11.4) (11.4)

# 60X (0.5)

# 64X (1.5)

# 64X (0.3)

# ( 0.2) TYP VIA (6.5)

# (8) NOTE 8

# (R0.05) TYP

# (1.1 TYP)

# (1.1 TYP)

# PowerPAD TQFP - 1.2 mm max height **PAP0064F**

# PLASTIC QUAD FLATPACK

# TM

NOTES: (continued) 6. Publication IPC-7351 may have alternate designs.  7. Solder mask tolerances between and around signal pads can vary based on board fabrication site.  8. This package is designed to be soldered to a thermal pad on the board. See technical brief, Powerpad thermally enhanced package, Texas Instruments Literature No. SLMA002 (<https://www.ti.com/lit/slma002)> and SLMA004 (<https://www.ti.com/lit/slma004).> 9. Vias are optional depending on application, refer to device data sheet. It is recommended that vias under paste be filled, plugged or tented. 10. Size of metal pad may vary due to creepage requirement.

# LAND PATTERN EXAMPLE EXPOSED METAL SHOWN SCALE:6X

# SYMM

# SOLDER MASK DEFINED PAD

# METAL COVERED BY SOLDER MASK

# SEE DETAILS

# SYMM

# METAL

# SOLDER MASK OPENING

# NON SOLDER MASK DEFINED SOLDER MASK DETAILS

# EXPOSED METAL

| SOLDER MASK | OPENING |
|:--- |:--- |
| METAL UNDER | SOLDER MASK |
| SOLDER MASK | DEFINED |

# METAL UNDER SOLDER MASK

# SOLDER MASK DEFINED

# EXPOSED METAL

# 4226412/A 11/2020 <https://www.ti.com>

# EXAMPLE STENCIL DESIGN (6.5)

# 60X (0.5)

# 64X (1.5)

# 64X (0.3)

# (R0.05) TYP (11.4) (11.4)

# PowerPAD TQFP - 1.2 mm max height **PAP0064F**

# PLASTIC QUAD FLATPACK

NOTES: (continued) 11. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate design recommendations. 12. Board assembly site may have different recommendations for stencil design.

# TM

# SOLDER PASTE EXAMPLE

EXPOSED PAD 100% PRINTED SOLDER COVERAGE BY AREA SCALE:6X

# SEE TABLE FOR

DIFFERENT OPENINGS FOR OTHER STENCIL THICKNESSES

# BASED ON 0.125 THICK STENCIL SYMM

# SYMM

# METAL COVERED BY SOLDER MASK

# 4226412/A 11/2020

# 5.49 X 5.49

0.175 5.93 X 5.93 0.15 6.5 X 6.5 (SHOWN) 0.125 7.27 X 7.27 0.1

# SOLDER STENCIL OPENING STENCIL THICKNESS

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