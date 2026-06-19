# EVM User's Guide: UCC28750EVM-071 UCC287502

***Using the UCC28750EVM-071 60-W AC to DC Converter***

## Description

The UCC28750EVM-071 is a 60-W evaluation module (EVM) for evaluating an off-line power AC to DC flyback converter. The UCC28750EVM-071 is intended for evaluation purposes and is not intended to be an end product. The UCC28750EVM-071 converters 85-V RMS to 265-V RMS input voltage down to 24-V DC, capable of delivering 60 W of output power. This evaluation module uses the UCC287502 Constant-Voltage Flyback Controller Using OptoCoupled Feed-Back in a 60 W converter to provide 2.5 A of constant charge current. The input accepts a voltge range of 85 VAC to 265 VAC. Depending upon the operating conditions, the control law algorithm modulates the switching frequency or the peak primary current to satisfy the power transfer requirements. The programmable slope compensation enables both CCM and DCM operation. Power-boost mode provides additional power for momentary peak demand.

## Get Started

1. Read and study this user's guide completely before evaluating 2. Order the UCC28750EVM-071 for evaluation if step 1 and 2 is met 3. Setup and test the UCC28750EVM-071 per user's guide instructions

## Features

- • Regulated 24 V,+/-5%, 60 W Ouput - • Wide Input Range 85 to 265-V RMS - • Max Load Efficency \> 90%

## Applications

- • Isolated offline AC/DC power supply - • Industrial AC/DC for grid infrastructure, appliances - • Audio, printer, TV, set-top box offline AC/DC - • Battery charger - • Merchant DIN rail power supply, Server PSU - • Electricity meter - • String inverter, Micro inverter - • Small home appliances, Major appliances, AC  indoor/outdoor unit

# UCC28750EVM-071 <https://www.ti.com> *Description*

SLUUCW5 - NOVEMBER 2023 *Submit Document Feedback*

*Using the UCC28750EVM-071 60-W AC to DC Converter*

Copyright © 2023 Texas Instruments Incorporated

## 1 Evaluation Module Overview **1.1 Introduction**

## The UCC28750EVM-071 has frequency foldback and burst mode enable higher efficiency and standby

performance at light load. Opto-coupled feed-back maintains a tightly regulated output with fast dynamic response to load transients. The controller further enhances the efficient operation with valley switching. The UCC287502 also includes a omprehensive protection features including UVLO/OVLO, OTP, OPP, OVP, OCP, brown-out detection, and options to latch and auto-restart. The UCC287502 also uses dithering of the gate drive helps to ease EMI compliance. This user's guide provides the schematic, component list, assembly drawing, art work, and test set up necessary to evaluate the UCC287502 in a typical off-line converter application.

## 1.2 Kit Contents

## • • An Evaluation Module (EVM) TI part number UCC28750EVM-071 - • EVM Disclaimer and Read Me material

## 1.3 Specifications

## Table 1-1. UCC28750EVM-071 Electrical Performance Specifications

# PARAMETER

**TEST CONDITIONS** **MIN** **TYP** **MAX** **UNIT**

# INPUT CHARACTERISTICS

| VIN | Input voltage (RMS) | 115/230 | V |
|:--- |:--- |:--- |:--- |
| fLINE | Line frequency | 50/60 | Hz |
| PSTBY | No load input power | VIN = 115 V / 230 V RMS, IOUT = 0 A | mW | f LINE Line frequency 50/60 Hz

P STBY No load input power $$ VIN = 115 V / 230 V RMS, IOUT = 0 A $$ mW

# OUTPUT CHARACTERISTICS

V OUT Output voltage $$ VIN = 85 - 265 V AC, IOUT = 0 A-2.5 A $$ 22.8 25.2 V

V OUT Output ripple voltage VIN = nom, IOUT = 0-2.5A, mVpp

I OUT Output current V IN = min to max 0.0 2.5 A

# SYSTEMS CHARACTERISTICS Average efficiency

25%, 50%, 75%, 100% load average at nominal input voltages 115-V / 230-V RMS input 89%

Operating temperature range V IN = min to max, I OUT = min to max °C

*Evaluation Module Overview* <https://www.ti.com>

*Using the UCC28750EVM-071 60-W AC to DC Converter* SLUUCW5 - NOVEMBER 2023

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## 2 Hardware **2.1 Test Points**

## Table 2-1. Test Point Functions

| TEST POINTS | DESCRIPTION |
|:--- |:--- |
| TP1 | AC LINE |
| TP2 | AC Neutral |
| TP3 | Capacitor Voltage C9..C12 |
| TP4 | Output Supply |
| TP5 | Secondary Switch Node |
| TP6 | Output Return |
| TP7 | AC Neutral |
| TP8 | Primary Switch Node |
| TP9 | Output Return |
| TP10 | UCC287502 Supply Voltage |
| TP11 | Feedback Test Point |
| TP12 | UCC287502 DRV Pin |
| TP13 | Q1 Gate |
| TP14 | Feedback Test Point |
| TP15 | UCC287502 CS Pin |
| TP16 | UCC287502 FB Pin |
| TP17 | UCC287502 OPP Pin |
| TP18 | Primary Ground |

# TP1 AC LINE TP2 AC Neutral TP3 Capacitor Voltage C9..C12 TP4 Output Supply TP5 Secondary Switch Node TP6 Output Return TP7 AC Neutral TP8 Primary Switch Node TP9 Output Return TP10 UCC287502 Supply Voltage TP11 Feedback Test Point

# TP12 UCC287502 DRV Pin TP13 Q1 Gate TP14 Feedback Test Point

# TP15 UCC287502 CS Pin

# TP16 UCC287502 FB Pin

# TP17 UCC287502 OPP Pin TP18 Primary Ground

## 2.2 Test Setup

## 2.2.1 Test Setup Requirements

## Safety: This evaluation module is not encapsulated and there are voltages that are much greater than 50 V DC.

# WARNING

## If you are not trained in the proper safety of handling and testing power electronics please do not test this evaluation module.

## Voltage Source: Isolated AC source or variable AC transformer capable of 265 V AC cable of handling 80 W

## Voltmeter: Digital voltage meter

## Power Analyzer: Capable of measuring 1 mW to 10 W of input power and capable of handling 265-V RMS input

voltage. Please read the power analyzer's user manual for proper setup.

## Oscilloscope

- • 4 Channel 100 MHz. - • Probes capable of handling 600 V.

## Output Load: Resistive or electronic load capable handling 60 W at 24 V.

## Recommended Wire Gauge: Insulated 22 AWG. <https://www.ti.com> *Hardware*

SLUUCW5 - NOVEMBER 2023 *Submit Document Feedback*

*Using the UCC28750EVM-071 60-W AC to DC Converter*

Copyright © 2023 Texas Instruments Incorporated

# 2.2.2 Test Setup Diagram **AC Line** **AC Neutral**

# VOUT +

# VOUT **Isolated ** **Variable AC ** **Source**

**Current** **Measurement** **Voltage** **Measurement** **Power Analyzer** **Load**

# UCC28750EVM-071

# TP1

# TP7

# TP4

# TP9 **Volt Meter** **Oscilloscope** **Scope ** **Probe** **J1 Pin1** **J1 Pin3** **J2 Pin1** **J2 Pin2**

# Figure 2-1. UCC28750EVM-001 Test Setup Diagram

# 2.3 Best Practices

# CAUTION!

# CAUTION

# This EVM has voltages greater than 50 V DC and 50 V AC when power is applied to the input.

Caution must be taken when evaluating the EVM.

# CAUTION

