AC Input Voltage (V RMS ) Power (mW)

# D001

2.7-W Low-Side Buck Standby Power UCC28881 Power Consumption

# UCC28881

# GND

# GND

# FB

# VDD

# DRAIN

# NC

# HVIN IN

# OUT +

| Product | Folder |
|:--- |:--- |
| Sample & | Buy |
| Technical | Documents |
| Tools & | Software |
| Support & | Community |
| Reference | Design | Sample & Buy Technical Documents Tools & Software Support & Community Reference Design

# UCC28881

SLUSC36B -NOVEMBER 2015-REVISED JANUARY 2016 **UCC28881 700-V, 225-mA Low Quiescent Current Off-Line Converter**

## Features

**Description** The UCC28881 integrates the controller and a 14- Ω, 1 • Integrated 14-\Omega, 700-V Power MOSFET

700-V power MOSFET into one monolithic device. - • Integrated High-Voltage Current Source for The device also integrates a high-voltage current Internal Device Bias Power source, enabling start up and operation directly from - • Integrated Current Sense the rectified mains voltage. UCC28881 is the same family device of UCC28880, with higher current - • Internal Soft Start

handling capability. - • Self-Biased Switcher (Start Up and Operation

The low quiescent current of the device enables Directly from Rectified Mains Voltage)

excellent efficiency. With the UCC28881 the most - • Supports Buck, Buck-Boost and Flyback common converter topologies, such as buck, buckTopologies boost and flyback can be built using a minimum - • \<100- μ A Device Quiescent Current number of external components. - • Robust Current Protection During Load Short The UCC28881 incorporates a soft-start feature for Circuit controlled start up of the power stage which - • Protection minimizes the stress on the power-stage components. - - Current Limit - - Overload and Output Short Circuit **Device** ** ** **Information** **(1)** - - Over Temperature **PART NUMBER** **PACKAGE** **BODY** ** ** **SIZE (NOM)**

UCC28881 SOIC (7) 5.00 mm \times 6.20 mm **Applications**

(1) For all available packages, see the orderable addendum at - • AC-to-DC Power Supplies the end of the data sheet. (Non-Isolated Buck Converter with Output Current up to 225 mA for CCM; 150 mA for DCM) - • E-Meter, Home Automation SMPS - • Bias Power for MCU, RF and IoT Enabled Devices - • Appliances, White Goods and LED Drivers **Simplified Schematic**

An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications, intellectual property matters and other important disclaimers. PRODUCTION DATA.

# UCC28881

# SLUSC36B -NOVEMBER 2015-REVISED JANUARY 2016 **<https://www.ti.com**>

## Table of Contents

8.3 Feature Description................................................. 10 **Features**.................................................................. 1

8.4 Device Functional Modes........................................ 12 **Applications**........................................................... 1

**Application and Implementation**........................ 16 **Description**............................................................. 1

9.1 Application Information............................................ 16 **Revision** ** ** **History**..................................................... 2

9.2 Typical Application.................................................. 16 **Device** ** ** **Comparison**............................................... 3

**Power Supply Recommendations**..................... 26 **Pin** ** ** **Configuration and Functions**......................... 3

**Layout**................................................................... 26 **Specifications**......................................................... 4

11.1 Layout Guidelines................................................ 26 7.1 Absolute Maximum Ratings...................................... 4

11.2 Layout Example.................................................... 26 7.2 ESD Ratings.............................................................. 4

**Device** ** ** **and Documentation** ** ** **Support**................. 27 7.3 Recommended Operating Conditions....................... 5

| 12.1 | Device Support.................................................... 27 | 7.4 | Thermal Information.................................................. 5 |
| ---: |:--- | ---: |:--- |
| 12.2 | Community Resources.......................................... 27 | 7.5 | Electrical Characteristics........................................... 6 |
| 12.3 | Trademarks........................................................... 27 | 7.6 | Switching Characteristics.......................................... 6 |
| 12.4 | Electrostatic Discharge Caution............................ 27 | 7.7 | Typical Characteristics............................................. 7 |

12.2 Community Resources.......................................... 27 7.5 Electrical Characteristics........................................... 6

12.3 Trademarks........................................................... 27 7.6 Switching Characteristics.......................................... 6

12.4 Electrostatic Discharge Caution............................ 27 7.7 Typical Characteristics............................................. 7

12.5 Glossary................................................................ 27 **Detailed Description**.............................................. 9

**Mechanical,** ** ** **Packaging,** ** ** **and Orderable** 8.1 Overview................................................................... 9 **Information**........................................................... 27 8.2 Functional Block Diagram......................................... 9

## Revision History

| Changes from Revision A (December 2015) to Revision B | Page |
|:--- |:--- |
| •• Changed the documents title from, "UCC28881 700-V, 225-mA Low Quiescent Current Off-Line Switcher", to | "UCC28881 700-V, 225-mA Low Quiescent Current Off-Line Converter"............................................................................ 1 |
| Changes from Original (November 2015) to Revision A | Page |

- • Changed the documents title from, "UCC28881 700-V, 225-mA Low Quiescent Current Off-Line Switcher", to "UCC28881 700-V, 225-mA Low Quiescent Current Off-Line Converter"............................................................................ 1

**Changes** ** ** **from** ** ** **Original** ** ** **(November** ** ** **2015) to** ** ** **Revision** ** ** **A** **Page**

- • Changed marketing status from product preview to production data.................................................................................... 1

*Submit Documentation Feedback* Copyright © 2015-2016, Texas Instruments Incorporated Product Folder Links: * * *UCC28881*

# DRAIN

# NC

# HVIN

# GND

# GND

# FB

# VDD

# UCC28881

# www.ti.com SLUSC36B -NOVEMBER 2015-REVISED JANUARY 2016

## Device Comparison

## Power Handling Capability with Different Topologies

# MAXIMUM OUTPUT CURRENT

**MAXIMUM** ** ** **OUTPUT** ** ** **POWER** **for** ** ** **85** ** ** **~ 265 VAC OPEN** ** ** **FRAME DESIGN** **for** ** ** **85** ** ** **~ 265 VAC OPEN** ** ** **FRAME DESIGN** **PRODUCT**

# NON-ISOLATED BUCK **FLYBACK**

# UCC28880 100 mA 3 W

# UCC28881 225 mA 4.5 W

## Pin Configuration and Functions

**D** ** ** **package** **8-Pin** ** ** **SOIC** **Top View**

## Pin Functions

# PIN

# I/O **DESCRIPTION** **NAME** **NO.**

| DRAIN | P | Drain pin |
|:--- |:--- |:--- |
| FB | I | Feedback terminal |
| GND | G | Ground |
| GND | G | Ground |
| HVIN | P | Supply pin |
| NC | N/C | Not internally connected |
| VDD | O | Supply pin, supply is provided by internal LDO | FB I Feedback terminal GND G Ground GND G Ground HVIN P Supply pin NC N/C Not internally connected

VDD O Supply pin, supply is provided by internal LDO

Copyright © 2015-2016, Texas Instruments Incorporated *Submit Documentation Feedback* Product Folder Links: * * *UCC28881*

# UCC28881

# SLUSC36B -NOVEMBER 2015-REVISED JANUARY 2016 **<https://www.ti.com**>

## Specifications

## 7.1 **Absolute Maximum Ratings**

over operating free-air temperature range (unless otherwise noted) (1) (2) (3)

# MIN **MAX** **UNIT**

# HVIN -0.3 700 (4) V DRAIN Internally 700 (4) V clamped

I DRAIN Positive drain current single pulse, pulse max duration 25 μ s 770 (5) mA I DRAIN Negative drain current mA

# FB -0.3 V

VDD VDD is supplied from low impedance source -0.3 V

I VDD VDD is supplied from high impedance source µA T J Junction temperature °C

Lead temperature 1.6 mm (1/16 inch) from case 10 seconds °C T stg Storage temperature range °C

(1) Stresses beyond those listed under * Absolute Maximum Ratings* may cause permanent damage to the device. These are stress ratings only, which do not imply functional operation of the device at these or any other conditions beyond those indicated under * * *Recommended* *Operating Conditions*. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability. (2) All voltages are with respect to GND. Currents are positive into, negative out of the specified terminal. These ratings apply over the operating ambient temperature ranges unless otherwise noted. (3) The device is not rated to withstand operating conditions when multiple parameters are at or near, absolute maximum ratings. (4) $$ TA = 25°C $$ (5) The MOSFET drain to source voltage is less than 400V

