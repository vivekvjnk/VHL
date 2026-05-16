# Using the UCC28881EVM-680

# User's Guide

Literature Number: SLUUBB6A November 2015-Revised December 2015

## User's Guide

*SLUUBB6A-November* * * *2015-Revised* * * *December* * * *2015*

# Offline High-Side Buck Converter

# Evaluation Module (EVM) **Introduction**

The UCC28881EVM-680 evaluation module (EVM) is an offline high-voltage buck-type power supply that provides 13 V DC at a maximum output of 225 mA. The input accepts a voltage range of 85 V AC to 265 V AC. **Description**

The EVM uses the UCC28881 low quiescent current switcher device. This device integrates a 700-V FET and controller into one SOIC7 package. The device also features a high-voltage current source, enabling start-up and operation directly from the rectified mains voltage. The low quiescent current of the device enables very high efficiency in non-isolated high-side buck low-power converter.

The PWM signal generation is based on a maximum constant ON time concept and each ON pulse is followed by a minimum OFF time to ensure the power MOSFET is not continuously driven in the ON state. The PWM signal is AND gated with the signal from a current limiter. The AND gated signal controls the power MOSFET through a driver. Thereby no internal clock is required, and the switching of the power MOSFET is load dependent. The device is also protected from failure conditions with thermal shutdown, under-voltage lockout, soft start and overload protection. Please refer to the UCC28881, ( SLUSC05 ), data sheet for details. ***2.1*** ***Applications***

The UCC28881 is suited for use in non-isolated off-line systems requiring high efficiency and advanced fault protection features. Typical applications include: - • Home Appliances - • White Goods - • E Metering - • Home Automation - • Infrastructure - • LED Lighting

*Offline* * * *High-Side Buck* * * *Converter Evaluation* * * *Module (EVM)* SLUUBB6A-November 2015-Revised December 2015

*Submit Documentation Feedback* Copyright © 2015, Texas Instruments Incorporated <https://www.ti.com> *Description*

## 2.2 ***Features***

The UCC28881EVM-680 features include: - • Single13-V Output - • No Load to 225-mA Load Range - • Universal Off-Line Input Voltage Range - • Overload and Output Short-Circuit Protection - • Controlled Start Up and Restart After Fault Protection

# CAUTION

High voltage levels are present on the evaluation module whenever it is energized. Proper precautions must be taken when working with the EVM. The large bulk capacitors, C1 and C2 must be completely discharged before the EVM can be handled. Serious injury can occur if proper safety precautions are not followed.

## Electrical Performance Specifications

**Table 1. UCC28881EVM-680** ** ** **Electrical** ** ** **Specifications**

# PARAMETER

**DESCRIPTION** **MIN** **TYP** **MAX** **UNITS**

# INPUT CHARACTERISTICS

IN Input voltage 115/230 RMS LINE Line frequency 50/60 Hz

O Output voltage 13-V output target at full load over 12.5 17.9 V line and load output can drift OUT Output current mA OUT Output power 2.9 W

TR Operating temperature range IOUT < or = 225 mA °C OR Output ripple voltage mV

ƞ Efficiency $$ IOUT = 225 mA, VIN = 230 V/115 V $$ 80%

SLUUBB6A-November 2015-Revised December 2015 *Offline* * * *High-Side Buck* * * *Converter Evaluation* * * *Module (EVM)* *Submit Documentation Feedback*

Copyright © 2015, Texas Instruments Incorporated

# 1000V

# D1

# 600V

# D4

# L2 1 mH 121k

# R3 10.0k R2 8.2

# 3W

# R1 0.1µF C3 330µF C5

# GND

# P2 282841-2

# TP3

# TP2

# TP5

# D3 0.015µF C4

# TP4

# JP1

# R4

# 1000V

# D2

# L

# N

# 85-265VAC 1A

# 13VDC 225mA

# GND

# GND

# FB

# VDD HVIN

# NC

# DRAIN

# U1

# UCC28881DR

# P1 282841-2

# TP1 1mH

# L1

# DANGER, HIGH VOLTAGE 10µF C1 10µF C2

# C6

# J1

# 923345-03-C

# VIN+

# VIN

# VO+

# VO

# 16V

# D5

# Schematic <https://www.ti.com>

# Schematic

# No parametric value means the device is not populated.

# Figure 1. UCC28881EVM-680 Power Stage Schematic

# Offline High-Side Buck Converter Evaluation Module (EVM) SLUUBB6A-November 2015-Revised December 2015

# Submit Documentation Feedback

Copyright © 2015, Texas Instruments Incorporated

<https://www.ti.com> *Circuit* * * *Description* **Circuit Description**

The UCC28881EVM-680 is a non-isolated AC-to-DC high-side buck configuration with direct feedback. The EVM, on the input side, has a half-wave rectifier assembled for rectification of AC-to-DC, followed by an EMI filter.

**NOTE:** The GND node is one diode drop (D2) above the input neutral (N) node.

In addition to the UCC28881 device, the EVM holds the following key components: - • A Half-Wave Rectifier (D1, D2) - • EMI Filter (L1, C1, C2) - • Freewheeling Diode (D4) - • 16-V Zener Clamp to Regulate no Load Output Voltage (D5) - • Inductor (L2) - • Load Capacitor (C5) - • Feedback Path (C4, D3, R2, R3, R4, JP1) - • VAC Input Connector (P1) - • VDC Output Connector (P2) **Test** ** ** **Points**

**Table 2. UCC28881EVM-680** ** ** **Test Points**

| DESIGNATOR | DESCRIPTION |
|:--- |:--- |
| TP1 | Buck switch node |
| TP2 | High voltage rectified DC |
| TP3 | GND |
| TP4 | GND |
| TP5 | VOUT | TP1 Buck switch node TP2 High voltage rectified DC

# TP3 GND

# TP4 GND

# TP5 VOUT