# This EVM has components that reach tempataures of greater than 55 ℃. Caution must be taken when evaluating the EVM.

## Hardware <https://www.ti.com>

## Using the UCC28750EVM-071 60-W AC to DC Converter SLUUCW5 - NOVEMBER 2023

## Submit Document Feedback

Copyright © 2023 Texas Instruments Incorporated

**2.3.1 General Texas Instruments High Voltage Evaluation (TI HV EVM) User Safety Guidelines**

# WARNING

Always follow TI's setup and application instructions, including use of all interface components within the recommended electrical rated voltage and power limits. Always use electrical safety precautions to help verify your personal safety and those working around you. Contact TI's Product Information Center http:// support/ti./com for further information.

**Save all warnings and instructions for future reference.**

# WARNING

Failure to follow warnings and instructions can result in personal injury, property damage or death due to electrical shock and burn hazards.

The term TI HV EVM refers to an electronic device typically provided as an open framed, unenclosed printed circuit board assembly. It is *intended strictly for use in development laboratory environments, solely for qualified * *professional users having training, expertise and knowledge of electrical safety risks in development and * *application of high voltage electrical circuits. Any other use and/or application are strictly prohibited by Texas * *Instruments.* If you are not suitably qualified, then immediately stop from further use of the HV EVM.

1. Work Area Safety a. Keep work area clean and orderly. b. Qualified observers must be present anytime circuits are energized. c. Effective barriers and signage must be present in the area where the TI HV EVM and the interface electronics are energized, indicating operation of accessible high voltages can be present, for the purpose of protecting inadvertent access. d. All interface circuits, power supplies, evaluation modules, instruments, meters, scopes and other related apparatus used in a development environment exceeding 50Vrms/75VDC must be electrically located within a protected Emergency Power Off EPO protected power strip. e. Use stable and nonconductive work surface. f. Use adequately insulated clamps and wires to attach measurement probes and instruments. No freehand testing whenever possible. 2. Electrical Safety As a precautionary measure, it is always a good engineering practice to assume that the entire EVM can have fully accessible and active high voltages. a. De-energize the TI HV EVM and all the inputs, outputs and electrical loads before performing any electrical or other diagnostic measurements. Revalidate that TI HV EVM power has been safely deenergized. b. With the EVM confirmed de-energized, proceed with required electrical circuit configurations, wiring, measurement equipment connection, and other application needs, while still assuming the EVM circuit and measuring instruments are electrically live. c. After EVM readiness is complete, energize the EVM as intended.

# WARNING

While the EVM is energized, never touch the EVM or the electrical circuits, as they can be at high voltages capable of causing electrical shock hazard.

3. Personal Safety a. Wear personal protective equipment (for example, latex gloves or safety glasses with side shields) or protect EVM in an adequate lucent plastic box with interlocks to protect from accidental touch. **Limitation for safe use:**

EVMs are not to be used as all or part of a production unit. <https://www.ti.com> *Hardware*

SLUUCW5 - NOVEMBER 2023 *Submit Document Feedback*

*Using the UCC28750EVM-071 60-W AC to DC Converter*

Copyright © 2023 Texas Instruments Incorporated

## 3 Implementation Results

**3.1 Performance Data and Typical Characteristic Curves**

## 3.1.1 Efficiency

## Table 3-1. Efficiency Test Data

# V IN RMS

**V** **OUT** **I** **OUT** **P** **IN** **P** **OUT** **EFFICIENCY**

# 24.2 0.00 0.059 NA

| 24.145 | 0.055 | 1.573 | 1.3273 | 84.38 |
| ---: | ---: | ---: | ---: | ---: |
| 24.143 | 0.197 | 5.353 | 4.763 | 88.98 |
| 24.137 | 0.46 | 12.278 | 11.104 | 90.43 |
| 24.132 | 0.696 | 18.566 | 16.813 | 90.55 |
| 24.13 | 0.968 | 25.8 | 23.357 | 90.53 |
| 24.127 | 1.2119 | 32.462 | 29.239 | 90.07 | 24.143 0.197 5.353 4.763 88.98 24.137 0.46 12.278 11.104 90.43 24.132 0.696 18.566 16.813 90.55 24.13 0.968 25.8 23.357 90.53 24.127 1.2119 32.462 29.239 90.07 24.125 1.451 89.74

| 24.122 | 1.6398 | 44.17 | 39.554 | 89.54 |
| ---: | ---: | ---: | ---: | ---: |
| 24.12 | 1.887 | 50.88 | 45.53 | 89.48 |
| 24.113 | 2.231 | 60.4 | 53.83 | 89.12 | 24.12 1.887 50.88 45.53 89.48 24.113 2.231 60.4 53.83 89.12 24.1 2.726 73.9 88.97

| 24.21 | 0.000 | 0.065 | 0.000 | NA |
| ---: | ---: | ---: | ---: | ---: |
| 24.145 | 0.055 | 1.57 | 1.328 | 84.58 |
| 24.136 | 0.196 | 5.35 | 4.747 | 88.73 |
| 24.131 | 0.46 | 12.26 | 11.09 | 90.45 |
| 24.126 | 0.698 | 18.56 | 16.85 | 90.78 |
| 24.122 | 0.972 | 25.76 | 23.45 | 91.03 |
| 24.120 | 1.211 | 32.09 | 29.21 | 91.02 |
| 24.115 | 1.449 | 38.41 | 34.96 | 91.02 |
| 24.113 | 1.74\] | 46.25 | 42.02 | 90.85 |
| 24.112 | 1.88 | 49.97 | 45.35 | 90.75 |
| 24.110 | 2.228 | 59.2 | 53.73 | 90.76 | 24.145 0.055 1.57 1.328 84.58 24.136 0.196 5.35 4.747 88.73 24.131 0.46 12.26 11.09 90.45 24.126 0.698 18.56 16.85 90.78 24.122 0.972 25.76 23.45 91.03 24.120 1.211 32.09 29.21 91.02 24.115 1.449 38.41 34.96 91.02 24.113 1.74\] 46.25 42.02 90.85 24.112 1.88 49.97 45.35 90.75 24.110 2.228 59.2 53.73 90.76 24.108 2.72 72.6 89.53

# 24.227 0.000 0.102 0.000 NA 24.147 0.055 1.6628 1.328

| 24.138 | 0.197 | 5.512 | 4.759 | 86.34 |
| ---: | ---: | ---: | ---: | ---: |
| 24.135 | 0.46 | 12.425 | 11.106 | 89.38 |
| 24.135 | 0.696 | 18.644 | 16.812 | 90.17 |
| 24.133 | 0.969 | 25.7 | 23.379 | 90.96 |
| 24.132 | 1.2113 | 32.1 | 29.219 | 91.02 |
| 24.128 | 1.4512 | 38.5 | 35.017 | 90.95 |
| 24.123 | 1.6398 | 43.418 | 39.548 | 91.08 |
| 24.121 | 1.8872 | 49.95 | 45.51 | 91.11 | 24.135 0.46 12.425 11.106 89.38 24.135 0.696 18.644 16.812 90.17 24.133 0.969 25.7 23.379 90.96 24.132 1.2113 32.1 29.219 91.02 24.128 1.4512 38.5 35.017 90.95 24.123 1.6398 43.418 39.548 91.08 24.121 1.8872 49.95 45.51 91.11 24.118 2.23 53.83 91.23 24.115 2.7287 72.33 65.813 90.99

# 24.32 0.151 NA *Implementation Results* <https://www.ti.com>