## 7.2 **ESD Ratings**

# UNIT

Human Body Model (HBM), per ANSI/ESDA/JEDEC JS-001, all pins \pm2000 V except HVIN pin (1)

V (ESD) Electrostatic discharge Human Body Model (HBM) per ANSI/ESDA/JEDEC JS-001, HVIN pin (1) \pm1500 V

Charged device model (CDM), per JEDEC specification JESD22-C101, \pm500 V all pins (2)

(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process. (2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.

*Submit Documentation Feedback* Copyright © 2015-2016, Texas Instruments Incorporated Product Folder Links: * * *UCC28881*

# UCC28881

# www.ti.com SLUSC36B -NOVEMBER 2015-REVISED JANUARY 2016

## 7.3

**Recommended Operating** ** ** **Conditions**

over operating free-air temperature range (unless otherwise noted)

# MIN **NOM** **MAX** **UNIT** V VDD Voltage On VDD pin V V FB Voltage on FB pin -0.2 V T J Operating junction temperature +125 °C

## 7.4 **Thermal** ** ** **Information**

# UCC28881

# THERMAL METRIC (1) **D** ** ** **(SOIC)** **UNIT**

# 7 PINS

R\thetaJA Junction-to-ambient thermal resistance 134.4 °C/W

R\thetaJC(top) Junction-to-case (top) thermal resistance 42.6 °C/W

R\thetaJB Junction-to-board thermal resistance °C/W

\psiJT Junction-to-top characterization parameter 6.4 °C/W

\psiJB Junction-to-board characterization parameter °C/W

(1) For more information about traditional and new thermal metrics, see the * Semiconductor* * * *and IC Package Thermal* * * *Metrics* application report, SPRA953.

Copyright © 2015-2016, Texas Instruments Incorporated *Submit Documentation Feedback* Product Folder Links: * * *UCC28881*

# UCC28881

# SLUSC36B -NOVEMBER 2015-REVISED JANUARY 2016 **<https://www.ti.com**>

## 7.5 **Electrical Characteristics**

VHVIN = 30 V, TA = TJ = -40°C to +125°C (unless otherwise noted)

# PARAMETER

**TEST** ** ** **CONDITIONS** **MIN** **TYP** **MAX** **UNIT** V HVIN(min) Minimum Voltage to start-up V

I NL Internal supply current, no load $$ FB = 1.25 V (> VFB_TH) $$ µA

Internal supply current, full I FL $$ FB = 0.75 V (> VFB_TH) $$ µA load

I CH0 Charging VDD Cap current VVDD = 0 V, -3.8 -1.6 -0.4 mA

I CH1 Charging VDD Cap current VVDD = 4.4V, VFB = 1.25 V -3.40 -1.30 -0.25 mA

Internally regulated low V VDD Voltage supply (supplied from 4.5 5.0 5.5 V HVIN pin)

V FB\_TH FB pin reference threshold 0.96 1.03 1.105 V

V VDD(on) VDD turn-on threshold VDD low-to-high 3.55 3.92 4.28 V

V VDD(off) VDD turn-off threshold VDD high-to-low 3.28 3.62 3.89 V

\DeltaVVDD(uvlo) VDD UVLO Hysteresis VDD high-to-low 0.27 0.345 0.39 V

D MAX Maximum Duty Cycle $$ FB = 0.75 V $$ 45% 55% Static, T A = -40°C mA I LIMIT Current Limit Static, T A = 25°C mA Static, TA = 125°C mA

Thermal Shutdown T J(stop) Internal junction temperature 138.5 °C Temperature

| TJ(hyst) | Thermal Shutdown Hysteresis | Internal junction temperature | 37. | °C |
|:--- |:--- |:--- |:--- |:--- |
| Power MOSFET Breakdown | BV | TJ = 25°C | V | Voltage |
| Power MOSFET On- | ID = 60 mA, TJ = 25°C | Ω | RDS(on) | Resistance (includes internal |

Power MOSFET Breakdown BV $$ TJ = 25°C $$ V Voltage

Power MOSFET On$$ ID = 60 mA, TJ = 25°C $$ \Omega R DS(on) Resistance (includes internal

$$ ID = 60 mA, TJ = 125°C $$ \Omega sense-resistor)

VDRAIN = 700V, TJ = 25°C µA Power MOSFET off state DRAIN\_I LEAKAGE leakage current $$ VDRAIN = 400 V, TJ = 125°C $$ µA

VHVIN = 700 V, TJ = 25°C, VVDD = 4.0 7.5 36.0 µA 5.8 V HVIN\_I OFF HVIN off state current

# VHVIN = 400 V, TJ = 125°C, VVDD = µA 5.8 V

V VDD(clamp) VDD clamp voltage $$ IVDD = 250 µA $$ 6.0 6.7 7.5 V

## 7.6 **Switching** ** ** **Characteristics**

over operating free-air temperature range (unless otherwise noted)

# MIN **TYP** **MAX** **UNIT** f SW(max) Maximum switching frequency kHz

| tON\_MAX | Maximum switch on time (current limiter not triggered), FB = 0.75 V | 6.5 | 8.3 | 9.7 | µs |
|:--- |:--- | ---: | ---: | ---: |:--- |
| tOFF\_MIN | Minimum switch off time follows every tON time, FB = 0.75 V | 6.5 | 8.3 | 9.7 | µs |
| tMIN | Minimum on time | 0.17 | 0.27 | 0.30 | µs |

t OFF\_MIN Minimum switch off time follows every t ON time, FB = 0.75 V 6.5 8.3 9.7 µs t MIN Minimum on time 0.17 0.27 0.30 µs

t OFF(ovl) Max off time (OL condition), t OFF(ovl) = t SW - t ON(max) µs

t ON\_TO Inductor current run away protection time threshold ns

*Submit Documentation Feedback* Copyright © 2015-2016, Texas Instruments Incorporated Product Folder Links: * * *UCC28881* Temperature ( o C)

V VDD(on) and Hysteresis (normalized to 25 o C) 0.98 0.985 0.99 0.995 1.005 1.01

# D305 V VDD(on) V VDD Hysteresis Drain to Source Voltage (V) Drain to Source Current (mA)

# D316

# I DRAIN 25 o C I DRAIN 125 o C Temperature ( o C) I FL and I NL (normalized to 25 o C) 0.85 0.9 0.95 1.05 1.1 1.15 1.2

# D303

# I FL I NL Temperature (°C) I CH0 and I CH1 (normalized to 25°C) 0.5 0.6 0.7 0.8 0.9 1.1 1.2 1.3 1.4 1.5

# D001

# I CH0 I CH1 Temperature ( o C) Current Limit (normalized to 25 o C) 0.8 0.85 0.9 0.95 1.05 1.1 1.15 1.2 D301 Drain Current Slope (mA/ P s) Current Limit (normalized to 50 mA/ P s) 0.4 0.5 0.6 0.7 0.8 0.9 1.1 1.2 1.3 1.4 1.5 1.6

# D002

# UCC28881

| www.ti.com | SLUSC36B -NOVEMBER 2015-REVISED JANUARY 2016 |
|:--- |:--- |
| 7.7 | Typical Characteristics |
| Figure 2. ILIMIT vs Drain Current Slope | Figure 1. ILIMIT vs Temperature |
| Figure 4. ICH0 and ICH1 vs Temperature | Figure 3. INL and IFL vs Temperature |
| Figure 6. IDS vs VDS at 25°C and 125°C | Figure 5. VVDD(on) and VVDD Hysteresis vs Temperature |
| Copyright © 2015-2016, Texas Instruments Incorporated | Submit Documentation Feedback |

## 7.7 **Typical Characteristics**

## Figure 2. I LIMIT vs Drain Current Slope

**Figure** ** ** **1. I** **LIMIT** ** vs** ** ** **Temperature**

## Figure 4. I CH0 and I CH1 vs Temperature

**Figure** ** ** **3. I** **NL** ** and** ** ** **I** **FL** ** vs** ** ** **Temperature**

## Figure 6. I DS vs V DS at 25°C and 125°C

**Figure** ** ** **5. V** **VDD(on)** ** and** ** ** **V** **VDD** ** Hysteresis** ** ** **vs** ** ** **Temperature**

Copyright © 2015-2016, Texas Instruments Incorporated *Submit Documentation Feedback*

## Product Folder Links: UCC28881 Copper Area (mm 2 )

# R T JA ( o C/W)

# D201 D001 Temperature ( o C)

DRAIN Breakdown Voltage (normalized to 25 o C) 0.9 0.92 0.94 0.96 0.98 1.02 1.04 1.06 1.08 1.1 1.12 D310 Temperature (°C) t ON(max) and t OFF(min) (normalized to 25°C) 0.99 0.995 1.005 1.01 1.015 1.02 1.025 1.03 1.035 1.04 1.045 1.05

# D001 T OFF(min) T ON(max) Temperature ( o C) Feedback Voltage (normalized to 25 o C) 0.96 0.97 0.98 0.99 1.01 1.02 D308 Temperature (°C) F SW(max) (normalized to 25°C) 0.96 0.97 0.98 0.99 1.01 1.02

# D012

# UCC28881

# SLUSC36B -NOVEMBER 2015-REVISED JANUARY 2016 **<https://www.ti.com**>

## Typical Characteristics (continued)

## Figure 7. Maximum Switching Frequency vs Temperature

**Figure** ** ** **8. V** **FB\_TH** ** vs** ** ** **Temperature**

## Figure 9. t ON(max) and t OFF(min) vs Temperature

**Figure** ** ** **10. DRAIN breakdown voltage vs** ** ** **Temperature**

## Figure 11. R TH J A vs Copper Area

*Submit Documentation Feedback* Copyright © 2015-2016, Texas Instruments Incorporated

## Product Folder Links: UCC28881

# LDO Control and Reference

# VDD

# VREF\_TH = 1 V

# DRAIN

# HVIN

# FB

# UVLO

+ PWM Controller and Output Short Circuit Protection

# LEB

| Leading Edge | Blanking Time |
|:--- |:--- |
| S | Q |
| Q | R |
| Current | Limit |

# S Q

# Q R Current Limit 1, 2

# GND Gate High Voltage Current Source Thermal Shutdown

# UCC28881

# www.ti.com SLUSC36B -NOVEMBER 2015-REVISED JANUARY 2016

## Detailed Description **8.1** **Overview**

The UCC28881 integrates a controller and a 700-V power MOSFET into one monolithic device. The device also integrates a high-voltage current source, enabling start up and operation directly from the rectified mains voltage. UCC28881 is the same family device as UCC28880 and it provides higher power handling capability.

The low-quiescent current of the device enables excellent efficiency. The device is suitable for non-isolated ACto-DC low-side buck and buck-boost configurations with level-shifted direct feedback, but also more traditional high-side buck, buck boost and low-power flyback converters with low standby power can be built using a minimum number of external components.

The device generates its own internal low-voltage supply (5 V referenced to the device's ground, GND) from the integrated high-voltage current source. The PWM signal generation is based on a maximum constant on-time, minimum off-time concept, with the triggering of the on-pulse depending on the feedback voltage level. Each onpulse is followed by a minimum off-time to ensure that the power MOSFET is not continuously driven in an onstate. The PWM signal is AND-gated with the signal from a current limit circuit. No internal clock is required, as the switching of the power MOSFET is load dependent. A special protection mechanism is included to avoid runaway of the inductor current when the converter operates with the output shorted or in other abnormal conditions that can lead to an uncontrolled increase of the inductor current. This special protection feature keeps the MOSFET current at a safe operating level. The device is also protected from other fault conditions with thermal shutdown, under-voltage lockout and soft-start features.

**8.2** **Functional** ** ** **Block Diagram**

Copyright © 2015-2016, Texas Instruments Incorporated *Submit Documentation Feedback* Product Folder Links: * * *UCC28881*

# UCC28881

# SLUSC36B -NOVEMBER 2015-REVISED JANUARY 2016 **<https://www.ti.com**> **8.3** **Feature** ** ** **Description**

The UCC28881 integrates a 700-V rated power MOSFET switch, a PWM controller, a high-voltage current source to supply a low-voltage power supply regulator. A bias and reference block, thermal shutdown and the following protection features, current limiter, under voltage lockout (UVLO) and overload protection for situations like short circuit at the output are also integrated inside UCC28881. UCC28881 is the same family device as UCC28880 and it provides higher power handling capability.

The positive high-voltage input of the converter node (VIN+) functions as a system reference ground for the output voltage in low-side topologies. In the low-side buck topology the output voltage is negative with respect to the positive high-voltage input (VIN+), and in low-side buck-boost topology the output voltage is positive with respect to the positive high-voltage input (VIN+).

In low-side buck and buck-boost topologies, the external level-shifted direct feedback circuit can be implemented by two resistors and a high-voltage PNP transistor.

In high-side buck configuration, as well as in non-isolated flyback configuration, the output voltage is positive with respect to the negative high-voltage input (VIN-), which is the system reference ground.

UCC28881 can operate under continuous conduction mode (CCM) or discontinuous conduction mode (DCM) mode. CCM operation allows the converter to deliver more output power because of less current ripple. However, it requires a higher inductor value and generally results in lower efficiency due to the added losses associated with diode reverse recovery current. DCM mode operation uses a smaller inductor and achieves better efficiency, but the output current handling capability is reduced because of increased current ripple. The table below shows the current handling capability in DCM and CCM operation for the UCC28880, UCC28881 family.

**Table 1. Current Handling Capability** ** ** **for** ** UCC28880** ** ** **and UCC28881**

**DEVICE** **CURRENT** ** ** **HANDLING MODE** 230 VAC \pm15% **85** ** ** **V** ** ** **~ 265 V** **AC** UCC28881 Discontinuous Conduction Mode (DCM) 150 mA 150 mA

| UCC28881 | Continuous Conduction Mode (CCM) | 225 mA | 225 mA |
|:--- |:--- |:--- |:--- |
| UCC28880 | Discontinuous Conduction Mode (DCM) | 70 mA | 70 mA |
| UCC28880 | Continuous Conduction Mode (CCM) | 100 mA | 100 mA |
| When the bus voltage is higher than 400 V, it is recommended to limit operation to DCM mode only to avoid the | diode reverse recovery current and the associated internal MOSFET stress. Due to the higher switching loss and | device stresses at higher bus voltage, it is recommended to keep the converter input voltage less than 560 V for | the buck applications. |

UCC28880 Discontinuous Conduction Mode (DCM) 70 mA 70 mA

UCC28880 Continuous Conduction Mode (CCM) 100 mA 100 mA

When the bus voltage is higher than 400 V, it is recommended to limit operation to DCM mode only to avoid the diode reverse recovery current and the associated internal MOSFET stress. Due to the higher switching loss and device stresses at higher bus voltage, it is recommended to keep the converter input voltage less than 560 V for the buck applications.

UCC28881 power handling capability is reduced at higher ambient temperature, as a function of the power dissipation of the device, the device's recommended maximum operating junction temperature and the thermal dissipation capability of the total system. De-rating of the output current according to maximum ambient temperature can be estimated from Figure 12. The de-rating estimation assumes CCM operation, 10 µJ of switching loss and 135°C/W R θ JA and 30-kHz, full-load switching frequency. This is a conservative estimation. The thermal handling capability can be more accurately determined through experimental measurement. For more information on thermal evaluation methods see the IC Package and Thermal Metrics application report: SPRA953.

*Submit Documentation Feedback* Copyright © 2015-2016, Texas Instruments Incorporated Product Folder Links: * * *UCC28881* Ambient Temperature ( o C) Output Current Derating Factor 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.1 1.2

# D012

# UCC28881

# www.ti.com SLUSC36B -NOVEMBER 2015-REVISED JANUARY 2016

**Figure 12.** ** ** **Output Current (De-Rating** ** ** **Factor) vs. Temperature**

It is required to use fast recovery diode for the buck freewheeling diode. When designed in CCM, the diode reverse recovery time should be less than 35 ns to keep low reverse recovery current and the switching loss. For example, STTH1R06A provides 25-ns reverse recovery time. When designed in DCM, a slower diode can be used, but the reverse-recovery time should be kept less than 75 ns. MURS160 can fit the requirement.

The device has a low-standby power consumption (no-load condition), only 18 mW (typical) when connected to a 230-V AC mains and 9 mW when connected to an 115-V AC mains.

The standby power does not include the power dissipated in the external feedback path, the power dissipated in the external pre-load, the inductor in the freewheeling diode and the converter input stage (rectifiers and filter).

Copyright © 2015-2016, Texas Instruments Incorporated *Submit Documentation Feedback* Product Folder Links: * * *UCC28881*

# UCC28881

| SLUSC36B -NOVEMBER 2015-REVISED JANUARY 2016 | www.ti.com |
|:--- |:--- |
| 8.4 | Device Functional Modes |
| 8.4.1 | Start-Up Operation | **8.4** **Device Functional** ** ** **Modes** **8.4.1** **Start-Up Operation**

The device includes a high-voltage current source connected between the HVIN pin and the internal supply for the regulator. When the voltage on the HVIN pin rises, the current source is activated and starts to supply current to the internal 5-V regulator. The 5-V regulator charges the external capacitor connected between VDD pin and GND pin. When the VDD voltage exceeds the VDD turn-on threshold, V VDD(on), device starts operations. The minimum voltage across HVIN and GND pins, to ensure enough current to charge the capacitance on VDD pin, is V HVIN(min). At the First switching cycle the minimum MOSFET off time is set to be \>100 μ s and cycle-by-cycle is progressively reduced up to t OFF(min) providing soft start.

**8.4.2** **Feedback and Voltage Control Loop**

The feedback circuit consists of a voltage comparator with the positive input connected to an internal reference voltage (referenced to GND) and the negative input connected to FB pin. When the feedback voltage at the FB pin is below the reference voltage V FB\_TH logic high is generated at the comparator output. This logic high triggers the PWM controller, which generates the PWM signal turning on the MOSFET. When the feedback voltage at the FB pin is above the reference voltage, it indicates that the output voltage of the converter is above the targeted output voltage set by the external feedback circuitry and PWM is stopped.

*Submit Documentation Feedback* Copyright © 2015-2016, Texas Instruments Incorporated Product Folder Links: * * *UCC28881*

# FB\_COMP\_OUT

# PWM

# CURRENT LIMIT

# GATE

# RSTN *t* *t* *t* *t* *t* *t*

# FB\_TH FB

ON(max) OFF(min) ON(max) OFF(min) ON(max) OFF(min) ON(max) OFF(min)

# UCC28881

# www.ti.com SLUSC36B -NOVEMBER 2015-REVISED JANUARY 2016

**Device Functional** ** ** **Modes** ** ** **(continued)** **8.4.3** **PWM Controller**

UCC28881 operates under on/off control. When the FB pin voltage is below internal reference 1 V, the converter is switching and sending power to the load. When the FB pin voltage is above internal reference 1 V, the converter shuts off and stops delivering power to the load.

The PWM controller does not need a clock signal. The PWM signal's frequency is set to f SW(max) = (1/(t ON(max) + t OFF(min) )) which occurs when the voltage on the FB pin is continuously below V FB\_TH.

PWM duty cycle is determined by both the peak current and maximum on time. At each switching cycle, after turn on, the MOSFET is turned off if its current reaches the fixed peak-current threshold or its on time reaches the maximum value of on-time pulse t ON(max).

Normally the converter would operate under frequency control, which means the converter is only enabled one switching cycle and then disabled. Next switching cycle starts when output voltage decays and the feedback enable the converter again. This way, the converter appears to operate under variable switching frequency control.

The user might observe the converter operates in burst mode that converter is enabled for multiple switching cycles and then stopped for multiple switching cycles. This causes larger output voltage ripple. However, due to the infrequent switching it actually helps on the standby power at no load.

**Figure 13.** ** ** **UCC28881 Timing Diagram**

Copyright © 2015-2016, Texas Instruments Incorporated *Submit Documentation Feedback* Product Folder Links: * * *UCC28881*

# PWM Gate Current Limit Increase t OFF ( Decrease f SW )

# LIMIT Drain Current

# CNT\_IN

# ON\_MAX OFF

# LEB ~200 ns Decrease t OFF (Increase f SW )

# ON\_TO

# ON\_TO ON\_TO Inductor Current ***t*** ***t*** ***t*** ***t*** ***t*** ***t*** ***t*** ~200 ns

# ON ON

# UCC28881

# SLUSC36B -NOVEMBER 2015-REVISED JANUARY 2016 **<https://www.ti.com**>

**Device Functional** ** ** **Modes** ** ** **(continued)** **8.4.4** **Current Limit**

The current limit circuit senses the current through the power MOSFET. The sensing circuit is located between the source of the power MOSFET and the GND pin. When the current in the power MOSFET exceeds the threshold I LIMIT, the internal current limit signal goes high, which sets the internal RSTN signal low. This disables the power MOSFET by driving its gate low. The current limit signal is set back low after the falling edge of the PWM signal. After the rising edge of the GATE signal, there is a blanking time. During this blanking time, the current limit signal cannot go high. This blanking time and the internal propagation delay result in minimum on time, t MIN.

**8.4.5** **Inductor** ** ** **Current Runaway Protection**

To protect the device from overload conditions, including a short circuit at the output, the PWM controller incorporates a protection feature which prevents the inductor current from runaway. When the output is shorted the inductor demagnetization is very slow, with low di/dt, and when the next switching cycle starts energy stored in the inductance is still high. After the MOSFET switches on, the current starts to rise from pre-existing DC value and reaches the current-limit value in a short duration of time. Because of the intrinsic minimum on-time of the device the MOSFET on-time cannot be lower than t MIN, in an overload or output short circuit the energy inductance is not discharged sufficiently during MOSFET off-time, it is possible to lose control of the current leading to a runaway of the inductor current. To avoid this, if the on-time is less than t ON\_TO (t ON\_TO is a device internal time out), the controller increases the MOSFET off-time (t OFF ). If the MOSFET on-time is longer than t ON\_TO then t OFF is decreased. The controller increases t OFF, cycle-by-cycle, through discrete steps until the ontime continues to stay below t ON\_TO. The t OFF is increased up to t OFF(ovl) after that, if the on-time is still below t ON\_TO the off-time is kept equal to t OFF(ovl). The controller decreases t OFF cycle-by-cycle until the on-time continues to stay above t ON\_TO up to t OFF(min). This mechanism prevents control loss of the inductor current and prevents over stress of the MOSFET (see typical waveforms in Figure 14 and Figure 15 ). At start up, the t OFF is set to t OFF(ovl) and reduced cycle-by-cycle (if the on-time is longer than t ON\_TO ) up to t OFF(min) providing a soft start for the power stage.

**Figure 14.** ** ** **Current Runaway Protection Logic Timing Diagram**

*Submit Documentation Feedback* Copyright © 2015-2016, Texas Instruments Incorporated Product Folder Links: * * *UCC28881*

# IN max ON\_ TO LIMIT V L t I! u

# INDUCTOR CURRENT

# DRAIN CURRENT ***t***

# t GATE ***t*** Output Shorted Here

# ON\_TO ON \< t ON\_TO

# ON\_TO ON \> t ON\_TO ON \< t ON\_TO

# ON\_TO ON\_TO ON \< t ON\_TO

# ON\_TO

# LIMIT

# FB\_TH FB

# UCC28881

# www.ti.com SLUSC36B -NOVEMBER 2015-REVISED JANUARY 2016

**Device Functional** ** ** **Modes** ** ** **(continued)**

**Figure 15.** ** ** **Current Runaway Protection,** ** ** **Inductor and MOSFET Current**

A minimal value needs to be imposed on the inductance value to avoid nuisance tripping of the protection feature that prevents the loss of control of the inductor current. Inadvertent operation of the protection feature limits the output-power capability of the converter. This condition depends on the converter's maximum input operating voltage and temperature. Use Equation 1 to calculate your minimum inductance value. (1)

In this equation, V IN(max) is the maximum voltage on the DC input. If the input is a rectifed AC voltage, it should be the peak value of the maximum AC line. For a DC input case, it should be the maximum DC input voltage.

If the inductance value is too low, such that the MOSFET on-time is always less than t ON\_TO timeout and the device progressively increases the MOSFET off-time up to t OFF(ovl), the output power is reduced and the converter fails to supply the load.

**8.4.6** **Over** ** ** **Temperature Protection**

If the junction temperature rises above T J(stop), the over temperature protection is triggered. This disables the power MOSFET switching. To re-enable the switching of the MOSFET the junction temperature has to fall by T J(hyst) below the T J(stop) where the device moves out of over temperature protection.

Copyright © 2015-2016, Texas Instruments Incorporated *Submit Documentation Feedback* Product Folder Links: * * *UCC28881*

# HVIN

# VDD

# FB

# DRAIN

# GND

# UCC28881

# VIN +

# FB2

# FB1

# FB

# L

# D4

# D1 VOUT +

# L

# F

# C2

# VDD

# L2 D2

# D3

# L1

# UCC28881

# SLUSC36B -NOVEMBER 2015-REVISED JANUARY 2016 **<https://www.ti.com**>

## Application and Implementation

**NOTE** Information in the following applications sections is not part of the TI component specification, and TI does not warrant its accuracy or completeness. TI's customers are responsible for determining suitability of components for their purposes. Customers should validate and test their design implementation to confirm system functionality. **9.1** **Application** ** ** **Information**

The UCC28881 can be used in various application topologies with direct or isolated feedback. The device can be used in low-side buck, where the output voltage is negative, or as a low-side buck-boost configuration, where the output voltage is positive. In both configurations the common reference node is the positive input node (VIN+). The device can also be configured as a LED driver in either of the above mentioned configurations. If the application requires the AC-to-DC power supply output to be referenced to the negative input node (VIN-), the UCC28881 can also be configured as a traditional high-side buck as shown in Figure 16. In this configuration, the voltage feedback is sampling the output voltage VOUT, making the DC regulation less accurate and load dependent than in low-side buck configuration, where the feedback is always tracking the VOUT. However, highconversion efficiency can still be obtained. **9.2** **Typical Application**

**9.2.1** **13-V, 225-mA High-Side Buck Converter**

Figure 16 shows a typical application example of a non-isolated power supply, where the UCC28881 is connected in a high-side buck configuration having an output voltage that is positive with respect to the negative high-voltage input (VIN-). The output voltage is set to 13 V in this example, but can easily be changed by changing the value of R FB1. This application can be used for a wide variety of household appliances and automation, or any other applications where mains isolation is not required.

**Figure 16.** ** ** **Universal Input,** ** ** **12-V,** ** ** **225-mA Output** ** ** **High-Side** ** ** **Buck**

*Submit Documentation Feedback* Copyright © 2015-2016, Texas Instruments Incorporated Product Folder Links: * * *UCC28881* BULK min IN LINE min IN min BULK min IN min BULK min V P arccos f RCT V C V V

ª º § - · u « » ¨ ¸ u  u « » ¨ ¸ u S u « » © ¹ ¬ ¼ u 

# UCC28881

# www.ti.com SLUSC36B -NOVEMBER 2015-REVISED JANUARY 2016

## Typical Application (continued)

***9.2.1.1*** ***Design*** *** *** ***Requirements*** **Table 2. Design Specification**

# DESCRIPTION **MIN** **TYP** **MAX** **UNIT**

# DESIGN INPUT

V IN AC input voltage V RMS f LINE Line frequency Hz I OUT Output current mA

# DESIGN REQUIREMENTS P NL No-load input power mW V OUT Output voltage 12.5 17.5 V Δ V OUT Output voltage ripple mV \eta Converter full-load efficiency 70% ***9.2.1.2*** ***Detailed Design Procedure***

**9.2.1.2.1** **Input** ** ** **Stage** ** ** **(R** **F** **, D2, D3, C1, C2, L2)** - • Resistor R F is a flame-proof fusible resistor. R F limits the inrush current, and also provide protection in case any component failure causes a short circuit. Value for its resistance is generally selected between 4.7 Ω to 15 \Omega. - • A half-wave rectifier is chosen and implemented by diode D2 (1N4937). It is a general purpose 1-A, 600-V rated diode. It has a fast reverse recovery time (200 ns) for improved differential-mode-conducted EMI noise performance. Diode D3 (1N4007) is a general purpose 1-A, 1-kV rated diode with standard reverse recovery time (\>500 ns), and is added for improved common-mode-conducted EMI noise performance. D3 can be removed and replaced by a short if not needed. - • EMI filtering is implemented by using a single differential-stage filter (C1-L2-C2).

Capacitors C1 and C2 in the EMI filter also acts as storage capacitors for the high-voltage input DC voltage (VIN). The required input capacitor size can be calculated according Equation 2. where

- • C BULK(min) is minimum value for the total input capacitor value (C1 + C2 in the schematic of Figure 16 ). - • RCT = 1 in case of half wave rectifier and RCT = 2 in case of full-wave rectifier. - • P IN is the converter input power. - • V IN(min) is the minimum RMS value of the AC input voltage. - • V BULK(min) is the minimum allowed voltage value across bulk capacitor during converter operation. - • f LINE(min) is the minimum line frequency when the line voltage is V IN(min).

The converter input power can be easily calculated as follow:

- • The converter maximum output power is: P OUT = I OUT x V OUT = 0.225 A x 13 V = 2.925 W - • Assuming the efficiency η = 68% the input power is P IN = P OUT / η = 4.178 W

Using the following values for the other parameters

•• VBULK(min) = 80 V - • V IN(min) = 85 V RMS (from design specification table) •• fLINE(min) = 57 Hz (2)

Copyright © 2015-2016, Texas Instruments Incorporated *Submit Documentation Feedback* Product Folder Links: * * *UCC28881*

# OUT ESR LIMIT

# V R 0.8 I ':

# LIMIT OUT L OUT SW max

I I 440mA 225mA C 200 F f V 62kHz 350mV  ! u u P u ' u

## D1(max) IN(max) V 2 V 2 265V 375V u u BULK(min) BULKn(min) CBULK

# C C 19.5 F 1 TOL! P 

# UCC28881

# SLUSC36B -NOVEMBER 2015-REVISED JANUARY 2016 **<https://www.ti.com**>

C BULK(min) = 15.6 μ F. Considering that electrolytic capacitors, generally used as bulk capacitor, have 20% of tolerance in value, the minimum nominal value required for C BULK is: (3)

Select C1 and C2 to be 10 \muF each (CBULK = 10 \muF + 10 \muF = 20 \muF > CBULKn(min)).

By using a full-wave rectifier allows a smaller capacitor for C1 and C2, almost 50% smaller.

**9.2.1.2.2** **Regulator** ** ** **Capacitor (C** **VDD** **)**

Capacitor C VDD acts as the decoupling capacitor and storage capacitor for the internal regulator. A 100-nF, 10-V rated ceramic capacitor is enough for proper operation of the device's internal LDO.

**9.2.1.2.3** **Freewheeling** ** ** **Diode** ** ** **(D1)**

The freewheeling diode has to be rated for high-voltage with as short as possible reverse-recovery time (t rr ).

The maximum reverse voltage that the diode should experience in the application, during normal operation, is given by Equation 4. (4) A margin of 20% is generally considered.

The use of a fast recovery diode is required for the buck-freewheeling rectifier. When designed in CCM, the diode reverse recovery time should be less than 35 ns to keep low reverse recovery current and the switching loss. For example, STTH1R06A provides 25-ns reverse recovery time. When designed in DCM, slower diode can be used, but the reverse recovery time should be kept less than 75 ns. MURS160 can fit the requirement.

**9.2.1.2.4** **Output** ** ** **Capacitor (C** **L** **)**

The value of the output capacitor impacts the output ripple. Depending on the combination of capacitor value and equivalent series resistor (R ESR ). A larger capacitor value also has an impact on the start-up time. For a typical application, the capacitor value can start from 47 μ F, to hundreds of μ F. A guide for sizing the capacitor value can be calculated by the following equations: (5) (6)

Take into account that both C L and R ESR contribute to output voltage ripple. A first pass capacitance value can be selected and the contribution of C L and R ESR to the output voltage ripple can be evaluated. If the total ripple is too high the capacitance value has to increase or R ESR value must be reduced. In the application example C L was selected (330 µF) and it has an R ESR of 0.03 Ω. So the R ESR contributes for 4% of the total ripple. The formula that calculates C L is based on the assumption that the converter operates in burst of twenty switching cycles. The number of bursts per cycle could be different, the formula for C L is a first approximation.

**9.2.1.2.5** **Pre-Load Resistor (R** **L** **)**

The pre-load resistor connected at the output is required for the high-side buck topology. Unlike low side buck topology, the output voltage is directly sensed, in high-side buck topology the output is sampled and estimated. At no-load condition, because the feedback loop runs with its own time constant, the buck converter operates with a fixed minimum switching frequency. Select the pre-load resistor or using a zener diode to prevent output voltage goes too high at no-load condition.

A simple zener diode would be a good choice without going through the calculation. Besides the simplifying the calculation, zener diode doesn't consumes power at heavy load condition, which helps to improve the converter heavy-load efficiency.

*Submit Documentation Feedback* Copyright © 2015-2016, Texas Instruments Incorporated Product Folder Links: * * *UCC28881*

# IN max ON\_ TO LIMIT V 375V L t 450ns 536 H I 315mA! u u # P

# OUT d L SW \_ VIN max

# V V L 1mH I F ! ' u

# MIN SW \_ VIN(max) SW(max) ON\_ TO D F 80kHz f 62kHz t! OUT d MIN IN(max) d

# V V D 3.61% V V  

# MIN SW \_ VIN(max) ON\_ TO D F t

# OUT OUT d MIN LIMIT IN(max) d

# I V V D I V V  u  OUT d MIN IN(max) d

# V V D V V  

# L LIMIT OUT I I I ' u 

# MAX MAX REG FB FB1 FB2 L MAX REG LIMIT

# V V V C R R R V V L I u u  u  u  u

# UCC28881

# www.ti.com SLUSC36B -NOVEMBER 2015-REVISED JANUARY 2016

A simple resistor can also be used to limit the output voltage at no load condition. However, this resistor connects to the output all the time and it reduces the full-load efficiency. The pre-load resistor can be calculated based on below equation or based on experiments. In this equation, the V MAX is allowed maximum output voltage, and V REG is the regulated output voltage. (7) **9.2.1.2.6** **Inductor (L1)** Initial calculations:

Half of the peak-to-peak ripple current at full load: (8)

When operating in DCM, the peak-to-peak current ripple is the peak current of the device.

Average MOSFET conduction minimum duty cycle at continuous conduction mode is: (9)

If the converter operates in discontinuous conduction mode: (10)

Maximum allowed switching frequency at V IN(max) and full load: (11)

Switching frequency has a maximum value limit of f SW(max).

The worst case I LIMIT = 315 mA, but assuming Δ I L = 180 mA.

The converter works in continuous conduction mode ( Δ I L \< I LIMIT ) so based on V OUT = 13 V, V d = 0.5 V and $$ VIN(max) = 375 V $$ (12)

The maximum allowed switching frequency is 62 kHz because the calculated value exceeds it. (13)

The duty cycle does not force the MOSFET on time to go below t ON\_TO. If D MIN /T ON\_TO \< f SW(max), the switching frequency is reduced by current runaway protection and the maximum average switching frequency is lower than f SW(max), the converter can't support full load.

The minimum inductance value satisfies both the following conditions: (14) (15)

In the application example, 1 mH is selected as the minimum standard value that satisfy Equation 14 and Equation 15.

Copyright © 2015-2016, Texas Instruments Incorporated *Submit Documentation Feedback* Product Folder Links: * * *UCC28881*

# FB FB FB1 FB2 L LOAD C R R 0.1 C R W u  u u

# OUT(T) d4 d1 FB \_ TH OUT(T) FB \_ TH FB1

# FB2 FB \_ TH FB \_ TH

# V V V V V V R R V V     #

# UCC28881

# SLUSC36B -NOVEMBER 2015-REVISED JANUARY 2016 **<https://www.ti.com**>

**9.2.1.2.7** **Feedback** ** ** **Path (C** **FB** **, R** **FB1** ** and R** **FB2** **)** ** ** **and Load Resistor (R** **L** **)**

In low-side buck converter the output voltage is always sensed by the FB pin and UCC28881 internal controller can turn on the MOSFET on VOUT. In high-side buck converter applications the information on the output voltage value is stored on C FB capacitor. This information is not updated in real time. The information on C FB capacitor is updated just after MOSFET turn-off event. When the MOSFET is turned off, the inductor current forces the freewheeling diode (D1 in Figure 16 ) to turn on and the GND pin of UCC28881 goes negative at -V d1 (where V d1 is the forward drop voltage of diode D1) with respect to the negative terminal of bulk capacitor (C1 in Figure 16 ). When D1 is on, through diode D4, the C FB capacitor is charged at V OUT - V d4 + V d1. Set the output voltage regulation level using Equation 16. where

- • V FB\_TH is the FB pin reference voltage. - • V OUT\_T is the target output voltage. - • R FB1, R FB2 is the resistance of the resistor divider connected with FB pin (see Figure 16 ) - • The capacitor C FB after D1 is discharged with a time constant that is τ FB = C FB x (R FB1 + R FB2 ). - • Select the time constant τ FB, given in Equation 17 (16) (17)

In this equation, R LOAD is the full load resistor value.

The time constant selection leads to a slight output-voltage increase in no-load or light-load conditions. In order to reduce the output-voltage increase, increase τ FB. The drawback of increasing τ FB is t in high-load conditions V OUT could drop.

Because of the nature of sample and hold of output voltage feedback, the feedback loop components need some adjustment after the initial design. The larger time constant of the feedback components leads to lower no-load switching frequency. As the results, the no-load standby power and light-load voltage regulation are improved. Because of larger time constant, at heavier load, the load regulation start to get worse. On the contrast, decreasing the time constant makes the heavy load regulation better but increases the no-load standby power and makes the light-load voltage regulation worse. Some tradeoff is required to make the regulation and standby power. Below table summarizes the relationship between the feedback loop time constant and the load regulation. This can be used for an easy guideline for fine tuning the circuit performance.

**Table 3. Feedback Loop Time Constant Adjustment**

# FEEDBACK LOOP TIME

**HEAVY-LOAD** ** ** **OUTPUT** **NO-LOAD REGULATION** **STANDBY POWER** **CONSTANT** ** ** **(** **τ** **FB** **)** **VOLTAGE RIPPLE** Increase Better Worse Better Decrease Worse Better Worse

*Submit Documentation Feedback* Copyright © 2015-2016, Texas Instruments Incorporated Product Folder Links: * * *UCC28881* Output Current (A) Output Voltage (V) 0.05 0.1 0.15 0.2 0.25

# D001

# 115V AC 230V AC Output Power (W) Efficiency (%) 0.3 0.6 0.9 1.2 1.5 1.8 2.1 2.4 2.7

# D001

# 115V AC 230V AC

# UCC28881

# www.ti.com SLUSC36B -NOVEMBER 2015-REVISED JANUARY 2016

## 9.2.1.3 ***Application Curves***

## Figure 17 shows the output voltage vs output current. Different curves correspond to different converter AC input

voltages. Figure 18 shows efficiency changes vs output power. Different curves correspond to different converter AC input voltages.

**Figure** ** ** **17. Output IV Characteristic** **Figure** ** ** **18. Efficiency vs** ** ** **P** **OUT**

## Table 4. Converter Efficiency

# V IN\_AC (V RMS )

**LOAD** ** ** **(mA)** **EFFICIENCY (%)** **AVERAGE** ** ** **EFFICIENCY (%)** 80.8

## Table 5. Key Component List for 13-V 225-mA High-Side Buck Converter

| DES | DESCRIPTION | PART NUMBER | MANUFACTURER(1) |
|:--- |:--- |:--- |:--- |
| C1, C2 | Bulk capacitor, 10 μF, 450 V | EEUED2W100 | Panasonic |
| CFB | Feedback capacitor, ceramic, 0.015 μF, 50 V | C0805C153K5RACTU | Kemet |
| CL | Output capacitor, 330 μF, 35 V | EEU-FM1V331L | Panasonic |
| D1 | Buck freewheeling diode, ultrafast, 600 V, 1 A | STTH1R06A | ST Microelectronics |

C1, C2 Bulk capacitor, 10 \muF, 450 V EEUED2W100 Panasonic

C FB Feedback capacitor, ceramic, 0.015 μ F, 50 V C0805C153K5RACTU Kemet

C L Output capacitor, 330 μ F, 35 V EEU-FM1V331L Panasonic

D1 Buck freewheeling diode, ultrafast, 600 V, 1 A STTH1R06A ST Microelectronics

D2, D3 Rectifier diodes, standard recovery rectifier, 1000 1N4007 Fairchild semiconductor V, 1 A

D4 Feedback diode, standard recovery rectifier, 600 V, 1N4006-T Diodes Inc. 1 A

L1 Buck inductor, 1 mH, 0.4 A, Wurth Elektronik

| L2 | Filter inductor, 1 mH, 0.2 A | 5800-102-RC | Bourns |
|:--- |:--- |:--- |:--- |
| RFB1 | Upper feedback resistor 121 kΩ, 1% | ERJ-6ENF1213V | Panasonic |
| RFB2 | Lower feedback resistor, 10.0 kΩ, 1% | ERJ-6ENF1002V | Panasonic |

R FB1 Upper feedback resistor 121 k Ω, 1% ERJ-6ENF1213V Panasonic

R FB2 Lower feedback resistor, 10.0 k Ω, 1% ERJ-6ENF1002V Panasonic

(1) See * Third-Party* * * *Products Discalimer*

Copyright © 2015-2016, Texas Instruments Incorporated *Submit Documentation Feedback* Product Folder Links: * * *UCC28881*

# HVIN

# VDD

# FB

# DRAIN

# GND

# UCC28881

# L1

# L

# D1

# RSENSE

# C1

# R1

# R2

# Q2

# Q1 Current Feedback

# RFB1

# RFB1

# VOUT

# VIN +

# HVIN

# VDD

# FB

# DRAIN

# GND

# UCC28881

# L1

# FB2

# FB1

# L

# VIN

# VOUT

# D1

# Q1 + +

# UCC28881

# SLUSC36B -NOVEMBER 2015-REVISED JANUARY 2016 **<https://www.ti.com**>

## 9.2.2

**Additional UCC28881 Application Topologies**

## 9.2.2.1

***Low-Side*** *** *** ***Buck and LED Driver -*** *** *** ***Direct*** *** *** ***Feedback (Level*** *** *** ***Shifted)***

## Features include

- • Output Referenced to Input - • Negative Output (V OUT ) with Respect to VIN+ - • Step Down: V OUT \< V IN - • Direct Level-Shifted Feedback

## Figure 19. Low-Side Buck, Direct Feedback (Level Shifted)

## Figure 20. Low-Side Buck LED Driver, Direct Feedback (Level Shifted)

*Submit Documentation Feedback* Copyright © 2015-2016, Texas Instruments Incorporated Product Folder Links: * * *UCC28881*

# HVIN

# VDD

# FB

# DRAIN

# GND

# UCC28881

# VIN +

# FB2

# D1

# L1

# VOUT +

# L

# HVIN

# VDD

# FB

# DRAIN

# GND

# UCC28881

# VIN +

# FB2

# FB

# L

# D2

# D1

# L1

# VOUT +

# UCC28881

# www.ti.com SLUSC36B -NOVEMBER 2015-REVISED JANUARY 2016

## 9.2.2.2 ***High-Side Buck Converter***

## Features include

- • Output Referenced to Input - • Positive Output (V OUT ) with Respect to VIN- - • Step Down (V OUT \< V IN )

## Figure 21. High-Side Buck Converter Schematic

## 9.2.2.3

***Non-Isolated, Low-Side Buck-Boost Converter***

## Features Include

- • Output Referenced to Input - • Positive Output (V OUT ) with Respect to VIN+ - • Step Up, Step Down: V OUT \> V IN or V OUT \< V IN - • Direct Level-Shifted Feedback

## Figure 22. Low-Side Buck-Boost Converter

Copyright © 2015-2016, Texas Instruments Incorporated *Submit Documentation Feedback* Product Folder Links: * * *UCC28881*

# HVIN

# VDD

# FB

# DRAIN

# GND

# UCC28881

# FB2

# FB1

# VDD

# L

# VIN +

# VOUT +

# HVIN

# VDD

# FB

# DRAIN

# GND

# UCC28881

# VIN +

# FB2

# FB1

# FB

# L

# D2

# D1 L1 VOUT +

# UCC28881

# SLUSC36B -NOVEMBER 2015-REVISED JANUARY 2016 **<https://www.ti.com**>

## 9.2.2.4

***Non-Isolated, High-Side Buck-Boost Converter***

## Features include

- • Output Referenced to Input - • Positive Output (V OUT ) with Respect to VIN- - • Step Up, Step Down: V OUT \> V IN or V OUT \< V IN

## Figure 23. High-Side Buck-Boost Converter

## 9.2.2.5 ***Non-Isolated Flyback Converter***

## Features include

- • Output Referenced to Input - • Positive Output (V OUT ) with Respect VIN- - • Direct Feedback - • Higher Output Current Capability, 4.5 W for 85 V AC ~ 265 V AC Input and 6 W for 176 V AC ~ 265 V AC Input

## Figure 24. Non-Isolated Flyback Configuration

*Submit Documentation Feedback* Copyright © 2015-2016, Texas Instruments Incorporated Product Folder Links: * * *UCC28881*

# HVIN

# VDD

# FB

# DRAIN

# GND

# UCC28881

# FB

# VDD

# L

# VIN +

# VOUT +

# UCC28881

# www.ti.com SLUSC36B -NOVEMBER 2015-REVISED JANUARY 2016

## 9.2.2.6

***Isolated*** *** *** ***Flyback Converter***

## Features include

- • Output Isolated from Input - • Direct Feedback - • Higher Output Current Capability, 4.5 W for 85 V AC ~ 265 V AC Input and 6 W for 176 V AC ~ 265V AC Input

## Figure 25. Isolated Flyback Converter

Copyright © 2015-2016, Texas Instruments Incorporated *Submit Documentation Feedback* Product Folder Links: * * *UCC28881* xxx xx xx xxx

# GND\_IC

# FB

# VDD

# DRAIN

# NC

# HVIN

# AC INPUT

# DC OUTPUT

# GND\_IC

# L2

# C1 C2 Rf D2

# D3 Rfb2 Q1 xx xx 60 mils

# L1 D1 = top layer = bottom layer = connect top and bot Rfb1

# RL

# CL xxxx

# UCC28881

# SLUSC36B -NOVEMBER 2015-REVISED JANUARY 2016 **<https://www.ti.com**>

## Power Supply Recommendations

The VDD capacitor recommended value is 100 nF to ensure high-phase margin of the internal 5-V regulator and it should be placed close to VDD pin and GND pins to minimize the series resistance and inductance.

The VDD pin provides a regulated 5-V output but it is not intended as a supply for external load. Do not supply VDD pin with external voltage source (for example the auxiliary winding of flyback converter).

Always keep GND pin 1 and GND pin 2 connected together with the shortest possible connection.

## Layout

**11.1** **Layout** ** ** **Guidelines** - • In both buck and buck-boost low-side configurations, the copper area of the switching node DRAIN should be minimized to reduce EMI. - • Similarly, the copper area of the FB pin should be minimized to reduce coupling to feedback path. Loop C L, Q1, R FB1 should be minimized to reduce coupling to feedback path. - • In high-side buck and buck boost the GND, VDD and FB pins are all part of the switching node so the copper area connected with these pins should be optimized. Large copper area allows better thermal management, but it causes more common mode EMI noise. Use the minimum copper area that is required to handle the thermal dissipation. - • Minimum distance between 700-V coated traces is 1.41 mm (60 mils). **11.2** **Layout** ** ** **Example**

Figure 26 shows and example PCB layout for UCC28881 in low-side buck configuration.

**Figure 26.** ** ** **UCC28881 Layout Example**

*Submit Documentation Feedback* Copyright © 2015-2016, Texas Instruments Incorporated Product Folder Links: * * *UCC28881*

# UCC28881

# www.ti.com SLUSC36B -NOVEMBER 2015-REVISED JANUARY 2016

## Device and Documentation Support **12.1** **Device Support**

**12.1.1** **Third-Party Products Disclaimer**

# TI'S PUBLICATION OF INFORMATION REGARDING THIRD-PARTY PRODUCTS OR SERVICES DOES NOT

CONSTITUTE AN ENDORSEMENT REGARDING THE SUITABILITY OF SUCH PRODUCTS OR SERVICES OR A WARRANTY, REPRESENTATION OR ENDORSEMENT OF SUCH PRODUCTS OR SERVICES, EITHER ALONE OR IN COMBINATION WITH ANY TI PRODUCT OR SERVICE. **12.2** **Community** ** ** **Resources**

The following links connect to TI community resources. Linked contents are provided "AS IS" by the respective contributors. They do not constitute TI specifications and do not necessarily reflect TI's views; see TI's Terms of Use.

**TI E2E™Online** ** ** **Community** *** *** ***TI's Engineer-to-Engineer (E2E)*** *** *** ***Community.*** Created to foster collaboration

among engineers. At e2e.ti.com, you can ask questions, share knowledge, explore ideas and help solve problems with fellow engineers.

**Design** ** ** **Support** *** *** ***TI's Design Support*** Quickly find helpful E2E forums along with design support tools and contact information for technical support.

**12.3** **Trademarks** E2E is a trademark of Texas Instruments. All other trademarks are the property of their respective owners.

| 12.4 | Electrostatic Discharge Caution |
|:--- |:--- |
| These devices have limited built-in ESD protection. The leads should be shorted together or the device placed in conductive foam | during storage or handling to prevent electrostatic damage to the MOS gates. |
| 12.5 | Glossary |

These devices have limited built-in ESD protection. The leads should be shorted together or the device placed in conductive foam during storage or handling to prevent electrostatic damage to the MOS gates. **12.5** **Glossary** SLYZ022 - * TI* * * *Glossary*.

This glossary lists and explains terms, acronyms, and definitions.

## Mechanical, Packaging, and Orderable Information

The following pages include mechanical, packaging, and orderable information. This information is the most current data available for the designated devices. This data is subject to change without notice and revision of this document. For browser-based versions of this data sheet, refer to the left-hand navigation.

Copyright © 2015-2016, Texas Instruments Incorporated *Submit Documentation Feedback* Product Folder Links: * * *UCC28881*

# PACKAGE OPTION ADDENDUM <https://www.ti.com> 10-Nov-2025

# PACKAGING INFORMATION **Orderable part number** **Status** (1) **Material type** (2)

**Package \| Pins** **Package qty \| Carrier** **RoHS** (3) **Lead finish/** **Ball material** (4) **MSL rating/** **Peak reflow** (5) **Op temp (°C)** **Part marking** (6)

UCC28881D Active Production SOIC (D) \| 7 75 \| TUBE Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 U28881

UCC28881D.B Active Production SOIC (D) \| 7 75 \| TUBE Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 U28881

UCC28881DR Active Production SOIC (D) \| 7 2500 \| LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 U28881

UCC28881DR.B Active Production SOIC (D) \| 7 2500 \| LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 U28881

UCC28881DRG4 Active Production SOIC (D) \| 7 2500 \| LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 U28881

UCC28881DRG4.B Active Production SOIC (D) \| 7 2500 \| LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 U28881 **(1)** ** Status: ** For more details on status, see our product life cycle.

**(2)** ** Material type: ** When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance, reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind.

**(3)** ** RoHS values: ** Yes, No, RoHS Exempt. See the TI RoHS Statement for additional information and value definition.

**(4)** ** Lead finish/Ball material: ** Parts may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two lines if the finish value exceeds the maximum column width.

**(5)** ** MSL rating/Peak reflow: ** The moisture sensitivity level ratings and peak solder (reflow) temperatures. In the event that a part has multiple moisture sensitivity ratings, only the lowest level per JEDEC standards is shown. Refer to the shipping label for the actual reflow temperature that will be used to mount the part to the printed circuit board.

**(6)** ** Part marking: ** There may be an additional marking, which relates to the logo, the lot trace code information, or the environmental category of the part. Multiple part markings will be inside parentheses. Only one part marking contained in parentheses and separated by a "~" will appear on a part. If a line is indented then it is a continuation of the previous line and the two combined represent the entire part marking for that device. **Important Information and Disclaimer:** The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release. In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis. Addendum-Page 1

# PACKAGE OPTION ADDENDUM <https://www.ti.com> 10-Nov-2025 Addendum-Page 2 <https://www.ti.com>

# PACKAGE OUTLINE

# C

|.228-.244  TYP | \[5.80-6.19\] |
|:--- |:--- |
|.069 MAX | \[1.75\] |
|.100 | \[2.54\] |
| 7X.012-.020 | \[0.31-0.51\] |

#.069 MAX \[1.75\].100 \[2.54\]

# 7X.012-.020 \[0.31-0.51\]

# 2X.150 \[3.81\]

#.005-.010 TYP \[0.13-0.25\] 0 - 8.004-.010 \[0.11-0.25\]

|.010 | \[0.25\] |
|:--- |:--- |
|.016-.050 | \[0.41-1.27\] |
| 4X.050 | \[1.27\] |.016-.050 \[0.41-1.27\]

# 4X.050 \[1.27\]

# A

#.189-.197 \[4.81-5.00\] NOTE 3

# B.150-.157 \[3.81-3.98\] NOTE 4 (.041) \[1.04\]

# SOIC - 1.75 mm max height **D0007A**

# SMALL OUTLINE INTEGRATED CIRCUIT

# 4220728/A 01/2018

NOTES: 1. Linear dimensions are in inches \[millimeters\]. Dimensions in parenthesis are for reference only. Controlling dimensions are in inches. Dimensioning and tolerancing per ASME Y14.5M. 2. This drawing is subject to change without notice.  3. This dimension does not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not exceed.006 \[0.15\] per side. 4. This dimension does not include interlead flash. 5. Reference JEDEC registration MS-012, variation AA.

#.010 \[0.25\] C A B

# PIN 1 ID AREA

# SEATING PLANE

#.004 \[0.1\] C

# SEE DETAIL A

# DETAIL A TYPICAL

# SCALE 2.800 <https://www.ti.com>

# EXAMPLE BOARD LAYOUT

#.0028 MAX \[0.07\] ALL AROUND

#.0028 MIN \[0.07\] ALL AROUND

| (.213) | \[5.4\] |
|:--- |:--- |
| 4X (.050 ) | \[1.27\] |
| 7X (.061 ) | \[1.55\] |
| 7X (.024) | \[0.6\] |
| (.100 ) | \[2.54\] |
| SOIC - 1.75 mm max height | D0007A |

# 4X (.050 ) \[1.27\]

# 7X (.061 ) \[1.55\]

# 7X (.024) \[0.6\] (.100 ) \[2.54\]

# SOIC - 1.75 mm max height **D0007A**

# SMALL OUTLINE INTEGRATED CIRCUIT

# 4220728/A 01/2018

NOTES: (continued) 6. Publication IPC-7351 may have alternate designs.  7. Solder mask tolerances between and around signal pads can vary based on board fabrication site.

# METAL SOLDER MASK OPENING

# NON SOLDER MASK DEFINED

# SOLDER MASK DETAILS

# EXPOSED METAL

# OPENING SOLDER MASK METAL UNDER SOLDER MASK

# SOLDER MASK DEFINED

# EXPOSED METAL

# LAND PATTERN EXAMPLE EXPOSED METAL SHOWN SCALE:8X

# SYMM

# SEE DETAILS

# SYMM <https://www.ti.com>

# EXAMPLE STENCIL DESIGN

| 7X (.061 ) | \[1.55\] |
|:--- |:--- |
| 7X (.024) | \[0.6\] |
| 4X (.050 ) | \[1.27\] |
| (.213) | \[5.4\] |
| (.100 ) | \[2.54\] |
| SOIC - 1.75 mm max height | D0007A |

# 7X (.024) \[0.6\]

# 4X (.050 ) \[1.27\] (.213) \[5.4\] (.100 ) \[2.54\]

# SOIC - 1.75 mm max height **D0007A**

# SMALL OUTLINE INTEGRATED CIRCUIT

# 4220728/A 01/2018

NOTES: (continued) 8. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate design recommendations. 9. Board assembly site may have different recommendations for stencil design.

# SOLDER PASTE EXAMPLE

BASED ON.005 INCH \[0.125 MM\] THICK STENCIL SCALE:8X

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