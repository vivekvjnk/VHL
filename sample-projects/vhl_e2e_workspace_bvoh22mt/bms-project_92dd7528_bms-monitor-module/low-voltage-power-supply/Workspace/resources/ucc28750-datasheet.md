## UCC28750 Current-Mode Flyback Controller with Secondary-Side Regulation (SSR) **for Off-Line Applications**

## 1 Features

- • Stable continuous conduction mode (CCM)  operation with internal slope compensation - • Fixed-frequency operation of 65kHz or 100kHz - • Secondary-side regulation (SSR) with opto-coupler - • Frequency foldback and burst mode for improved  light-load efficiency - • Frequency dithering for improved EMI  performance - • Gate source/sink capability: 300mA/500mA - • Internal 4ms soft-start - • Robust protection features: - - Over-voltage and Under-voltage lockout - - Output over-power protection (OPP) - - Output short-circuit (OSC) protection - - Output over-voltage (OVP) protection - - Cycle-by-cycle peak over-current limit - - External over-temperature, over-voltage  protection (OTP, OVP) and brownout detection on FLT pin - - Internal thermal shutdown

## 2 Applications

- • Isolated offline AC/DC power supply - • Appliances - - Battery pack and charger - - Small home appliances - - Major appliance - • Grid Infrastructure - - Electricity meter - - String inverter - - Micro-inverter - • Power Delivery - - Server PSU with 12V output

## 3 Description

UCC28750 is a highly-integrated current-mode, continuous-conduction-capable, PWM controller optimized for high performance, low standby power, and cost effective offline flyback converter applications using an opto-coupler. During light-load conditions the device enters frequency foldback and burst modes, improving light-load efficiency. The burst-mode algorithm used in UCC28750 controls the minimum effective switching frequency to prevent audible noise during light-load conditions. Frequency dithering improves EMI performance, and is active in normal, frequency foldback, and power boost operations.

UCC28750 provides protection features that enable a robust converter design with minimal external components. Output over-power protection (OPP) and cycle-by-cycle over-current limit protect the load and power-stage components from electrical stress. Overvoltage and under-voltage lockout (OVLO and UVLO) prevent switching in unwanted input conditions. The FLT pin provides line brown-out sensing and protection, or external over-temperature and overvoltage protection, depending on the device variant. The FLT pin is also used to disable the device through external control by pulling the pin to ground, regardless of the device variant. **Device Information**

# PART NUMBER **PACKAGE** (1) **BODY SIZE (NOM)** UCC28750 DBV (SOT23-6) 2.9mm x 1.6mm

(1) For all available packages, see the orderable addendum at the end of the data sheet.

# UCC28750X SOT23-6 DRV

# CS

# VDD

# GND

# FLT

# FB

# FB

# FB

# VOUT

# BULK AC RECT

# BULK

# FLT

# AC **Figure 3-1. Typical Application Diagram**

# UCC28750 SLUSEW0 - DECEMBER 2023

An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications, intellectual property matters and other important disclaimers. PRODUCTION DATA.

## Table of Contents

**1 Features**............................................................................ 1 **2 Applications**..................................................................... 1 **3 Description**....................................................................... 1 **4 Device Comparison**......................................................... 3 **5 Pin Configuration and Functions**................................... 4 **6 Specifications**.................................................................. 5

6.1 Absolute Maximum Ratings........................................ 5 6.2 ESD Ratings............................................................... 5 6.3 Recommended Operating Conditions......................... 5 6.4 Thermal Information.................................................... 5 6.5 Electrical Characteristics............................................. 6 6.6 Switching Characteristics............................................ 8 6.7 Timing Requirements.................................................. 8 6.8 Typical Characteristics.............................................. 10 **7 Detailed Description**...................................................... 12

7.1 Overview................................................................... 12 7.2 Functional Block Diagram......................................... 13 7.3 Detailed Pin Descriptions.......................................... 14

7.4 Feature Description................................................... 18 7.5 Device Functional Modes.......................................... 28 **8 Application and Implementation**.................................. 29

8.1 Application Information............................................. 29 8.2 Typical Application.................................................... 29 8.3 Power Supply Recommendations............................. 41 8.4 Layout....................................................................... 42 **9 Device and Documentation Support**............................ 44

9.1 Documentation Support............................................ 44 9.2 Receiving Notification of Documentation Updates.... 44 9.3 Support Resources................................................... 44 9.4 Trademarks............................................................... 44 9.5 Electrostatic Discharge Caution................................ 44 9.6 Glossary.................................................................... 44 **10 Revision History**.......................................................... 44 **11 Mechanical, Packaging, and Orderable **

**Information**.................................................................... 45

**UCC28750** SLUSEW0 - DECEMBER 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## 4 Device Comparison

## Device Comparison

| PART NUMBER | SWITCHING FREQUENCY | PROTECTION RESPONSE | FAULT PIN MODE |
|:--- |:--- |:--- |:--- |
| UCC287501 | 65kHz | Auto-Restart | Brown Out |
| UCC287502 | 65kHz | Auto-Restart | OVP, External NTC |
| UCC287503 | 65kHz | Latching | Brown Out |
| UCC287504 | 65kHz | Latching | OVP, External NTC |
| UCC287505 | 100kHz | Auto-Restart | Brown Out |
| UCC287506 | 100kHz | Auto-Restart | OVP, External NTC |
| UCC287507 | 100kHz | Latching | Brown Out |
| UCC287508 | 100kHz | Latching | OVP, External NTC | UCC287501 65kHz Auto-Restart Brown Out

UCC287502 65kHz Auto-Restart OVP, External NTC UCC287503 65kHz Latching Brown Out UCC287504 65kHz Latching OVP, External NTC UCC287505 100kHz Auto-Restart Brown Out

UCC287506 100kHz Auto-Restart OVP, External NTC UCC287507 100kHz Latching Brown Out UCC287508 100kHz Latching OVP, External NTC **<https://www.ti.com**>

# UCC28750 SLUSEW0 - DECEMBER 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## 5 Pin Configuration and Functions

# GND DRV

# CS

# VDD FB

# FLT

## Figure 5-1. Top-view of DBV package (6 pins)

## Table 5-1. Pin Descriptions

# PIN

# TYPE (1) **DESCRIPTION** **NAME** **NO.**

GND G Ground return for the controller. Connect this pin to the primary-side ground of the converter using a low-impedance path.

# FB I

Voltage feedback pin with internal DC bias. Typically, connect this pin to the collector of an opto-coupler device to provide isolated voltage feedback from the secondary side of the converter.

# FLT I

Fault sensing pin. Implement over-temperature protection by connecting an NTC resistor between this pin and GND. Connecting a resistor or Zener diode from a rectified auxiliary winding voltage can also implement output voltage overvoltage protection. Implement brownout detection by using a resistor divider from the bulk voltage to the FLT pin. Pulling this pin below the disable threshold disables switching operation.

# CS I

Current-sense and slope-compensation input pin. Connect this pin to the source lead of the flyback power MOSFET and the external current sensing resistor. An optional series resistor between the CS pin and source of the power MOSFET can be used to adjsut the amplitude of the controller's internal slope compensation.

# VDD P

Bias supply pin for the controller. Typically connect this pin the output of an auxiliary bias winding from the flyback transformer, and to a resistor network from the line voltage to provide bias at start-up. Other bias schemes that do not violate the pin ratings of the device are permissible.

# DRV O

Low-side gate-driver output optimized to drive low-cost silicon MOSFETs with up to 300 mA peak pull-up and 500 mA peak pull-down capability. A series gate resistor can be used to slow the turn-on and turn-off of the MOSFET to control high-frequency EMI.

(1) I = Input, O = Output, I/O = Input or Output, G = Ground, P = Power.

**UCC28750** SLUSEW0 - DECEMBER 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## 6 Specifications

**6.1 Absolute Maximum Ratings** Over operating free-air temperature range (unless otherwise noted) (1)

# MIN **MAX** **UNIT** VDD VDD input voltage range -0.3 V

DRV DRV output voltage range -0.3 V VDD + 0.3 V CS CS pin voltage -0.3 5.5 V

# FB FB pin voltage -0.3 5.5 V FB pin source current Internally limited mA

# FLT FLT pin voltage range -0.3 5.5 V FLT pin sink current mA T J Junction temperature °C T stg Storage temperature °C

(1) Stresses beyond those listed under *Absolute Maximum Rating* may cause permanent damage to the device. These are stress ratings only, which do not imply functional operation of the device at these or any other conditions beyond those indicated under *Recommended Operating Condition*. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability.

## 6.2 ESD Ratings

# VALUE **UNIT** V (ESD) Electrostatic discharge

Human body model (HBM), per ANSI/ESDA/ JEDEC JS-001, all pins (1) \pm2000

V Charged device model (CDM), per JEDEC specification JS-002, all pins (2) \pm500