*Using the UCC28750EVM-071 60-W AC to DC Converter* SLUUCW5 - NOVEMBER 2023

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## Table 3-1. Efficiency Test Data (continued)

# V IN RMS

**V** **OUT** **I** **OUT** **P** **IN** **P** **OUT** **EFFICIENCY**

| 24.144 | 0.055 | 1.7 | 1.33 | 78.2 |
| ---: | ---: | ---: | ---: | ---: |
| 24.134 | 0.197 | 5.5925 | 4.7635 | 85.17 |
| 24.132 | 0.46 | 12.56 | 11.108 | 88.43 |
| 24.13 | 0.697 | 18.76 | 16.83 | 89.7 |
| 24.128 | 0.968 | 25.903 | 23.348 | 90.13 |
| 24.126 | 1.211 | 32.224 | 29.21 | 90.64 |
| 24.125 | 1.4513 | 38.53 | 35.018 | 90.88 |
| 24.122 | 1.64 | 43.54 | 39.55 | 90.83 |
| 24.12 | 1.8872 | 50.06 | 45.52 | 90.91 | 24.134 0.197 5.5925 4.7635 85.17 24.132 0.46 12.56 11.108 88.43 24.13 0.697 18.76 16.83 89.7 24.128 0.968 25.903 23.348 90.13 24.126 1.211 32.224 29.21 90.64 24.125 1.4513 38.53 35.018 90.88 24.122 1.64 43.54 39.55 90.83 24.12 1.8872 50.06 45.52 90.91 24.118 2.231 59.13 53.813 24.115 2.72 72.09 65.63 91.03

## Output Power (W)

## Efficiency (%)

## 0.78

## 0.8

## 0.82

## 0.84

## 0.86

## 0.88

## 0.9

## 0.92

## 85 Vrms 115 Vrms 230 Vrms 265 Vrms

## Figure 3-1. Efficiency

## Note

The inductor L1, which is mounted on the PCB and shown in BOM needs to be removed and shorted out to get best efficiency results. **Standby Power** AC Input Voltage (Volts) Power (mW) <https://www.ti.com> *Implementation Results*

SLUUCW5 - NOVEMBER 2023 *Submit Document Feedback*

*Using the UCC28750EVM-071 60-W AC to DC Converter*

Copyright © 2023 Texas Instruments Incorporated **3.1.2 Startup**

# CH1 =V BULK, CH2 = V CC, CH3 = V GATE, CH4 = V OUT

**Figure 3-2. Start-up Waveforms at 85Vac and No ** **Load**

**Figure 3-3. Start-up Waveforms at 85Vac and Full ** **Load**

**Figure 3-4. Start-up Waveforms at 115Vac and No ** **Load**

**Figure 3-5. Start-up Waveforms at 115Vac and Full ** **Load**

**Figure 3-6. Start-up Waveforms at 230Vac and No ** **Load**

**Figure 3-7. Start-up Waveforms at 230Vac and Full ** **Load** *Implementation Results* <https://www.ti.com>

*Using the UCC28750EVM-071 60-W AC to DC Converter* SLUUCW5 - NOVEMBER 2023

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## Figure 3-8. Start-up Waveforms at 265Vac and No

## Load

## Figure 3-9. Start-up Waveforms at 265Vac and Full

## Load

## 3.1.3 Load Transients

# CH1 = V OUT, CH4 = I OUT

## Load = 0.100A to 2.5A, 1 kHz, 50% Duty Cycle

# VIN = 85 VAC

## Figure 3-10. Load Transients at 85Vac

# VIN = 115 VAC

## Figure 3-11. Load Transients at 115Vac

# VIN = 230 VAC

## Figure 3-12. Load Transients at 230Vac

# VIN = 265 VAC

## Figure 3-13. Load Transients at 265Vac <https://www.ti.com> *Implementation Results*

SLUUCW5 - NOVEMBER 2023 *Submit Document Feedback*

*Using the UCC28750EVM-071 60-W AC to DC Converter*

Copyright © 2023 Texas Instruments Incorporated

## 3.1.4 Output Ripple Voltage at Full Load

# CH1 = V OUT, CH2 = V AUX, CH3 = V CS

# VIN = 85 VAC, RLOAD = 9.6 ohm

## Figure 3-14. Voltage Ripple at 85Vac and Full Load

# VIN = 265 VAC, RLOAD = 9.6 ohm

## Figure 3-15. Voltage Ripple at 265Vac and Full

## Load *Implementation Results* <https://www.ti.com>

*Using the UCC28750EVM-071 60-W AC to DC Converter* SLUUCW5 - NOVEMBER 2023

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## 3.1.5 Q1 Drain Voltage Evaluation

# CH1=VQ1d, CH3 = VGATE, CH4 = VOUT

## Figure 3-16. Steady State Waveform at 85Vac

## Figure 3-17. Steady State Waveform at 85Vac <https://www.ti.com> *Implementation Results*

SLUUCW5 - NOVEMBER 2023 *Submit Document Feedback*

*Using the UCC28750EVM-071 60-W AC to DC Converter*

Copyright © 2023 Texas Instruments Incorporated

# 4 Hardware Design Files **4.1 Schematic**

# GND

# GND

# Q1 IPP65R190C7

# GND

# GND

| 1mH | L2 |
|:--- |:--- |
| 1kV | D1 |
| 330pF | C24 | 1kV D1 330pF C24

# J1

# TP1

# TP7 Primary\_GND Vout

# FB 43:10:6

# T1

# FB Aux

# DRV Aux Vin

# VDD

# VDD

# TP2

# TP4

# TP9

# TP6

# TP18

# TP10

# CGND

# GND Aux Primary\_GND

# CS

# CS FLT

# FLT 22.0

# R9 DRV

# R18 Primary\_GND

# TP3

# TP12

# TP15

# TP17

# TP16 Primary\_GND

# C25 4.7uF C10 4.7uF C9 4.7uF C14

# GND

| 0.1uF | C1 |
|:--- |:--- |
| U2 | TL431AIDBZR |
| 1nF | C23 |

# U2 TL431AIDBZR 1nF C23 680pF

# C8 1nF C6

# F1 0.47uF C3 0.47uF

# C4 0.47uF

# C5

# D7 1.00k

# R13 0.1uF C17

# H2

# 7173DG Primary\_GND

# TP13

# NC

# 200V

# D5

# NC

# 200V D6

# R5

| 470uF | C11 |
|:--- |:--- |
| 470uF | C12 |
| 470uF | C13 | 470uF C12 470uF C13

# U1

# TCMT1107

# TP11

# TP14

# 51.0 R8

# TP5

# TP8

# H1

# 7173DG

| 1000pF | C16 |
|:--- |:--- |
| 2200pF | C15 |
| 2200pF | C7 |
| Primary\_GND | Primary\_GND | 2200pF C15 2200pF C7 Primary\_GND Primary\_GND Primary\_GND Primary\_GND Primary\_GND Primary\_GND Primary\_GND Primary\_GND 1uH

# L3

# 600V

# D3

| 86.6k | R14 |
|:--- |:--- |
| 10.0k | R19 |
| 10.0k | R11 | 10.0k R19 10.0k R11

# R20 Vin 20.5k R21 22.1

# R6 R1 511k 133k

# R15 680pF

# C20 56pF

# C22

# VDD

# CS

# DRV

# FB

# FLT

# UCC287502DBV

# GND

# U3

# 200V

# D2 + 150uF 450V

# C2

No designated component value means the device is not populated R16 and R17 effective is around 0.2875 ohms

| 0.56 | R16 |
|:--- |:--- |
| 0.56 | R17 |
| 50V | 22pF |