SLUUBB6A-November 2015-Revised December 2015 *Offline* * * *High-Side Buck* * * *Converter Evaluation* * * *Module (EVM)* *Submit Documentation Feedback*

Copyright © 2015, Texas Instruments Incorporated

*Recommended* * * *Basic* * * *Test* * * *Equipment* <https://www.ti.com>

**Recommended Basic** ** ** **Test Equipment**

**AC Input Source:** The input source is an isolated variable AC source capable of supplying between 85 V RMS and 265 V RMS at no less than 5 W and connected as shown in Figure 2. For accurate efficiency calculations, a power meter (PM1) should be inserted between the AC source and the EVM. For highest accuracy, connect the voltage terminals of the power meter directly across the power source.

**NOTE:** Connecting the voltage terminals directly to the EVM results in a small current error. This is very significant when measuring no-load power.

**Load** ** ** **(R1):** The UCC28881EVM-680 is capable of delivering 225 mA of output current.

**NOTE:** The output is not isolated from the AC and the electronic load must be capable of operating from a high-voltage input.

**Power Meter (PM1):** The power analyzer (PM1) is capable of measuring low-input current, typically less than 100 μ A, and a long averaging mode if low-power standby mode input power measurements are to be taken. An example of such an analyzer is the Yokogawa WT210 Digital Power Meter.

**Multimeters (V1, V2, A1 ):** Three digital multimeters are used to measure the regulated output voltage and load current.

**Oscilloscope:** A digital or analog oscilloscope with a 500-MHz scope probe is recommended.

**Recommended Wire Gauge:** A minimum of AWG 24 wire is recommended. The wire connections between the AC source and the EVM, and the wire connections between the EVM and the load should be less than two feet long.

*Offline* * * *High-Side Buck* * * *Converter Evaluation* * * *Module (EVM)* SLUUBB6A-November 2015-Revised December 2015

*Submit Documentation Feedback* Copyright © 2015, Texas Instruments Incorporated

# V1

# AC

# R1 Oscilloscope

# PM1

# V1 A1 A2

# V2 1 ohm

# PM1

# A <https://www.ti.com> *Test* * * *Setup* **Test** ** ** **Setup** **Figure 2. Test Setup**

**Power** ** ** **On/Off** ** ** **Procedure** 1. The EVM should only be handled by persons trained in the design/testing and evaluation of offline

power supplies. (a) Offline voltage 0 V RMS to 265 V RMS (b) DC voltages up to 380 V DC 2. All necessary connections must be made before applying power. 3. After the EVM is powered down, monitor the voltage across the high-voltage DC bulk voltage. (a) This is the voltage across TP2 and TP3.

**NOTE:** Do not handle this EVM or disconnect the setup if the voltage across these pins are greater than 50 V DC or if the AC voltage is still applied to the EVM.

SLUUBB6A-November 2015-Revised December 2015 *Offline* * * *High-Side Buck* * * *Converter Evaluation* * * *Module (EVM)* *Submit Documentation Feedback*

Copyright © 2015, Texas Instruments Incorporated Output Power (W) Efficiency (%) 0.3 0.6 0.9 1.2 1.5 1.8 2.1 2.4 2.7

# D001

# 115V AC 230V AC *Test* * * *Data* <https://www.ti.com>

## Test Data

## 10.1

***Line/Load*** *** *** ***Regulation and*** *** *** ***Efficiency*** *** *** ***Test Data***

## Table 3. Line/Load Regulations and Efficiency Test Data

# OUT

**LOAD** **IN** **OUT** **OUT** **IN** **EFFICIENCY**

| 0% | 0.000 | 16.510 | 0.000 | 0.315(1) | 0% |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 10% | 0.022 | 15.501 | 0.022 | 0.403 | 85% |
| 22% | 0.050 | 13.849 | 0.050 | 0.847 | 82% |
| 33% | 0.075 | 13.400 | 0.075 | 1.238 | 81% |
| 44% | 0.100 | 13.174 | 0.100 | 1.623 | 81% |
| 67% | 0.150 | 12.949 | 0.150 | 2.412 | 81% |
| 100% | 0.225 | 12.795 | 0.225 | 3.599 | 80% |
| 0% | 0.000 | 16.515 | 0.000 | 0.361(1) | 0% |
| 10% | 0.022 | 15.610 | 0.022 | 0.441 | 78% |
| 22% | 0.050 | 13.901 | 0.050 | 0.872 | 80% |
| 33% | 0.075 | 13.438 | 0.075 | 1.256 | 80% |
| 44% | 0.100 | 13.201 | 0.100 | 1.636 | 81% |
| 67% | 0.150 | 12.971 | 0.150 | 2.402 | 81% |
| 100% | 0.225 | 12.822 | 0.225 | 3.581 | 81% | 10% 0.022 15.501 0.022 0.403 85% 22% 0.050 13.849 0.050 0.847 82% 33% 0.075 13.400 0.075 1.238 81% 44% 0.100 13.174 0.100 1.623 81% 67% 0.150 12.949 0.150 2.412 81% 100% 0.225 12.795 0.225 3.599 80% 0% 0.000 16.515 0.000 0.361 (1) 0% 10% 0.022 15.610 0.022 0.441 78% 22% 0.050 13.901 0.050 0.872 80% 33% 0.075 13.438 0.075 1.256 80% 44% 0.100 13.201 0.100 1.636 81% 67% 0.150 12.971 0.150 2.402 81% 100% 0.225 12.822 0.225 3.581 81%

(1) Power dissipation at no load is mostly due to Zener clamp D5. This Zener diode is required to keep the output in regulation under no load conditions, due to the sample and hold technique that was used in this design. The power dissipation of D5 under no load is roughly 300 mW.

## Figure 3. Efficiency Graph

*Offline* * * *High-Side Buck* * * *Converter Evaluation* * * *Module (EVM)* SLUUBB6A-November 2015-Revised December 2015