(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process. (2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.

## 6.3 Recommended Operating Conditions

Over operating free-air temperature range (unless otherwise noted)

# MIN **TYP** **MAX** **UNIT** VDD Operating VDD input voltage V DRV DRV output voltage range -0.3 V CS CS pin voltage -0.3 0.9 V FB FB pin voltage -0.3 2.6 V FLT FLT pin voltage range -0.3 V GND GND pin voltage -0.3 0.3 V T J Junction temperature °C

## 6.4 Thermal Information

# THERMAL METRIC (1)

# UCC28750

# UNIT **PKG DBV (SOT-23)**

# 6 PINS

| RθJA | Junction-to-ambient thermal resistance | 231.1 | ℃/W |
|:--- |:--- | ---: |:--- |
| RθJC(top) | Junction-to-case (top) thermal resistance | 158.9 | ℃/W |
| RθJB | Junction-to-board thermal resistance | 117.2 | ℃/W |
| ΨJT | Junction-to-top characterization parameter | 94.9 | ℃/W |

R\thetaJC(top) Junction-to-case (top) thermal resistance 158.9 ℃ /W

R\thetaJB Junction-to-board thermal resistance 117.2 ℃ /W

\PsiJT Junction-to-top characterization parameter 94.9 ℃ /W **<https://www.ti.com**>

# UCC28750 SLUSEW0 - DECEMBER 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

# THERMAL METRIC (1)

# UCC28750

# UNIT **PKG DBV (SOT-23)**

# 6 PINS

\PsiJB Junction-to-board characterization parameter 116.9 ℃ /W

(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application report.

## 6.5 Electrical Characteristics

Unless otherwise specified, VDD = 20 V; V FB = 2.3 V; V FLT = 2 V; T A = 25 ℃; C DRV = 1000 pF

# PARAMETER

**TEST CONDITIONS** **MIN** **TYP** **MAX** **UNIT**

# VDD PIN V uvlo(on)

VDD undervoltage-lockout turn-on voltage (rising) -40℃ < TJ < 125℃ 14.3 15.3 16.3 V

V uvlo(off) VDD undervoltage-lockout turn-off voltage (falling) -40℃ < TJ < 125℃ V

| Vovlo (1) | VDD overvoltage-lockout threshold | VFB = 2.3 V | V |
|:--- |:--- |:--- |:--- |
| Vpor (1) | Power-on reset level (latch-off fault un- | latches, IC reset) | V |
| IVDD(start) | Start-up controller bias current | VVDD = 14 V | μA |

V por (1) Power-on reset level (latch-off fault unlatches, IC reset) V

I VDD(start) Start-up controller bias current VVDD = 14 V \muA I VDD(on) Operating controller bias current

# UCC287501/2/3/4 (65 kHz) fSW = 65 kHz $$ CDRV = 1000 pF $$ VFB = 2.3 V 1.8 2.5 mA

# UCC287505/6/7/8 (100 kHz) fSW = 100 kHz $$ CDRV = 1000 pF $$ VFB = 2.3 V 2.7 mA

I VDD(wait) (1) Wait state bias current FB Pin bias current subracted from value \muA

I VDD(fault) (1) Fault state controller bias current FB Pin bias current subracted from value \muA

I VDD(dis) (1) Disabled state controller bias current VFLT = 0 V \muA

# FB PIN (1) R FB Pull-up resistor k\Omega V FB(offset) Internal offset of V FB 0.8 V G FB FB pin to CS pin ratio V/V

I FB(short) FB pin short circuit current 0.5 mA V0 peak

Feedback voltage pin threshold to clamp maximum switching frequency 3.0 V V1 norm

Feedback voltage threshold to operate at the fixed switching frequency 2.6 V V2 foldback

Feedback voltage pin threshold to linearly lower switching frequency 2.0 V V3 burst

Feedback voltage pin threshold to enter burst mode 1.2 V V4 stop

Feedback voltage pin threshold to stop switching 1.1 V V open Feedback voltage open loop V V opp

Feedback voltage which starts the over-power protection fault timer Duty cycle > 60-% 2.6 V

# DRV PIN (1)

I source(pk) (1) Peak driver source current mA

**UCC28750** SLUSEW0 - DECEMBER 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

Unless otherwise specified, VDD = 20 V; V FB = 2.3 V; V FLT = 2 V; T A = 25 ℃; C DRV = 1000 pF

# PARAMETER

**TEST CONDITIONS** **MIN** **TYP** **MAX** **UNIT** I sink(pk) (1) Peak driver sink current mA

R OL (1) Pull-down resistance (off-state) VDD = VUVLO(off) + 100 mV, IDRV =1 mA \Omega

| VDRV(clamp) (1) | DRV voltage clamp |
|:--- |:--- |
| VDD = 20 V | V |
| VDD = Vuvlo(off) + 100 mV | V |

# VDD = 20 V V VDD = Vuvlo(off) + 100 mV V

# FLT PIN V brownout (1)

Voltage on FLT pin which causes the controller to stop switching when a brownout event is detected

# 1.4 V I brownout (1)

Current source which changes the threshold of V brownout after a brown-in event, providing hysteresis \muA FLT hyst(brownout) (1)

Hysteresis on FLT pin for the brownout threshold. The FLT pin must cross V brownout + FLT hyst(brownout) to enable switching operation mV

V FLT(open) (1) Voltage on FLT pin when nothing is connected UCC287502/4/6/8 2.3 V V FLT(ovp)

Voltage on FLT pin which causes the controller to stop switching when an overvoltage event occurs

| 3.8 | 4.1 | 4.3 | V |
|:--- |:--- |:--- |:--- |
| FLThyst(ovp) (1) | Hyteresis on FLT pin for the | overvoltage protection threshold | mV |
| IFLT(ovp, clamp) (1) | Current sink that is enabled during the | OVP fault | μA |

FLT hyst(ovp) (1) Hyteresis on FLT pin for the overvoltage protection threshold mV

I FLT(ovp, clamp) (1) Current sink that is enabled during the OVP fault \muA I FLT(tsd) (1)

Current source out of the pin into an NTC resistor for external overtemperature fault \muA V FLT(tsd) (1)

Voltage on FLT pin which causes the controller to stop switching when an overtemperature even occurs

# 0.95 1.05 V

FLT hyst(tsd) (1) Hysteresis on FLT pin for the thermal shutdown theshold mV V FLT(dis)

Voltage on FLT pin which causes the controller to stop switching when the pin is pulled below the threshold

# 0.45 0.5 0.55 V

FLT hyst(dis) (1) Hysteresis on FLT pin for the disable theshold mV t prop(dis) (1)

Propagation from the time when the disable fault occurs to the time when the controller stops switching µs

# CS PIN AND INTERNAL SLOPE-COMPENSATION (1)

V CS(limit) CS peak current limit voltage V FB \> V0 Norm mV

V CS(min) CS peak current limit voltage V FB \< V3 Burst mV t ontime(min)

Minimum on time possible, this is a sum of the t prop(ocl) and t leb specifications ns

t prop(ocl) Current limit propagation delay ns t leb Leading edge blanking time ns t ss Soft-start time 4.3 ms I ramp(slope)

Slope compensation current ramp amplitude VFB = 2.3 V \muA

# INTERNAL THERMAL SHUTDOWN (1) **<https://www.ti.com**>

# UCC28750 SLUSEW0 - DECEMBER 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

Unless otherwise specified, VDD = 20 V; V FB = 2.3 V; V FLT = 2 V; T A = 25 ℃; C DRV = 1000 pF

# PARAMETER

**TEST CONDITIONS** **MIN** **TYP** **MAX** **UNIT** T shut

Internal die temperature that will stop device operation ℃ T shut(hyst) Thermal shutdown hysteresis ℃ T shut(rec)

Internal die temperature to recover from thermal shutdown ℃

(1) Specified by design, not production tested.

## 6.6 Switching Characteristics

Unless otherwise specified, VDD = 20 V; V FB = 2.3 V; V FLT = 2 V; T A = 25 ℃; C DRV = 1000 pF

# PARAMETER

**TEST CONDITIONS** **MIN** **TYP** **MAX** **UNIT**

# DRV PIN (1)

t rise Drive voltage rise time VDD > 12 V, 10-90% Rise time CLOAD $$ = 1000 pF $$ ns

t fall Drive voltage fall time 90-10% Fall time CLOAD = 1000 pF ns

# OSCILLATOR AND FREQUENCY FOLDBACK f sw Switching frequency

| UCC287501/2/3/4 (65 kHz version) | VFB = 3.5 V | kHz |
|:--- |:--- |:--- |
| UCC287505/6/7/8 (100 kHz version) | VFB = 3.5 V | kHz |
| V1norm \< VFB | Frequency Increase | kHz |
| UCC287501/2/3/4 | -40℃ \< TJ \< 125℃ | V2foldback \< VFB \< V1norm |

UCC287505/6/7/8 (100 kHz version) VFB = 3.5 V kHz V1 norm \< V FB Frequency Increase kHz

UCC287501/2/3/4 -40℃ < TJ < 125℃ V2 foldback \< V FB \< V1 norm kHz

UCC287505/6/7/8 -40℃ < TJ < 125℃ V2 foldback \< V FB \< V1 norm kHz

V3 burst \< V FB \< V2 foldback Frequency Foldback kHz V4 stop \< V FB \< V3 burst kHz V FB \< V burst Burst Mode Operation kHz D max Max Duty Cycle %

f dither(range) Frequency modulation (EMI dither) range \pm 5 % T dither

Frequency modulation period (EMI dither) From peak to peak f sw 4.4 ms

(1) Specified by design, not production tested.

## 6.7 Timing Requirements

Unless otherwise specified, VDD = 20 V; V FB = 2.3 V; V FLT = 2 V; T A = 25 ℃; C DRV = 1000 pF

# PARAMETER

**TEST CONDITIONS** **MIN** **TYP** **MAX** **UNIT**

# PROTECTIONS (1) VDD delay(ovlo)

Switching cycles required to trigger over-voltage lockout VVDD = 29 V VFB = 2.3 V cycles t opp

Duration that V FB must be at or above the V opp threshold to trigger the fault VFB = 3 V, Duty cycle > 60 % ms t brownout

Amount of time the brownout threshold must be active to trigger the brownout fault

# VFLT = 1.3 V ms FLT delay(ovp)

Delay from the time the FLT overvoltage fault occurs to when the controller stops switching VFLT = 4.1 V cycles

**UCC28750** SLUSEW0 - DECEMBER 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

Unless otherwise specified, VDD = 20 V; V FB = 2.3 V; V FLT = 2 V; T A = 25 ℃; C DRV = 1000 pF

# PARAMETER

**TEST CONDITIONS** **MIN** **TYP** **MAX** **UNIT** FLT delay(tsd)

Delay from the time the FLT thermal shutdown fault occurs to when the controller stops switching VFLT = 0.9 V cycles CS oscp(delay)

Number of cycles of output short circuit condition to trigger the fault V CS ≥ V CS(limit) during t leb cycles T shut(delay)

Number of switching cycles once internal temperature reaches threshold to trigger fault TJ > 160 °C cycles

(1) Specified by design, not production tested. **<https://www.ti.com**>

# UCC28750 SLUSEW0 - DECEMBER 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

# 6.8 Typical Characteristics

## Figure 6-1. Switching Frequency vs Temperature Temperature (°C) 6.4 6.8 7.2 7.6 8.4 8.8 9.2 Istart (\muA)

## Figure 6-2. Startup Current vs Temperature

## Figure 6-3. UVLO On/Off vs Temperature Temperature (°C) FLT NTC Current (μA)

## Figure 6-4. FLT NTC Current vs Temperature Temperature (°C) 4.05 4.1 4.15 4.2 4.25 4.3 4.35 4.4 4.45 4.5 FLT Brownout Current (μA)

## Figure 6-5. FLT Brownout Current vs Temperature Temperature (°C) 1.5 1.6 1.7 1.8 1.9 2.1 2.2 2.3 2.4 2.5

# IVDD (\\muA)

# UCC287501/3/5/7

# UCC287502/4/6/8

## Figure 6-6. Operating Current vs Temperature

## UCC28750

SLUSEW0 - DECEMBER 2023 **<https://www.ti.com**>

## Submit Document Feedback

Copyright © 2023 Texas Instruments Incorporated

## 6.8 Typical Characteristics (continued)

**Figure 6-7. Current Sense Max Limit vs Temperature** **<https://www.ti.com**>

# UCC28750 SLUSEW0 - DECEMBER 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

# 7 Detailed Description **7.1 Overview**

## UCC28750 is a flyback controller which provides high-performance voltage regulation using an optocoupler

feedback from the secondary-side. A control law allows a high efficiency across the entire load range, enabling both discontinuous-conduction mode (DCM) and continuous-conduction mode (CCM) designs. Frequency dithering lowers the EMI energy and helps ease with EMI standards compliance. The programmable FLT pin makes the controller adaptable to various protection requirements such as brown in/out, over-voltage, over-temperature, and external disable control.

# UCC28750X SOT23-6 DRV

# CS

# VDD

# GND

# FLT

# FB

# FB

# FB

# VOUT

# BULK AC RECT

# BULK

# FLT

# AC

## Figure 7-1. The UCC28750 in a flyback design

**UCC28750** SLUSEW0 - DECEMBER 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

# 7.2 Functional Block Diagram

# FB +

# CS

# CTRL +

# V FB OFFSET

# R

# R

# CS HI ramp(slope)

# REF SS RAMP

# GND

# REF

# DRV +

# VDD VDD Power Mgmt UVLO

# REF

# POR

# FLT

# VDD

# OVLO +

# VDD OVLO th 3 Cycle Counter

# LEB CS limit OSCP + 8 Cycle Counter

# SW CLK

# FLT OVP +

# FLT OVP th 3 Cycle Counter

# FLT OTP + FLT OTP th 32 Cycle Counter FLT BO FLT BO th Brownout Timer +

# REF +

# FLT DIS th brownout

# FLT DIS 02/04/06/08 Versions 01/03/05/07 Versions CS th

# OVLO

# OPP OSCP

# UVLO

# IC OTP

# FLT OVP

# FLT OTP

# FLT BO

# FLT DIS

# CTRL +

# OPP

# U

# D OPP Clock

| OPP | OPP |
|:--- |:--- |
| 12-V | Clamp |
| S | Q | 12-V Clamp

# S Q

# Q R CS HI

# FAULT

# LEB

# CTRL

# CTRL

# SW Control Law Oscillator Dithering 85 ms Counter/Timer Clamp

# SW CLK

# SW CLOCK

# SW CLOCK

# SW CLOCK REF tsd + Fault Management

# FAULT

# FAULT

# ENABLE

| REF | POR |
|:--- |:--- |
| S | Q |
| Q | R |

# S Q

# Q R

## Figure 7-2. Functional Block Diagram

## www.ti.com

# UCC28750 SLUSEW0 - DECEMBER 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## 7.3 Detailed Pin Descriptions

## 7.3.1 VDD - Input Bias

## The VDD pin provides the bias to the controller, powering the internal references, regulators, and the

undervoltage lockout (UVLO) circuit. The VDD pin is typically powered through a resistor network connected to the rectified bulk voltage and later an auxiliary winding in an AC/DC flyback application or a separate, active source outside of AC/DC applications. The VDD pin has a wide range of operation from a turn on of 15.3V, V uvlo(on), to a turn off of 9V, V uvlo(off), and a max voltage of 28V, V ovlo. The VDD pin has low startup current, decreasing startup time and lowering the power loss of the trickle charging network used in AC/DC flyback applications.

## In addition to the C VDD capacitors shown in figures Figure 7-3 and Figure 7-4, bypass capacitors can be added for additional filtering at the pin.

# UCC28750X SOT23-6 DRV

# CS

# VDD

# GND

# FLT

# FB FB

# VOUT

# BULK Auxiliary Power Path Startup Resistor Power Path

# START

# VDD

## Figure 7-3. Biasing paths in a flyback application

# UCC28750X SOT23-6 DRV

# CS

# VDD

# GND

# FLT

# FB FB

# VOUT

# BULK Startup Resistor Power Path

# START Auxiliary Power Path

# VDD1 VDD2

## Figure 7-4. Biasing path using two diodes to split the VDD capacitance

## Refer to Section 8.2.3.5 in the design guide to size the VDD pin capacitance.

**UCC28750** SLUSEW0 - DECEMBER 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated **7.3.2 DRV - Gate Drive Out**

The DRV pin is the output of the internal gate drive of the UCC28750 controller, and is connected to the gate pin of a MOSFET switching device, typically with a series resistor. The DRV pin drives a MOSFET gate with a sink/source current of 500mA and 300mA, respectively. The DRV signal is powered through VDD, but is clamped to 12V. **7.3.3 CS - Current Sensing**

The current sensing pin, CS, is an input pin which translates the primary switching device's current information into a voltage to be compared to the internal control voltage. The CS pin has a range of 200mV, V CS(min), to 900mV, V CS(limit). The generated current sense threshold is the control voltage (V CTRL ) divided down by a gain of 2V/V, G FB.

# CS

# CTRL R

# R

# CS HI ramp(slope)

# REF + CS th slope cs

# PWM

# DRV

# GND cs **Figure 7-5. Current Sensing Pin Circuit**

An internal slope compensation ramp, I ramp(slope), programmed through an external series resistor R slope enables stable operation in a continuous-conduction-mode (CCM) by removing the unwanted effect of sub-harmonic oscillation when the duty cycle is above 50%.

An internal leading-edge blanking circuit blinds the controller from noise during the turn-on edge of a MOSFET. If additional filtering is required a capacitor from the CS pin to GND can be used. The time constant of the RC filter cannot be similar to the leading edge blanking time of 250ns, as the additional filtering can lead to more power being delivered than designed due to delays in sensing. In addition to delivering more power, heavy filtering on the CS pin does not allow the criteria to be met for the short-circuit protection response. The criteria for a short-circuit pulse is that the CS pin voltage is greater than 900mV, V CS(limit), during the leading edge blanking time.

A small capacitor with a value of 10pF to 50pF is recommended on C CS. **<https://www.ti.com**>

# UCC28750 SLUSEW0 - DECEMBER 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## 7.3.4 FB - Feedback

## The Feedback (FB) pin connects to the collector of an analog optocoupler output transistor and carries

information about the system output state. Internally, the FB node is pulled up to V REF by the R FB resistor. This interaction of the pull up resistor and the output current from the optocoupler output transistor work together to create a control voltage. The current sense threshold reference CS th is created by offsetting the FB pin voltage by 0.8V, V FB(offset), then divided down by a factor of 2V/V, G FB.

## The control voltage directly determines the converter switching frequency and peak primary current limit. More

detail is provided in the Section 7.4.2 section of the data sheet. + +

# V FB OFFSET

# SS RAMP

# REF

# CTRL

# FB +

## Figure 7-6. Feedback pin schematic drawing

**UCC28750** SLUSEW0 - DECEMBER 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## 7.3.5 FLT - Fault

## The FLT pin is a programmable protection pin that shuts down the device in unwanted conditions. The

UCC28750 device has two versions of the FLT pin: a programmable brown-in/brown-out detection version, and over-temperature and over-voltage version. All versions of the device can disable the system by pulling the FLT pin below 0.5V, V FLT(dis). There is no delay in exiting the disable state when the FLT pin is raised above the V FLT(dis) threshold.

| The brown-in/out fault detection monitors the rectified bulk voltage in a flyback application and stops switching | operation when the line voltage drops below a programmed threshold longer than 45ms, tbrown-out. The brown-out | fault resumes switching operation immediately when the FLT pin voltage goes above the brown-out threshold | and does not wait for a new VDD fault cycle. |
|:--- |:--- |:--- |:--- |
| The overvoltage protection fault triggers when the FLT pin rises above VFLT(ovp) for three consecutive switching | cycles. Care is required when designing the overvoltage circuit such that the current going into the FLT pin | does not exceed 5mA. If the FLT pin voltage drops below 1.0V, VFLT(tsd), for 32 switching cycles then the | overtemperature protection response is triggered. |
| The FLT pin can be left floating, or open, for only the UCC287502/4/6/8 variants. If the pin is left floating in | UCC287501/3/5/7 variants that have the brown-out feature the device does not start up as the FLT pin is in a | disable state. At startup with the brown-out configuration there is no current sourced from the FLT pin to raise the | pin voltage above protection levels. |

## The overvoltage protection fault triggers when the FLT pin rises above V FLT(ovp) for three consecutive switching

cycles. Care is required when designing the overvoltage circuit such that the current going into the FLT pin does not exceed 5mA. If the FLT pin voltage drops below 1.0V, V FLT(tsd), for 32 switching cycles then the overtemperature protection response is triggered.

## The FLT pin can be left floating, or open, for only the UCC287502/4/6/8 variants. If the pin is left floating in

UCC287501/3/5/7 variants that have the brown-out feature the device does not start up as the FLT pin is in a disable state. At startup with the brown-out configuration there is no current sourced from the FLT pin to raise the pin voltage above protection levels.

## More information on the operation and programming of the FLT pin is found in section Section 7.4.4.

# FLT FLT OVP +

# FLT OVP th 3 Cycle Counter

# FLT OTP + FLT OTP th 32 Cycle Counter FLT BO FLT BO th Brownout Timer +

# REF +

# FLT DIS th brownout

# FLT DIS 02/04/06/08 Versions 01/03/05/07 Versions Clamp

# SW CLOCK

# SW CLOCK REF tsd

## Figure 7-7. FLT Pin Block Diagram

## 7.3.6 GND - Ground Return

## The GND pin is the external return pin, and provides a reference point for the internal circuitry and the gate drive of the device. **<https://www.ti.com**>

# UCC28750 SLUSEW0 - DECEMBER 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## 7.4 Feature Description

## 7.4.1 Soft Start

## The UCC28750 includes a soft start feature to lower the peak current during the start-up phase. At the beginning

of a normal startup operation the output voltage of the system is zero, and the capacitors at the output are discharged. In this scenario the FB pin is pulled up to the internal V REF value. In a controller without a soft start feature, the controller switches at the highest power mode. The soft-start feature limits the stresses on the system and switching devices by clamping the internal FB voltage during the start-up phase to a stepping ramp. Now, the output voltage can rise in a controlled manner.

## The internal soft-start ramp is compared to the FB pin voltage, and as long as the internal ramp is lower than the

FB pin voltage, the internal ramp is in control of the power delivery level. As the output voltage increases to the programmed level, the FB pin decreases and takes control instead of the internal soft start ramp. The full ramp time of soft start is fixed internally to 4.3ms, t ss. FB Pin Soft Start Ramp

# V FB OFFSET Output Voltage

# CTRL FB, V CTRL Output Voltage t

## Figure 7-8. Softstart Ramp on Startup

**UCC28750** SLUSEW0 - DECEMBER 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated **7.4.2 Control Law**

UCC28750 is a fixed frequency controller under normal operating conditions, but modulates the switching frequency and CS thresholds at higher and lighter loads, providing a momentary boost of power for high loads and increased efficiency at light loads.The frequency control law uses alternating amplitude and frequency modulating regions in conjunction with an amplitude modulated current sense threshold to achieve regulation at varying conditions.

There are five regions of operation, referred to as section A-E in Figure 7-9.

# VFb (V) TSw (us) VCsTh (mV) V4Stop V3Burst V2Foldback V1Norm V0PwrBst VCsMax 15/10 7.7/5 VCs TSw

# A B C D E 65 / 100 kHz 130 / 200 kHz 25 kHz **Figure 7-9. UCC28750 Control Law**

1. Region A: This region is the power boost region in which the frequency increased to the maximum of 130/200kHz (based on the device variant) and the current sense threshold is fixed to the V CS(limit) of 900mV. 2. Region B: This is the normal operating region, where the switching frequency is fixed to 65/100kHz, but the current sensing threshold is amplitude modulated to provide the necessary power required by the application load. 3. Region C: This is the frequency foldback region, where the switching frequency and current sensing threshold are being lowered, to accommodate lower power requirements and lower switching losses. 4. Region D, E: These two regions are the burst mode operation of the controller. When the FB voltage is lower than 1.2V,V3Burst, but higher than 1.1V, V4Stop, the controller continues to switch but at the lowest current sensing threshold and frequency. When the FB pin voltage is below V4Stop, the controller stops switching operation. Without switching the FB pin rises as the output voltage drops, and the controller resumes switching operation. **<https://www.ti.com**>

# UCC28750 SLUSEW0 - DECEMBER 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* **7.4.3 Frequency Dithering**

Frequency dithering, also known as frequency swapping, frequency hopping, frequency jitter, is a concept to modulate the primary switching frequency by a small amount to spread the EMI energy, lowering EMI peaks. UCC28750 modulates the primary switching frequency by superimposing a triangular frequency onto the switching frequency, shifting the switching frequency by 5%, f dither(range), over a period of 240Hz, T dither. Base Frequency Dithered Frequency t Frequency dither dither(range)

**Figure 7-10. Frequency Dithering of a Fixed Frequency** **7.4.4 Fault Protections**

UCC28750 includes a set of protection features, both internally fixed and externally programmable. These faults are designed to protect the device and the system application. UCC28750 has latches and auto-restart options for the protection responses. In a latched device when a fault is detected UCC28750 does not resume switching operation, even if all faults are removed, until the VDD pin voltage is brought below 5V, V por, and then up to the turn on threshold of 15.3V, V uvlo(on). In the auto-restart response the device resumes switching operation every startup cycle. The a fault is detected again the controller re-enters the fault state. If all faults are removed prior to a startup cycle then the controller resumes normal operation.

The faults are listen below: - • VDD under and overvoltage lockout - • Internal overtemperature shutdown - • Output overpower protection (OPP) with internal compensation - • Output short circuit protection (OSCP) - • FLT pin protections - - Input line brown-in/out detection - - Overvoltage protection - - External overtemperature protection - - Controllable disable/shutdown

**UCC28750** SLUSEW0 - DECEMBER 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

# VDD

# ENABLE uvlo(on) por uvlo(off)

Normal startup process can continue when the fault is removed fault on start

# FAULT fault(delay) fault(delay)

## Figure 7-11. Auto-Restart Fault Diagram

# VDD

# ENABLE uvlo(on) por uvlo(off)

Pull down on VDD or remove the input bias to allow voltage  to fall below the latch reset threshold

Normal startup process can continue when the fault is removed and the latch is reset fault start fault(delay)

# LATCH

# FAULT

# RESET

## Figure 7-12. Latch Fault Diagram

## 7.4.4.1 VDD Overvoltage and Undervoltage Lockout

## UCC28750 operates over a wide input voltage range, and has protections to enable safe operation. The

device does not start switching operation until the input voltage, VDD, reaches above 15.3V, V uvlo(on), threshold. UCC28750 continues to operate until the input voltage reaches either 9V, V uvlo(off), or 28V, V ovlo. The upper limit to the operation range is defined as the over-voltage lockout threshold. In the UVLO case, the device stops switching immediately. In the OVLO case, the device stops switching operation and triggers a protection response after the input voltage goes above the V ovlo threshold for three consecutive switching cycles.

## 7.4.4.2 Internal Overtemperature Protection

## The device has an internal temperature threshold, which disables the part once the internal die has reached

160 ℃ and is qualified after 32 switching cycles. The thermal shutdown threshold has a large hysteresis of 20 ℃. Once the fault clear temperature of 140 ℃ is reached the part can resume normal switching operation. If the device is a latched version, then the VDD pin voltage needs to be brought below 5V, V por, to have the device resume switching operation. **<https://www.ti.com**>

# UCC28750 SLUSEW0 - DECEMBER 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## 7.4.4.3 Output Overpower Protection

## The output power-protection is a line-compensated, feedback based protection to limit the output power of the

system application. The FB pin voltage is compared to a ramp that is generated based on the switch on-time, the duty cycle, of each switching event. When the FB pin voltage is greater than the ramp at the negative edge of the internal PWM signal, the OPP timer increases. If the FB pin voltage is less than the OPP threshold, the timer decreases. When the timer reaches the OPP time, t opp, of 85ms the fault is engaged and the device stops switching. Duty Cycle (%) OPP Ramp (V) 20% 60%

# 2.3 V

# 2.6 V

## Figure 7-13. OPP Ramp

## In Figure 7-14, the output load in an application is increased which causes the control loop to increase the

FB pin voltage. The increase in FB pin voltage indicates the need to deliver more power to maintain regulation. Once the FB pin is above the OPP ramp and OPP is detected, the internal OPP timer starts counting towards the t opp limit of 85ms. Eventually the OPP timer is reached and the protection is engaged and the device stops switching.

# OPP RAMP

# OPP DETECTED

# FB

# IOUT

# OPP

# PWM

FB less than OPP RAMP FB greater than OPP RAMP OPP Timer Limit Reached

## Figure 7-14. Load Step Causing OPP

**UCC28750** SLUSEW0 - DECEMBER 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## Figure 7-15 shows how the timer operation works, with a load condition that is not as long as t opp initially,

but with repetitive high load pulses the overpower protection can still engage. In an application that requires momentary power boosts, the time of the power boost pulse must be shorter than the time without a power boost to not engage OPP. Otherwise, over time, the internal timer reaches the 85ms limit to engage OPP.

# OPP

# OPP TIMER

# LOAD FB OPP Threshold OPP Timer Limit

## Figure 7-15. OPP Timer Increasing to the OPP Timer Limit **<https://www.ti.com**>

# UCC28750 SLUSEW0 - DECEMBER 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## 7.4.4.4 Output Short-Circuit Protection

## In the event of an output short circuit, the UCC28750 can protect the system by quickly shutting down. During

a short-circuit event, the current sense sees a sharp rise during the switch on-time, and a very shallow negative slope during the off-time of the switching cycle. The UCC28750 is turned on for a minimum amount of time for every switching cycle due to the leading edge blanking (LEB) feature and internal logic delays. If the CS pin is above the maximum CS threshold during the leading edge blanking time for eight cycles, the output short-circuit protection is engaged and the device stops switching operation.

# PWM LEB

# OSCP EVENT

# OSCP FAULT

# ENABLE

# CS

## Figure 7-16. Output Short-Circuit Protection Diagram

**UCC28750** SLUSEW0 - DECEMBER 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated ***7.4.4.5 FLT Pin Protections***

The FLT pin is a programmable fault pin and changes operation basedo on the UCC28750 variant, whether the device is a brown-out or over-temperature/over-voltage version. FLT BO FLT BO th Brownout Timer +

# REF

# BULK botop bobot brownout FLT

**Figure 7-17. FLT Pin Brown-out Configuration Example**

The brown-out variant is a fault method to control the turn-on and turn-off thresholds of the system application. Once the system has crossed the turn-on (also known as brown-in) threshold, the UCC28750 turns on an offset current, typically 4μA, which makes the thresholds programmable. The offset current is turned on only after the bulk voltage passes the brown-in threshold first. The FLT pin voltage must cross the V brown-out threshold for t brown-out for the brown-out fault to trigger. The time required to trigger the fault disqualifies any short term false triggering events from incorrectly triggering the brown-out. The FLT pin has a clamp internally that prevents the FLT pin from reaching dangerous levels if the application requires the brownout feature and has a wide input range requirement (such as a 100V,AC to 400V,AC operating range).

The top resistor shown in Figure 7-17 must not be a single resistor. Most non-high-voltage rated resistors typically have a voltage rating of around 200V. Therefore, the top resistor in the brownout resistor divider must be formed with several resistors, typically three.

Programming the brown-in and brown-out thresholds is a matter of choosing the desired voltage divider resistor values: Vbi = Vbrownout + 50mV × Rbotop + Rbobot Rbobot (1) Vbo =

Vbrownout × Rbotop + Rbobot −Ibrownout × Rbobot × Rbotop Rbobot (2)

Where: - • V bi is the programmed brown-in input voltage level - • V bo is the resultant brown-out input voltage level - • V brown-out is the FLT pin's brown-out threshold, 1.4V - • R bobot is the bottom resistor in the voltage divider - • R botop is the top equivalent resistor in the voltage divider - • I brown-out is the offset current enabled once the input voltage passes the V bi level **<https://www.ti.com**>

# UCC28750 SLUSEW0 - DECEMBER 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* ntc

# FLT

# FLT OVP +

# FLT OVP th 3 Cycle Counter

# FLT OTP + FLT OTP th 32 Cycle Counter

# SW CLOCK

# SW CLOCK REF tsd

# SYS\_OVP Z,limit

# Z

## Figure 7-18. FLT Pin Overvoltage/Overtemperature Configuration Example

## The programmable over-voltage and over-temperature features are available in the UCC28750 variants. The

overvoltage protection fault is triggered when the FLT pin voltage crosses 4V, V FLT(ovp), for three consecutive switching cycles, similar as the three switching cycles required for OVLO. In Figure 7-18, V SYS\_OVP is a voltage source that can be used to triggeer the protection outside of the device VDD and system output voltage. If the overvoltage is configured with a Zener diode, then the following restriction applies:

# V SYS\_OVP \> V Z −V FLT(ovp) (3)

## Where

- • V Z is the breakdown voltage of the Zener diode - • V SYS\_OVP is a user defined location that is susceptible to over-voltage and is used to turn off the UCC28750

## Care must be take that the current going into the FLT pin from the Zener diode's breakdown does not exceed

5mA. Therefore a current limiting resistor is recommended if a Zener diode is use for overvoltage protection on the FLT pin.

## A different method can be applied as long as the voltage stays within the FLT pin's voltage rating.

## The overtemperature fault is triggered when the FLT pin voltage crosses the 1V, V FLT(tsd), overtemperature

threshold for 32 switching cycles, FLT delay(tsd). Finally, the disable threshold of 0.5V,V FLT(dis), stops switching operation immediately immediately.

**UCC28750** SLUSEW0 - DECEMBER 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## 7.4.5 Slope Compensation

## The UCC28750 device is a peak-current mode control device which offers high efficiency while overcoming

drawbacks from voltage-mode control devices. However, when the application requires switching with a duty cycle greater than 50%, the application can suffer from an instability called sub-harmonic oscillation. Figure 7-19 shows what can happen to the switching operation and inductor current of a peak current mode control scheme. The perturbed current, without a compensated ramp, cannot return to a normal steady state operation. By adding a ramp onto the fixed threshold, this phenomenon is resolved.

## The slope compensation ramp is programmed through a series resistor on the CS pin, and is shown in more detail in Section 8.2.3.3.

# SW SW SW SW SW SW Perturbed current without slope compensation Perturbed current with slope compensation Steady state current Perturbed current Compensated current Compensation ramp Fixed threshold

## Figure 7-19. Slope Compensation in a Peak Current Mode Control Scheme **<https://www.ti.com**>

# UCC28750 SLUSEW0 - DECEMBER 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* **7.5 Device Functional Modes** **7.5.1 Off**

At an initial startup phase, the device is in the off state while the voltage at the VDD pin is below the V uvlo(on) voltage of 15.3 V. In this state the device's features and circuitry are disabled, and the device's current consumption is only the quiescent current, I VDD(start), of 5 μA. Once the VDD pin voltages crosses the turn on threshold, the device enters in to the startup phase. If a fault occurs, or the system application is shutting down, the device remains on until the VDD pin voltage falls below V uvlo(off). **7.5.2 Startup**

When the UCC28750's VDD pin voltage reaches the turn-on threshold, the device enters into the startup state and begins to deliver power to the output. In this state the internal control voltage is clamped to a fixed ramp, enabling a controlled rise in the output voltage while lowering current stresses on the switching devices. After the soft start ramp is finished rising, or the FB pin voltage falls below the soft start ramp, is the startup state finished. All of the fault features are still enabled during this time, and can cause the device to enter into a fault state. **7.5.3 On**

Once finished with the startup state, the device enteres the on state. In this state all of the features of the control law are enabled. The control loop of the system application takes over as the main feedback signal for the control voltage. The FB pin voltage determines the switching operation of the device, and decides if the controller operates in the burst mode, frequency foldback, fixed frequency, or power boost modes, as seen in the Section 7.4.2 section. **7.5.4 Fault**

The fault state is entered when the UCC28750 devices recognizes one of the numerous faults available, as seen in Section 7.4.4. When a fault is triggered, the device stop switching operation, and begins to sink a fault current of 350 μA. This fault current causes the VDD pin voltage to drop to the V uvlo(off) voltage, turning off the device and resetting the fault logic states. Once the device crosses the turn on voltage, V uvlo(on), the startup phase begins and if the fault is removed then normal operation resumes. If the device is a latched variant (UCC287501/3/5/7), then the switching operation cannot resume until the VDD pin voltage is brought below the 5 V, V por, power-on reset threshold. Refer to figures below for expected operation waveforms in a fault state.

To have the correctly VDD cycle as shown in the fault diagrams a restriction on the startup resistors is placed, where R START is the startup resistor network shown in Section 7.3.1. Vbulk,max Ifault \< R start (4) **7.5.5 Disabled**

The disabled state is a low-power state that is entered by bringing the FLT pin voltage below the V flt(dis) threshold of 0.5 V, available in all variants of the UCC28750 device. In this state the device current consumption drops to 250 μA, and switching operation is stopped. The device resumes normal operation, if no other faults are present, once the FLT pin voltage exceeds 0.5 V. A logic level MOSFET can be used with a control signal from another source to bring the FLT pin voltage below the 0.5-V threshold.

Because the device consumes less current in the disabled state, extra care must be taken with the selection of the start up trickle charge resistors if that biasing scheme is used as shown in Figure 7-3 and Figure 7-4. If the startup resistors are too small and do not meet the criteria of Equation 5, the amount of current through the biasing path can be greater than the current that the device consumes. This leads to the VDD pin voltage rising and causing an over stress event on the VDD pin. A Zener diode can be put from VDD to GND as a safety clamp. Vbulk,max Idis \< R start (5)

**UCC28750** SLUSEW0 - DECEMBER 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## 8 Application and Implementation

## Note

## Information in the following applications sections is not part of the TI component specification,

and TI does not warrant its accuracy or completeness. TI's customers are responsible for determining suitability of components for their purposes, as well as validating and testing their design implementation to confirm system functionality.

## 8.1 Application Information

## The UCC28750 device is an optimized AC-DC flyback controller that uses secondary side regulation through

an optocoupler interface and peak-current mode control to tightly regulate the output voltage. The information from the optocoupler interface determines the voltage at the FB pin, which controls the mode of operation. Under light loads the UCC28750 switches at a lower frequency, entering burst mode if the load is light enough. At higher loads the device switches at the fixed frequency, 65kHz or 100kHz, depending on the UCC28750 variant. The UCC28750 has duty cycle capabilities greater than 50%, and the integrated slope compensation allows the application to make full use of both continuous and discontinuous conduction modes of operation. **8.2 Typical Application**

# UCC28750X SOT23-6 DRV

# CS

# VDD

# GND

# FLT

# FB

# FB

# FB

# VOUT

# BULK AC RECT

# BULK

# FLT

# AC

## Figure 8-1. Typical Application Diagram **<https://www.ti.com**>

# UCC28750 SLUSEW0 - DECEMBER 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## 8.2.1 Application

## The typical application of the UCC28750 is an off-line flyback power supply up to 70W. A trickle charge resistor

network and an auxiliary winding provide the bias from startup to normal operation to the controller. The auxiliary winding provides information of the ouput voltage, which can be used for over-voltage protection. The FLT pin is programmed to provide over-temperature protection to an expected hotspot on the printed circuit board, such as the transformer.

## 8.2.2 Design Requirements

## Table 8-1. Design Parameters

# PARAMETER

**Conditions** **MIN** **TYP** **MAX** **UNIT** **Input Requirements** Input Line Voltage 120/240 V, AC Minimum Bulk Voltage V, DC Input Line Frequency 50/60 Hz **Output Requirements**

Output Voltage VIN = Min to max, Iout = No load to Full load V Output Current VIN = Min to max 2.5 A Output Voltage Ripple Steady state % Load transient 10% to 90% of maximum current % **System Characteristics** Switching Frequency VIN = Min to max, Max output current kHz VIN = Min to max, Min output current kHz

**UCC28750** SLUSEW0 - DECEMBER 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated **8.2.3 Detailed Design Procedure**

***8.2.3.1 Input Bulk Capacitance with Minimum Bulk Voltage***

The bulk capacitance can consist of a set of one or more capacitors connected in parallel, often with some inductance between them to suppress differential mode noise. Input EMI filter design is outside the scope of this data sheet and is not discussed.

The mimimum bulk voltage valley, V bulk,min, is dependent on the total input capacitance value used in the power stage design. The input capacitor is chosen to maintain an acceptable input voltage ripple. The ripple is largest at the minimum input line at the largest output power scenario. Therefore, the input bulk capacitance is based on the a wanted V bulk,min at the max power.

The input power can be estimated by taking the maximum output power and dividing the result by the estimated efficiency. Pin = Vout × Iout,max \eta (6) C bulk = 2Pin \times 4 + 1 2 \pi arcsin Vbulk,min 2VINmin 2VINmin 2 −Vbulk,min (7)

Where - • V bulk,min is the minimum DC bulk voltage - • VIN min is the minimum AC voltage applied to the flyback application

For this design, the result from taking the design requirements and the plugging in those values to Equation 6 and Equation 7, a recommended minimum of 110μF for the bulk input capacitance.

***8.2.3.2 Transformer Turns Ratio and Inductance***

The transformer design process starts with selecting a switching frequency and maximum duty cycle. With the UCC287502, the switching frequency is set to 65kHz for the max load operation. The maximum duty cycle can safely be chosen to be above 50% as the UCC28750 is a flexible controller capable of DCM and CCM operation while handling sub-harmonic oscillation with the internal slope compensation feature. D max,initial = 65 % (8)

With the maximum duty cycle for the design set, the secondary to primary transformer turns ratio, N S to N P, can be chosen by using the boundary mode condition equations to simplify the design process. The turns ratio selection is an iterative process, and the primary switching MOSFET device maximim drain-to-source voltage must be accounted for when designing the transformer.

The turns ratio is initially chosen by using the minimum input voltage and the maximum duty cycle value. This scenario has the highest average current the transformer and switching device must handle, and is why in most of the equations use this worst case for determining the inductance and turns ratio of the transformer. Setting N P to 1 turn, the secondary turns in the turns ratio is determined with Equation 9

# NS =

Vo × 1 −Dmax,initial Vbulk,min × Dmax,initial (9)

The 650V drain-to-source (V DS ) rated MOSFET is a popular device used in flyback topologies, especially those with a universal input requirement (80V,AC to 265V,AC). The reflected voltage, the voltage seen by the transformer during the secondary conduction time, must be below the MOSFET V DS rating, with additional margin for the leakage spike. The leakage spike is additional ringing that occurs in flyback designs due to the MOSFET output capacitance and transformer leakage inductance. **<https://www.ti.com**>

# UCC28750 SLUSEW0 - DECEMBER 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* Vmargin = 0.8 \times VDS (10) V reflected = V bulk,max +

# NP NS × V o (11)

| Vreflected \< Vmargin | (12) |
|:--- |:--- |
| Combining Equation 10, Equation 11, Equation 12, and solving for the turns ratio results in a constraint for the | turns ratio: |
| NP | NS \< |

Combining Equation 10, Equation 11, Equation 12, and solving for the turns ratio results in a constraint for the turns ratio:

# NP NS < Vmargin −Vbulk,max Vo (13)

A turns ratio of 1:6 is chosen for this design concept. The duty cycle can be iterated on and a new maximum duty cycle, D max, can be selected with the new turns ratio, and comes out to be around 65%, which is what the max was initially set to. D max = Vo NS NP × Vbulk,min + Vo (14)

With the selected turns ratio, maximum duty cycle, input range, and output power range, the magnetizing inductance value can be calculated using equation Equation 15, and comes out to be approximately 480μH. The equation for the inductance is derived by using the boundary mode equations and equating the average input power equal to the average output power, with a factor for the efficiency.

# L =

Vbulk,min × Dmax \times Tsw \times \eta 2 × Pout,max × Kccm (15)

Where - • η as the assumed efficiency of the flyback - • T sw as the normal operation switching period - - In this case 15μs, as the device variant for this application design is a 65kHz variant - • K ccm is factor from 0.1 to 1 that determines the percentage of output max output power at the boundary  condition that the flyback enters into the CCM state

**UCC28750** SLUSEW0 - DECEMBER 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

***8.2.3.3 Current Sense and Slope Compensation Network***

The CS pin consists of a network of current sensing resistors and the slope compensation components. For designs with a maximum duty cycle less than 50%, the slope compensation network is not necessary, and thus the current sensing resistor is a calculation based on just the maximum peak current and the maximum threshold on the CS pin. The current sensing resistors connected from the source of the MOSFET to the ground control the maximum peak current of the power stage. The CS pin maximum threshold is 900mV, and a small margin is used to have a more robust design.

# CS

# CTRL R

# R

# CS HI ramp(slope)

# REF + CS th slope cs

# PWM

# DRV

# GND cs **Figure 8-2. CS Pin Diagram**

# RCS = 0.8 \times VCS,max ipk (16) **<https://www.ti.com**>

# UCC28750 SLUSEW0 - DECEMBER 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

Because UCC28750 can operate in CCM and DCM, the boundary mode equation for i pk is used as a starting point for selecting the current sense resistor value, with R CS initially selected with a nominal value of 420mΩ. Ipk = Vbulk,min × Dmax × Tsw L (17)

In a design with the duty cycle greater than 50% slope compensation must be used to avoid sub-harmonic isolation. UCC28750 has an internal ramp that helps remedy this issue. A resistor is added between the CS pin and the current sense resistor which programs the amount value of the ramp. In a peak-current current scheme, adding a ramp that is equal to half of the slope of the flyback transformer during the off-time of the switching device removes instability. The slope, S off, with units Amps per second, and reflected to the primary side, during the off time of the primary switching MOSFET is shown in Equation 18. S off = Vo

# NP NS L (18)

UCC28750 has a current source that ramps to 100μA at the device's maximum duty cycle of 80%. Therefore the ramp amplitude is a ratio of the max level and the calculated duty cycle of the design. The term i slope has units of Amps per second, just like S off. i slope = iramp Dmax × Tsw (19)

Where i ramp is the 100μA amplitude of the slope compensation current during the fixed frequency (65/100 kHz) region in the control law.

The value of the R slope resistor is half of the S off value divided by the i slope. R slope = 2 \times Soff islope (20)

With a slope compensation resistor in place, the CS pin voltage needs to be re-evaluated to make sure that full power delivery is still possible at the minimum input voltage and highest load. The ramp that is generated from R slope causes the CS pin threshold to be reached earlier than expected, if the R CS stays the same as calculated from Equation 16.

V CS,with slope comp = R slope × i slope × D max × T sw + R CS × I pk (21) V CS,with slope comp \< 0.8 × V CS,max (22)

V CS,with slope comp, the addition of the peak current, represented as a voltage, and the ramp from the slope compensation current source, can go above the threshold set in Equation 22. The slope compensation resistor is changed to be lowered, rather than the current sense changing to accommodate the value from Equation 20, as adding too much of a ramp can change the control mode from peak-current mode control to effectively voltage mode control.

Equation 21 is modified to solve for R slope with R CS locked from the initial value of 420mΩ, the new R slope is 1kΩ.

**UCC28750** SLUSEW0 - DECEMBER 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated ***8.2.3.4 Output Capacitors***

The output capacitor value is determined by two factors in a power supply design: steady state ripple voltage and the output transient voltage response. The capacitor values for the transient response are typically specified as a load step from no load to full load of the power supply design. C out = Istep × tresponse Δ Vout (23)

Where - • I step is the largest step in load current - • t response is the approximate response time - • ΔV out is the allowable output voltage change tresponse = 0.33 fc + T sw (24)

Where - • f c is the approximate crossover frequency, typically set to one-tenth the switching frequency - • T sw is the switching period expected at the initial load condition before the load step

The ripple voltage in steady state has two major contributors: the change in the output voltage due to the charge and discharge of the output capacitors in every switching cycle, and the step in the output voltage due to the equivalent series resistor of the capacitors. An additional margin is placed on the ESR calculation to account for variance and aging of the

# ESR ≤ Vripple ipk,max × NPS\times50 % (25) C ripple = Iout,max × Dmax Vripple × fsw (26)

Where - • V ripple is the allowable voltage ripple for a design - • N PS is the primary to secondary turns ratio - • I out,max is the maximum output load current - • i pk, max is the primary side maximum peak current of the transformer

The final output capacitor value is the larger of the C out and C ripple values. The estimated crossover frequency largely determines the value of capacitance to use. For example, a crossover frequency of 2.5kHz suggests to use 900μF, while a 6.5kHz crossover is much lower capacitance, about 350μF. Use multiple capacitors to lower the equivalent ESR and get the actual capacitance close to the nameplate capacitance. Multiple capacitors increase robustness by accounting for DC derating and temperature rating fluctuations in the capacitance value. **<https://www.ti.com**>

# UCC28750 SLUSEW0 - DECEMBER 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* ***8.2.3.5 VDD Capacitance, C*** ***VDD***

The capacitance on VDD needs to supply the device operating current until the output of the converter reaches the target minimum operating voltage. At this time the auxiliary winding can sustain the voltage to the UCC28750. The input VDD capacitance is determind by the on current of the controller and the output voltage rise time of the application. The VDD capacitor must be able to keep the VDD pin voltage above 9V, V uvlo(off), until the output voltage reflected to the auxiliary can take over as the primary bias to the controller.

The soft start feature in UCC28750 does not ramp to full power deliver in the first steps, therefore a conservative 2ms addition is placed into Equation 27 to help size the input capacitors.

A split diode and capacitor network can be used in flyback designs to lower the initial startup time, but still have a path for a bulk capacitance on the device's input put, as shown Section 7.3.1 and reproduced here for ease of use.

# UCC28750X SOT23-6 DRV

# CS

# VDD

# GND

# FLT

# FB FB

# VOUT

# BULK Startup Resistor Power Path

# START Auxiliary Power Path

# VDD1 VDD2

**Figure 8-3. Split Diode Biasing Scheme for Use With Startup Resistors**

The first capacitor, C VDD1, is determined by the startup resistor value and the desired turn-on time. The startup resistor values are constrained by power loss and fault requirements as mentioned in Section 7.5.4.

For a design with a typical one second start time, and a startup resistor network with an sum resistance of 1.2MΩ after adding in additional margin. The resulting C VDD1 value is approximatly 6μF. The nearest standard value is 6.8μF.

C VDD2 is largely determined by the output voltage rise time and the feedback loop estimates. Those parameters can cause an small overshoot during startup, especially at no load applications. When an overshoot occurs the device can stop switching if the feedback loop pulls down on the FB pin voltage enough to push the control law into the off state ("F" region in Figure 7-9 ).

The output voltage rise time is derived from the assumed power available to charge the capacitor from zero volts to the programmed output voltage. The "2ms" term added in Equation 27 is to account for the fact that the device's soft start does not output full power in the first two milliseconds which, if not added to the equation, which can understate the rise time of the output voltage. t vo,rise = 1 Cout × Vout Pout,max + 2 ms (27)

**UCC28750** SLUSEW0 - DECEMBER 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

Typically, the crossover frequency is initially placed at one-tenth the switching frequency of the power stage. That estimate can be used to determine the initial value of C VDD2. Through experiementation and measurement, the actual crossover frequency can be determined. Using the response time estimate equation from Section 8.2.3.4, Equation 24, the overshoot of the output can be determined by modifying Equation 27 for V out and adding the t response estimate into the time term. The overshoot value can then be used to determine the amount of time required for that overshoot to decay back to steady state. V out,overshoot = 2× tvo,rise −2 ms + tresponse Cout −V out (28) t decay = Cout×Vout,overshoot Iload (29)

Equation 29 is dependent on the output load. When the output load is near zero, the decay time becomes long and therefore C VDD2 must be large to survive the decay time. Experimentation and testing must be performed to determine if a "dummy load," a resistor put at the output, is required to lower the decay time if the feedback loop causes too large of an overshoot.

The time for the overshoot to reach down to steady state regulation levels uses the fundamental capacitor equation.

# CVDD2 = Ioff × tdecay VUVLO,on −VUVLO,off + 1 V (30)

Where - • I off is the UCC28750 off-state current, typically 350μA

With the large range of t decay from the sum of t vo,rise and t response to the worse case of a one second decay time, CVDD2 can range from 15\muF to 70\muF. **<https://www.ti.com**>

# UCC28750 SLUSEW0 - DECEMBER 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback* **8.2.4 Application Performance Plots**

The figures below are a result of testing and experimentation of the universal input, 60 W output, UCC28750 Evaluation Module. In the waveforms showcasing the switching node (the drain of the switching device) in Section 8.2.4.3, Q1 refers to the switching device in a flyback application. ***8.2.4.1 Startup***

# CH1 =V BULK, CH2 = V CC, CH3 = V GATE, CH4 = V OUT

**Figure 8-4. Start-Up Waveforms at 85Vac and No ** **Load**

**Figure 8-5. Start-Up Waveforms at 85Vac and Full ** **Load**

**Figure 8-6. Start-Up Waveforms at 115Vac and No ** **Load**

**Figure 8-7. Start-Up Waveforms at 115Vac and Full ** **Load**

**Figure 8-8. Start-Up Waveforms at 230Vac and No ** **Load**

**Figure 8-9. Start-Up Waveforms at 230Vac and Full ** **Load**

**UCC28750** SLUSEW0 - DECEMBER 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## Figure 8-10. Start-Up Waveforms at 265Vac and No

## Load

## Figure 8-11. Start-Up Waveforms at 265Vac and

## Full Load

## 8.2.4.2 Load Transients

# CH1 = V OUT, CH4 = I OUT

## Load = 0.100A to 2.5A, 1kHz, 50% Duty Cycle

# VIN = 85 VAC

## Figure 8-12. Load Transients at 85Vac

# VIN = 115 VAC

## Figure 8-13. Load Transients at 115Vac

# VIN = 230 VAC

## Figure 8-14. Load Transients at 230Vac

# VIN = 265 VAC

## Figure 8-15. Load Transients at 265Vac **<https://www.ti.com**>

# UCC28750 SLUSEW0 - DECEMBER 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## 8.2.4.3 Q1 Drain Voltage Evaluation

# CH1=VQ1d, CH3 = VGATE, CH4 = VOUT

## Figure 8-16. Steady State Waveform at 85Vac

## Figure 8-17. Steady State Waveform at 85Vac

**UCC28750** SLUSEW0 - DECEMBER 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated **8.2.5 What to Do and What Not to Do**

Do - • Use multiple resistors for the high voltage startup resistor network - • Limit the current into the FLT pin, as the pin can only handle 5mA - • Use multiple resistors for the current sensing resistor if designing for higher power designs (such as 60W) - • Use high frequency bypass capacitors close to the transformer in addition to the bulk capacitors - • Place the slope compensation resistor close to the UCC28750 device, not the current sensing resistor - • Use an additional current sensing filter capacitor to aid the leading edge blanking with noise filtering - • Place a resistor in series with the DRV pin to the gate of the MOSFET to tune the turn-on and turn-off rate of  the MOSFET - - To increase turn off speed, use a separate diode and resistor path for the turn-off edge to have a faster  turn-off edge and a slower turn-on edge

# DRV on off off

**Figure 8-18. DRV gate drive resistor network setup**

Do not - • Use small traces for the power path, use large traces, greater than 40mil (1mm) - - A trace can carry about 0.5A to 1A per 10mil (0.254mm) trace thickness - • Put high voltage traces next to low voltage traces, use a high voltage spacing rule and set a restriction in  layout - • Arbitrarily place grounding points, have a particular power path ground loop and a separate signal ground  loop, tied together near the power stage input bulk capacitor **8.3 Power Supply Recommendations**

The UCC28750 is intended for AC-to-DC adapters and chargers with universal input voltage range of 85 VRMS to 265VRMS, 47Hz to 63Hz, using flyback topology. The UCC28750 can also be used in other applications and converter topologies with different input voltages. In any case, be sure that all voltages and currents are within the recommended operating conditions and absolute maximum ratings of the device. **<https://www.ti.com**>

# UCC28750 SLUSEW0 - DECEMBER 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## 8.4 Layout

## 8.4.1 Layout Guidelines

## To increase the reliability and feasability of the project adhere to the following guidelines on PCB layout with

the UCC28750. These guidelines are general rules that can be followed for any power supply topology and are generally topology-agnostic. The main theme in power supply layouts is to keep the power loops and signal loops as small as possible to avoid coupling of strong signals from one to another and to lower losses caused by additional parasitics that arise from poor layout.

## In a flyback topology, especially the primary which this guidelines are for, there are several loops to pay attention

to and minimize: - • The primary power loop that delivers power to the output - • The snubber loop that absorbs the ringing due to leakage inductances - • The gate drive loop from the device to the gate of the switching device and back to the return - • The auxiliary power loop that rectifies the auxiliary voltage to a steady bias voltage for the UCC28750 - • The feedback loop which carries low-current, sensitive information regarding regulation

## The startup resistor path is not critical, as once startup is complete the path does not deliver significant power

or information. The auxiliary winding takes over as the bias for the UCC28750 instead and is the higher priority power path for the device.

# UCC28750X SOT23-6 DRV

# CS

# VDD

# GND

# FLT

# FB FB

# BULK

# IN

# START

# VDD

# CS

# SLOPE

# NTC

# CS Primary Power Loop Snubber Loop Gate Drive Loop Aux Power Loop Feedback Loop

## Figure 8-19. Simplified Primary Side Schematic Layout Guidelines

**UCC28750** SLUSEW0 - DECEMBER 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

# 8.4.2 Layout Example Primary Power Loop Snubber Loop Gate Drive Loop Aux Power Loop Feedback Loop Drain Bulk Optocoupler

# Figure 8-20. Bottom Layout of the Guidelines Schematic

# Figure 8-21. Top Layout of the Guidelines Schematic, No Traces

## www.ti.com

# UCC28750 SLUSEW0 - DECEMBER 2023

## Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

## 9 Device and Documentation Support

TI offers an extensive line of development tools. Tools and software to evaluate the performance of the device, generate code, and develop solutions are listed below. **9.1 Documentation Support** **9.1.1 Related Documentation**

**9.2 Receiving Notification of Documentation Updates**

To receive notification of documentation updates, navigate to the device product folder on ti.com. Click on *Notifications* to register and receive a weekly digest of any product information that has changed. For change details, review the revision history included in any revised document. **9.3 Support Resources**

TI E2E ™ support forums are an engineer's go-to source for fast, verified answers and design help - straight from the experts. Search existing answers or ask your own question to get the quick design help you need.

Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do not necessarily reflect TI's views; see TI's Terms of Use.

**9.4 Trademarks** TI E2E ™ is a trademark of Texas Instruments. All trademarks are the property of their respective owners. **9.5 Electrostatic Discharge Caution**

This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.

ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may be more susceptible to damage because very small parametric changes could cause the device not to meet its published specifications. **9.6 Glossary**

TI Glossary This glossary lists and explains terms, acronyms, and definitions.

**10 Revision History** NOTE: Page numbers for previous revisions may differ from page numbers in the current version.

# DATE **REVISION** **NOTES** December 2023 \* Initial release

**UCC28750** SLUSEW0 - DECEMBER 2023 **<https://www.ti.com**>

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## 11 Mechanical, Packaging, and Orderable Information

The following pages include mechanical, packaging, and orderable information. This information is the most current data available for the designated devices. This data is subject to change without notice and revision of this document. For browser-based versions of this data sheet, refer to the left-hand navigation. **<https://www.ti.com**>

# UCC28750 SLUSEW0 - DECEMBER 2023

Copyright © 2023 Texas Instruments Incorporated *Submit Document Feedback*

# PACKAGE OPTION ADDENDUM <https://www.ti.com> 9-Nov-2025

# PACKAGING INFORMATION **Orderable part number** **Status** (1) **Material type** (2)

**Package \| Pins** **Package qty \| Carrier** **RoHS** (3) **Lead finish/** **Ball material** (4) **MSL rating/** **Peak reflow** (5) **Op temp (°C)** **Part marking** (6)

UCC287501DBVR Active Production SOT-23 (DBV) \| 6 3000 \| LARGE T&R Yes SN Level-1-260C-UNLIM -40 to 125 U501

UCC287501DBVR.A Active Production SOT-23 (DBV) \| 6 3000 \| LARGE T&R Yes SN Level-1-260C-UNLIM -40 to 125 U501

UCC287502DBVR Active Production SOT-23 (DBV) \| 6 3000 \| LARGE T&R Yes SN Level-2-260C-1 YEAR -40 to 125 U502

UCC287502DBVR.A Active Production SOT-23 (DBV) \| 6 3000 \| LARGE T&R Yes SN Level-2-260C-1 YEAR -40 to 125 U502

UCC287503DBVR Active Production SOT-23 (DBV) \| 6 3000 \| LARGE T&R Yes SN Level-1-260C-UNLIM -40 to 125 U503

UCC287503DBVR.A Active Production SOT-23 (DBV) \| 6 3000 \| LARGE T&R Yes SN Level-1-260C-UNLIM -40 to 125 U503

UCC287504DBVR Active Production SOT-23 (DBV) \| 6 3000 \| LARGE T&R Yes SN Level-1-260C-UNLIM -40 to 125 U504

UCC287504DBVR.A Active Production SOT-23 (DBV) \| 6 3000 \| LARGE T&R Yes SN Level-1-260C-UNLIM -40 to 125 U504

UCC287505DBVR Active Production SOT-23 (DBV) \| 6 3000 \| LARGE T&R Yes SN Level-1-260C-UNLIM -40 to 125 U505

UCC287505DBVR.A Active Production SOT-23 (DBV) \| 6 3000 \| LARGE T&R Yes SN Level-1-260C-UNLIM -40 to 125 U505

UCC287506DBVR Active Production SOT-23 (DBV) \| 6 3000 \| LARGE T&R Yes SN Level-1-260C-UNLIM -40 to 125 U506

UCC287506DBVR.A Active Production SOT-23 (DBV) \| 6 3000 \| LARGE T&R Yes SN Level-1-260C-UNLIM -40 to 125 U506

UCC287507DBVR Active Production SOT-23 (DBV) \| 6 3000 \| LARGE T&R Yes SN Level-1-260C-UNLIM -40 to 125 U507

UCC287507DBVR.A Active Production SOT-23 (DBV) \| 6 3000 \| LARGE T&R Yes SN Level-1-260C-UNLIM -40 to 125 U507

UCC287508DBVR Active Production SOT-23 (DBV) \| 6 3000 \| LARGE T&R Yes SN Level-1-260C-UNLIM -40 to 125 U508

UCC287508DBVR.A Active Production SOT-23 (DBV) \| 6 3000 \| LARGE T&R Yes SN Level-1-260C-UNLIM -40 to 125 U508 **(1)** ** Status: ** For more details on status, see our product life cycle.

**(2)** ** Material type: ** When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance, reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind.

**(3)** ** RoHS values: ** Yes, No, RoHS Exempt. See the TI RoHS Statement for additional information and value definition.

**(4)** ** Lead finish/Ball material: ** Parts may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two lines if the finish value exceeds the maximum column width.

**(5)** ** MSL rating/Peak reflow: ** The moisture sensitivity level ratings and peak solder (reflow) temperatures. In the event that a part has multiple moisture sensitivity ratings, only the lowest level per JEDEC standards is shown. Refer to the shipping label for the actual reflow temperature that will be used to mount the part to the printed circuit board. Addendum-Page 1

# PACKAGE OPTION ADDENDUM <https://www.ti.com> 9-Nov-2025

**(6)** ** Part marking: ** There may be an additional marking, which relates to the logo, the lot trace code information, or the environmental category of the part. Multiple part markings will be inside parentheses. Only one part marking contained in parentheses and separated by a "~" will appear on a part. If a line is indented then it is a continuation of the previous line and the two combined represent the entire part marking for that device. **Important Information and Disclaimer:** The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release. In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis. Addendum-Page 2

# PACKAGE MATERIALS INFORMATION <https://www.ti.com> 22-Jan-2026

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

# UCC287501DBVR SOT-23 DBV 180.0 8.4 3.2 3.2 1.4 4.0 8.0 Q3

# UCC287503DBVR SOT-23 DBV 180.0 8.4 3.2 3.2 1.4 4.0 8.0 Q3

# UCC287504DBVR SOT-23 DBV 180.0 8.4 3.2 3.2 1.4 4.0 8.0 Q3

# UCC287505DBVR SOT-23 DBV 180.0 8.4 3.2 3.2 1.4 4.0 8.0 Q3

# UCC287506DBVR SOT-23 DBV 180.0 8.4 3.2 3.2 1.4 4.0 8.0 Q3

# UCC287507DBVR SOT-23 DBV 180.0 8.4 3.2 3.2 1.4 4.0 8.0 Q3

# UCC287508DBVR SOT-23 DBV 180.0 8.4 3.2 3.2 1.4 4.0 8.0 Q3 Pack Materials-Page 1

# PACKAGE MATERIALS INFORMATION <https://www.ti.com> 22-Jan-2026

# TAPE AND REEL BOX DIMENSIONS ***Width (mm)***

# W

# L

# H \*All dimensions are nominal

**Device** **Package Type** **Package Drawing** **Pins** **SPQ** **Length (mm)** **Width (mm)** **Height (mm)**

| UCC287501DBVR | SOT-23 | DBV | 210.0 | 185.0 | 35.0 |
|:--- |:--- |:--- | ---: | ---: | ---: |
| UCC287503DBVR | SOT-23 | DBV | 210.0 | 185.0 | 35.0 |
| UCC287504DBVR | SOT-23 | DBV | 210.0 | 185.0 | 35.0 |
| UCC287505DBVR | SOT-23 | DBV | 210.0 | 185.0 | 35.0 |
| UCC287506DBVR | SOT-23 | DBV | 210.0 | 185.0 | 35.0 |
| UCC287507DBVR | SOT-23 | DBV | 210.0 | 185.0 | 35.0 |
| UCC287508DBVR | SOT-23 | DBV | 210.0 | 185.0 | 35.0 |

# UCC287503DBVR SOT-23 DBV 210.0 185.0 35.0

# UCC287504DBVR SOT-23 DBV 210.0 185.0 35.0

# UCC287505DBVR SOT-23 DBV 210.0 185.0 35.0

# UCC287506DBVR SOT-23 DBV 210.0 185.0 35.0

# UCC287507DBVR SOT-23 DBV 210.0 185.0 35.0

# UCC287508DBVR SOT-23 DBV 210.0 185.0 35.0 Pack Materials-Page 2 <https://www.ti.com>

# PACKAGE OUTLINE

# C

# 0.22 0.08 TYP 0.25 3.0 2.6

# 2X 0.95

| 1.45 | 0.90 |
|:--- |:--- |
| 0.15 | 0.00 TYP |
| 6X 0.50 | 0.25 |

# 0.15 0.00 TYP

# 6X 0.50 0.25

# 0.6 0.3 TYP 0  TYP 1.9

# 4X 0 -15

# 4X 4 -15

# A 3.05 2.75

# B 1.75 1.45 (1.1)

# SOT-23 - 1.45 mm max height **DBV0006A**

# SMALL OUTLINE TRANSISTOR

# 4214840/G 08/2024

NOTES: 1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M. 2. This drawing is subject to change without notice. 3. Body dimensions do not include mold flash or protrusion. Mold flash and protrusion shall not exceed 0.25 per side. 4. Leads 1,2,3 may be wider than leads 4,5,6 for package orientation. 5. Refernce JEDEC MO-178.

# 0.2 C A B

# INDEX AREA PIN 1

# GAGE PLANE

# SEATING PLANE

# 0.1 C

# SCALE 4.000 <https://www.ti.com>

# EXAMPLE BOARD LAYOUT

# 0.07 MAX ARROUND

# 0.07 MIN ARROUND

# 6X (1.1)

# 6X (0.6) (2.6)

# 2X (0.95)

# (R0.05) TYP

# 4214840/G 08/2024

# SOT-23 - 1.45 mm max height **DBV0006A**

# SMALL OUTLINE TRANSISTOR

NOTES: (continued) 6. Publication IPC-7351 may have alternate designs.  7. Solder mask tolerances between and around signal pads can vary based on board fabrication site.

# SYMM

# LAND PATTERN EXAMPLE EXPOSED METAL SHOWN SCALE:15X

# PKG

# SOLDER MASK OPENING METAL UNDER SOLDER MASK

# SOLDER MASK DEFINED

# EXPOSED METAL

# METAL SOLDER MASK OPENING

# NON SOLDER MASK DEFINED (PREFERRED)

# SOLDER MASK DETAILS

# EXPOSED METAL <https://www.ti.com>

# EXAMPLE STENCIL DESIGN (2.6)

# 2X(0.95)

# 6X (1.1)

# 6X (0.6)

# (R0.05) TYP

# SOT-23 - 1.45 mm max height **DBV0006A**

# SMALL OUTLINE TRANSISTOR

# 4214840/G 08/2024

NOTES: (continued) 8. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate design recommendations. 9. Board assembly site may have different recommendations for stencil design.

# SOLDER PASTE EXAMPLE BASED ON 0.125 mm THICK STENCIL SCALE:15X

# SYMM

# PKG

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