# 0.56 R17 50V 22pF

# C21

# R7 + 35V 100µF

# C19 50V 4.7uF

# C18

# NC

# 200V

# D8

# D4

Do not populate (DNP) R20, R7 & C25 (V ariant - 001)

# MMSZ4707T1G 10.0k

# R10

# 2.00M

# R2

# 2.00M

# R3

# 2.00M

# R4 2.49k R12

# GATE

# J2

Note: On actual hardware (pcb) L1 needs to be shorted with a jumper for best efficiency results

# Figure 4-1. UCC28750EVM-071 Schematic

# Hardware Design Files <https://www.ti.com>

# Using the UCC28750EVM-071 60-W AC to DC Converter SLUUCW5 - NOVEMBER 2023

# Submit Document Feedback

Copyright © 2023 Texas Instruments Incorporated

## 4.2 EVM Assembly and Layout

## Figure 4-2. EVM Assembly (Top View) <https://www.ti.com> *Hardware Design Files*

SLUUCW5 - NOVEMBER 2023 *Submit Document Feedback*

*Using the UCC28750EVM-071 60-W AC to DC Converter*

Copyright © 2023 Texas Instruments Incorporated

## Figure 4-3. EVM Assembly/Layout (Bottom View) *Hardware Design Files* <https://www.ti.com>

*Using the UCC28750EVM-071 60-W AC to DC Converter* SLUUCW5 - NOVEMBER 2023

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

## 4.3 Bill of Materials

## UCC28750EVM-071 bill of materials as shown in Table 4-1.

## Table 4-1. UCC28750EVM-001 Bill of Materials

# QTY

**DES** **DESCRIPTION** **PART NUMBER** **MANUFACTURER**

C1 Cap Film Suppression X2 0.1uF 560VDC/275VAC PP 10% (18 X 5 X 11mm) Radial Plastic Rectangular Can 15 mm 110C Bulk R46KI3100JBM1K Kemet

C2 150 µF 450 V Aluminum Electrolytic Capacitors Radial, Can - Snap-In 5000 Hrs @ 105°C

# 450VXH150MEFCSN25X Rubycon

C3, C4, C5 CAP, CERM, 0.47 uF, 500 V, +/- 10%, X7R, 1812 1812Y5000474KXTWS2 Knowles Capacitors

# C6

CAP, CERM, 1000 pF, 250 V, +/- 10%, X7R, 0603 GRM188R72E102KW07D MuRata

C7, C15 Cap Ceramic Disc 2200 pF 20% 250VAC Thru-Hole 9.0x4.0x10.0 Ammo pack DE1E3RA222MN4AN01F Murata

C8 680 pF \pm5% 200 V Ceramic Capacitor C0G, NP0 1210 (3225 Metric)

| 12102A681JAT2A | KYOCERA AVX |
|:--- |:--- |
| C9, C10, | C14 |
| Cap Ceramic 4.7uF 35 V X5R ±10% Pad SMD 0603 +85°C | T/R |
| CL10A475KL8NRNC | Samsung |

# C9, C10, C14

Cap Ceramic 4.7uF 35 V X5R \pm10% Pad SMD 0603 +85°C T/R CL10A475KL8NRNC Samsung

| C12, C13 | CAP, AL, 470 uF, 35 V, +/- 20%, TH | EKZE350ELL471MJ20S | Chemi-Con |
|:--- |:--- |:--- |:--- |
| C16 | CAP, CERM, 1000 pF, V, +/- 20%, Y5V, D7xT5mm | C901U102MYVDBA7317 | Kemet |
| C17 | CAP, CERM, 0.1 uF, 50 V,+/- 10%, X7R, 0402 | C1005X7R1H104K050BE | TDK |
| C18 | CAP, CERM, 4.7 uF, 50 V, +/- 10%, X7S, 0805 | GRM21BC71H475KE11K | MuRata |

# C16

CAP, CERM, 1000 pF, V, +/- 20%, Y5V, D7xT5mm C901U102MYVDBA7317 Kemet

# C17

CAP, CERM, 0.1 uF, 50 V,+/- 10%, X7R, 0402 C1005X7R1H104K050BE TDK

# C18

CAP, CERM, 4.7 uF, 50 V, +/- 10%, X7S, 0805 GRM21BC71H475KE11K MuRata

C19 100 µF 35 V Aluminum Electrolytic Capacitors Radial, Can 5000 Hrs @ 105°C Wurth Electronics

| C20 | CAP, CERM, 680 pF, 50 V, +/- 5%, C0G/NP0, 0603 | GRM1885C1H681JA01D | MuRata |
|:--- |:--- |:--- |:--- |
| C21 | CAP, CERM, 22 pF, 50 V, +/- 5%, C0G/NP0, 0603 | GRM1885C1H220JA01D | MuRata |
| C22 | CAP, CERM, 56 pF, 50 V, +/- 5%, C0G/NP0, 0603 | 06035A560JAT2A | AVX |
| C23 | CAP, CERM, 1000 pF, 50 V, +/- 10%, X7R, 0603 | C0603X102K5RACTU | KEMET |
| C24 | CAP, CERM, 330 pF, 50 V, +/- 5%, C0G/NP0, 0603 | C0603C331J5GACTU | KEMET |

# C21

CAP, CERM, 22 pF, 50 V, +/- 5%, C0G/NP0, 0603 GRM1885C1H220JA01D MuRata

# C22

CAP, CERM, 56 pF, 50 V, +/- 5%, C0G/NP0, 0603 06035A560JAT2A AVX

# C23

CAP, CERM, 1000 pF, 50 V, +/- 10%, X7R, 0603 C0603X102K5RACTU KEMET

# C24

CAP, CERM, 330 pF, 50 V, +/- 5%, C0G/NP0, 0603 C0603C331J5GACTU KEMET

D1 Bridge Rectifier Single Phase Standard 1 kV Through Hole GBU GBU4M-E3/51 Vishay Semiconductor

| D2 | Diode Schottky 200 V 6 A ITO220AC | MBR6200F\_T0\_00001 | Panjit |
|:--- |:--- |:--- |:--- |
| D3 | Diode, Ultrafast, 600 V, 1 A, SMB | MURS160-13-F | Diodes Inc. |
| D4 | Zener Diode 20 V 500 mW ±5% Surface Mount SOD-123 | MMSZ4707T1G | Onsemi |

D3 Diode, Ultrafast, 600 V, 1 A, SMB MURS160-13-F Diodes Inc.

D4 Zener Diode 20 V 500 mW \pm5% Surface Mount SOD-123 MMSZ4707T1G Onsemi

| D5, D6, | D8 |
|:--- |:--- |
| Diode Standard 200 V 200 mA Surface Mount SOT-23-3 | (TO-236) |
| BAS20LT3G | On Semiconductor |

Diode Standard 200 V 200 mA Surface Mount SOT-23-3 (TO-236) BAS20LT3G On Semiconductor F1 Fuse, 3.15 A, 250VAC/VDC, TH Littelfuse

H1, H2 Heat Sink, TO-220 Vertical 7173DG Aavid

# H3, H4, H5, H6

Machine Screw, Round, #4-40 x 1/4, Nylon, Philips panhead NY PMS 440 0025 PH B&F Fastener Supply

# H7, H8, H9, H10

Standoff, Hex, 0.5"L #4-40 Nylon 1902C Keystone

J1 Header, 312mil, 3x1, Tin, TH 1-1318301-3 TE Connectivity

J2 Terminal Block, 5.08 mm, 2x1, TH Phoenix Contact