*Submit Documentation Feedback* Copyright © 2015, Texas Instruments Incorporated <https://www.ti.com> *Test* * * *Data*

## 10.2 ***Transient*** *** *** ***Response***

# CH1 = VOUT

| Figure 4. VIN = 85 VRMS, IOUT = 0 A | Figure 5. VIN = 85 V, IOUT = 225 mA |
|:--- |:--- |
| Figure 6. VIN = 265 VRMS, IOUT = 0 A | Figure 7. VIN = 265 V, IOUT = 225 mA |
| 10.3 | Load Transient Response |

Figure 6. VIN = 265 VRMS, IOUT = 0 A Figure 7. VIN = 265 V, IOUT = 225 mA

## 10.3

***Load*** *** *** ***Transient*** *** *** ***Response***

# CH1 = VOUT, CH4 = IOUT, 500 mA/10 mV

## Load step 0.022 A to 0.225 A Figure 8. VIN = 85 V Figure 9. VIN = 265 VRMS

SLUUBB6A-November 2015-Revised December 2015 *Offline* * * *High-Side Buck* * * *Converter Evaluation* * * *Module (EVM)* *Submit Documentation Feedback*

Copyright © 2015, Texas Instruments Incorporated *Test* * * *Data* <https://www.ti.com>

## 10.4 ***Output Ripple Voltage***

# CH1 = VOUT

Figure 10. VIN = 85 V, IOUT = 0 A Figure 11. VIN = 85 V, IOUT = 0.225 A

Figure 12. VIN = 265 V, IOUT = 0 A Figure 13. VIN = 265 V, IOUT = 0.225 A

*Offline* * * *High-Side Buck* * * *Converter Evaluation* * * *Module (EVM)* SLUUBB6A-November 2015-Revised December 2015

*Submit Documentation Feedback* Copyright © 2015, Texas Instruments Incorporated <https://www.ti.com> *Test* * * *Data* ***10.5*** ***Audible Noise***

When evaluating this EVM it's apparent that at full load the EVM runs quiet, but as the load decreases the EVM becomes noticeably audible. This is because the converter at full load operates with an inductor ripple current frequency/output ripple voltage at frequency of roughly 22 kHz, which is out of the audible range for most humans. However as load decreases the inductor goes heavy into discontinuous mode operation and the output frequency drops. When the output frequency drops below 18 kHz to 16 kHz, audible noise can be heard. To illustrate this behavior the scope plots of Figure 14 (Full Load) and Figure 15 (60% Load) were taken. Ch1 is the output voltage of the EVM, where CH4 is the inductor (L2) current (500 mA/10 mV). At full load the inductor ripple and output ripple voltage run at a frequency of roughly 22 kHz ( Figure 14 ), which is not audible. However, as the load decreases the inductor ripple and output ripple frequency decreases to the point where the EVM enters the audible frequency range and is audible ( Figure 15 ).

**NOTE:** It is normal for this control methodology to become audible as the load decreases. It is more suited for end products that operate heavily loaded (75% to 100%) and no load.

Figure 14. IOUT = 225 mA Figure 15. IOUT = 138 mA

SLUUBB6A-November 2015-Revised December 2015 *Offline* * * *High-Side Buck* * * *Converter Evaluation* * * *Module (EVM)* *Submit Documentation Feedback*

Copyright © 2015, Texas Instruments Incorporated

*Assembly* * * *Drawing/Layout* <https://www.ti.com>

## Assembly Drawing/Layout

## Figure 16. UCC28881EVM-680 Assembly Drawing/Layout

*Offline* * * *High-Side Buck* * * *Converter Evaluation* * * *Module (EVM)* SLUUBB6A-November 2015-Revised December 2015

*Submit Documentation Feedback* Copyright © 2015, Texas Instruments Incorporated

<https://www.ti.com> *List* * * *of* * * *Materials*

## List of Materials

## Table 4. UCC28881EVM-680 List of Materials

# QTY

**DES** **DESCRIPTION** **PART NUMBER** **MANUFACTURER**

C1, C2 Capacitor, aluminum, 10 µF, 450 V, \pm20%, 2.864788 Ω, EEUED2W100 Panasonic TH

C3 Capacitor, ceramic, 0.1 µF, 50 V, \pm10%, X7R, 0805 C0805C104K5RACTU Kemet

C4 Capacitor, ceramic, 0.015 µF, 50 V, \pm10%, X7R, 0805 C0805C153K5RACTU Kemet

C5 Capacitor, aluminum, 330 µF, 35 V, \pm20%, 0.03 Ω, TH EEU-FM1V331L Panasonic

C6 Capacitor, ceramic, 0.01 µF, 100 V, \pm10%, X7R, 0805 C0805C103K1RACTU Kemet

D1, D2 Diode, P-N, 1000 V, 1 A, TH 1N4007 Fairchild Semiconductor

| D3 | Diode, standard recovery rectifier, 600 V, 1 A, TH | 1N4006-T | Diodes Inc. |
|:--- |:--- |:--- |:--- |
| D4 | Diode, ultrafast, 600 V, 1 A, SMA | STTH1R06A | ST Microelectronics |
| D5 | Diode, Zener, 16 V, 500 mW, SOD-123 | MMSZ4703T1G | ON Semiconductor |

D4 Diode, ultrafast, 600 V, 1 A, SMA STTH1R06A ST Microelectronics

D5 Diode, Zener, 16 V, 500 mW, SOD-123 MMSZ4703T1G ON Semiconductor

H1, H2, Bumpon, hemisphere, 0.44 inch x 0.20 inch, clear SJ-5303 (CLEAR) 3M H3, H4

J1 Jumper wire, 300 mil spacing, orange, pkg of 200 923345-03-C 3M

JP1 Header, TH, 100 mil, 2 inch x 1 inch, gold plated, 230 mil TSW-102-07-G-S Samtec above insulator

L1 Inductor, wirewound, ferrite, 1 mH, 0.2 A, 2.3 Ω, TH 5800-102-RC Bourns

L2 Inductor, wirewound, ferrite, 1 mH, 0.4 A, 1.2 Ω, TH Wurth Elektronik

| P1, P2 | Terminal block, 2 inch x 1 inch, 5.08 mm, TH | 282841-2 | TE Connectivity |
|:--- |:--- |:--- |:--- |
| R1 | Resistor, 8.2 Ω, 5%, 3 W, fusible, TH | PWR4522AS8R20JA | Bourns |
| R2 | Resistor, 10.0 kΩ, 1%, 0.125 W, 0805 | ERJ-6ENF1002V | Panasonic |
| R3 | Resistor, 121 kΩ, 1%, 0.125 W, 0805 | ERJ-6ENF1213V | Panasonic |
| R4 | Resistor, 61.9 kΩ, 1%, 0.125 W, 0805 | ERJ-6ENF6192V | Panasonic |

R1 Resistor, 8.2 Ω, 5%, 3 W, fusible, TH PWR4522AS8R20JA Bourns

R2 Resistor, 10.0 k\Omega, 1%, 0.125 W, 0805 ERJ-6ENF1002V Panasonic

R3 Resistor, 121 k\Omega, 1%, 0.125 W, 0805 ERJ-6ENF1213V Panasonic

R4 Resistor, 61.9 k\Omega, 1%, 0.125 W, 0805 ERJ-6ENF6192V Panasonic

SH-JP1 Shunt, 100 mil, flash gold, black 1 inch x 2 inch SPC02SYAN Sullins Connector Solutions

| TP1, TP2 | Test point, miniature, red, TH | Keystone |
|:--- |:--- |:--- |
| TP3, TP4 | Test point, miniature, black, TH | Keystone |
| TP5 | Test point, miniature, white, TH | Keystone |

TP3, TP4 Test point, miniature, black, TH Keystone TP5 Test point, miniature, white, TH Keystone

U1 700-V Lowest Quiescent Current Off-Line Switcher, UCC28881DR Texas Instruments D0007A PCB Printed circuit board PWR680 Any

## Revision History

**Changes** ** ** **from** ** ** **Original** ** ** **(November** ** ** **2015) to** ** ** **A** ** ** **Revision**................................................................................................ ** ** **Page**

- • Changed output voltage MIN and MAX specifications................................................................................ 3 - • Added power dissipation note...........................................................................................................

NOTE: Page numbers for previous revisions may differ from page numbers in the current version.

SLUUBB6A-November 2015-Revised December 2015 *Revision History* *Submit Documentation Feedback*

Copyright © 2015, Texas Instruments Incorporated

# STANDARD TERMS AND CONDITIONS FOR EVALUATION MODULES

1. *Delivery:* TI delivers TI evaluation boards, kits, or modules, including any accompanying demonstration software, components, or documentation (collectively, an "EVM" or "EVMs") to the User ("User") in accordance with the terms and conditions set forth herein. Acceptance of the EVM is expressly subject to the following terms and conditions.

1.1 EVMs are intended solely for product or software developers for use in a research and development setting to facilitate feasibility evaluation, experimentation, or scientific analysis of TI semiconductors products. EVMs have no direct function and are not finished products. EVMs shall not be directly or indirectly assembled as a part or subassembly in any finished product. For clarification, any software or software tools provided with the EVM ("Software") shall not be subject to the terms and conditions set forth herein but rather shall be subject to the applicable terms and conditions that accompany such Software

1.2 EVMs are not intended for consumer or household use. EVMs may not be sold, sublicensed, leased, rented, loaned, assigned, or otherwise distributed for commercial purposes by Users, in whole or in part, or used in any finished product or production system.

*Limited* * * *Warranty and Related* * * *Remedies/Disclaimers*:

2.1 These terms and conditions do not apply to Software. The warranty, if any, for Software is covered in the applicable Software License Agreement.

2.2 TI warrants that the TI EVM will conform to TI's published specifications for ninety (90) days after the date TI delivers such EVM to User. Notwithstanding the foregoing, TI shall not be liable for any defects that are caused by neglect, misuse or mistreatment by an entity other than TI, including improper installation or testing, or for any EVMs that have been altered or modified in any way by an entity other than TI. Moreover, TI shall not be liable for any defects that result from User's design, specifications or instructions for such EVMs. Testing and other quality control techniques are used to the extent TI deems necessary or as mandated by government requirements. TI does not test all parameters of each EVM.

2.3 If any EVM fails to conform to the warranty set forth above, TI's sole liability shall be at its option to repair or replace such EVM, or credit User's account for such EVM. TI's liability under this warranty shall be limited to EVMs that are returned during the warranty period to the address designated by TI and that are determined by TI not to conform to such warranty. If TI elects to repair or replace such EVM, TI shall have a reasonable time to repair such EVM or provide replacements. Repaired EVMs shall be warranted for the remainder of the original warranty period. Replaced EVMs shall be warranted for a new full ninety (90) day warranty period. *Regulatory Notices:* 3.1 *United States*

3.1.1 *Notice applicable* * * *to EVMs not FCC-Approved:*

This kit is designed to allow product developers to evaluate electronic components, circuitry, or software associated with the kit to determine whether to incorporate such items in a finished product and software developers to write software applications for use with the end product. This kit is not a finished product and when assembled may not be resold or otherwise marketed unless all required FCC equipment authorizations are first obtained. Operation is subject to the condition that this product not cause harmful interference to licensed radio stations and that this product accept harmful interference. Unless the assembled kit is designed to operate under part 15, part 18 or part 95 of this chapter, the operator of the kit must operate under the authority of an FCC license holder or must secure an experimental authorization under part 5 of this chapter.

3.1.2 *For EVMs annotated* * * *as* * * *FCC* * * *- FEDERAL COMMUNICATIONS* * * *COMMISSION Part* * * *15* * * *Compliant:*