L1 22 µH Semi-Shielded Drum Core, Wirewound Inductor 1.8 A 89mOhm Nonstandard Wurth Electronics

L2 Coupled inductor, 1 mH, 2 A, 0.045 ohm, TH Wurth Elektronik

L3 1 µH Unshielded Drum Core, Wirewound Inductor 7.5 A 10mOhm Max Radial, Vertical Cylinder (Open) Wurth Electronics

| MP1, MP2 | Mounting Kit For TO-220 Heat Sinks | 4880SG | Aavid Thermalloy |
|:--- |:--- |:--- |:--- |
| Q1 | MOSFET, N-CH, 700 V, 13 A, TO-220AB | IPP65R190C7 | Infineon Technologies |
| R1 | RES, 511 k, 1%, 0.125 W, AEC-Q200 Grade 0, 0805 | ERJ-6ENF5113V | Panasonic |

Q1 MOSFET, N-CH, 700 V, 13 A, TO-220AB IPP65R190C7 Infineon Technologies

R1 RES, 511 k, 1%, 0.125 W, AEC-Q200 Grade 0, 0805 ERJ-6ENF5113V Panasonic <https://www.ti.com> *Hardware Design Files*

SLUUCW5 - NOVEMBER 2023 *Submit Document Feedback*

*Using the UCC28750EVM-071 60-W AC to DC Converter*

Copyright © 2023 Texas Instruments Incorporated

## Table 4-1. UCC28750EVM-001 Bill of Materials (continued)

# QTY

**DES** **DESCRIPTION** **PART NUMBER** **MANUFACTURER**

R2, R3, R4 RES, 2.00 M, 1%, 0.25 W, 1206 RC1206FR-072ML Yageo America

R5 100 Ohms \pm0.1% 0.2W, 1/5W Chip Resistor 0805 (2012 Metric) Anti-Sulfur, Automotive AEC-Q200, Moisture Resistant TNPW0805100RBYEN Vishay

# R6

RES, 22.1, 1%, 0.5 W, 1210 RC1210FR-0722R1L Yageo

R7 RES, 0, 1%, 0.1 W, AEC-Q200 Grade 0, 0603 RMCF0603ZT0R00 Stackpole Electronics Inc

R8 RES, 51.0, 1%, 0.25 W, 1206 RC1206FR-0751RL Yageo America

# R9

RES, 22.0, 1%, 0.1 W, 0603 RC0603FR-0722RL Yageo

R10 RES, 10.0 k, 1%, 0.1 W, AEC-Q200 Grade 0, 0603 RMCF0603FT10K0 Stackpole Electronics Inc

| R11, R19 | RES, 10.0 k, 1%, 0.25 W, 1206 | RC1206FR-0710KL | Yageo America |
|:--- |:--- |:--- |:--- |
| R12 | RES, 2.49 k, 1%, 0.1 W, 0603 | RC0603FR-072K49L | Yageo |
| R13 | RES, 1.00 k, 0.1%, 0.1 W, 0603 | RT0603BRD071KL | Yageo America |
| R14 | RES, 86.6 k, 0.1%, 0.125 W, 0805 | RT0805BRD0786K6L | Yageo America |
| R15 | RES, 133 k, 1%, 0.25 W, 1206 | RC1206FR-07133KL | Yageo America |
| R16, R17 | RES, 0.56, 1%, 0.25 W, 1206 | ERJ-8RQFR56V | Panasonic |
| R18 | RES, 220, 1%, 0.1 W, 0603 | RC0603FR-07220RL | Yageo |
| R21 | RES, 20.5 k, 1%, 0.125 W, AEC-Q200 Grade 0, 0805 | ERJ-6ENF2052V | Panasonic |
| T1 | CCM Flyback Transformer for UCC28750EVM-071 | RLTI-1450 | Renco Electronics |

# R12

RES, 2.49 k, 1%, 0.1 W, 0603 RC0603FR-072K49L Yageo

R13 RES, 1.00 k, 0.1%, 0.1 W, 0603 RT0603BRD071KL Yageo America

R14 RES, 86.6 k, 0.1%, 0.125 W, 0805 RT0805BRD0786K6L Yageo America

R15 RES, 133 k, 1%, 0.25 W, 1206 RC1206FR-07133KL Yageo America

R16, R17 RES, 0.56, 1%, 0.25 W, 1206 ERJ-8RQFR56V Panasonic

# R18

RES, 220, 1%, 0.1 W, 0603 RC0603FR-07220RL Yageo

R21 RES, 20.5 k, 1%, 0.125 W, AEC-Q200 Grade 0, 0805 ERJ-6ENF2052V Panasonic

T1 CCM Flyback Transformer for UCC28750EVM-071 RLTI-1450 Renco Electronics

# TP1, TP2,

TP3, TP4, TP5, TP7, TP8, TP10, TP12, TP13, TP15, TP16, TP17

| Test Point, Compact, Red, TH | Keystone Electronics |
|:--- |:--- |
| TP6, TP9, | TP18 |
| Test Point, Compact, Black, TH | Keystone Electronics |
| TP11, | TP14 |
| Test Point, Compact, White, TH | Keystone Electronics |

# TP6, TP9, TP18

Test Point, Compact, Black, TH Keystone Electronics

# TP11, TP14

Test Point, Compact, White, TH Keystone Electronics

U1 Optocoupler, 3.75 kV, 80-160% CTR, SMT TCMT1107 Vishay-Semiconductor

U2 Adjustable Precision Shunt Regulator, 34 ppm / degC, 100 mA, -40 to 85 degC, 3-pin SOT-23 (DBZ), Green (RoHS & no Sb/Br) TL431AIDBZR Texas Instruments

U3 Continuous Conduction Mode (CCM) Secondary Side Regulated (SSR) Current-Mode Offline Flyback Controller UCC287502DBV Texas Instruments

## 5 Additional Information

**5.1 Trademarks** All trademarks are the property of their respective owners. *Additional Information* <https://www.ti.com>

*Using the UCC28750EVM-071 60-W AC to DC Converter* SLUUCW5 - NOVEMBER 2023

*Submit Document Feedback* Copyright © 2023 Texas Instruments Incorporated

# STANDARD TERMS FOR EVALUATION MODULES

1. *Delivery:* TI delivers TI evaluation boards, kits, or modules, including any accompanying demonstration software, components, and/or documentation which may be provided together or separately (collectively, an "EVM" or "EVMs") to the User ("User") in accordance with the terms set forth herein. User's acceptance of the EVM is expressly subject to the following terms.

1.1 EVMs are intended solely for product or software developers for use in a research and development setting to facilitate feasibility evaluation, experimentation, or scientific analysis of TI semiconductors products. EVMs have no direct function and are not finished products. EVMs shall not be directly or indirectly assembled as a part or subassembly in any finished product. For clarification, any software or software tools provided with the EVM ("Software") shall not be subject to the terms and conditions set forth herein but rather shall be subject to the applicable terms that accompany such Software

1.2 EVMs are not intended for consumer or household use. EVMs may not be sold, sublicensed, leased, rented, loaned, assigned, or otherwise distributed for commercial purposes by Users, in whole or in part, or used in any finished product or production system.

*Limited* * * *Warranty and Related* * * *Remedies/Disclaimers*:

2.1 These terms do not apply to Software. The warranty, if any, for Software is covered in the applicable Software License Agreement.