# CAUTION

This device complies with part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

Changes or modifications not expressly approved by the party responsible for compliance could void the user's authority to operate the equipment.

**FCC Interference** ** ** **Statement** ** ** **for** ** ** **Class** ** ** **A** ** ** **EVM devices**

*NOTE:* * * *This* * * *equipment* * * *has* * * *been* * * *tested* * * *and* * * *found* * * *to* * * *comply* * * *with* * * *the* * * *limits* * * *for* * * *a* * * *Class* * * *A* * * *digital* * * *device,* * * *pursuant* * * *to* * * *part* * * *15* * * *of* *the* * * *FCC* * * *Rules.* * * *These* * * *limits* * * *are* * * *designed* * * *to* * * *provide* * * *reasonable* * * *protection* * * *against* * * *harmful* * * *interference* * * *when* * * *the* * * *equipment* * * *is* *operated* * * *in* * * *a* * * *commercial* * * *environment.* * * *This* * * *equipment* * * *generates,* * * *uses,* * * *and* * * *can* * * *radiate* * * *radio* * * *frequency* * * *energy* * * *and,* * * *if* * * *not* *installed* * * *and* * * *used* * * *in* * * *accordance* * * *with* * * *the* * * *instruction* * * *manual,* * * *may* * * *cause* * * *harmful* * * *interference* * * *to* * * *radio* * * *communications.* *Operation* * * *of* * * *this* * * *equipment* * * *in* * * *a* * * *residential* * * *area* * * *is* * * *likely* * * *to* * * *cause* * * *harmful* * * *interference* * * *in* * * *which* * * *case* * * *the* * * *user* * * *will* * * *be* * * *required* * * *to* *correct* * * *the interference at his own expense.*

# SPACER

# SPACER

# SPACER

# SPACER

# SPACER

# SPACER

# SPACER

# SPACER

**FCC Interference** ** ** **Statement** ** ** **for** ** ** **Class** ** ** **B** ** ** **EVM devices**

*NOTE:* * * *This* * * *equipment* * * *has* * * *been* * * *tested* * * *and* * * *found* * * *to* * * *comply* * * *with* * * *the* * * *limits* * * *for* * * *a* * * *Class* * * *B* * * *digital* * * *device,* * * *pursuant* * * *to* * * *part* * * *15* * * *of* *the* * * *FCC* * * *Rules.* * * *These* * * *limits* * * *are* * * *designed* * * *to* * * *provide* * * *reasonable* * * *protection* * * *against* * * *harmful* * * *interference* * * *in* * * *a* * * *residential* *installation. This equipment generates, uses* * * *and can* * * *radiate* * * *radio frequency energy* * * *and, if not installed* * * *and used in accordance* *with* * * *the* * * *instructions,* * * *may* * * *cause* * * *harmful* * * *interference* * * *to* * * *radio* * * *communications.* * * *However,* * * *there* * * *is* * * *no* * * *guarantee* * * *that* * * *interference* *will* * * *not* * * *occur* * * *in* * * *a* * * *particular* * * *installation.* * * *If* * * *this* * * *equipment* * * *does* * * *cause* * * *harmful* * * *interference* * * *to* * * *radio* * * *or* * * *television* * * *reception,* * * *which* *can* * * *be* * * *determined* * * *by* * * *turning* * * *the* * * *equipment* * * *off* * * *and* * * *on,* * * *the* * * *user* * * *is* * * *encouraged* * * *to* * * *try* * * *to* * * *correct* * * *the* * * *interference* * * *by* * * *one* * * *or* * * *more* *of the following measures:*

- * * *Reorient or relocate* * * *the receiving* * * *antenna.* - * * *Increase the separation between the equipment and receiver.* - * * *Connect the equipment into* * * *an* * * *outlet on* * * *a* * * *circuit different from that* * * *to which* * * *the receiver* * * *is* * * *connected.* - * * *Consult the dealer or an* * * *experienced* * * *radio/TV* * * *technician* * * *for* * * *help.* 3.2 * * *Canada*

3.2.1 *For EVMs issued* * * *with* * * *an* * * *Industry Canada* * * *Certificate of Conformance* * * *to RSS-210*

**Concerning EVMs** ** ** **Including** ** ** **Radio Transmitters:**

This device complies with Industry Canada license-exempt RSS standard(s). Operation is subject to the following two conditions: (1) this device may not cause interference, and (2) this device must accept any interference, including interference that may cause undesired operation of the device.

**Concernant** ** ** **les EVMs** ** ** **avec appareils** ** ** **radio:**

Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes: (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

**Concerning EVMs** ** ** **Including** ** ** **Detachable** ** ** **Antennas:**

Under Industry Canada regulations, this radio transmitter may only operate using an antenna of a type and maximum (or lesser) gain approved for the transmitter by Industry Canada. To reduce potential radio interference to other users, the antenna type and its gain should be so chosen that the equivalent isotropically radiated power (e.i.r.p.) is not more than that necessary for successful communication. This radio transmitter has been approved by Industry Canada to operate with the antenna types listed in the user guide with the maximum permissible gain and required antenna impedance for each antenna type indicated. Antenna types not included in this list, having a gain greater than the maximum gain indicated for that type, are strictly prohibited for use with this device.

**Concernant** ** ** **les EVMs** ** ** **avec antennes** ** ** **détachables**

Conformément à la réglementation d'Industrie Canada, le présent émetteur radio peut fonctionner avec une antenne d'un type et d'un gain maximal (ou inférieur) approuvé pour l'émetteur par Industrie Canada. Dans le but de réduire les risques de brouillage radioélectrique à l'intention des autres utilisateurs, il faut choisir le type d'antenne et son gain de sorte que la puissance isotrope rayonnée équivalente (p.i.r.e.) ne dépasse pas l'intensité nécessaire à l'établissement d'une communication satisfaisante. Le présent émetteur radio a été approuvé par Industrie Canada pour fonctionner avec les types d'antenne énumérés dans le manuel d'usage et ayant un gain admissible maximal et l'impédance requise pour chaque type d'antenne. Les types d'antenne non inclus dans cette liste, ou dont le gain est supérieur au gain maximal indiqué, sont strictement interdits pour l'exploitation de l'émetteur 3.3 * * *Japan*

3.3.1 *Notice* * * *for* * * *EVMs* * * *delivered* * * *in* * * *Japan:* Please see <http://www.tij.co.jp/lsds/ti\_ja/general/eStore/notice\_01.page> 日本国内に 輸入される評価用キット、ボードについては、次のところをご覧ください。 <http://www.tij.co.jp/lsds/ti\_ja/general/eStore/notice\_01.page>

3.3.2 *Notice* * * *for* * * *Users* * * *of* * * *EVMs* * * *Considered* * * *"Radio* * * *Frequency* * * *Products"* * * *in* * * *Japan:* EVMs entering Japan may not be certified by TI as conforming to Technical Regulations of Radio Law of Japan.

If User uses EVMs in Japan, not certified to Technical Regulations of Radio Law of Japan, User is required by Radio Law of Japan to follow the instructions below with respect to EVMs:

1. Use EVMs in a shielded room or any other test facility as defined in the notification #173 issued by Ministry of Internal Affairs and Communications on March 28, 2006, based on Sub-section 1.1 of Article 6 of the Ministry's Rule for Enforcement of Radio Law of Japan, 2. Use EVMs only after User obtains the license of Test Radio Station as provided in Radio Law of Japan with respect to EVMs, or 3. Use of EVMs only after User obtains the Technical Regulations Conformity Certification as provided in Radio Law of Japan with respect to EVMs. Also, do not transfer EVMs, unless User gives the same notice above to the transferee. Please note that if User does not follow the instructions above, User will be subject to penalties of Radio Law of Japan.

# SPACER

# SPACER

# SPACER

# SPACER

# SPACER

【無線電波を送信する製品の開発キットをお使いになる際の注意事項】開発キットの中には技術基準適合証明を受けて

いないものがあります。技術適合証明を受けていないもののご使用に際しては、電波法遵守のため、以下のいずれかの 措置を取っていただく必要がありますのでご注意ください。

1. 電波法施行規則第 6 条第 1 項第 1 号に基づく平成 18 年 3 月 28 日総務省告示第 173 号で定められた電波暗室等の試験設備でご使用 いただく。 2. 実験局の免許を取得後ご使用いただく。 3. 技術基準適合証明を取得後ご使用いただく。

なお、本製品は、上記の「ご使用にあたっての注意」を譲渡先、移転先に通知しない限り、譲渡、移転できないものとします。

上記を遵守頂けない場合は、電波法の罰則が適用される可能性があることをご留意ください。日本テキサス・イ ンスツルメンツ株式会社 東京都新宿区西新宿６丁目２４番１号 西新宿三井ビル

3.3.3 *Notice for* * * *EVMs for* * * *Power Line* * * *Communication:* Please see <http://www.tij.co.jp/lsds/ti\_ja/general/eStore/notice\_02.page>

電力線搬送波通信についての開発キットをお使いになる際の注意事項については、次のところをご覧くださ い。 <http://www.tij.co.jp/lsds/ti\_ja/general/eStore/notice\_02.page>

# SPACER *EVM Use Restrictions* * * *and Warnings:*

# 4.1 EVMS ARE NOT FOR USE IN FUNCTIONAL SAFETY AND/OR SAFETY CRITICAL EVALUATIONS, INCLUDING BUT NOT

# LIMITED TO EVALUATIONS OF LIFE SUPPORT APPLICATIONS.

4.2 User must read and apply the user guide and other available documentation provided by TI regarding the EVM prior to handling

or using the EVM, including without limitation any warning or restriction notices. The notices contain important safety information related to, for example, temperatures and voltages.

4.3 * * *Safety-Related Warnings* * * *and Restrictions:*

4.3.1 User shall operate the EVM within TI's recommended specifications and environmental considerations stated in the user guide, other available documentation provided by TI, and any other applicable requirements and employ reasonable and customary safeguards. Exceeding the specified performance ratings and specifications (including but not limited to input and output voltage, current, power, and environmental ranges) for the EVM may cause personal injury or death, or property damage. If there are questions concerning performance ratings and specifications, User should contact a TI field representative prior to connecting interface electronics including input power and intended loads. Any loads applied outside of the specified output range may also result in unintended and/or inaccurate operation and/or possible permanent damage to the EVM and/or interface electronics. Please consult the EVM user guide prior to connecting any load to the EVM output. If there is uncertainty as to the load specification, please contact a TI field representative. During normal operation, even with the inputs and outputs kept within the specified allowable ranges, some circuit components may have elevated case temperatures. These components include but are not limited to linear regulators, switching transistors, pass transistors, current sense resistors, and heat sinks, which can be identified using the information in the associated documentation. When working with the EVM, please be aware that the EVM may become very warm.

4.3.2 EVMs are intended solely for use by technically qualified, professional electronics experts who are familiar with the dangers and application risks associated with handling electrical mechanical components, systems, and subsystems. User assumes all responsibility and liability for proper and safe handling and use of the EVM by User or its employees, affiliates, contractors or designees. User assumes all responsibility and liability to ensure that any interfaces (electronic and/or mechanical) between the EVM and any human body are designed with suitable isolation and means to safely limit accessible leakage currents to minimize the risk of electrical shock hazard. User assumes all responsibility and liability for any improper or unsafe handling or use of the EVM by User or its employees, affiliates, contractors or designees.

4.4 User assumes all responsibility and liability to determine whether the EVM is subject to any applicable international, federal,

state, or local laws and regulations related to User's handling and use of the EVM and, if applicable, User assumes all responsibility and liability for compliance in all respects with such laws and regulations. User assumes all responsibility and liability for proper disposal and recycling of the EVM consistent with all applicable international, federal, state, and local requirements.

5. *Accuracy* * * *of* * * *Information:* To the extent TI provides information on the availability and function of EVMs, TI attempts to be as accurate as possible. However, TI does not warrant the accuracy of EVM descriptions, EVM availability or other information on its websites as accurate, complete, reliable, current, or error-free.

# SPACER

# SPACER

# SPACER

# SPACER

# SPACER

# SPACER

# SPACER 6. *Disclaimers:*

# 6.1 EXCEPT AS SET FORTH ABOVE, EVMS AND ANY WRITTEN DESIGN MATERIALS PROVIDED WITH THE EVM (AND THE

# DESIGN OF THE EVM ITSELF) ARE PROVIDED "AS IS" AND "WITH ALL FAULTS." TI DISCLAIMS ALL OTHER

WARRANTIES, EXPRESS OR IMPLIED, REGARDING SUCH ITEMS, INCLUDING BUT NOT LIMITED TO ANY IMPLIED WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF ANY THIRD PARTY PATENTS, COPYRIGHTS, TRADE SECRETS OR OTHER INTELLECTUAL PROPERTY RIGHTS.

# 6.2 EXCEPT FOR THE LIMITED RIGHT TO USE THE EVM SET FORTH HEREIN, NOTHING IN THESE TERMS AND

# CONDITIONS SHALL BE CONSTRUED AS GRANTING OR CONFERRING ANY RIGHTS BY LICENSE, PATENT, OR ANY

OTHER INDUSTRIAL OR INTELLECTUAL PROPERTY RIGHT OF TI, ITS SUPPLIERS/LICENSORS OR ANY OTHER THIRD PARTY, TO USE THE EVM IN ANY FINISHED END-USER OR READY-TO-USE FINAL PRODUCT, OR FOR ANY INVENTION, DISCOVERY OR IMPROVEMENT MADE, CONCEIVED OR ACQUIRED PRIOR TO OR AFTER DELIVERY OF THE EVM.

# 7.

*USER'S* * * *INDEMNITY* * * *OBLIGATIONS* * * *AND* * * *REPRESENTATIONS.* USER WILL DEFEND, INDEMNIFY AND HOLD TI, ITS LICENSORS AND THEIR REPRESENTATIVES HARMLESS FROM AND AGAINST ANY AND ALL CLAIMS, DAMAGES, LOSSES, EXPENSES, COSTS AND LIABILITIES (COLLECTIVELY, "CLAIMS") ARISING OUT OF OR IN CONNECTION WITH ANY HANDLING OR USE OF THE EVM THAT IS NOT IN ACCORDANCE WITH THESE TERMS AND CONDITIONS. THIS OBLIGATION SHALL APPLY WHETHER CLAIMS ARISE UNDER STATUTE, REGULATION, OR THE LAW OF TORT, CONTRACT OR ANY OTHER LEGAL THEORY, AND EVEN IF THE EVM FAILS TO PERFORM AS DESCRIBED OR EXPECTED.

8. *Limitations* * * *on* * * *Damages and Liability:*

# 8.1 General Limitations. IN NO EVENT SHALL TI BE LIABLE FOR ANY SPECIAL, COLLATERAL, INDIRECT, PUNITIVE,

# INCIDENTAL, CONSEQUENTIAL, OR EXEMPLARY DAMAGES IN CONNECTION WITH OR ARISING OUT OF THESE

TERMS ANDCONDITIONS OR THE USE OF THE EVMS PROVIDED HEREUNDER, REGARDLESS OF WHETHER TI HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. EXCLUDED DAMAGES INCLUDE, BUT ARE NOT LIMITED TO, COST OF REMOVAL OR REINSTALLATION, ANCILLARY COSTS TO THE PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES, RETESTING, OUTSIDE COMPUTER TIME, LABOR COSTS, LOSS OF GOODWILL, LOSS OF PROFITS, LOSS OF SAVINGS, LOSS OF USE, LOSS OF DATA, OR BUSINESS INTERRUPTION. NO CLAIM, SUIT OR ACTION SHALL BE BROUGHT AGAINST TI MORE THAN ONE YEAR AFTER THE RELATED CAUSE OF ACTION HAS OCCURRED.

# 8.2 Specific Limitations. IN NO EVENT SHALL TI'S AGGREGATE LIABILITY FROM ANY WARRANTY OR OTHER OBLIGATION

# ARISING OUT OF OR IN CONNECTION WITH THESE TERMS AND CONDITIONS, OR ANY USE OF ANY TI EVM

PROVIDED HEREUNDER, EXCEED THE TOTAL AMOUNT PAID TO TI FOR THE PARTICULAR UNITS SOLD UNDER THESE TERMS AND CONDITIONS WITH RESPECT TO WHICH LOSSES OR DAMAGES ARE CLAIMED. THE EXISTENCE OF MORE THAN ONE CLAIM AGAINST THE PARTICULAR UNITS SOLD TO USER UNDER THESE TERMS AND CONDITIONS SHALL NOT ENLARGE OR EXTEND THIS LIMIT.

9. *Return* * * *Policy.* Except as otherwise provided, TI does not offer any refunds, returns, or exchanges. Furthermore, no return of EVM(s) will be accepted if the package has been opened and no return of the EVM(s) will be accepted if they are damaged or otherwise not in a resalable condition. If User feels it has been incorrectly charged for the EVM(s) it ordered or that delivery violates the applicable order, User should contact TI. All refunds will be made in full within thirty (30) working days from the return of the components(s), excluding any postage or packaging costs.

10. *Governing* * * *Law:* These terms and conditions shall be governed by and interpreted in accordance with the laws of the State of Texas, without reference to conflict-of-laws principles. User agrees that non-exclusive jurisdiction for any dispute arising out of or relating to these terms and conditions lies within courts located in the State of Texas and consents to venue in Dallas County, Texas. Notwithstanding the foregoing, any judgment may be enforced in any United States or foreign court, and TI may seek injunctive relief in any United States or foreign court.

Mailing Address: Texas Instruments, Post Office Box 655303, Dallas, Texas 75265

Copyright © 2015, Texas Instruments Incorporated

## spacer

# IMPORTANT NOTICE

Texas Instruments Incorporated and its subsidiaries (TI) reserve the right to make corrections, enhancements, improvements and other changes to its semiconductor products and services per JESD46, latest issue, and to discontinue any product or service per JESD48, latest issue. Buyers should obtain the latest relevant information before placing orders and should verify that such information is current and complete. All semiconductor products (also referred to herein as "components") are sold subject to TI's terms and conditions of sale supplied at the time of order acknowledgment.

TI warrants performance of its components to the specifications applicable at the time of sale, in accordance with the warranty in TI's terms and conditions of sale of semiconductor products. Testing and other quality control techniques are used to the extent TI deems necessary to support this warranty. Except where mandated by applicable law, testing of all parameters of each component is not necessarily performed.

TI assumes no liability for applications assistance or the design of Buyers' products. Buyers are responsible for their products and applications using TI components. To minimize the risks associated with Buyers' products and applications, Buyers should provide adequate design and operating safeguards.

TI does not warrant or represent that any license, either express or implied, is granted under any patent right, copyright, mask work right, or other intellectual property right relating to any combination, machine, or process in which TI components or services are used. Information published by TI regarding third-party products or services does not constitute a license to use such products or services or a warranty or endorsement thereof. Use of such information may require a license from a third party under the patents or other intellectual property of the third party, or a license from TI under the patents or other intellectual property of TI.

Reproduction of significant portions of TI information in TI data books or data sheets is permissible only if reproduction is without alteration and is accompanied by all associated warranties, conditions, limitations, and notices. TI is not responsible or liable for such altered documentation. Information of third parties may be subject to additional restrictions.

Resale of TI components or services with statements different from or beyond the parameters stated by TI for that component or service voids all express and any implied warranties for the associated TI component or service and is an unfair and deceptive business practice. TI is not responsible or liable for any such statements.

Buyer acknowledges and agrees that it is solely responsible for compliance with all legal, regulatory and safety-related requirements concerning its products, and any use of TI components in its applications, notwithstanding any applications-related information or support that may be provided by TI. Buyer represents and agrees that it has all the necessary expertise to create and implement safeguards which anticipate dangerous consequences of failures, monitor failures and their consequences, lessen the likelihood of failures that might cause harm and take appropriate remedial actions. Buyer will fully indemnify TI and its representatives against any damages arising out of the use of any TI components in safety-critical applications.

In some cases, TI components may be promoted specifically to facilitate safety-related applications. With such components, TI's goal is to help enable customers to design and create their own end-product solutions that meet applicable functional safety standards and requirements. Nonetheless, such components are subject to these terms.

No TI components are authorized for use in FDA Class III (or similar life-critical medical equipment) unless authorized officers of the parties have executed a special agreement specifically governing such use.

Only those TI components which TI has specifically designated as military grade or "enhanced plastic" are designed and intended for use in military/aerospace applications or environments. Buyer acknowledges and agrees that any military or aerospace use of TI components which have *** not*** been so designated is solely at the Buyer's risk, and that Buyer is solely responsible for compliance with all legal and regulatory requirements in connection with such use.

TI has specifically designated certain components as meeting ISO/TS16949 requirements, mainly for automotive use. In any case of use of non-designated products, TI will not be responsible for any failure to meet ISO/TS16949. **Products** **Applications**

| Audio | www.ti.com/audio | Automotive and Transportation | www.ti.com/automotive |
|:--- |:--- |:--- |:--- |
| Amplifiers | amplifier.ti.com | Communications and Telecom | www.ti.com/communications |
| Data Converters | dataconverter.ti.com | Computers and Peripherals | www.ti.com/computers |
| DLP® Products | www.dlp.com | Consumer Electronics | www.ti.com/consumer-apps |
| DSP | dsp.ti.com | Energy and Lighting | www.ti.com/energy |
| Clocks and Timers | www.ti.com/clocks | Industrial | www.ti.com/industrial |
| Interface | interface.ti.com | Medical | www.ti.com/medical |
| Logic | logic.ti.com | Security | www.ti.com/security |
| Power Mgmt | power.ti.com | Space, Avionics and Defense | www.ti.com/space-avionics-defense |
| Microcontrollers | microcontroller.ti.com | Video and Imaging | www.ti.com/video |

Amplifiers amplifier.ti.com Communications and Telecom <https://www.ti.com/communications>

Data Converters dataconverter.ti.com Computers and Peripherals <https://www.ti.com/computers>

DLP® Products <https://www.dlp.com> Consumer Electronics <https://www.ti.com/consumer-apps>

DSP dsp.ti.com Energy and Lighting <https://www.ti.com/energy>

Clocks and Timers <https://www.ti.com/clocks> Industrial <https://www.ti.com/industrial>

Interface interface.ti.com Medical <https://www.ti.com/medical>

Logic logic.ti.com Security <https://www.ti.com/security>

Power Mgmt power.ti.com Space, Avionics and Defense <https://www.ti.com/space-avionics-defense>

Microcontrollers microcontroller.ti.com Video and Imaging <https://www.ti.com/video> RFID <https://www.ti-rfid.com>

OMAP Applications Processors <https://www.ti.com/omap> **TI** ** ** **E2E Community** e2e.ti.com

Wireless Connectivity <https://www.ti.com/wirelessconnectivity>

Mailing Address: Texas Instruments, Post Office Box 655303, Dallas, Texas 75265

Copyright © 2015, Texas Instruments Incorporated