2.2 TI warrants that the TI EVM will conform to TI's published specifications for ninety (90) days after the date TI delivers such EVM to User. Notwithstanding the foregoing, TI shall not be liable for a nonconforming EVM if (a) the nonconformity was caused by neglect, misuse or mistreatment by an entity other than TI, including improper installation or testing, or for any EVMs that have been altered or modified in any way by an entity other than TI, (b) the nonconformity resulted from User's design, specifications or instructions for such EVMs or improper system design, or (c) User has not paid on time. Testing and other quality control techniques are used to the extent TI deems necessary. TI does not test all parameters of each EVM. User's claims against TI under this Section 2 are void if User fails to notify TI of any apparent defects in the EVMs within ten (10) business days after delivery, or of any hidden defects with ten (10) business days after the defect has been detected.

2.3 TI's sole liability shall be at its option to repair or replace EVMs that fail to conform to the warranty set forth above, or credit User's account for such EVM. TI's liability under this warranty shall be limited to EVMs that are returned during the warranty period to the address designated by TI and that are determined by TI not to conform to such warranty. If TI elects to repair or replace such EVM, TI shall have a reasonable time to repair such EVM or provide replacements. Repaired EVMs shall be warranted for the remainder of the original warranty period. Replaced EVMs shall be warranted for a new full ninety (90) day warranty period.

# WARNING

## Evaluation Kits are intended solely for use by technically qualified,

## professional electronics experts who are familiar with the dangers

**and** ** ** **application risks associated** ** ** **with** ** ** **handling** ** ** **electrical mechanical**

## components, systems, and subsystems.

## User shall operate the Evaluation Kit within TI's recommended

**guidelines** ** ** **and** ** ** **any applicable legal** ** ** **or** ** ** **environmental** ** ** **requirements**

## as well as reasonable and customary safeguards. Failure to set up

## and/or operate the Evaluation Kit within TI's recommended

**guidelines** ** ** **may result in** ** ** **personal injury** ** ** **or** ** ** **death or** ** ** **property**

## damage. Proper set up entails following TI's instructions for

**electrical ratings of interface** ** ** **circuits such as input,** ** ** **output** ** ** **and**

## electrical loads.

# NOTE

EXPOSURE TO ELECTROSTATIC DISCHARGE (ESD) MAY CAUSE DEGREDATION OR FAILURE OF THE EVALUATION KIT; TI RECOMMENDS STORAGE OF THE EVALUATION KIT IN A PROTECTIVE ESD BAG. <https://www.ti.com> *Regulatory Notices:* 3.1 *United States*

3.1.1 *Notice applicable* * * *to EVMs not FCC-Approved:*

**FCC** ** ** **NOTICE:** This kit is designed to allow product developers to evaluate electronic components, circuitry, or software associated with the kit to determine whether to incorporate such items in a finished product and software developers to write software applications for use with the end product. This kit is not a finished product and when assembled may not be resold or otherwise marketed unless all required FCC equipment authorizations are first obtained. Operation is subject to the condition that this product not cause harmful interference to licensed radio stations and that this product accept harmful interference. Unless the assembled kit is designed to operate under part 15, part 18 or part 95 of this chapter, the operator of the kit must operate under the authority of an FCC license holder or must secure an experimental authorization under part 5 of this chapter.

3.1.2 *For EVMs annotated* * * *as* * * *FCC* * * *- FEDERAL COMMUNICATIONS* * * *COMMISSION Part* * * *15* * * *Compliant:*

# CAUTION

This device complies with part 15 of the FCC Rules. Operation is subject to the following two conditions: (1) This device may not cause harmful interference, and (2) this device must accept any interference received, including interference that may cause undesired operation.

Changes or modifications not expressly approved by the party responsible for compliance could void the user's authority to operate the equipment.

**FCC Interference** ** ** **Statement** ** ** **for** ** ** **Class** ** ** **A** ** ** **EVM devices**

*NOTE:* * * *This* * * *equipment* * * *has* * * *been* * * *tested* * * *and* * * *found* * * *to* * * *comply* * * *with* * * *the* * * *limits* * * *for* * * *a* * * *Class* * * *A* * * *digital* * * *device,* * * *pursuant* * * *to* * * *part* * * *15* * * *of* *the* * * *FCC* * * *Rules.* * * *These* * * *limits* * * *are* * * *designed* * * *to* * * *provide* * * *reasonable* * * *protection* * * *against* * * *harmful* * * *interference* * * *when* * * *the* * * *equipment* * * *is* *operated* * * *in* * * *a* * * *commercial* * * *environment.* * * *This* * * *equipment* * * *generates,* * * *uses,* * * *and* * * *can* * * *radiate* * * *radio* * * *frequency* * * *energy* * * *and,* * * *if* * * *not* *installed* * * *and* * * *used* * * *in* * * *accordance* * * *with* * * *the* * * *instruction* * * *manual,* * * *may* * * *cause* * * *harmful* * * *interference* * * *to* * * *radio* * * *communications.* *Operation* * * *of* * * *this* * * *equipment* * * *in* * * *a* * * *residential* * * *area* * * *is* * * *likely* * * *to* * * *cause* * * *harmful* * * *interference* * * *in* * * *which* * * *case* * * *the* * * *user* * * *will* * * *be* * * *required* * * *to* *correct* * * *the interference at his own expense.*

**FCC Interference** ** ** **Statement** ** ** **for** ** ** **Class** ** ** **B** ** ** **EVM devices**

*NOTE:* * * *This* * * *equipment* * * *has* * * *been* * * *tested* * * *and* * * *found* * * *to* * * *comply* * * *with* * * *the* * * *limits* * * *for* * * *a* * * *Class* * * *B* * * *digital* * * *device,* * * *pursuant* * * *to* * * *part* * * *15* * * *of* *the* * * *FCC* * * *Rules.* * * *These* * * *limits* * * *are* * * *designed* * * *to* * * *provide* * * *reasonable* * * *protection* * * *against* * * *harmful* * * *interference* * * *in* * * *a* * * *residential* *installation. This equipment generates, uses* * * *and can* * * *radiate* * * *radio frequency energy* * * *and, if not installed* * * *and used in accordance* *with* * * *the* * * *instructions,* * * *may* * * *cause* * * *harmful* * * *interference* * * *to* * * *radio* * * *communications.* * * *However,* * * *there* * * *is* * * *no* * * *guarantee* * * *that* * * *interference* *will* * * *not* * * *occur* * * *in* * * *a* * * *particular* * * *installation.* * * *If* * * *this* * * *equipment* * * *does* * * *cause* * * *harmful* * * *interference* * * *to* * * *radio* * * *or* * * *television* * * *reception,* * * *which* *can* * * *be* * * *determined* * * *by* * * *turning* * * *the* * * *equipment* * * *off* * * *and* * * *on,* * * *the* * * *user* * * *is* * * *encouraged* * * *to* * * *try* * * *to* * * *correct* * * *the* * * *interference* * * *by* * * *one* * * *or* * * *more* *of the following measures:*

- * * *Reorient or relocate* * * *the receiving* * * *antenna.* - * * *Increase the separation between the equipment and receiver.* - * * *Connect the equipment into* * * *an* * * *outlet on* * * *a* * * *circuit different from that* * * *to which* * * *the receiver* * * *is* * * *connected.* - * * *Consult the dealer or an* * * *experienced* * * *radio/TV* * * *technician* * * *for* * * *help.* 3.2 * * *Canada*

3.2.1 *For EVMs issued* * * *with* * * *an* * * *Industry Canada* * * *Certificate of Conformance* * * *to RSS-210 or RSS-247*

**Concerning EVMs** ** ** **Including** ** ** **Radio Transmitters:**

This device complies with Industry Canada license-exempt RSSs. Operation is subject to the following two conditions:

(1) this device may not cause interference, and (2) this device must accept any interference, including interference that may cause undesired operation of the device.

**Concernant** ** ** **les EVMs** ** ** **avec appareils** ** ** **radio:**

Le présent appareil est conforme aux CNR d'Industrie Canada applicables aux appareils radio exempts de licence. L'exploitation est autorisée aux deux conditions suivantes: (1) l'appareil ne doit pas produire de brouillage, et (2) l'utilisateur de l'appareil doit accepter tout brouillage radioélectrique subi, même si le brouillage est susceptible d'en compromettre le fonctionnement.

**Concerning EVMs** ** ** **Including** ** ** **Detachable** ** ** **Antennas:**

Under Industry Canada regulations, this radio transmitter may only operate using an antenna of a type and maximum (or lesser) gain approved for the transmitter by Industry Canada. To reduce potential radio interference to other users, the antenna type and its gain should be so chosen that the equivalent isotropically radiated power (e.i.r.p.) is not more than that necessary for successful communication. This radio transmitter has been approved by Industry Canada to operate with the antenna types listed in the user guide with the maximum permissible gain and required antenna impedance for each antenna type indicated. Antenna types not included in this list, having a gain greater than the maximum gain indicated for that type, are strictly prohibited for use with this device. <https://www.ti.com>

**Concernant** ** ** **les EVMs** ** ** **avec antennes** ** ** **détachables**

Conformément à la réglementation d'Industrie Canada, le présent émetteur radio peut fonctionner avec une antenne d'un type et d'un gain maximal (ou inférieur) approuvé pour l'émetteur par Industrie Canada. Dans le but de réduire les risques de brouillage radioélectrique à l'intention des autres utilisateurs, il faut choisir le type d'antenne et son gain de sorte que la puissance isotrope rayonnée équivalente (p.i.r.e.) ne dépasse pas l'intensité nécessaire à l'établissement d'une communication satisfaisante. Le présent émetteur radio a été approuvé par Industrie Canada pour fonctionner avec les types d'antenne énumérés dans le manuel d'usage et ayant un gain admissible maximal et l'impédance requise pour chaque type d'antenne. Les types d'antenne non inclus dans cette liste, ou dont le gain est supérieur au gain maximal indiqué, sont strictement interdits pour l'exploitation de l'émetteur 3.3 * * *Japan*

3.3.1 *Notice* * * *for* * * *EVMs* * * *delivered* * * *in* * * *Japan:* Please see <http://www.tij.co.jp/lsds/ti\_ja/general/eStore/notice\_01.page> 日本国内に 輸入される評価用キット、ボードについては、次のところをご覧ください。

<https://www.ti.com/ja-jp/legal/notice-for-evaluation-kits-delivered-in-japan.html> 3.3.2 *Notice* * * *for* * * *Users* * * *of* * * *EVMs* * * *Considered* * * *"Radio* * * *Frequency* * * *Products"* * * *in* * * *Japan:* EVMs entering Japan may not be certified by TI as conforming to Technical Regulations of Radio Law of Japan.

If User uses EVMs in Japan, not certified to Technical Regulations of Radio Law of Japan, User is required to follow the instructions set forth by Radio Law of Japan, which includes, but is not limited to, the instructions below with respect to EVMs (which for the avoidance of doubt are stated strictly for convenience and should be verified by User):

1. Use EVMs in a shielded room or any other test facility as defined in the notification #173 issued by Ministry of Internal Affairs and Communications on March 28, 2006, based on Sub-section 1.1 of Article 6 of the Ministry's Rule for Enforcement of Radio Law of Japan, 2. Use EVMs only after User obtains the license of Test Radio Station as provided in Radio Law of Japan with respect to EVMs, or 3. Use of EVMs only after User obtains the Technical Regulations Conformity Certification as provided in Radio Law of Japan with respect to EVMs. Also, do not transfer EVMs, unless User gives the same notice above to the transferee. Please note that if User does not follow the instructions above, User will be subject to penalties of Radio Law of Japan.

【無線電波を送信する製品の開発キットをお使いになる際の注意事項】開発キットの中には技術基準適合証明を受けて

いないものがあります。技術適合証明を受けていないもののご使用に際しては、電波法遵守のため、以下のいずれかの 措置を取っていただく必要がありますのでご注意ください。

1. 電波法施行規則第 6 条第 1 項第 1 号に基づく平成 18 年 3 月 28 日総務省告示第 173 号で定められた電波暗室等の試験設備でご使用 いただく。 2. 実験局の免許を取得後ご使用いただく。 3. 技術基準適合証明を取得後ご使用いただく。

なお、本製品は、上記の「ご使用にあたっての注意」を譲渡先、移転先に通知しない限り、譲渡、移転できないものとします。

上記を遵守頂けない場合は、電波法の罰則が適用される可能性があることをご留意ください。日本テキサス・イ ンスツルメンツ株式会社 東京都新宿区西新宿６丁目２４番１号 西新宿三井ビル

3.3.3 *Notice for* * * *EVMs for* * * *Power Line Communication:* Please see <http://www.tij.co.jp/lsds/ti\_ja/general/eStore/notice\_02.page>

電力線搬送波通信についての開発キットをお使いになる際の注意事項については、次のところをご覧くださ い。 <https://www.ti.com/ja-jp/legal/notice-for-evaluation-kits-for-power-line-communication.html> 3.4 * * *European Union*

3.4.1 *For EVMs subject* * * *to EU Directive 2014/30/EU (Electromagnetic Compatibility* * * *Directive)*:

This is a class A product intended for use in environments other than domestic environments that are connected to a low-voltage power-supply network that supplies buildings used for domestic purposes. In a domestic environment this product may cause radio interference in which case the user may be required to take adequate measures. <https://www.ti.com>

*EVM* * * *Use Restrictions* * * *and Warnings:*

# 4.1 EVMS ARE NOT FOR USE IN FUNCTIONAL SAFETY AND/OR SAFETY CRITICAL EVALUATIONS, INCLUDING BUT NOT

LIMITED TO EVALUATIONS OF LIFE SUPPORT APPLICATIONS.

4.2 User must read and apply the user guide and other available documentation provided by TI regarding the EVM prior to handling or using the EVM, including without limitation any warning or restriction notices. The notices contain important safety information related to, for example, temperatures and voltages.

4.3 * * *Safety-Related Warnings* * * *and Restrictions:*

4.3.1 User shall operate the EVM within TI's recommended specifications and environmental considerations stated in the user guide, other available documentation provided by TI, and any other applicable requirements and employ reasonable and customary safeguards. Exceeding the specified performance ratings and specifications (including but not limited to input and output voltage, current, power, and environmental ranges) for the EVM may cause personal injury or death, or property damage. If there are questions concerning performance ratings and specifications, User should contact a TI field representative prior to connecting interface electronics including input power and intended loads. Any loads applied outside of the specified output range may also result in unintended and/or inaccurate operation and/or possible permanent damage to the EVM and/or interface electronics. Please consult the EVM user guide prior to connecting any load to the EVM output. If there is uncertainty as to the load specification, please contact a TI field representative. During normal operation, even with the inputs and outputs kept within the specified allowable ranges, some circuit components may have elevated case temperatures. These components include but are not limited to linear regulators, switching transistors, pass transistors, current sense resistors, and heat sinks, which can be identified using the information in the associated documentation. When working with the EVM, please be aware that the EVM may become very warm.

4.3.2 EVMs are intended solely for use by technically qualified, professional electronics experts who are familiar with the dangers and application risks associated with handling electrical mechanical components, systems, and subsystems. User assumes all responsibility and liability for proper and safe handling and use of the EVM by User or its employees, affiliates, contractors or designees. User assumes all responsibility and liability to ensure that any interfaces (electronic and/or mechanical) between the EVM and any human body are designed with suitable isolation and means to safely limit accessible leakage currents to minimize the risk of electrical shock hazard. User assumes all responsibility and liability for any improper or unsafe handling or use of the EVM by User or its employees, affiliates, contractors or designees.

4.4 User assumes all responsibility and liability to determine whether the EVM is subject to any applicable international, federal, state, or local laws and regulations related to User's handling and use of the EVM and, if applicable, User assumes all responsibility and liability for compliance in all respects with such laws and regulations. User assumes all responsibility and liability for proper disposal and recycling of the EVM consistent with all applicable international, federal, state, and local requirements.

5. *Accuracy* * * *of* * * *Information:* To the extent TI provides information on the availability and function of EVMs, TI attempts to be as accurate as possible. However, TI does not warrant the accuracy of EVM descriptions, EVM availability or other information on its websites as accurate, complete, reliable, current, or error-free. 6. *Disclaimers:*

# 6.1 EXCEPT AS SET FORTH ABOVE, EVMS AND ANY MATERIALS PROVIDED WITH THE EVM (INCLUDING, BUT NOT

LIMITED TO, REFERENCE DESIGNS AND THE DESIGN OF THE EVM ITSELF) ARE PROVIDED "AS IS" AND "WITH ALL FAULTS." TI DISCLAIMS ALL OTHER WARRANTIES, EXPRESS OR IMPLIED, REGARDING SUCH ITEMS, INCLUDING BUT NOT LIMITED TO ANY EPIDEMIC FAILURE WARRANTY OR IMPLIED WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF ANY THIRD PARTY PATENTS, COPYRIGHTS, TRADE SECRETS OR OTHER INTELLECTUAL PROPERTY RIGHTS.

# 6.2 EXCEPT FOR THE LIMITED RIGHT TO USE THE EVM SET FORTH HEREIN, NOTHING IN THESE TERMS SHALL BE

CONSTRUED AS GRANTING OR CONFERRING ANY RIGHTS BY LICENSE, PATENT, OR ANY OTHER INDUSTRIAL OR INTELLECTUAL PROPERTY RIGHT OF TI, ITS SUPPLIERS/LICENSORS OR ANY OTHER THIRD PARTY, TO USE THE EVM IN ANY FINISHED END-USER OR READY-TO-USE FINAL PRODUCT, OR FOR ANY INVENTION, DISCOVERY OR IMPROVEMENT, REGARDLESS OF WHEN MADE, CONCEIVED OR ACQUIRED.

# 7.

*USER'S* * * *INDEMNITY* * * *OBLIGATIONS* * * *AND* * * *REPRESENTATIONS.* USER WILL DEFEND, INDEMNIFY AND HOLD TI, ITS LICENSORS AND THEIR REPRESENTATIVES HARMLESS FROM AND AGAINST ANY AND ALL CLAIMS, DAMAGES, LOSSES, EXPENSES, COSTS AND LIABILITIES (COLLECTIVELY, "CLAIMS") ARISING OUT OF OR IN CONNECTION WITH ANY HANDLING OR USE OF THE EVM THAT IS NOT IN ACCORDANCE WITH THESE TERMS. THIS OBLIGATION SHALL APPLY WHETHER CLAIMS ARISE UNDER STATUTE, REGULATION, OR THE LAW OF TORT, CONTRACT OR ANY OTHER LEGAL THEORY, AND EVEN IF THE EVM FAILS TO PERFORM AS DESCRIBED OR EXPECTED. <https://www.ti.com>

8. *Limitations* * * *on* * * *Damages and Liability:*

# 8.1 General Limitations. IN NO EVENT SHALL TI BE LIABLE FOR ANY SPECIAL, COLLATERAL, INDIRECT, PUNITIVE,

INCIDENTAL, CONSEQUENTIAL, OR EXEMPLARY DAMAGES IN CONNECTION WITH OR ARISING OUT OF THESE TERMS OR THE USE OF THE EVMS, REGARDLESS OF WHETHER TI HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. EXCLUDED DAMAGES INCLUDE, BUT ARE NOT LIMITED TO, COST OF REMOVAL OR REINSTALLATION, ANCILLARY COSTS TO THE PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES, RETESTING, OUTSIDE COMPUTER TIME, LABOR COSTS, LOSS OF GOODWILL, LOSS OF PROFITS, LOSS OF SAVINGS, LOSS OF USE, LOSS OF DATA, OR BUSINESS INTERRUPTION. NO CLAIM, SUIT OR ACTION SHALL BE BROUGHT AGAINST TI MORE THAN TWELVE (12) MONTHS AFTER THE EVENT THAT GAVE RISE TO THE CAUSE OF ACTION HAS OCCURRED.

# 8.2 Specific Limitations. IN NO EVENT SHALL TI'S AGGREGATE LIABILITY FROM ANY USE OF AN EVM PROVIDED

HEREUNDER, INCLUDING FROM ANY WARRANTY, INDEMITY OR OTHER OBLIGATION ARISING OUT OF OR IN CONNECTION WITH THESE TERMS,, EXCEED THE TOTAL AMOUNT PAID TO TI BY USER FOR THE PARTICULAR EVM(S) AT ISSUE DURING THE PRIOR TWELVE (12) MONTHS WITH RESPECT TO WHICH LOSSES OR DAMAGES ARE CLAIMED. THE EXISTENCE OF MORE THAN ONE CLAIM SHALL NOT ENLARGE OR EXTEND THIS LIMIT.

9. *Return* * * *Policy.* Except as otherwise provided, TI does not offer any refunds, returns, or exchanges. Furthermore, no return of EVM(s) will be accepted if the package has been opened and no return of the EVM(s) will be accepted if they are damaged or otherwise not in a resalable condition. If User feels it has been incorrectly charged for the EVM(s) it ordered or that delivery violates the applicable order, User should contact TI. All refunds will be made in full within thirty (30) working days from the return of the components(s), excluding any postage or packaging costs.

10. *Governing* * * *Law:* These terms and conditions shall be governed by and interpreted in accordance with the laws of the State of Texas, without reference to conflict-of-laws principles. User agrees that non-exclusive jurisdiction for any dispute arising out of or relating to these terms and conditions lies within courts located in the State of Texas and consents to venue in Dallas County, Texas. Notwithstanding the foregoing, any judgment may be enforced in any United States or foreign court, and TI may seek injunctive relief in any United States or foreign court.

Mailing Address: Texas Instruments, Post Office Box 655303, Dallas, Texas 75265 Copyright © 2023, Texas Instruments Incorporated

# IMPORTANT NOTICE AND DISCLAIMER

# TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATA SHEETS), DESIGN RESOURCES (INCLUDING REFERENCE

DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES "AS IS" AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.

These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, regulatory or other requirements.

These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you will fully indemnify TI and its representatives against, any claims, damages, costs, losses, and liabilities arising out of your use of these resources.

TI's products are provided subject to TI's Terms of Sale or other applicable terms available either on ti.com or provided in conjunction with such TI products. TI's provision of these resources does not expand or otherwise alter TI's applicable warranties or warranty disclaimers for TI products.

TI objects to and rejects any additional or different terms you may have proposed. IMPORTANT NOTICE

Mailing Address: Texas Instruments, Post Office Box 655303, Dallas, Texas 75265 Copyright © 2023, Texas Instruments Incorporated