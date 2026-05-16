| Product | Folder |
|:--- |:--- |
| Sample & | Buy |
| Technical | Documents |
| Tools & | Software |
| Support & | Community | Sample & Buy Technical Documents Tools & Software Support & Community

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## TMS570LS1227 16- and 32-Bit RISC Flash Microcontroller

## Device Overview **1.1** **Features**

- • High-Performance Automotive-Grade - • Enhanced Timing Peripherals for Motor Control Microcontroller for Safety-Critical Applications - 7 Enhanced Pulse Width Modulator (ePWM) - Dual CPUs Running in Lockstep Modules - ECC on Flash and RAM Interfaces - 6 Enhanced Capture (eCAP) Modules - Built-In Self-Test (BIST) for CPU and On-chip - 2 Enhanced Quadrature Encoder Pulse (eQEP) RAMs Modules - Error Signaling Module With Error Pin - • Two Next Generation High-End Timer (N2HET) Modules - Voltage and Clock Monitoring

- N2HET1: 32 Programmable Channels - • ARM ® Cortex ® -R4F 32-Bit RISC CPU

- N2HET2: 18 Programmable Channels - 1.66 DMIPS/MHz With 8-Stage Pipeline

- 160-Word Instruction RAM Each With Parity - FPU With Single- and Double-Precision

Protection - 12-Region Memory Protection Unit (MPU)

- Each N2HET Includes Hardware Angle - Open Architecture With Third-Party Support Generator - • Operating Conditions - Dedicated High-End Timer Transfer Unit (HTU) - Up to 180-MHz System Clock for Each N2HET - Core Supply Voltage (VCC): 1.14 to 1.32 V - • Two 12-Bit Multibuffered ADC Modules - I/O Supply Voltage (VCCIO): 3.0 to 3.6 V - ADC1: 24 Channels - • Integrated Memory - ADC2: 16 Channels Shared With ADC1 - 1.25MB of Program Flash With ECC - 64 Result Buffers Each With Parity Protection - 192KB of RAM With ECC - • Multiple Communication Interfaces - 64KB of Flash for Emulated EEPROM With - 10/100 Mbps Ethernet MAC (EMAC) ECC - • IEEE 802.3 Compliant (3.3-V I/O Only) - • 16-Bit External Memory Interface (EMIF) - • Supports MII, RMII, and MDIO - • Common Platform Architecture - FlexRay Controller With 2 Channels - Consistent Memory Map Across Family - • 8KB of Message RAM With Parity Protection - Real-Time Interrupt (RTI) Timer (OS Timer)

- • Dedicated FlexRay Transfer Unit (FTU) - 128-Channel Vectored Interrupt Module (VIM)

- Three CAN Controllers (DCANs) - 2-Channel Cyclic Redundancy Checker (CRC)

- • 64 Mailboxes Each With Parity Protection - • Direct Memory Access (DMA) Controller

- • Compliant to CAN Protocol Version 2.0A and - 16 Channels and 32 Control Packets 2.0B - Parity Protection for Control Packet RAM - Inter-Integrated Circuit (I 2 C) - DMA Accesses Protected by Dedicated MPU - Three Multibuffered Serial Peripheral Interface - • Frequency-Modulated Phase-Locked Loop (MibSPI) Modules (FMPLL) With Built-In Slip Detector - • 128 Words Each With Parity Protection - • Separate Nonmodulating PLL - • 8 Transfer Groups - • IEEE 1149.1 JTAG, Boundary Scan and ARM - Up to Two Standard Serial Peripheral Interface CoreSight™Components (SPI) Modules - • Advanced JTAG Security Module (AJSM) - Two UART (SCI) Interfaces, One With Local - • Calibration Capabilities Interconnect Network (LIN 2.1) Interface - Parameter Overlay Module (POM) Support - • 16 General-Purpose Input/Output (GPIO) Pins - • Packages Capable of Generating Interrupts - 144-Pin Quad Flatpack (PGE) \[Green\] - 337-Ball Grid Array (ZWT) \[Green\]

An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications, intellectual property matters and other important disclaimers. PRODUCTION DATA.

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**> **1.2** **Applications**

- • Braking Systems (ABS and ESC) - • Active Driver Assistance Systems - • Electric Power Steering (EPS) - • Aerospace and Avionics - • HEV and EV Inverter Systems - • Railway Communications - • Battery Management Systems - • Off-road Vehicles **1.3** **Description**

The TMS570LS1227 device is a high-performance automotive-grade microcontroller family for safety systems. The safety architecture includes dual CPUs in lockstep, CPU and memory BIST logic, ECC on both the flash and the data SRAM, parity on peripheral memories, and loopback capability on peripheral I/Os.

The TMS570LS1227 device integrates the ARM Cortex-R4F floating-point CPU which offers an efficient 1.66 DMIPS/MHz, and has configurations which can run up to 180 MHz providing up to 298 DMIPS. The device supports the word-invariant big-endian \[BE32\] format.

The TMS570LS1227 device has 1.25MB of integrated flash and 192KB of data RAM with single-bit error correction and double-bit error detection. The flash memory on this device is a nonvolatile, electrically erasable and programmable memory, implemented with a 64-bit-wide data bus interface. The flash operates on a 3.3-V supply input (same level as I/O supply) for all read, program, and erase operations. When in pipeline mode, the flash operates with a system clock frequency of up to 180 MHz. The SRAM supports single-cycle read and write accesses in byte, halfword, word, and double-word modes throughout the supported frequency range.

The TMS570LS1227 device features peripherals for real-time control-based applications, including two Next Generation High-End Timer (N2HET) timing coprocessors with up to 44 I/O terminals, seven Enhanced Pulse Width Modulator (ePWM) modules with up to 14 outputs, six Enhanced Capture (eCAP) modules, two Enhanced Quadrature Encoder Pulse (eQEP) modules, and two 12-bit Analog-to-Digital Converters (ADCs) supporting up to 24 inputs.

The N2HET is an advanced intelligent timer that provides sophisticated timing functions for real-time applications. The timer is software-controlled, using a reduced instruction set, with a specialized timer micromachine and an attached I/O port. The N2HET can be used for pulse-width-modulated outputs, capture or compare inputs, or general-purpose I/O (GIO). The N2HET is especially well suited for applications requiring multiple sensor information and drive actuators with complex and accurate time pulses. A High-End Timer Transfer Unit (HTU) can perform DMA-type transactions to transfer N2HET data to or from main memory. A Memory Protection Unit (MPU) is built into the HTU.

The ePWM module can generate complex pulse width waveforms with minimal CPU overhead or intervention. The ePWM is easy to use and it supports both high-side and low-side PWM and deadband generation. With integrated trip zone protection and synchronization with the on-chip MibADC, the ePWM module is ideal for digital motor control applications.

The eCAP module is essential in systems where the accurately timed capture of external events is important. The eCAP can also be used to monitor the ePWM outputs or for simple PWM generation when the eCAP is not needed for capture applications.

The eQEP module is used for direct interface with a linear or rotary incremental encoder to get position, direction, and speed information from a rotating machine as used in high-performance motion and position-control systems.

*Device* * * *Overview* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

The device has two 12-bit-resolution MibADCs with 24 total inputs and 64 words of parity-protected buffer RAM each. The MibADC channels can be converted individually or can be grouped by software for sequential conversion sequences. Sixteen inputs are shared between the two MibADCs. Each MibADC supports three separate groupings of channels. Each group can be converted once when triggered or configured for continuous conversion mode. The MibADC has a 10-bit mode for use when compatibility with older devices or faster conversion time is desired. MibADC1 also supports the use of external analog multiplexers.

The device has multiple communication interfaces: three MibSPIs, two SPIs, one LIN, one SCI, three DCANs, one I 2 C, one Ethernet, and one FlexRay controller with two channels. The SPI provides a convenient method of serial high-speed communications between similar shift-register type devices. The LIN supports the Local Interconnect standard 2.0 and can be used as a UART in full-duplex mode using the standard Non-Return-to-Zero (NRZ) format. The DCAN supports the CAN 2.0 (A and B) protocol standard and uses a serial, multimaster communication protocol that efficiently supports distributed realtime control with robust communication rates of up to 1 Mbps. The DCAN is ideal for systems operating in noisy and harsh environments (for example, automotive and industrial fields) that require reliable serial communication or multiplexed wiring. The FlexRay controller uses a dual-channel serial, fixed time base multimaster communication protocol with communication rates of 10 Mbps per channel. A FlexRay Transfer Unit (FTU) enables autonomous transfers of FlexRay data to and from main CPU memory. Transfers are protected by a dedicated, built-in MPU. The Ethernet module supports MII, RMII, and MDIO interfaces.

The I2C module is a multimaster communication module providing an interface between the microcontroller and an I 2 C-compatible device through the I 2 C serial bus. The I 2 C supports speeds of 100 and 400 Kbps.

A Frequency-Modulated Phase-Locked Loop (FMPLL) clock module is used to multiply the external frequency reference to a higher frequency for internal use. The Global Clock Module (GCM) manages the mapping between the available clock sources and the device clock domains.

The device also has an External Clock Prescaler (ECP) module that when enabled, outputs a continuous external clock on the ECLK terminal. The ECLK frequency is a user-programmable ratio of the peripheral interface clock (VCLK) frequency. This low-frequency output can be monitored externally as an indicator of the device operating frequency.

The Direct Memory Access (DMA) controller has 16 channels, 32 control packets, and parity protection on its memory. An MPU is built into the DMA to protect memory against erroneous transfers.

The Error Signaling Module (ESM) monitors all device errors and determines whether an interrupt or external error pin (ball) is triggered when a fault is detected. The nERROR terminal can be monitored externally as an indicator of a fault condition in the microcontroller.

The External Memory Interface (EMIF) provides a memory extension to asynchronous and synchronous memories or other slave devices.

A Parameter Overlay Module (POM) enhances the calibration capabilities of application code. The POM can reroute flash accesses to internal memory or to the EMIF, thus avoiding the reprogramming steps necessary for parameter updates in flash.

With integrated safety features and a wide choice of communication and control peripherals, the TMS570LS1227 device is an ideal solution for high-performance real-time control applications with safetycritical requirements.

**Table 1-1.** ** ** **Device** ** ** **Information** **(1)**

| PART NUMBER | PACKAGE | BODY SIZE |
|:--- |:--- |:--- |
| TMS570LS1227ZWT | NFBGA (337) | 16.0 mm × 16.0 mm |
| TMS570LS1227PGE | LQFP (144) | 20.0 mm × 20.0 mm |

TMS570LS1227ZWT NFBGA (337) 16.0 mm \times 16.0 mm

TMS570LS1227PGE LQFP (144) 20.0 mm \times 20.0 mm

(1) For more information, see Section 9, * Mechanical* * * *Packaging and Orderable Information*.

Copyright © 2012-2015, Texas Instruments Incorporated *Device* * * *Overview* *Submit Documentation Feedback*

# HTU1 FTU HTU2 EMAC

Switched Central Resource Switched Central Resource

Main Cross Bar: Arbitration and Prioritization Control

CRC Switched Central Resource Peripheral Central Resource Bridge Dual Cortex-R4F CPUs in Lockstep EMAC Slaves Switched Central Resource

# DCAN1

# DCAN2

# DCAN3

# LIN

# SCI

# SPI4 64 KB Flash for EEPROM Emulation with ECC

# MDIO

# MII MibSPI1

# CAN1\_RX

CAN1\_TX CAN2\_RX CAN2\_TX CAN3\_RX CAN3\_TX MIBSPI1\_CLK MIBSPI1\_SIMO\[1:0\] MIBSPI1\_SOMI\[1:0\]

# MIBSPI1\_nCS\[5:0\] MIBSPI1\_nENA

# SPI2

# SPI2\_CLK

SPI2\_SIMO SPI2\_SOMI SPI2\_nCS\[1:0\] SPI2\_nENA MibSPI3

# MIBSPI3\_CLK

MIBSPI3\_SIMO MIBSPI3\_SOMI MIBSPI3\_nCS\[5:0\] MIBSPI3\_nENA

# SPI4\_CLK SPI4\_SIMO SPI4\_SOMI SPI4\_nCS0 SPI4\_nENA MibSPI5

# LIN\_RX LIN\_TX

# SCI\_RX SCI\_TX

# IOMM

# PMM

# VIM

# RTI

# DCC1

# DCC2

# 32K 32K 32K 192kB RAM with ECC

# DMA POM

# MDCLK

MDIO MII\_RXD\[3:0\] MII\_RXER MII\_TXD\[3:0\] MII\_TXEN MII\_TXCLK MII\_RXCLK MII\_CRS MII\_RXDV MII\_COL

# EMIF **# 2** **# 3** **# 4** **#** ** ** **1** **#** ** ** **2** **#** ** ** **1** always on Core/RAM RAM Core **#** ** ** **5**

## Color Legend for Power Domains

# SYS

# nPORRST nRST ECLK

# ESM nERROR 1.25MB Flash with ECC

# 32K 32K 32K

# eQEP 1,2 eQEPxA eQEPxB eQEPxS eQEPxI

# eCAP 1..6

# eCAP\[6:1\]

# ePWM 1..7

# nTZ\[3:1\] SYNCO SYNCI ePWMxA ePWMxB Switched Central Resource

# EMIF\_CLK

EMIF\_CKE EMIF\_nCS\[4:2\] EMIF\_nCS\[0\] EMIF\_ADDR\[12:0\] EMIF\_BA\[1:0\] EMIF\_DATA\[15:0\] EMIF\_nDQM\[1:0\] EMIF\_nOE EMIF\_nWE EMIF\_nRAS EMIF\_nCAS

# EMIF\_nWAIT

# I2C N2HET1 FlexRay GIO N2HET2

# I2C\_SCL

# I2C\_SDA

# FRAY\_RX1 FRAY\_TX1 FRAY\_TXEN1

# FRAY\_RX2 FRAY\_TX2 FRAY\_TXEN2

# GIOB\[7:0\]

# GIOA\[7:0\]

# N2HET2\[18,16\]

# N2HET2\[15:0\]

# N2HET1\[31:0\]

# N2HET1\_PIN\_nDIS

# N2HET2\_PIN\_nDIS MibADC1 MibADC2

# AD1EVT AD1IN\[7:0\]

# AD2EVT

| VSSAD | VCCAD |
|:--- |:--- |
| ADREFHI | ADREFLO |
| AD1IN\[15:8\] \\ | AD2IN\[15:8\] |
| AD1IN\[23:16\] \\ | AD2IN\[7:0\] |

# ADREFHI ADREFLO

# AD1IN\[15:8\] \\ AD2IN\[15:8\]

# AD1IN\[23:16\] \\ AD2IN\[7:0\]

# MIBSPI5\_SIMO\[3:0\]

MIBSPI5\_SOMI\[3:0\] MIBSPI5\_nCS\[3:0\] MIBSPI5\_nENA

# MIBSPI5\_CLK

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## 1.4 **Functional** ** ** **Block Diagram**

**NOTE** The block diagram reflects the 337BGA package. Some pins are multiplexed or not available in the 144QFP. For details, see the respective terminal functions tables in Section 4.3.

## Figure 1-1. Functional Block Diagram

*Device* * * *Overview* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## Table of Contents

**Device** ** ** **Overview**......................................... ** ** **1** 6.10 Flash Memory.......................................

| 1.1 | Features.............................................. | 6.11 | Tightly Coupled RAM Interface Module............. 84 |
| ---: |:--- | ---: |:--- |
| 1.2 | Applications........................................... | 6.12 | Parity Protection for Accesses to Peripheral RAMs |
| 1.3 | Description............................................ | 6.13 | On-Chip SRAM Initialization and Testing........... 86 |

1.2 Applications........................................... 6.12 Parity Protection for Accesses to Peripheral RAMs

1.3 Description............................................ 6.13 On-Chip SRAM Initialization and Testing........... 86

1.4 Functional Block Diagram............................ 4 6.14 External Memory Interface (EMIF).................. 89 **Revision** ** ** **History**......................................... ** ** **6** 6.15 Vectored Interrupt Manager......................... 97 **Device** ** ** **Comparison**..................................... ** ** **8** 6.16 DMA Controller..................................... **Terminal** ** ** **Configuration and Functions**............. ** ** **9** 6.17 Real Time Interrupt Module........................ 103

4.1 PGE QFP Package Pinout (144-Pin)................. 9 6.18 Error Signaling Module............................. 105

4.2 ZWT BGA Package Ball-Map (337 Ball Grid Array) 6.19 Reset / Abort / Error Sources...................... 109

4.3 Terminal Functions................................. 11 6.20 Digital Windowed Watchdog....................... 112 **Specifications**.......................................... ** ** **44** 6.21 Debug Subsystem................................. 113 5.1 Absolute Maximum Ratings Over Operating Free**Peripheral Information** ** ** **and Electrical** Air Temperature Range............................ **Specifications**......................................... ** ** **118** 5.2 ESD Ratings........................................ 7.1 Enhanced Translator PWM Modules (ePWM)..... 118 5.3 Power-On Hours (POH)............................. 7.2 Enhanced Capture Modules (eCAP)............... 123 5.4 Device Recommended Operating Conditions....... 45 7.3 Enhanced Quadrature Encoder (eQEP)........... 125 5.5 Switching Characteristics Over Recommended 7.4 Multibuffered 12bit Analog-to-Digital Converter.... 126 Operating Conditions for Clock Domains........... 46 7.5 General-Purpose Input/Output..................... 138 5.6 Wait States Required............................... 7.6 Enhanced High-End Timer (N2HET).............. 139 5.7 Power Consumption Over Recommended 7.7 FlexRay Interface.................................. Operating Conditions................................

7.8 Controller Area Network (DCAN).................. 145 5.8 Input/Output Electrical Characteristics Over

7.9 Local Interconnect Network Interface (LIN)........ 146 Recommended Operating Conditions............... 48

| 7.10 | Serial Communication Interface (SCI)............. 147 | 5.9 | Thermal Resistance Characteristics................ 48 |
| ---: |:--- | ---: |:--- |
| 7.11 | Inter-Integrated Circuit (I2C)....................... 148 | 5.10 | Output Buffer Drive Strengths...................... 49 |
| 7.12 | Multibuffered / Standard Serial Peripheral | 5.11 | Input Timings........................................ |

7.11 Inter-Integrated Circuit (I2C)....................... 148 5.10 Output Buffer Drive Strengths...................... 49

7.12 Multibuffered / Standard Serial Peripheral 5.11 Input Timings........................................

Interface............................................ 5.12 Output Timings......................................

7.13 Ethernet Media Access Controller................. 163 5.13 Low-EMI Output Buffers............................

**Device** ** ** **and Documentation** ** ** **Support**.............. ** ** **167** **System Information** ** ** **and Electrical**

8.1 Device and Development-Support Tool **Specifications**........................................... ** ** **54**

Nomenclature...................................... 6.1 Device Power Domains............................. 54

| 8.2 | Documentation Support............................ | 6.2 | Voltage Monitor Characteristics..................... 54 |
| ---: |:--- | ---: |:--- |
| 8.3 | Trademarks........................................ | 6.3 | Power Sequencing and Power On Reset........... 56 |
| 8.4 | Electrostatic Discharge Caution................... 169 | 6.4 | Warm Reset (nRST)................................. |
| 8.5 | Glossary............................................ | 6.5 | ARM Cortex-R4F CPU Information................. 59 |
| 8.6 | Device Identification................................ 170 | 6.6 | Clocks............................................... |

8.3 Trademarks........................................ 6.3 Power Sequencing and Power On Reset........... 56

8.4 Electrostatic Discharge Caution................... 169 6.4 Warm Reset (nRST).................................

8.5 Glossary............................................ 6.5 ARM Cortex-R4F CPU Information................. 59

8.6 Device Identification................................ 170 6.6 Clocks...............................................

8.7 Module Certifications............................... 6.7 Clock Monitoring.................................... 71 **Mechanical Packaging and Orderable** 6.8 Glitch Filters......................................... **Information**............................................. ** ** **179** 6.9 Device Memory Map................................ 74 9.1 Packaging Information............................. 179

Copyright © 2012-2015, Texas Instruments Incorporated *Table of Contents* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## Revision History

This data manual revision history highlights the technical changes made to the SPNS192A device-specific data manual addendum to make it an SPNS192B revision.

**Scope:** Applicable updates to the Hercules™TMS570 MCU device family, specifically relating to the TMS570LS1227 devices, which are now in the production data (PD) stage of development have been incorporated.

**Changes** ** ** **from** ** ** **September 1,** ** ** **2013** ** ** **to** ** ** **February 28, 2015** ** ** **(from** ** ** **A** ** ** **Revision** ** ** **(September 2013) to** ** ** **B** ** ** **Revision)** **Page**

- • Updated/Changed section title to "Device Overview"........................................................................... 1 - • Updated/changed the N2HET feature............................................................................................. 1 - • Added Table 1-1, * * *Device Information*.............................................................................................. - • Added Section 3, * * *Device Comparison*............................................................................................. - • Updated/Changed section title to "Terminal Configuration and Functions"................................................... 9 - • Table 4-2 (PGE Enhanced High-End Timer Modules (N2HET)) Updated/Changed N2HET1 time input capture or output compare pin description.................................................................................................... - • Table 4-2 Updated/Changed N2HET2 time input capture or output compare pin description............................ 14 - • Table 4-5 Updated/Changed the EPWM1SYNCI Signal Type from "Output" to "Input".................................... 15 - • Table 4-5 Updated/Changed the EPWM1SYNCI pin description from "Output" to "Input"................................. 15 - • Table 4-19 (PGE Test and Debug Modules Interface): Updated/Changed TEST pin description........................ 22 - • Table 4-25 (ZWT Enhanced High-End Timer Modules (N2HET)) Updated/Changed N2HET1 time input capture or output compare pin description................................................................................................ 26 - • Table 4-25 Updated/Changed N2HET2 time input capture or output compare pin description.......................... 27 - • Updated/Changed the EPWM1SYNCI pin description from "Output" to "Input"............................................ 29 - • Table 4-38: Added "receive" to the RMII\_CRS\_DV pin Description.......................................................... 34 - • Table 4-38: Added "receive" to the MII\_CRS pin Description................................................................. 34 - • Table 4-40 (External Memory Interface (EMIF)): Global: Deleted EMIF\_RNW pin function............................... 35 - • Table 4-43 (ZWT Test and Debug Modules Interface): Updated/Changed TEST pin description....................... 38 - • Updated/Changed section title to "Specifications"............................................................................. 44 - • Moved Storage temperature range, T stg back to Section 5.1, * * *Absolute Maximum* * * *Ratings Over Operating Free-* *Air* * * *Temperature* * * *Range*............................................................................................................ - • Added Section 5.2, * * *Handling Ratings (Automotive)*............................................................................ 44 - • Added Section 5.3, * * *Power-On-Hours (POH)*.................................................................................... 44 - • Moved * Thermal Data* section here................................................................................................ - • Section 5.9 (Thermal Resistance Characteristics): Updated/Changed title from "Thermal Data" to "Thermal Resistance Characteristics"........................................................................................................ - • Added Θ JA test conditions and added Ψ JT for PGE package.................................................................. 48 - • Added Θ JA test conditions and added Ψ JT for ZWT package.................................................................. 49 - • Clarified impact of SPI2PC9 register on drive strength of SPI2SOMI pin.................................................. 50 - • Changed the number of cycles of t v(RST) from 2252 to 2256................................................................... 58 - • Figure 6-7 (Device Clock Domains): Added VCLK4 (to ePWM, eQEP, eCAP)............................................. 68 - • Table 6-23 (Flash Memory Banks and Sectors): Added associated footnotes............................................. 81 - • Figure 6-11 (TCRAM Block Diagram): Updated/Changed figure............................................................. 84 - • Added table notes identifying address ranges of ESRAM PBIST groups................................................... 86 - • Updated/Changed N2HET2 RAM ending address from "0xFF **57** FFFF" to "0xFF **45** FFFF" in Table 6-27, * * *Memory* *Initialization*.......................................................................................................................... - • Updated EMIF Timings............................................................................................................ - • Changed maximum addressable size of asynchronous memories from 16MB to 32KB.................................. 89 - • Updated/Changed the EMIF address bus signals from "EMIF\_ADDR\[21:0\]" to "EMIF\_ADDR\[12:0\]" for all figures in Section 6.14.2, * * *Electrical* * * *and Timing Specifications*........................................................................ 89 - • Updated/Changed EMIF address from "EMIF\_ADDR\[21:0\]" to "EMIF\_ADDR\[12:0\]"...................................... 89 - • Changed EMIF t su(EMDV-EMOEH) from 30nS to 9nS................................................................................ 91 - • Changed EMIF t h(EMOEH-EMDIV) from 0.5nS to 0nS............................................................................... 91 - • Changed EMIF t su(EMOEL-EMWAIT) from 4E+30nS to 4E+9nS.................................................................... 91 - • Changed EMIF t su(EMWEL-EMWAIT) from 4E+30nS to 4E+14nS................................................................... 91 - • Changed EMIF t su(EMCEL-EMOEL) from (RS)\*E-5 to (RS)\*E-6..................................................................... 92 - • Changed EMIF t su(EMCEL-EMOEL) from -5 to -6..................................................................................... 92 - • Changed EMIF t h(EMOEH-EMCEH) from (RH)\*E -4 to (RH)\*E -3................................................................... 92

*Revision History* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

- • Changed EMIF t h(EMOEH-EMCEH) from (RH)\*E +4 to (RH)\*E +5.................................................................. 92 - • Changed EMIF t h(EMOEH-EMCEH) from -4 to -3...................................................................................... 92 - • Changed EMIF t h(EMOEH-EMCEH) from +4 to +5.................................................................................... 92 - • Changed EMIF t su(EMBAV-EMOEL) from (RS)\*E-5 to (RS)\*E-6..................................................................... 92 - • Changed EMIF t h(EMOEH-EMBAIV) from (RS)\*E-4 to (RS)\*E-3..................................................................... 92 - • Changed EMIF t su(EMAV-EMOEL) from (RS)\*E-5 to (RS)\*E-6...................................................................... 92 - • Changed EMIF t h(EMOEH-EMAIV) from (RS)\*E-4 to (RS)\*E-3...................................................................... 92 - • Changed EMIF t d(EMWAITH-EMOEH) from 3E-3 to 3E+9............................................................................ 92 - • Changed EMIF t d(EMWAITH-EMOEH) from 4E+30 to 4E+20......................................................................... 92 - • Changed EMIF t su(EMDQMV-EMOEL) from (RS)\*E-5 to (RS)\*E-6................................................................... 92 - • Changed EMIF t h(EMOEH-EMDQMIV) from (RS)\*E-4 to (RS)\*E-3................................................................... 92 - • Changed EMIF t su(EMCEL-EMWEL) from (WS)\*E -4 to (WS)\*E -3................................................................. 93 - • Changed EMIF t su(EMCEL-EMWEL) from -4 to -3..................................................................................... 93 - • Changed EMIF t h(EMWEH-EMCEH) from (WS)\*E -4 to (WS)\*E -3.................................................................. 93 - • Changed EMIF t h(EMWEH-EMCEH) from -4 to -3..................................................................................... 93 - • Changed EMIF t su(EMDQMV-EMWEL) from (WS)\*E -4 to (WS)\*E -3................................................................ 93 - • Changed EMIF t h(EMWEH-EMDQMIV) from (WS)\*E -4 to (WS)\*E -3................................................................ 93 - • Changed EMIF t su(EMBAV-EMWEL) from (WS)\*E -4 to (WS)\*E -3................................................................. 93 - • Changed EMIF t h(EMWEH-EMBAIV) from (WS)\*E -4 to (WS)\*E -3................................................................. 93 - • Changed EMIF t su(EMAV-EMWEL) from (WS)\*E -4 to (WS)\*E -3................................................................... 93 - • Changed EMIF t h(EMWEH-EMAIV) from (WS)\*E -4 to (WS)\*E -3................................................................... 93 - • Changed EMIF t d(EMWAITH-EMWEH) from 3E-4 to 3E+11........................................................................... 93 - • Changed EMIF t d(EMWAITH-EMWEH) from 4E+30 to 4E+24........................................................................ 93 - • Changed EMIF t su(EMDV-EMWEL) from (WS)\*E -4 to (WS)\*E -3.................................................................. 93 - • Changed EMIF t h(EMWEH-EMDIV) from (WS)\*E -4 to (WS)\*E -3................................................................... 93 - • Changed EMIF t su(EMDQMV-EMWEL) from (WS)\*E -4 to (WS)\*E -3................................................................ 93 - • Changed EMIF t h(EMWEH-EMDQMIV) from (WS)\*E -4 to (WS)\*E -3................................................................ 93 - • Added JTAG ID for revision C silicon.......................................................................................... 113 - • Revised description of ePWM Trip Zone Timing Requirement t w(TZ)........................................................ 122 - • Corrected SPI table note describing Master mode, phase = 0 condition.................................................. 155 - • Updated/Changed the parameter names and parametric descriptions for Section 7.13.1, * * *Ethernet MII Electrical* *and Timing Specifications*........................................................................................................ - • Updated/Changed "Ethernet RMII Timing" title to Section 7.13.2, " **Ethernet** ** ** **RMII Electrical** ** ** **and Timing** **Specifications** "................................................................................................................... - • Updated/Changed the parameter names and parametric descriptions for Section 7.13.1, * * *Ethernet RMII Electrical* *and Timing Specifications*........................................................................................................ - • Added Device Identification code for revision C silicon...................................................................... 170 - • Changed address of die identification registers............................................................................... 170 - • Updated/Changed the section title to "Mechanical Packaging and Orderable Information"............................. 179 - • Section 9.1 (Packaging Information): Updated/Changed paragraph........................................................ 179

Copyright © 2012-2015, Texas Instruments Incorporated *Revision History* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

# Device Comparison

# Table 3-1 lists the features of the TMS570LS1227 devices.

# Table 3-1. TMS570LS1227 Device Comparison (1)(2)

# FEATURES **DEVICES**

# Generic Part

**TMS570LS3137ZWT** (3) ** ** **TMS570LS1227ZWT** (3) TMS570LS1227PGE TMS570LS1114ZWT TMS570LS0714PGE TMS570LS0714PZ TMS570LS0432PZ Number

# Package

337 BGA 337 BGA 144 QFP 337 BGA 144 QFP 100 QFP 100 QFP

CPU ARM Cortex-R4F ARM Cortex-R4F ARM Cortex-R4F ARM Cortex-R4F ARM Cortex-R4F ARM Cortex-R4F ARM Cortex-R4 Frequency (MHz) Flash (KB)

# RAM (KB) Data Flash \[EEPROM\] (KB)

# EMAC 10/100 10/100 10/100 - - - - - - FlexRay 2-ch 2-ch 2-ch - - - -
# CAN

MibADC 2 (24ch) 2 (24ch) 2 (24ch) 2 (24ch) 2 (24ch) 2 (16ch) 1 (16ch) 12-bit (Ch)

# N2HET (Ch)

2 (44) 2 (44) 2 (40) 2 (44) 2 (40) 2 (21) 1 (19) ePWM Channels - - - eCAP Channels eQEP Channels

# MibSPI (CS)

3 (6 + 6 + 4) 3 (6 + 6 + 4) 3 (5 + 6 + 1) 3 (6 + 6 + 4) 3 (5 + 6 + 4) 2 (5 + 1) 1 (4)

# SPI (CS)

2 (2 + 1) 2 (2 + 1) 1 (1) 2 (2 + 1) 1 (1) 1 (1)

SCI (LIN) 2 (1 with LIN) 2 (1 with LIN) 2 (1 with LIN) 2 (1 with LIN) 2 (1 with LIN) 1 (with LIN) 1 (with LIN)

# I2C -
144 (with 16 interrupt 101 (with 16 interrupt 58 (with 4 interrupt 101 (with 16 interrupt 64 (with 10 interrupt 45 (with 9 interrupt 45 (with 8 interrupt GPIO (INT) (4)

capable) capable) capable) capable) capable) capable) capable)

EMIF 16-bit data 16-bit data - - 16-bit data - - - ETM (Trace) 32-bit - - - - - - -
# RTP/DMM YES - - - - - - -
Operating -40ºC to 125ºC -40ºC to 125ºC -40ºC to 125ºC -40ºC to 125ºC -40ºC to 125ºC -40ºC to 125ºC -40ºC to 125ºC Temperature

Core Supply (V) 1.14 V - 1.32 V 1.14 V - 1.32 V 1.14 V - 1.32 V 1.14 V - 1.32 V 1.14 V - 1.32 V 1.14 V - 1.32 V 1.14 V - 1.32 V

# I/O Supply (V)

3.0 V - 3.6 V 3.0 V - 3.6 V 3.0 V - 3.6 V 3.0 V - 3.6 V 3.0 V - 3.6 V 3.0 V - 3.6 V 3.0 V - 3.6 V

## (1)

For additional device variants, see <https://www.ti.com/tms570> (2) This table reflects the maximum configuration for each peripheral. Some functions are multiplexed and not all pins are available at the same time. (3) Superset device. (4) Total number of pins that can be used as general purpose input or output when not used as part of a peripheral.

## Device Comparison

Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# FRAYTXEN2

# nTRST

# AD1IN\[10\] / AD2IN\[10\]

# FRAYTX2 FRAYRX2 MIBSPI3NCS\[3\] MIBSPI3NCS\[2\]

# N2HET1\[11\]

FLTP1 FLTP2 GIOA\[2\] VCCIO VSS CAN3RX CAN3TX GIOA\[5\] N2HET1\[22\] GIOA\[6\] VCC OSCIN Kelvin\_GND OSCOUT VSS

# GIOA\[7\]

N2HET1\[1\] N2HET1\[3\] N2HET1\[0\] VCCIO VSS VSS VCC N2HET1\[2\] N2HET1\[5\] MIBSPI5NCS\[0\] N2HET1\[7\] TEST N2HET1\[9\] N2HET1\[4\]

# MIBSPI3NCS\[1\]

N2HET1\[6\] N2HET1\[13\] MIBSPI1NCS\[2\] N2HET1\[15\] VCCIO VSS VSS VCC nPORRST VSS VCC VCC VSS MIBSPI3SOMI MIBSPI3SIMO MIBSPI3CLK MIBSPI3NENA MIBSPI3NCS\[0\] VSS VCC AD1IN\[16\] / AD2IN\[0\] AD1IN\[17\] / AD2IN\[1\] AD1IN\[0\] AD1IN\[7\] AD1IN\[18\] / AD2IN\[2\] AD1IN\[19\] / AD2IN\[3\] AD1IN\[20\] / AD2IN\[4\] AD1IN\[21\] / AD2IN\[5\] ADREFHI ADREFLO VSSAD VCCAD AD1IN\[9\] / AD2IN\[9\] AD1IN\[1\]

# AD1IN\[2\]

AD1IN\[3\] AD1IN\[11\] / AD2IN\[11\] AD1IN\[4\] AD1IN\[12\] / AD2IN\[12\] AD1IN\[5\] AD1IN\[13\] / AD2IN\[13\] AD1IN\[6\] AD1IN\[22\] / AD2IN\[6\] AD1IN\[14\] / AD2IN\[14\] AD1IN\[8\] / AD2IN\[8\] AD1IN\[23\] / AD2IN\[7\] AD1IN\[15\] / AD2IN\[15\] AD1EVT VCC VSS CAN1TX CAN1RX N2HET1\[24\] N2HET1\[26\] MIBSPI1SIMO MIBSPI1SOMI MIBSPI1CLK MIBSPI1NENA MIBSPI5NENA MIBSPI5SOMI\[0\] MIBSPI5SIMO\[0\] MIBSPI5CLK VCC VSS VSS VCCIO

# N2HET1\[8\] N2HET1\[28\] TMS

# TDI

TDO TCK RTCK VCC VSS nRST nERROR N2HET1\[10\] ECLK VCCIO VSS VSS VCC N2HET1\[12\] N2HET1\[14\] FRAYRX1 N2HET1\[30\] CAN2TX CAN2RX MIBSPI1NCS\[1\] LINRX LINTX FRAYTX1 VCCP

# VSS

VCCIO VCC VSS N2HET1\[16\] N2HET1\[18\] N2HET1\[20\] FRAYTXEN1 VCC VSS

# MIBSPI1NCS\[0\]

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

# Terminal Configuration and Functions

## 4.1

**PGE** ** ** **QFP Package** ** ** **Pinout** ** ** **(144-Pin)**

## Figure 4-1. PGE QFP Package Pinout (144-Pin)

## Note: Pins can have multiplexed functions. Only the default function is depicted in above diagram.

Copyright © 2012-2015, Texas Instruments Incorporated *Terminal Configuration and Functions* *Submit Documentation Feedback*

# A

**B** **C** **D** **E** **F** **G** **H** **J** **K** **L** **M** **N** **P** **R** **T** **U** **V** **W**

# VSS **VSS** **TMS** **N2HET1** **\[10\]**

| MIBSPI5 | NCS\[0\] |
|:--- |:--- |
| MIBSPI1 | SIMO |
| MIBSPI1 | NENA |
| MIBSPI5 | CLK |
| MIBSPI5 | SIMO\[0\] |

# MIBSPI1 **SIMO**

# MIBSPI1 **NENA**

# MIBSPI5 **CLK**

# MIBSPI5 **SIMO\[0\]**

# N2HET1 **\[28\]** **NC** **CAN3RX** **AD1EVT**

# AD1IN\[15\] **/** **AD2IN\[15\]**

# AD1IN\[22\] **/** **AD2IN\[6\]**

# AD1IN **\[6\]**

# AD1IN\[11\] **/** **AD2IN\[11\]**

# VSSAD **VSSAD**

# VSS

**TCK** **TDO** **nTRST** **N2HET1** **\[8\]**

| MIBSPI1 | CLK |
|:--- |:--- |
| MIBSPI1 | SOMI |
| MIBSPI5 | NENA |
| MIBSPI5 | SOMI\[0\] |

# MIBSPI1 **SOMI**

# MIBSPI5 **NENA**

# MIBSPI5 **SOMI\[0\]**

# N2HET1 **\[0\]** **NC** **CAN3TX** **NC**

| AD1IN\[8\] | / | AD2IN\[8\] |
|:--- |:--- |:--- |
| AD1IN\[14\] | / | AD2IN\[14\] |
| AD1IN\[13\] | / | AD2IN\[13\] |

# AD1IN\[14\] **/** **AD2IN\[14\]**

# AD1IN\[13\] **/** **AD2IN\[13\]**

# AD1IN **\[4\]**

# AD1IN **\[2\]** **VSSAD**

# TDI **nRST** **NC** **EMIF\_** **nWE**

# MIBSPI5

**SOMI\[1\]** **NC** **MIBSPI5** **SIMO\[3\]**

| MIBSPI5 | SIMO\[2\] |
|:--- |:--- |
| N2HET1 | \[31\] |
| EMIF\_ | nCS\[3\] |
| EMIF\_ | nCS\[2\] |
| EMIF\_ | nCS\[4\] |

# N2HET1 **\[31\]**

# EMIF\_ **nCS\[3\]**

# EMIF\_ **nCS\[2\]**

# EMIF\_ **nCS\[4\]**

# EMIF\_ **nCS\[0\]** **NC** **AD1IN** **\[5\]**

# AD1IN **\[3\]**

# AD1IN\[10\] **/** **AD2IN\[10\]**

# AD1IN **\[1\]**

# AD1IN\[9\] **/** **AD2IN\[9\]**

# RTCK

**FRAY** **TXEN1** **NC** **EMIF\_** **BA\[1\]**

# MIBSPI5

**SIMO\[1\]** **NC** **MIBSPI5** **SOMI\[3\]**

# MIBSPI5

**SOMI\[2\]** **NC** **NC** **NC** **NC** **NC** **NC**

| AD1IN\[23\] | / | AD2IN\[7\] |
|:--- |:--- |:--- |
| AD1IN\[12\] | / | AD2IN\[12\] |
| AD1IN\[19\] | / | AD2IN\[3\] |

# AD1IN\[12\] **/** **AD2IN\[12\]**

# AD1IN\[19\] **/** **AD2IN\[3\]**

# ADREFLO **VSSAD**

# FRAY **RX1**

# FRAY

**TX1** **NC** **NC** **NC** **NC** **NC** **NC** **NC** **EMIF\_** **DATA\[0\]**

# EMIF\_ **DATA\[1\]**

# EMIF\_ **DATA\[2\]**

# EMIF\_ **DATA\[3\]** **NC** **NC**

# AD1IN\[21\] **/** **AD2IN\[5\]**

# AD1IN\[20\] **/** **AD2IN\[4\]**

# ADREFHI **VCCAD**

# N2HET1

**\[26\]** **nERROR** **NC** **NC** **NC** **VCCIO** **VCCIO** **VCCIO** **VCC** **VCC** **VCCIO** **VCCIO** **VCCIO** **VCCIO** **NC** **NC**

# AD1IN\[18\] **/** **AD2IN\[2\]**

| AD1IN | \[7\] |
|:--- |:--- |
| AD1IN | \[0\] |
| N2HET1 | \[17\] |

# AD1IN **\[0\]**

# N2HET1 **\[17\]**

# N2HET1

**\[19\]** **NC** **NC** **EMIF\_BA\[0\]** **VCCIO** **VCCIO** **NC** **NC**

# AD1IN\[17\] **/** **AD2IN\[1\]**

# AD1IN\[16\] **/** **AD2IN\[0\]**

# NC

# ECLK

**N2HET1** **\[4\]** **NC** **NC** **EMIF\_nOE** **VCCIO** **VSS** **VSS** **VCC** **VSS** **VSS** **VCCIO** **NC** **MIBSPI5** **NCS\[3\]** **NC** **NC** **NC**

# N2HET1 **\[14\]**

# N2HET1

**\[30\]** **NC** **NC** **EMIF\_** **nDQM\[1\]** **VCCIO** **VSS** **VSS** **VSS** **VSS** **VSS** **VCCPLL** **NC** **NC** **NC** **NC** **NC**

# CAN1TX

**CAN1RX** **EMIF\_** **ADDR\[12\]** **NC** **EMIF\_** **nDQM\[0\]** **VCC** **VCC** **VSS** **VSS** **VSS** **VCC** **VCC** **NC** **NC** **NC** **MIBSPI3** **NCS\[0\]** **GIOB\[3\]**

# N2HET1 **\[27\]**

# FRAY **TXEN2**

# EMIF\_

**ADDR\[11\]** **NC** **EMIF\_** **ADDR\[5\]** **VCC** **VSS** **VSS** **VSS** **VSS** **VSS** **VCCIO** **EXTCLKI** **N2** **NC** **NC** **MIBSPI3** **CLK**

| MIBSPI3 | NENA |
|:--- |:--- |
| FRAY | RX2 |
| FRAY | TX2 |

# FRAY **RX2**

# FRAY **TX2**

# EMIF\_

**ADDR\[10\]** **NC** **EMIF\_** **ADDR\[4\]** **VCCP** **VSS** **VSS** **VCC** **VSS** **VSS** **VCCIO** **EMIF\_** **DATA\[15\]** **NC** **NC** **MIBSPI3** **SOMI**

# MIBSPI3 **SIMO**

# LINRX

**LINTX** **EMIF\_** **ADDR\[9\]** **NC** **EMIF\_** **ADDR\[3\]** **VCCIO** **VCCIO** **EMIF\_** **DATA\[14\]** **NC** **NC** **N2HET1** **\[9\]** **nPORRST** ** ** **7**

# GIOA\[4\] **MIBSPI5** **NCS\[1\]**

# EMIF\_

**ADDR\[8\]** **NC** **EMIF\_** **ADDR\[2\]** **VCCIO** **VCCIO** **VCCIO** **VCCIO** **VCC** **VCC** **VCCIO** **VCCIO** **VCCIO** **EMIF\_** **DATA\[13\]** **NC** **NC** **N2HET1** **\[5\]**

# MIBSPI5 **NCS\[2\]**

# GIOA\[0\] **GIOA\[5\]** **EMIF\_** **ADDR\[7\]**

# EMIF\_ **ADDR\[1\]**

# EMIF\_ **DATA\[4\]**

# EMIF\_ **DATA\[5\]**

# EMIF\_

**DATA\[6\]** **FLTP2** **FLTP1** **EMIF\_** **DATA\[7\]**

# EMIF\_ **DATA\[8\]**

# EMIF\_ **DATA\[9\]**

# EMIF\_ **DATA\[10\]**

# EMIF\_ **DATA\[11\]**

# EMIF\_

**DATA\[12\]** **NC** **NC** **MIBSPI3** **NCS\[1\]**

| N2HET1 | \[2\] |
|:--- |:--- |
| N2HET1 | \[16\] |
| N2HET1 | \[12\] |
| EMIF\_ | ADDR\[6\] |

# N2HET1 **\[16\]**

# N2HET1 **\[12\]**

# EMIF\_ **ADDR\[6\]**

# EMIF\_

**ADDR\[0\]** **NC** **NC** **NC** **N2HET1** **\[21\]**

# N2HET1

**\[23\]** **NC** **NC** **NC** **NC** **NC** **EMIF\_** **nCAS** **NC** **NC** **NC** **NC**

| N2HET1 | \[29\] |
|:--- |:--- |
| N2HET1 | \[22\] |
| MIBSPI3 | NCS\[3\] |
| SPI2 | NENA |
| N2HET1 | \[11\] |
| MIBSPI1 | NCS\[1\] |

# N2HET1 **\[22\]**

# MIBSPI3 **NCS\[3\]**

# SPI2 **NENA**

# N2HET1 **\[11\]**

# MIBSPI1 **NCS\[1\]**

# MIBSPI1

**NCS\[2\]** **GIOA\[6\]** **MIBSPI1** **NCS\[3\]**

| EMIF\_ | CLK |
|:--- |:--- |
| EMIF\_ | CKE |
| N2HET1 | \[25\] |
| SPI2 | NCS\[0\] |
| EMIF\_ | nWAIT |

# EMIF\_ **CKE**

# N2HET1 **\[25\]**

# SPI2 **NCS\[0\]**

# EMIF\_ **nWAIT**

# EMIF\_

**nRAS** **NC** **NC** **NC** **N2HET1** **\[6\]**

# VSS

**MIBSPI3** **NCS\[2\]** **GIOA\[1\]** **SPI2** **SOMI** **SPI2 CLK** **GIOB\[2\]** **GIOB\[5\]** **CAN2TX** **GIOB\[6\]** **GIOB\[1\]** **KELVIN\_** **GND** **GIOB\[0\]** **N2HET1** **\[13\]**

# N2HET1 **\[20\]**

# MIBSPI1

**NCS\[0\]** **NC** **TEST** **N2HET1** **\[1\]** **VSS**

# VSS

**VSS** **GIOA\[2\]** **SPI2** **SIMO** **GIOA\[3\]** **GIOB\[7\]** **GIOB\[4\]** **CAN2RX** **N2HET1** **\[18\]** **OSCIN** **OSCOUT** **GIOA\[7\]** **N2HET1** **\[15\]**

# N2HET1 **\[24\]** **NC** **N2HET1** **\[7\]**

# N2HET1 **\[3\]** **VSS** **VSS**

# A

**B** **C** **D** **E** **F** **G** **H** **J** **K** **L** **M** **N** **P** **R** **T** **U** **V** **W**

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

# 4.2

**ZWT BGA Package** ** ** **Ball-Map (337 Ball Grid Array)**

# Figure 4-2. ZWT Package Pinout. Top View

# Note: Balls can have multiplexed functions. Only the default function is depicted in above diagram.

# Terminal Configuration and Functions

Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **4.3** **Terminal Functions**

Section 4.3.1 and Section 4.3.2 identify the external signal names, the associated pin/ball numbers along with the mechanical package designator, the pin/ball type (Input, Output, IO, Power or Ground), whether the pin/ball has any internal pullup/pulldown, whether the pin/ball can be configured as a GPIO, and a functional pin/ball description. The first signal name listed is the primary function for that terminal. The signal name in ** ** **Bold** is the function being described. Refer to the I/O Multiplexing Module (IOMM) chapter of the TMS570LS12x/11x Technical Reference Manual ( SPNU515 ).

**NOTE** In the Terminal Functions table below, the "Reset Pull State" is the state of the pull applied to the terminal while nPORRST is low and immediately after nPORRST goes High. The default pull direction may change when software configures the pin for an alternate function. The "Pull Type" is the type of pull asserted when the signal name in bold is enabled for the given terminal by the IOMM control registers.

All I/O signals except nRST are configured as inputs while nPORRST is low and immediately after nPORRST goes High. While nPORRST is low, the input buffers are disabled, and the output buffers are disabled with the default pulls enabled.

All output-only signals have the output buffer disabled and the default pull enabled while nPORRST is low, and are configured as outputs with the pulls disabled immediately after nPORRST goes High. ***4.3.1*** ***PGE*** *** *** ***Package***

**4.3.1.1** **Multibuffered Analog-to-Digital Converters (MibADC)**

**Table 4-1. PGE Multibuffered Analog-to-Digital** ** ** **Converters (MibADC1,** ** ** **MibADC2)**

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **PGE**

**ADREFHI** (1) Power N/A None ADC high reference supply

**ADREFLO** (1) Power ADC low reference supply **VCCAD** (1) Power Operating supply for ADC **VSSAD** (1) Ground

**AD1EVT** /MII\_RX\_ER/RMII\_RX\_ER I/O Pull Down Programmable, ADC1 event trigger input, 20 µA or GPIO

MIBSPI3NCS\[0\]/ **AD2EVT** /GIOB\[2\]/ I/O Pull Up Programmable, ADC2 event trigger input, EQEP1I/N2HET2\_PIN\_nDIS 20 µA or GPIO

**AD1IN\[0\]** Input N/A None ADC1 analog input

# AD1IN\[1\]

# AD1IN\[2\]

# AD1IN\[3\]

# AD1IN\[4\]

# AD1IN\[5\]

# AD1IN\[6\]

# AD1IN\[7\]

(1) The ADREFHI, ADREFLO, VCCAD and VSSAD connections are common for both ADC cores.

Copyright © 2012-2015, Texas Instruments Incorporated *Terminal Configuration and Functions* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## Table 4-1. PGE Multibuffered Analog-to-Digital Converters (MibADC1, MibADC2) (continued)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **PGE**

**AD1IN\[8\]** / AD2IN\[8\] Input N/A None ADC1/ADC2 shared analog inputs **AD1IN\[9\]** / AD2IN\[9\]

# AD1IN\[10\] / AD2IN\[10\]

# AD1IN\[11\] / AD2IN\[11\]

# AD1IN\[12\] / AD2IN\[12\]

# AD1IN\[13\] / AD2IN\[13\]

# AD1IN\[14\] / AD2IN\[14\]

# AD1IN\[15\] / AD2IN\[15\]

# AD1IN\[16\] / AD2IN\[0\]

# AD1IN\[17\] / AD2IN\[1\]

# AD1IN\[18\] / AD2IN\[2\]

# AD1IN\[19\] / AD2IN\[3\]

# AD1IN\[20\] / AD2IN\[4\]

# AD1IN\[21\] / AD2IN\[5\]

# AD1IN\[22\] / AD2IN\[6\]

# AD1IN\[23\] / AD2IN\[7\]

| MIBSPI3SOMI\[0\]/AWM1\_EXT\_ENA/ECAP2 | Output | Pull Up | None | AWM1 external analog | mux enable |
|:--- |:--- |:--- |:--- |:--- |:--- |
| MIBSPI3SIMO\[0\]/AWM1\_EXT\_SEL\[0\]/ECAP3 | Output | Pull Up | None | AWM1 external analog | mux select line0 |
| MIBSPI3CLK/AWM1\_EXT\_SEL\[1\]/EQEP1A | Output | Pull Up | None | AWM1 external analog | mux select line0 |

MIBSPI3SIMO\[0\]/ **AWM1\_EXT\_SEL\[0\]** /ECAP3 Output Pull Up None AWM1 external analog mux select line0

MIBSPI3CLK/ **AWM1\_EXT\_SEL\[1\]** /EQEP1A Output Pull Up None AWM1 external analog mux select line0

*Terminal Configuration and Functions* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 4.3.1.2 **Enhanced High-End Timer Modules (N2HET)**

## Table 4-2. PGE Enhanced High-End Timer Modules (N2HET)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **PGE**

**N2HET1\[0\]** /SPI4CLK/EPWM2B I/O Pull Down Programmable, N2HET1 time input 20 µA **N2HET1\[1\]** /SPI4NENA/N2HET2\[8\]/EQEP2A capture or output compare, or GIO. **N2HET1\[2\]** /SPI4SIMO\[0\]/EPWM3A

Each terminal has a **N2HET1\[3\]** /SPI4NCS\[0\]/N2HET2\[10\]/EQEP2B

suppression filter with a **N2HET1\[4\]** /EPWM4B programmable duration. **N2HET1\[5\]** /SPI4SOMI\[0\]/N2HET2\[12\]/EPWM3B

# N2HET1\[6\] /SCIRX/EPWM5A

# N2HET1\[7\] /N2HET2\[14\]/EPWM7B

# N2HET1\[8\] /MIBSPI1SIMO\[1\]/MII\_TXD\[3\]

# N2HET1\[9\] /N2HET2\[16\]/EPWM7A

# N2HET1\[10\] /MII\_TXCLK/MII\_TX\_VCLKA4/nTZ3

# N2HET1\[11\] /MIBSPI3NCS\[4\]/N2HET2\[18\]/ EPWM1SYNCO

# N2HET1\[12\] /MII\_CRS/RMII\_CRS\_DV

# N2HET1\[13\] /SCITX/EPWM5B

# N2HET1\[14\]

# N2HET1\[15\] /MIBSPI1NCS\[4\]/ECAP1

# N2HET1\[16\] /EPWM1SYNCI/EPWM1SYNCO

# MIBSPI1NCS\[1\]/ N2HET1\[17\] /MII\_COL/EQEP1S Pull Up **N2HET1\[18\]** /EPWM6A Pull Down

# MIBSPI1NCS\[2\]/ N2HET1\[19\] /MDIO Pull Up **N2HET1\[20\]** /EPWM6B Pull Down

# N2HET1\[22\]

# MIBSPI1NENA/ N2HET1\[23\] /MII\_RXD\[2\]/ECAP4 Pull Up

# N2HET1\[24\] /MIBSPI1NCS\[5\]/MII\_RXD\[0\]/RMII\_RXD\[0\] Pull Down

# MIBSPI3NCS\[1\]/ N2HET1\[25\] /MDCLK Pull Up

# N2HET1\[26\] /MII\_RXD\[1\]/RMII\_RXD\[1\] Pull Down

# MIBSPI3NCS\[2\]/I2C\_SDA/ N2HET1\[27\] /nTZ2 Pull Up

# N2HET1\[28\] /MII\_RXCLK/RMII\_REFCLK/MII\_RX\_VCLKA4 Pull Down

# MIBSPI3NCS\[3\]/I2C\_SCL/ N2HET1\[29\] /nTZ1 Pull Up

# N2HET1\[30\] /MII\_RX\_DV/EQEP2S Pull Down

# MIBSPI3NENA/MIBSPI3NCS\[5\]/ N2HET1\[31\] /EQEP1B Pull Up

Copyright © 2012-2015, Texas Instruments Incorporated *Terminal Configuration and Functions* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## Table 4-2. PGE Enhanced High-End Timer Modules (N2HET) (continued)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **PGE**

GIOA\[5\]/EXTCLKIN/EPWM1A/ **N2HET1\_PIN\_nDIS** I/O Pull Down Programmable, Disable selected PWM 20 µA (1) outputs

GIOA\[2\]/ **N2HET2\[0\]** / EQEP2I I/O Pull Down Programmable, N2HET2 time input 20 µA GIOA\[6\]/ **N2HET2\[4\]** /EPWM1B capture or output compare, or GPIO GIOA\[7\]/ **N2HET2\[6\]** /EPWM2A

Each terminal has a N2HET1\[1\]/SPI4NENA/ **N2HET2\[8\]** /EQEP2A

suppression filter with a N2HET1\[3\]/SPI4NCS\[0\]/ **N2HET2\[10\]** /EQEP2B programmable duration. N2HET1\[5\]/SPI4SOMI\[0\]/ **N2HET2\[12\]** /EPWM3B

# N2HET1\[7\]/ N2HET2\[14\] /EPWM7B

# N2HET1\[9\]/ N2HET2\[16\] /EPWM7A

# N2HET1\[11\]/MIBSPI3NCS\[4\]/ N2HET2\[18\] / EPWM1SYNCO

MIBSPI3NCS\[0\]/AD2EVT/GIOB\[2\]/ I/O Pull Up Programmable, Disable selected PWM EQEP1I/ **N2HET2\_PIN\_nDIS** 20 µA (1) outputs

(1) The N2HETx\_PIN\_nDIS function is always available on this terminal. There is no mux control to select this function. The pull direction is controlled by the function which is selected by the output mux control for this terminal.

## 4.3.1.3 **Enhanced Capture Modules (eCAP)**

**Table 4-3. PGE Enhanced Capture Modules (eCAP)** **(1)**

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **PGE**

N2HET1\[15\]/MIBSPI1NCS\[4\]/ **ECAP1** I/O Pull Down Fixed 20 µA Enhanced Capture Pull Up Module 1 I/O

MIBSPI3SOMI\[0\]/AWM1\_EXT\_ENA/ **ECAP2** Pull Up Enhanced Capture Module 2 I/O

| MIBSPI3SIMO\[0\]/AWM1\_EXT\_SEL\[0\]/ECAP3 | Enhanced Capture | Module 3 I/O |
|:--- |:--- |:--- |
| MIBSPI1NENA/N2HET1\[23\]/MII\_RXD\[2\]/ECAP4 | Enhanced Capture | Module 4 I/O |
| MIBSPI5NENA/MII\_RXD\[3\]/MIBSPI5SOMI\[1\]/ ECAP5 | Enhanced Capture | Module 5 I/O |
| MIBSPI1NCS\[0\]/MIBSPI1SOMI\[1\]/MII\_TXD\[2\]/ECAP6 | Enhanced Capture | Module 6 I/O |

MIBSPI1NENA/N2HET1\[23\]/MII\_RXD\[2\]/ **ECAP4** Enhanced Capture Module 4 I/O

MIBSPI5NENA/MII\_RXD\[3\]/MIBSPI5SOMI\[1\]/ ** ** **ECAP5** Enhanced Capture Module 5 I/O

MIBSPI1NCS\[0\]/MIBSPI1SOMI\[1\]/MII\_TXD\[2\]/ **ECAP6** Enhanced Capture Module 6 I/O

(1) These signals, when used as inputs, are double-synchronized and then optionally filtered with a 6-cycle VCLK4-based counter.

*Terminal Configuration and Functions* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 4.3.1.4

**Enhanced Quadrature Encoder Pulse** ** ** **Modules (eQEP)**

**Table 4-4. PGE Enhanced Quadrature Encoder Pulse Modules (eQEP)** **(1)**

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **PGE**

MIBSPI3CLK/AWM1\_EXT\_SEL\[1\]/ **EQEP1A** Input Pull Up Fixed 20 µA Enhanced QEP1 Input A Pull Up MIBSPI3NENA/MIBSPI3NCS\[5\]/N2HET1\[31\]/ **EQEP1B** Input Enhanced QEP1 Input B

# MIBSPI3NCS\[0\]/AD2EVT/GIOB\[2\]/

I/O Enhanced QEP1 Index **EQEP1I** /N2HET2\_PIN\_nDIS

# MIBSPI1NCS\[1\]/N2HET1\[17\]/MII\_COL/ EQEP1S I/O Enhanced QEP1 Strobe

N2HET1\[1\]/SPI4NENA/N2HET2\[8\]/ **EQEP2A** Input Pull Down Enhanced QEP2 Input A

| N2HET1\[3\]/SPI4NCS\[0\]/N2HET2\[10\]/EQEP2B | Input | Enhanced QEP2 Input B |
|:--- |:--- |:--- |
| GIOA\[2\]/N2HET2\[0\]/ EQEP2I | I/O | Enhanced QEP2 Index |
| N2HET1\[30\]/MII\_RX\_DV/EQEP2S | I/O | Enhanced QEP2 Strobe |

GIOA\[2\]/N2HET2\[0\]/ ** ** **EQEP2I** I/O Enhanced QEP2 Index

N2HET1\[30\]/MII\_RX\_DV/ **EQEP2S** I/O Enhanced QEP2 Strobe

(1) These signals are double-synchronized and then optionally filtered with a 6-cycle VCLK4-based counter.

## 4.3.1.5

**Enhanced Pulse-Width Modulator Modules (ePWM)**

## Table 4-5. PGE Enhanced Pulse-Width Modulator Modules (ePWM)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **PGE**

GIOA\[5\]/EXTCLKIN/ **EPWM1A** /N2HET1\_PIN\_nDIS Output Pull Down None Enhanced PWM1 Output A

GIOA\[6\]/N2HET2\[4\]/ **EPWM1B** Enhanced PWM1 Output B

N2HET1\[11\]/MIBSPI3NCS\[4\]/N2HET2\[18\]/ **EPWM1SYNCO** External ePWM Sync Pulse Output

N2HET1\[16\]/ **EPWM1SYNCI** /EPWM1SYNCO Input Fixed 20 µA External ePWM Sync Pull Up Pulse Input

GIOA\[7\]/N2HET2\[6\]/ **EPWM2A** Output None Enhanced PWM2 Output A

| N2HET1\[0\]/SPI4CLK/EPWM2B | Enhanced PWM2 Output | B |
|:--- |:--- |:--- |
| N2HET1\[2\]/SPI4SIMO\[0\]/EPWM3A | Enhanced PWM3 Output | A |
| N2HET1\[5\]/SPI4SOMI\[0\]/N2HET2\[12\]/EPWM3B | Enhanced PWM3 Output | B |

N2HET1\[2\]/SPI4SIMO\[0\]/ **EPWM3A** Enhanced PWM3 Output A

N2HET1\[5\]/SPI4SOMI\[0\]/N2HET2\[12\]/ **EPWM3B** Enhanced PWM3 Output B

MIBSPI5NCS\[0\]/ **EPWM4A** Pull Up Enhanced PWM4 Output A

N2HET1\[4\]/ **EPWM4B** Pull Down Enhanced PWM4 Output B

| N2HET1\[6\]/SCIRX/EPWM5A | Enhanced PWM5 Output | A |
|:--- |:--- |:--- |
| N2HET1\[13\]/SCITX/EPWM5B | Enhanced PWM5 Output | B |
| N2HET1\[18\]/EPWM6A | Enhanced PWM6 Output | A |
| N2HET1\[20\]/EPWM6B | Enhanced PWM6 Output | B |
| N2HET1\[9\]/N2HET2\[16\]/EPWM7A | Enhanced PWM7 Output | A |
| N2HET1\[7\]/N2HET2\[14\]/EPWM7B | Enhanced PWM7 Output | B |
| Copyright © 2012-2015, Texas Instruments Incorporated | Terminal Configuration and Functions | Submit Documentation Feedback |

N2HET1\[13\]/SCITX/ **EPWM5B** Enhanced PWM5 Output B

N2HET1\[18\]/ **EPWM6A** Enhanced PWM6 Output A

N2HET1\[20\]/ **EPWM6B** Enhanced PWM6 Output B

N2HET1\[9\]/N2HET2\[16\]/ **EPWM7A** Enhanced PWM7 Output A

N2HET1\[7\]/N2HET2\[14\]/ **EPWM7B** Enhanced PWM7 Output B

Copyright © 2012-2015, Texas Instruments Incorporated *Terminal Configuration and Functions* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## Table 4-5. PGE Enhanced Pulse-Width Modulator Modules (ePWM) (continued)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **PGE**

MIBSPI3NCS\[3\]/I2C\_SCL/N2HET1\[29\]/ **nTZ1** Input Pull Up Fixed 20 µA Trip Zone Inputs 1, 2 and Pull Up 3. These signals are MIBSPI3NCS\[2\]/I2C\_SDA/N2HET1\[27\]/ **nTZ2** either connected N2HET1\[10\]/MII\_TXCLK/MII\_TX\_VCLKA4/ **nTZ3** Pull Down asynchronously to the ePWMx trip zone inputs, or double-synchronized with VCLK4, or doublesynchronized and then filtered with a 6-cycle VCLK4-based counter before connecting to the ePWMx trip zone inputs.

## 4.3.1.6 **General-Purpose Input / Output (GPIO)**

## Table 4-6. PGE General-Purpose Input / Output (GPIO)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **PGE**

**GIOA\[2\]** /N2HET2\[0\]/EQEP2I I/O Pull Down Programmable, General-purpose I/O. 20 µA All GPIO terminals are **GIOA\[5\]** /EXTCLKIN/EPWM1A/N2HET1\_PIN\_nDIS capable of generating **GIOA\[6\]** /N2HET2\[4\]/EPWM1B interrupts to the CPU on rising / falling / both **GIOA\[7\]** /N2HET2\[6\]/EPWM2A edges. MIBSPI3NCS\[0\]/AD2EVT/ **GIOB\[2\]** / 55 (1) Pull Up EQEP1I/N2HET2\_PIN\_nDIS

(1) GIOB\[2\] cannot output a level on to pin 55. Only the input functionality is supported so that the application can generate an interrupt whenever the N2HET2\_PIN\_nDIS is asserted (driven low). Also, a pull up is enabled on the input. This is not programmable using the GIO module control registers.

## 4.3.1.7

**FlexRay** ** ** **Interface Controller (FlexRay)**

## Table 4-7. FlexRay Interface Controller (FlexRay)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **PGE**

**FRAYRX1** Input Pull Up Fixed 100 µA FlexRay data receive Pull Up (channel 1)

**FRAYTX1** Output N/A None FlexRay data transmit (channel 1)

**FRAYTXEN1** Output FlexRay transmit enable (channel 1)

**FRAYRX2** Input Pull Up Fixed 100 µA FlexRay data receive Pull Up (channel 2)

**FRAYTX2** Output N/A None FlexRay data transmit (channel 2)

**FRAYTXEN2** Output FlexRay transmit enable (channel 2)

*Terminal Configuration and Functions* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 4.3.1.8

**Controller Area Network Controllers (DCAN)**

## Table 4-8. PGE Controller Area Network Controllers (DCAN)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **PGE**

**CAN1RX** I/O Pull Up Programmable, CAN1 receive, or GPIO 20 µA **CAN1TX** CAN1 transmit, or GPIO

| CAN2RX | CAN2 receive, or GPIO |
|:--- |:--- |
| CAN2TX | CAN2 transmit, or GPIO |
| CAN3RX | CAN3 receive, or GPIO |
| CAN3TX | CAN3 transmit, or GPIO |
| 4.3.1.9 | Local Interconnect Network Interface Module (LIN) | **CAN2TX** CAN2 transmit, or GPIO **CAN3RX** CAN3 receive, or GPIO **CAN3TX** CAN3 transmit, or GPIO

## 4.3.1.9

**Local** ** ** **Interconnect Network Interface Module (LIN)**

## Table 4-9. PGE Local Interconnect Network Interface Module (LIN)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **PGE**

**LINRX** I/O Pull Up Programmable, LIN receive, or GPIO 20 µA **LINTX** LIN transmit, or GPIO

## 4.3.1.10

**Standard Serial Communication Interface** ** ** **(SCI)**

## Table 4-10. PGE Standard Serial Communication Interface (SCI)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **PGE**

N2HET1\[6\]/ **SCIRX** /EPWM5A I/O Pull Down Programmable, SCI receive, or GPIO 20 µA N2HET1\[13\]/ **SCITX** /EPWM5B SCI transmit, or GPIO

## 4.3.1.11

**Inter-Integrated Circuit Interface Module (I2C)**

## Table 4-11. PGE Inter-Integrated Circuit Interface Module (I2C)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **PGE**

MIBSPI3NCS\[2\]/ **I2C\_SDA** /N2HET1\[27\]/nTZ2 I/O Pull Up Programmable, I2C serial data, or GPIO 20 µA MIBSPI3NCS\[3\]/ **I2C\_SCL** /N2HET1\[29\]/nTZ1 I2C serial clock, or GPIO

Copyright © 2012-2015, Texas Instruments Incorporated *Terminal Configuration and Functions* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## 4.3.1.12

**Standard Serial Peripheral Interface (SPI)**

## Table 4-12. PGE Standard Serial Peripheral Interface (SPI)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **PGE**

N2HET1\[0\]/ **SPI4CLK** /EPWM2B I/O Pull Down Programmable, SPI4 clock, or GPIO 20 µA N2HET1\[3\]/ **SPI4NCS\[0\]** /N2HET2\[10\]/EQEP2B SPI4 chip select, or GPIO

# N2HET1\[1\]/ SPI4NENA /N2HET2\[8\]/EQEP2A SPI4 enable, or GPIO

N2HET1\[2\]/ **SPI4SIMO\[0\]** /EPWM3A SPI4 slave-input masteroutput, or GPIO

N2HET1\[5\]/ **SPI4SOMI\[0\]** /N2HET2\[12\]/EPWM3B SPI4 slave-output masterinput, or GPIO

## 4.3.1.13

**Multibuffered Serial Peripheral Interface Modules (MibSPI)**

## Table 4-13. PGE Multibuffered Serial Peripheral Interface Modules (MibSPI)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **PGE**

**MIBSPI1CLK** I/O Pull Up Programmable, MibSPI1 clock, or GPIO 20 µA **MIBSPI1NCS\[0\]** /MIBSPI1SOMI\[1\]/MII\_TXD\[2\]/ECAP6 MibSPI1 chip select, or GPIO **MIBSPI1NCS\[1\]** /N2HET1\[17\]/MII\_COL/EQEP1S

# MIBSPI1NCS\[2\] /N2HET1\[19\]/MDIO

N2HET1\[15\]/ **MIBSPI1NCS\[4\]** /ECAP1 Pull Down Programmable, MibSPI1 chip select, or 20 µA GPIO N2HET1\[24\]/ **MIBSPI1NCS\[5\]** /MII\_RXD\[0\]/RMII\_RXD\[0\]

**MIBSPI1NENA** /N2HET1\[23\]/MII\_RXD\[2\]/ECAP4 Pull Up Programmable, MibSPI1 enable, or GPIO 20 µA **MIBSPI1SIMO\[0\]** MibSPI1 slave-in masterout, or GPIO

N2HET1\[8\]/ **MIBSPI1SIMO\[1\]** /MII\_TXD\[3\] Pull Down Programmable, MibSPI1 slave-in master20 µA out, or GPIO

**MIBSPI1SOMI\[0\]** Pull Up Programmable, MibSPI1 slave-out master20 µA in, or GPIO MIBSPI1NCS\[0\]/ **MIBSPI1SOMI\[1\]** /MII\_TXD\[2\]/ECAP6

**MIBSPI3CLK** /AWM1\_EXT\_SEL\[1\]/EQEP1A I/O Pull Up Programmable, MibSPI3 clock, or GPIO 20 µA **MIBSPI3NCS\[0\]** /AD2EVT/GIOB\[2\]/ MibSPI3 chip select, or EQEP1I/N2HET2\_PIN\_nDIS GPIO

# MIBSPI3NCS\[1\] /N2HET1\[25\]/MDCLK

# MIBSPI3NCS\[2\] /I2C\_SDA/N2HET1\[27\]/nTZ2

# MIBSPI3NCS\[3\] /I2C\_SCL/N2HET1\[29\]/nTZ1

N2HET1\[11\]/ **MIBSPI3NCS\[4\]** /N2HET2\[18\]/EPWM1SYNCO Pull Down Programmable, MibSPI3 chip select, or 20 µA GPIO

MIBSPI3NENA / **MIBSPI3NCS\[5\]** /N2HET1\[31\]/EQEP1B Pull Up Programmable, MibSPI3 chip select, or 20 µA GPIO

# MIBSPI3NENA /MIBSPI3NCS\[5\]/N2HET1\[31\]/EQEP1B MibSPI3 enable, or GPIO

| MIBSPI3SIMO\[0\]/AWM1\_EXT\_SEL\[0\]/ECAP3 | MibSPI3 slave-in master- | out, or GPIO |
|:--- |:--- |:--- |
| MIBSPI3SOMI\[0\]/AWM1\_EXT\_ENA/ECAP2 | MibSPI3 slave-out master- | in, or GPIO |
| Terminal Configuration and Functions | Copyright © 2012-2015, Texas Instruments Incorporated | Submit Documentation Feedback |

**MIBSPI3SOMI\[0\]** /AWM1\_EXT\_ENA/ECAP2 MibSPI3 slave-out masterin, or GPIO

*Terminal Configuration and Functions* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## Table 4-13. PGE Multibuffered Serial Peripheral Interface Modules (MibSPI) (continued)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **PGE**

**MIBSPI5CLK** /MII\_TXEN/RMII\_TXEN I/O Pull Up Programmable, MibSPI5 clock, or GPIO 20 µA **MIBSPI5NCS\[0\]** /EPWM4A MibSPI5 chip select, or GPIO

# MIBSPI5NENA /MII\_RXD\[3\]/MIBSPI5SOMI\[1\]/ ECAP5 MibSPI5 enable, or GPIO

| MIBSPI5SIMO\[0\]/MII\_TXD\[1\]/RMII\_TXD\[1\]/MIBSPI5SOMI\[2\] | MibSPI5 slave-in master- | out, or GPIO |
|:--- |:--- |:--- |
| MIBSPI5SOMI\[0\]/MII\_TXD\[0\]/RMII\_TXD\[0\] | MibSPI5 slave-out master- | in, or GPIO |
| MIBSPI5NENA/MII\_RXD\[3\]/MIBSPI5SOMI\[1\]/ ECAP5 | MibSPI5 slave-out master- | in, or GPIO |
| MIBSPI5SIMO\[0\]/MII\_TXD\[1\]/RMII\_TXD\[1\]/MIBSPI5SOMI\[2\] | MibSPI5 slave-out master- | in, or GPIO |

**MIBSPI5SOMI\[0\]** /MII\_TXD\[0\]/RMII\_TXD\[0\] MibSPI5 slave-out masterin, or GPIO

MIBSPI5NENA/MII\_RXD\[3\]/ **MIBSPI5SOMI\[1\]** / ECAP5 MibSPI5 slave-out masterin, or GPIO

MIBSPI5SIMO\[0\]/MII\_TXD\[1\]/RMII\_TXD\[1\]/ **MIBSPI5SOMI\[2\]** MibSPI5 slave-out masterin, or GPIO

## 4.3.1.14 **Ethernet Controller**

## Table 4-14. PGE Ethernet Controller: MDIO Interface

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **PGE**

MIBSPI3NCS\[1\]/N2HET1\[25\]/ **MDCLK** Output Pull Up None Serial clock output

MIBSPI1NCS\[2\]/N2HET1\[19\]/ **MDIO** I/O Pull Up Fixed 20 µA Serial data input/output Pull Up

## Table 4-15. PGE Ethernet Controller: Reduced Media Independent Interface (RMII)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **PGE**

N2HET1\[12\]/MII\_CRS/ **RMII\_CRS\_DV** Input Pull Down Fixed 20 µA RMII carrier sense and Pull Down data valid

N2HET1\[28\]/MII\_RXCLK/ **RMII\_REFCLK** /MII\_RX\_VCLKA4 RMII synchronous reference clock for receive, transmit and control interface

AD1EVT/MII\_RX\_ER/ **RMII\_RX\_ER** RMII receive error

# N2HET1\[24\]/MIBSPI1NCS\[5\]/MII\_RXD\[0\]/ RMII\_RXD\[0\] RMII receive data

# N2HET1\[26\]/MII\_RXD\[1\]/ RMII\_RXD\[1\]

MIBSPI5SOMI\[0\]/MII\_TXD\[0\]/ **RMII\_TXD\[0\]** Output Pull Up None RMII transmit data

# MIBSPI5SIMO\[0\]/MII\_TXD\[1\]/ RMII\_TXD\[1\] /MIBSPI5SOMI\[2\]

MIBSPI5CLK/MII\_TXEN/ **RMII\_TXEN** RMII transmit enable

## Table 4-16. PGE Ethernet Controller: Media Independent Interface (MII)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **PGE**

MIBSPI1NCS\[1\]/N2HET1\[17\]/ **MII\_COL** /EQEP1S Input Pull Up None Collision detect

N2HET1\[12\]/ **MII\_CRS** /RMII\_CRS\_DV Pull Down Fixed 20 µA Carrier sense and receive Pull Down data valid

N2HET1\[28\]/MII\_RXCLK/RMII\_REFCLK/ **MII\_RX\_VCLKA4** I/O Pull Down None MII output receive clock

Copyright © 2012-2015, Texas Instruments Incorporated *Terminal Configuration and Functions* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## Table 4-16. PGE Ethernet Controller: Media Independent Interface (MII) (continued)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **PGE**

N2HET1\[30\]/ **MII\_RX\_DV** /EQEP2S Input Pull Down Fixed 20 µA Received data valid Pull Down AD1EVT/ **MII\_RX\_ER** /RMII\_RX\_ER Receive error

# N2HET1\[28\]/ MII\_RXCLK /RMII\_REFCLK/MII\_RX\_VCLKA4 I/O Receive clock

N2HET1\[24\]/MIBSPI1NCS\[5\]/ **MII\_RXD\[0\]** /RMII\_RXD\[0\] Input Receive data

# N2HET1\[26\]/ MII\_RXD\[1\] /RMII\_RXD\[1\]

# MIBSPI1NENA/N2HET1\[23\]/ MII\_RXD\[2\] /ECAP4 Pull Up Fixed 20 µA

# Pull Down

MIBSPI5NENA/ **MII\_RXD\[3\]** /MIBSPI5SOMI\[1\]/ ECAP5

N2HET1\[10\]/MII\_TXCLK/ **MII\_TX\_VCLKA4** /nTZ3 I/O Pull Down None MII output transmit clock

N2HET1\[10\]/ **MII\_TXCLK** /MII\_TX\_VCLKA4/nTZ3 Fixed 20 µA Transmit clock Pull Down

MIBSPI5SOMI\[0\]/ **MII\_TXD\[0\]** /RMII\_TXD\[0\] Output Pull Up None Transmit data

# MIBSPI5SIMO\[0\]/MIBSPI5SOMI\[2\]/ MII\_TXD\[1\] /RMII\_TXD\[1\]

# MIBSPI1NCS\[0\]/MIBSPI1SOMI\[1\]/ MII\_TXD\[2\] /ECAP6

# N2HET1\[8\]/MIBSPI1SIMO\[1\]/ MII\_TXD\[3\] Pull Down

MIBSPI5CLK/ **MII\_TXEN** /RMII\_TXEN Pull Up Transmit enable

*Terminal Configuration and Functions* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 4.3.1.15 **System Module Interface**

## Table 4-17. PGE System Module Interface

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **PGE**

**nPORRST** Input Pull Down Fixed 100 µA Power-on reset, cold reset Pull Down External power supply monitor circuitry must drive nPORRST low when any of the supplies to the microcontroller fall out of the specified range. This terminal has a glitch filter. See Section 6.8.

**nRST** I/O Pull Up Fixed 100 µA System reset, warm reset, Pull Up bidirectional. The internal circuitry indicates any reset condition by driving nRST low. The external circuitry can assert a system reset by driving nRST low. To ensure that an external reset is not arbitrarily generated, TI recommends that an external pull-up resistor is connected to this terminal. This terminal has a glitch filter. See Section 6.8.

**nERROR** I/O Pull Down Fixed 20 µA ESM Error Signal Pull Down Indicates error of high severity. See Section 6.18.

## 4.3.1.16 **Clock Inputs and Outputs**

## Table 4-18. PGE Clock Inputs and Outputs

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **PGE**

**OSCIN** Input N/A None From external crystal/resonator, or external clock input

**KELVIN\_GND** Input Kelvin ground for oscillator

**OSCOUT** Output To external crystal/resonator

**ECLK** I/O Pull Down Programmable, External prescaled clock 20 µA output, or GPIO.

GIOA\[5\]/ **EXTCLKIN** /EPWM1A /N2HET1\_PIN\_nDIS Input Pull Down Fixed 20 µA External clock input #1 Pull Down

Copyright © 2012-2015, Texas Instruments Incorporated *Terminal Configuration and Functions* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## 4.3.1.17

**Test** ** ** **and Debug Modules Interface**

## Table 4-19. PGE Test and Debug Modules Interface

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **PGE**

**TEST** Input Pull Down Fixed 100 µA Test enable. This terminal Pull Down must be connected to ground directly or via a pull-down resistor. **nTRST** Input JTAG test hardware reset

**RTCK** Output N/A None JTAG return test clock

| TCK | Input | Pull Down | Fixed 100 µA | JTAG test clock | Pull Down |
|:--- |:--- |:--- |:--- |:--- |:--- |
| TDI | Input | Pull Up | Fixed 100 µA | JTAG test data in | Pull Up |
| TDO | Output | 100 µA | None | JTAG test data out | Pull Down |
| TMS | Input | Pull Up | Fixed 100 µA | JTAG test select | Pull Up |

**TDI** Input Pull Up Fixed 100 µA JTAG test data in Pull Up

**TDO** Output 100 µA None JTAG test data out Pull Down

**TMS** Input Pull Up Fixed 100 µA JTAG test select Pull Up

## 4.3.1.18 **Flash** ** ** **Supply and Test Pads**

## Table 4-20. PGE Flash Supply and Test Pads

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **PGE**

**VCCP** 3.3V N/A None Flash pump supply Power

**FLTP1** - - N/ANone Flash test pads. These terminals are reserved for **FLTP2** TI use only. For proper operation these terminals must connect only to a test pad or not be connected at all \[no connect (NC)\].

*Terminal Configuration and Functions* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 4.3.1.19

**Supply** ** ** **for Core Logic: 1.2V nominal**

## Table 4-21. PGE Supply for Core Logic: 1.2V nominal

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **PGE**

**VCC** 1.2V N/A None Core supply Power **VCC**

# VCC

# VCC

# VCC

# VCC

# VCC

# VCC

# VCC

# VCC

# VCC

# VCC

## 4.3.1.20

**Supply** ** ** **for I/O Cells: 3.3V nominal**

## Table 4-22. PGE Supply for I/O Cells: 3.3V nominal

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **PGE**

**VCCIO** 3.3V N/A None Operating supply for I/Os Power **VCCIO**

# VCCIO

# VCCIO

# VCCIO

# VCCIO

Copyright © 2012-2015, Texas Instruments Incorporated *Terminal Configuration and Functions* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## 4.3.1.21

**Ground Reference for All Supplies Except VCCAD**

## Table 4-23. PGE Ground Reference for All Supplies Except VCCAD

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **PGE** **VSS** Ground N/A None Ground reference

# VSS

# VSS

# VSS

# VSS

# VSS

# VSS

# VSS

# VSS

# VSS

# VSS

# VSS

# VSS

# VSS

# VSS

# VSS

# VSS

# VSS

*Terminal Configuration and Functions* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 4.3.2 ***ZWT Package***

## 4.3.2.1

**Multibuffered Analog-to-Digital Converters (MibADC)**

## Table 4-24. ZWT Multibuffered Analog-to-Digital Converters (MibADC1, MibADC2)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **ZWT**

**ADREFHI** (1) V15 Power N/A None ADC high reference supply

**ADREFLO** (1) V16 Power ADC low reference supply

**VCCAD** (1) W15 Power Operating supply for ADC

**VSSAD** V19 Ground N/A None ADC supply power

| VSSAD | W16 |
|:--- |:--- |
| VSSAD | W18 |
| VSSAD | W19 |

# VSSAD W18

# VSSAD W19

**AD1EVT** /MII\_RX\_ER/RMII\_RX\_ER N19 I/O Pull Down Programmable, ADC1 event trigger input, 20 µA or GPIO

MIBSPI3NCS\[0\]/ **AD2EVT** /GIOB\[2\]/ V10 I/O Pull Up Programmable, ADC2 event trigger input, EQEP1I/N2HET2\_PIN\_nDIS 20 µA or GPIO

**AD1IN\[0\]** W14 Input N/A None ADC1 analog input

| AD1IN\[1\] | V17 |
|:--- |:--- |
| AD1IN\[2\] | V18 |
| AD1IN\[3\] | T17 |
| AD1IN\[4\] | U18 |
| AD1IN\[5\] | R17 |
| AD1IN\[6\] | T19 |
| AD1IN\[7\] | V14 |

# AD1IN\[2\] V18

# AD1IN\[3\] T17

# AD1IN\[4\] U18

# AD1IN\[5\] R17

# AD1IN\[6\] T19

# AD1IN\[7\] V14

**AD1IN\[8\]** / AD2IN\[8\] P18 Input N/A None ADC1/ADC2 shared analog inputs **AD1IN\[9\]** / AD2IN\[9\] W17

| AD1IN\[10\] / AD2IN\[10\] | U17 |
|:--- |:--- |
| AD1IN\[11\] / AD2IN\[11\] | U19 |
| AD1IN\[12\] / AD2IN\[12\] | T16 |
| AD1IN\[13\] / AD2IN\[13\] | T18 |
| AD1IN\[14\] / AD2IN\[14\] | R18 |
| AD1IN\[15\] / AD2IN\[15\] | P19 |
| AD1IN\[16\] / AD2IN\[0\] | V13 |
| AD1IN\[17\] / AD2IN\[1\] | U13 |
| AD1IN\[18\] / AD2IN\[2\] | U14 |
| AD1IN\[19\] / AD2IN\[3\] | U16 |
| AD1IN\[20\] / AD2IN\[4\] | U15 |
| AD1IN\[21\] / AD2IN\[5\] | T15 |
| AD1IN\[22\] / AD2IN\[6\] | R19 |
| AD1IN\[23\] / AD2IN\[7\] | R16 |

# AD1IN\[11\] / AD2IN\[11\] U19

# AD1IN\[12\] / AD2IN\[12\] T16

# AD1IN\[13\] / AD2IN\[13\] T18

# AD1IN\[14\] / AD2IN\[14\] R18

# AD1IN\[15\] / AD2IN\[15\] P19

# AD1IN\[16\] / AD2IN\[0\] V13

# AD1IN\[17\] / AD2IN\[1\] U13

# AD1IN\[18\] / AD2IN\[2\] U14

# AD1IN\[19\] / AD2IN\[3\] U16

# AD1IN\[20\] / AD2IN\[4\] U15

# AD1IN\[21\] / AD2IN\[5\] T15

# AD1IN\[22\] / AD2IN\[6\] R19

# AD1IN\[23\] / AD2IN\[7\] R16

MIBSPI3SOMI\[0\]/ **AWM1\_EXT\_ENA** /ECAP2 V8 Output Pull Up None AWM1 external analog mux enable

MIBSPI3SIMO\[0\]/ **AWM1\_EXT\_SEL\[0\]** /ECAP3 W8 AWM1 external analog mux select line0

MIBSPI3CLK/ **AWM1\_EXT\_SEL\[1\]** /EQEP1A V9 AWM1 external analog mux select line0

(1) The ADREFHI, ADREFLO, VCCAD and VSSAD connections are common for both ADC cores.

Copyright © 2012-2015, Texas Instruments Incorporated *Terminal Configuration and Functions* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## 4.3.2.2 **Enhanced High-End Timer Modules (N2HET)**

## Table 4-25. ZWT Enhanced High-End Timer Modules (N2HET)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **ZWT**

**N2HET1\[0\]** /SPI4CLK/EPWM2B K18 I/O Pull Down Programmable, N2HET1 time input 20 µA **N2HET1\[1\]** /SPI4NENA/N2HET2\[8\]/EQEP2A V2 capture or output compare, or GIO. **N2HET1\[2\]** /SPI4SIMO\[0\]/EPWM3A W5

Each terminal has a **N2HET1\[3\]** /SPI4NCS\[0\]/N2HET2\[10\]/EQEP2B U1

suppression filter with a **N2HET1\[4\]** /EPWM4B B12 programmable duration. **N2HET1\[5\]** /SPI4SOMI\[0\]/N2HET2\[12\]/EPWM3B V6

| N2HET1\[6\]/SCIRX/EPWM5A | W3 |
|:--- |:--- |
| N2HET1\[7\]/N2HET2\[14\]/EPWM7B | T1 |
| N2HET1\[8\]/MIBSPI1SIMO\[1\]/MII\_TXD\[3\] | E18 |
| N2HET1\[9\]/N2HET2\[16\]/EPWM7A | V7 |
| N2HET1\[10\]/MII\_TXCLK/MII\_TX\_VCLKA4/nTZ3 | D19 |
| N2HET1\[11\]/MIBSPI3NCS\[4\]/N2HET2\[18\]/EPWM1SYNCO | E3 |
| N2HET1\[12\]/MII\_CRS/RMII\_CRS\_DV | B4 |
| N2HET1\[13\]/SCITX/EPWM5B | N2 |
| N2HET1\[14\] | A11 |
| N2HET1\[15\]/MIBSPI1NCS\[4\]/ECAP1 | N1 |
| N2HET1\[16\]/EPWM1SYNCI/EPWM1SYNCO | A4 |
| N2HET1\[17\] | A13 |
| MIBSPI1NCS\[1\]/N2HET1\[17\]/MII\_COL/ EQEP1S | F3 |
| N2HET1\[18\]/EPWM6A | J1 |
| N2HET1\[19\] | B13 |
| MIBSPI1NCS\[2\]/N2HET1\[19\]/MDIO | G3 |
| N2HET1\[20\]/EPWM6B | P2 |
| N2HET1\[21\] | H4 |
| MIBSPI1NCS\[3\]/N2HET1\[21\] | J3 |
| N2HET1\[22\] | B3 |
| N2HET1\[23\] | J4 |

# N2HET1\[7\] /N2HET2\[14\]/EPWM7B T1

# N2HET1\[8\] /MIBSPI1SIMO\[1\]/MII\_TXD\[3\] E18

# N2HET1\[9\] /N2HET2\[16\]/EPWM7A V7

# N2HET1\[10\] /MII\_TXCLK/MII\_TX\_VCLKA4/nTZ3 D19

# N2HET1\[11\] /MIBSPI3NCS\[4\]/N2HET2\[18\]/EPWM1SYNCO E3

# N2HET1\[12\] /MII\_CRS/RMII\_CRS\_DV B4

# N2HET1\[13\] /SCITX/EPWM5B N2

# N2HET1\[14\] A11

# N2HET1\[15\] /MIBSPI1NCS\[4\]/ECAP1 N1

# N2HET1\[16\] /EPWM1SYNCI/EPWM1SYNCO A4

# N2HET1\[17\] A13

# MIBSPI1NCS\[1\]/ N2HET1\[17\] /MII\_COL/ EQEP1S F3

# N2HET1\[18\] /EPWM6A J1

# N2HET1\[19\] B13

# MIBSPI1NCS\[2\]/ N2HET1\[19\] /MDIO G3

# N2HET1\[20\] /EPWM6B P2

# N2HET1\[21\] H4

# MIBSPI1NCS\[3\]/ N2HET1\[21\] J3

# N2HET1\[22\] B3

# N2HET1\[23\] J4

# MIBSPI1NENA/ N2HET1\[23\] /MII\_RXD\[2\]/ECAP4 G19 Pull Up

# N2HET1\[24\] /MIBSPI1NCS\[5\]/MII\_RXD\[0\]/RMII\_RXD\[0\] P1 Pull Down

| N2HET1\[25\] | M3 |
|:--- |:--- |
| MIBSPI3NCS\[1\]/N2HET1\[25\]/MDCLK | V5 |
| N2HET1\[26\]/MII\_RXD\[1\]/RMII\_RXD\[1\] | A14 |
| N2HET1\[27\] | A9 |

# MIBSPI3NCS\[1\]/ N2HET1\[25\] /MDCLK V5

# N2HET1\[26\] /MII\_RXD\[1\]/RMII\_RXD\[1\] A14

# N2HET1\[27\] A9

# MIBSPI3NCS\[2\]/I2C\_SDA/ N2HET1\[27\] /nTZ2 B2 Pull Up

# N2HET1\[28\] /MII\_RXCLK/RMII\_REFCLK/MII\_RX\_VCLKA4 K19 Pull Down

# N2HET1\[29\] A3

# MIBSPI3NCS\[3\]/I2C\_SCL/ N2HET1\[29\] /nTZ1 C3

*Terminal Configuration and Functions* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## Table 4-25. ZWT Enhanced High-End Timer Modules (N2HET) (continued)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **ZWT**

**N2HET1\[30\]** /MII\_RX\_DV/EQEP2S B11 I/O Pull Down Programmable,

# 20 µA **N2HET1\[31\]** J17

# MIBSPI3NENA/MIBSPI3NCS\[5\]/ N2HET1\[31\] /EQEP1B W9 Pull Up

GIOA\[5\]/EXTCLKIN/EPWM1A **/N2HET1\_PIN\_nDIS** B5 input Pull Down Programmable, Disable selected PWM 20 µA (1) outputs

GIOA\[2\]/ **N2HET2\[0\]** /EQEP2I C1 I/O Pull Down Programmable, N2HET2 time input 20 µA EMIF\_ADDR\[0\]/ **N2HET2\[1\]** D4 capture or output compare, or GIO. GIOA\[3\]/ **N2HET2\[2\]** E1

Each terminal has a EMIF\_ADDR\[1\]/ **N2HET2\[3\]** D5

suppression filter with a GIOA\[6\]/ **N2HET2\[4\]** /EPWM1B H3 programmable duration. EMIF\_BA\[1\]/ **N2HET2\[5\]** D16

| GIOA\[7\]/N2HET2\[6\]/EPWM2A | M1 |
|:--- |:--- |
| EMIF\_nCS\[0\]/N2HET2\[7\] | N17 |
| N2HET1\[1\]/SPI4NENA/ N2HET2\[8\]/EQEP2A | V2 |
| EMIF\_nCS\[3\]/N2HET2\[9\] | K17 |
| N2HET1\[3\]/SPI4NCS\[0\]/N2HET2\[10\]/EQEP2B | U1 |
| EMIF\_ADDR\[6\]/N2HET2\[11\] | C4 |
| N2HET1\[5\]/SPI4SOMI\[0\]/N2HET2\[12\]/EPWM3B | V6 |
| EMIF\_ADDR\[7\]/N2HET2\[13\] | C5 |
| N2HET1\[7\]/N2HET2\[14\]/EPWM7B | T1 |
| EMIF\_ADDR\[8\]/N2HET2\[15\] | C6 |
| N2HET1\[9\]/N2HET2\[16\]/EPWM7A | V7 |
| N2HET1\[11\]/MIBSPI3NCS\[4\]/N2HET2\[18\]/EPWM1SYNCO | E3 |

# EMIF\_nCS\[0\]/ N2HET2\[7\] N17

# N2HET1\[1\]/SPI4NENA/ N2HET2\[8\] /EQEP2A V2

# EMIF\_nCS\[3\]/ N2HET2\[9\] K17

# N2HET1\[3\]/SPI4NCS\[0\]/ N2HET2\[10\] /EQEP2B U1

# EMIF\_ADDR\[6\]/ N2HET2\[11\] C4

# N2HET1\[5\]/SPI4SOMI\[0\]/ N2HET2\[12\] /EPWM3B V6

# EMIF\_ADDR\[7\]/ N2HET2\[13\] C5

# N2HET1\[7\]/ N2HET2\[14\] /EPWM7B T1

# EMIF\_ADDR\[8\]/ N2HET2\[15\] C6

# N2HET1\[9\]/ N2HET2\[16\] /EPWM7A V7

# N2HET1\[11\]/MIBSPI3NCS\[4\]/ N2HET2\[18\] /EPWM1SYNCO E3

MIBSPI3NCS\[0\]/AD2EVT/GIOB\[2\]/ V10 I/O Pull Up Programmable, Disable selected PWM EQEP1I/ **N2HET2\_PIN\_nDIS** 20 µA (1) outputs

(1) The N2HETx\_PIN\_nDIS function is always available on this terminal. There is no mux control to select this function. The pull direction is controlled by the function which is selected by the output mux control for this terminal.

Copyright © 2012-2015, Texas Instruments Incorporated *Terminal Configuration and Functions* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## 4.3.2.3 **Enhanced Capture Modules (eCAP)**

**Table 4-26. ZWT Enhanced Capture Modules (eCAP)** **(1)**

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **ZWT**

N2HET1\[15\]/MIBSPI1NCS\[4\]/ **ECAP1** N1 I/O Pull Down Fixed 20 µA Enhanced Capture Pull Up Module 1 I/O

MIBSPI3SOMI\[0\]/AWM1\_EXT\_ENA/ **ECAP2** V8 I/O Pull Up Enhanced Capture Module 2 I/O

| MIBSPI3SIMO\[0\]/AWM1\_EXT\_SEL\[0\]/ECAP3 | W8 | I/O | Enhanced Capture | Module 3 I/O |
|:--- |:--- |:--- |:--- |:--- |
| MIBSPI1NENA/N2HET1\[23\]/MII\_RXD\[2\]/ECAP4 | G19 | I/O | Enhanced Capture | Module 4 I/O |
| MIBSPI5NENA/MII\_RXD\[3\]/MIBSPI5SOMI\[1\]/ ECAP5 | H18 | I/O | Enhanced Capture | Module 5 I/O |
| MIBSPI1NCS\[0\]/MIBSPI1SOMI\[1\]/MII\_TXD\[2\]/ ECAP6 | R2 | I/O | Enhanced Capture | Module 6 I/O |

MIBSPI1NENA/N2HET1\[23\]/MII\_RXD\[2\]/ **ECAP4** G19 I/O Enhanced Capture Module 4 I/O

MIBSPI5NENA/MII\_RXD\[3\]/MIBSPI5SOMI\[1\]/ ** ** **ECAP5** H18 I/O Enhanced Capture Module 5 I/O

MIBSPI1NCS\[0\]/MIBSPI1SOMI\[1\]/MII\_TXD\[2\]/ ** ECAP6** R2 I/O Enhanced Capture Module 6 I/O

(1) These signals, when used as inputs, are double-synchronized and then optionally filtered with a 6-cycle VCLK4-based counter.

## 4.3.2.4

**Enhanced Quadrature Encoder Pulse** ** ** **Modules (eQEP)**

**Table 4-27. ZWT Enhanced Quadrature Encoder Pulse Modules (eQEP)** **(1)**

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **ZWT**

MIBSPI3CLK/AWM1\_EXT\_SEL\[1\]/ **EQEP1A** V9 Input Pull Up Fixed 20 µA Enhanced QEP1 Input A Pull Up MIBSPI3NENA/MIBSPI3NCS\[5\]/N2HET1\[31\]/ **EQEP1B** W9 Input Enhanced QEP1 Input B

# MIBSPI3NCS\[0\]/AD2EVT/GIOB\[2\]/

V10 I/O Enhanced QEP1 Index **EQEP1I** /N2HET2\_PIN\_nDIS

# MIBSPI1NCS\[1\]/N2HET1\[17\]/MII\_COL/ EQEP1S F3 I/O Enhanced QEP1 Strobe

| N2HET1\[1\]/SPI4NENA/N2HET2\[8\]/EQEP2A | V2 | Input | Pull Down | Enhanced QEP2 Input A |
|:--- |:--- |:--- |:--- |:--- |
| N2HET1\[3\]/SPI4NCS\[0\]/N2HET2\[10\]/EQEP2B | U1 | Input | Pull Down | Enhanced QEP2 Input B |
| GIOA\[2\]/N2HET2\[0\]/ EQEP2I | C1 | I/O | Pull Down | Enhanced QEP2 Index |
| N2HET1\[30\]/MII\_RX\_DV/EQEP2S | B11 | I/O | Pull Down | Enhanced QEP2 Strobe |

N2HET1\[3\]/SPI4NCS\[0\]/N2HET2\[10\]/ **EQEP2B** U1 Input Pull Down Enhanced QEP2 Input B

GIOA\[2\]/N2HET2\[0\]/ ** ** **EQEP2I** C1 I/O Pull Down Enhanced QEP2 Index

N2HET1\[30\]/MII\_RX\_DV/ **EQEP2S** B11 I/O Pull Down Enhanced QEP2 Strobe

(1) These signals are double-synchronized and then optionally filtered with a 6-cycle VCLK4-based counter.

*Terminal Configuration and Functions* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 4.3.2.5

**Enhanced Pulse-Width Modulator Modules (ePWM)**

## Table 4-28. ZWT Enhanced Pulse-Width Modulator Modules (ePWM)

# TERMINAL

# SIGNA

**Reset Pull** **PULL TYPE** **DESCRIPTION** **L TYPE** **State** **SIGNAL NAME** **ZWT**

GIOA\[5\]/EXTCLKIN/ **EPWM1A** /N2HET1\_PIN\_nDIS B5 Output Pull Down None Enhanced PWM1 Output A

GIOA\[6\]/N2HET2\[4\]/ **EPWM1B** H3 Enhanced PWM1 Output B

N2HET1\[11\]/MIBSPI3NCS\[4\]/N2HET2\[18\]/ **EPWM1SYNCO** E3 External ePWM Sync Pulse Output

N2HET1\[16\]/ **EPWM1SYNCI** /EPWM1SYNCO A4 Input Fixed 20 µA External ePWM Sync Pulse Pull Up Input

GIOA\[7\]/N2HET2\[6\]/ **EPWM2A** M1 Output None Enhanced PWM2 Output A

| N2HET1\[0\]/SPI4CLK/EPWM2B | K18 | Enhanced PWM2 Output B |
|:--- |:--- |:--- |
| N2HET1\[2\]/SPI4SIMO\[0\]/EPWM3A | W5 | Enhanced PWM3 Output A |
| N2HET1\[5\]/SPI4SOMI\[0\]/N2HET2\[12\]/EPWM3B | V6 | Enhanced PWM3 Output B |

N2HET1\[2\]/SPI4SIMO\[0\]/ **EPWM3A** W5 Enhanced PWM3 Output A

N2HET1\[5\]/SPI4SOMI\[0\]/N2HET2\[12\]/ **EPWM3B** V6 Enhanced PWM3 Output B

MIBSPI5NCS\[0\]/ **EPWM4A** E19 Pull Up Enhanced PWM4 Output A

N2HET1\[4\]/ **EPWM4B** B12 Pull Down Enhanced PWM4 Output B

| N2HET1\[6\]/SCIRX/EPWM5A | W3 | Enhanced PWM5 Output A |
|:--- |:--- |:--- |
| N2HET1\[13\]/SCITX/EPWM5B | N2 | Enhanced PWM5 Output B |
| N2HET1\[18\]/EPWM6A | J1 | Enhanced PWM6 Output A |
| N2HET1\[20\]/EPWM6B | P2 | Enhanced PWM6 Output B |
| N2HET1\[9\]/N2HET2\[16\]/EPWM7A | V7 | Enhanced PWM7 Output A |
| N2HET1\[7\]/N2HET2\[14\]/EPWM7B | T1 | Enhanced PWM7 Output B |

N2HET1\[13\]/SCITX/ **EPWM5B** N2 Enhanced PWM5 Output B

N2HET1\[18\]/ **EPWM6A** J1 Enhanced PWM6 Output A

N2HET1\[20\]/ **EPWM6B** P2 Enhanced PWM6 Output B

N2HET1\[9\]/N2HET2\[16\]/ **EPWM7A** V7 Enhanced PWM7 Output A

N2HET1\[7\]/N2HET2\[14\]/ **EPWM7B** T1 Enhanced PWM7 Output B

MIBSPI3NCS\[3\]/I2C\_SCL/N2HET1\[29\]/ **nTZ1** C3 Input Pull Up Fixed 20 µA Trip Zone Inputs 1, 2 and 3. Pull Up These signals are either MIBSPI3NCS\[2\]/I2C\_SDA/N2HET1\[27\]/ **nTZ2** B2 connected asynchronously to N2HET1\[10\]/MII\_TXCLK/MII\_TX\_VCLKA4/ **nTZ3** D19 Pull Down the ePWMx trip zone inputs, or double-synchronized with VCLK4, or doublesynchronized and then filtered with a 6-cycle VCLK4-based counter before connecting to the ePWMx trip zone inputs.

Copyright © 2012-2015, Texas Instruments Incorporated *Terminal Configuration and Functions* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## 4.3.2.6 **General-Purpose Input / Output (GPIO)**

## Table 4-29. ZWT General-Purpose Input / Output (GPIO)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **ZWT**

**GIOA\[0\]** A5 I/O Pull Down Programmable, General-purpose I/O. 20 µA All GPIO terminals are **GIOA\[1\]** C2 capable of generating **GIOA\[2\]** /N2HET2\[0\] /EQEP2I C1 interrupts to the CPU on rising / falling / both **GIOA\[3\]** /N2HET2\[2\] E1 edges. **GIOA\[4\]** A6

| GIOA\[5\]/EXTCLKIN/EPWM1A/N2HET1\_PIN\_nDIS | B5 |
|:--- |:--- |
| GIOA\[6\]/N2HET2\[4\]/EPWM1B | H3 |
| GIOA\[7\]/N2HET2\[6\]/EPWM2A | M1 |
| GIOB\[0\] | M2 |
| GIOB\[1\] | K2 |
| GIOB\[2\] | F2 |
| MIBSPI3NCS\[0\]/AD2EVT/GIOB\[2\]/ | V10(1) |

# GIOA\[6\] /N2HET2\[4\]/EPWM1B H3

# GIOA\[7\] /N2HET2\[6\]/EPWM2A M1

# GIOB\[0\] M2

# GIOB\[1\] K2

# GIOB\[2\] F2

# MIBSPI3NCS\[0\]/AD2EVT/ GIOB\[2\] / V10 (1)

# EQEP1I/N2HET2\_PIN\_nDIS

| GIOB\[3\] | W10 |
|:--- |:--- |
| GIOB\[4\] | G1 |
| GIOB\[5\] | G2 |
| GIOB\[6\] | J2 |
| GIOB\[7\] | F1 |

# GIOB\[4\] G1

# GIOB\[5\] G2

# GIOB\[6\] J2

# GIOB\[7\] F1

(1) GIOB\[2\] cannot output a level on to terminal V10. Only the input functionality is supported so that the application can generate an interrupt whenever the N2HET2\_PIN\_nDIS is asserted (driven low). Also, a pull up is enabled on the input. This is not programmable using the GIO module control registers.

## 4.3.2.7

**FlexRay** ** ** **Interface Controller (FlexRay)**

## Table 4-30. FlexRay Interface Controller (FlexRay)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **ZWT**

**FRAYRX1** A15 Input Pull Up Fixed 100 µA FlexRay data receive Pull Up (channel 1)

**FRAYTX1** B15 Output N/A None FlexRay data transmit (channel 1)

**FRAYTXEN1** B16 Output FlexRay transmit enable (channel 1)

**FRAYRX2** A8 Input Pull Up Fixed 100 µA FlexRay data receive Pull Up (channel 2)

**FRAYTX2** B8 Output N/A None FlexRay data transmit (channel 2)

**FRAYTXEN2** B9 Output FlexRay transmit enable (channel 2)

*Terminal Configuration and Functions* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 4.3.2.8

**Controller Area Network Controllers (DCAN)**

## Table 4-31. ZWT Controller Area Network Controllers (DCAN)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **ZWT**

**CAN1RX** B10 I/O Pull Up Programmable, CAN1 receive, or GPIO 20 µA **CAN1TX** A10 CAN1 transmit, or GPIO

| CAN2RX | H1 | CAN2 receive, or GPIO |
|:--- |:--- |:--- |
| CAN2TX | H2 | CAN2 transmit, or GPIO |
| CAN3RX | M19 | CAN3 receive, or GPIO |
| CAN3TX | M18 | CAN3 transmit, or GPIO | **CAN2TX** H2 CAN2 transmit, or GPIO **CAN3RX** M19 CAN3 receive, or GPIO **CAN3TX** M18 CAN3 transmit, or GPIO

## 4.3.2.9

**Local** ** ** **Interconnect Network Interface Module (LIN)**

## Table 4-32. ZWT Local Interconnect Network Interface Module (LIN)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **ZWT**

**LINRX** A7 I/O Pull Up Programmable, LIN receive, or GPIO 20 µA **LINTX** B7 LIN transmit, or GPIO

## 4.3.2.10

**Standard Serial Communication Interface** ** ** **(SCI)**

## Table 4-33. ZWT Standard Serial Communication Interface (SCI)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **ZWT**

N2HET1\[6\]/ **SCIRX** /EPWM5A W3 I/O Pull Down Programmable, SCI receive, or GPIO 20 µA N2HET1\[13\]/ **SCITX** /EPWM5B N2 SCI transmit, or GPIO

Copyright © 2012-2015, Texas Instruments Incorporated *Terminal Configuration and Functions* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## 4.3.2.11

**Inter-Integrated Circuit Interface Module (I2C)**

## Table 4-34. ZWT Inter-Integrated Circuit Interface Module (I2C)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **ZWT**

MIBSPI3NCS\[2\]/ **I2C\_SDA** /N2HET1\[27\]/nTZ2 B2 I/O Pull Up Programmable, I2C serial data, or GPIO 20 µA MIBSPI3NCS\[3\]/ **I2C\_SCL** /N2HET1\[29\]/nTZ1 C3 I2C serial clock, or GPIO

## 4.3.2.12

**Standard Serial Peripheral Interface (SPI)**

## Table 4-35. ZWT Standard Serial Peripheral Interface (SPI)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **ZWT**

**SPI2CLK** E2 I/O Pull Up Programmable, SPI2 clock, or GPIO 20 µA **SPI2NCS\[0\]** N3 SPI2 chip select, or GPIO

SPI2NENA/ **SPI2NCS\[1\]** D3 SPI2 chip select, or GPIO

# SPI2NENA /SPI2NCS\[1\] D3 SPI2 enable, or GPIO

**SPI2SIMO\[0\]** D1 SPI2 slave-input masteroutput, or GPIO

**SPI2SOMI\[0\]** D2 SPI2 slave-output masterinput, or GPIO

N2HET1\[0\]/ **SPI4CLK** /EPWM2B K18 I/O Pull Down Programmable, SPI4 clock, or GPIO 20 µA N2HET1\[3\]/ **SPI4NCS\[0\]** /N2HET2\[10\]/EQEP2B U1 SPI4 chip select, or GPIO

# N2HET1\[1\]/ SPI4NENA /N2HET2\[8\]/EQEP2A V2 SPI4 enable, or GPIO

N2HET1\[2\]/ **SPI4SIMO\[0\]** /EPWM3A W5 SPI4 slave-input masteroutput, or GPIO

N2HET1\[5\]/ **SPI4SOMI\[0\]** /N2HET2\[12\]/EPWM3B V6 SPI4 slave-output masterinput, or GPIO

*Terminal Configuration and Functions* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 4.3.2.13

**Multibuffered Serial Peripheral Interface Modules (MibSPI)**

## Table 4-36. ZWT Multibuffered Serial Peripheral Interface Modules (MibSPI)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **ZWT**

**MIBSPI1CLK** F18 I/O Pull Up Programmable, MibSPI1 clock, or GPIO 20 µA **MIBSPI1NCS\[0\]** /MIBSPI1SOMI\[1\]/MII\_TXD\[2\]/ECAP6 R2 MibSPI1 chip select, or GPIO **MIBSPI1NCS\[1\]** /N2HET1\[17\]/MII\_COL/EQEP1S F3

# MIBSPI1NCS\[2\] /N2HET1\[19\]/MDIO G3

# MIBSPI1NCS\[3\] /N2HET1\[21\] J3

N2HET1\[15\]/ **MIBSPI1NCS\[4\]** /ECAP1 N1 Pull Down Programmable, MibSPI1 chip select, or 20 µA GPIO N2HET1\[24\]/ **MIBSPI1NCS\[5\]** /MII\_RXD\[0\]/RMII\_RXD\[0\] P1

**MIBSPI1NENA** /N2HET1\[23\]/MII\_RXD\[2\]/ECAP4 G19 Pull Up Programmable, MibSPI1 enable, or GPIO 20 µA **MIBSPI1SIMO\[0\]** F19 MibSPI1 slave-in masterout, or GPIO

N2HET1\[8\]/ **MIBSPI1SIMO\[1\]** /MII\_TXD\[3\] E18 Pull Down Programmable, MibSPI1 slave-in master20 µA out, or GPIO

**MIBSPI1SOMI\[0\]** G18 Pull Up Programmable, MibSPI1 slave-out master20 µA in, or GPIO MIBSPI1NCS\[0\]/ **MIBSPI1SOMI\[1\]** /MII\_TXD\[2\]/ECAP6 R2

**MIBSPI3CLK** /AWM1\_EXT\_SEL\[1\]/EQEP1A V9 I/O Pull Up Programmable, MibSPI3 clock, or GPIO 20 µA **MIBSPI3NCS\[0\]** /AD2EVT/GIOB\[2\]/ V10 MibSPI3 chip select, or EQEP1I/N2HET2\_PIN\_nDIS GPIO

| MIBSPI3NCS\[1\]/N2HET1\[25\]/MDCLK | V5 |
|:--- |:--- |
| MIBSPI3NCS\[2\]/I2C\_SDA/N2HET1\[27\]/nTZ2 | B2 |
| MIBSPI3NCS\[3\]/I2C\_SCL/N2HET1\[29\]/nTZ1 | C3 |

# MIBSPI3NCS\[2\] /I2C\_SDA/N2HET1\[27\]/nTZ2 B2

# MIBSPI3NCS\[3\] /I2C\_SCL/N2HET1\[29\]/nTZ1 C3

N2HET1\[11\]/ **MIBSPI3NCS\[4\]** /N2HET2\[18\]/EPWM1SYNCO E3 Pull Down Programmable, MibSPI3 chip select, or 20 µA GPIO

MIBSPI3NENA/ **MIBSPI3NCS\[5\]** /N2HET1\[31\]/EQEP1B W9 Pull Up Programmable, MibSPI3 chip select, or 20 µA GPIO

# MIBSPI3NENA /MIBSPI3NCS\[5\]/N2HET1\[31\]/EQEP1B W9 MibSPI3 enable, or GPIO

**MIBSPI3SIMO\[0\]** /AWM1\_EXT\_SEL\[0\]/ECAP3 W8 MibSPI3 slave-in masterout, or GPIO

**MIBSPI3SOMI\[0\]** /AWM1\_EXT\_ENA/ECAP2 V8 MibSPI3 slave-out masterin, or GPIO

**MIBSPI5CLK** /MII\_TXEN/RMII\_TXEN H19 I/O Pull Up Programmable, MibSPI5 clock, or GPIO 20 µA **MIBSPI5NCS\[0\]** /EPWM4A E19 MibSPI5 chip select, or GPIO **MIBSPI5NCS\[1\]** B6

# MIBSPI5NCS\[2\] W6

# MIBSPI5NCS\[3\] T12

# MIBSPI5NENA /MII\_RXD\[3\]/MIBSPI5SOMI\[1\]/ECAP5 H18 MibSPI5 enable, or GPIO

# MIBSPI5SIMO\[0\] /MIBSPI5SOMI\[2\]/MII\_TXD\[1\]/RMII\_TXD\[1\]

J19 MibSPI5 slave-in masterout, or GPIO **MIBSPI5SIMO\[1\]** E16

# MIBSPI5SIMO\[2\] H17

# MIBSPI5SIMO\[3\] G17

**MIBSPI5SOMI\[0\]** /MII\_TXD\[0\]/RMII\_TXD\[0\] J18 MibSPI5 slave-out masterin, or GPIO **MIBSPI5SOMI\[1\]** E17

| MIBSPI5NENA/MII\_RXD\[3\]/MIBSPI5SOMI\[1\]/ECAP5 | H18 |
|:--- |:--- |
| MIBSPI5SOMI\[2\] | H16 |
| MIBSPI5SIMO\[0\]/MIBSPI5SOMI\[2\]/MII\_TXD\[1\]/RMII\_TXD\[1\] | J19 |
| MIBSPI5SOMI\[3\] | G16 |

# MIBSPI5SOMI\[2\] H16

# MIBSPI5SIMO\[0\]/ MIBSPI5SOMI\[2\] /MII\_TXD\[1\]/RMII\_TXD\[1\] J19

# MIBSPI5SOMI\[3\] G16

Copyright © 2012-2015, Texas Instruments Incorporated *Terminal Configuration and Functions* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## 4.3.2.14 **Ethernet Controller**

## Table 4-37. ZWT Ethernet Controller: MDIO Interface

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **ZWT**

MIBSPI3NCS\[1\]/N2HET1\[25\]/ **MDCLK** V5 Output Pull Up None Serial clock output

MIBSPI1NCS\[2\]/N2HET1\[19\]/ **MDIO** G3 I/O Pull Up Fixed 20 µA Serial data input/output Pull Up

## Table 4-38. ZWT Ethernet Controller: Reduced Media Independent Interface (RMII)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **ZWT**

N2HET1\[12\]/MII\_CRS/ **RMII\_CRS\_DV** B4 Input Pull Down Fixed 20 µA RMII carrier sense and Pull Down receive data valid

N2HET1\[28\]/MII\_RXCLK/ **RMII\_REFCLK** /MII\_RX\_VCLKA4 K19 RMII synchronous reference clock for receive, transmit and control interface

AD1EVT/MII\_RX\_ER/ **RMII\_RX\_ER** N19 RMII receive error

# N2HET1\[24\]/MIBSPI1NCS\[5\]/MII\_RXD\[0\]/ RMII\_RXD\[0\] P1 RMII receive data

# N2HET1\[26\]/MII\_RXD\[1\]/ RMII\_RXD\[1\] A14

MIBSPI5SOMI\[0\]/MII\_TXD\[0\]/ **RMII\_TXD\[0\]** J18 Output Pull Up None RMII transmit data

# MIBSPI5SIMO\[0\]/MIBSPI5SOMI\[2\]/MII\_TXD\[1\]/ RMII\_TXD\[1\] J19

MIBSPI5CLK/MII\_TXEN/ **RMII\_TXEN** H19 RMII transmit enable

## Table 4-39. ZWT Ethernet Controller: Media Independent Interface (MII)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **ZWT**

MIBSPI1NCS\[1\]/N2HET1\[17\]/ **MII\_COL** /EQEP1S F3 Input Pull Up None Collision detect

N2HET1\[12\]/ **MII\_CRS** /RMII\_CRS\_DV B4 Pull Down Fixed 20 µA Carrier sense and receive Pull Down data valid

N2HET1\[28\]/MII\_RXCLK/RMII\_REFCLK/ **MII\_RX\_VCLKA4** K19 I/O Pull Down None MII output receive clock

N2HET1\[30\]/ **MII\_RX\_DV** /EQEP2S B11 Input Pull Down Fixed 20 µA Received data valid Pull Down AD1EVT/ **MII\_RX\_ER** /RMII\_RX\_ER N19 Receive error

# N2HET1\[28\]/ MII\_RXCLK /RMII\_REFCLK/MII\_RX\_VCLKA4 K19 I/O Receive clock

N2HET1\[24\]/MIBSPI1NCS\[5\]/ **MII\_RXD\[0\]** /RMII\_RXD\[0\] P1 Input Receive data

# N2HET1\[26\]/ MII\_RXD\[1\] /RMII\_RXD\[1\] A14

# MIBSPI1NENA/N2HET1\[23\]/ MII\_RXD\[2\] /ECAP4 G19 Pull Up Fixed 20 µA

# Pull Down

MIBSPI5NENA/ **MII\_RXD\[3\]** /MIBSPI5SOMI\[1\]/ ECAP5 H18

N2HET1\[10\]/MII\_TXCLK/ **MII\_TX\_VCLKA4** /nTZ3 D19 I/O Pull Down None MII output transmit clock

N2HET1\[10\]/ **MII\_TXCLK** /MII\_TX\_VCLKA4/nTZ3 D19 Fixed 20 µA Transmit clock Pull Down

MIBSPI5SOMI\[0\]/ **MII\_TXD\[0\]** /RMII\_TXD\[0\] J18 Output Pull Up None Transmit data

# MIBSPI5SIMO\[0\]/MIBSPI5SOMI\[2\]/ MII\_TXD\[1\] /RMII\_TXD\[1\] J19

# MIBSPI1NCS\[0\]/MIBSPI1SOMI\[1\]/ MII\_TXD\[2\] /ECAP6 R2

# N2HET1\[8\]/MIBSPI1SIMO\[1\]/ MII\_TXD\[3\] E18 Pull Down

MIBSPI5CLK/ **MII\_TXEN** /RMII\_TXEN H19 Pull Up Transmit enable

*Terminal Configuration and Functions* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 4.3.2.15 **External Memory Interface (EMIF)**

## Table 4-40. External Memory Interface (EMIF)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **ZWT**

**EMIF\_CKE** L3 Output Pull Up None EMIF Clock Enable

**EMIF\_CLK** K3 I/O None EMIF clock. This is an output signal in functional mode. It is gated off by default, so that the signal is pulled up. PINMUX29\[8\] must be cleared to enable this output.

**EMIF\_nOE** E12 Output Pull Up None EMIF Read Enable

**EMIF\_nWAIT** P3 I/O Pull Up Fixed 20 µA EMIF Extended Wait Pull Up Signal

**EMIF\_nWE** D17 Output Pull Up None EMIF Write Enable

**EMIF\_nCAS** R4 Output EMIF column address strobe

**EMIF\_nRAS** R3 Output EMIF row address strobe

**EMIF\_nCS\[0\]** /N2HET2\[7\] (1) N17 Output EMIF chip select, synchronous

**EMIF\_nCS\[2\]** L17 Output EMIF chip selects, asynchronous **EMIF\_nCS\[3\]** /N2HET2\[9\] (1) K17 Output This applies to chip **EMIF\_nCS\[4\]** M17 Output selects 2, 3 and 4

**EMIF\_nDQM\[0\]** E10 Output EMIF Data Mask or Write Strobe. **EMIF\_nDQM\[1\]** E11 Output Data mask for SDRAM devices, write strobe for connected asynchronous devices.

**EMIF\_BA\[0\]** E13 Output EMIF bank address or address line

**EMIF\_BA\[1\]** /N2HET2\[5\] (1) D16 Output EMIF bank address or address line

**EMIF\_ADDR\[0\]** /N2HET2\[1\] (1) D4 Output EMIF address

| EMIF\_ADDR\[1\]/N2HET2\[3\](1) | D5 | Output |
|:--- |:--- |:--- |
| EMIF\_ADDR\[2\] | E6 | Output |
| EMIF\_ADDR\[3\] | E7 | Output |
| EMIF\_ADDR\[4\] | E8 | Output |
| EMIF\_ADDR\[5\] | E9 | Output |
| EMIF\_ADDR\[6\]/N2HET2\[11\](1) | C4 | Output |
| EMIF\_ADDR\[7\]/N2HET2\[13\](1) | C5 | Output |
| EMIF\_ADDR\[8\]/N2HET2\[15\](1) | C6 | Output |
| EMIF\_ADDR\[9\] | C7 | Output |
| EMIF\_ADDR\[10\] | C8 | Output |
| EMIF\_ADDR\[11\] | C9 | Output |
| EMIF\_ADDR\[12\] | C10 | Output |
| (1) | These signals are tri-stated and pulled up by default after power-up. Any application that requires the EMIF must set the bit 31 of the | system module general-purpose register GPREG1. |
| Copyright © 2012-2015, Texas Instruments Incorporated | Terminal Configuration and Functions | Submit Documentation Feedback | **EMIF\_ADDR\[2\]** E6 Output **EMIF\_ADDR\[3\]** E7 Output **EMIF\_ADDR\[4\]** E8 Output **EMIF\_ADDR\[5\]** E9 Output

# EMIF\_ADDR\[6\] /N2HET2\[11\] (1) C4 Output

# EMIF\_ADDR\[7\] /N2HET2\[13\] (1) C5 Output

# EMIF\_ADDR\[8\] /N2HET2\[15\] (1) C6 Output **EMIF\_ADDR\[9\]** C7 Output **EMIF\_ADDR\[10\]** C8 Output **EMIF\_ADDR\[11\]** C9 Output **EMIF\_ADDR\[12\]** C10 Output

(1) These signals are tri-stated and pulled up by default after power-up. Any application that requires the EMIF must set the bit 31 of the system module general-purpose register GPREG1.

Copyright © 2012-2015, Texas Instruments Incorporated *Terminal Configuration and Functions* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## Table 4-40. External Memory Interface (EMIF) (continued)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **ZWT**

**EMIF\_DATA\[0\]** K15 I/O Pull Up Fixed 20 µA EMIF Data Pull Up **EMIF\_DATA\[1\]** L15 I/O

| EMIF\_DATA\[2\] | M15 | I/O |
|:--- |:--- |:--- |
| EMIF\_DATA\[3\] | N15 | I/O |
| EMIF\_DATA\[4\] | E5 | I/O |
| EMIF\_DATA\[5\] | F5 | I/O |
| EMIF\_DATA\[6\] | G5 | I/O |
| EMIF\_DATA\[7\] | K5 | I/O |
| EMIF\_DATA\[8\] | L5 | I/O |
| EMIF\_DATA\[9\] | M5 | I/O |
| EMIF\_DATA\[10\] | N5 | I/O |
| EMIF\_DATA\[11\] | P5 | I/O |
| EMIF\_DATA\[12\] | R5 | I/O |
| EMIF\_DATA\[13\] | R6 | I/O |
| EMIF\_DATA\[14\] | R7 | I/O |
| EMIF\_DATA\[15\] | R8 | I/O |
| Terminal Configuration and Functions | Copyright © 2012-2015, Texas Instruments Incorporated | Submit Documentation Feedback |

# EMIF\_DATA\[3\] N15 I/O

# EMIF\_DATA\[4\] E5 I/O

# EMIF\_DATA\[5\] F5 I/O

# EMIF\_DATA\[6\] G5 I/O

# EMIF\_DATA\[7\] K5 I/O

# EMIF\_DATA\[8\] L5 I/O

# EMIF\_DATA\[9\] M5 I/O

# EMIF\_DATA\[10\] N5 I/O

# EMIF\_DATA\[11\] P5 I/O

# EMIF\_DATA\[12\] R5 I/O

# EMIF\_DATA\[13\] R6 I/O

# EMIF\_DATA\[14\] R7 I/O

# EMIF\_DATA\[15\] R8 I/O

*Terminal Configuration and Functions* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 4.3.2.16 **System Module Interface**

## Table 4-41. ZWT System Module Interface

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **ZWT**

**nPORRST** W7 Input Pull Down Fixed 100 µA Power-on reset, cold reset Pull Down External power supply monitor circuitry must drive nPORRST low when any of the supplies to the microcontroller fall out of the specified range. This terminal has a glitch filter. See Section 6.8.

**nRST** B17 I/O Pull Up Fixed 100 µA System reset, warm reset, Pull Up bidirectional. The internal circuitry indicates any reset condition by driving nRST low. The external circuitry can assert a system reset by driving nRST low. To ensure that an external reset is not arbitrarily generated, TI recommends that an external pull-up resistor is connected to this terminal. This terminal has a glitch filter. See Section 6.8.

**nERROR** B14 I/O Pull Down Fixed 20 µA ESM Error Signal Pull Down Indicates error of high severity. See Section 6.18.

## 4.3.2.17 **Clock Inputs and Outputs**

## Table 4-42. ZWT Clock Inputs and Outputs

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **ZWT**

**OSCIN** K1 Input N/A None From external crystal/resonator, or external clock input

**KELVIN\_GND** L2 Input Kelvin ground for oscillator

**OSCOUT** L1 Output To external crystal/resonator

**ECLK** A12 I/O Pull Down Programmable, External prescaled clock 20 µA output, or GIO.

GIOA\[5\]/ **EXTCLKIN** /EPWM1A/N2HET1\_PIN\_nDIS B5 Input Pull Down 20 µA External clock input #1

**EXTCLKIN2** R9 Input External clock input #2

**VCCPLL** P11 1.2V N/A None Dedicated core supply for Power PLL's

Copyright © 2012-2015, Texas Instruments Incorporated *Terminal Configuration and Functions* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## 4.3.2.18

**Test** ** ** **and Debug Modules Interface**

## Table 4-43. ZWT Test and Debug Modules Interface

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **ZWT**

**TEST** U2 Input Pull Down Fixed 100 µA Test enable. This terminal Pull Down must be connected to ground directly or via a pull-down resistor. **nTRST** D18 Input JTAG test hardware reset

**RTCK** A16 Output N/A None JTAG return test clock

**TCK** B18 Input Pull Down Fixed 100 µA JTAG test clock Pull Down

**TDI** A17 Input Pull Up Fixed 100 µA JTAG test data in Pull Up

**TDO** C18 Output 100 µA None JTAG test data out Pull Down

**TMS** C19 Input Pull Up Fixed 100 µA JTAG test select Pull Up

## 4.3.2.19 **Flash** ** ** **Supply and Test Pads**

## Table 4-44. ZWT Flash Supply and Test Pads

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **ZWT**

**VCCP** F8 3.3V N/A None Flash pump supply Power

**FLTP1** J5 - - N/A None Flash test pads. These terminals are reserved for **FLTP2** H5 TI use only. For proper operation these terminals must connect only to a test pad or not be connected at all \[no connect (NC)\].

*Terminal Configuration and Functions* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 4.3.2.20 **No Connects**

## Table 4-45. No Connects

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **ZWT**

NC C11 - - N/A None No Connects. These balls are not connected to any NC C12 - - N/A None internal logic and can be NC C13 - - N/A None connected to the PCB ground without affecting NC C14 - - N/A None the functionality of the NC C15 - - N/A None device. NC C16 - - N/A None

| NC | C17 | -- N/A | None |
|:--- |:--- |:--- |:--- |
| NC | D6 | -- N/A | None |
| NC | D7 | -- N/A | None |
| NC | D8 | -- N/A | None |
| NC | D9 | -- N/A | None |
| NC | D10 | -- N/A | None |
| NC | D11 | -- N/A | None |
| NC | D12 | -- N/A | None |
| NC | D13 | -- N/A | None |
| NC | D14 | -- N/A | None |
| NC | D15 | -- N/A | None |
| NC | E4 | -- N/A | None |
| NC | E14 | -- N/A | None |
| NC | E15 | -- N/A | None |
| NC | F4 | -- N/A | None |
| NC | F15 | -- N/A | None |
| NC | F16 | -- N/A | None |
| NC | F17 | -- N/A | None |
| NC | G4 | -- N/A | None |
| NC | G15 | -- N/A | None |
| NC | H15 | -- N/A | None |
| NC | J15 | -- N/A | None |
| NC | J16 | -- N/A | None |
| NC | K4 | -- N/A | None |
| NC | K16 | -- N/A | None |
| NC | L4 | -- N/A | None |
| NC | L16 | -- N/A | None |
| NC | L18 | -- N/A | None |
| NC | L19 | -- N/A | None |
| NC | M4 | -- N/A | None |
| NC | M16 | -- N/A | None |
| NC | N4 | -- N/A | None |
| NC | N16 | -- N/A | None |
| NC | N18 | -- N/A | None |
| NC | P4 | -- N/A | None | NC D6 - - N/A None NC D7 - - N/A None NC D8 - - N/A None NC D9 - - N/A None NC D10 - - N/A None NC D11 - - N/A None NC D12 - - N/A None NC D13 - - N/A None NC D14 - - N/A None NC D15 - - N/A None NC E4 - - N/A None NC E14 - - N/A None NC E15 - - N/A None NC F4 - - N/A None NC F15 - - N/A None NC F16 - - N/A None NC F17 - - N/A None NC G4 - - N/A None NC G15 - - N/A None NC H15 - - N/A None NC J15 - - N/A None NC J16 - - N/A None NC K4 - - N/A None NC K16 - - N/A None NC L4 - - N/A None NC L16 - - N/A None NC L18 - - N/A None NC L19 - - N/A None NC M4 - - N/A None NC M16 - - N/A None NC N4 - - N/A None NC N16 - - N/A None NC N18 - - N/A None NC P4 - - N/A None

Copyright © 2012-2015, Texas Instruments Incorporated *Terminal Configuration and Functions* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## Table 4-45. No Connects (continued)

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **ZWT**

NC P15 - - N/A None No Connects. These balls are not connected to any NC P16 - - N/A None internal logic and can be NC P17 - - N/A None connected to the PCB ground without affecting NC R1 - - N/A None the functionality of the NC R10 - - N/A None device. NC R11 - - N/A None

| NC | R12 | -- N/A | None |
|:--- |:--- |:--- |:--- |
| NC | R13 | -- N/A | None |
| NC | R14 | -- N/A | None |
| NC | R15 | -- N/A | None |
| NC | T2 | -- N/A | None |
| NC | T3 | -- N/A | None |
| NC | T4 | -- N/A | None |
| NC | T5 | -- N/A | None |
| NC | T6 | -- N/A | None |
| NC | T7 | -- N/A | None |
| NC | T8 | -- N/A | None |
| NC | T9 | -- N/A | None |
| NC | T10 | -- N/A | None |
| NC | T11 | -- N/A | None |
| NC | T13 | -- N/A | None |
| NC | T14 | -- N/A | None |
| NC | U3 | -- N/A- | None |
| NC | U4 | -- N/A | None |
| NC | U5 | -- N/A | None |
| NC | U6 | -- N/A | None |
| NC | U7 | -- N/A | None |
| NC | U8 | -- N/A | None |
| NC | U9 | -- N/A | None |
| NC | U10 | -- N/A | None |
| NC | U11 | -- N/A | None |
| NC | U12 | -- N/A | None |
| NC | V3 | -- N/A | None |
| NC | V4 | -- N/A | None |
| NC | V11 | -- N/A | None |
| NC | V12 | -- N/A | None |
| NC | W4 | -- N/A | None |
| NC | W11 | -- N/A | None |
| NC | W12 | -- N/A | None |
| NC | W13 | -- N/A | None | NC R13 - - N/A None NC R14 - - N/A None NC R15 - - N/A None NC T2 - - N/A None NC T3 - - N/A None NC T4 - - N/A None NC T5 - - N/A None NC T6 - - N/A None NC T7 - - N/A None NC T8 - - N/A None NC T9 - - N/A None NC T10 - - N/A None NC T11 - - N/A None NC T13 - - N/A None NC T14 - - N/A None NC U3 - - N/ANone NC U4 - - N/A None NC U5 - - N/A None NC U6 - - N/A None NC U7 - - N/A None NC U8 - - N/A None NC U9 - - N/A None NC U10 - - N/A None NC U11 - - N/A None NC U12 - - N/A None NC V3 - - N/A None NC V4 - - N/A None NC V11 - - N/A None NC V12 - - N/A None NC W4 - - N/A None NC W11 - - N/A None NC W12 - - N/A None NC W13 - - N/A None

*Terminal Configuration and Functions* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 4.3.2.21

**Supply** ** ** **for Core Logic: 1.2V nominal**

## Table 4-46. ZWT Supply for Core Logic: 1.2V nominal

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **ZWT**

**VCC** F9 1.2V N/A None Core supply Power **VCC** F10

| VCC | H10 |
|:--- |:--- |
| VCC | J14 |
| VCC | K6 |
| VCC | K8 |
| VCC | K12 |
| VCC | K14 |
| VCC | L6 |
| VCC | M10 |
| VCC | P10 |

# VCC J14

# VCC K6

# VCC K8

# VCC K12

# VCC K14

# VCC L6

# VCC M10

# VCC P10

Copyright © 2012-2015, Texas Instruments Incorporated *Terminal Configuration and Functions* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## 4.3.2.22

**Supply** ** ** **for I/O Cells: 3.3V nominal**

## Table 4-47. ZWT Supply for I/O Cells: 3.3V nominal

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **ZWT**

**VCCIO** F6 3.3V N/A None Operating supply for I/Os Power **VCCIO** F7

| VCCIO | F11 |
|:--- |:--- |
| VCCIO | F12 |
| VCCIO | F13 |
| VCCIO | F14 |
| VCCIO | G6 |
| VCCIO | G14 |
| VCCIO | H6 |
| VCCIO | H14 |
| VCCIO | J6 |
| VCCIO | L14 |
| VCCIO | M6 |
| VCCIO | M14 |
| VCCIO | N6 |
| VCCIO | N14 |
| VCCIO | P6 |
| VCCIO | P7 |
| VCCIO | P8 |
| VCCIO | P9 |
| VCCIO | P12 |
| VCCIO | P13 |
| VCCIO | P14 |

# VCCIO F12

# VCCIO F13

# VCCIO F14

# VCCIO G6

# VCCIO G14

# VCCIO H6

# VCCIO H14

# VCCIO J6

# VCCIO L14

# VCCIO M6

# VCCIO M14

# VCCIO N6

# VCCIO N14

# VCCIO P6

# VCCIO P7

# VCCIO P8

# VCCIO P9

# VCCIO P12

# VCCIO P13

# VCCIO P14

*Terminal Configuration and Functions* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 4.3.2.23

**Ground Reference for All Supplies Except VCCAD**

## Table 4-48. ZWT Ground Reference for All Supplies Except VCCAD

**Terminal** **Signal** **Reset Pull** **Pull Type** **Description** **Type** **State** **Signal** ** ** **Name** **ZWT** **VSS** A1 Ground N/A None Ground reference

| VSS | A2 |
|:--- |:--- |
| VSS | A18 |
| VSS | A19 |
| VSS | B1 |
| VSS | B19 |
| VSS | H8 |
| VSS | H9 |
| VSS | H11 |
| VSS | H12 |
| VSS | J8 |
| VSS | J9 |
| VSS | J10 |
| VSS | J11 |
| VSS | J12 |
| VSS | K9 |
| VSS | K10 |
| VSS | K11 |
| VSS | L8 |
| VSS | L9 |
| VSS | L10 |
| VSS | L11 |
| VSS | L12 |
| VSS | M8 |
| VSS | M9 |
| VSS | M11 |
| VSS | M12 |
| VSS | V1 |
| VSS | W1 |
| VSS | W2 |

# VSS A18

# VSS A19

# VSS B1

# VSS B19

# VSS H8

# VSS H9

# VSS H11

# VSS H12

# VSS J8

# VSS J9

# VSS J10

# VSS J11

# VSS J12

# VSS K9

# VSS K10

# VSS K11

# VSS L8

# VSS L9

# VSS L10

# VSS L11

# VSS L12

# VSS M8

# VSS M9

# VSS M11

# VSS M12

# VSS V1

# VSS W1

# VSS W2

Copyright © 2012-2015, Texas Instruments Incorporated *Terminal Configuration and Functions* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## Specifications

## 5.1

**Absolute Maximum Ratings Over** ** ** **Operating** ** ** **Free-Air Temperature Range** ** ** **(1)**

# MIN **MAX** **UNIT**

# V CC (2) -0.3 1.43 V

Supply voltage range: V CCIO, V CCP (2) -0.3 4.6 V

# V CCAD -0.3 6.25 V

All input pins, with exception of ADC pins -0.3 4.6 V Input voltage range: ADC input pins -0.3 6.25 V

IIK (VI < 0 or VI > VCCIO) +20 mA All pins, except AD1IN\[23:0\] or AD2IN\[15:0\]

Input clamp current: IIK (VI < 0 or VI > VCCAD) +10 mA AD1IN\[23:0\] or AD2IN\[15:0\] Total +40 mA

| Operating free-air temperature range, TA: | -40 | °C |
|:--- | ---: |:--- |
| Operating junction temperature range, TJ: | -40 | °C |
| Storage temperature range, Tstg | -65 | °C |

Operating junction temperature range, T J: °C Storage temperature range, T stg °C

(1) Stresses beyond those listed under "absolute maximum ratings" may cause permanent damage to the device. These are stress ratings only, and functional operation of the device at these or any other conditions beyond those indicated under "recommended operating conditions" is not implied. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability. (2) Maximum-rated conditions for extended periods may affect device reliability. All voltage values are with respect to their associated grounds.

## 5.2 **ESD Ratings**

# VALUE **UNIT**

Human body model (HBM), per AEC Q100-002 (1) \pm2 kV

Electrostatic discharge All pins \pm500 V V ESD Charged device model (CDM), (ESD) performance: Corner pins on 144-pin PGE per AEC Q100-011 \pm750 V (1, 36, 37, 72, 73, 108, 109, 144)

Corner balls on 337-ball ZWT \pm750 V (A1, A19, W1, W19)

(1) AEC Q100-002 indicates HBM stressing is done in accordance with the ANSI/ESDA/JEDEC JS ‑ 001 specification.

## 5.3

**Power-On** ** ** **Hours** ** ** **(POH)** **(1)(2)**

# JUNCTION

**NOMINAL CORE** ** ** **VOLTAGE (V** **CC** **)** **LIFETIME POH** **TEMPERATURE (Tj)** 1.2 105ºC 100K

(1) This information is provided solely for your convenience and does not extend or modify the warranty provided under TI's standard terms and conditions for TI semiconductor products. (2) To avoid significant degradation, the device power-on hours (POH) must be limited to those specified in this table. To convert to equivalent POH for a specific temperature profile, see the * * *Calculating Equivalent* * * *Power-on-Hours for* * * *Hercules Safety* * * *MCUs* Application Report ( SPNA207 ).

*Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 5.4

**Device Recommended Operating** ** ** **Conditions** **(1)**

# MIN **NOM** **MAX** **UNIT**

V CC Digital logic supply voltage (Core) 1.14 1.2 1.32 V V CCPLL PLL Supply Voltage 1.14 1.2 1.32 V

V CCIO Digital logic supply voltage (I/O) 3.3 3.6 V V CCAD MibADC supply voltage 5.25 V V CCP Flash pump supply voltage 3.3 3.6 V V SS Digital logic supply ground V

| VSSAD | MibADC supply ground | -0.1 | 0.1 | V |
|:--- |:--- |:--- |:--- |:--- |
| VADREFHI | A-to-D high-voltage reference source | VSSAD | VCCAD | V |
| VADREFLO | A-to-D low-voltage reference source | VSSAD | VCCAD | V |

V ADREFHI A-to-D high-voltage reference source V SSAD V CCAD V

V ADREFLO A-to-D low-voltage reference source V SSAD V CCAD V

V SLEW Maximum positive slew rate for V CCIO, V CCAD and V CCP supplies V/µs T A Operating free-air temperature °C T J Operating junction temperature (2) °C

(1) All voltages are with respect to V SS, except V CCAD, which is with respect to V SSAD (2) Reliability data is based upon a temperature profile that is equivalent to 100,000 power-on hours at 105°C junction temperature.

Copyright © 2012-2015, Texas Instruments Incorporated *Specifications* *Submit Documentation Feedback*

## Address Wait States

## Data Wait States

# RAM

## Address Wait States

## Data Wait States

## Flash (Main Memory) **0MHz** **0MHz** **0MHz** **0MHz** **50MHz** **150MHz** **150MHz** **HCLK(max)** **HCLK(max)** **HCLK(max)** **HCLK(max)**

## Data Wait States **0MHz** **150MHz** **HCLK(max)**

## Flash (Data Memory) **100MHz** **50MHz** **100MHz**

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## 5.5

**Switching** ** ** **Characteristics Over** ** ** **Recommended Operating** ** ** **Conditions for Clock Domains**

## Table 5-1. Clock Domain Timing Specifications

# PARAMETER

**DESCRIPTION** **CONDITIONS** **MAX** **UNIT** Pipeline mode MHz enabled PGE

Pipeline mode MHz disabled f HCLK HCLK - System clock frequency Pipeline mode MHz enabled ZWT Pipeline mode MHz disabled f GCLK GCLK - CPU clock frequency f HCLK MHz

f VCLK VCLK - Primary peripheral clock frequency MHz

| VCLK2 - Secondary peripheral clock | fVCLK2 | MHz | frequency |
|:--- |:--- |:--- |:--- |
| VCLK3 - Secondary peripheral clock | fVCLK3 | MHz | frequency |
| VCLK4 - Secondary peripheral clock | fVCLK4 | MHz | frequency |
| VCLKA1 - Primary asynchronous | fVCLKA1 | MHz | peripheral clock frequency |
| VCLKA2 - Secondary asynchronous | fVCLKA2 | MHz | peripheral clock frequency |
| VCLKA3 - Primary asynchronous | fVCLKA3 | MHz | peripheral clock frequency |
| VCLKA4 - Secondary asynchronous | fVCLKA4 | MHz | peripheral clock frequency |
| fRTICLK | RTICLK - clock frequency | fVCLK | MHz |

VCLK3 - Secondary peripheral clock f VCLK3 MHz frequency

VCLK4 - Secondary peripheral clock f VCLK4 MHz frequency

VCLKA1 - Primary asynchronous f VCLKA1 MHz peripheral clock frequency

VCLKA2 - Secondary asynchronous f VCLKA2 MHz peripheral clock frequency

VCLKA3 - Primary asynchronous f VCLKA3 MHz peripheral clock frequency

VCLKA4 - Secondary asynchronous f VCLKA4 MHz peripheral clock frequency f RTICLK RTICLK - clock frequency f VCLK MHz

## 5.6 **Wait** ** ** **States** ** ** **Required**

## Figure 5-1. Wait States Scheme

## As shown in the figure above, the TCM RAM can support program and data fetches at full CPU speed without any address or data wait states required.

## The TCM flash can support zero address and data wait states up to a CPU speed of 50 MHz in nonpipelined

mode. The flash supports a maximum CPU clock speed of 160 MHz in pipelined mode for the PGE Package and 180 MHz for the ZWT package, with one address wait state and three data wait states.

## The flash wrapper defaults to non-pipelined mode with zero address wait state and one random-read data wait state.

*Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 5.7

**Power** ** ** **Consumption** ** ** **Over** ** ** **Recommended Operating** ** ** **Conditions**

# PARAMETER

**TEST** ** ** **CONDITIONS** **MIN** **TYP** **MAX** ** ** **UNIT**

fHCLK = 160MHz 175 (1) 360 (2) V CC digital supply current (operating mode) mA f VCLK = f HCLK /2; Flash in pipelined mode; V CCmax fHCLK = 180MHz 195 (1) 380 (2)

I CC LBIST/PBIST clock 215 (1) 475 (3)(4) mA frequency = 80MHz V CC Digital supply current (LBIST/PBIST mode)

LBIST/PBIST clock 475 (3)(4) mA 240 (1) frequency = 90MHz

I CCPLL V CCPLL digital supply current (operating mode) V CCPLL = V CCPLLmax mA

I CCIO V CCIO Digital supply current (operating mode. No DC load, V CCmax mA

Single ADC operational, V CCADmax I CCAD V CCAD supply current (operating mode) mA Both ADCs operational, V CCADmax Single ADC operational, AD REFHImax I ADREFHI AD REFHI supply current (operating mode) mA Both ADCs operational, AD REFHImax read from 1 bank and program I CCP V CCP supply current mA another bank, V CCPmax

(1) The typical value is the average current for the nominal process corner and junction temperature of 25C. (2) The maximum I CC, value can be derated - • linearly with voltage - • by 1 ma/MHz for lower operating frequency when f HCLK = 2 \* f VCLK - • for lower junction temperature by the equation below where T JK is the junction temperature in Kelvin and the result is in milliamperes. **174 - 0.064e** **0.0187** ** ** **T** **JK** (3) The maximum I CC, value can be derated - • linearly with voltage - • by 1.5 ma/MHz for lower operating frequency - • for lower junction temperature by the equation below where T JK is the junction temperature in Kelvin and the result is in milliamperes. **186 - 0.064 e** **0.0187** ** ** **T** **JK** (4) LBIST and PBIST currents are for a short duration, typically less than 10ms. They are usually ignored for thermal calculations for the device and the voltage regulator

Copyright © 2012-2015, Texas Instruments Incorporated *Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## 5.8

**Input/Output** ** ** **Electrical Characteristics Over** ** ** **Recommended Operating** ** ** **Conditions** **(1)**

# PARAMETER

**TEST** ** ** **CONDITIONS** **MIN** **TYP** **MAX** **UNIT**

All inputs (except FRAYRX1, mV V hys Input hysteresis FRAYRX2)

# FRAYRX1, FRAYRX2 mV

All inputs (2) (except FRAYRX1, -0.3 0.8 V V IL Low-level input voltage FRAYRX2)

# FRAYRX1, FRAYRX2 0.4 V CCIO V

All inputs (2) (except FRAYRX1, V CCIO + 0.3 V V IH High-level input voltage FRAYRX2)

# FRAYRX1, FRAYRX2 0.6 V CCIO V

I OL = I OLmax 0.2 V CCIO I OL = 50 µA, standard 0.2 output mode V OL Low-level output voltage V IOL = 50 µA, low-EMI output mode (see 0.2 V CCIO Section 5.13 )

I OH = I OHmax 0.8 V CCIO I OH = 50 µA, standard V CCIO -0.3 output mode V OH High-level output voltage V IOH = 50 µA, low-EMI output mode (see 0.8 V CCIO Section 5.13 )

VI < VSSIO - 0.3 or VI I IK Input clamp current (I/O pins) (3) -3.5 3.5 mA > VCCIO + 0.3 I IH Pulldown 20µA V I = V CCIO I IH Pulldown 100µA V I = V CCIO

I I Input current (I/O pins) I IL Pullup 20µA V I = V SS µA I IL Pullup 100µA V I = V SS

| All other pins | No pullup or pulldown | -1 |
|:--- |:--- |:--- |
| CI | Input capacitance | pF |
| CO | Output capacitance | pF | C I Input capacitance pF C O Output capacitance pF

(1) Source currents (out of the device) are negative while sink currents (into the device) are positive. (2) This does not apply to the nPORRST pin. (3) If the input voltage extends outside of the range V IL to V IH then the input current must be limited to I IK to maintain proper operation. See the application note SPNA201 for more information on limiting input clamp currents.

## 5.9

**Thermal** ** ** **Resistance** ** ** **Characteristics**

## Table 5-2 shows the thermal resistance characteristics for the QFP - PGE mechanical package.

## Table 5-3 shows the thermal resistance characteristics for the BGA - ZWT mechanical package.

## Table 5-2. Thermal Resistance Characteristics (PGE Package)

# °C/W

| Junction-to-free air thermal resistance, Still | RΘJA | air using JEDEC 2S2P test board |
|:--- |:--- | ---: |
| RΘJB | Junction-to-board thermal resistance | 27.2 |
| RΘJC | Junction-to-case thermal resistance | 7.3 |
| ΨJT | Junction-to-package top, Still air | 0.10 |
| Specifications | Copyright © 2012-2015, Texas Instruments Incorporated | Submit Documentation Feedback |

R\ThetaJB Junction-to-board thermal resistance 27.2

R\ThetaJC Junction-to-case thermal resistance 7.3

\PsiJT Junction-to-package top, Still air 0.10

*Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## Table 5-3. Thermal Resistance Characteristics (ZWT Package)

# °C/W

Junction-to-free air thermal resistance, Still R\ThetaJA air (includes 5x5 thermal via cluster in 2s2p 18.8 PCB connected to 1st ground plane)

R\ThetaJB Junction-to-board thermal resistance 14.1

R\ThetaJC Junction-to-case thermal resistance 7.1

Junction-to-package top, Still air (includes \PsiJT 5x5 thermal via cluster in 2s2p PCB 0.33 connected to 1st ground plane)

## 5.10 **Output Buffer Drive** ** ** **Strengths**

## Table 5-4. Output Buffer Drive Strengths

# LOW-LEVEL OUTPUT CURRENT,

**I** **OL** ** for** ** ** **V** **I** **=V** **OLmax**

# or

**SIGNALS** **HIGH-LEVEL OUTPUT** ** ** **CURRENT,**

**I** **OH** ** ** **for** ** ** **V** **I** **=V** **OHmin**

# FRAYTX2, FRAYTX1, FRAYTXEN1, FRAYTXEN2,

# MIBSPI5CLK,

MIBSPI5SOMI\[0\], MIBSPI5SOMI\[1\], MIBSPI5SOMI\[2\], MIBSPI5SOMI\[3\], MIBSPI5SIMO\[0\], MIBSPI5SIMO\[1\], MIBSPI5SIMO\[2\], MIBSPI5SIMO\[3\],

# TMS, TDI, TDO, RTCK,

# SPI4CLK, SPI4SIMO, SPI4SOMI, nERROR,

# N2HET2\[1\], N2HET2\[3\], N2HET2\[5\], N2HET2\[7\], N2HET2\[9\], N2HET2\[11\], N2HET2\[13\], N2HET2\[15\]

# 8 mA ECAP1, ECAP4, ECAP5, ECAP6

# EQEP1I, EQEP1S, EQEP2I, EQEP2S

# EPWM1A,

EPWM1B, EPWM1SYNCO, ETPW2A, EPWM2B, EPWM3A, EPWM3B, EPWM4A, EPWM4B, EPWM5A, EPWM5B, EPWM6A, EPWM6B, EPWM7A, EPWM7B

# EMIF\_ADDR\[0:12\], EMIF\_BA\[0:1\], EMIF\_CKE, EMIF\_CLK, EMIF\_DATA\[0:15\], EMIF\_nCAS,

EMIF\_nCS\[0:4\], EMIF\_nDQM\[0:1\], EMIF\_nOE, EMIF\_nRAS, EMIF\_nWAIT, EMIF\_nWE, EMIF\_RNW

# MDCLK,

MDIO, MII\_RX\_VCLKA4, MII\_TX\_VCLKA4, MII\_TXD\[0:3\], MII\_TXEN, RMII\_REFCLK, RMII\_TXD\[0:1\], RMII\_TXEN

# TEST,

# MIBSPI3SOMI, MIBSPI3SIMO, MIBSPI3CLK, MIBSPI1SIMO, MIBSPI1SOMI, MIBSPI1CLK, 4 mA

# ECAP2, ECAP3

# nRST

# AD1EVT,

# CAN1RX, CAN1TX, CAN2RX, CAN2TX, CAN3RX, CAN3TX,

# GIOA\[0-7\], GIOB\[0-7\],

# LINRX, LINTX,

2 mA zero-dominant MIBSPI1nCS\[0\], MIBSPI1nCS\[1-3\], MIBSPI1nENA, MIBSPI3nCS\[0-3\], MIBSPI3nENA, MIBSPI5nCS\[0-3\], MIBSPI5nENA,

# N2HET1\[0-31\], N2HET2\[0\], N2HET2\[2\], N2HET2\[4\], N2HET2\[5\], N2HET2\[6\], N2HET2\[7\],

N2HET2\[8\], N2HET2\[9\], N2HET2\[10\], N2HET2\[11\], N2HET2\[12\], N2HET2\[13\], N2HET2\[14\], N2HET2\[15\], N2HET2\[16\], N2HET2\[18\],

# SPI2nCS\[0\], SPI2nENA, SPI4nCS\[0\], SPI4nENA

Copyright © 2012-2015, Texas Instruments Incorporated *Specifications* *Submit Documentation Feedback*

# V CCIO **0.6\*V** **CCIO**

# 0.4\*V CCIO **Input** **t** **pw**

# 0.6\*V CCIO

# 0.4\*V CCIO

# V CCIO **V** **IH** **V** **IH**

# V IL **Input** **t** **pw**

# V IL

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## Table 5-4. Output Buffer Drive Strengths (continued)

# LOW-LEVEL OUTPUT CURRENT,

**I** **OL** ** for** ** ** **V** **I** **=V** **OLmax**

# or

**SIGNALS** **HIGH-LEVEL OUTPUT** ** ** **CURRENT,**

**I** **OH** ** ** **for** ** ** **V** **I** **=V** **OHmin**

ECLK, selectable 8 mA / 2 mA SPI2CLK, SPI2SIMO, SPI2SOMI

The default output buffer drive strength is 8 mA for these signals.

## Table 5-5. Selectable 8 mA/2 mA Control

**Signal** **Control** ** ** **Bit** **Address** **8** ** ** **mA** **2** ** ** **mA**

| ECLK | SYSPC10\[0\] | 0xFFFF FF78 |
|:--- |:--- |:--- |
| SPI2CLK | SPI2PC9\[9\] | 0xFFF7 F668 |
| SPI2SIMO | SPI2PC9\[10\] | 0xFFF7 F668 |
| SPI2SOMI | SPI2PC9\[11\](1) | 0xFFF7 F668 |
| (1) | Either SPI2PC9\[11\] or SPI2PC9\[24\] can change the output strength of the SPI2SOMI pin. In case of a 32-bit write where these two bits | differ, SPI2PC9\[11\] determines the drive strength. |

# SPI2CLK SPI2PC9\[9\] 0xFFF7 F668

# SPI2SIMO SPI2PC9\[10\] 0xFFF7 F668

# SPI2SOMI SPI2PC9\[11\] (1) 0xFFF7 F668

(1) Either SPI2PC9\[11\] or SPI2PC9\[24\] can change the output strength of the SPI2SOMI pin. In case of a 32-bit write where these two bits differ, SPI2PC9\[11\] determines the drive strength.

## 5.11 **Input** ** ** **Timings**

## Figure 5-2. TTL-Level Inputs

**Table 5-6. Timing Requirements for Inputs** **(1)** **Parameter** **MIN** **MAX** **Unit**

t pw Input minimum pulse width t c(VCLK) + 10 (2) ns

t in\_slew Time for input signal to go from V IL to V IH or from V IH to V IL ns

(1) t c(VCLK) = peripheral VBUS clock cycle time = 1 / f (VCLK) (2) The timing shown above is only valid for pin used in general-purpose input mode.

## Figure 5-3. Flexray Inputs

## Table 5-7. Timing Requirements for FlexRay Inputs (1) **Parameter** **MIN** **MAX** **Unit**

t pw Input minimum pulse width to meet the Flexray sampling t c(VCLKA2) + 2.5 ns requirement

(1) t c(VCLKA2) = sample clock cycle time for FlexRay = 1 / f (VCLKA2)

*Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 5.12 **Output Timings**

## Table 5-8. Switching Characteristics for Output Timings versus Load Capacitance © L ) **Parameter** **MIN** **MAX** **Unit**

Rise time, t r 8 mA low EMI pins $$ CL = 15 pF $$ 2.5 ns (see Table 5-4 ) $$ CL = 50 pF $$

# CL = 100 pF 7.2

# CL = 150 pF 12.5 Fall time, t f $$ CL = 15 pF $$ 2.5 ns

# CL = 50 pF

# CL = 100 pF 7.2

# CL = 150 pF 12.5

Rise time, t r 4 mA low EMI pins $$ CL = 15 pF $$ 5.6 ns (see Table 5-4 ) $$ CL = 50 pF $$ 10.4

# CL = 100 pF 16.8

# CL = 150 pF 23.2 Fall time, t f $$ CL = 15 pF $$ 5.6 ns

| CL= 50 pF | 10.4 |
|:--- | ---: |
| CL = 100 pF | 16.8 |
| CL = 150 pF | 23.2 |

# CL = 100 pF 16.8

# CL = 150 pF 23.2

Rise time, t r 2 mA-z low EMI pins $$ CL = 15 pF $$ ns (see Table 5-4 ) $$ CL = 50 pF $$

# CL = 100 pF

# CL = 150 pF Fall time, t f $$ CL = 15 pF $$ ns

# CL = 50 pF

# CL = 100 pF

# CL = 150 pF

Rise time, t r Selectable 8 mA / 2 mA-z 8 mA mode $$ CL = 15 pF $$ 2.5 ns pins $$ CL = 50 pF $$ (see Table 5-4 )

# CL = 100 pF 7.2

# CL = 150 pF 12.5 Fall time, t f $$ CL = 15 pF $$ 2.5 ns

# CL = 50 pF

# CL = 100 pF 7.2

# CL = 150 pF 12.5

Rise time, t r 2 mA-z mode $$ CL = 15 pF $$ ns

# CL = 50 pF

# CL = 100 pF

# CL = 150 pF Fall time, t f $$ CL = 15 pF $$ ns

# CL = 50 pF

# CL = 100 pF

# CL = 150 pF

Copyright © 2012-2015, Texas Instruments Incorporated *Specifications* *Submit Documentation Feedback*

# t f

**t** **r** **V** **CCIO** **V** **OH** **V** **OH**

# V OL **V** **OL** **Output**

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## Figure 5-4. CMOS-Level Outputs

**Table 5-9. Timing Requirements for Outputs** **(1)** **Parameter** **MIN** **MAX** **UNIT**

t d(parallel\_out) Delay between low to high, or high to low transition of general-purpose output signals ns that can be configured by an application in parallel, e.g. all signals in a GIOA port, or all N2HET1 signals, etc.

(1) This specification does not account for any output buffer drive strength differences or any external capacitive loading differences. Check Table 5-4 for output buffer drive strength information on each signal.

*Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **5.13** **Low-EMI** ** ** **Output Buffers**

The low-EMI output buffer has been designed explicitly to address the issue of decoupling sources of emissions from the pins which they drive. This is accomplished by adaptively controlling the impedance of the output buffer, and is particularly effective with capacitive loads.

This is not the default mode of operation of the low-EMI output buffers and must be enabled by setting the system module GPCR1 register for the desired module or signal, as shown in. The adaptive impedance control circuit monitors the DC bias point of the output signal. The buffer internally generates two reference levels, VREFLOW and VREFHIGH, which are set to approximately 10% and 90% of V CCIO, respectively.

Once the output buffer has driven the output to a low level, if the output voltage is below VREFLOW, then the output buffer's impedance will increase to hi-Z. A high degree of decoupling between the internal ground bus and the output pin will occur with capacitive loads, or any load in which no current is flowing, e.g. the buffer is driving low on a resistive path to ground. Current loads on the buffer which attempt to pull the output voltage above VREFLOW will be opposed by the buffer's output impedance so as to maintain the output voltage at or below VREFLOW.

Conversely, once the output buffer has driven the output to a high level, if the output voltage is above VREFHIGH then the output buffer's impedance will again increase to hi-Z. A high degree of decoupling between internal power bus ad output pin will occur with capacitive loads or any loads in which no current is flowing, e.g. buffer is driving high on a resistive path to VCCIO. Current loads on the buffer which attempt to pull the output voltage below VREFHIGH will be opposed by the buffer's output impedance so as to maintain the output voltage at or above VREFHIGH.

The bandwidth of the control circuitry is relatively low, so that the output buffer in adaptive impedance control mode cannot respond to high-frequency noise coupling into the buffer's power buses. In this manner, internal bus noise approaching 20% peak-to-peak of VCCIO can be rejected.

Unlike standard output buffers which clamp to the rails, an output buffer in impedance control mode will allow a positive current load to pull the output voltage up to VCCIO + 0.6V without opposition. Also, a negative current load will pull the output voltage down to VSSIO - 0.6V without opposition. This is not an issue since the actual clamp current capability is always greater than the IOH / IOL specifications.

The low-EMI output buffers are automatically configured to be in the standard buffer mode when the device enters a low-power mode.

**Table 5-10.** ** ** **Low-EMI** ** ** **Output** ** ** **Buffer Hookup**

**Module** ** ** **or Signal** ** ** **Name** **Control** ** ** **Register to Enable Low-EMI** ** ** **Mode** Module: MibSPI1 GPREG1.0 Module: SPI2 GPREG1.1 Module: MibSPI3 GPREG1.2 Reserved GPREG1.3 Module: MibSPI5 GPREG1.4 Module: FlexRay GPREG1.5 Module: EMIF GPREG1.6 Reserved GPREG1.7 Signal: TMS GPREG1.8 Signal: TDI GPREG1.9 Signal: TDO GPREG1.10 Signal: RTCK GPREG1.11 Signal: TEST GPREG1.12 Signal: nERROR GPREG1.13 Signal: AD1EVT GPREG1.14

Copyright © 2012-2015, Texas Instruments Incorporated *Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## System Information and Electrical Specifications **6.1** **Device Power** ** ** **Domains**

The device core logic is split up into multiple power domains to optimize the Self-Test Clock Configuration power for a given application use case. There are 7 power domains in total: PD1, PD2, PD3, PD4, PD5, RAM\_PD1, and RAM\_PD2. Refer to Section 1.4 for more information.

PD1 is an "always-ON" power domain, which cannot be turned off. Each of the other power domains can be turned OFF one time during device initialization as per the application requirement. Refer to the Power Management Module (PMM) chapter of TMS570LS12x/11x Technical Reference Manual ( SPNU515 ) for more details.

**NOTE** The clocks to a module must be turned off before powering down the core domain that contains the module.

**NOTE** The logic in the modules that are powered down loses its power completely. Any access to modules that are powered down results in an abort being generated. When power is restored, the modules power-up to their default states (after normal power-up). No register or memory contents are preserved in the core domains that are turned off.

| 6.2 | Voltage Monitor Characteristics |
|:--- |:--- |
| A voltage monitor is implemented on this device. The purpose of this voltage monitor is to eliminate the | requirement for a specific sequence when powering up the core and I/O voltage supplies. |
| 6.2.1 | Important Considerations |

A voltage monitor is implemented on this device. The purpose of this voltage monitor is to eliminate the requirement for a specific sequence when powering up the core and I/O voltage supplies.

***6.2.1*** ***Important*** *** *** ***Considerations***

- • The voltage monitor does not eliminate the need of a voltage supervisor circuit to ensure that the device is held in reset when the voltage supplies are out of range. - • The voltage monitor only monitors the core supply (VCC) and the I/O supply (VCCIO). The other supplies are not monitored by the VMON. For example, if the VCCAD or VCCP are supplied from a source different from that for VCCIO, then there is no internal voltage monitor for the VCCAD and VCCP supplies.

***6.2.2*** ***Voltage*** *** *** ***Monitor Operation***

The voltage monitor generates the Power Good MCU signal (PGMCU) as well as the I/Os Power Good IO signal (PGIO) on the device. During power-up or power-down, the PGMCU and PGIO are driven low when the core or I/O supplies are lower than the specified minimum monitoring thresholds. The PGIO and PGMCU being low isolates the core logic as well as the I/O controls during the power-up or power-down of the supplies. This allows the core and I/O supplies to be powered up or down in any order.

When the voltage monitor detects a low voltage on the I/O supply, it will assert a power-on reset. When the voltage monitor detects an out-of-range voltage on the core supply, it asynchronously makes all output pins high impedance, and asserts a power-on reset. The voltage monitor is disabled when the device enters a low power mode.

The VMON also incorporates a glitch filter for the nPORRST input. Refer to Section 6.3.3.1 for the timing information on this glitch filter.

*System* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## Table 6-1. Voltage Monitoring Specifications

# PARAMETER **MIN** **TYP** **MAX** **UNIT**

VCC low - VCC level below this 0.75 0.9 1.13 V threshold is detected as too low.

Voltage monitoring VCC high - VCC level above this 1.40 1.7 2.1 V MON thresholds threshold is detected as too high.

VCCIO low - VCCIO level below this 1.85 2.4 2.9 threshold is detected as too low.

## 6.2.3 ***Supply*** *** *** ***Filtering***

## The VMON has the capability to filter glitches on the VCC and VCCIO supplies.

## The following table shows the characteristics of the supply filtering. Glitches in the supply larger than the maximum specification cannot be filtered.

## Table 6-2. VMON Supply Glitch Filtering Capability

| Parameter | MIN | MAX |
|:--- |:--- |:--- |
| Width of glitch on VCC that can be filtered | 250 ns | 1 µs |
| Width of glitch on VCCIO that can be filtered | 250 ns | 1 µs |
| Copyright © 2012-2015, Texas Instruments Incorporated | System Information and Electrical Specifications | Submit Documentation Feedback |

Width of glitch on VCC that can be filtered 250 ns 1 µs

Width of glitch on VCCIO that can be filtered 250 ns 1 µs

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

| SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 | www.ti.com |
|:--- |:--- |
| 6.3 | Power Sequencing and Power On Reset |
| 6.3.1 | Power-Up Sequence |

**6.3** **Power** ** ** **Sequencing and** ** ** **Power** ** ** **On** ** ** **Reset** ***6.3.1*** ***Power-Up Sequence***

There is no timing dependency between the ramp of the VCCIO and the VCC supply voltage. The powerup sequence starts with the I/O voltage rising above the minimum I/O supply threshold, (see Table 6-4 for more details), core voltage rising above the minimum core supply threshold and the release of power-on reset. The high frequency oscillator will start up first and its amplitude will grow to an acceptable level. The oscillator start up time is dependent on the type of oscillator and is provided by the oscillator vendor. The different supplies to the device can be powered up in any order.

The device goes through the following sequential phases during power up. **Table 6-3.** ** ** **Power-Up Phases**

Oscillator start-up and validity check 1032 oscillator cycles eFuse autoload 1160 oscillator cycles Flash pump power-up 688 oscillator cycles Flash bank power-up 617 oscillator cycles

**Total** **3497 oscillator** ** ** **cycles**

The CPU reset is released at the end of the above sequence and fetches the first instruction from address 0x00000000.

***6.3.2*** ***Power-Down*** *** *** ***Sequence***

The different supplies to the device can be powered down in any order.

***6.3.3*** ***Power-On*** *** *** ***Reset:*** *** *** ***nPORRST***

This is the power-on reset. This reset must be asserted by an external circuitry whenever the I/O or core supplies are outside the specified recommended range. This signal has a glitch filter on it. It also has an internal pulldown.

**6.3.3.1** **nPORRST Electrical and Timing Requirements**

**Table 6-4. Electrical Requirements for nPORRST**

| NO | Parameter | MIN | MAX | Unit |
|:--- |:--- | ---: |:--- |:--- |
| VCCPORL | VCC low supply level when nPORRST must be active during power- | 0.5 | V | up |
| VCCPORH | VCC high supply level when nPORRST must remain active during | 1.14 | V | power-up and become active during power down |
| VCCIOPORL | VCCIO / VCCP low supply level when nPORRST must be active during | 1.1 | V | power-up |
| VCCIOPORH | VCCIO / VCCP high supply level when nPORRST must remain active | 3.0 | V | during power-up and become active during power down |

V CCPORL V CC low supply level when nPORRST must be active during power0.5 V up

V CCPORH V CC high supply level when nPORRST must remain active during 1.14 V power-up and become active during power down

V CCIOPORL V CCIO / V CCP low supply level when nPORRST must be active during 1.1 V power-up

V CCIOPORH V CCIO / V CCP high supply level when nPORRST must remain active 3.0 V during power-up and become active during power down

V IL(PORRST) Low-level input voltage of nPORRST V CCIO \> 2.5V 0.2 \* V CCIO V

Low-level input voltage of nPORRST V CCIO \< 2.5V 0.5 V

t su(PORRST) Setup time, nPORRST active before V CCIO and V CCP \> V CCIOPORL ms during power-up

t h(PORRST) Hold time, nPORRST active after V CC \> V CCPORH ms

t su(PORRST) Setup time, nPORRST active before V CC \< V CCPORH during power µs down

| th(PORRST) | Hold time, nPORRST active after VCCIO and VCCP \> VCCIOPORH | ms |
|:--- |:--- |:--- |
| th(PORRST) | Hold time, nPORRST active after VCC \< VCCPORL | ms |
| System Information and Electrical Specifications | Copyright © 2012-2015, Texas Instruments Incorporated | Submit Documentation Feedback |

t h(PORRST) Hold time, nPORRST active after V CC \< V CCPORL ms

*System* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# 3.3 V CCIOPORH

# 1.2 V CCPORH

# CCIOPORL

# V (1.2 V) V / V (3.3 V)

# CC

# CCIO CCP

# nPORRST

# CCPORL

# IL(PORRST)

# V / V CCIO CCP

# CC

# CCPORL

# IL(PORRST) IL IL IL

# CCIOPORH

# CCPORH

# CCIOPORL

NOTE: There is no timing dependency between the ramp of the VCCIO and the VCC supply voltage; this is just an exemplary drawing.

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## Table 6-4. Electrical Requirements for nPORRST (continued) **NO** **Parameter** **MIN** **MAX** **Unit** t f(nPORRST) ns Filter time nPORRST pin;

pulses less than MIN will be filtered out, pulses greater than MAX will generate a reset.

## Figure 6-1. nPORRST Timing Diagram

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## 6.4 **Warm** ** ** **Reset (nRST)**

## This is a bidirectional reset signal. The internal circuitry drives the signal low on detecting any device reset

condition. An external circuit can assert a device reset by forcing the signal low. On this terminal, the output buffer is implemented as an open drain (drives low only). To ensure an external reset is not arbitrarily generated, TI recommends that an external pullup resistor is connected to this terminal.

## This terminal has a glitch filter. It also has an internal pullup.

## 6.4.1

***Causes*** *** *** ***of Warm*** *** *** ***Reset***

## Table 6-5. Causes of Warm Reset

# DEVICE EVENT **SYSTEM** ** ** **STATUS** ** ** **FLAG**

Power-Up Reset Exception Status Register, bit 15 Oscillator fail Global Status Register, bit 0 PLL slip Global Status Register, bits 8 and 9

Watchdog exception / Debugger reset Exception Status Register, bit 13

Software Reset Exception Status Register, bit 4

External Reset Exception Status Register, bit 3

## 6.4.2 ***nRST*** *** *** ***Timing Requirements***

## Table 6-6. nRST Timing Requirements

# PARAMETER **MIN** **MAX** **UNIT**

t v(RST) Valid time, nRST active after 2256 t c(OSC) (1) ns nPORRST inactive

| Valid time, nRST active (all other | 32 tc(VCLK) | System reset conditions) |
|:--- |:--- |:--- |
| tf(nRST) | ns | Filter time nRST pin; |
| pulses less than MIN will be | filtered out, pulses greater than | MAX will generate a reset | t f(nRST) ns Filter time nRST pin;

pulses less than MIN will be filtered out, pulses greater than MAX will generate a reset

(1) Assumes the oscillator has started up and stabilized before nPORRST is released..

*System* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback* North Flip West F

# F

# TMS570LS1227

| www.ti.com | SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 |
|:--- |:--- |
| 6.5 | ARM Cortex-R4F CPU Information |
| 6.5.1 | Summary of ARM Cortex-R4F CPU Features |

**6.5** **ARM** ** ** **Cortex-R4F** ** ** **CPU Information**

***6.5.1*** ***Summary of ARM*** *** *** ***Cortex-R4F*** *** *** ***CPU*** *** *** ***Features***

The features of the ARM Cortex-R4F CPU include: - • An integer unit with integral Embedded ICE-RT logic. - • High-speed Advanced Microprocessor Bus Architecture (AMBA) Advanced eXtensible Interfaces (AXI) for Level two (L2) master and slave interfaces. - • Floating Point Coprocessor - • Dynamic branch prediction with a global history buffer, and a 4-entry return stack - • Low interrupt latency. - • Non-maskable interrupt. - • A Harvard Level one (L1) memory system with: - - Tightly-Coupled Memory (TCM) interfaces with support for error correction or parity checking memories - - ARMv7-R architecture Memory Protection Unit (MPU) with 12 regions - • Dual core logic for fault detection in safety-critical applications. - • An L2 memory interface: - - Single 64-bit master AXI interface - - 64-bit slave AXI interface to TCM RAM blocks - • A debug interface to a CoreSight Debug Access Port (DAP). - • A Performance Monitoring Unit (PMU). - • A Vectored Interrupt Controller (VIC) port.

For more information on the ARM Cortex-R4F CPU, see <https://www.arm.com>.

***6.5.2*** ***ARM*** *** *** ***Cortex-R4F*** *** *** ***CPU Features*** *** *** ***Enabled*** *** *** ***by*** *** *** ***Software***

The following CPU features are disabled on reset and must be enabled by the application if required. - • ECC On Tightly-Coupled Memory (TCM) Accesses - • Hardware Vectored Interrupt (VIC) Port - • Floating Point Coprocessor - • Memory Protection Unit (MPU)

***6.5.3*** ***Dual*** *** *** ***Core*** *** *** ***Implementation***

The device has two Cortex-R4F cores, where the output signals of both CPUs are compared in the CCMR4 unit. To avoid common mode impacts the signals of the CPUs to be compared are delayed by 2 clock cycles as shown in Figure 6-3.

The CPUs have a diverse CPU placement given by following requirements: - • different orientation; for example, CPU1 = "north" orientation, CPU2 = "flip west" orientation - • dedicated guard ring for each CPU

**Figure 6-2.** ** ** **Dual - CPU Orientation**

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# CPU 1 CPU 2 2 cycle delay 2 cycle delay

# CCM-R4

# CCM-R4 compare CPU1CLK

# CPU2CLK compare error Input + Control Output + Control

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

***6.5.4*** ***Duplicate*** *** *** ***clock tree after*** *** *** ***GCLK***

The CPU clock domain is split into two clock trees, one for each CPU, with the clock of the 2nd CPU running at the same frequency and in phase to the clock of CPU1. See Figure 6-3.

***6.5.5*** ***ARM*** *** *** ***Cortex-R4F*** *** *** ***CPU Compare Module*** *** *** ***(CCM-R4) for Safety***

This device has two ARM Cortex-R4F CPU cores, where the output signals of both CPUs are compared in the CCM-R4 unit. To avoid common mode impacts the signals of the CPUs to be compared are delayed in a different way as shown in the figure below. **Figure 6-3. Dual Core Implementation**

To avoid an erroneous CCM-R4 compare error, the application software must initialize the registers of both CPUs before the registers are used, including function calls where the register values are pushed onto the stack. ***6.5.6*** ***CPU Self-Test***

The CPU STC (Self-Test Controller) is used to test the two Cortex-R4F CPU Cores using the Deterministic Logic BIST Controller as the test engine.

The main features of the self-test controller are: - • Ability to divide the complete test run into independent test intervals - • Capable of running the complete test as well as running few intervals at a time - • Ability to continue from the last executed interval (test set) as well as ability to restart from the beginning (First test set) - • Complete isolation of the self-tested CPU core from rest of the system during the self-test run - • Ability to capture the Failure interval number - • Timeout counter for the CPU self-test run as a fail-safe feature

*System* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

**6.5.6.1** **Application Sequence for CPU Self-Test**

1. Configure clock domain frequencies. 2. Select number of test intervals to be run. 3. Configure the timeout period for the self-test run. 4. Enable self-test. 5. Wait for CPU reset. 6. In the reset handler, read CPU self-test status to identify any failures. 7. Retrieve CPU state if required.

For more information see TMS570LS12x/11x Technical Reference Manual ( SPNU515 ).

**6.5.6.2** **CPU Self-Test Clock Configuration**

The maximum clock rate for the self-test is 90MHz. The STCCLK is divided down from the CPU clock. This divider is configured by the STCCLKDIV register at address 0xFFFFE108.

For more information see TMS570LS12x/11x Technical Reference Manual ( SPNU515 ). **6.5.6.3** **CPU Self-Test Coverage**

Table 6-7 shows CPU test coverage achieved for each self-test interval. It also lists the cumulative test cycles. The test time can be calculated by multiplying the number of test cycles with the STC clock period.

**Table 6-7. CPU Self-Test** ** ** **Coverage**

# INTERVALS

**TEST** ** ** **COVERAGE, %** **TEST** ** ** **CYCLES** 62.13 70.09 74.49 77.28 79.28 80.90 82.02 83.10 84.08 84.87 85.59 86.11 86.67 87.16 87.61 87.98 88.38 88.69 88.98 89.28 89.50 89.76 90.01 90.21

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# OSCIN OSCOUT

# C1 (see Note A)

# C2 Crystal (a)

# OSCIN OSCOUT (b) External (toggling 0 V to 3.3 V) Clock Signal

Note A: The values of C1 and C2 should be provided by the resonator/crystal vendor. Kelvin\_GND

Note B: Kelvin\_GND should not be connected to any other GND. (see Note B)

# TMS570LS1227

| SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 | www.ti.com |
|:--- |:--- |
| 6.6 | Clocks |
| 6.6.1 | Clock Sources | **6.6** **Clocks** ***6.6.1*** ***Clock Sources***

The table below lists the available clock sources on the device. Each of the clock sources can be enabled or disabled using the CSDISx registers in the system module. The clock source number in the table corresponds to the control bit in the CSDISx register for that clock source.

The table also shows the default state of each clock source.

**Table 6-8.** ** ** **Available** ** ** **Clock Sources**

**Clock** **Name** **Description** **Default** ** ** **State** **Source** ** ** **#**

| OSCIN | Main Oscillator | Enabled |
|:--- |:--- |:--- |
| PLL1 | Output From PLL1 | Disabled |
| Reserved | Reserved | Disabled |
| EXTCLKIN1 | External Clock Input #1 | Disabled |
| LFLPO | Low Frequency Output of Internal Reference Oscillator | Enabled | PLL1 Output From PLL1 Disabled Reserved Reserved Disabled EXTCLKIN1 External Clock Input #1 Disabled

LFLPO Low Frequency Output of Internal Reference Oscillator Enabled

High Frequency Output of Internal Reference HFLPO Enabled Oscillator PLL2 Output From PLL2 Disabled EXTCLKIN2 External Clock Input #2 Disabled **6.6.1.1** **Main** ** ** **Oscillator**

The oscillator is enabled by connecting the appropriate fundamental resonator/crystal and load capacitors across the external OSCIN and OSCOUT pins as shown in Figure 6-4. The oscillator is a single stage inverter held in bias by an integrated bias resistor. This resistor is disabled during leakage test measurement and low power modes.

**TI** ** ** **strongly** ** ** **encourages** ** ** **each** ** ** **customer** ** ** **to** ** ** **submit** ** ** **samples** ** ** **of** ** ** **the** ** ** **device** ** ** **to** ** ** **the** ** ** **resonator/crystal** **vendors** ** ** **for** ** ** **validation.** ** ** **The** ** ** **vendors** ** ** **are** ** ** **equipped** ** ** **to** ** ** **determine** ** ** **what** ** ** **load** ** ** **capacitors** ** ** **will** ** ** **best** ** ** **tune** **their** ** ** **resonator/crystal** ** ** **to** ** ** **the** ** ** **microcontroller** ** ** **device** ** ** **for** ** ** **optimum** ** ** **start-up** ** ** **and** ** ** **operation** ** ** **over** **temperature/voltage extremes.**

An external oscillator source can be used by connecting a 3.3 V clock signal to the OSCIN pin and leaving the OSCOUT pin unconnected (open) as shown in the figure below.

**Figure 6-4. Recommended Crystal/Clock** ** ** **Connection**

*System* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 6.6.1.1.1 ***Timing Requirements for Main Oscillator***

## Table 6-9. Timing Requirements for Main Oscillator

**Parameter** **MIN** **Type** **MAX** **Unit**

tc(OSC) Cycle time, OSCIN (when using a sine-wave input) ns

| tc(OSC\_SQR) | Cycle time, OSCIN, (when input to the OSCIN is a | ns | square wave ) |
|:--- |:--- |:--- |:--- |
| tw(OSCIL) | Pulse duration, OSCIN low (when input to the OSCIN | ns | is a square wave) |
| tw(OSCIH) | Pulse duration, OSCIN high (when input to the OSCIN | ns | is a square wave) |

tw(OSCIL) Pulse duration, OSCIN low (when input to the OSCIN ns is a square wave)

tw(OSCIH) Pulse duration, OSCIN high (when input to the OSCIN ns is a square wave)

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# BIAS\_EN Low Power Oscillator

# LFEN

# LF\_TRIM

# HFEN

# HF\_TRIM

# LFLPO

# HFLPO

# HFLPO\_VALID

# nPORRST

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

**6.6.1.2** **Low** ** ** **Power Oscillator**

The Low Power Oscillator (LPO) is comprised of two oscillators - HF LPO and LF LPO, in a single macro. ***6.6.1.2.1*** ***Features***

The main features of the LPO are: - • Supplies a clock at extremely low power for power-saving modes. This is connected as clock source # 4 of the Global Clock Module. - • Supplies a high-frequency clock for non-timing-critical systems. This is connected as clock source # 5 of the Global Clock Module. - • Provides a comparison clock for the crystal oscillator failure detection circuit. **Figure 6-5.** ** ** **LPO Block Diagram**

Figure 6-5 shows a block diagram of the internal reference oscillator. This is a low power oscillator (LPO) and provides two clock sources: one nominally 80KHz and one nominally 10MHz. **Table 6-10.** ** ** **LPO Specifications**

**Parameter** **MIN** **Typical** **MAX** **Unit**

Clock Detection oscillator fail frequency - lower threshold, using 1.375 2.4 4.875 MHz untrimmed LPO output

oscillator fail frequency - higher threshold, using 38.4 MHz untrimmed LPO output

LPO - HF oscillator untrimmed frequency 5.5 19.5 MHz (f HFLPO ) trimmed frequency 9.6 MHz

startup time from STANDBY (LPO BIAS\_EN High for µs at least 900µs) cold startup time µs LPO - LF oscillator untrimmed frequency kHz

startup time from STANDBY (LPO BIAS\_EN High for µs at least 900µs) cold startup time µs

*System* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# /NR /1 to /64

# OSCIN

# PLL

# INTCLK

# /OD /1 to /8

# VCOCLK

# /R /1 to /32 post\_ODCLK

# /NF /1 to /256

# PLLCLK

# /NR2

# /1 to /64 OSCIN

# PLL#2

# INTCLK2

# /OD2 /1 to /8

# VCOCLK2

# /R2 /1 to /32 post\_ODCLK2

# /NF2 /1 to /256

# PLL2CLK

# fPLLCLK = (fOSCIN / NR) \* NF / (OD \* R)

# fPLL2CLK = (fOSCIN / NR2) \* NF2 / (OD2 \* R2)

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 6.6.1.3

**Phase** ** ** **Locked Loop (PLL) Clock Modules**

## The PLL is used to multiply the input frequency to some higher frequency.

## The main features of the PLL are

- • Frequency modulation can be optionally superimposed on the synthesized frequency of PLL1. The frequency modulation capability of PLL2 is permanently disabled. - • Configurable frequency multipliers and dividers. - • Built-in PLL Slip monitoring circuit. - • Option to reset the device on a PLL slip detection.

## 6.6.1.3.1 ***Block*** *** *** ***Diagram***

## Figure 6-6 shows a high-level block diagram of the two PLL macros on this microcontroller. PLLCTL1 and

PLLCTL2 are used to configure the multiplier and dividers for the PLL1. PLLCTL3 is used to configure the multiplier and dividers for PLL2.

## Figure 6-6. PLLx Block Diagram

## 6.6.1.3.2 ***PLL Timing Specifications***

## Table 6-11. PLL Timing Specifications

| PARAMETER | MIN | MAX | UNIT |
|:--- |:--- |:--- |:--- |
| fINTCLK | PLL1 Reference Clock frequency | f(OSC\_SQR) | MHz |
| fpost\_ODCLK | Post-ODCLK - PLL1 Post-divider input | MHz | clock frequency |
| fVCOCLK | VCOCLK - PLL1 Output Divider (OD) input | MHz | clock frequency |
| fINTCLK2 | PLL2 Reference Clock frequency | f(OSC\_SQR) | MHz |
| fpost\_ODCLK2 | Post-ODCLK - PLL2 Post-divider input | MHz | clock frequency |
| fVCOCLK2 | VCOCLK - PLL2 Output Divider (OD) input | MHz | clock frequency |

f INTCLK PLL1 Reference Clock frequency f (OSC\_SQR) MHz

f post\_ODCLK Post-ODCLK - PLL1 Post-divider input MHz clock frequency

f VCOCLK VCOCLK - PLL1 Output Divider (OD) input MHz clock frequency

f INTCLK2 PLL2 Reference Clock frequency f (OSC\_SQR) MHz

f post\_ODCLK2 Post-ODCLK - PLL2 Post-divider input MHz clock frequency

f VCOCLK2 VCOCLK - PLL2 Output Divider (OD) input MHz clock frequency

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## 6.6.1.4 **External Clock Inputs**

## The device supports up to two external clock inputs. This clock input must be a square wave input. The

electrical and timing requirements for these clock inputs are specified below. The external clock sources are not checked for validity. They are assumed valid when enabled.

## Table 6-12. External Clock Timing and Electrical Specifications

**Parameter** **Description** **Min** **Max** **Unit**

| fEXTCLKx | External clock input frequency | MHz |
|:--- |:--- |:--- |
| tw(EXTCLKIN)H | EXTCLK high-pulse duration | ns |
| tw(EXTCLKIN)L | EXTCLK low-pulse duration | ns | t w(EXTCLKIN)H EXTCLK high-pulse duration ns t w(EXTCLKIN)L EXTCLK low-pulse duration ns

v iL(EXTCLKIN) Low-level input voltage -0.3 0.8 V

v iH(EXTCLKIN) High-level input voltage VCCIO + 0.3 V

## 6.6.2 ***Clock Domains***

## 6.6.2.1 **Clock** ** ** **Domain Descriptions**

## The table below lists the device clock domains and their default clock sources. The table also shows the

system module control register that is used to select an available clock source for each clock domain.

## Table 6-13. Clock Domain Descriptions

**Clock** ** ** **Domain Name** **Default** ** ** **Clock** **Clock** ** ** **Source** **Description** **Source** **Selection** ** ** **Register**

HCLK OSCIN GHVSRC - • Is disabled through the CDDISx registers bit 1 - • Used for all system modules including DMA, ESM

GCLK OSCIN GHVSRC - • Always the same frequency as HCLK - • In phase with HCLK - • Is disabled separately from HCLK through the CDDISx registers bit 0 - • Can be divided by 1up to 8 when running CPU self-test (LBIST) using the CLKDIV field of the STCCLKDIV register at address 0xFFFFE108

GCLK2 OSCIN GHVSRC - • Always the same frequency as GCLK - • 2 cycles delayed from GCLK - • Is disabled along with GCLK - • Gets divided by the same divider setting as that for GCLK when running CPU self-test (LBIST)

VCLK OSCIN GHVSRC - • Divided down from HCLK - • Can be HCLK/1, HCLK/2,... or HCLK/16 - • Is disabled separately from HCLK through the CDDISx registers bit 2

VCLK2 OSCIN GHVSRC - • Divided down from HCLK - • Can be HCLK/1, HCLK/2,... or HCLK/16 - • Frequency must be an integer multiple of VCLK frequency - • Is disabled separately from HCLK through the CDDISx registers bit 3

VCLK3 OSCIN GHVSRC - • Divided down from HCLK - • Can be HCLK/1, HCLK/2,... or HCLK/16 - • Is disabled separately from HCLK through the CDDISx registers bit 8

VCLK4 OSCIN GHVSRC - • Divided down from HCLK - • Can be HCLK/1, HCLK/2,... or HCLK/16 - • Is disabled separately from HCLK through the CDDISx registers bit 9

*System* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## Table 6-13. Clock Domain Descriptions (continued)

**Clock** ** ** **Domain Name** **Default** ** ** **Clock** **Clock** ** ** **Source** **Description** **Source** **Selection** ** ** **Register**

VCLKA1 VCLK VCLKASRC - • Defaults to VCLK as the source - • Is disabled through the CDDISx registers bit 4

VCLKA2 VCLK VCLKASRC - • Defaults to VCLK as the source - • Is disabled through the CDDISx registers bit 5

VCLKA4\_S VCLK VCLKACON1 - • Defaults to VCLK as the source - • Frequency can be as fast as HCLK frequency - • Is disabled through the CDDISx registers bit 11

VCLKA4\_DIVR VCLK VCLKACON1 - • Divided down from the VCLKA4\_S using the VCLKA4R field of the VCLKACON1 register at address 0xFFFFE140 - • Frequency can be VCLKA4\_S/1, VCLKA4\_S/2,..., or VCLKA4\_S/8 - • Default frequency is VCLKA4\_S/2 - • Is disabled separately through the VCLKACON1 register VCLKA4\_DIV\_CDDIS bit only if the VCLKA4\_S clock is not disabled

RTICLK VCLK RCLKSRC - • Defaults to VCLK as the source - • If a clock source other than VCLK is selected for RTICLK, then the RTICLK frequency must be less than or equal to VCLK/3 - - Application can ensure this by programming the RTI1DIV field of the RCLKSRC register, if necessary - • Is disabled through the CDDISx registers bit 6

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# HCLK (to SYSTEM) GCLK, GCLK2 (to CPU)

# GCM /1..16 /1..16 VCLK\_peri (VCLK to peripherals on PCR1)

# OSCIN Low Power Oscillator 10MHz 80kHz /1..64

# X1..256 /1..8 /1..32

## \*

# VCLK /1,2,..1024 Phase\_seg2 CAN Baud Rate Phase\_seg1

# VCLKA1 /1,2,..256 SPIx,MibSPIx /2,3..2 24

# LIN, SCI

# SPI

# LIN / SCI /1,2..32 MibADCx

# ADCLK /1,2..65536 External Clock

# ECLK

# VCLK2

# N2HETx

# HRP /1..64

# LRP /2 0..2 5 Loop Resolution Clock High Baud Rate Baud Rate

# N2HETx TU

# VCLK2 Ethernet

# VCLKA4\_DIVR /1..64

# X1..256 /1..8 /1..32

## \*

# EXTCLKIN1

# EXTCLKIN2

# RTICLK (to RTI, DWWD) /1, 2, 4, or 8

# VCLK

# VCLK3

# EMIF VCLK3 (to EMIF, and Ethernet) /1..16 VCLK\_sys (VCLK to system modules)

\* the frequency at this node must not exceed the maximum HCLK specifiation. /1,2..256

# I2C I2C baud rate /1,2,..4

# VCLKA2

# GTUC1,2

# NTU\[1\]

# NTU\[0\]

# NTU\[2\] NTU\[3\]

# RTI Macro Tick Start of cycle PLL#2 output

# EXTCLKIN1

# VCLKA2 Prop\_seg

# DCANx FlexRay Baud Rate FlexRay TU FlexRay VCLK2 (to N2HETx and HTUx)

# VCLKA1 (to DCANx)

# VCLK VCLKA2 (to FlexRay)

# VCLK

# VCLKA4\_DIVR\_EMAC (to EMAC)

# VCLKA4\_DIVR

# /DIVR

# PLL2 ODCLK/8

# PLL2 ODCLK/16 VCLKA4\_S (left open)

# VCLK

# VCLKA4\_SRC

# PLL #1 (FMzPLL)

# PLL #2 (FMzPLL)

# VCLK4 (to ePWM, eQEP, eCAP) /1..16

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## 6.6.2.2

**Mapping of Clock Domains to Device** ** ** **Modules**

## Each clock domain has a dedicated functionality as shown in the figures below.

## Figure 6-7. Device Clock Domains

## System Information and Electrical Specifications

Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# VCLKA4\_SRC

# VCLK VCLKA4\_S (left open)

# /DIVR PLL2 post\_ODCLK/8 PLL2 post\_ODCLK/16

# VCLKA4\_DIVR\_EMAC (to EMAC)

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

**6.6.2.3** **Special Clock Source Selection Scheme for VCLKA4\_DIVR\_EMAC**

Some applications may need to use both the FlexRay and the Ethernet interfaces. The FlexRay controller requires the VCLKA2 frequency to be 80MHz, while the MII interface requires VCLKA4\_DIVR\_EMAC to be 25MHz and the RMII requires VCLKA4\_DIVR\_EMAC to be 50MHz.

These different frequencies are supported by adding special dedicated clock source selection options for the VCLKA4\_DIVR\_EMAC clock domain. This logic is shown in Figure 6-8.

**Figure 6-8. VCLKA4\_DIVR Source Selection** ** ** **Options**

The PLL2 post\_ODCLK is brought out as a separate output from the PLL wrapper module. There are two additional dividers implemented at the device-level to divide this PLL2 post\_ODCLK by 8 and by 16.

As shown in Figure 6-8, the VCLKA4\_SRC configured through the system module VCLKACON1 control register is used to determine the clock source for the VCLKA4\_S and VCLKA4\_DIVR. An additional multiplexor is implemented to select between the VCLKA4\_DIVR and the two additional clock sources - PLL2 post\_ODCLK/8 and post\_ODCLK/16.

The selection is done as shown in the following table.

**Table 6-14. VCLKA4\_DIVR\_EMAC** ** ** **Clock Source** **Selection**

**VCLKA4\_SRC from** **Clock** ** ** **Source** ** ** **for** **VCLKACON1\[19-16\]** **VCLKA4\_DIVR\_EMAC**

| 0x0 | OSCIN / VCLKA4R |
|:--- |:--- |
| 0x1 | PLL1CLK / VCLKA4R |
| 0x2 | Reserved |
| 0x3 | EXTCLKIN1 / VCLKA4R |
| 0x4 | LF LPO / VCLKA4R |
| 0x5 | HF LPO / VCLKA4R |
| 0x6 | PLL2CLK / VCLKA4R |
| 0x7 | EXTCLKIN2 / VCLKA4R |

# 0x1 PLL1CLK / VCLKA4R 0x2 Reserved

# 0x3 EXTCLKIN1 / VCLKA4R

# 0x4 LF LPO / VCLKA4R

# 0x5 HF LPO / VCLKA4R

# 0x6 PLL2CLK / VCLKA4R

# 0x7 EXTCLKIN2 / VCLKA4R

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## 6.6.3 ***Clock Test Mode***

## The platform architecture defines a special mode that allows various clock signals to be brought out on to

the ECLK pin and N2HET1\[12\] device outputs. This mode is called the Clock Test mode. It is very useful for debugging purposes and can be configured through the CLKTEST register in the system module.

## Table 6-15. Clock Test Mode Options

# SEL\_ECP\_PIN

**SEL\_GIO\_PIN** $$ = $$ **SIGNAL ON ECLK** $$ = $$ **SIGNAL ON N2HET1\[12\]** **CLKTEST\[3-0\]** **CLKTEST\[11-8\]**

| Oscillator | Oscillator Valid Status |
|:--- |:--- |
| Main PLL free-running clock output | Main PLL Valid status |
| Reserved | Reserved |
| EXTCLKIN1 | Reserved |
| LFLPO | Reserved |
| HFLPO | HFLPO Valid status |
| Secondary PLL free-running clock output | Secondary PLL Valid Status |
| EXTCLKIN2 | Reserved |
| GCLK | LFLPO |
| RTI Base | Oscillator Valid status |
| Reserved | Oscillator Valid status |
| VCLKA1 | Oscillator Valid status |
| VCLKA2 | Oscillator Valid status |
| Reserved | Reserved |
| VCLKA4\_DIVR | VCLKA4\_S |
| Reserved | Oscillator Valid status |

Main PLL free-running clock output Main PLL Valid status Reserved Reserved EXTCLKIN1 Reserved LFLPO Reserved HFLPO HFLPO Valid status

Secondary PLL free-running clock output Secondary PLL Valid Status EXTCLKIN2 Reserved

# GCLK LFLPO RTI Base Oscillator Valid status Reserved Oscillator Valid status VCLKA1 Oscillator Valid status VCLKA2 Oscillator Valid status Reserved Reserved

# VCLKA4\_DIVR VCLKA4\_S Reserved Oscillator Valid status

*System* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback* f\[MHz\] 1.375 4.875

fail lower threshold pass upper threshold fail

# TMS570LS1227

| www.ti.com | SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 |
|:--- |:--- |
| 6.7 | Clock Monitoring |
| The LPO Clock Detect (LPOCLKDET) module consists of a clock monitor (CLKDET) and an internal low | power oscillator (LPO). | **6.7** **Clock Monitoring**

The LPO Clock Detect (LPOCLKDET) module consists of a clock monitor (CLKDET) and an internal low power oscillator (LPO).

The LPO provides two different clock sources - a low frequency (LFLPO) and a high frequency (HFLPO).

The CLKDET is a supervisor circuit for an externally supplied clock signal (OSCIN). In case the OSCIN frequency falls out of a frequency window, the CLKDET flags this condition in the global status register (GLBSTAT bit 0: OSC FAIL) and switches all clock domains sourced by OSCIN to the HFLPO clock (limp mode clock).

The valid OSCIN frequency range is defined as: f HFLPO / 4 \< f OSCIN \< f HFLPO \* 4. ***6.7.1*** ***Clock Monitor Timings***

For more information on LPO and Clock detection, refer to Table 6-10.

**Figure 6-9. LPO and Clock Detection,** ** ** **Untrimmed HFLPO**

***6.7.2*** ***External Clock (ECLK)*** *** *** ***Output Functionality***

The ECLK pin can be configured to output a pre-scaled clock signal indicative of an internal device clock. This output can be externally monitored as a safety diagnostic.

***6.7.3*** ***Dual*** *** *** ***Clock Comparators***

The Dual Clock Comparator (DCC) module determines the accuracy of selectable clock sources by counting the pulses of two independent clock sources (counter 0 and counter 1). If one clock is out of spec, an error signal is generated. For example, the DCC1 can be configured to use HFLPO as the reference clock (for counter 0) and VCLK as the "clock under test" (for counter 1). This configuration allows the DCC1 to monitor the PLL output clock when VCLK is using the PLL output as its source.

An additional use of this module is to measure the frequency of a selectable clock source, using the input clock as a reference, by counting the pulses of two independent clock sources. Counter 0 generates a fixed-width counting window after a preprogrammed number of pulses. Counter 1 generates a fixed-width pulse (1 cycle) after a pre-programmed number of pulses. This pulse sets as an error signal if counter 1 does not reach 0 within the counting window generated by counter 0. **6.7.3.1** **Features**

- • Takes two different clock sources as input to two independent counter blocks. - • One of the clock sources is the known-good, or reference clock; the second clock source is the "clock under test." - • Each counter block is programmable with initial, or seed values. - • The counter blocks start counting down from their seed values at the same time; a mismatch from the expected frequency for the clock under test generates an error signal which is used to interrupt the CPU.

**6.7.3.2** **Mapping of DCC Clock Source Inputs** **Table 6-16. DCC1 Counter 0 Clock Sources**

| CLOCK SOURCE \[3:0\] | CLOCK NAME |
|:--- |:--- |
| others | oscillator (OSCIN) |
| 0x5 | high frequency LPO | others oscillator (OSCIN) 0x5 high frequency LPO

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## Table 6-16. DCC1 Counter 0 Clock Sources (continued)

# CLOCK SOURCE \[3:0\] **CLOCK NAME** 0xA test clock (TCK)

## Table 6-17. DCC1 Counter 1 Clock Sources

# KEY \[3:0\] **CLOCK SOURCE \[3:0\]** **CLOCK NAME**

| others | -- N2HET1\[31\] |
|:--- |:--- |
| 0x0 | Main PLL free-running clock output |
| 0x1 | PLL #2 free-running clock output |
| 0x2 | low frequency LPO | 0x0 Main PLL free-running clock output 0x1 PLL #2 free-running clock output 0x2 low frequency LPO 0xA 0x3 high frequency LPO

| 0x4 | reserved |
|:--- |:--- |
| 0x5 | EXTCLKIN1 |
| 0x6 | EXTCLKIN2 |
| 0x7 | reserved |
| 0x8 - 0xF | VCLK |

# 0x5 EXTCLKIN1

# 0x6 EXTCLKIN2 0x7 reserved

# 0x8 - 0xF VCLK

## Table 6-18. DCC2 Counter 0 Clock Sources

| CLOCK SOURCE \[3:0\] | CLOCK NAME |
|:--- |:--- |
| others | oscillator (OSCIN) |
| 0xA | test clock (TCK) | others oscillator (OSCIN) 0xA test clock (TCK)

## Table 6-19. DCC2 Counter 1 Clock Sources

# KEY \[3:0\] **CLOCK SOURCE \[3:0\]** **CLOCK NAME** others - - N2HET2\[0\] 0xA 00x0 - 0x7 Reserved

# 0x8 - 0xF VCLK

*System* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 6.8 **Glitch** ** ** **Filters**

## A glitch filter is present on the following signals.

## Table 6-20. Glitch Filter Timing Specifications

**Pin** **Parameter** **MIN** **MAX** **Unit**

nPORRST t f(nPORRST) ns Filter time nPORRST pin;

pulses less than MIN will be filtered out, pulses greater than MAX will generate a reset (1) nRST t f(nRST) ns Filter time nRST pin;

pulses less than MIN will be filtered out, pulses greater than MAX will generate a reset TEST t f(TEST) ns Filter time TEST pin;

pulses less than MIN will be filtered out, pulses greater than MAX will pass through

(1) The glitch filter design on the nPORRST signal is designed such that no size pulse will reset any part of the microcontroller (flash pump, I/O pins, etc.) without also generating a valid reset signal to the CPU.

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback* **Flash (1.25MB)**

# RAM (192KB) **0x00000000**

# 0x0013FFFF

| 0x08000000 | 0x0802FFFF |
|:--- |:--- |
| CRC | 0xFE000000 |
| Peripherals - Frame 1 | 0xFF000000 |
| SYSTEM Modules | 0xFFFFFFFF |

# CRC **0xFE000000** **Peripherals - Frame 1** **0xFF000000** **SYSTEM Modules** **0xFFFFFFFF**

# 0xF07FFFFF

# RAM - ECC **0x08400000** **0x0842FFFF**

# RESERVED

# RESERVED

# RESERVED **0xF0000000** **0x60000000**

# 0x6FFFFFFF

# CS2

# RESERVED

# CS3

**Flash (1.25MB) (Mirrored Image)** **0x20000000**

# RESERVED

# CS4

# RESERVED

**Peripherals - Frame 2** **0xFC000000** **0xFCFFFFFF**

# 0xFFF80000 **0x80000000**

# 0x87FFFFFF

# CS0

# RESERVED reserved **Async RAM**

# SDRAM 0x64000000 0x68000000 0x6C000000 **Flash Module Bus2 Interface**

# RESERVED

**(Flash ECC, OTP and** **EEPROM Emulation accesses)**

# EMIF (128MB)

# EMIF (32KB \* 3)

# 0x2013FFFF

# TMS570LS1227

| SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 | www.ti.com |
|:--- |:--- |
| 6.9 | Device Memory Map |
| 6.9.1 | Memory Map Diagram | **6.9** **Device Memory Map**

***6.9.1*** ***Memory Map*** *** *** ***Diagram*** The figure below shows the device memory map. **Figure 6-10.** ** ** **Memory Map**

The Flash memory is mirrored to support ECC logic testing. The base address of the mirrored Flash image is 0x2000 0000.

*System* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 6.9.2 ***Memory Map*** *** *** ***Table***

## Table 6-21. Device Memory Map

# FRAME ADDRESS RANGE

**RESPNSE FOR ACCESS TO** **FRAME CHIP** **FRAME** **ACTUAL** **MODULE NAME** **UNIMPLEMENTED LOCATIONS IN** **SELECT** **SIZE** **SIZE** **START** **END** **FRAME**

**Memories** ** ** **tightly** ** ** **coupled to the ARM** ** ** **Cortex-R4F** ** ** **CPU**

# TCM Flash CS0 0x0000\_0000 0x00FF\_FFFF 16MB 1.25MB

# TCM RAM + RAM

CSRAM0 0x0800\_0000 0x0BFF\_FFFF 64MB 192KB ECC Abort

Flash mirror Mirrored Flash 0x2000\_0000 0x20FF\_FFFF 16MB 1.25MB frame **External Memory Accesses**

EMIF Chip Select EMIF select 2 0x6000\_0000 0x63FF\_FFFF 64MB 32KB 2 (asynchronous)

EMIF Chip Select EMIF select 3 0x6400\_0000 0x67FF\_FFFF 64MB 32KB 3 (asynchronous) Access to "Reserved" space will

generate Abort EMIF Chip Select EMIF select 4 0x6800\_0000 0x6BFF\_FFFF 64MB 32KB 4 (asynchronous)

EMIF Chip Select EMIF select 0 0x8000\_0000 0x87FF\_FFFF 128MB 128MB 0 (synchronous) **Flash Module** ** ** **Bus2 Interface**

Customer OTP, 0xF000\_0000 0xF000\_1FFF 8KB 4KB TCM Flash Banks

Customer OTP, 0xF000\_E000 0xF000\_FFFF 8KB 2KB Bank 7

Customer OTP-ECC, TCM 0xF004\_0000 0xF004\_03FF 1KB 512B Flash Banks

Customer OTP-ECC, 0xF004\_1C00 0xF004\_1FFF 1KB 256B Bank 7

TI OTP, TCM 0xF008\_0000 0xF008\_1FFF 8KB 4KB Flash Banks

TI OTP, 0xF008\_E000 0xF008\_FFFF 8KB 2KB Abort Bank 7

TI OTP-ECC, 0xF00C\_0000 0xF00C\_03FF 1KB 512B TCM Flash Banks

# TI OTP-ECC, 0xF00C\_1C00 0xF00C\_1FFF 1KB 256B Bank 7

# Bank 7 - ECC 0xF010\_0000 0xF013\_FFFF 256KB 8KB

# Bank 7 0xF020\_0000 0xF03F\_FFFF 2MB 64KB

Flash Data Space 0xF040\_0000 0xF04F\_FFFF 1MB 160KB ECC

**Ethernet and** ** ** **EMIF** ** ** **slave** ** ** **interfaces**

CPPI Memory Slave (Ethernet 0xFC52\_0000 0xFC52\_1FFF 8KB 8KB Abort RAM)

CPGMAC Slave 0xFCF7\_8000 0xFCF7\_87FF 2KB 2KB No error (Ethernet Slave)

# CPGMACSS

Wrapper 0xFCF7\_8800 0xFCF7\_88FF 256B 256B No error (Ethernet Wrapper)

Ethernet MDIO 0xFCF7\_8900 0xFCF7\_89FF 256B 256B No error Interface

EMIF Registers 0xFCFF\_E800 0xFCFF\_E8FF 256B 256B Abort

**SCR5: Enhanced Timer** ** ** **Peripherals**

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## Table 6-21. Device Memory Map (continued)

# FRAME ADDRESS RANGE

**RESPNSE FOR ACCESS TO** **FRAME CHIP** **FRAME** **ACTUAL** **MODULE NAME** **UNIMPLEMENTED LOCATIONS IN** **SELECT** **SIZE** **SIZE** **START** **END** **FRAME**

| ePWM1 | 0xFCF7\_8C00 | 0xFCF7\_8CFF | 256B | 256B | Abort |
|:--- |:--- |:--- |:--- |:--- |:--- |
| ePWM2 | 0xFCF7\_8D00 | 0xFCF7\_8DFF | 256B | 256B | Abort |
| ePWM3 | 0xFCF7\_8E00 | 0xFCF7\_8EFF | 256B | 256B | Abort |
| ePWM4 | 0xFCF7\_8F00 | 0xFCF7\_8FFF | 256B | 256B | Abort |
| ePWM5 | 0xFCF7\_9000 | 0xFCF7\_90FF | 256B | 256B | Abort |
| ePWM6 | 0xFCF7\_9100 | 0xFCF7\_91FF | 256B | 256B | Abort |
| ePWM7 | 0xFCF7\_9200 | 0xFCF7\_92FF | 256B | 256B | Abort |
| eCAP1 | 0xFCF7\_9300 | 0xFCF7\_93FF | 256B | 256B | Abort |
| eCAP2 | 0xFCF7\_9400 | 0xFCF7\_94FF | 256B | 256B | Abort |
| eCAP3 | 0xFCF7\_9500 | 0xFCF7\_95FF | 256B | 256B | Abort |
| eCAP4 | 0xFCF7\_9600 | 0xFCF7\_96FF | 256B | 256B | Abort |
| eCAP5 | 0xFCF7\_9700 | 0xFCF7\_97FF | 256B | 256B | Abort |
| eCAP6 | 0xFCF7\_9800 | 0xFCF7\_98FF | 256B | 256B | Abort |
| eQEP1 | 0xFCF7\_9900 | 0xFCF7\_99FF | 256B | 256B | Abort |
| eQEP2 | 0xFCF7\_9A00 | 0xFCF7\_9AFF | 256B | 256B | Abort |

ePWM2 0xFCF7\_8D00 0xFCF7\_8DFF 256B 256B Abort

ePWM3 0xFCF7\_8E00 0xFCF7\_8EFF 256B 256B Abort

ePWM4 0xFCF7\_8F00 0xFCF7\_8FFF 256B 256B Abort

ePWM5 0xFCF7\_9000 0xFCF7\_90FF 256B 256B Abort

ePWM6 0xFCF7\_9100 0xFCF7\_91FF 256B 256B Abort

ePWM7 0xFCF7\_9200 0xFCF7\_92FF 256B 256B Abort

eCAP1 0xFCF7\_9300 0xFCF7\_93FF 256B 256B Abort

eCAP2 0xFCF7\_9400 0xFCF7\_94FF 256B 256B Abort

eCAP3 0xFCF7\_9500 0xFCF7\_95FF 256B 256B Abort

eCAP4 0xFCF7\_9600 0xFCF7\_96FF 256B 256B Abort

eCAP5 0xFCF7\_9700 0xFCF7\_97FF 256B 256B Abort

eCAP6 0xFCF7\_9800 0xFCF7\_98FF 256B 256B Abort

eQEP1 0xFCF7\_9900 0xFCF7\_99FF 256B 256B Abort

eQEP2 0xFCF7\_9A00 0xFCF7\_9AFF 256B 256B Abort

**Cyclic Redundancy** ** ** **Checker (CRC)** ** ** **Module** ** ** **Registers**

Accesses above 0x200 generate CRC CRC frame 0xFE00\_0000 0xFEFF\_FFFF 16MB 512B abort. **Peripheral** ** ** **Memories**

MIBSPI5 RAM PCS\[5\] 0xFF0A\_0000 0xFF0B\_FFFF 128KB 2KB Abort for accesses above 2KB

MIBSPI3 RAM PCS\[6\] 0xFF0C\_0000 0xFF0D\_FFFF 128KB 2KB Abort for accesses above 2KB

MIBSPI1 RAM PCS\[7\] 0xFF0E\_0000 0xFF0F\_FFFF 128KB 2KB Abort for accesses above 2KB

Wrap around for accesses to unimplemented address offsets lower DCAN3 RAM PCS\[13\] 0xFF1A\_0000 0xFF1B\_FFFF 128KB 2KB than 0x7FF. Abort generated for accesses beyond offset 0x800.

Wrap around for accesses to unimplemented address offsets lower DCAN2 RAM PCS\[14\] 0xFF1C\_0000 0xFF1D\_FFFF 128KB 2KB than 0x7FF. Abort generated for accesses beyond offset 0x800.

Wrap around for accesses to unimplemented address offsets lower DCAN1 RAM PCS\[15\] 0xFF1E\_0000 0xFF1F\_FFFF 128KB 2KB than 0x7FF. Abort generated for accesses beyond offset 0x800.

Wrap around for accesses to unimplemented address offsets lower MIBADC2 RAM 8KB than 0x1FFF. Abort generated for accesses beyond 0x1FFF.

Look-Up Table for ADC2 wrapper. PCS\[29\] 0xFF3A\_0000 0xFF3B\_FFFF 128KB

Starts at address offset 0x2000 and MIBADC2 Lookends at address offset 0x217F. Wrap 384B Up Table around for accesses between offsets 0x0180 and 0x3FFF. Abort generated for accesses beyond offset 0x4000.

Wrap around for accesses to unimplemented address offsets lower MIBADC1 RAM 8KB than 0x1FFF. Abort generated for accesses beyond 0x1FFF.

Look-Up Table for ADC1 wrapper. PCS\[31\] 0xFF3E\_0000 0xFF3F\_FFFF 128KB

Starts at address offset 0x2000 and MibADC1 Lookends at address offset 0x217F. Wrap 384B Up Table around for accesses between offsets 0x0180 and 0x3FFF. Abort generated for accesses beyond offset 0x4000.

*System* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## Table 6-21. Device Memory Map (continued)

# FRAME ADDRESS RANGE

**RESPNSE FOR ACCESS TO** **FRAME CHIP** **FRAME** **ACTUAL** **MODULE NAME** **UNIMPLEMENTED LOCATIONS IN** **SELECT** **SIZE** **SIZE** **START** **END** **FRAME**

Wrap around for accesses to unimplemented address offsets lower N2HET2 RAM PCS\[34\] 0xFF44\_0000 0xFF45\_FFFF 128KB 16KB than 0x3FFF. Abort generated for accesses beyond 0x3FFF.

Wrap around for accesses to unimplemented address offsets lower N2HET1 RAM PCS\[35\] 0xFF46\_0000 0xFF47\_FFFF 128KB 16KB than 0x3FFF. Abort generated for accesses beyond 0x3FFF.

# HTU2 RAM

PCS\[38\] 0xFF4C\_0000 0xFF4D\_FFFF 128KB 1KB Abort

# HTU1 RAM

PCS\[39\] 0xFF4E\_0000 0xFF4F\_FFFF 128KB 1KB Abort

FlexRay TU RAM PCS\[40\] 0xFF50\_0000 0xFF51\_FFFF 128KB 1KB Abort **Debug Components**

CoreSight Debug Reads return zeros, writes have no CSCS0 0xFFA0\_0000 0xFFA0\_0FFF 4KB 4KB ROM effect

Cortex-R4F Reads return zeros, writes have no CSCS1 0xFFA0\_1000 0xFFA0\_1FFF 4KB 4KB Debug effect

# POM CSCS4 0xFFA0\_4000 0xFFA0\_4FFF 4KB 4KB Abort

**Peripheral** ** ** **Control** ** ** **Registers**

Reads return zeros, writes have no FTU PS\[23\] 0xFFF7\_A000 0xFFF7\_A1FF 512B 512B effect

Reads return zeros, writes have no HTU1 PS\[22\] 0xFFF7\_A400 0xFFF7\_A4FF 256B 256B effect

Reads return zeros, writes have no HTU2 PS\[22\] 0xFFF7\_A500 0xFFF7\_A5FF 256B 256B effect

Reads return zeros, writes have no N2HET1 PS\[17\] 0xFFF7\_B800 0xFFF7\_B8FF 256B 256B effect

Reads return zeros, writes have no N2HET2 PS\[17\] 0xFFF7\_B900 0xFFF7\_B9FF 256B 256B effect

Reads return zeros, writes have no GIO PS\[16\] 0xFFF7\_BC00 0xFFF7\_BDFF 512B 256B effect

Reads return zeros, writes have no MIBADC1 PS\[15\] 0xFFF7\_C000 0xFFF7\_C1FF 512B 512B effect

Reads return zeros, writes have no MIBADC2 PS\[15\] 0xFFF7\_C200 0xFFF7\_C3FF 512B 512B effect

Reads return zeros, writes have no FlexRay PS\[12\]+PS\[13\] 0xFFF7\_C800 0xFFF7\_CFFF 2KB 2KB effect

Reads return zeros, writes have no I2C PS\[10\] 0xFFF7\_D400 0xFFF7\_D4FF 256B 256B effect

Reads return zeros, writes have no DCAN1 PS\[8\] 0xFFF7\_DC00 0xFFF7\_DDFF 512B 512B effect

Reads return zeros, writes have no DCAN2 PS\[8\] 0xFFF7\_DE00 0xFFF7\_DFFF 512B 512B effect

Reads return zeros, writes have no DCAN3 PS\[7\] 0xFFF7\_E000 0xFFF7\_E1FF 512B 512B effect

Reads return zeros, writes have no LIN PS\[6\] 0xFFF7\_E400 0xFFF7\_E4FF 256B 256B effect

Reads return zeros, writes have no SCI PS\[6\] 0xFFF7\_E500 0xFFF7\_E5FF 256B 256B effect

Reads return zeros, writes have no MibSPI1 PS\[2\] 0xFFF7\_F400 0xFFF7\_F5FF 512B 512B effect

Reads return zeros, writes have no SPI2 PS\[2\] 0xFFF7\_F600 0xFFF7\_F7FF 512B 512B effect

Reads return zeros, writes have no MibSPI3 PS\[1\] 0xFFF7\_F800 0xFFF7\_F9FF 512B 512B effect

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## Table 6-21. Device Memory Map (continued)

# FRAME ADDRESS RANGE

**RESPNSE FOR ACCESS TO** **FRAME CHIP** **FRAME** **ACTUAL** **MODULE NAME** **UNIMPLEMENTED LOCATIONS IN** **SELECT** **SIZE** **SIZE** **START** **END** **FRAME**

Reads return zeros, writes have no SPI4 PS\[1\] 0xFFF7\_FA00 0xFFF7\_FBFF 512B 512B effect

Reads return zeros, writes have no MibSPI5 PS\[0\] 0xFFF7\_FC00 0xFFF7\_FDFF 512B 512B effect

**System** ** ** **Modules** ** ** **Control** ** ** **Registers and** ** ** **Memories**

# DMA RAM PPCS0 0xFFF8\_0000 0xFFF8\_0FFF 4KB 4KB Abort

Wrap around for accesses to VIM RAM PPCS2 0xFFF8\_2000 0xFFF8\_2FFF 4KB 1KB unimplemented address offsets between 1KB and 4KB.

Flash Module PPCS7 0xFFF8\_7000 0xFFF8\_7FFF 4KB 4KB Abort

eFuse Controller PPCS12 0xFFF8\_C000 0xFFF8\_CFFF 4KB 4KB Abort

Power Management PPSE0 0xFFFF\_0000 0xFFFF\_01FF 512B 512B Abort Module (PMM)

Reads return zeros, writes have no PCR registers PPS0 0xFFFF\_E000 0xFFFF\_E0FF 256B 256B effect

System Module Reads return zeros, writes have no Frame 2 (see PPS0 0xFFFF\_E100 0xFFFF\_E1FF 256B 256B effect SPNU515 )

Reads return zeros, writes have no PBIST PPS1 0xFFFF\_E400 0xFFFF\_E5FF 512B 512B effect

Generates address error interrupt, if STC PPS1 0xFFFF\_E600 0xFFFF\_E6FF 256B 256B enabled

IOMM Reads return zeros, writes have no Multiplexing PPS2 0xFFFF\_EA00 0xFFFF\_EBFF 512B 512B effect Control Module

Reads return zeros, writes have no DCC1 PPS3 0xFFFF\_EC00 0xFFFF\_ECFF 256B 256B effect

Reads return zeros, writes have no DMA PPS4 0xFFFF\_F000 0xFFFF\_F3FF 1KB 1KB effect

Reads return zeros, writes have no DCC2 PPS5 0xFFFF\_F400 0xFFFF\_F4FF 256B 256B effect

Reads return zeros, writes have no ESM PPS5 0xFFFF\_F500 0xFFFF\_F5FF 256B 256B effect

Reads return zeros, writes have no CCMR4 PPS5 0xFFFF\_F600 0xFFFF\_F6FF 256B 256B effect

Reads return zeros, writes have no RAM ECC even PPS6 0xFFFF\_F800 0xFFFF\_F8FF 256B 256B effect

Reads return zeros, writes have no RAM ECC odd PPS6 0xFFFF\_F900 0xFFFF\_F9FF 256B 256B effect

Reads return zeros, writes have no RTI + DWWD PPS7 0xFFFF\_FC00 0xFFFF\_FCFF 256B 256B effect

Reads return zeros, writes have no VIM Parity PPS7 0xFFFF\_FD00 0xFFFF\_FDFF 256B 256B effect

Reads return zeros, writes have no VIM PPS7 0xFFFF\_FE00 0xFFFF\_FEFF 256B 256B effect

System Module Reads return zeros, writes have no Frame 1 (see PPS7 0xFFFF\_FF00 0xFFFF\_FFFF 256B 256B effect SPNU515 )

*System* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 6.9.3

***Special*** *** *** ***Consideration*** *** *** ***for CPU Access Errors*** *** *** ***Resulting in*** *** *** ***Imprecise*** *** *** ***Aborts***

Any CPU write access to a Normal or Device type memory, which generates a fault, will generate an imprecise abort. The imprecise abort exception is disabled by default and must be enabled for the CPU to handle this exception. The imprecise abort handling is enabled by clearing the "A" bit in the CPU's program status register (CPSR).

## 6.9.4 ***Master/Slave Access Privileges***

The table below lists the access permissions for each bus master on the device. A bus master is a module that can initiate a read or a write transaction on the device.

Each slave module on the main interconnect is listed in the table. A "Yes" indicates that the module listed in the "MASTERS" column can access that slave module.

**Table 6-22.** ** ** **Master** ** ** **/ Slave Access Matrix**

# MASTERS

**ACCESS MODE** **SLAVES** ** ** **ON MAIN SCR**

**Flash Module** **Non-CPU** **CRC** **EMIF, Ethernet** **Peripheral** **Bus2 Interface:** **Accesses to** **Slave** ** ** **Interfaces** **Control** **OTP, ECC,** ** ** **Bank** **Program Flash** **Registers,** ** ** **All** **and** ** ** **CPU Data** **Peripheral** **RAM** **Memories, And**

**All** ** ** **System** **Module** ** ** **Control** **Registers** ** ** **And** **Memories** CPU READ User/Privilege Yes Yes Yes Yes Yes

CPU WRITE User/Privilege **No** Yes Yes Yes Yes DMA User Yes Yes Yes Yes Yes POM User Yes Yes Yes Yes Yes DAP Privilege Yes Yes Yes Yes Yes HTU1 Privilege **No** Yes Yes Yes Yes HTU2 Privilege **No** Yes Yes Yes Yes FTU User **No** Yes Yes Yes Yes EMAC User **No** Yes **No** Yes **No**

## 6.9.5

***Special*** *** *** ***Notes*** *** *** ***on Accesses to Certain Slaves***

Write accesses to the Power Domain Management Module (PMM) control registers are limited to the CPU (master id = 1). The other masters can only read from these registers.

A debugger can also write to the PMM registers. The master-id check is disabled in debug mode.

The device contains dedicated logic to generate a bus error response on any access to a module that is in a power domain that has been turned OFF.

## 6.9.6

***Parameter*** *** *** ***Overlay*** *** *** ***Module*** *** *** ***(POM) Considerations***

- • The POM can map onto up to 8MB of the internal or external memory space. The starting address and the size of the memory overlay are configurable through the POM control registers. Care must be taken to ensure that the overlay is mapped on to available memory. - • ECC must be disabled by software through CP15 in case POM overlay is enabled; otherwise ECC errors will be generated. - • POM overlay must not be enabled when the flash and internal RAM memories are swapped through the MEM SWAP field of the Bus Matrix Module Control Register 1 (BMMCR1).

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

- • When POM is used to overlay the flash on to internal or external RAM, there is a bus contention possibility when another master accesses the TCM flash. This results in a system hang. - - The POM implements a timeout feature to detect this exact scenario. The timeout needs to be enabled whenever POM overlay is enabled. - - The timeout can be enabled by writing 1010 to the Enable TimeOut (ETO) field of the POM Global Control register (POMGLBCTRL, address = 0xFFA04000). - - In case a read request by the POM cannot be completed within 32 HCLK cycles, the timeout (TO) flag is set in the POM Flag register (POMFLG, address = 0xFFA0400C). Also, an abort is generated to the CPU. This can be a prefetch abort for an instruction fetch or a data abort for a data fetch. - - The prefetch- and data-abort handlers must be modified to check if the TO flag in the POM is set. If so, then the application can assume that the timeout is caused by a bus contention between the POM transaction and another master accessing the same memory region. The abort handlers need to clear the TO flag, so that any further aborts are not misinterpreted as having been caused due to a timeout from the POM.

*System* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

| www.ti.com | SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 |
|:--- |:--- |
| 6.10 | Flash Memory |
| 6.10.1 | Flash Memory Configuration |

## 6.10 **Flash** ** ** **Memory**

## 6.10.1

***Flash*** *** *** ***Memory Configuration***

**Flash** ** ** **Bank:** A separate block of logic consisting of 1 to 16 sectors. Each flash bank normally has a customer-OTP and a TI-OTP area. These flash sectors share input/output buffers, data paths, sense amplifiers, and control logic.

**Flash** ** ** **Sector:** A contiguous region of flash memory which must be erased simultaneously due to physical construction constraints.

**Flash** ** ** **Pump:** A charge pump which generates all the voltages required for reading, programming, or erasing the flash banks.

**Flash** ** ** **Module:** Interface circuitry required between the host CPU and the flash banks and pump module.

**Table 6-23. Flash Memory Banks and Sectors**

**Memory Arrays (or** ** ** **Banks)** **Sector** **Segment** **Low** ** ** **Address** **High Address** **No.**

BANK0 (1.25MBytes) (1) 16K Bytes 0x0000\_0000 0x0000\_3FFF

| 16K Bytes | 0x0000\_4000 | 0x0000\_7FFF |
|:--- |:--- |:--- |
| 16K Bytes | 0x0000\_8000 | 0x0000\_BFFF |
| 16K Bytes | 0x0000\_C000 | 0x0000\_FFFF |
| 16K Bytes | 0x0001\_0000 | 0x0001\_3FFF |
| 16K Bytes | 0x0001\_4000 | 0x0001\_7FFF |
| 32K Bytes | 0x0001\_8000 | 0x0001\_FFFF |
| 128K Bytes | 0x0002\_0000 | 0x0003\_FFFF |
| 128K Bytes | 0x0004\_0000 | 0x0005\_FFFF |
| 128K Bytes | 0x0006\_0000 | 0x0007\_FFFF |
| 128K Bytes | 0x0008\_0000 | 0x0009\_FFFF |
| 128K Bytes | 0x000A\_0000 | 0x000B\_FFFF |
| 128K Bytes | 0x000C\_0000 | 0x000D\_FFFF |
| 128K Bytes | 0x000E\_0000 | 0x000F\_FFFF |
| 128K Bytes | 0x0010\_0000 | 0x0011\_FFFF |
| 128K Bytes | 0x0012\_0000 | 0x0013\_FFFF | 16K Bytes 0x0000\_8000 0x0000\_BFFF 16K Bytes 0x0000\_C000 0x0000\_FFFF 16K Bytes 0x0001\_0000 0x0001\_3FFF 16K Bytes 0x0001\_4000 0x0001\_7FFF 32K Bytes 0x0001\_8000 0x0001\_FFFF 128K Bytes 0x0002\_0000 0x0003\_FFFF 128K Bytes 0x0004\_0000 0x0005\_FFFF 128K Bytes 0x0006\_0000 0x0007\_FFFF 128K Bytes 0x0008\_0000 0x0009\_FFFF 128K Bytes 0x000A\_0000 0x000B\_FFFF 128K Bytes 0x000C\_0000 0x000D\_FFFF 128K Bytes 0x000E\_0000 0x000F\_FFFF 128K Bytes 0x0010\_0000 0x0011\_FFFF 128K Bytes 0x0012\_0000 0x0013\_FFFF

BANK7 (64KBytes) for EEPROM emulation (2)(3) 16K Bytes 0xF020\_0000 0xF020\_3FFF

| 16K Bytes | 0xF020\_4000 | 0xF020\_7FFF |
|:--- |:--- |:--- |
| 16K Bytes | 0xF020\_8000 | 0xF020\_BFFF |
| 16K Bytes | 0xF020\_C000 | 0xF020\_FFFF | 16K Bytes 0xF020\_8000 0xF020\_BFFF 16K Bytes 0xF020\_C000 0xF020\_FFFF

(1) The Flash banks are 144-bit wide bank with ECC support. (2) The flash bank7 can be programmed while executing code from flash bank0. (3) Code execution is not allowed from flash bank7.

## 6.10.2

***Main*** *** *** ***Features*** *** *** ***of Flash*** *** *** ***Module***

- • Support for multiple flash banks for program and/or data storage - • Simultaneous read access on a bank while performing program or erase operation on any other bank - • Integrated state machines to automate flash erase and program operations - • Pipelined mode operation to improve instruction access interface bandwidth - • Support for Single Error Correction Double Error Detection (SECDED) block inside Cortex-R4F CPU - - Error address is captured for host system debugging - • Support for a rich set of diagnostic features

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

***6.10.3*** ***ECC Protection*** *** *** ***for Flash*** *** *** ***Accesses***

All accesses to the program flash memory are protected by Single Error Correction Double Error Detection (SECDED) logic embedded inside the CPU. The flash module provides 8 bits of ECC code for 64 bits of instructions or data fetched from the flash memory. The CPU calculates the expected ECC code based on the 64 bits received and compares it with the ECC code returned by the flash module. A single-bit error is corrected and flagged by the CPU, while a multibit error is only flagged. The CPU signals an ECC error through its Event bus. This signaling mechanism is not enabled by default and must be enabled by setting the "X" bit of the Performance Monitor Control Register, c9.

MRC p15,#0,r1,c9,c12,#0;Enabling Event monitor states ORR r1, r1, #0x00000010 MCR p15,#0,r1,c9,c12,#0;Set 4th bit ('X') of PMNC register MRC p15,#0,r1,c9,c12,#0

The application must also explicitly enable the CPU's ECC checking for accesses on the CPU's ATCM and BTCM interfaces. These are connected to the program flash and data RAM respectively. ECC checking for these interfaces can be done by setting the B1TCMPCEN, B0TCMPCEN and ATCMPCEN bits of the System Control coprocessor's Auxiliary Control Register, c1.

MRC p15, #0, r1, c1, c0, #1 ORR r1, r1, #0x0e000000;Enable ECC checking for ATCM and BTCMs DMB MCR p15, #0, r1, c1, c0, #1

***6.10.4*** ***Flash*** *** *** ***Access Speeds***

For information on flash memory access speeds and the relevant wait states required, refer to Section 5.6.

*System* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 6.10.5 ***Program*** *** *** ***Flash***

## Table 6-24. Timing Requirements for Program Flash

**Parameter** **MIN** **NOM** **MAX** **Unit**

t prog(144bit) Wide Word (144bit) programming time µs

t prog(Total) 1.25MByte programming time (1) -40°C to 125°C s 0°C to 60°C, for first 3.3 6.6 s 25 cycles

t erase(bank0) Sector/Bank erase time (2) -40°C to 125°C 0.03 s 0°C to 60°C, for first ms 25 cycles

t wec Write/erase cycles with 15 year Data Retention -40°C to 125°C cycles requirement

(1) This programming time includes overhead of state machine, but does not include data transfer time. The programming time assumes programming 144 bits at a time at the maximum specified operating frequency. (2) During bank erase, the selected sectors are erased simultaneously. The time to erase the bank is specified as equal to the time to erase a sector.

## 6.10.6 ***Data*** *** *** ***Flash***

## Table 6-25. Timing Requirements for Data Flash

**Parameter** **MIN** **NOM** **MAX** **Unit**

t prog(144bit) Wide Word (144bit) programming time µs

t prog(Total) EEPROM Emulation (bank 7) 64KByte -40°C to 125°C ms programming time (1) 0°C to 60°C, for first ms 25 cycles

t erase(bank7) EEPROM Emulation (bank 7) Sector/Bank -40°C to 125°C 0.2 s erase time (2) 0°C to 60°C, for first ms 25 cycles

t wec Write/erase cycles with 15 year Data Retention -40°C to 125°C cycles requirement

(1) This programming time includes overhead of state machine, but does not include data transfer time. The programming time assumes programming 144 bits at a time at the maximum specified operating frequency. (2) During bank erase, the selected sectors are erased simultaneously. The time to erase the bank is specified as equal to the time to erase a sector.

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TCM BUS

# TCM BUS 72 Bit data + ECC 72 Bit data + ECC Upper 32 bits data & 4 ECC bits Lower32 bits data & 4 ECC bits

| 36 Bit | wide | RAM |
|:--- |:--- |:--- |
| 36 Bit | wide | RAM |
| 36 Bit | wide | RAM |
| 36 Bit | wide | RAM |
| 36 Bit | wide | RAM |
| 36 Bit | wide | RAM | 36 Bit wide RAM 36 Bit wide RAM 36 Bit wide RAM 36 Bit wide RAM 36 Bit wide RAM Upper 32 bits data & 4 ECC bits Lower32 bits data & 4 ECC bits

| 36 Bit | wide | RAM |
|:--- |:--- |:--- |
| 36 Bit | wide | RAM |
| 36 Bit | wide | RAM |
| 36 Bit | wide | RAM |
| 36 Bit | wide | RAM |
| 36 Bit | wide | RAM | 36 Bit wide RAM 36 Bit wide RAM 36 Bit wide RAM 36 Bit wide RAM 36 Bit wide RAM **TCRAM** **Interface 1**

## Cortex-R4F

| B0 | TCM |
|:--- |:--- |
| B1 | TCM |
| TCRAM | Interface 2 |

# B1 TCM **TCRAM** **Interface 2**

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

**6.11** **Tightly Coupled** ** ** **RAM** ** ** **Interface** ** ** **Module**

Figure 6-11 illustrates the connection of the Tightly Coupled RAM (TCRAM) to the Cortex-R4F CPU.

**Figure 6-11.** ** ** **TCRAM Block Diagram** ***6.11.1*** ***Features***

The features of the Tightly Coupled RAM (TCRAM) Module are: - • Acts as slave to the BTCM interface of the Cortex-R4F CPU - • Supports the internal ECC scheme of the CPU by providing 64-bit data and 8-bit ECC code - • Monitors CPU Event Bus and generates single or multibit error interrupts - • Stores addresses for single and multibit errors - • Supports RAM trace module - • Provides CPU address bus integrity checking by supporting parity checking on the address bus - • Performs redundant address decoding for the RAM bank chip select and ECC select generation logic - • Provides enhanced safety for the RAM addressing by implementing two 36-bit-wide byte-interleaved RAM banks and generating independent RAM access control signals to the two banks - • Supports auto-initialization of the RAM banks along with the ECC bits

***6.11.2*** ***TCRAM*** *** *** ***ECC Support***

The TCRAM interface passes on the ECC code for each data read by the Cortex-R4F CPU from the RAM. It also stores the contents of the CPU ECC port in the ECC RAM when the CPU does a write to the RAM. The TCRAM interface monitors the CPU event bus and provides registers for indicating single/multibit errors and also for identifying the address that caused the single or multibit error. The event signaling and the ECC checking for the RAM accesses must be enabled inside the CPU.

For more information see TMS570LS12x/11x Technical Reference Manual ( SPNU515 ).

**6.12** **Parity** ** ** **Protection for Accesses to Peripheral** ** ** **RAMs**

Accesses to some peripheral RAMs are protected by odd/even parity checking. During a read access the parity is calculated based on the data read from the peripheral RAM and compared with the good parity value stored in the parity RAM for that peripheral. If any word fails the parity check, the module generates a parity error signal that is mapped to the Error Signaling Module. The module also captures the peripheral RAM address that caused the parity error.

The parity protection for peripheral RAMs is not enabled by default and must be enabled by the application. Each individual peripheral contains control registers to enable the parity protection for accesses to its RAM.

*System* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

**NOTE** The CPU read access gets the actual data from the peripheral. The application can choose to generate an interrupt whenever a peripheral RAM parity error is detected.

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

| SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 | www.ti.com |
|:--- |:--- |
| 6.13 | On-Chip SRAM Initialization and Testing |
| 6.13.1 | On-Chip SRAM Self-Test Using PBIST |
| 6.13.1.1 | Features |

## 6.13

**On-Chip** ** ** **SRAM Initialization** ** ** **and** ** ** **Testing**

## 6.13.1

***On-Chip*** *** *** ***SRAM Self-Test*** *** *** ***Using PBIST***

## 6.13.1.1 **Features**

- • Extensive instruction set to support various memory test algorithms - • ROM-based algorithms allow application to run TI production-level memory tests - • Independent testing of all on-chip SRAM

## 6.13.1.2 **PBIST RAM Groups**

## Table 6-26. PBIST RAM Grouping **Test Pattern (Algorithm)**

**March 13N** **(1)** **March 13N** **(1)** **triple** ** ** **read** **triple** ** ** **read** **two port** **single** ** ** **port** **Memory** **RAM** ** ** **Group** **Test Clock** **MEM** ** ** **Type** **slow read** **fast read** **(cycles)** **(cycles)**

# ALGO MASK

**ALGO** ** ** **MASK** **ALGO** ** ** **MASK** **ALGO** ** ** **MASK** **0x1** **0x2** **0x4** **0x8**

| PBIST\_ROM | ROM CLK | ROM |
|:--- |:--- |:--- |
| STC\_ROM | ROM CLK | ROM |
| DCAN1 | VCLK | Dual Port |
| DCAN2 | VCLK | Dual Port |
| DCAN3 | VCLK | Dual Port |
| ESRAM1(2) | HCLK | Single Port |
| MIBSPI1 | VCLK | Dual Port |
| MIBSPI3 | VCLK | Dual Port |
| MIBSPI5 | VCLK | Dual Port |
| VIM | VCLK | Dual Port |
| MIBADC1 | VCLK | Dual Port |
| DMA | HCLK | Dual Port |
| N2HET1 | VCLK | Dual Port |
| HTU1 | VCLK | Dual Port |

# STC\_ROM ROM CLK ROM DCAN1 VCLK Dual Port DCAN2 VCLK Dual Port DCAN3 VCLK Dual Port ESRAM1 (2) HCLK Single Port MIBSPI1 VCLK Dual Port MIBSPI3 VCLK Dual Port MIBSPI5 VCLK Dual Port VIM VCLK Dual Port MIBADC1 VCLK Dual Port DMA HCLK Dual Port N2HET1 VCLK Dual Port HTU1 VCLK Dual Port

# FLEXRAY I/O

buffer, Transient 16 (3) VCLK Dual Port Buffer, FTU Control Packet FLEXRAY 17 (4) VCLK Single Port Message RAM

| MIBADC2 | VCLK | Dual Port |
|:--- |:--- |:--- |
| N2HET2 | VCLK | Dual Port |
| HTU2 | VCLK | Dual Port |
| ESRAM5(5) | HCLK | Single Port |
| ESRAM6(6) | HCLK | Single Port |
| Dual Port | ETHERNET | VCLK3 | N2HET2 VCLK Dual Port HTU2 VCLK Dual Port ESRAM5 (5) HCLK Single Port ESRAM6 (6) HCLK Single Port

# Dual Port ETHERNET VCLK3 Single Port

(1) There are several memory testing algorithms stored in the PBIST ROM. However, TI recommends the March13N algorithm for application testing. (2) ESRAM1: Address 0x08000000 - 0x0800FFFF (3) This RAM group includes the FTU control packet RAM, the FlexRay controller's I/O buffer, and the transient buffer. (4) This RAM group inclludes the FlexRay controller's message RAM (5) ESRAM5: Address 0x08010000 - 0x0801FFFF (6) ESRAM6: Address 0x08020000 - 0x0802FFFF

*System* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

The PBIST ROM clock frequency is limited to 100MHz, if 100MHz \< HCLK \<= HCLKmax, or HCLK, if HCLK <= 100MHz.

The PBIST ROM clock is divided down from HCLK. The divider is selected by programming the ROM\_DIV field of the Memory Self-Test Global Control Register (MSTGCR) at address 0xFFFFFF58.

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## 6.13.2

***On-Chip*** *** *** ***SRAM Auto*** *** *** ***Initialization***

## This microcontroller allows some of the on-chip memories to be initialized through the Memory Hardware

Initialization mechanism in the System module. This hardware mechanism allows an application to program the memory arrays with error detection capability to a known state based on their error detection scheme (odd/even parity or ECC).

## The MINITGCR register enables the memory initialization sequence, and the MSINENA register selects the memories that are to be initialized.

## For more information on these registers see TMS570LS12x/11x Technical Reference Manual ( SPNU515 ).

## The mapping of the different on-chip memories to the specific bits of the MSINENA registers is shown in Table 6-27.

## Table 6-27. Memory Initialization

# ADDRESS RANGE

**CONNECTING** ** ** **MODULE** **MSINENA REGISTER** ** ** **BIT #** **BASE** ** ** **ADDRESS** **ENDING** ** ** **ADDRESS**

| RAM (PD#1) | 0x08000000 | 0x0800FFFF | 0(1) |
|:--- |:--- |:--- | ---: |
| RAM (RAM\_PD#1) | 0x08010000 | 0x0801FFFF | 0(1) |
| RAM (RAM\_PD#2) | 0x08020000 | 0x0802FFFF | 0(1) |
| MIBSPI5 RAM | 0xFF0A0000 | 0xFF0BFFFF | 12(2) |
| MIBSPI3 RAM | 0xFF0C0000 | 0xFF0DFFFF | 11(2) |
| MIBSPI1 RAM | 0xFF0E0000 | 0xFF0FFFFF | 7(2) |

# RAM (RAM\_PD#1) 0x08010000 0x0801FFFF 0 (1)

# RAM (RAM\_PD#2) 0x08020000 0x0802FFFF 0 (1)

# MIBSPI5 RAM 0xFF0A0000 0xFF0BFFFF 12 (2)

# MIBSPI3 RAM 0xFF0C0000 0xFF0DFFFF 11 (2)

# MIBSPI1 RAM 0xFF0E0000 0xFF0FFFFF 7 (2)

| DCAN3 RAM | 0xFF1A0000 | 0xFF1BFFFF |
|:--- |:--- |:--- |
| DCAN2 RAM | 0xFF1C0000 | 0xFF1DFFFF |
| DCAN1 RAM | 0xFF1E0000 | 0xFF1FFFFF |
| FlexRay RAM | RAM is not CPU-Addressable | n/a(3) |
| MIBADC2 RAM | 0xFF3A0000 | 0xFF3BFFFF |
| MIBADC1 RAM | 0xFF3E0000 | 0xFF3FFFFF |
| N2HET2 RAM | 0xFF440000 | 0xFF45FFFF |
| N2HET1 RAM | 0xFF460000 | 0xFF47FFFF |
| HTU2 RAM | 0xFF4C0000 | 0xFF4DFFFF |
| HTU1 RAM | 0xFF4E0000 | 0xFF4FFFFF |
| DMA RAM | 0xFFF80000 | 0xFFF80FFF |
| VIM RAM | 0xFFF82000 | 0xFFF82FFF |
| FlexRay TU (FTU) RAM | 0xFF500000 | 0xFF51FFFF |

# DCAN2 RAM 0xFF1C0000 0xFF1DFFFF

# DCAN1 RAM 0xFF1E0000 0xFF1FFFFF

FlexRay RAM RAM is not CPU-Addressable n/a (3)

# MIBADC2 RAM 0xFF3A0000 0xFF3BFFFF

# MIBADC1 RAM 0xFF3E0000 0xFF3FFFFF

# N2HET2 RAM 0xFF440000 0xFF45FFFF

# N2HET1 RAM 0xFF460000 0xFF47FFFF

# HTU2 RAM 0xFF4C0000 0xFF4DFFFF

# HTU1 RAM 0xFF4E0000 0xFF4FFFFF

# DMA RAM 0xFFF80000 0xFFF80FFF

# VIM RAM 0xFFF82000 0xFFF82FFF

# FlexRay TU (FTU) RAM 0xFF500000 0xFF51FFFF

Ethernet RAM (CPPI Memory 0xFC520000 0xFC521FFF n/a Slave)

(1) The TCM RAM interface module has separate control bits to select the RAM power domain that is to be auto-initialized. (2) The MibSPIx modules perform an initialization of the transmit and receive RAMs as soon as the module is released from its local reset.. This is independent of whether the application chooses to initialize the MibSPIx RAMs using the system module auto-initialization method. The MibSPIx module must be first brought out of its local reset in order to use the system module auto-initialization method. (3) Reserved only. The FlexRay RAM has its own initialization mechanism.

*System* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# EMIF\_nCS\[3:2\]

# EMIF\_BA\[1:0\]

# EMIF\_ADDR\[12:0\]

# EMIF\_nOE

# EMIF\_DATA\[15:0\]

# EMIF\_nWE

# EMIF\_nDQM\[1:0\]

# TMS570LS1227

| www.ti.com | SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 |
|:--- |:--- |
| 6.14 | External Memory Interface (EMIF) |
| 6.14.1 | Features |

**6.14** **External Memory Interface** ** ** **(EMIF)** ***6.14.1*** ***Features***

The EMIF includes many features to enhance the ease and flexibility of connecting to external asynchronous memories or SDRAM devices. The EMIF features includes support for: - • 3 addressable chip select for asynchronous memories of up to 32KB each - • 1 addressable chip select space for SDRAMs up to 128MB - • 8 or 16-bit data bus width - • Programmable cycle timings such as setup, strobe, and hold times as well as turnaround time - • Select strobe mode - • Extended Wait mode - • Data bus parking

***6.14.2*** ***Electrical and*** *** *** ***Timing Specifications*** **6.14.2.1** **Asynchronous RAM**

**Figure 6-12. Asynchronous Memory Read Timing**

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# EMIF\_nCS\[3:2\]

# EMIF\_BA\[1:0\]

# EMIF\_ADDR\[12:0\]

# EMIF\_nWE

# EMIF\_DATA\[15:0\]

# EMIF\_nOE

# EMIF\_nDQM\[1:0\]

# EMIF\_nCS\[3:2\] Asserted Deasserted

# EMIF\_BA\[1:0\]

# EMIF\_ADDR\[12:0\]

# EMIF\_DATA\[15:0\]

# EMIF\_nOE

# EMIF\_WAIT SETUP Extended Due to EMIF\_WAIT STROBE HOLD

# STROBE

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## Figure 6-13. EMIFnWAIT Read Timing Requirements

## Figure 6-14. Asynchronous Memory Write Timing

*System* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# EMIF\_nCS\[3:2\] Asserted

# EMIF\_BA\[1:0\]

# EMIF\_ADDR\[12:0\]

# EMIF\_DATA\[15:0\]

# EMIF\_nWE

# EMIF\_WAIT SETUP Extended Due to EMIF\_WAIT Deasserted

# STROBE STROBE HOLD

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## Figure 6-15. EMIFnWAIT Write Timing Requirements

**Table 6-28. EMIF Asynchronous Memory Timing Requirements** **(1)** **NO.** **Value** **Unit**

# MIN **NOM** **MAX** **Reads and** ** ** **Writes** E EMIF clock period ns

t w(EM\_WAIT) Pulse duration, EMIF\_nWAIT 2E ns assertion and deassertion **Reads**

t su(EMDV-EMOEH) Setup time, EMIF\_DATA\[15:0\] ns valid before EMIFnOE high

t h(EMOEH-EMDIV) Hold time, EMIF\_DATA\[15:0\] ns valid after EMIF\_nOE high

t su(EMOEL-EMWAIT) Setup Time, EMIF\_nWAIT 4E+9 ns asserted before end of Strobe Phase (2) **Writes**

t su(EMWEL-EMWAIT) Setup Time, EMIF\_nWAIT 4E+14 ns asserted before end of Strobe Phase (2)

(1) E = EMIF\_CLK period in ns. (2) Setup before end of STROBE phase (if no extended wait states are inserted) by which EMIFnWAIT must be asserted to add extended wait states. Figure 6-13 and Figure 6-15 describe EMIF transactions that include extended wait states inserted during the STROBE phase. However, cycles inserted as part of this extended wait period should not be counted; the 4E requirement is to the start of where the HOLD phase would begin if there were no extended wait cycles.

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## Table 6-29. EMIF Asynchronous Memory Switching Characteristics (1)(2)(3)

# NO **PARAMETER** **Value** **UNIT**

# MIN **NOM** **MAX** **Reads and** ** ** **Writes**

t d(TURNAROUND) Turnaround time (TA)\*E - 4 (TA)\*E (TA)\*E + 3 ns **Reads**

t c(EMRCYCLE) EMIF read cycle time (EW = 0) (RS+RST+RH)\* (RS+RST+RH)\* (RS+RST+RH)\* ns E -3 E E + 3

# EMIF read cycle time (EW = 1)

(RS+RST+RH+( (RS+RST+RH+( (RS+RST+RH+( ns EWC\*16))\*E -3 EWC\*16))\*E EWC\*16))\*E +

t su(EMCEL-EMOEL) Output setup time, (RS)\*E-6 (RS)\*E (RS)\*E+3 ns EMIF\_nCS\[4:2\] low to EMIF_nOE low (SS = 0)

Output setup time, +3 ns EMIF\_nCS\[4:2\] low to EMIF_nOE low (SS = 1)

t h(EMOEH-EMCEH) Output hold time, EMIF\_nOE (RH)\*E -3 (RH)\*E (RH)\*E + 5 ns high to EMIF\_nCS\[4:2\] high (SS $$ = 0) $$

Output hold time, EMIF\_nOE +5 ns high to EMIF\_nCS\[4:2\] high (SS $$ = 1) $$

t su(EMBAV-EMOEL) Output setup time, (RS)\*E-6 (RS)\*E (RS)\*E+3 ns EMIF\_BA\[1:0\] valid to EMIF\_nOE low

t h(EMOEH-EMBAIV) Output hold time, EMIF\_nOE (RH)\*E-3 (RH)\*E (RH)\*E+5 ns high to EMIF\_BA\[1:0\] invalid

t su(EMAV-EMOEL) Output setup time, (RS)\*E-6 (RS)\*E (RS)\*E+3 ns EMIF\_ADDR\[12:0\] valid to EMIFnOE low

t h(EMOEH-EMAIV) Output hold time, EMIF\_nOE (RH)\*E-3 (RH)\*E (RH)\*E+5 ns high to EMIF\_ADDR\[12:0\] invalid

t w(EMOEL) EMIF\_nOE active low width (EW (RST)\*E-3 (RST)\*E (RST)\*E+3 ns $$ = 0) $$

EMIF\_nOE active low width (EW (RST+(EWC\*16 (RST+(EWC\*16 (RST+(EWC\*16 ns $$ = 1) $$ )) \*E-3 ))\*E )) \*E+3

t d(EMWAITH-EMOEH) Delay time from EMIF\_nWAIT 3E+9 4E 4E+20 ns deasserted to EMIF\_nOE high

t su(EMDQMV-EMOEL) Output setup time, (RS)\*E-6 (RS)\*E (RS)\*E+3 ns EMIF\_nDQM\[1:0\] valid to EMIF\_nOE low

t h(EMOEH-EMDQMIV) Output hold time, EMIF\_nOE (RH)\*E-3 (RH)\*E (RH)\*E+5 ns high to EMIF\_nDQM\[1:0\] invalid **Writes**

t c(EMWCYCLE) EMIF write cycle time (EW = 0) (WS+WST+WH (WS+WST+WH (WS+WST+WH ns )\* E-3 )\*E )\* E+3

# EMIF write cycle time (EW = 1)

(WS+WST+WH (WS+WST+WH (WS+WST+WH ns +( EWC\*16))\*E +(E WC\*16))\*E +( EWC\*16))\*E + 3

(1) TA = Turnaround, RS = Read setup, RST = Read strobe, RH = Read hold, WS = Write setup, WST = Write strobe, WH = Write hold, MEWC = Maximum external wait cycles. These parameters are programmed through the Asynchronous Bank and Asynchronous Wait Cycle Configuration Registers. These support the following ranges of values: TA\[4-1\], RS\[16-1\], RST\[64-1\], RH\[8-1\], WS\[16-1\], WST\[64-1\], WH\[8-1\], and MEWC\[1-256\]. See the TMS570LS12x/11x Technical Reference Manual ( SPNU515 ) for more information. (2) E = EMIF\_CLK period in ns. (3) EWC = external wait cycles determined by EMIF\_nWAIT input signal. EWC supports the following range of values. EWC\[256-1\]. Note that the maximum wait time before timeout is specified by bit field MEWC in the Asynchronous Wait Cycle Configuration Register. See the TMS570LS12x/11x Technical Reference Manual ( SPNU515 ) for more information.

*System* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## Table 6-29. EMIF Asynchronous Memory Switching Characteristics (1)(2)(3) (continued)

# NO **PARAMETER** **Value** **UNIT**

# MIN **NOM** **MAX**

t su(EMCEL-EMWEL) Output setup time, (WS)\*E -3 (WS)\*E (WS)\*E + 3 ns EMIF\_nCS\[4:2\] low to EMIF_nWE low (SS = 0)

Output setup time, +3 ns EMIF\_nCS\[4:2\] low to EMIF_nWE low (SS = 1)

t h(EMWEH-EMCEH) Output hold time, EMIF\_nWE (WH)\*E-3 (WH)\*E (WH)\*E+3 ns high to EMIF\_nCS\[4:2\] high (SS $$ = 0) $$

Output hold time, EMIF\_nWE +3 ns high to EMIF_CS[4:2] high (SS = 1)

t su(EMDQMV-EMWEL) Output setup time, (WS)\*E-3 (WS)\*E (WS)\*E+3 ns EMIF\_BA\[1:0\] valid to EMIF\_nWE low

t h(EMWEH-EMDQMIV) Output hold time, EMIF\_nWE (WH)\*E-3 (WH)\*E (WH)\*E+3 ns high to EMIF\_BA\[1:0\] invalid

t su(EMBAV-EMWEL) Output setup time, (WS)\*E-3 (WS)\*E (WS)\*E+3 ns EMIF\_BA\[1:0\] valid to EMIF\_nWE low

t h(EMWEH-EMBAIV) Output hold time, EMIF\_nWE (WH)\*E-3 (WH)\*E (WH)\*E+3 ns high to EMIF\_BA\[1:0\] invalid

t su(EMAV-EMWEL) Output setup time, (WS)\*E-3 (WS)\*E (WS)\*E+3 ns EMIF\_ADDR\[12:0\] valid to EMIF\_nWE low

t h(EMWEH-EMAIV) Output hold time, EMIF\_nWE (WH)\*E-3 (WH)\*E (WH)\*E+3 ns high to EMIF\_ADDR\[12:0\] invalid

t w(EMWEL) EMIF\_nWE active low width (WST)\*E-3 (WST)\*E (WST)\*E+3 ns $$ (EW = 0) $$

EMIF\_nWE active low width (WST+(EWC\*1 (WST+(EWC\*1 (WST+(EWC\*1 ns $$ (EW = 1) $$ 6)) \*E-3 6))\*E 6)) \*E+3

t d(EMWAITH-EMWEH) Delay time from EMIF\_nWAIT 3E+11 4E 4E+24 ns deasserted to EMIF\_nWE high

t su(EMDV-EMWEL) Output setup time, (WS)\*E-3 (WS)\*E (WS)\*E+3 ns EMIF\_DATA\[15:0\] valid to EMIF\_nWE low

t h(EMWEH-EMDIV) Output hold time, EMIF\_nWE (WH)\*E-3 (WH)\*E (WH)\*E+3 ns high to EMIF\_DATA\[15:0\] invalid

t su(EMDQMV-EMWEL) Output setup time, (WH)\*E-3 (WH)\*E (WH)\*E+3 ns EMIF\_nDQM\[1:0\] valid to EMIF\_nWE low

t h(EMWEH-EMDQMIV) Output hold time, EMIF\_nWE (WH)\*E-3 (WH)\*E (WH)\*E+3 ns high to EMIF\_nDQM\[1:0\] invalid

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# EMIF\_CLK

# EMIF\_BA\[1:0\]

# EMIF\_ADDR\[12:0\]

# EMIF\_DATA\[15:0\] 2 EM\_CLK Delay

# BASIC SDRAM

# READ OPERATION

# EMIF\_nCS\[0\]

# EMIF\_nDQM\[1:0\]

# EMIF\_nRAS

# EMIF\_nCAS

# EMIF\_nWE

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## 6.14.2.2 **Synchronous Timing**

## Figure 6-16. Basic SDRAM Read Operation

*System* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# EMIF\_CLK

# EMIF\_BA\[1:0\]

# EMIF\_ADDR\[12:0\]

# EMIF\_DATA\[15:0\]

# BASIC SDRAM WRITE OPERATION

# EMIF\_CS\[0\]

# EMIF\_DQM\[1:0\]

# EMIF\_nRAS

# EMIF\_nCAS

# EMIF\_nWE

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## Figure 6-17. Basic SDRAM Write Operation

## Table 6-30. EMIF Synchronous Memory Timing Requirements

| NO. | Parameter | MIN | MAX | Unit |
|:--- |:--- |:--- |:--- |:--- |
| tsu(EMIFDV-EM\_CLKH) | Input setup time, read data valid on | ns | EMIF\_DATA\[15:0\] before EMIF\_CLK | rising |
| th(CLKH-DIV) | Input hold time, read data valid on | ns | EMIF\_DATA\[15:0\] after EMIF\_CLK | rising |

t su(EMIFDV-EM\_CLKH) Input setup time, read data valid on ns EMIF\_DATA\[15:0\] before EMIF\_CLK rising

t h(CLKH-DIV) Input hold time, read data valid on ns EMIF\_DATA\[15:0\] after EMIF\_CLK rising

## Table 6-31. EMIF Synchronous Memory Switching Characteristics

**NO.** **Parameter** **MIN** **MAX** **Unit** t c(CLK) Cycle time, EMIF clock EMIF\_CLK ns

| tw(CLK) | Pulse width, EMIF clock EMIF\_CLK | ns | high or low |
|:--- |:--- |:--- |:--- |
| td(CLKH-CSV) | Delay time, EMIF\_CLK rising to | ns | EMIF\_nCS\[0\] valid |
| toh(CLKH-CSIV) | Output hold time, EMIF\_CLK rising to | ns | EMIF\_nCS\[0\] invalid |
| td(CLKH-DQMV) | Delay time, EMIF\_CLK rising to | ns | EMIF\_nDQM\[1:0\] valid |
| toh(CLKH-DQMIV) | Output hold time, EMIF\_CLK rising to | ns | EMIF\_nDQM\[1:0\] invalid |

t d(CLKH-CSV) Delay time, EMIF\_CLK rising to ns EMIF\_nCS\[0\] valid

t oh(CLKH-CSIV) Output hold time, EMIF\_CLK rising to ns EMIF\_nCS\[0\] invalid

t d(CLKH-DQMV) Delay time, EMIF\_CLK rising to ns EMIF\_nDQM\[1:0\] valid

t oh(CLKH-DQMIV) Output hold time, EMIF\_CLK rising to ns EMIF\_nDQM\[1:0\] invalid

t d(CLKH-AV) Delay time, EMIF\_CLK rising to ns EMIF\_ADDR\[12:0\] and EMIFBA\[1:0\] valid

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## Table 6-31. EMIF Synchronous Memory Switching Characteristics (continued)

**NO.** **Parameter** **MIN** **MAX** **Unit**

t oh(CLKH-AIV) Output hold time, EMIF\_CLK rising to ns EMIF\_ADDR\[12:0\] and EMIF\_BA\[1:0\] invalid

| td(CLKH-DV) | Delay time, EMIF\_CLK rising to | ns | EMIF\_DATA\[15:0\] valid |
|:--- |:--- |:--- |:--- |
| toh(CLKH-DIV) | Output hold time, EMIF\_CLK rising to | ns | EMIF\_DATA\[15:0\] invalid |
| td(CLKH-RASV) | Delay time, EMIF\_CLK rising to | ns | EMIF\_nRAS valid |
| toh(CLKH-RASIV) | Output hold time, EMIF\_CLK rising to | ns | EMIF\_nRAS invalid |
| td(CLKH-CASV) | Delay time, EMIF\_CLK rising to | ns | EMIF\_nCAS valid |
| toh(CLKH-CASIV) | Output hold time, EMIF\_CLK rising to | ns | EMIF\_nCAS invalid |
| td(CLKH-WEV) | Delay time, EMIF\_CLK rising to | ns | EMIF\_nWE valid |
| toh(CLKH-WEIV) | Output hold time, EMIF\_CLK rising to | ns | EMIF\_nWE invalid |
| tdis(CLKH-DHZ) | Delay time, EMIF\_CLK rising to | ns | EMIF\_DATA\[15:0\] tri-stated |
| tena(CLKH-DLZ) | Output hold time, EMIF\_CLK rising to | ns | EMIF\_DATA\[15:0\] driving |

t oh(CLKH-DIV) Output hold time, EMIF\_CLK rising to ns EMIF\_DATA\[15:0\] invalid

t d(CLKH-RASV) Delay time, EMIF\_CLK rising to ns EMIF\_nRAS valid

t oh(CLKH-RASIV) Output hold time, EMIF\_CLK rising to ns EMIF\_nRAS invalid

t d(CLKH-CASV) Delay time, EMIF\_CLK rising to ns EMIF\_nCAS valid

t oh(CLKH-CASIV) Output hold time, EMIF\_CLK rising to ns EMIF\_nCAS invalid

t d(CLKH-WEV) Delay time, EMIF\_CLK rising to ns EMIF\_nWE valid

t oh(CLKH-WEIV) Output hold time, EMIF\_CLK rising to ns EMIF\_nWE invalid

t dis(CLKH-DHZ) Delay time, EMIF\_CLK rising to ns EMIF\_DATA\[15:0\] tri-stated

t ena(CLKH-DLZ) Output hold time, EMIF\_CLK rising to ns EMIF\_DATA\[15:0\] driving

*System* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 6.15

**Vectored** ** ** **Interrupt** ** ** **Manager**

## The vectored interrupt manager (VIM) provides hardware assistance for prioritizing and controlling the

many interrupt sources present on this device. Interrupts are caused by events outside of the normal flow of program execution. Normally, these events require a timely response from the central processing unit (CPU); therefore, when an interrupt occurs, the CPU switches execution from the normal program flow to an interrupt service routine (ISR).

## 6.15.1 ***VIM*** *** *** ***Features***

## The VIM module has the following features

- • Supports 128 interrupt channels. - - Provides programmable priority and enable for interrupt request lines. - • Provides a direct hardware dispatch mechanism for fastest IRQ dispatch. - • Provides two software dispatch mechanisms when the CPU VIC port is not used. - - Index interrupt - - Register vectored interrupt - • Parity protected vector interrupt table against soft errors.

## 6.15.2

***Interrupt*** *** *** ***Request Assignments***

## Table 6-32. Interrupt Request Assignments

**Modules** **Interrupt** ** ** **Sources** **Default** ** ** **VIM** ** ** **Interrupt** **Channel**

| ESM | ESM High level interrupt (NMI) |
|:--- |:--- |
| Reserved | Reserved |
| RTI | RTI compare interrupt 0 |
| RTI | RTI compare interrupt 1 |
| RTI | RTI compare interrupt 2 |
| RTI | RTI compare interrupt 3 |
| RTI | RTI overflow interrupt 0 |
| RTI | RTI overflow interrupt 1 |
| RTI | RTI timebase interrupt |
| GIO | GIO interrupt A |
| N2HET1 | N2HET1 level 0 interrupt |
| HTU1 | HTU1 level 0 interrupt |
| MIBSPI1 | MIBSPI1 level 0 interrupt |
| LIN | LIN level 0 interrupt |
| MIBADC1 | MIBADC1 event group interrupt |
| MIBADC1 | MIBADC1 sw group 1 interrupt |
| DCAN1 | DCAN1 level 0 interrupt |
| SPI2 | SPI2 level 0 interrupt |
| FlexRay | FlexRay level 0 interrupt |
| CRC | CRC Interrupt |
| ESM | ESM Low level interrupt |
| SYSTEM | Software interrupt (SSI) |
| CPU | PMU Interrupt |
| GIO | GIO interrupt B |
| N2HET1 | N2HET1 level 1 interrupt |
| HTU1 | HTU1 level 1 interrupt |
| MIBSPI1 | MIBSPI1 level 1 interrupt | Reserved Reserved RTI RTI compare interrupt 0 RTI RTI compare interrupt 1 RTI RTI compare interrupt 2 RTI RTI compare interrupt 3 RTI RTI overflow interrupt 0 RTI RTI overflow interrupt 1 RTI RTI timebase interrupt GIO GIO interrupt A N2HET1 N2HET1 level 0 interrupt HTU1 HTU1 level 0 interrupt MIBSPI1 MIBSPI1 level 0 interrupt LIN LIN level 0 interrupt MIBADC1 MIBADC1 event group interrupt MIBADC1 MIBADC1 sw group 1 interrupt DCAN1 DCAN1 level 0 interrupt SPI2 SPI2 level 0 interrupt FlexRay FlexRay level 0 interrupt CRC CRC Interrupt ESM ESM Low level interrupt SYSTEM Software interrupt (SSI) CPU PMU Interrupt GIO GIO interrupt B N2HET1 N2HET1 level 1 interrupt HTU1 HTU1 level 1 interrupt MIBSPI1 MIBSPI1 level 1 interrupt

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## Table 6-32. Interrupt Request Assignments (continued)

**Modules** **Interrupt** ** ** **Sources** **Default** ** ** **VIM** ** ** **Interrupt** **Channel**

| LIN | LIN level 1 interrupt |
|:--- |:--- |
| MIBADC1 | MIBADC1 sw group 2 interrupt |
| DCAN1 | DCAN1 level 1 interrupt |
| SPI2 | SPI2 level 1 interrupt |
| MIBADC1 | MIBADC1 magnitude compare interrupt |
| FlexRay | FlexRay level 1 interrupt |
| DMA | FTCA interrupt |
| DMA | LFSA interrupt |
| DCAN2 | DCAN2 level 0 interrupt |
| Reserved | Reserved |
| MIBSPI3 | MIBSPI3 level 0 interrupt |
| MIBSPI3 | MIBSPI3 level 1 interrupt |
| DMA | HBCA interrupt |
| DMA | BTCA interrupt |
| EMIF | AEMIFINT3 |
| DCAN2 | DCAN2 level 1 interrupt |
| Reserved | Reserved |
| DCAN1 | DCAN1 IF3 interrupt |
| DCAN3 | DCAN3 level 0 interrupt |
| DCAN2 | DCAN2 IF3 interrupt |
| FPU | FPU interrupt |
| FlexRay TU (FTU) | FTU Transfer Status interrupt |
| SPI4 | SPI4 level 0 interrupt |
| MIBADC2 | MibADC2 event group interrupt |
| MIBADC2 | MibADC2 sw group1 interrupt |
| FlexRay | FlexRay T0C interrupt |
| MIBSPI5 | MIBSPI5 level 0 interrupt |
| SPI4 | SPI4 level 1 interrupt |
| DCAN3 | DCAN3 level 1 interrupt |
| MIBSPI5 | MIBSPI5 level 1 interrupt |
| MIBADC2 | MibADC2 sw group2 interrupt |
| FlexRay TU (FTU) | FTU Error interrupt |
| MIBADC2 | MibADC2 magnitude compare interrupt |
| DCAN3 | DCAN3 IF3 interrupt |
| FMC | FSM\_DONE interrupt |
| FlexRay | FlexRay T1C interrupt |
| N2HET2 | N2HET2 level 0 interrupt |
| SCI | SCI level 0 interrupt |
| HTU2 | HTU2 level 0 interrupt |
| I2C | I2C level 0 interrupt | MIBADC1 MIBADC1 sw group 2 interrupt DCAN1 DCAN1 level 1 interrupt SPI2 SPI2 level 1 interrupt MIBADC1 MIBADC1 magnitude compare interrupt FlexRay FlexRay level 1 interrupt DMA FTCA interrupt DMA LFSA interrupt DCAN2 DCAN2 level 0 interrupt Reserved Reserved MIBSPI3 MIBSPI3 level 0 interrupt MIBSPI3 MIBSPI3 level 1 interrupt DMA HBCA interrupt DMA BTCA interrupt

# EMIF AEMIFINT3 DCAN2 DCAN2 level 1 interrupt Reserved Reserved DCAN1 DCAN1 IF3 interrupt DCAN3 DCAN3 level 0 interrupt DCAN2 DCAN2 IF3 interrupt FPU FPU interrupt

FlexRay TU (FTU) FTU Transfer Status interrupt SPI4 SPI4 level 0 interrupt MIBADC2 MibADC2 event group interrupt MIBADC2 MibADC2 sw group1 interrupt FlexRay FlexRay T0C interrupt MIBSPI5 MIBSPI5 level 0 interrupt SPI4 SPI4 level 1 interrupt DCAN3 DCAN3 level 1 interrupt MIBSPI5 MIBSPI5 level 1 interrupt MIBADC2 MibADC2 sw group2 interrupt FlexRay TU (FTU) FTU Error interrupt MIBADC2 MibADC2 magnitude compare interrupt DCAN3 DCAN3 IF3 interrupt FMC FSM\_DONE interrupt FlexRay FlexRay T1C interrupt N2HET2 N2HET2 level 0 interrupt SCI SCI level 0 interrupt HTU2 HTU2 level 0 interrupt I2C I2C level 0 interrupt Reserved Reserved 67-72

| N2HET2 | N2HET2 level 1 interrupt |
|:--- |:--- |
| SCI | SCI level 1 interrupt |
| HTU2 | HTU2 level 1 interrupt |
| Ethernet | C0\_MISC\_PULSE |
| Ethernet | C0\_TX\_PULSE |
| Ethernet | C0\_THRESH\_PULSE | SCI SCI level 1 interrupt HTU2 HTU2 level 1 interrupt Ethernet C0\_MISC\_PULSE Ethernet C0\_TX\_PULSE Ethernet C0\_THRESH\_PULSE

*System* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

**Table 6-32. Interrupt Request Assignments (continued)**

**Modules** **Interrupt** ** ** **Sources** **Default** ** ** **VIM** ** ** **Interrupt** **Channel**

| Ethernet | C0\_RX\_PULSE |
|:--- |:--- |
| HWAG1 | HWA\_INT\_REQ\_H |
| HWAG2 | HWA\_INT\_REQ\_H |
| DCC1 | DCC done interrupt |
| DCC2 | DCC2 done interrupt |
| Reserved | Reserved |
| PBIST Controller | PBIST Done Interrupt |

# HWAG1 HWA\_INT\_REQ\_H

# HWAG2 HWA\_INT\_REQ\_H DCC1 DCC done interrupt DCC2 DCC2 done interrupt Reserved Reserved PBIST Controller PBIST Done Interrupt Reserved Reserved 86-87

| HWAG1 | HWA\_INT\_REQ\_L |
|:--- |:--- |
| HWAG2 | HWA\_INT\_REQ\_L |
| ePWM1INTn | ePWM1 Interrupt |
| ePWM1TZINTn | ePWM1 Trip Zone Interrupt |
| ePWM2INTn | ePWM2 Interrupt |
| ePWM2TZINTn | ePWM2 Trip Zone Interrupt |
| ePWM3INTn | ePWM3 Interrupt |
| ePWM3TZINTn | ePWM3 Trip Zone Interrupt |
| ePWM4INTn | ePWM4 Interrupt |
| ePWM4TZINTn | ePWM4 Trip Zone Interrupt |
| ePWM5INTn | ePWM5 Interrupt |
| ePWM5TZINTn | ePWM5 Trip Zone Interrupt |
| ePWM6INTn | ePWM6 Interrupt |
| ePWM6TZINTn | ePWM6 Trip Zone Interrupt |
| ePWM7INTn | ePWM7 Interrupt |
| ePWM7TZINTn | ePWM7 Trip Zone Interrupt |
| eCAP1INTn | eCAP1 Interrupt |
| eCAP2INTn | eCAP2 Interrupt |
| eCAP3INTn | eCAP3 Interrupt |
| eCAP4INTn | eCAP4 Interrupt |
| eCAP5INTn | eCAP5 Interrupt |
| eCAP6INTn | eCAP6 Interrupt |
| eQEP1INTn | eQEP1 Interrupt |
| eQEP2INTn | eQEP2 Interrupt |

# HWAG2 HWA\_INT\_REQ\_L ePWM1INTn ePWM1 Interrupt ePWM1TZINTn ePWM1 Trip Zone Interrupt ePWM2INTn ePWM2 Interrupt ePWM2TZINTn ePWM2 Trip Zone Interrupt ePWM3INTn ePWM3 Interrupt ePWM3TZINTn ePWM3 Trip Zone Interrupt ePWM4INTn ePWM4 Interrupt ePWM4TZINTn ePWM4 Trip Zone Interrupt ePWM5INTn ePWM5 Interrupt ePWM5TZINTn ePWM5 Trip Zone Interrupt ePWM6INTn ePWM6 Interrupt ePWM6TZINTn ePWM6 Trip Zone Interrupt ePWM7INTn ePWM7 Interrupt ePWM7TZINTn ePWM7 Trip Zone Interrupt eCAP1INTn eCAP1 Interrupt eCAP2INTn eCAP2 Interrupt eCAP3INTn eCAP3 Interrupt eCAP4INTn eCAP4 Interrupt eCAP5INTn eCAP5 Interrupt eCAP6INTn eCAP6 Interrupt eQEP1INTn eQEP1 Interrupt eQEP2INTn eQEP2 Interrupt Reserved Reserved 112-127

**NOTE** Address location 0x00000000 in the VIM RAM is reserved for the phantom interrupt ISR entry; therefore only request channels 0..126 can be used and are offset by 1 address in the VIM RAM.

**NOTE** The EMIF\_nWAIT signal has a pull-up on it. The EMIF module generates a "Wait Rise" interrupt whenever it detects a rising edge on the EMIF\_nWAIT signal. This interrupt condition is indicated as soon as the device is powered up. This can be ignored if the EMIF\_nWAIT signal is not used in the application. If the EMIF\_nWAIT signal is actually used in the application, then the external slave memory must always drive the EMIF\_nWAIT signal such that an interrupt is not caused due to the default pull-up on this signal.

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

| NOTE | The lower-order interrupt channels are higher priority channels than the higher-order interrupt | channels. |
|:--- |:--- |:--- |
| NOTE | The application can change the mapping of interrupt sources to the interrupt channels | through the interrupt channel control registers (CHANCTRLx) inside the VIM module. |
| System Information and Electrical Specifications | Copyright © 2012-2015, Texas Instruments Incorporated | Submit Documentation Feedback |

**NOTE** The application can change the mapping of interrupt sources to the interrupt channels through the interrupt channel control registers (CHANCTRLx) inside the VIM module.

*System* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **6.16** **DMA** ** ** **Controller**

The DMA controller is used to transfer data between two locations in the memory map in the background of CPU operations. Typically, the DMA is used to: - • Transfer blocks of data between external and internal data memories - • Restructure portions of internal data memory - • Continually service a peripheral ***6.16.1*** ***DMA*** *** *** ***Features***

- • CPU independent data transfer - • One 64-bit master port that interfaces to the Memory System. - • FIFO buffer(4 entries deep and each 64bit wide) - • Channel control information is stored in RAM protected by parity - • 16 channels with individual enable - • Channel chaining capability - • 32 peripheral DMA requests - • Hardware and Software DMA requests - • 8, 16, 32 or 64-bit transactions supported - • Multiple addressing modes for source/destination (fixed, increment, offset) - • Auto-initiation - • Power-management mode - • Memory Protection with four configurable memory regions

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## 6.16.2

***Default*** *** *** ***DMA*** *** *** ***Request Map***

## The DMA module on this microcontroller has 16 channels and up to 32 hardware DMA requests. The

module contains DREQASIx registers which are used to map the DMA requests to the DMA channels. By default, channel 0 is mapped to request 0, channel 1 to request 1, and so on.

## Some DMA requests have multiple sources, as shown in Table 6-33. The application must ensure that

only one of these DMA request sources is enabled at any time.

## Table 6-33. DMA Request Line Connection

| Modules | DMA Request Sources | DMA Request |
|:--- |:--- |:--- |
| MIBSPI1 | MIBSPI1\[1\](1) | DMAREQ\[0\] |
| MIBSPI1 | MIBSPI1\[0\](2) | DMAREQ\[1\] |
| SPI2 | SPI2 receive | DMAREQ\[2\] |
| SPI2 | SPI2 transmit | DMAREQ\[3\] |
| MIBSPI1 / MIBSPI3 / DCAN2 | MIBSPI1\[2\] / MIBSPI3\[2\] / DCAN2 IF3 | DMAREQ\[4\] |
| MIBSPI1 / MIBSPI3 / DCAN2 | MIBSPI1\[3\] / MIBSPI3\[3\] / DCAN2 IF2 | DMAREQ\[5\] |
| DCAN1 / MIBSPI5 | DCAN1 IF2 / MIBSPI5\[2\] | DMAREQ\[6\] |
| MIBADC1 / MIBSPI5 | MIBADC1 event / MIBSPI5\[3\] | DMAREQ\[7\] |
| MIBSPI1 / MIBSPI3 / DCAN1 | MIBSPI1\[4\] / MIBSPI3\[4\] / DCAN1 IF1 | DMAREQ\[8\] |
| MIBSPI1 / MIBSPI3 / DCAN2 | MIBSPI1\[5\] / MIBSPI3\[5\] / DCAN2 IF1 | DMAREQ\[9\] |
| MIBADC1 / I2C / MIBSPI5 | MIBADC1 G1 / I2C receive / MIBSPI5\[4\] | DMAREQ\[10\] |
| MIBADC1 / I2C / MIBSPI5 | MIBADC1 G2 / I2C transmit / MIBSPI5\[5\] | DMAREQ\[11\] |
| RTI / MIBSPI1 / MIBSPI3 | RTI DMAREQ0 / MIBSPI1\[6\] / MIBSPI3\[6\] | DMAREQ\[12\] |
| RTI / MIBSPI1 / MIBSPI3 | RTI DMAREQ1 / MIBSPI1\[7\] / MIBSPI3\[7\] | DMAREQ\[13\] |
| MIBSPI3 / MibADC2 / MIBSPI5 | MIBSPI3\[1\](1) / MibADC2 event / MIBSPI5\[6\] | DMAREQ\[14\] |
| MIBSPI3 / MIBSPI5 | MIBSPI3\[0\](2) / MIBSPI5\[7\] | DMAREQ\[15\] |
| MIBSPI1 / MIBSPI3 / DCAN1 / MibADC2 | MIBSPI1\[8\] / MIBSPI3\[8\] / DCAN1 IF3 / MibADC2 G1 | DMAREQ\[16\] |
| MIBSPI1 / MIBSPI3 / DCAN3 / MibADC2 | MIBSPI1\[9\] / MIBSPI3\[9\] / DCAN3 IF1 / MibADC2 G2 | DMAREQ\[17\] |
| RTI / MIBSPI5 | RTI DMAREQ2 / MIBSPI5\[8\] | DMAREQ\[18\] |
| RTI / MIBSPI5 | RTI DMAREQ3 / MIBSPI5\[9\] | DMAREQ\[19\] |

# MIBSPI1 MIBSPI1\[1\] (1) DMAREQ\[0\]

# MIBSPI1 MIBSPI1\[0\] (2) DMAREQ\[1\] SPI2 SPI2 receive DMAREQ\[2\] SPI2 SPI2 transmit DMAREQ\[3\]

# MIBSPI1 / MIBSPI3 / DCAN2

MIBSPI1\[2\] / MIBSPI3\[2\] / DCAN2 IF3 DMAREQ\[4\]

# MIBSPI1 / MIBSPI3 / DCAN2

MIBSPI1\[3\] / MIBSPI3\[3\] / DCAN2 IF2 DMAREQ\[5\]

# DCAN1 / MIBSPI5 DCAN1 IF2 / MIBSPI5\[2\] DMAREQ\[6\]

# MIBADC1 / MIBSPI5 MIBADC1 event / MIBSPI5\[3\] DMAREQ\[7\]

# MIBSPI1 / MIBSPI3 / DCAN1

MIBSPI1\[4\] / MIBSPI3\[4\] / DCAN1 IF1 DMAREQ\[8\]

# MIBSPI1 / MIBSPI3 / DCAN2

MIBSPI1\[5\] / MIBSPI3\[5\] / DCAN2 IF1 DMAREQ\[9\]

# MIBADC1 / I2C / MIBSPI5

MIBADC1 G1 / I2C receive / MIBSPI5\[4\] DMAREQ\[10\]

# MIBADC1 / I2C / MIBSPI5

MIBADC1 G2 / I2C transmit / MIBSPI5\[5\] DMAREQ\[11\]

# RTI / MIBSPI1 / MIBSPI3

RTI DMAREQ0 / MIBSPI1\[6\] / MIBSPI3\[6\] DMAREQ\[12\]

# RTI / MIBSPI1 / MIBSPI3

RTI DMAREQ1 / MIBSPI1\[7\] / MIBSPI3\[7\] DMAREQ\[13\]

# MIBSPI3 / MibADC2 / MIBSPI5

MIBSPI3\[1\] (1) / MibADC2 event / MIBSPI5\[6\] DMAREQ\[14\]

# MIBSPI3 / MIBSPI5 MIBSPI3\[0\] (2) / MIBSPI5\[7\] DMAREQ\[15\]

# MIBSPI1 / MIBSPI3 / DCAN1 / MibADC2

MIBSPI1\[8\] / MIBSPI3\[8\] / DCAN1 IF3 / MibADC2 G1 DMAREQ\[16\]

# MIBSPI1 / MIBSPI3 / DCAN3 / MibADC2

MIBSPI1\[9\] / MIBSPI3\[9\] / DCAN3 IF1 / MibADC2 G2 DMAREQ\[17\]

# RTI / MIBSPI5 RTI DMAREQ2 / MIBSPI5\[8\] DMAREQ\[18\]

# RTI / MIBSPI5 RTI DMAREQ3 / MIBSPI5\[9\] DMAREQ\[19\]

# N2HET1 / N2HET2 / DCAN3

N2HET1 DMAREQ\[4\] / N2HET2 DMAREQ\[4\] / DCAN3 DMAREQ\[20\] IF2

# N2HET1 / N2HET2 / DCAN3

N2HET1 DMAREQ\[5\] / N2HET2 DMAREQ\[5\] / DCAN3 DMAREQ\[21\] IF3

# MIBSPI1 / MIBSPI3 / MIBSPI5

MIBSPI1\[10\] / MIBSPI3\[10\] / MIBSPI5\[10\] DMAREQ\[22\]

# MIBSPI1 / MIBSPI3 / MIBSPI5

MIBSPI1\[11\] / MIBSPI3\[11\] / MIBSPI5\[11\] DMAREQ\[23\]

# N2HET1 / N2HET2 / SPI4 / MIBSPI5

N2HET1 DMAREQ\[6\] / N2HET2 DMAREQ\[6\] / SPI4 DMAREQ\[24\] receive / MIBSPI5\[12\]

# N2HET1 / N2HET2 / SPI4 / MIBSPI5

N2HET1 DMAREQ\[7\] / N2HET2 DMAREQ\[7\] / SPI4 DMAREQ\[25\] transmit / MIBSPI5\[13\]

| CRC / MIBSPI1 / MIBSPI3 | CRC DMAREQ\[0\] / MIBSPI1\[12\] / MIBSPI3\[12\] | DMAREQ\[26\] |
|:--- |:--- |:--- |
| CRC / MIBSPI1 / MIBSPI3 | CRC DMAREQ\[1\] / MIBSPI1\[13\] / MIBSPI3\[13\] | DMAREQ\[27\] |
| LIN / MIBSPI5 | LIN receive / MIBSPI5\[14\] | DMAREQ\[28\] |
| LIN / MIBSPI5 | LIN transmit / MIBSPI5\[15\] | DMAREQ\[29\] |

# CRC / MIBSPI1 / MIBSPI3

CRC DMAREQ\[1\] / MIBSPI1\[13\] / MIBSPI3\[13\] DMAREQ\[27\]

# LIN / MIBSPI5 LIN receive / MIBSPI5\[14\] DMAREQ\[28\]

# LIN / MIBSPI5 LIN transmit / MIBSPI5\[15\] DMAREQ\[29\]

# MIBSPI1 / MIBSPI3 / SCI / MIBSPI5

MIBSPI1\[14\] / MIBSPI3\[14\] / SCI receive / DMAREQ\[30\] MIBSPI5\[1\] (1)

# MIBSPI1 / MIBSPI3 / SCI / MIBSPI5

MIBSPI1\[15\] / MIBSPI3\[15\] / SCI transmit / DMAREQ\[31\] MIBSPI5\[0\] (2)

(1) Receive DMA when configured in standard SPI mode (2) Transmit DMA when configured in standard SPI mode

*System* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback* 31          0 31           0

# RTICLK 31           0 31                          0 31                         0 External control CAP event source 0 CAP event source 1 $$ = $$ Up counter Capture up counter Compare up counter Free running counter Capture

# RTIFRCx free running counter RTICAFRCx

# OVLINTx RTICPUCx

# RTIUCx

# RTICAUCx To Compare Unit NTU0 NTU1 NTU2 NTU3

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

**6.17** **Real Time Interrupt** ** ** **Module**

The real-time interrupt (RTI) module provides timer functionality for operating systems and for benchmarking code. The RTI module can incorporate several counters that define the timebases needed for scheduling an operating system.

The timers also allow you to benchmark certain areas of code by reading the values of the counters at the beginning and the end of the desired code range and calculating the difference between the values.

In addition the RTI provides a mechanism to synchronize the operating system to the FlexRay communication cycle. Clock supervision can detect issues on the FlexRay bus with an automatic switch to an internally generated timebase. ***6.17.1*** ***Features***

The RTI module has the following features: - • Two independent 64 bit counter blocks - • Four configurable compares for generating operating system ticks or DMA requests. Each event can be driven by either counter block 0 or counter block 1. - • One counter block usable for application synchronization to FlexRay network including clock supervision - • Fast enabling/disabling of events - • Two time-stamp (capture) functions for system or peripheral interrupts, one for each counter block ***6.17.2*** ***Block Diagrams***

Figure 6-18 shows a high-level block diagram for one of the two 64-bit counter blocks inside the RTI module. Both the counter blocks are identical except the Network Time Unit (NTUx) inputs are only available as time base inputs for the counter block 0.

**Figure 6-18.** ** ** **Counter Block Diagram**

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback* 31          0 Compare control

# INTy

| DMAREQy | Compare |
|:--- |:--- |
| Update | compare |
| From counter | block 0 |
| From counter | block 1 | Update compare From counter block 0 From counter block 1

# RTIUDCPy

# RTICOMPy 31          0 $$ = $$ +

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

**Figure 6-19.** ** ** **Compare Block Diagram**

***6.17.3*** ***Clock Source*** *** *** ***Options***

The RTI module uses the RTI1CLK clock domain for generating the RTI time bases.

The application can select the clock source for the RTI1CLK by configuring the RCLKSRC register in the System module at address 0xFFFFFF50. The default source for RTI1CLK is VCLK.

For more information on clock sources refer to Table 6-8 and Table 6-13.

***6.17.4*** ***Network Time Synchronization Inputs***

The RTI module supports 4 Network Time Unit (NTU) inputs that signal internal system events, and which can be used to synchronize the time base used by the RTI module. On this device, these NTU inputs are connected as shown below.

**Table 6-34. Network Time Synchronization Inputs** **NTU Input** **Source** FlexRay Macrotick FlexRay Start of Cycle PLL2 Clock output EXTCLKIN1 clock input

*System* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 6.18 **Error Signaling Module**

The Error Signaling Module (ESM) manages the various error conditions on the microcontroller. The error condition is handled based on a fixed severity level assigned to it. Any severe error condition can be configured to drive a low level on a dedicated device terminal called nERROR. This can be used as an indicator to an external monitor circuit to put the system into a safe state.

## 6.18.1 ***Features***

The features of the Error Signaling Module are: - • 128 interrupt/error channels are supported, divided into 3 different groups - - 64 channels with maskable interrupt and configurable error pin behavior - - 32 error channels with non-maskable interrupt and predefined error pin behavior - - 32 channels with predefined error pin behavior only - • Error pin to signal severe device failure - • Configurable timebase for error signal - • Error forcing capability

## 6.18.2 ***ESM*** *** *** ***Channel Assignments***

The Error Signaling Module (ESM) integrates all the device error conditions and groups them in the order of severity. Group1 is used for errors of the lowest severity while Group3 is used for errors of the highest severity. The device response to each error is determined by the severity group it is connected to. Table 6-36 shows the channel assignment for each group. **Table 6-35.** ** ** **ESM Groups**

| ERROR GROUP | INTERRUPT CHARACTERISTICS | INFLUENCE ON ERROR PIN |
|:--- |:--- |:--- |
| Group1 | maskable, low or high priority | configurable |
| Group2 | non-maskable, high priority | fixed |
| Group3 | no interrupt generated | fixed |

Group1 maskable, low or high priority configurable Group2 non-maskable, high priority fixed Group3 no interrupt generated fixed **Table 6-36. ESM Channel Assignments** **ERROR Condition** **Group** **Channels**

| Reserved | Group1 |
|:--- |:--- |
| MibADC2 - RAM parity error | Group1 |
| DMA - MPU configuration violation | Group1 |
| DMA - control packet RAM parity error | Group1 |
| Reserved | Group1 |
| DMA - error on DMA read access, imprecise error | Group1 | MibADC2 - RAM parity error Group1 DMA - MPU configuration violation Group1 DMA - control packet RAM parity error Group1 Reserved Group1

DMA - error on DMA read access, imprecise error Group1

FMC - correctable ECC error: bus1 and bus2 interfaces Group1 (does not include accesses to Bank 7)

| N2HET1 - RAM parity error | Group1 |
|:--- |:--- |
| HTU1/HTU2 - dual-control packet RAM parity error | Group1 |
| HTU1/HTU2 - MPU configuration violation | Group1 |
| PLL1 - Slip | Group1 |
| Clock Monitor - oscillator fail | Group1 |
| Flexray - message RAM parity error | Group1 |
| DMA - error on DMA write access, imprecise error | Group1 |
| Flexray TU (FTU) - control packet RAM parity error | Group1 |
| VIM RAM - parity error | Group1 |
| FTU - MPU configuration violation | Group1 |
| MibSPI1 - RAM parity error | Group1 |
| MibSPI3 - RAM parity error | Group1 |

HTU1/HTU2 - dual-control packet RAM parity error Group1

HTU1/HTU2 - MPU configuration violation Group1 PLL1 - Slip Group1 Clock Monitor - oscillator fail Group1 Flexray - message RAM parity error Group1

DMA - error on DMA write access, imprecise error Group1

Flexray TU (FTU) - control packet RAM parity error Group1 VIM RAM - parity error Group1 FTU - MPU configuration violation Group1 MibSPI1 - RAM parity error Group1 MibSPI3 - RAM parity error Group1

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## Table 6-36. ESM Channel Assignments (continued) **ERROR Condition** **Group** **Channels**

| MibADC1 - RAM parity error | Group1 |
|:--- |:--- |
| Reserved | Group1 |
| DCAN1 - RAM parity error | Group1 |
| DCAN3 - RAM parity error | Group1 |
| DCAN2 - RAM parity error | Group1 |
| MibSPI5 - RAM parity error | Group1 |
| Reserved | Group1 |
| RAM even bank (B0TCM) - correctable ECC error | Group1 |
| CPU - self-test failed | Group1 |
| RAM odd bank (B1TCM) - correctable ECC error | Group1 |
| Reserved | Group1 |
| DCC1 - error | Group1 |
| CCM-R4 - self-test failed | Group1 |
| Reserved | Group1 |
| Reserved | Group1 |
| N2HET2 - RAM parity error | Group1 |
| FMC - correctable ECC error (Bank 7 access) | Group1 |
| FMC - uncorrectable ECC error (Bank 7 access) | Group1 | Reserved Group1 DCAN1 - RAM parity error Group1 DCAN3 - RAM parity error Group1 DCAN2 - RAM parity error Group1 MibSPI5 - RAM parity error Group1 Reserved Group1

RAM even bank (B0TCM) - correctable ECC error Group1 CPU - self-test failed Group1

RAM odd bank (B1TCM) - correctable ECC error Group1 Reserved Group1 DCC1 - error Group1 CCM-R4 - self-test failed Group1 Reserved Group1 Reserved Group1 N2HET2 - RAM parity error Group1

FMC - correctable ECC error (Bank 7 access) Group1

FMC - uncorrectable ECC error (Bank 7 access) Group1

IOMM - Access to unimplemented location in IOMM frame, or write access Group1 detected in unprivileged mode Power domain controller compare error Group1

Power domain controller self-test error Group1

eFuse Controller Error - this error signal is generated when any bit in the eFuse Group1 controller error status register is set. The application can choose to generate an interrupt whenever this bit is set to service any eFuse controller error conditions.

eFuse Controller - Self Test Error. This error signal is generated only when a self Group1 test on the eFuse controller generates an error condition. When an ECC self test

error is detected, group 1 channel 40 error signal will also be set.

| PLL#2 - Slip | Group1 |
|:--- |:--- |
| Ethernet Controller bus master access error | Group1 |
| Reserved | Group1 |
| Reserved | Group1 |
| Reserved | Group1 |
| Reserved | Group1 |
| Reserved | Group1 |
| Reserved | Group1 |
| Reserved | Group1 |
| Reserved | Group1 |
| Reserved | Group1 |
| Reserved | Group1 |
| Reserved | Group1 |
| Reserved | Group1 |
| Reserved | Group1 |
| Reserved | Group1 |
| Reserved | Group1 |
| Reserved | Group1 |
| Reserved | Group1 |
| Reserved | Group1 |
| DCC2 - error | Group1 |

Ethernet Controller bus master access error Group1 Reserved Group1 Reserved Group1 Reserved Group1 Reserved Group1 Reserved Group1 Reserved Group1 Reserved Group1 Reserved Group1 Reserved Group1 Reserved Group1 Reserved Group1 Reserved Group1 Reserved Group1 Reserved Group1 Reserved Group1 Reserved Group1 Reserved Group1 Reserved Group1 DCC2 - error Group1

*System* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## Table 6-36. ESM Channel Assignments (continued) **ERROR Condition** **Group** **Channels**

| Reserved | Group1 |
|:--- |:--- |
| Reserved | Group2 |
| Reserved | Group2 |
| CCMR4 - dual-CPU lock-step error | Group2 |
| Reserved | Group2 |
| FMC - uncorrectable address parity error on accesses to main flash | Group2 |
| Reserved | Group2 |
| RAM even bank (B0TCM) - uncorrectable redundant address decode error | Group2 |
| Reserved | Group2 |
| RAM odd bank (B1TCM) - uncorrectable redundant address decode error | Group2 |
| Reserved | Group2 |
| RAM even bank (B0TCM) - address bus parity error | Group2 |
| Reserved | Group2 |
| RAM odd bank (B1TCM) - address bus parity error | Group2 |
| Reserved | Group2 |
| Reserved | Group2 |
| Reserved | Group2 |
| TCM - ECC live lock detect | Group2 |
| Reserved | Group2 |
| Reserved | Group2 |
| Reserved | Group2 |
| Reserved | Group2 |
| Reserved | Group2 |
| Reserved | Group2 |
| Reserved | Group2 |
| Windowed Watchdog (WWD) violation | Group2 |
| Reserved | Group2 |
| Reserved | Group2 |
| Reserved | Group2 |
| Reserved | Group2 |
| Reserved | Group2 |
| Reserved | Group2 |
| Reserved | Group2 |
| Reserved | Group3 |
| eFuse Farm - autoload error | Group3 |
| Reserved | Group3 |
| RAM even bank (B0TCM) - ECC uncorrectable error | Group3 |
| Reserved | Group3 |
| RAM odd bank (B1TCM) - ECC uncorrectable error | Group3 |
| Reserved | Group3 | Reserved Group2 Reserved Group2 CCMR4 - dual-CPU lock-step error Group2 Reserved Group2

FMC - uncorrectable address parity error on accesses to main flash Group2 Reserved Group2

RAM even bank (B0TCM) - uncorrectable redundant address decode error Group2 Reserved Group2

RAM odd bank (B1TCM) - uncorrectable redundant address decode error Group2 Reserved Group2

RAM even bank (B0TCM) - address bus parity error Group2 Reserved Group2

RAM odd bank (B1TCM) - address bus parity error Group2 Reserved Group2 Reserved Group2 Reserved Group2 TCM - ECC live lock detect Group2 Reserved Group2 Reserved Group2 Reserved Group2 Reserved Group2 Reserved Group2 Reserved Group2 Reserved Group2 Windowed Watchdog (WWD) violation Group2 Reserved Group2 Reserved Group2 Reserved Group2 Reserved Group2 Reserved Group2 Reserved Group2 Reserved Group2 Reserved Group3 eFuse Farm - autoload error Group3 Reserved Group3

RAM even bank (B0TCM) - ECC uncorrectable error Group3 Reserved Group3

RAM odd bank (B1TCM) - ECC uncorrectable error Group3 Reserved Group3

FMC - uncorrectable ECC error: ATCM and Flash OTP interfaces Group3 (does not include address parity error and errors on accesses to Bank 7 data memory)

| Reserved | Group3 |
|:--- |:--- |
| Reserved | Group3 |
| Reserved | Group3 |
| Reserved | Group3 |
| Reserved | Group3 | Reserved Group3 Reserved Group3 Reserved Group3 Reserved Group3

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## Table 6-36. ESM Channel Assignments (continued) **ERROR Condition** **Group** **Channels**

| Reserved | Group3 |
|:--- |:--- |
| Reserved | Group3 |
| Reserved | Group3 |
| Reserved | Group3 |
| Reserved | Group3 |
| Reserved | Group3 |
| Reserved | Group3 |
| Reserved | Group3 |
| Reserved | Group3 |
| Reserved | Group3 |
| Reserved | Group3 |
| Reserved | Group3 |
| Reserved | Group3 |
| Reserved | Group3 |
| Reserved | Group3 |
| Reserved | Group3 |
| Reserved | Group3 |
| Reserved | Group3 |
| Reserved | Group3 | Reserved Group3 Reserved Group3 Reserved Group3 Reserved Group3 Reserved Group3 Reserved Group3 Reserved Group3 Reserved Group3 Reserved Group3 Reserved Group3 Reserved Group3 Reserved Group3 Reserved Group3 Reserved Group3 Reserved Group3 Reserved Group3 Reserved Group3 Reserved Group3

*System* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 6.19

**Reset /** ** ** **Abort /** ** ** **Error Sources**

## Table 6-37. Reset/Abort/Error Sources

# ESM HOOKUP

**ERROR SOURCE** **SYSTEM** ** ** **MODE** **ERROR RESPONSE** **group.channel**

# CPU TRANSACTIONS

| Precise write error (NCNB/Strongly Ordered) | User/Privilege | Precise Abort (CPU) | n/a |
|:--- |:--- |:--- |:--- |
| Precise read error (NCB/Device or Normal) | User/Privilege | Precise Abort (CPU) | n/a |
| Imprecise write error (NCB/Device or Normal) | User/Privilege | Imprecise Abort (CPU) | n/a |

Precise read error (NCB/Device or Normal) User/Privilege Precise Abort (CPU) n/a

Imprecise write error (NCB/Device or Normal) User/Privilege Imprecise Abort (CPU) n/a

Undefined Instruction Trap Illegal instruction User/Privilege n/a (CPU) (1)

MPU access violation User/Privilege Abort (CPU) n/a

# SRAM

B0 TCM (even) ECC single error (correctable) User/Privilege ESM 1.26

Abort (CPU), ESM => B0 TCM (even) ECC double error (non-correctable) User/Privilege 3.3 nERROR

B0 TCM (even) uncorrectable error (for example, redundant User/Privilege ESM => NMI => nERROR 2.6 address decode)

B0 TCM (even) address bus parity error User/Privilege ESM => NMI => nERROR 2.10

B1 TCM (odd) ECC single error (correctable) User/Privilege ESM 1.28

Abort (CPU), ESM => B1 TCM (odd) ECC double error (non-correctable) User/Privilege 3.5 nERROR

B1 TCM (odd) uncorrectable error (for example, redundant User/Privilege ESM => NMI => nERROR 2.8 address decode)

B1 TCM (odd) address bus parity error User/Privilege ESM => NMI => nERROR 2.12

# FLASH WITH CPU BASED ECC

FMC correctable error - Bus1 and Bus2 interfaces (does not User/Privilege ESM 1.6 include accesses to Bank 7)

FMC uncorrectable error - Bus1 and Bus2 accesses Abort (CPU), ESM => User/Privilege 3.7 (does not include address parity error) nERROR

FMC uncorrectable error - address parity error on Bus1 User/Privilege ESM => NMI => nERROR 2.4 accesses

FMC correctable error - Accesses to Bank 7 User/Privilege ESM 1.35

FMC uncorrectable error - Accesses to Bank 7 User/Privilege ESM 1.36

# DMA TRANSACTIONS

External imprecise error on read (Illegal transaction with ok User/Privilege ESM 1.5 response)

External imprecise error on write (Illegal transaction with ok User/Privilege ESM 1.13 response)

Memory access permission violation User/Privilege ESM 1.2 Memory parity error User/Privilege ESM 1.3

**High-End Timer** ** ** **Transfer Unit** ** ** **1** ** ** **(HTU1)**

| NCNB (Strongly Ordered) transaction with slave error response | User/Privilege | Interrupt =\> VIM | n/a |
|:--- |:--- |:--- |:--- |
| External imprecise error (Illegal transaction with ok response) | User/Privilege | Interrupt =\> VIM | n/a |
| Memory access permission violation | User/Privilege | ESM | 1.9 |
| Memory parity error | User/Privilege | ESM | 1.8 |

External imprecise error (Illegal transaction with ok response) User/Privilege Interrupt =\> VIM n/a

Memory access permission violation User/Privilege ESM 1.9 Memory parity error User/Privilege ESM 1.8

**High-End Timer** ** ** **Transfer Unit** ** ** **2** ** ** **(HTU2)**

| NCNB (Strongly Ordered) transaction with slave error response | User/Privilege | Interrupt =\> VIM | n/a |
|:--- |:--- |:--- |:--- |
| External imprecise error (Illegal transaction with ok response) | User/Privilege | Interrupt =\> VIM | n/a |
| Memory access permission violation | User/Privilege | ESM | 1.9 |
| Memory parity error | User/Privilege | ESM | 1.8 |

External imprecise error (Illegal transaction with ok response) User/Privilege Interrupt =\> VIM n/a

Memory access permission violation User/Privilege ESM 1.9 Memory parity error User/Privilege ESM 1.8

(1) The Undefined Instruction TRAP is NOT detectable outside the CPU. The trap is taken only if the instruction reaches the execute stage of the CPU.

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## Table 6-37. Reset/Abort/Error Sources (continued)

# ESM HOOKUP

**ERROR SOURCE** **SYSTEM** ** ** **MODE** **ERROR RESPONSE** **group.channel**

# N2HET1 Memory parity error User/Privilege ESM 1.7

# N2HET2 Memory parity error User/Privilege ESM 1.34

# FLEXRAY Memory parity error User/Privilege ESM 1.12

**FLEXRAY** ** ** **Transfer Unit** ** ** **(FTU)**

| NCNB (Strongly Ordered) transaction with slave error response | User/Privilege | Interrupt =\> VIM | n/a |
|:--- |:--- |:--- |:--- |
| External imprecise error (Illegal transaction with ok response) | User/Privilege | Interrupt =\> VIM | n/a |
| Memory access permission violation | User/Privilege | ESM | 1.16 |
| Memory parity error | User/Privilege | ESM | 1.14 |

External imprecise error (Illegal transaction with ok response) User/Privilege Interrupt =\> VIM n/a

Memory access permission violation User/Privilege ESM 1.16 Memory parity error User/Privilege ESM 1.14

# ETHERNET MASTER INTERFACE

Any error reported by slave being accessed User/Privilege ESM 1.43

# MIBSPI

| MibSPI1 memory parity error | User/Privilege | ESM | 1.17 |
|:--- |:--- |:--- | ---: |
| MibSPI3 memory parity error | User/Privilege | ESM | 1.18 |
| MibSPI5 memory parity error | User/Privilege | ESM | 1.24 |

MibSPI3 memory parity error User/Privilege ESM 1.18

MibSPI5 memory parity error User/Privilege ESM 1.24

# MIBADC

MibADC1 Memory parity error User/Privilege ESM 1.19

MibADC2 Memory parity error User/Privilege ESM 1.1

# DCAN

| DCAN1 memory parity error | User/Privilege | ESM | 1.21 |
|:--- |:--- |:--- | ---: |
| DCAN2 memory parity error | User/Privilege | ESM | 1.23 |
| DCAN3 memory parity error | User/Privilege | ESM | 1.22 |

DCAN2 memory parity error User/Privilege ESM 1.23

DCAN3 memory parity error User/Privilege ESM 1.22

# PLL PLL slip error User/Privilege ESM 1.10 PLL #2 slip error User/Privilege ESM 1.42

# CLOCK MONITOR

Clock monitor interrupt User/Privilege ESM 1.11

# DCC DCC1 error User/Privilege ESM 1.30 DCC2 error User/Privilege ESM 1.62

# CCM-R4 Self test failure User/Privilege ESM 1.31

Compare failure User/Privilege ESM => NMI => nERROR 2.2

# VIM Memory parity error User/Privilege ESM 1.15

# VOLTAGE MONITOR VMON out of voltage range n/a Reset n/a

# CPU SELFTEST (LBIST)

CPU Selftest (LBIST) error User/Privilege ESM 1.27

# PIN MULTIPLEXING CONTROL

Mux configuration error User/Privilege ESM 1.37

# POWER DOMAIN CONTROL PSCON compare error User/Privilege ESM 1.38 PSCON self-test error User/Privilege ESM 1.39

# eFuse CONTROLLER

*System* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## Table 6-37. Reset/Abort/Error Sources (continued)

# ESM HOOKUP

**ERROR SOURCE** **SYSTEM** ** ** **MODE** **ERROR RESPONSE** **group.channel**

| eFuse Controller Autoload error | User/Privilege | ESM =\> nERROR | 3.1 |
|:--- |:--- |:--- | ---: |
| eFuse Controller - Any bit set in the error status register | User/Privilege | ESM | 1.40 |
| eFuse Controller self-test error | User/Privilege | ESM | 1.41 |

eFuse Controller - Any bit set in the error status register User/Privilege ESM 1.40

eFuse Controller self-test error User/Privilege ESM 1.41

# WINDOWED WATCHDOG

WWD Non-Maskable Interrupt exception n/a ESM => NMI => nERROR 2.24

# ERRORS REFLECTED IN THE SYSESR REGISTER

| Power-Up Reset | n/a | Reset | n/a |
|:--- |:--- |:--- |:--- |
| Oscillator fail / PLL slip(2) | n/a | Reset | n/a |
| Watchdog exception | n/a | Reset | n/a |
| CPU Reset (driven by the CPU STC) | n/a | Reset | n/a |
| Software Reset | n/a | Reset | n/a |
| External Reset | n/a | Reset | n/a | Oscillator fail / PLL slip (2) n/a Reset n/a Watchdog exception n/a Reset n/a

CPU Reset (driven by the CPU STC) n/a Reset n/a Software Reset n/a Reset n/a External Reset n/a Reset n/a

(2) Oscillator fail/PLL slip can be configured in the system register (SYS.PLLCTL1) to generate a reset.

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

| SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 | www.ti.com |
|:--- |:--- |
| 6.20 | Digital Windowed Watchdog |
| This device includes a digital windowed watchdog (DWWD) module that protects against runaway code | execution. | **6.20** **Digital Windowed Watchdog**

This device includes a digital windowed watchdog (DWWD) module that protects against runaway code execution.

The DWWD module allows the application to configure the time window within which the DWWD module expects the application to service the watchdog. A watchdog violation occurs if the application services the watchdog outside of this window, or fails to service the watchdog at all. The application can choose to generate a system reset or an ESM group2 error signal in case of a watchdog violation.

The watchdog is disabled by default and must be enabled by the application. Once enabled, the watchdog can only be disabled upon a system reset.

*System* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TRST

# TMS **TCK**

# TDI **TDO**

# RTCK

# ICEPICK\_C

## Boundary Scan **BSR/BSDL** **Boundary** ** Scan I/F**

## Secondary Tap 0 **DAP** **Debug APB**

## Debug **ROM1**

## APB slave

## Cortex **R4F** **APB** ** Mux**

# AHB-AP **POM** to SCR1 via A2A from PCR1/Bridge

| Test Tap 0 | eFuse Farm |
|:--- |:--- |
| Secondary Tap 2 | AJSM |
| Test Tap 1 | PSCON |

## Secondary Tap 2 **AJSM**

## Test Tap 1 **PSCON**

# TMS570LS1227

| www.ti.com | SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 |
|:--- |:--- |
| 6.21 | Debug Subsystem |
| 6.21.1 | Block Diagram |

## 6.21 **Debug** ** ** **Subsystem**

## 6.21.1 ***Block Diagram***

## The device contains an ICEPICK module to allow JTAG access to the scan chains.

## Figure 6-20. Debug Subsystem Block Diagram

## 6.21.2

***Debug*** *** *** ***Components*** *** *** ***Memory Map***

## Table 6-38. Debug Components Memory Map

# FRAME ADDRESS RANGE

**RESPNSE FOR ACCESS TO** **FRAME CHIP** **FRAME** **ACTUA** **MODULE NAME** **UNIMPLEMENTED LOCATIONS IN** **SELECT** **SIZE** **L SIZE** **START** **END** **FRAME**

CoreSight Debug Reads return zeros, writes have no CSCS0 0xFFA0\_0000 0xFFA0\_0FFF 4KB 4KB ROM effect

Cortex-R4F Reads return zeros, writes have no CSCS1 0xFFA0\_1000 0xFFA0\_1FFF 4KB 4KB Debug effect

## 6.21.3

***JTAG*** *** *** ***Identification*** *** *** ***Code***

## The JTAG ID code for this device is the same as the device ICEPick Identification Code.

## Table 6-39. JTAG ID Code

| Silicon Revision | ID |
|:--- |:--- |
| Rev A | 0x0B95502F |
| Rev B | 0x2B95502F |
| Rev C | 0x3B95502F | Rev A 0x0B95502F Rev B 0x2B95502F Rev C 0x3B95502F

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## 6.21.4 ***Debug*** *** *** ***ROM***

## The Debug ROM stores the location of the components on the Debug APB bus

## Table 6-40. Debug ROM table

| ADDRESS | DESCRIPTION | VALUE |
|:--- |:--- |:--- |
| 0x000 | pointer to Cortex-R4F | 0x0000 1003 |
| 0x001 | Reserved | 0x0000 2002 |
| 0x002 | Reserved | 0x0000 3002 |
| 0x003 | POM | 0x0000 4003 |
| 0x004 | end of table | 0x0000 0000 |
| System Information and Electrical Specifications | Copyright © 2012-2015, Texas Instruments Incorporated | Submit Documentation Feedback | 0x000 pointer to Cortex-R4F 0x0000 1003 0x001 Reserved 0x0000 2002 0x002 Reserved 0x0000 3002 0x003 POM 0x0000 4003 0x004 end of table 0x0000 0000

*System* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS TDI

# TDO

# RTCK

# TCK

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 6.21.5

***JTAG*** *** *** ***Scan*** *** *** ***Interface*** *** *** ***Timings***

## Table 6-41. JTAG Scan Interface Timing (1)

**No.** **Parameter** **Min** **MAX** **Unit**

| fTCK | TCK frequency (at HCLKmax) | MHz |
|:--- |:--- |:--- |
| fRTCK | RTCK frequency (at TCKmax and HCLKmax) | MHz |
| td(TCK -RTCK) | Delay time, TCK to RTCK | ns |
| tsu(TDI/TMS - RTCKr) | Setup time, TDI, TMS before RTCK rise (RTCKr) | ns |
| th(RTCKr -TDI/TMS) | Hold time, TDI, TMS after RTCKr | ns |
| th(RTCKr -TDO) | Hold time, TDO after RTCKf | ns |
| td(TCKf -TDO) | Delay time, TDO valid after RTCK fall (RTCKf) | ns |

fRTCK RTCK frequency (at TCKmax and HCLKmax) MHz td(TCK -RTCK) Delay time, TCK to RTCK ns

tsu(TDI/TMS - RTCKr) Setup time, TDI, TMS before RTCK rise (RTCKr) ns

th(RTCKr -TDI/TMS) Hold time, TDI, TMS after RTCKr ns th(RTCKr -TDO) Hold time, TDO after RTCKf ns

td(TCKf -TDO) Delay time, TDO valid after RTCK fall (RTCKf) ns

(1) Timings for TDO are specified for a maximum of 50pF load on TDO

## Figure 6-21. JTAG Timing

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# H **L** **H** **L** **H** **L** **L** **H**

#... **...** **128-bit** ** comparator**

# H **L** **L** **H** **H** **L** **L** **H**

# UNLOCK **Flash Module Output** **OTP Contents** **Unlock** ** By Scan** **Register** **Internal Tie-Offs** **(example only)** **(example)**

# L

# H

# H

# L

# L **Internal** ** Tie-Offs** **(example only)**

# L

# H

# H

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

***6.21.6*** ***Advanced*** *** *** ***JTAG*** *** *** ***Security Module***

This device includes a an Advanced JTAG Security Module (AJSM). which provides maximum security to the device's memory content by allowing users to secure the device after programming. **Figure 6-22.** ** ** **AJSM Unlock**

The device is unsecure by default by virtue of a 128-bit visible unlock code programmed in the OTP address 0xF0000000.The OTP contents are XOR-ed with the "Unlock By Scan" register contents. The outputs of these XOR gates are again combined with a set of secret internal tie-offs. The output of this combinational logic is compared against a secret hard-wired 128-bit value. A match results in the UNLOCK signal being asserted, so that the device is now unsecure.

A user can secure the device by changing at least one bit in the visible unlock code from 1 to 0. Changing a 0 to 1 is not possible since the visible unlock code is stored in the One Time Programmable (OTP) flash region. Also, changing all the 128 bits to zeros is not a valid condition and will permanently secure the device.

Once secured, a user can unsecure the device by scanning an appropriate value into the "Unlock By Scan" register of the AJSM module. This register is accessible by configuring an IR value of 0b1011 on the AJSM TAP. The value to be scanned is such that the XOR of the OTP contents and the Unlock-ByScan register contents results in the original visible unlock code.

The Unlock-By-Scan register is reset only upon asserting power-on reset (nPORRST).

A secure device only permits JTAG accesses to the AJSM scan chain through the Secondary Tap # 2 of the ICEPick module. All other secondary taps, test taps and the boundary scan interface are not accessible in this state.

*System* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TRST

# TMS **TCK**

# TDI **TDO**

# RTCK

# IC EPICK **Boundary**

# BSDL **Boundary Scan Interface** **Scan** **Device Pins (conceptual)**

# TDI

# TDO

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

***6.21.7*** ***Boundary Scan*** *** *** ***Chain***

The device supports BSDL-compliant boundary scan for testing pin-to-pin compatibility. The boundary scan chain is connected to the Boundary Scan Interface of the ICEPICK module.

**Figure 6-23. Boundary Scan Implementation** ** ** **(Conceptual** ** ** **Diagram)**

Data is serially shifted into all boundary-scan buffers through TDI, and out through TDO.

Copyright © 2012-2015, Texas Instruments Incorporated *System* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# SOCA1, SOCB1

# EPWM1INTn

# EPWM1TZINTn

# EQEP1ERR / EQEP2ERR / EQEP1ERR or EQEP2ERR Debug Mode Entry OSC FAIL or PLL Slip

# IOMUX

# EPWMSYNCI

# EPWM1

# ECAP

# EPWM1A

# EPWM1B

# EPWM2/3/4/5/6A

# EPWM2/3/4/5/6B

# EPWM

# EPWM7A

# ECAP1 Pulse Stretch, 8 VCLK4 cycles

# EPWMSYNCO ADC Wrapper VBus32 / VBus32DP TZ1/2/3n

# EPWM1ENCLK

# TBCLKSYNC

# VIM

# VCLK4, SYS\_nRST

# EPWM2/3/4/5/6ENCLK

# TBCLKSYNC

# EPWM7ENCLK

# TBCLKSYNC

# ECAP1INTn

# EPWM **2/3/4/5/6**

# VIM

# EQEP1 + EQEP2

# EPWM7B

# CPU System Module TZ6n TZ5n TZ4n

# VCLK4, SYS\_nRST TZ1/2/3n TZ1/2/3n Debug Mode Entry OSC FAIL or PLL Slip TZ6n TZ5n TZ4n Debug Mode Entry

# OSC FAIL or PLL SLip TZ6n TZ5n TZ4n

# SOCA2/3/4/5/6 SOCB2/3/4/5/6

# EPWM2/3/4/5/6INTn

# EPWM2/3/4/5/6TZINTn

# EPWM7INTn

# EPWM7TZINTn VBus32 VBus32

# VCLK4, SYS\_nRST VBus32

# VIM ADC Wrapper

# VIM

# EQEP1 + EQEP2

# CPU System Module

# VIM ADC Wrapper

# VIM

# EQEP1 + EQEP2

# CPU System Module

# VIM

| Mux | Selector |
|:--- |:--- |
| Mux | Selector |
| EQEP1ERR / EQEP2ERR / | EQEP1ERR or EQEP2ERR |
| EQEP1ERR / EQEP2ERR / | EQEP1ERR or EQEP2ERR | Mux Selector

# EQEP1ERR / EQEP2ERR / EQEP1ERR or EQEP2ERR

# EQEP1ERR / EQEP2ERR / EQEP1ERR or EQEP2ERR SOCA7, SOCB7 Mux Selector

# NHET1\_LOOP\_SYNC

# PINMMR36\[25\]

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

# Peripheral Information and Electrical Specifications

## 7.1

**Enhanced Translator** ** ** **PWM Modules (ePWM)**

## Figure 7-1 illustrates the connections between the seven ePWM modules (ePWM1,2,3,4,5,6,7) on the device.

## Figure 7-1. ePWMx Module Interconnections

*Peripheral* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# N2HET1 N2HET2

# ePWM1 2 VCLK4 cycles Pulse Strength

# ePWM1\_SYNCI

# SYNCI

# EXT\_LOOP\_SYNC N2HET1\_LOOP\_SYNC

# ePWM1\_SYNCI\_SYNCED

# ePWM1\_SYNCI\_FILTERED

# PINMMR47\[8,9,10\]

# PINMMR36\[25\]

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

***7.1.1*** ***ePWM*** *** *** ***Clocking*** *** *** ***and*** *** *** ***Reset***

Each ePWM module has a clock enable (EPWMxENCLK). When SYS\_nRST is active low, the clock enables are ignored and the ePWM logic is clocked so that it can reset to a proper state. When SYS\_nRST goes in-active high, the state of clock enable is respected.

**Table 7-1. ePWMx** ** ** **Clock Enable Control**

**ePWM Module** ** ** **Instance** **Control** ** ** **Register to Enable Clock** **Default** ** ** **Value**

| ePWM1 | PINMMR37\[8\] |
|:--- |:--- |
| ePWM2 | PINMMR37\[16\] |
| ePWM3 | PINMMR37\[24\] |
| ePWM4 | PINMMR38\[0\] |
| ePWM5 | PINMMR38\[8\] |
| ePWM6 | PINMMR38\[16\] |
| ePWM7 | PINMMR38\[24\] |

# ePWM2 PINMMR37\[16\]

# ePWM3 PINMMR37\[24\]

# ePWM4 PINMMR38\[0\]

# ePWM5 PINMMR38\[8\]

# ePWM6 PINMMR38\[16\]

# ePWM7 PINMMR38\[24\]

The default value of the control registers to enable the clocks to the ePWMx modules is 1. This means that the VCLK4 clock connections to the ePWMx modules are enabled by default. The application can choose to gate off the VCLK4 clock to any ePWMx module individually by clearing the respective control register bit.

***7.1.2*** ***Synchronization of ePWMx Time Base*** *** *** ***Counters***

A time-base synchronization scheme connects all of the ePWM modules on a device. Each ePWM module has a synchronization input (EPWMxSYNCI) and a synchronization output (EPWMxSYNCO). The input synchronization for the first instance (ePWM1) comes from an external pin. Figure 7-1 shows the synchronization connections for all the ePWMx modules. Each ePWM module can be configured to use or ignore the synchronization input. Refer to the ePWM chapter in the TMS570LS12x/11x Technical Reference Manual ( SPNU515 ) for more information.

***7.1.3*** ***Synchronizing all*** *** *** ***ePWM*** *** *** ***Modules to the*** *** *** ***N2HET1 Module*** *** *** ***Time Base***

The connection between the N2HET1\_LOOP\_SYNC and SYNCI input of ePWM1 module is implemented as shown in Figure 7-2.

**Figure** ** ** **7-2. Synchronizing Time Bases Between** ** ** **N2HET1, N2HET2 and ePWMx** ** ** **Modules**

Copyright © 2012-2015, Texas Instruments Incorporated *Peripheral* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

***7.1.4*** ***Phase-Locking*** *** *** ***the*** *** *** ***Time-Base Clocks*** *** *** ***of Multiple ePWM*** *** *** ***Modules***

The TBCLKSYNC bit can be used to globally synchronize the time-base clocks of all enabled ePWM modules on a device. This bit is implemented as PINMMR37 register bit 1.

When TBCLKSYNC = 0, the time-base clock of all ePWM modules is stopped. This is the default condition.

When TBCLKSYNC = 1, all ePWM time-base clocks are started with the rising edge of TBCLK aligned.

For perfectly synchronized TBCLKs, the prescaler bits in the TBCTL register of each ePWM module must be set identically. The proper procedure for enabling the ePWM clocks is as follows: 1. Enable the individual ePWM module clocks (if disable) using the control registers shown in Table 7-1. 2. Configure TBCLKSYNC = 0. This will stop the time-base clock within any enabled ePWM module. 3. Configure the prescaler values and desired ePWM modes. 4. Configure TBCLKSYNC = 1.

***7.1.5*** ***ePWM*** *** *** ***Synchronization with*** *** *** ***External Devices***

The output sync from EPWM1 Module is also exported to a device output terminal so that multiple devices can be synchronized together. The signal pulse is stretched by eight VCLK4 cycles before being exported on the terminal as the EPWM1SYNCO signal.

***7.1.6*** ***ePWM*** *** *** ***Trip*** *** *** ***Zones***

The ePWMx modules have six trip zone inputs each. These are active-low signals. The application can control the ePWMx module response to each of the trip zone input separately. The timing requirements from the assertion of the trip zone inputs to the actual response are specified in Section 7.1.8.

**7.1.6.1** **Trip** ** ** **Zones TZ1n, TZ2n, TZ3n**

These three trip zone inputs are driven by external circuits and are connected to device-level inputs. These signals are either connected asynchronously to the ePWMx trip zone inputs, or doublesynchronized with VCLK4, or double-synchronized and then filtered with a 6-cycle VCLK4-based counter before connecting to the ePWMx. By default, the trip zone inputs are asynchronously connected to the ePWMx modules.

**Table 7-2. Connection to ePWMx** ** ** **Modules for Device-Level** ** ** **Trip Zone Inputs**

**Trip** ** ** **Zone** ** ** **Input** **Control** ** ** **for** **Control** ** ** **for** ** ** **Double-Synchronized** **Control** ** ** **for** ** ** **Double-Synchronized and** ** ** **Filtered** **Asynchronous** **Connection to ePWMx** **Connection to ePWMx** **Connection to ePWMx**

| TZ1n | PINMMR46\[16\] = 1 | PINMMR46\[16\] = 0 AND | PINMMR46\[16\] = 0 AND PINMMR46\[17\] = 0 | PINMMR46\[17\] = 1 | AND PINMMR46\[18\] = 1 |
|:--- |:--- |:--- |:--- |:--- |:--- |
| TZ2n | PINMMR46\[24\] = 1 | PINMMR46\[24\] = 0 AND | PINMMR46\[24\] = 0 AND PINMMR46\[25\] = 0 | PINMMR46\[25\] = 1 | AND PINMMR46\[26\] = 1 |
| TZ3n | PINMMR47\[0\] = 1 | PINMMR47\[0\] = 0 AND PINMMR47\[1\] | PINMMR47\[0\] = 0 AND PINMMR47\[1\] = 0 AND | = 1 | PINMMR47\[2\] = 1 |

# TZ2n

$$ PINMMR46[24] = 1 $$ $$ PINMMR46[24] = 0 AND $$ $$ PINMMR46[24] = 0 AND PINMMR46[25] = 0 $$ $$ PINMMR46[25] = 1 $$ $$ AND PINMMR46[26] = 1 $$

# TZ3n

$$ PINMMR47[0] = 1 $$ $$ PINMMR47[0] = 0 AND PINMMR47[1] $$ $$ PINMMR47[0] = 0 AND PINMMR47[1] = 0 AND $$ $$ = 1 $$ $$ PINMMR47[2] = 1 $$ **7.1.6.2** **Trip** ** ** **Zone TZ4n**

This trip zone input is dedicated to eQEPx error indications. There are two eQEP modules on this device. Each eQEP module indicates a phase error by driving its EQEPxERR output High. The following control registers allow the application to configure the trip zone input (TZ4n) to each ePWMx module based on the application's requirements.

*Peripheral* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## Table 7-3. TZ4n Connections for ePWMx Modules

**ePWMx** **Control** ** ** **for** ** ** **TZ4n** ** ** **=** **Control** ** ** **for** ** ** **TZ4n** ** ** **= not(EQEP1ERR)** **Control** ** ** **for** ** ** **TZ4n** ** ** **= not(EQEP2ERR)** **not(EQEP1ERR** ** ** **OR**

# EQEP2ERR)

| ePWM1 | PINMMR41\[0\] = 1 | PINMMR41\[0\] = 0 AND PINMMR41\[1\] | PINMMR41\[0\] = 1 AND PINMMR41\[1\] = 0 AND | = 1 | PINMMR41\[2\] = 1 |
|:--- |:--- |:--- |:--- |:--- |:--- |
| ePWM2 | PINMMR41\[8\] | PINMMR41\[8\] = 0 AND PINMMR41\[9\] | PINMMR41\[8\] = 1 AND PINMMR41\[9\] = 0 AND | = 1 | PINMMR41\[10\] = 1 |
| ePWM3 | PINMMR41\[16\] | PINMMR41\[16\] = 0 AND | PINMMR41\[16\] = 1 AND PINMMR41\[17\] = 0 | PINMMR41\[17\] = 1 | AND PINMMR41\[18\] = 1 |
| ePWM4 | PINMMR41\[24\] | PINMMR41\[24\] = 0 AND | PINMMR41\[24\] = 1 AND PINMMR41\[25\] = 0 | PINMMR41\[25\] = 1 | AND PINMMR41\[26\] = 1 |
| ePWM5 | PINMMR42\[0\] | PINMMR42\[0\] = 0 AND PINMMR42\[1\] | PINMMR42\[0\] = 1 AND PINMMR42\[1\] = 0 AND | = 1 | PINMMR42\[2\] = 1 |
| ePWM6 | PINMMR42\[8\] | PINMMR42\[8\] = 0 AND PINMMR42\[9\] | PINMMR42\[8\] = 1 AND PINMMR42\[9\] = 0 AND | = 1 | PINMMR42\[10\] = 1 |
| ePWM7 | PINMMR42\[16\] | PINMMR42\[16\] = 0 AND | PINMMR42\[16\] = 1 AND PINMMR42\[17\] = 0 | PINMMR42\[17\] = 1 | AND PINMMR42\[18\] = 1 |

# ePWM2

PINMMR41\[8\] $$ PINMMR41[8] = 0 AND PINMMR41[9] $$ $$ PINMMR41[8] = 1 AND PINMMR41[9] = 0 AND $$ $$ = 1 $$ $$ PINMMR41[10] = 1 $$

# ePWM3

PINMMR41\[16\] $$ PINMMR41[16] = 0 AND $$ $$ PINMMR41[16] = 1 AND PINMMR41[17] = 0 $$ $$ PINMMR41[17] = 1 $$ $$ AND PINMMR41[18] = 1 $$

# ePWM4

PINMMR41\[24\] $$ PINMMR41[24] = 0 AND $$ $$ PINMMR41[24] = 1 AND PINMMR41[25] = 0 $$ $$ PINMMR41[25] = 1 $$ $$ AND PINMMR41[26] = 1 $$

# ePWM5

PINMMR42\[0\] $$ PINMMR42[0] = 0 AND PINMMR42[1] $$ $$ PINMMR42[0] = 1 AND PINMMR42[1] = 0 AND $$ $$ = 1 $$ $$ PINMMR42[2] = 1 $$

# ePWM6

PINMMR42\[8\] $$ PINMMR42[8] = 0 AND PINMMR42[9] $$ $$ PINMMR42[8] = 1 AND PINMMR42[9] = 0 AND $$ $$ = 1 $$ $$ PINMMR42[10] = 1 $$

# ePWM7

PINMMR42\[16\] $$ PINMMR42[16] = 0 AND $$ $$ PINMMR42[16] = 1 AND PINMMR42[17] = 0 $$ $$ PINMMR42[17] = 1 $$ $$ AND PINMMR42[18] = 1 $$

## 7.1.6.3 **Trip** ** ** **Zone TZ5n**

## This trip zone input is dedicated to a clock failure on the device. That is, this trip zone input is asserted

whenever an oscillator failure or a PLL slip is detected on the device. The application can use this trip zone input for each ePWMx module in order to prevent the external system from going out of control when the device clocks are not within expected range (system running at limp clock).

## The oscillator failure and PLL slip signals used for this trip zone input are taken from the status flags in the

system module. These are level signals are set until cleared by the application.

## 7.1.6.4 **Trip** ** ** **Zone TZ6n**

## This trip zone input to the ePWMx modules is dedicated to a debug mode entry of the CPU. If enabled,

the user can force the PWM outputs to a known state when the emulator stops the CPU. This prevents the external system from going out of control when the CPU is stopped.

## 7.1.7

***Triggering*** *** *** ***of ADC*** *** *** ***Start*** *** *** ***of Conversion*** *** *** ***Using ePWMx SOCA*** *** *** ***and*** *** *** ***SOCB*** *** *** ***Outputs***

## A special scheme is implemented in order to select the actual signal used for triggering the start of

conversion on the two ADCs on this device. This scheme is defined in Section 7.4.2.3.

## 7.1.8

***Enhanced Translator-Pulse Width Modulator*** *** *** ***(ePWMx)*** *** *** ***Timings***

## Table 7-4. ePWMx Timing Requirements

# PARAMETER

**TEST** ** ** **CONDITIONS** **MIN** **MAX** **UNIT**

t w(SYNCIN) Synchronization input pulse width Asynchronous 2 t c(VCLK4) cycles Synchronous 2 t c(VCLK4) cycles

Synchronous, with input 2 t c(VCLK4) + filter width cycles filter

## Table 7-5. ePWMx Switching Characteristics

# PARAMETER

**TEST** ** ** **CONDITIONS** **MIN** **MAX** **UNIT**

t w(PWM) Pulse duration, ePWMx output high or low 33.33 ns

t w(SYNCOUT Synchronization Output Pulse Width 8 t c(VCLK4) cycles

) t d(PWM)tza Delay time, trip input active to PWM forced high, no pin load ns OR Delay time, trip input active to PWM forced low

Copyright © 2012-2015, Texas Instruments Incorporated *Peripheral* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## Table 7-5. ePWMx Switching Characteristics (continued)

# PARAMETER

**TEST** ** ** **CONDITIONS** **MIN** **MAX** **UNIT**

t d(TZDelay time, trip input active to PWM Hi-Z ns

# PWM)HZ

## Table 7-6. ePWMx Trip-Zone Timing Requirements

# PARAMETER

**TEST** ** ** **CONDITIONS** **MIN** **MAX** **UNIT**

t w(TZ) Pulse duration, TZn input low Asynchronous 2 \* HSPCLKDIV \* ns CLKDIV \* t c(VCLK4) (1) Synchronous 2 t c(VCLK4) ns

Synchronous, with input 8 t c(VCLK4) ns filter

(1) Refer to the ePWM chapter of the TMS570LS12x/11x Technical Reference Manual ( SPNU515 ) for more information on the clock divider fields HSPCLKDIV and CLKDIV.

*Peripheral* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# IOMUX

# EPWM1SYNCO

# ECAP1

# ECAP

# ECAP1INTn

# ECAP1ENCLK

# VCLK4, SYS\_nRST

# ECAP2ENCLK

# ECAP **2/3/4/5**

# VCLK4, SYS\_nRST

# ECAP2INTn

# ECAP6INTn VBus32

# VBus32 VIM

# VIM

# VIM

# ECAP1

# ECAP1SYNCI

# ECAP1SYNCO

# ECAP2SYNCI

# ECAP2SYNCO

# ECAP2

# ECAP6ENCLK

# VCLK4, SYS\_nRST VBus32

# ECAP6

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

**7.2** **Enhanced Capture** ** ** **Modules (eCAP)**

Figure 7-3 shows how the eCAP modules are interconnected on this microcontroller. **Figure 7-3. eCAP Module Connections**

***7.2.1*** ***Clock Enable Control for eCAPx Modules***

Each of the ECAPx modules have a clock enable (ECAPxENCLK). These signals need to be generated from a device-level control register. When SYS\_nRST is active low, the clock enables are ignored and the ECAPx logic is clocked so that it can reset to a proper state. When SYS\_nRST goes in-active high, the state of clock enable is respected.

Copyright © 2012-2015, Texas Instruments Incorporated *Peripheral* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**> **Table 7-7. eCAPx Clock Enable Control**

**ePWM Module** ** ** **Instance** **Control** ** ** **Register to Enable Clock** **Default** ** ** **Value**

| eCAP1 | PINMMR39\[0\] |
|:--- |:--- |
| eCAP2 | PINMMR39\[8\] |
| eCAP3 | PINMMR39\[16\] |
| eCAP4 | PINMMR39\[24\] |
| eCAP5 | PINMMR40\[0\] |
| eCAP6 | PINMMR40\[8\] |

# eCAP2 PINMMR39\[8\]

# eCAP3 PINMMR39\[16\]

# eCAP4 PINMMR39\[24\]

# eCAP5 PINMMR40\[0\]

# eCAP6 PINMMR40\[8\]

The default value of the control registers to enable the clocks to the eCAPx modules is 1. This means that the VCLK4 clock connections to the eCAPx modules are enabled by default. The application can choose to gate off the VCLK4 clock to any eCAPx module individually by clearing the respective control register bit.

***7.2.2*** ***PWM Output Capability of eCAPx***

When not used in capture mode, each of the eCAPx modules can be used as a single-channel PWM output. This is called the auxiliary PWM (APWM) mode of operation of the eCAP modules. Refer to the eCAP chapter of the TMS570LS12x/11x Technical Reference Manual ( SPNU515 ) for more information.

***7.2.3*** ***Input*** *** *** ***Connection to eCAPx Modules***

The input connection to each of the eCAP modules can be selected between a double-VCLK4synchronized input or a double-VCLK4-synchronized and filtered input, as shown in Table 7-8.

**Table 7-8. Device-Level** ** ** **Input Connection to eCAPx Modules**

**Input** ** ** **Signal** **Control** ** ** **for** ** ** **Double-Synchronized Connection to** **Control** ** ** **for** ** ** **Double-Synchronized and** ** ** **Filtered** **eCAPx** **Connection to eCAPx**

| eCAP1 | PINMMR43\[0\] = 1 | PINMMR43\[0\] = 0 AND PINMMR43\[1\] = 1 |
|:--- |:--- |:--- |
| eCAP2 | PINMMR43\[8\] = 1 | PINMMR43\[8\] = 0 AND PINMMR43\[9\] = 1 |
| eCAP3 | PINMMR43\[16\] = 1 | PINMMR43\[16\] = 0 AND PINMMR43\[17\] = 1 |
| eCAP4 | PINMMR43\[24\] = 1 | PINMMR43\[24\] = 0 AND PINMMR43\[25\] = 1 |
| eCAP5 | PINMMR44\[0\] = 1 | PINMMR44\[0\] = 0 AND PINMMR44\[1\] = 1 |
| eCAP6 | PINMMR44\[8\] = 1 | PINMMR44\[8\] = 0 AND PINMMR44\[9\] = 1 |

# eCAP2

$$ PINMMR43[8] = 1 $$ $$ PINMMR43[8] = 0 AND PINMMR43[9] = 1 $$

# eCAP3

$$ PINMMR43[16] = 1 $$ $$ PINMMR43[16] = 0 AND PINMMR43[17] = 1 $$

# eCAP4

$$ PINMMR43[24] = 1 $$ $$ PINMMR43[24] = 0 AND PINMMR43[25] = 1 $$

# eCAP5

$$ PINMMR44[0] = 1 $$ $$ PINMMR44[0] = 0 AND PINMMR44[1] = 1 $$

# eCAP6

$$ PINMMR44[8] = 1 $$ $$ PINMMR44[8] = 0 AND PINMMR44[9] = 1 $$

***7.2.4*** ***Enhanced Capture*** *** *** ***Module*** *** *** ***(eCAP) Timings*** **Table 7-9. eCAPx Timing Requirements**

# PARAMETER

**TEST** ** ** **CONDITIONS** **MIN** **MAX** **UNIT**

t w(CAP) Capture input pulse width Synchronous 2 t c(VCLK4) cycles

Synchronous, with input 2 t c(VCLK4) + filter width cycles filter

**Table 7-10. eCAPx Switching** ** ** **Characteristics**

# PARAMETER

**TEST** ** ** **CONDITIONS** **MIN** **MAX** **UNIT**

t w(APWM) Pulse duration, APWMx output high or low ns

*Peripheral* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# EQEP1A

# VIM EQEP1INTn EQEP1 Module IO Mux

# EQEP1ENCLK

# EQEP1IO

# EQEP1I VBus32

# VCLK4 SYS\_nRST

# EQEP1B

# EQEP1IOE

# EQEP1SO

# EQEP1S

# EQEP1SOE

# EQEP1ERR

# EPWM1/../7 TZ4n

# EQEP2A

# VIM EQEP2INTn EQEP2 Module

# EQEP2ENCLK

# EQEP2IO

# EQEP2I VBus32

# VCLK4 SYS\_nRST

# EQEP2B

# EQEP2IOE

# EQEP2SO

# EQEP2S

# EQEP2SOE EQEP2ERR Connection Selection Mux

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

**7.3** **Enhanced Quadrature** ** ** **Encoder** ** ** **(eQEP)**

Figure 7-4 shows the eQEP module interconnections on the device. **Figure 7-4. eQEP Module Interconnections**

***7.3.1*** ***Clock Enable Control for eQEPx Modules***

Device-level control registers are implemented to generate the EQEPxENCLK signals. When SYS\_nRST is active low, the clock enables are ignored and the eQEPx logic is clocked so that it can reset to a proper state. When SYS\_nRST goes in-active high, the state of clock enable is respected. **Table 7-11. eQEPx Clock Enable Control**

**ePWM Module** ** ** **Instance** **Control** ** ** **Register to Enable Clock** **Default** ** ** **Value**

# eQEP1 PINMMR40\[16\]

# eQEP2 PINMMR40\[24\]

The default value of the control registers to enable the clocks to the eQEPx modules is 1. This means that the VCLK4 clock connections to the eQEPx modules are enabled by default. The application can choose to gate off the VCLK4 clock to any eQEPx module individually by clearing the respective control register bit.

***7.3.2*** ***Using*** *** *** ***eQEPx Phase Error to Trip*** *** *** ***ePWMx Outputs***

The eQEP module sets the EQEPERR signal output whenever a phase error is detected in its inputs EQEPxA and EQEPxB. This error signal from both the eQEP modules is input to the connection selection multiplexor. This multiplexor is defined in Table 7-3. As shown in Figure 7-1, the output of this selection multiplexor is inverted and connected to the TZ4n trip-zone input of all EPWMx modules. This connection allows the application to define the response of each ePWMx module on a phase error indicated by the eQEP modules.

***7.3.3*** ***Input*** *** *** ***Connections to eQEPx Modules***

The input connections to each of the eQEP modules can be selected between a double-VCLK4synchronized input or a double-VCLK4-synchronized and filtered input, as shown in Table 7-12.

Copyright © 2012-2015, Texas Instruments Incorporated *Peripheral* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## Table 7-12. Device-Level Input Connection to eCAPx Modules

**Input** ** ** **Signal** **Control** ** ** **for** ** ** **Double-Synchronized Connection to** **Control** ** ** **for** ** ** **Double-Synchronized and** ** ** **Filtered** **eQEPx** **Connection to eQEPx**

| eQEP1A | PINMMR44\[16\] = 1 | PINMMR44\[16\] = 0 and PINMMR44\[17\] = 1 |
|:--- |:--- |:--- |
| eQEP1B | PINMMR44\[24\] = 1 | PINMMR44\[24\] = 0 and PINMMR44\[25\] = 1 |
| eQEP1I | PINMMR45\[0\] = 1 | PINMMR45\[0\] = 0 and PINMMR45\[1\] = 1 |
| eQEP1S | PINMMR45\[8\] = 1 | PINMMR45\[8\] = 0 and PINMMR45\[9\] = 1 |
| eQEP2A | PINMMR45\[16\] = 1 | PINMMR45\[16\] = 0 and PINMMR45\[17\] = 1 |
| eQEP2B | PINMMR45\[24\] = 1 | PINMMR45\[24\] = 0 and PINMMR45\[25\] = 1 |
| eQEP2I | PINMMR46\[0\] = 1 | PINMMR46\[0\] = 0 and PINMMR46\[1\] = 1 |
| eQEP2S | PINMMR46\[8\] = 1 | PINMMR46\[8\] = 0 and PINMMR46\[9\] = 1 |

# eQEP1B

$$ PINMMR44[24] = 1 $$ $$ PINMMR44[24] = 0 and PINMMR44[25] = 1 $$

# eQEP1I

$$ PINMMR45[0] = 1 $$ $$ PINMMR45[0] = 0 and PINMMR45[1] = 1 $$

# eQEP1S

$$ PINMMR45[8] = 1 $$ $$ PINMMR45[8] = 0 and PINMMR45[9] = 1 $$

# eQEP2A

$$ PINMMR45[16] = 1 $$ $$ PINMMR45[16] = 0 and PINMMR45[17] = 1 $$

# eQEP2B

$$ PINMMR45[24] = 1 $$ $$ PINMMR45[24] = 0 and PINMMR45[25] = 1 $$

# eQEP2I

$$ PINMMR46[0] = 1 $$ $$ PINMMR46[0] = 0 and PINMMR46[1] = 1 $$

# eQEP2S

$$ PINMMR46[8] = 1 $$ $$ PINMMR46[8] = 0 and PINMMR46[9] = 1 $$

## 7.3.4

***Enhanced Quadrature*** *** *** ***Encoder*** *** *** ***Pulse*** *** *** ***(eQEPx)*** *** *** ***Timing***

## Table 7-13. eQEPx Timing Requirements

# PARAMETER

**TEST** ** ** **CONDITIONS** **MIN** **MAX** **UNIT**

t w(QEPP) QEP input period Synchronous 2 t c(VCLK4) cycles

Synchronous, with input 2 t c(VCLK4) + filter width cycles filter

t w(INDEXH) QEP Index Input High Time Synchronous 2 t c(VCLK4) cycles

Synchronous, with input 2 t c(VCLK4) + filter width cycles filter

t w(INDEXL) QEP Index Input Low Time Synchronous 2 t c(VCLK4) cycles

Synchronous, with input 2 t c(VCLK4) + filter width cycles filter

t w(STROBH) QEP Strobe Input High Time Synchronous 2 t c(VCLK4) cycles

Synchronous, with input 2 t c(VCLK4) + filter width cycles filter

t w(STROBL) QEP Strobe Input Low Time Synchronous 2 t c(VCLK4) cycles

Synchronous, with input 2 t c(VCLK4) + filter width cycles filter

## Table 7-14. eQEPx Switching Characteristics

| PARAMETER | MIN | MAX | UNIT |
|:--- |:--- |:--- |:--- |
| td(CNTR)xin | Delay time, external clock to counter increment | 4 tc(VCLK4) | cycles |
| td(PCS-OUT)QEP | Delay time, QEP input edge to position compare sync output | 6 tc(VCLK4) | cycles |

t d(CNTR)xin Delay time, external clock to counter increment 4 t c(VCLK4) cycles

t d(PCS-OUT)QEP Delay time, QEP input edge to position compare sync output 6 t c(VCLK4) cycles

## 7.4

**Multibuffered 12bit Analog-to-Digital** ** ** **Converter**

## The multibuffered A-to-D converter (MibADC) has a separate power bus for its analog circuitry that

enhances the A-to-D performance by preventing digital switching noise on the logic circuitry which could be present on V SS and V CC from coupling into the A-to-D analog stage. All A-to-D specifications are given with respect to AD REFLO unless otherwise noted.

## Table 7-15. MibADC Overview

| Description | Value |
|:--- |:--- |
| Resolution | 12 bits |
| Monotonic | Assured |
| Output conversion code | 00h to 3FFh \[00 for VAI ≤ADREFLO; 3FFh for VAI ≥ADREFHI\] | Resolution 12 bits Monotonic Assured

Output conversion code 00h to 3FFh \[00 for V AI ≤ AD REFLO; 3FFh for V AI ≥ AD REFHI \]

*Peripheral* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 7.4.1 ***Features***

- • 12-bit resolution - • AD REFHI and AD REFLO pins (high and low reference voltages) - • Total Sample/Hold/Convert time: 600ns Minimum at 30MHz ADCLK - • One memory region per conversion group is available (event, group 1, group 2) - • Allocation of channels to conversion groups is completely programmable - • Supports flexible channel conversion order - • Memory regions are serviced either by interrupt or by DMA - • Programmable interrupt threshold counter is available for each group - • Programmable magnitude threshold interrupt for each group for any one channel - • Option to read either 8-bit, 10-bit or 12-bit values from memory regions - • Single or continuous conversion modes - • Embedded self-test - • Embedded calibration logic - • Enhanced power-down mode - - Optional feature to automatically power down ADC core when no conversion is in progress - • External event pin (ADxEVT) programmable as general-purpose I/O

## 7.4.2 ***Event Trigger Options***

The ADC module supports 3 conversion groups: Event Group, Group1 and Group2. Each of these 3 groups can be configured to be hardware event-triggered. In that case, the application can select from among 8 event sources to be the trigger for a group's conversions. **7.4.2.1** **MIBADC1 Event Trigger Hookup**

**Table 7-16.** ** ** **MIBADC1** ** ** **Event Trigger Hookup**

**Trigger** ** ** **Event** ** ** **Signal** **Group** ** ** **Source** **Select,** ** ** **G1SRC,** $$ PINMMR30[0] = 0 and PINMMR30[1] = 1 $$ **Event** ** ** **#** $$ PINMMR30[0] = 1 $$ **G2SRC or** **Control** ** ** **for** **Control** ** ** **for** **(default)** **Option** ** ** **A** **Option** ** ** **B** **EVSRC** **Option** ** ** **A** **Option** ** ** **B**

# AD1EVT AD1EVT - - AD1EVT

# PINMMR30\[8\] = 0

N2HET1\[8\] N2HET2\[5\] $$ PINMMR30[8] = 1 $$ ePWM\_B and $$ PINMMR30[9] = 1 $$

# N2HET1\[10\] N2HET1\[27\] - - N2HET1\[27\]

$$ PINMMR30[16] = $$ RTI Compare 0 RTI Compare 0 $$ PINMMR30[16] = $$ 0 and ePWM\_A1 Interrupt Interrupt $$ PINMMR30[17] = $$

# N2HET1\[12\] N2HET1\[17\] - - N2HET1\[17\]

# PINMMR30\[24\] =

$$ PINMMR30[24] = $$ 0 and N2HET1\[14\] N2HET1\[19\] N2HET2\[1\] $$ PINMMR30[25] = $$

# PINMMR31\[0\] = 0

GIOB\[0\] N2HET1\[11\] $$ PINMMR31[0] = 1 $$ ePWM\_A2 and $$ PINMMR31[1] = 1 $$

# PINMMR31\[8\] = 0 GIOB\[1\] ePWM\_AB and $$ PINMMR31[9] = 1 $$

Copyright © 2012-2015, Texas Instruments Incorporated *Peripheral* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

**NOTE** If ADEVT, N2HET1 or GIOB is used as a trigger source, the connection to the MibADC1 module trigger input is made from the output side of the input buffer. This way, a trigger condition can be generated either by configuring the function as output onto the pad (through the mux control), or by driving the function from an external trigger source as input. If the mux control module is used to select different functionality instead of the ADEVT, N2HET1\[x\] or GIOB\[x\] signals, then care must be taken to disable these signals from triggering conversions; there is no multiplexing on the input connections.

If N2HET2\[1\], N2HET2\[5\], N2HET2\[13\], N2HET1\[11\], N2HET1\[17\] or N2HET1\[19\] is used to trigger the ADC the connection to the ADC is made directly from the N2HET module outputs. As a result, the ADC can be triggered without having to enable the signal from being output on a device terminal.

**NOTE** For the RTI compare 0 interrupt source, the connection is made directly from the output of the RTI module. That is, the interrupt condition can be used as a trigger source even if the actual interrupt is not signaled to the CPU. **7.4.2.2** **MIBADC2 Event Trigger Hookup**

**Table 7-17.** ** ** **MIBADC2** ** ** **Event Trigger Hookup**

**Trigger** ** ** **Event** ** ** **Signal** **Group** ** ** **Source** **Select,** ** ** **G1SRC,** $$ PINMMR30[0] = 0 and PINMMR30[1] = 1 $$ **Event** ** ** **#** $$ PINMMR30[0] = 1 $$ **G2SRC or** **Control** ** ** **for** **Control** ** ** **for** **(default)** **Option** ** ** **A** **Option** ** ** **B** **EVSRC** **Option** ** ** **A** **Option** ** ** **B**

# AD2EVT AD2EVT - - AD2EVT

# PINMMR31\[16\] =

$$ PINMMR31[16] = $$ 0 and N2HET1\[8\] N2HET2\[5\] ePWM\_B $$ PINMMR31[17] = $$

# N2HET1\[10\] N2HET1\[27\] - - N2HET1\[27\]

$$ PINMMR31[24] = $$ RTI Compare 0 RTI Compare 0 $$ PINMMR31[24] = $$ 0 and ePWM\_A1 Interrupt Interrupt $$ PINMMR31[25] = $$

# N2HET1\[12\] N2HET1\[17\] - - N2HET1\[17\]

# PINMMR32\[0\] = 0

N2HET1\[14\] N2HET1\[19\] $$ PINMMR32[0] = 1 $$ N2HET2\[1\] and $$ PINMMR32[1] = 1 $$

# PINMMR32\[8\] = 0

GIOB\[0\] N2HET1\[11\] $$ PINMMR32[8] = 1 $$ ePWM\_A2 and $$ PINMMR32[9] = 1 $$

# PINMMR32\[16\] =

# 0 and GIOB\[1\] ePWM\_AB $$ PINMMR32[17] = $$

*Peripheral* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

**NOTE** If AD2EVT, N2HET1 or GIOB is used as a trigger source, the connection to the MibADC2 module trigger input is made from the output side of the input buffer. This way, a trigger condition can be generated either by configuring the function as output onto the pad (through the mux control), or by driving the function from an external trigger source as input. If the mux control module is used to select different functionality instead of the AD2EVT, N2HET1\[x\] or GIOB\[x\] signals, then care must be taken to disable these signals from triggering conversions; there is no multiplexing on the input connections.

If N2HET1\[11\], N2HET1\[17\] or N2HET1\[19\] is used to trigger the ADC the connection to the ADC is made directly from the N2HET module outputs. As a result, the ADC can be triggered without having to enable the signal from being output on a device terminal.

**NOTE** For the RTI compare 0 interrupt source, the connection is made directly from the output of the RTI module. That is, the interrupt condition can be used as a trigger source even if the actual interrupt is not signaled to the CPU.

**7.4.2.3** **Controlling ADC1 and ADC2 Event Trigger Options** ** ** **Using SOC Output** ** ** **from ePWM** ** ** **Modules**

As shown in Figure 7-5, the ePWMxSOCA and ePWMxSOCB outputs from each ePWM module are used to generate 4 signals - ePWM\_B, ePWM\_A1, ePWM\_A2 and ePWM\_AB, that are available to trigger the ADC based on the application requirement.

Copyright © 2012-2015, Texas Instruments Incorporated *Peripheral* * * *Information and Electrical Specifications* *Submit Documentation Feedback* EPWM2 module

# EPWM2SOCA

# EPWM2SOCB EPWM1 module

# EPWM1SOCA

# EPWM1SOCB EPWM3 module

# EPWM3SOCA

# EPWM3SOCB EPWM4 module

# EPWM4SOCA

# EPWM4SOCB EPWM5 module

# EPWM5SOCA

# EPWM5SOCB EPWM6 module

# EPWM6SOCA

# EPWM6SOCB

# EPWM7SOCA EPWM7SOCB EPWM7 module

# ePWM\_B ePWM\_A1 ePWM\_A2 ePWM\_AB

SOCAEN, SOCBEN bits inside ePWMx modules Controlled by PINMMR

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

**Figure 7-5. ADC Trigger Source Generation from ePWMx**

*Peripheral* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## Table 7-18. Control Bit to SOC Output **Control** ** ** **Bit** **SOC Output**

# PINMMR35\[0\] SOC1A\_SEL

# PINMMR35\[8\] SOC2A\_SEL

# PINMMR35\[16\] SOC3A\_SEL

# PINMMR35\[24\] SOC4A\_SEL

# PINMMR36\[0\] SOC5A\_SEL

# PINMMR36\[8\] SOC6A\_SEL

# PINMMR36\[16\] SOC7A\_SEL

## The SOCA output from each ePWM module is connected to a "switch" shown in Figure 7-5.

## The logic equations for the 4 outputs from the combinational logic shown in Figure 7-5 are

# ePWM\_ SOC1B or SOC2B or SOC3B or SOC4B or SOC5B or SOC6B or SOC7B $$ B = $$

ePWM\_ \[ SOC1A and not(SOC1A\_SEL) \] or \[ SOC2A and not(SOC2A\_SEL) \] or \[ SOC3A and not(SOC3A\_SEL) \] or $$ A1 = $$

\[ SOC4A and not(SOC4A\_SEL) \] or \[ SOC5A and not(SOC5A\_SEL) \] or \[ SOC6A and not(SOC6A\_SEL) \] or \[ SOC7A and not(SOC7A\_SEL) \]

ePWM\_ \[ SOC1A and SOC1A\_SEL \] or \[ SOC2A and SOC2A\_SEL \] or \[ SOC3A and SOC3A\_SEL \] or $$ A2 = $$

\[ SOC4A and SOC4A\_SEL \] or \[ SOC5A and SOC5A\_SEL \] or \[ SOC6A and SOC6A\_SEL \] or

# \[ SOC7A and SOC7A\_SEL \]

# ePWM\_ ePWM\_B or ePWM\_A2 AB =

Copyright © 2012-2015, Texas Instruments Incorporated *Peripheral* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## 7.4.3

***ADC*** *** *** ***Electrical and*** *** *** ***Timing Specifications***

## Table 7-19. MibADC Recommended Operating Conditions **Parameter** **MIN** **MAX** **Unit**

| ADREFHI | A-to-D high-voltage reference source | ADREFLO | VCCAD(1) | V |
|:--- |:--- |:--- |:--- |:--- |
| ADREFLO | A-to-D low-voltage reference source | VSSAD(1) | ADREFHI | V |
| VAI | Analog input voltage | ADREFLO | ADREFHI | V |

AD REFLO A-to-D low-voltage reference source V SSAD (1) AD REFHI V V AI Analog input voltage AD REFLO AD REFHI V

I AIK Analog input clamp current (2) mA (VAI < VSSAD - 0.3 or VAI > VCCAD + 0.3)

(1) For V CCAD and V SSAD recommended operating conditions, see Section 5.4. (2) Input currents into any ADC input channel outside the specified limits could affect conversion results of other channels.

## Table 7-20. MibADC Electrical Characteristics Over Full Ranges of Recommended Operating Conditions

**Parameter** **Description/Conditions** **MIN** **Nom** **MAX** **Unit**

R mux Analog input mux onSee Figure 7-6 \Omega resistance

R samp ADC sample switch onSee Figure 7-6 \Omega resistance C mux Input mux capacitance See Figure 7-6 pF

C samp ADC sample capacitance See Figure 7-6 pF

I AIL Analog off-state input VCCAD = 3.6V VSSAD \leqVIN < VSSAD + 100mV nA leakage current maximum V SSAD + 100mV ≤ V IN ≤ V CCAD - 200mV nA

# VCCAD - 200mV \< VIN \\leqVCCAD nA

I AIL Analog off-state input VCCAD = 5.5V VSSAD \leqVIN < VSSAD + 300mV nA leakage current maximum V SSAD + 300mV ≤ V IN ≤ V CCAD - 300mV nA

# VCCAD - 300mV \< VIN \\leqVCCAD nA

I AOSB1 (1) ADC1 Analog on-state input VCCAD = 3.6V VSSAD \leqVIN < VSSAD + 100mV µA bias current maximum VSSAD + 100mV < VIN < VCCAD - 200mV µA

# VCCAD - 200mV \< VIN \< VCCAD µA

I AOSB2 (1) ADC2 Analog on-state input VCCAD = 3.6V VSSAD \leqVIN < VSSAD + 100mV µA bias current maximum V SSAD + 100mV ≤ V IN ≤ V CCAD - 200mV µA

# VCCAD - 200mV \< VIN \\leqVCCAD µA

I AOSB1 (1) ADC1 Analog on-state input VCCAD = 5.5V VSSAD \leqVIN < VSSAD + 300mV µA bias current maximum V SSAD + 300mV ≤ V IN ≤ V CCAD - 300mV µA

# VCCAD - 300mV \< VIN \\leqVCCAD µA

I AOSB2 (1) ADC2 Analog on-state input VCCAD = 5.5V VSSAD \leqVIN < VSSAD + 300mV µA bias current maximum V SSAD + 300mV ≤ V IN ≤ V CCAD - 300mV µA

# VCCAD - 300mV \< VIN \\leqVCCAD µA

# I ADREFHI

AD REFHI input current AD REFHI = V CCAD, AD REFLO = V SSAD mA

I CCAD Static supply current Normal operating mode mA ADC core in power down mode µA

(1) If a shared channel is being converted by both ADC converters at the same time, the on-state leakage is equal to I AOSB1 + I AOSB2

*Peripheral* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# V S1 On-State Bias Current Off-State Leakages

# V S2

# V S24

# I AOSB

# I AIL

# I AIL R ext R ext R ext P in S mux R mux P in S mux R mux P in S mux R mux S samp R samp C samp C ext I AIL

# I AIL I AIL

# I AIL C mux C ext C ext

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## Figure 7-6. MibADC Input Equivalent Circuit

## Table 7-21. MibADC Timing Specifications

**Parameter** **MIN** **NOM** **MAX** **Unit**

t c(ADCLK) (1) Cycle time, MibADC clock 0.033 µs

t d(SH) (2) Delay time, sample and hold 0.2 µs time

t d(PU-ADV) Delay time from ADC power on µs until first input can be sampled **12-bit mode** t d©) Delay time, conversion time 0.4 µs

t d(SHC) (3) Delay time, total sample/hold 0.6 µs and conversion time **10-bit mode** t d©) Delay time, conversion time 0.33 µs

t d(SHC) (3) Delay time, total sample/hold 0.53 µs and conversion time

(1) The MibADC clock is the ADCLK, generated by dividing down the VCLK by a prescale factor defined by the ADCLOCKCR register bits 4:0. (2) The sample and hold time for the ADC conversions is defined by the ADCLK frequency and the AD\<GP\>SAMP register for each conversion group. The sample time needs to be determined by accounting for the external impedance connected to the input channel as well as the ADC's internal impedance. (3) This is the minimum sample/hold and conversion time that can be achieved. These parameters are dependent on many factors, for example, the prescale settings.

Copyright © 2012-2015, Texas Instruments Incorporated *Peripheral* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## Table 7-22. MibADC Operating Characteristics Over Full Ranges of Recommended Operating **Conditions** **(1)(2)**

**Parameter** **Description/Conditions** **MIN** **Type** **MAX** **Unit**

CR Conversion range over AD REFHI - AD REFLO 5.5 V which specified accuracy is maintained

Z SET Zero Scale Offset Difference between the first ideal transition 10-bit LSB (from code 000h to 001h) and the actual mode transition 12-bit LSB mode

F SET Full Scale Offset Difference between the range of the 10-bit LSB measured code transitions (from first to last) mode and the range of the ideal code transitions 12-bit LSB mode

E DNL Differential Difference between the actual step width and 10-bit \pm 1.5 LSB nonlinearity error the ideal value. (See Figure 7-7 ) mode 12-bit \pm 2 LSB mode

E INL Integral nonlinearity Maximum deviation from the best straight line 10-bit \pm 2 LSB error through the MibADC. MibADC transfer mode characteristics, excluding the quantization 12-bit \pm 2 LSB error. mode

E TOT Total unadjusted error Maximum value of the difference between an 10-bit \pm 2 LSB analog value and the ideal midstep value. mode 12-bit \pm 4 LSB mode

(1) 1 LSB = (ADREFHI - ADREFLO)/ 212 for 12-bit mode (2) 1 LSB = (ADREFHI - ADREFLO)/ 210 for 10-bit mode

*Peripheral* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback* **Differential Linearity** **Error (-½ LSB)**

# 1 LSB

# 1 LSB **Differential Linearity** **Error (-½ LSB)** **0... 110** **0... 101** **0... 100** **0... 011** **0... 010** **0... 001** **0... 000** **Digital Output Code** **Analog Input Value (LSB)**

# NOTE A: 1 LSB = (AD - AD         )/2 REFHI REFLO

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 7.4.4

***Performance*** *** *** ***(Accuracy)*** *** *** ***Specifications*** **7.4.4.1** **MibADC Nonlinearity Errors**

The differential nonlinearity error shown in Figure 7-7 (sometimes referred to as differential linearity) is the difference between an actual step width and the ideal value of 1 LSB.

**Figure 7-7. Differential** ** ** **Nonlinearity** ** ** **(DNL)** ** ** **Error**

Copyright © 2012-2015, Texas Instruments Incorporated *Peripheral* * * *Information and Electrical Specifications* *Submit Documentation Feedback* **0... 111** **0... 101** **0... 100** **0... 011** **0... 010** **0... 001** **0... 000** **Digital Output Code** **Analog Input Value (LSB)** **0... 110** **At Transition** **011/100** **(-½ LSB)**

| At Transition | 001/010 (-1/4 LSB) |
|:--- |:--- |
| Actual | Transition |
| Ideal | Transition | **Actual** **Transition** **Ideal** **Transition** **End-Point Lin. Error**

# NOTE A: 1 LSB = (AD - AD         )/2 REFHI REFLO

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

The integral nonlinearity error shown in Figure 7-8 (sometimes referred to as linearity error) is the deviation of the values on the actual transfer function from a straight line.

**Figure 7-8. Integral** ** ** **Nonlinearity** ** ** **(INL)** ** ** **Error**

*Peripheral* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback* **0... 111** **0... 101** **0... 100** **0... 011** **0... 010** **0... 001** **0... 000** **Digital Output Code** **Analog Input Value (LSB)** **0... 110**

**Total Error** **At Step** **0... 001 (1/2 LSB)**

**Total Error** **At Step 0... 101** **(-1 1/4 LSB)**

# NOTE A: 1 LSB = (AD - AD         )/2 REFHI REFLO

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **7.4.4.2** **MibADC Total Error**

The absolute accuracy or total error of an MibADC as shown in Figure 7-9 is the maximum value of the difference between an analog value and the ideal midstep value.

**Figure 7-9. Absolute Accuracy (Total)** ** ** **Error**

Copyright © 2012-2015, Texas Instruments Incorporated *Peripheral* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

| SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 | www.ti.com |
|:--- |:--- |
| 7.5 | General-Purpose Input/Output |
| The GPIO module on this device supports two ports, GIOA and GIOB. The I/O pins are bidirectional and | bit-programmable. Both GIOA and GIOB support external interrupt capability. |
| 7.5.1 | Features | **7.5** **General-Purpose Input/Output**

The GPIO module on this device supports two ports, GIOA and GIOB. The I/O pins are bidirectional and bit-programmable. Both GIOA and GIOB support external interrupt capability. ***7.5.1*** ***Features***

The GPIO module has the following features: - • Each IO pin can be configured as: - - Input - - Output - - Open Drain - • The interrupts have the following characteristics: - - Programmable interrupt detection either on both edges or on a single edge (set in GIOINTDET) - - Programmable edge-detection polarity, either rising or falling edge (set in GIOPOL register) - - Individual interrupt flags (set in GIOFLG register) - - Individual interrupt enables, set and cleared through GIOENASET and GIOENACLR registers respectively - - Programmable interrupt priority, set through GIOLVLSET and GIOLVLCLR registers - • Internal pullup/pulldown allows unused I/O pins to be left unconnected

For information on input and output timings see Section 5.11 and Section 5.12

*Peripheral* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

**7.6** **Enhanced High-End** ** ** **Timer (N2HET)**

The N2HET is an advanced intelligent timer that provides sophisticated timing functions for real-time applications. The timer is software-controlled, using a reduced instruction set, with a specialized timer micromachine and an attached I/O port. The N2HET can be used for pulse width modulated outputs, capture or compare inputs, or general-purpose I/O. It is especially well suited for applications requiring multiple sensor information and drive actuators with complex and accurate time pulses. ***7.6.1*** ***Features***

The N2HET module has the following features: - • Programmable timer for input and output timing functions - • Reduced instruction set (30 instructions) for dedicated time and angle functions - • 160 words of instruction RAM protected by parity - • User defined number of 25-bit virtual counters for timer, event counters and angle counters - • 7-bit hardware counters for each pin allow up to 32-bit resolution in conjunction with the 25-bit virtual counters - • Up to 32 pins usable for input signal measurements or output signal generation - • Programmable suppression filter for each input pin with adjustable limiting frequency - • Low CPU overhead and interrupt load - • Efficient data transfer to or from the CPU memory with dedicated High-End-Timer Transfer Unit (HTU) or DMA - • Diagnostic capabilities with different loopback mechanisms and pin status read back functionality

***7.6.2*** ***N2HET*** *** *** ***RAM*** *** *** ***Organization***

The timer RAM uses 4 RAM banks, where each bank has two port access capability. This means that one RAM address may be written while another address is read. The RAM words are 96-bits wide, which are split into three 32-bit fields (program, control, and data).

Copyright © 2012-2015, Texas Instruments Incorporated *Peripheral* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# NHET\_LOOP\_SYNC EXT\_LOOP\_SYNC

# EXT\_LOOP\_SYNC NHET\_LOOP\_SYNC N2HET1 N2HET2

# N2HETx

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

***7.6.3*** ***Input*** *** *** ***Timing Specifications***

All of the N2HET channels have an enhanced pulse capture circuit. The N2HET instructions PCNT and WCAP use this circuit to achieve the input timing requirements shown in Figure 7-10 and Table 7-23 below.

**Figure 7-10.** ** ** **N2HET Input Capture Timings**

**Table** ** ** **7-23. Input Timing Requirements for N2HET Channels with** ** ** **Enhanced Pulse Capture**

# PARAMETER **MIN** **MAX** **UNIT**

1, 2 Input signal period, PCNT or WCAP (HRP) (LRP) tc (VCLK2) + 2 2 25 (HRP) (LRP) tc (VCLK2) - 2 ns

Input signal high phase, PCNT or WCAP 2 (HRP) tc (VCLK2) + 2 2 25 (HRP) (LRP) tc (VCLK2) - 2 ns

Input signal low phase, PCNT or WCAP 2 (HRP) tc (VCLK2) + 2 2 25 (HRP) (LRP) tc (VCLK2) - 2 ns

***7.6.4*** ***N2HET1-N2HET2*** *** *** ***Synchronization***

In some applications the N2HET resolutions must be synchronized. Some other applications require a single time base to be used for all PWM outputs and input timing captures.

The N2HET provides such a synchronization mechanism. The Clk\_master/slave (HETGCR.16) configures the N2HET in master or slave mode (default is slave mode). A N2HET in master mode provides a signal to synchronize the prescalers of the slave N2HET. The slave N2HET synchronizes its loop resolution to the loop resolution signal sent by the master. The slave does not require this signal after it receives the first synchronization signal. However, anytime the slave receives the re-synchronization signal from the master, the slave must synchronize itself again..

**Figure 7-11. N2HET1 -** ** ** **N2HET2 Synchronization Hookup**

***7.6.5*** ***N2HET*** *** *** ***Checking*** **7.6.5.1** **Internal Monitoring**

To assure correctness of the high-end timer operation and output signals, the two N2HET modules can be used to monitor each other's signals as shown in Figure 7-12. The direction of the monitoring is controlled by the I/O multiplexing control module.

*Peripheral* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# N2HET1

# N2HET2 IOMM mux control signal x

# N2HET1\[1,3,5,7,9,11\] / N2HET2\[8,10,12,14,16,18\]

# N2HET1\[1,3,5,7,9,11\]

# N2HET2\[8,10,12,14,16,18\]

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **Figure 7-12.** ** ** **N2HET Monitoring**

**7.6.5.2** **Output Monitoring using Dual Clock Comparator (DCC)**

N2HET1\[31\] is connected as a clock source for counter 1 in DCC1. This allows the application to measure the frequency of the pulse-width modulated (PWM) signal on N2HET1\[31\].

Similarly, N2HET2\[0\] is connected as a clock source for counter 1 in DCC2. This allows the application to measure the frequency of the pulse-width modulated (PWM) signal on N2HET2\[0\].

Both N2HET1\[31\] and N2HET2\[0\] can be configured to be internal-only channels. That is, the connection to the DCC module is made directly from the output of the N2HETx module (from the input of the output buffer).

For more information on DCC see Section 6.7.3.

***7.6.6*** ***Disabling*** *** *** ***N2HET*** *** *** ***Outputs***

Some applications require the N2HET outputs to be disabled under some fault condition. The N2HET module provides this capability through the "Pin Disable" input signal. This signal, when driven low, causes the N2HET outputs identified by a programmable register (HETPINDIS) to be tri-stated. For more details on the "N2HET Pin Disable" feature, see the device-specific Terminal Reference Manual.

GIOA\[5\] is connected to the "Pin Disable" input for N2HET1, and GIOB\[2\] is connected to the "Pin Disable" input for N2HET2.

Copyright © 2012-2015, Texas Instruments Incorporated *Peripheral* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## 7.6.7

***High-End*** *** *** ***Timer Transfer*** *** *** ***Unit (HTU)***

A High End Timer Transfer Unit (HTU) can perform DMA type transactions to transfer N2HET data to or from main memory. A Memory Protection Unit (MPU) is built into the HTU. **7.6.7.1** **Features**

- • CPU and DMA independent - • Master Port to access system memory - • 8 control packets supporting dual buffer configuration - • Control packet information is stored in RAM protected by parity - • Event synchronization (HET transfer requests) - • Supports 32 or 64 bit transactions - • Addressing modes for HET address (8 byte or 16 byte) and system memory address (fixed, 32 bit or 64bit) - • One shot, circular and auto switch buffer transfer modes - • Request lost detection **7.6.7.2** **Trigger** ** ** **Connections** **Table 7-24. HTU1 Request Line Connection**

| Modules | Request Source | HTU1 Request |
|:--- |:--- |:--- |
| N2HET1 | HTUREQ\[0\] | HTU1 DCP\[0\] |
| N2HET1 | HTUREQ\[1\] | HTU1 DCP\[1\] |
| N2HET1 | HTUREQ\[2\] | HTU1 DCP\[2\] |
| N2HET1 | HTUREQ\[3\] | HTU1 DCP\[3\] |
| N2HET1 | HTUREQ\[4\] | HTU1 DCP\[4\] |
| N2HET1 | HTUREQ\[5\] | HTU1 DCP\[5\] |
| N2HET1 | HTUREQ\[6\] | HTU1 DCP\[6\] |
| N2HET1 | HTUREQ\[7\] | HTU1 DCP\[7\] |

# N2HET1 HTUREQ\[0\] HTU1 DCP\[0\]

# N2HET1 HTUREQ\[1\] HTU1 DCP\[1\]

# N2HET1 HTUREQ\[2\] HTU1 DCP\[2\]

# N2HET1 HTUREQ\[3\] HTU1 DCP\[3\]

# N2HET1 HTUREQ\[4\] HTU1 DCP\[4\]

# N2HET1 HTUREQ\[5\] HTU1 DCP\[5\]

# N2HET1 HTUREQ\[6\] HTU1 DCP\[6\]

# N2HET1 HTUREQ\[7\] HTU1 DCP\[7\]

**Table 7-25. HET TU2 Request Line Connection**

| Modules | Request Source | HET TU2 Request |
|:--- |:--- |:--- |
| N2HET2 | HTUREQ\[0\] | HTU2 DCP\[0\] |
| N2HET2 | HTUREQ\[1\] | HTU2 DCP\[1\] |
| N2HET2 | HTUREQ\[2\] | HTU2 DCP\[2\] |
| N2HET2 | HTUREQ\[3\] | HTU2 DCP\[3\] |
| N2HET2 | HTUREQ\[4\] | HTU2 DCP\[4\] |
| N2HET2 | HTUREQ\[5\] | HTU2 DCP\[5\] |
| N2HET2 | HTUREQ\[6\] | HTU2 DCP\[6\] |
| N2HET2 | HTUREQ\[7\] | HTU2 DCP\[7\] |
| Peripheral Information and Electrical Specifications | Copyright © 2012-2015, Texas Instruments Incorporated | Submit Documentation Feedback |

# N2HET2 HTUREQ\[0\] HTU2 DCP\[0\]

# N2HET2 HTUREQ\[1\] HTU2 DCP\[1\]

# N2HET2 HTUREQ\[2\] HTU2 DCP\[2\]

# N2HET2 HTUREQ\[3\] HTU2 DCP\[3\]

# N2HET2 HTUREQ\[4\] HTU2 DCP\[4\]

# N2HET2 HTUREQ\[5\] HTU2 DCP\[5\]

# N2HET2 HTUREQ\[6\] HTU2 DCP\[6\]

# N2HET2 HTUREQ\[7\] HTU2 DCP\[7\]

*Peripheral* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# V CCIO **0.6\*V** **CCIO**

# 0.4\*V CCIO **Input** **t** **pw**

# 0.6\*V CCIO

# 0.4\*V CCIO

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **7.7** **FlexRay Interface**

The FlexRay module performs communication according to the FlexRay protocol specification v2.1. The sample clock bitrate can be programmed to values up to 10 MBit per second. Additional bus driver (BD) hardware is required for connection to the physical layer.

For communication on a FlexRay network, individual message buffers with up to 254 data bytes are configurable. The message storage consists of a single-ported message RAM that holds up to 128 message buffers. All functions concerning the handling of messages are implemented in the message handler. Those functions are the acceptance filtering, the transfer of messages between the two FlexRay Channel Protocol Controllers and the message RAM, maintaining the transmission schedule as well as providing message status information.

The register set of the FlexRay module can be accessed directly by the CPU via the VBUS interface. These registers are used to control, configure and monitor the FlexRay channel protocol controllers, message handler, global time unit, system universal control, frame/symbol processing, network management, interrupt control, and to access the message RAM via the input / output buffer. ***7.7.1*** ***Features***

The FlexRay module has the following features: - • Conformance with FlexRay protocol specification v2.1 - • Data rates of up to 10 Mbit/s on each channel - • Up to 128 message buffers - • 8 Kbyte of message RAM for storage of, for example, 128 message buffers with a maximum 48 byte data section or up to 30 message buffers with 254 byte data section - • Configuration of message buffers with different payload lengths - • One configurable receive FIFO - • Each message buffer can be configured as receive buffer, as transmit buffer or as part of the receive FIFO - • CPU access to message buffers via input and output buffer - • FlexRay Transfer Unit (FTU) for automatic data transfer between data memory and message buffers without CPU interaction - • Filtering for slot counter, cycle counter, and channel ID - • Maskable module interrupts - • Supports Network Management

***7.7.2*** ***Electrical and*** *** *** ***Timing Specifications***

**Table 7-26. Timing Requirements for FlexRay** ** ** **Inputs** **Parameter** **MIN** **MAX** **UNIT**

t pw Input minimum pulse width to meet the FlexRay sampling t c(VCLKA2) + 2.5 (1) ns requirement (1) t RxAsymDelay parameter **Figure 7-13.** ** ** **FlexRay Inputs**

Copyright © 2012-2015, Texas Instruments Incorporated *Peripheral* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

**Table 7-27.** ** ** **FlexRay** ** ** **Jitter** ** ** **Timing** **(1)** **Parameter** **MIN** **MAX** **Unit** t Tx1bit Clock jitter and signal symmetry ns

t Tx10bit FlexRay BSS (byte start sequence) to BSS ns

t Tx10bitAvg Average over 10000 samples 999.5 1000.5 ns

t RxAsymDelay (2) Delay difference between rise and fall from Rx pin to sample - - 2.5 ns point in FlexRay core

t jit(SCLK) Jitter for the 80MHz Sample Clock generated by the PLL - - 0.5 ns

(1) This parameter will be characterized, but not production-tested. (2) This value is based on design simulation.

***7.7.3*** ***FlexRay Transfer*** *** *** ***Unit***

The FlexRay Transfer Unit is able to transfer data between the input buffer (IBF) and output buffer (OBF) of the communication controller and the system memory without CPU interaction.

Because the FlexRay module is accessed through the FTU, the FTU must be powered up by the setting bit 23 in the Peripheral Power Down Registers of the System Module before accessing any FlexRay module register.

For more information on the FTU refer to the TMS570LS12x/11x Technical Reference Manual ( SPNU515 ).

*Peripheral* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **7.8** **Controller Area Network (DCAN)**

The DCAN supports the CAN 2.0B protocol standard and uses a serial, multimaster communication protocol that efficiently supports distributed real-time control with robust communication rates of up to 1 megabit per second (Mbps). The DCAN is ideal for applications operating in noisy and harsh environments (for example, automotive and industrial fields) that require reliable serial communication or multiplexed wiring. ***7.8.1*** ***Features***

Features of the DCAN module include: - • Supports CAN protocol version 2.0 part A, B - • Bit rates up to 1 MBit/s - • The CAN kernel can be clocked by the oscillator for baud-rate generation. - • 64 mailboxes on each DCAN - • Individual identifier mask for each message object - • Programmable FIFO mode for message objects - • Programmable loop-back modes for self-test operation - • Automatic bus on after Bus-Off state by a programmable 32-bit timer - • Message RAM protected by parity - • Direct access to Message RAM during test mode - • CAN Rx / Tx pins configurable as general purpose IO pins - • Message RAM Auto Initialization - • DMA support

For more information on the DCAN see the TMS570LS12x/11x Technical Reference Manual ( SPNU515 ).

***7.8.2*** ***Electrical and*** *** *** ***Timing Specifications***

**Table 7-28. Dynamic Characteristics** ** ** **for the DCANx TX and RX pins** **Parameter** **MIN** **MAX** **Unit**

t d(CANnTX) Delay time, transmit shift register to CANnTX pin (1) ns

t d(CANnRX) Delay time, CANnRX pin to receive shift register ns

(1) These values do not include rise/fall times of the output buffer.

Copyright © 2012-2015, Texas Instruments Incorporated *Peripheral* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

| SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 | www.ti.com |
|:--- |:--- |
| 7.9 | Local Interconnect Network Interface (LIN) |
| The SCI/LIN module can be programmed to work either as an SCI or as a LIN. The core of the module is | an SCI. The SCI's hardware features are augmented to achieve LIN compatibility. |

**7.9** **Local** ** ** **Interconnect** ** ** **Network Interface** ** ** **(LIN)**

The SCI/LIN module can be programmed to work either as an SCI or as a LIN. The core of the module is an SCI. The SCI's hardware features are augmented to achieve LIN compatibility.

The SCI module is a universal asynchronous receiver-transmitter that implements the standard nonreturn to zero format. The SCI can be used to communicate, for example, through an RS-232 port or over a Kline.

The LIN standard is based on the SCI (UART) serial data link format. The communication concept is single-master/multiple-slave with a message identification for multi-cast transmission between any network nodes. ***7.9.1*** ***LIN*** *** *** ***Features***

The following are features of the LIN module: - • Compatible to LIN 1.3, 2.0 and 2.1 protocols - • Multibuffered receive and transmit units DMA capability for minimal CPU intervention - • Identification masks for message filtering - • Automatic Master Header Generation - - Programmable Synch Break Field - - Synch Field - - Identifier Field - • Slave Automatic Synchronization - - Synch break detection - - Optional baudrate update - - Synchronization Validation - • 2 31 programmable transmission rates with 7 fractional bits - • Error detection - • 2 Interrupt lines with priority encoding

*Peripheral* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

| www.ti.com | SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 |
|:--- |:--- |
| 7.10 | Serial Communication Interface (SCI) |
| 7.10.1 | Features |

## 7.10

**Serial Communication** ** ** **Interface** ** ** **(SCI)**

## 7.10.1 ***Features***

- • Standard universal asynchronous receiver-transmitter (UART) communication - • Supports full- or half-duplex operation - • Standard nonreturn to zero (NRZ) format - • Double-buffered receive and transmit functions - • Configurable frame format of 3 to 13 bits per character based on the following: - - Data word length programmable from one to eight bits - - Additional address bit in address-bit mode - - Parity programmable for zero or one parity bit, odd or even parity - - Stop programmable for one or two stop bits - • Asynchronous or isosynchronous communication modes - • Two multiprocessor communication formats allow communication between more than two devices. - • Sleep mode is available to free CPU resources during multiprocessor communication. - • The 24-bit programmable baud rate supports 2 24 different baud rates provide high accuracy baud rate selection. - • Four error flags and Five status flags provide detailed information regarding SCI events. - • Capability to use DMA for transmit and receive data.

Copyright © 2012-2015, Texas Instruments Incorporated *Peripheral* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

**7.11** **Inter-Integrated** ** ** **Circuit (I2C)**

The inter-integrated circuit (I2C) module is a multi-master communication module providing an interface between the microcontroller and devices compliant with Philips Semiconductor I2C-bus specification version 2.1 and connected by an I2C-bus. This module will support any slave or master I2C compatible device. ***7.11.1*** ***Features***

The I2C has the following features: - • Compliance to the Philips I2C bus specification, v2.1 (The I2C Specification, Philips document number 9398 393 40011) - - Bit/Byte format transfer - - 7-bit and 10-bit device addressing modes - - General call - - START byte - - Multi-master transmitter/ slave receiver mode - - Multi-master receiver/ slave transmitter mode - - Combined master transmit/receive and receive/transmit mode - - Transfer rates of 10 kbps up to 400 kbps (Phillips fast-mode rate) - • Free data format - • Two DMA events (transmit and receive) - • DMA event enable/disable capability - • Seven interrupts that can be used by the CPU - • Module enable/disable capability - • The SDA and SCL are optionally configurable as general purpose I/O - • Slew rate control of the outputs - • Open drain control of the outputs - • Programmable pullup/pulldown capability on the inputs - • Supports Ignore NACK mode

**NOTE** This I2C module does not support: - • High-speed (HS) mode - • C-bus compatibility mode - • The combined format in 10-bit address mode (the I2C sends the slave address second byte every time it sends the slave address first byte)

*Peripheral* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# SDA

# SCL t w(SDAH) t w(SCLL) t w(SCLH) t w(SP)

# t h(SCLL-SDAL)

# t h(SDA-SCLL) t h(SCLL-SDAL) t su(SCLH-SDAL) t f(SCL) t c(SCL) t r(SCL) t su(SCLH-SDAH) Stop Start Repeated Start Stop

# t su(SDA-SCLH)

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 7.11.2

***I2C*** *** *** ***I/O Timing Specifications***

## Table 7-29. I2C Signals (SDA and SCL) Switching Characteristics (1)

**Parameter** **Standard Mode** **Fast Mode** **Unit**

# MIN **MAX** **MIN** **MAX**

t c(I2CCLK) Cycle time, Internal Module clock for I2C, 75.2 75.2 ns prescaled from VCLK f (SCL) SCL Clock frequency kHz t c(SCL) Cycle time, SCL 2.5 µs

t su(SCLH-SDAL) Setup time, SCL high before SDA low (for a 4.7 0.6 µs repeated START condition)

t h(SCLL-SDAL) Hold time, SCL low after SDA low (for a repeated 0.6 µs START condition) t w(SCLL) Pulse duration, SCL low 4.7 1.3 µs t w(SCLH) Pulse duration, SCL high 0.6 µs

t su(SDA-SCLH) Setup time, SDA valid before SCL high ns

| th(SDA-SCLL) | Hold time, SDA valid after SCL low (for I2C bus | 3.45(2) | 0.9 | µs | devices) |
|:--- |:--- | ---: | ---: |:--- |:--- |
| tw(SDAH) | Pulse duration, SDA high between STOP and | 4.7 | 1.3 | µs | START conditions |
| tsu(SCLH-SDAH) | Setup time, SCL high before SDA high (for STOP | 4.0 | 0.6 | µs | condition) |

t w(SDAH) Pulse duration, SDA high between STOP and 4.7 1.3 µs START conditions

t su(SCLH-SDAH) Setup time, SCL high before SDA high (for STOP 4.0 0.6 µs condition)

t w(SP) Pulse duration, spike (must be suppressed) ns C b (3) Capacitive load for each bus line pF

(1) The I2C pins SDA and SCL do not feature fail-safe I/O buffers. These pins could potentially draw current when the device is powered down. (2) The maximum t h(SDA-SCLL) for I2C bus devices has only to be met if the device does not stretch the low period (t w(SCLL) ) of the SCL signal. (3) C b = The total capacitance of one bus line in pF.

## Figure 7-14. I2C Timings

Copyright © 2012-2015, Texas Instruments Incorporated *Peripheral* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

**NOTE** - • A device must internally provide a hold time of at least 300 ns for the SDA signal (referred to the VIHmin of the SCL signal) to bridge the undefined region of the falling edge of SCL. - • The maximum t h(SDA-SCLL) has only to be met if the device does not stretch the LOW period (t w(SCLL) ) of the SCL signal. - • A Fast-mode I2C-bus device can be used in a Standard-mode I2C-bus system, but the requirement t su(SDA-SCLH) ≥ 250 ns must then be met. This will automatically be the case if the device does not stretch the LOW period of the SCL signal. If such a device does stretch the LOW period of the SCL signal, it must output the next data bit to the SDA line tr max + t su(SDA-SCLH). - • C b = total capacitance of one bus line in pF. If mixed with fast-mode devices, faster falltimes are allowed.

*Peripheral* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

**7.12** **Multibuffered** ** ** **/** ** ** **Standard Serial Peripheral** ** ** **Interface**

The MibSPI is a high-speed synchronous serial input/output port that allows a serial bit stream of programmed length (2 to 16 bits) to be shifted in and out of the device at a programmed bit-transfer rate. Typical applications for the SPI include interfacing to external peripherals, such as I/Os, memories, display drivers, and analog-to-digital converters. ***7.12.1*** ***Features***

Both Standard and MibSPI modules have the following features: - • 16-bit shift register - • Receive buffer register - • 8-bit baud clock generator - • SPICLK can be internally-generated (master mode) or received from an external clock source (slave mode) - • Each word transferred can have a unique format - • SPI I/Os not used in the communication can be used as digital input/output signals

**Table 7-30. MibSPI/SPI** ** ** **Configurations PGE Package**

| MibSPIx/SPIx | I/Os |
|:--- |:--- |
| MibSPI1 | MIBSPI1SIMO\[1:0\], MIBSPI1SOMI\[1:0\], MIBSPI1CLK, MIBSPI1nCS\[5:4,2:0\], MIBSPI1nENA |
| MibSPI3 | MIBSPI3SIMO\[0\], MIBSPI3SOMI\[0\], MIBSPI3CLK, MIBSPI3nCS\[5:0\], MIBSPI3nENA |
| MibSPI5 | MIBSPI5SIMO\[0\], MIBSPI5SOMI\[2:0\], MIBSPI5CLK, MIBSPI5nCS\[0\], MIBSPI5nENA |
| SPI4 | SPI4SIMO\[0\], SPI4SOMI\[0\], SPI4CLK, SPI4nCS\[0\], SPI4nENA |

# MibSPI1

MIBSPI1SIMO\[1:0\], MIBSPI1SOMI\[1:0\], MIBSPI1CLK, MIBSPI1nCS\[5:4,2:0\], MIBSPI1nENA

# MibSPI3

MIBSPI3SIMO\[0\], MIBSPI3SOMI\[0\], MIBSPI3CLK, MIBSPI3nCS\[5:0\], MIBSPI3nENA

# MibSPI5

MIBSPI5SIMO\[0\], MIBSPI5SOMI\[2:0\], MIBSPI5CLK, MIBSPI5nCS\[0\], MIBSPI5nENA

# SPI4

SPI4SIMO\[0\], SPI4SOMI\[0\], SPI4CLK, SPI4nCS\[0\], SPI4nENA

**Table 7-31. MibSPI/SPI** ** ** **Configurations ZWT Package**

| MibSPIx/SPIx | I/Os |
|:--- |:--- |
| MibSPI1 | MIBSPI1SIMO\[1:0\], MIBSPI1SOMI\[1:0\], MIBSPI1CLK, MIBSPI1nCS\[5:0\], MIBSPI1nENA |
| MibSPI3 | MIBSPI3SIMO\[0\], MIBSPI3SOMI\[0\], MIBSPI3CLK, MIBSPI3nCS\[5:0\], MIBSPI3nENA |
| MibSPI5 | MIBSPI5SIMO\[3:0\], MIBSPI5SOMI\[3:0\], MIBSPI5CLK, MIBSPI5nCS\[3:0\], MIBSPI5nENA |
| SPI2 | SPI2SIMO\[0\], SPI2SOMI\[0\], SPI2CLK, SPI2nCS\[1:0\], SPI2nENA |
| SPI4 | SPI4SIMO\[0\], SPI4SOMI\[0\], SPI4CLK, SPI4nCS\[0\], SPI4nENA |
| 7.12.2 | MibSPI Transmit and Receive RAM Organization |

# MibSPI1

MIBSPI1SIMO\[1:0\], MIBSPI1SOMI\[1:0\], MIBSPI1CLK, MIBSPI1nCS\[5:0\], MIBSPI1nENA

# MibSPI3

MIBSPI3SIMO\[0\], MIBSPI3SOMI\[0\], MIBSPI3CLK, MIBSPI3nCS\[5:0\], MIBSPI3nENA

# MibSPI5

MIBSPI5SIMO\[3:0\], MIBSPI5SOMI\[3:0\], MIBSPI5CLK, MIBSPI5nCS\[3:0\], MIBSPI5nENA

# SPI2

SPI2SIMO\[0\], SPI2SOMI\[0\], SPI2CLK, SPI2nCS\[1:0\], SPI2nENA

# SPI4

SPI4SIMO\[0\], SPI4SOMI\[0\], SPI4CLK, SPI4nCS\[0\], SPI4nENA

***7.12.2*** ***MibSPI*** *** *** ***Transmit and*** *** *** ***Receive*** *** *** ***RAM*** *** *** ***Organization***

The Multibuffer RAM is comprised of 128 buffers. Each entry in the Multibuffer RAM consists of 4 parts: a 16-bit transmit field, a 16-bit receive field, a 16-bit control field and a 16-bit status field. The Multibuffer RAM can be partitioned into multiple transfer group with variable number of buffers each. Each MibSPIx module supports 8 transfer groups.

***7.12.3*** ***MibSPI*** *** *** ***Transmit Trigger Events***

Each of the transfer groups can be configured individually. For each of the transfer groups a trigger event and a trigger source can be chosen. A trigger event can be for example a rising edge or a permanent low level at a selectable trigger source. For example, up to 15 trigger sources are available for use by each transfer group.

Copyright © 2012-2015, Texas Instruments Incorporated *Peripheral* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**> **7.12.3.1** **MIBSPI1 Event Trigger Hookup**

**Table 7-32. MIBSPI1** ** ** **Event Trigger Hookup**

**Event** ** ** **#** **TGxCTRL** ** ** **TRIGSRC\[3:0\]** **Trigger**

| Disabled | No trigger source |
|:--- |:--- |
| EVENT0 | GIOA\[0\] |
| EVENT1 | GIOA\[1\] |
| EVENT2 | GIOA\[2\] |
| EVENT3 | GIOA\[3\] |
| EVENT4 | GIOA\[4\] |
| EVENT5 | GIOA\[5\] |
| EVENT6 | GIOA\[6\] |
| EVENT7 | GIOA\[7\] |
| EVENT8 | N2HET1\[8\] |
| EVENT9 | N2HET1\[10\] |
| EVENT10 | N2HET1\[12\] |
| EVENT11 | N2HET1\[14\] |
| EVENT12 | N2HET1\[16\] |
| EVENT13 | N2HET1\[18\] |
| EVENT14 | Internal Tick counter |

# EVENT0 GIOA\[0\]

# EVENT1 GIOA\[1\]

# EVENT2 GIOA\[2\]

# EVENT3 GIOA\[3\]

# EVENT4 GIOA\[4\]

# EVENT5 GIOA\[5\]

# EVENT6 GIOA\[6\]

# EVENT7 GIOA\[7\]

# EVENT8 N2HET1\[8\]

# EVENT9 N2HET1\[10\]

# EVENT10 N2HET1\[12\]

# EVENT11 N2HET1\[14\]

# EVENT12 N2HET1\[16\]

# EVENT13 N2HET1\[18\] EVENT14 Internal Tick counter

**NOTE** For N2HET1 trigger sources, the connection to the MibSPI1 module trigger input is made from the input side of the output buffer (at the N2HET1 module boundary). This way, a trigger condition can be generated even if the N2HET1 signal is not selected to be output on the pad.

**NOTE** For GIOx trigger sources, the connection to the MibSPI1 module trigger input is made from the output side of the input buffer. This way, a trigger condition can be generated either by selecting the GIOx pin as an output pin and selecting the pin to be a GIOx pin, or by driving the GIOx pin from an external trigger source. If the mux control module is used to select different functionality instead of the GIOx signal, then care must be taken to disable GIOx from triggering MibSPI1 transfers; there is no multiplexing on the input connections. **7.12.3.2** **MIBSPI3 Event Trigger Hookup**

**Table 7-33. MIBSPI3** ** ** **Event Trigger Hookup**

**Event** ** ** **#** **TGxCTRL** ** ** **TRIGSRC\[3:0\]** **Trigger**

| Disabled | No trigger source |
|:--- |:--- |
| EVENT0 | GIOA\[0\] |
| EVENT1 | GIOA\[1\] |
| EVENT2 | GIOA\[2\] |
| EVENT3 | GIOA\[3\] |
| EVENT4 | GIOA\[4\] |
| EVENT5 | GIOA\[5\] |
| EVENT6 | GIOA\[6\] |
| EVENT7 | GIOA\[7\] |
| EVENT8 | N2HET1\[8\] |

# EVENT0 GIOA\[0\]

# EVENT1 GIOA\[1\]

# EVENT2 GIOA\[2\]

# EVENT3 GIOA\[3\]

# EVENT4 GIOA\[4\]

# EVENT5 GIOA\[5\]

# EVENT6 GIOA\[6\]

# EVENT7 GIOA\[7\]

# EVENT8 N2HET1\[8\]

*Peripheral* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

**Table 7-33. MIBSPI3** ** ** **Event Trigger Hookup (continued)**

**Event** ** ** **#** **TGxCTRL** ** ** **TRIGSRC\[3:0\]** **Trigger**

| EVENT9 | N2HET1\[10\] |
|:--- |:--- |
| EVENT10 | N2HET1\[12\] |
| EVENT11 | N2HET1\[14\] |
| EVENT12 | N2HET1\[16\] |
| EVENT13 | N2HET1\[18\] |
| EVENT14 | Internal Tick counter |

# EVENT10 N2HET1\[12\]

# EVENT11 N2HET1\[14\]

# EVENT12 N2HET1\[16\]

# EVENT13 N2HET1\[18\] EVENT14 Internal Tick counter

**NOTE** For N2HET1 trigger sources, the connection to the MibSPI3 module trigger input is made from the input side of the output buffer (at the N2HET1 module boundary). This way, a trigger condition can be generated even if the N2HET1 signal is not selected to be output on the pad.

**NOTE** For GIOx trigger sources, the connection to the MibSPI3 module trigger input is made from the output side of the input buffer. This way, a trigger condition can be generated either by selecting the GIOx pin as an output pin and selecting the pin to be a GIOx pin, or by driving the GIOx pin from an external trigger source. If the mux control module is used to select different functionality instead of the GIOx signal, then care must be taken to disable GIOx from triggering MibSPI3 transfers; there is no multiplexing on the input connections. **7.12.3.3** **MIBSPI5 Event Trigger Hookup**

**Table 7-34. MIBSPI5** ** ** **Event Trigger Hookup** Event # TGxCTRL TRIGSRC\[3:0\] Trigger

| Disabled | No trigger source |
|:--- |:--- |
| EVENT0 | GIOA\[0\] |
| EVENT1 | GIOA\[1\] |
| EVENT2 | GIOA\[2\] |
| EVENT3 | GIOA\[3\] |
| EVENT4 | GIOA\[4\] |
| EVENT5 | GIOA\[5\] |
| EVENT6 | GIOA\[6\] |
| EVENT7 | GIOA\[7\] |
| EVENT8 | N2HET1\[8\] |
| EVENT9 | N2HET1\[10\] |
| EVENT10 | N2HET1\[12\] |
| EVENT11 | N2HET1\[14\] |
| EVENT12 | N2HET1\[16\] |
| EVENT13 | N2HET1\[18\] |
| EVENT14 | Internal Tick counter |

# EVENT0 GIOA\[0\]

# EVENT1 GIOA\[1\]

# EVENT2 GIOA\[2\]

# EVENT3 GIOA\[3\]

# EVENT4 GIOA\[4\]

# EVENT5 GIOA\[5\]

# EVENT6 GIOA\[6\]

# EVENT7 GIOA\[7\]

# EVENT8 N2HET1\[8\]

# EVENT9 N2HET1\[10\]

# EVENT10 N2HET1\[12\]

# EVENT11 N2HET1\[14\]

# EVENT12 N2HET1\[16\]

# EVENT13 N2HET1\[18\] EVENT14 Internal Tick counter

**NOTE** For N2HET1 trigger sources, the connection to the MibSPI5 module trigger input is made from the input side of the output buffer (at the N2HET1 module boundary). This way, a trigger condition can be generated even if the N2HET1 signal is not selected to be output on the pad.

Copyright © 2012-2015, Texas Instruments Incorporated *Peripheral* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

**NOTE** For GIOx trigger sources, the connection to the MibSPI5 module trigger input is made from the output side of the input buffer. This way, a trigger condition can be generated either by selecting the GIOx pin as an output pin and selecting the pin to be a GIOx pin, or by driving the GIOx pin from an external trigger source. If the mux control module is used to select different functionality instead of the GIOx signal, then care must be taken to disable GIOx from triggering MibSPI5 transfers; there is no multiplexing on the input connections.

*Peripheral* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 7.12.4

***MibSPI/SPI*** *** *** ***Master Mode*** *** *** ***I/O Timing Specifications***

## Table 7-35. SPI Master Mode External Timing Parameters (CLOCK PHASE = 0, SPICLK = output, SPISIMO

## = output, and SPISOMI = input)(1)(2)(3)

**NO.** **Parameter** **MIN** **MAX** **Unit**

t c(SPC)M Cycle time, SPICLK (4) 256t c(VCLK) ns

2 (5) t w(SPCH)M Pulse duration, SPICLK high (clock 0.5t c(SPC)M - t r(SPC)M - 3 0.5t c(SPC)M + 3 ns polarity = 0)

t w(SPCL)M Pulse duration, SPICLK low (clock 0.5t c(SPC)M - t f(SPC)M - 3 0.5t c(SPC)M + 3 polarity = 1)

3 (5) t w(SPCL)M Pulse duration, SPICLK low (clock 0.5t c(SPC)M - t f(SPC)M - 3 0.5t c(SPC)M + 3 ns polarity = 0)

t w(SPCH)M Pulse duration, SPICLK high (clock 0.5t c(SPC)M - t r(SPC)M - 3 0.5t c(SPC)M + 3 polarity = 1)

4 (5) t d(SPCH-SIMO)M Delay time, SPISIMO valid before 0.5t c(SPC)M - 6 ns SPICLK low (clock polarity = 0)

t d(SPCL-SIMO)M Delay time, SPISIMO valid before 0.5t c(SPC)M - 6 SPICLK high (clock polarity = 1)

5 (5) t v(SPCL-SIMO)M Valid time, SPISIMO data valid after 0.5t c(SPC)M - t f(SPC) - 4 ns SPICLK low (clock polarity = 0)

t v(SPCH-SIMO)M Valid time, SPISIMO data valid after 0.5t c(SPC)M - t r(SPC) - 4 SPICLK high (clock polarity = 1)

6 (5) t su(SOMI-SPCL)M Setup time, SPISOMI before SPICLK t f(SPC) + 2.2 ns low (clock polarity = 0)

t su(SOMI-SPCH)M Setup time, SPISOMI before SPICLK t r(SPC) + 2.2 high (clock polarity = 1)

7 (5) t h(SPCL-SOMI)M Hold time, SPISOMI data valid after ns SPICLK low (clock polarity = 0)

t h(SPCH-SOMI)M Hold time, SPISOMI data valid after SPICLK high (clock polarity = 1)

8 (6) t C2TDELAY Setup time CS active CSHOLD = 0 C2TDELAY\*t c(VCLK) + 2\*t c(VCLK) (C2TDELAY+2) \* t c(VCLK) ns until SPICLK high - t f(SPICS) + t r(SPC) - 7 t f(SPICS) + t r(SPC) + 5.5 (clock polarity = 0) CSHOLD = 1 C2TDELAY\*t c(VCLK) + 3\*t c(VCLK) (C2TDELAY+3) \* t c(VCLK) - t f(SPICS) + t r(SPC) - 7 t f(SPICS) + t r(SPC) + 5.5

Setup time CS active CSHOLD = 0 C2TDELAY\*t c(VCLK) + 2\*t c(VCLK) (C2TDELAY+2) \* t c(VCLK) ns until SPICLK low - t f(SPICS) + t f(SPC) - 7 t f(SPICS) + t f(SPC) + 5.5 (clock polarity = 1) CSHOLD = 1 C2TDELAY\*t c(VCLK) + 3\*t c(VCLK) (C2TDELAY+3) \* t c(VCLK) - t f(SPICS) + t f(SPC) - 7 t f(SPICS) + t f(SPC) + 5.5

9 (6) t T2CDELAY Hold time SPICLK low until CS inactive 0.5\*t c(SPC)M + 0.5\*t c(SPC)M + ns (clock polarity = 0) T2CDELAY\*t c(VCLK) + t c(VCLK) T2CDELAY\*t c(VCLK) + t c(VCLK) t f(SPC) + t r(SPICS) - 7 t f(SPC) + t r(SPICS) + 11

Hold time SPICLK high until CS 0.5\*t c(SPC)M + 0.5\*t c(SPC)M + ns inactive (clock polarity = 1) T2CDELAY\*t c(VCLK) + t c(VCLK) T2CDELAY\*t c(VCLK) + t c(VCLK) t r(SPC) + tr(SPICS) - 7 t r(SPC) + t r(SPICS) + 11

t SPIENA SPIENAn Sample point (C2TDELAY+1) \* t c(VCLK) (C2TDELAY+1)\*t c(VCLK) ns t f(SPICS) - 29

t SPIENAW SPIENAn Sample point from write to (C2TDELAY+2)\*t c(VCLK) ns buffer

(1) The MASTER bit (SPIGCR1.0) is set and the CLOCK PHASE bit (SPIFMTx.16) is cleared. (2) t c(VCLK) = interface clock cycle time = 1 / f (VCLK) (3) For rise and fall timings, see Table 5-8. (4) When the SPI is in Master mode, the following must be true: For PS values from 1 to 255: t c(SPC)M ≥ (PS +1)t c(VCLK) ≥ 40ns, where PS is the prescale value set in the SPIFMTx.\[15:8\] register bits. For PS values of 0: tc(SPC)M = 2tc(VCLK) \geq40ns. The external load on the SPICLK pin must be less than 60pF. (5) The active edge of the SPICLK signal referenced is controlled by the CLOCK POLARITY bit (SPIFMTx.17). (6) C2TDELAY and T2CDELAY is programmed in the SPIDELAY register

Copyright © 2012-2015, Texas Instruments Incorporated *Peripheral* * * *Information and Electrical Specifications* *Submit Documentation Feedback* **SPICLK** (clock polarity=0)

# SPISIMO

# SPICSn **Master Out Data Is Valid** **SPICLK** (clock polarity=1)

# SPIENAn **Write to buffer**

# SPISOMI

# SPISIMO

| SPICLK | (clock polarity = 1) |
|:--- |:--- |
| SPICLK | (clock polarity = 0) |
| Master In Data | Must Be Valid | **SPICLK** **(clock polarity = 0)** **Master In Data** **Must Be Valid** **Master Out Data Is Valid**

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## Figure 7-15. SPI Master Mode External Timing (CLOCK PHASE = 0)

## Figure 7-16. SPI Master Mode Chip Select Timing (CLOCK PHASE = 0)

*Peripheral* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## Table 7-36. SPI Master Mode External Timing Parameters (CLOCK PHASE = 1, SPICLK = output, SPISIMO

## = output, and SPISOMI = input)(1)(2)(3)

**NO.** **Parameter** **MIN** **MAX** **Unit**

t c(SPC)M Cycle time, SPICLK (4) 256t c(VCLK) ns

2 (5) t w(SPCH)M Pulse duration, SPICLK high (clock 0.5t c(SPC)M - t r(SPC)M - 3 0.5t c(SPC)M + 3 ns polarity = 0)

t w(SPCL)M Pulse duration, SPICLK low (clock 0.5t c(SPC)M - t f(SPC)M - 3 0.5t c(SPC)M + 3 polarity = 1)

3 (5) t w(SPCL)M Pulse duration, SPICLK low (clock 0.5t c(SPC)M - t f(SPC)M - 3 0.5t c(SPC)M + 3 ns polarity = 0)

t w(SPCH)M Pulse duration, SPICLK high (clock 0.5t c(SPC)M - t r(SPC)M - 3 0.5t c(SPC)M + 3 polarity = 1)

4 (5) t v(SIMO-SPCH)M Valid time, SPICLK high after 0.5t c(SPC)M - 6 ns SPISIMO data valid (clock polarity = 0)

t v(SIMO-SPCL)M Valid time, SPICLK low after 0.5t c(SPC)M - 6 SPISIMO data valid (clock polarity = 1)

5 (5) t v(SPCH-SIMO)M Valid time, SPISIMO data valid after 0.5t c(SPC)M - t r(SPC) - 4 ns SPICLK high (clock polarity = 0)

t v(SPCL-SIMO)M Valid time, SPISIMO data valid after 0.5t c(SPC)M - t f(SPC) - 4 SPICLK low (clock polarity = 1)

6 (5) t su(SOMI-SPCH)M Setup time, SPISOMI before t r(SPC) + 2.2 ns SPICLK high (clock polarity = 0)

t su(SOMI-SPCL)M Setup time, SPISOMI before t f(SPC) + 2.2 SPICLK low (clock polarity = 1)

7 (5) t v(SPCH-SOMI)M Valid time, SPISOMI data valid after ns SPICLK high (clock polarity = 0)

t v(SPCL-SOMI)M Valid time, SPISOMI data valid after SPICLK low (clock polarity = 1)

8 (6) t C2TDELAY Setup time CS CSHOLD = 0 0.5\*t c(SPC)M + 0.5\*t c(SPC)M + ns active until SPICLK (C2TDELAY+2) \* t c(VCLK) (C2TDELAY+2) \* t c(VCLK) high (clock polarity = t f(SPICS) + t r(SPC) - 7 t f(SPICS) + t r(SPC) + 5.5 0) CSHOLD = 1 0.5\*t c(SPC)M + 0.5\*t c(SPC)M + (C2TDELAY+3) \* t c(VCLK) (C2TDELAY+3) \* t c(VCLK) t f(SPICS) + t r(SPC) - 7 t f(SPICS) + t r(SPC) + 5.5

Setup time CS CSHOLD = 0 0.5\*t c(SPC)M + 0.5\*t c(SPC)M + ns active until SPICLK (C2TDELAY+2) \* t c(VCLK) (C2TDELAY+2) \* t c(VCLK) low (clock polarity = t f(SPICS) + t f(SPC) - 7 t f(SPICS) + t f(SPC) + 5.5 1) CSHOLD = 1 0.5\*t c(SPC)M + 0.5\*t c(SPC)M + (C2TDELAY+3) \* t c(VCLK) (C2TDELAY+3) \* t c(VCLK) t f(SPICS) + t f(SPC) - 7 t f(SPICS) + t f(SPC) + 5.5

9 (6) t T2CDELAY Hold time SPICLK low until CS T2CDELAY\*t c(VCLK) + T2CDELAY\*t c(VCLK) + ns inactive (clock polarity = 0) t c(VCLK) - t f(SPC) + t r(SPICS) t c(VCLK) - t f(SPC) + t r(SPICS) +

Hold time SPICLK high until CS T2CDELAY\*t c(VCLK) + T2CDELAY\*t c(VCLK) + ns inactive (clock polarity = 1) t c(VCLK) - t r(SPC) + t r(SPICS) t c(VCLK) - t r(SPC) + t r(SPICS) +

t SPIENA SPIENAn Sample Point (C2TDELAY+1)\* t c(VCLK) (C2TDELAY+1)\*t c(VCLK) ns t f(SPICS) - 29

t SPIENAW SPIENAn Sample point from write to (C2TDELAY+2)\*t c(VCLK) ns buffer

(1) The MASTER bit (SPIGCR1.0) is set and the CLOCK PHASE bit (SPIFMTx.16) is set. (2) t c(VCLK) = interface clock cycle time = 1 / f (VCLK) (3) For rise and fall timings, see the Table 5-8. (4) When the SPI is in Master mode, the following must be true: For PS values from 1 to 255: t c(SPC)M ≥ (PS +1)t c(VCLK) ≥ 40ns, where PS is the prescale value set in the SPIFMTx.\[15:8\] register bits. For PS values of 0: tc(SPC)M = 2tc(VCLK) \geq40ns. The external load on the SPICLK pin must be less than 60pF. (5) The active edge of the SPICLK signal referenced is controlled by the CLOCK POLARITY bit (SPIFMTx.17). (6) C2TDELAY and T2CDELAY is programmed in the SPIDELAY register

Copyright © 2012-2015, Texas Instruments Incorporated *Peripheral* * * *Information and Electrical Specifications* *Submit Documentation Feedback* **SPICLK** (clock polarity=0)

# SPISIMO

# SPICSn **Master Out Data Is Valid** **SPICLK** (clock polarity=1)

# SPIENAn **Write to buffer**

# SPISOMI

# SPISIMO **SPICLK** **(clock polarity = 1)** **SPICLK** **(clock polarity = 0)** **Data Valid** **Master In Data** **Must Be Valid** **Master Out Data Is Valid**

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## Figure 7-17. SPI Master Mode External Timing (CLOCK PHASE = 1)

## Figure 7-18. SPI Master Mode Chip Select Timing (CLOCK PHASE = 1)

*Peripheral* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 7.12.5

***SPI*** *** *** ***Slave Mode*** *** *** ***I/O Timings***

## Table 7-37. SPI Slave Mode External Timing Parameters (CLOCK PHASE = 0, SPICLK = input, SPISIMO =

## input, and SPISOMI = output)(1)(2)(3)(4)

**NO.** **Parameter** **MIN** **MAX** **Unit** t c(SPC)S Cycle time, SPICLK (5) ns

2 (6) t w(SPCH)S Pulse duration, SPICLK high (clock polarity = 0) ns

t w(SPCL)S Pulse duration, SPICLK low (clock polarity = 1)

3 (6) t w(SPCL)S Pulse duration, SPICLK low (clock polarity = 0) ns

t w(SPCH)S Pulse duration, SPICLK high (clock polarity = 1)

4 (6) t d(SPCH-SOMI)S Delay time, SPISOMI valid after SPICLK high (clock t rf(SOMI) + 20 ns polarity = 0)

t d(SPCL-SOMI)S Delay time, SPISOMI valid after SPICLK low (clock polarity t rf(SOMI) + 20 $$ = 1) $$

5 (6) t h(SPCH-SOMI)S Hold time, SPISOMI data valid after SPICLK high (clock ns polarity =0)

t h(SPCL-SOMI)S Hold time, SPISOMI data valid after SPICLK low (clock polarity =1)

6 (6) t su(SIMO-SPCL)S Setup time, SPISIMO before SPICLK low (clock polarity = ns 0)

t su(SIMO-SPCH)S Setup time, SPISIMO before SPICLK high (clock polarity = 1)

7 (6) t h(SPCL-SIMO)S Hold time, SPISIMO data valid after SPICLK low (clock ns polarity = 0)

t h(SPCH-SIMO)S Hold time, SPISIMO data valid after S PICLK high (clock polarity = 1)

t d(SPCL-SENAH)S Delay time, SPIENAn high after last SPICLK low (clock 1.5t c(VCLK) 2.5t c(VCLK) +t r(ENAn) + ns polarity = 0)

t d(SPCH-SENAH)S Delay time, SPIENAn high after last SPICLK high (clock 1.5t c(VCLK) 2.5t c(VCLK) + t r(ENAn) + polarity = 1)

t d(SCSL-SENAL)S Delay time, SPIENAn low after SPICSn low (if new data t f(ENAn) t c(VCLK) +t f(ENAn) +27 ns has been written to the SPI buffer)

(1) The MASTER bit (SPIGCR1.0) is cleared and the CLOCK PHASE bit (SPIFMTx.16) is cleared. (2) If the SPI is in slave mode, the following must be true: t c(SPC)S ≥ (PS + 1) t c(VCLK), where PS = prescale value set in SPIFMTx.\[15:8\]. (3) For rise and fall timings, see Table 5-8. (4) t c(VCLK) = interface clock cycle time = 1 /f (VCLK) (5) When the SPI is in Slave mode, the following must be true: For PS values from 1 to 255: t c(SPC)S ≥ (PS +1)t c(VCLK) ≥ 40ns, where PS is the prescale value set in the SPIFMTx.\[15:8\] register bits. For PS values of 0: tc(SPC)S = 2tc(VCLK) \geq40ns. (6) The active edge of the SPICLK signal referenced is controlled by the CLOCK POLARITY bit (SPIFMTx.17).

Copyright © 2012-2015, Texas Instruments Incorporated *Peripheral* * * *Information and Electrical Specifications* *Submit Documentation Feedback* **SPICLK** (clock polarity=0)

# SPICSn **SPICLK** (clock polarity=1)

# SPIENAn

# SPISOMI

| SPICLK | (clock polarity = 1) |
|:--- |:--- |
| SPICLK | (clock polarity = 0) |
| SPISIMO Data | Must Be Valid | **SPICLK** **(clock polarity = 0)** **SPISIMO** ** Data** **Must Be Valid** **SPISOMI Data Is Valid**

# SPISIMO

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## Figure 7-19. SPI Slave Mode External Timing (CLOCK PHASE = 0)

## Figure 7-20. SPI Slave Mode Enable Timing (CLOCK PHASE = 0)

*Peripheral* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## Table 7-38. SPI Slave Mode External Timing Parameters (CLOCK PHASE = 1, SPICLK = input, SPISIMO =

## input, and SPISOMI = output)(1)(2)(3)(4)

**NO.** **Parameter** **MIN** **MAX** **Unit** t c(SPC)S Cycle time, SPICLK (5) ns

2 (6) t w(SPCH)S Pulse duration, SPICLK high (clock polarity = 0) ns

t w(SPCL)S Pulse duration, SPICLK low (clock polarity = 1)

3 (6) t w(SPCL)S Pulse duration, SPICLK low (clock polarity = 0) ns

t w(SPCH)S Pulse duration, SPICLK high (clock polarity = 1)

4 (6) t d(SOMI-SPCL)S Delay time, SPISOMI data valid after SPICLK low t rf(SOMI) + 20 ns (clock polarity = 0)

t d(SOMI-SPCH)S Delay time, SPISOMI data valid after SPICLK high t rf(SOMI) + 20 (clock polarity = 1)

5 (6) t h(SPCL-SOMI)S Hold time, SPISOMI data valid after SPICLK high ns (clock polarity =0)

t h(SPCH-SOMI)S Hold time, SPISOMI data valid after SPICLK low (clock polarity =1)

6 (6) t su(SIMO-SPCH)S Setup time, SPISIMO before SPICLK high (clock ns polarity = 0)

t su(SIMO-SPCL)S Setup time, SPISIMO before SPICLK low (clock polarity $$ = 1) $$

7 (6) t v(SPCH-SIMO)S High time, SPISIMO data valid after SPICLK high ns (clock polarity = 0)

t v(SPCL-SIMO)S High time, SPISIMO data valid after SPICLK low (clock polarity = 1)

t d(SPCH-SENAH)S Delay time, SPIENAn high after last SPICLK high 1.5t c(VCLK) 2.5t c(VCLK) +t r(ENAn) + 22 ns (clock polarity = 0)

t d(SPCL-SENAH)S Delay time, SPIENAn high after last SPICLK low (clock 1.5t c(VCLK) 2.5t c(VCLK) +t r(ENAn) + 22 polarity = 1)

t d(SCSL-SENAL)S Delay time, SPIENAn low after SPICSn low (if new data t f(ENAn) t c(VCLK) +t f(ENAn) + 27 ns has been written to the SPI buffer)

t d(SCSL-SOMI)S Delay time, SOMI valid after SPICSn low (if new data t c(VCLK) 2t c(VCLK) +t rf(SOMI) + 28 ns has been written to the SPI buffer)

(1) The MASTER bit (SPIGCR1.0) is cleared and the CLOCK PHASE bit (SPIFMTx.16) is set. (2) If the SPI is in slave mode, the following must be true: tc(SPC)S ≤ (PS + 1) tc(VCLK), where PS = prescale value set in SPIFMTx.\[15:8\]. (3) For rise and fall timings, see Table 5-8. (4) t c(VCLK) = interface clock cycle time = 1 /f (VCLK) (5) When the SPI is in Slave mode, the following must be true: For PS values from 1 to 255: t c(SPC)S ≥ (PS +1)t c(VCLK) ≥ 40ns, where PS is the prescale value set in the SPIFMTx.\[15:8\] register bits. For PS values of 0: tc(SPC)S = 2tc(VCLK) \geq40ns. (6) The active edge of the SPICLK signal referenced is controlled by the CLOCK POLARITY bit (SPIFMTx.17).

Copyright © 2012-2015, Texas Instruments Incorporated *Peripheral* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# SPISOMI **Slave Out Data Is Valid** **SPICLK** (clock polarity=0)

# SPICSn **SPICLK** (clock polarity=1)

# SPIENAn

# SPISIMO

# SPISOMI **SPISIMO Data** **Must Be Valid** **SPISOMI Data Is Valid** **SPICLK** **(clock polarity = 1)** **SPICLK** **(clock polarity = 0)**

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## Figure 7-21. SPI Slave Mode External Timing (CLOCK PHASE = 1)

## Figure 7-22. SPI Slave Mode Enable Timing (CLOCK PHASE = 1)

*Peripheral* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# MII\_RX\_CLK

# MII\_RXD\[3:0\] MII\_RX\_DV MII\_RX\_ER

# VALID

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **7.13** **Ethernet Media Access Controller**

The Ethernet Media Access Controller (EMAC) provides an efficient interface between the CPU and the network. The EMAC supports both 10Base-T and 100Base-TX, or 10 Mbits/second (Mbps) and 100 Mbps in either half- or full-duplex mode, with hardware flow control and quality of service (QoS) support.

The EMAC controls the flow of packet data from the device to the PHY. The MDIO module controls PHY configuration and status monitoring.

Both the EMAC and the MDIO modules interface to the device through a custom interface that allows efficient data transmission and reception. This custom interface is referred to as the EMAC control module, and is considered integral to the EMAC/MDIO peripheral. The control module is also used to multiplex and control interrupts.

***7.13.1*** ***Ethernet MII*** *** *** ***Electrical and*** *** *** ***Timing Specifications***

**Figure 7-23.** ** ** **MII** ** ** **Receive** ** ** **Timing**

**Table 7-39. Timing Requirements for EMAC MII** ** ** **Receive**

# NO. **MIN** **MAX** **UNIT**

| tsu(MIIRXD - MIIRXCLKH) | Setup time, MII\_RXD\[3:0\] before MII\_RX\_CLK rising edge | ns |
|:--- |:--- |:--- |
| tsu(MIIRXDV - MIIRXCLKH) | Setup time, MII\_RX\_DV before MII\_RX\_CLK rising edge | ns |
| tsu(MIIRXER - MIIRXCLKH) | Setup time, MII\_RX\_ER before MII\_RX\_CLK rising edge | ns |
| th(MIIRXCLKH - MIIRXD) | Hold time, MII\_RXD\[3:0\] valid after MII\_RX\_CLK rising edge | ns |
| th(MIIRXCLKH - MIIRXDV) | Hold time, MII\_RX\_DV valid after MII\_RX\_CLK rising edge | ns |
| th(MIIRXCLKH - MIIRXER) | Hold time, MII\_RX\_ER valid after MII\_RX\_CLK rising edge | ns |
| Copyright © 2012-2015, Texas Instruments Incorporated | Peripheral Information and Electrical Specifications | Submit Documentation Feedback |

t su(MIIRXDV - MIIRXCLKH) Setup time, MII\_RX\_DV before MII\_RX\_CLK rising edge ns

t su(MIIRXER - MIIRXCLKH) Setup time, MII\_RX\_ER before MII\_RX\_CLK rising edge ns

t h(MIIRXCLKH - MIIRXD) Hold time, MII\_RXD\[3:0\] valid after MII\_RX\_CLK rising edge ns

t h(MIIRXCLKH - MIIRXDV) Hold time, MII\_RX\_DV valid after MII\_RX\_CLK rising edge ns

t h(MIIRXCLKH - MIIRXER) Hold time, MII\_RX\_ER valid after MII\_RX\_CLK rising edge ns

Copyright © 2012-2015, Texas Instruments Incorporated *Peripheral* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# MII\_TX\_CLK

# MII\_TXD\[3:0\] MII\_TXEN VALID

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## Figure 7-24. MII Transmit Timing

## Table 7-40. Switching Characteristics Over Recommended Operating Conditions for EMAC MII Transmit

# NO. **PARAMETER** **MIN** **MAX** **UNIT**

| td(MIIRXCLKH - MIITXD) | Delay time, MII\_TX\_CLK rising edge to MII\_TXD\[3:0\] valid | ns |
|:--- |:--- |:--- |
| td(MIIRXCLKH - MIITXEN) | Delay time, MII\_TX\_CLK rising edge to MII\_TXEN valid | ns |
| Peripheral Information and Electrical Specifications | Copyright © 2012-2015, Texas Instruments Incorporated | Submit Documentation Feedback |

t d(MIIRXCLKH - MIITXEN) Delay time, MII\_TX\_CLK rising edge to MII\_TXEN valid ns

*Peripheral* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# RMII\_REFCLK

# RMII\_TXEN

# RMII\_TXD\[1:0\]

# RMII\_RXD\[1:0\]

# RMII\_CRS\_DV

# RMII\_RX\_ER

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 7.13.2

***Ethernet RMII*** *** *** ***Electrical and*** *** *** ***Timing Specifications***

## Figure 7-25. RMII Timing Diagram

## Table 7-41. Timing Requirements for EMAC RMII Receive and RMII\_REFCLK

# NO. **MIN** **NOM** **MAX** **UNIT**

| tc(REFCLK) | Cycle time, RMII\_REFCLK | ns |
|:--- |:--- |:--- |
| tw(REFCLKH) | Pulse width, RMII\_REFCLK high | ns |
| tw(REFCLKL) | Pulse width, RMII\_REFCLK low | ns |
| tsu(RXD-REFCLK) | Input setup time, RMII\_RXD\[1:0\] valid before RMII\_REFCLK high | ns |
| th(REFCLK-RXD) | Input hold time, RMII\_RXD\[1:0\] valid after RMII\_REFCLK high | ns |

t w(REFCLKH) Pulse width, RMII\_REFCLK high ns t w(REFCLKL) Pulse width, RMII\_REFCLK low ns

t su(RXD-REFCLK) Input setup time, RMII\_RXD\[1:0\] valid before RMII\_REFCLK high ns

t h(REFCLK-RXD) Input hold time, RMII\_RXD\[1:0\] valid after RMII\_REFCLK high ns

t su(CRSDV-REFCLK) Input setup time, RMII\_CRS\_DV valid before RMII\_REFCLK high ns

| th(REFCLK-CRSDV) | Input hold time, RMII\_CRS\_DV valid after RMII\_REFCLK high | ns |
|:--- |:--- |:--- |
| tsu(RXER-REFCLK) | Input setup time, RMII\_RX\_ER valid before RMII\_REFCLK high | ns |
| th(REFCLK-RXER) | Input hold time, RMII\_RX\_ER valid after RMII\_REFCLK high | ns |

t su(RXER-REFCLK) Input setup time, RMII\_RX\_ER valid before RMII\_REFCLK high ns

t h(REFCLK-RXER) Input hold time, RMII\_RX\_ER valid after RMII\_REFCLK high ns

## Table 7-42. Switching Characteristics Over Recommended Operating Conditions for EMAC RMII Transmit

# NO. **PARAMETER** **MIN** **MAX** **UNIT**

| td(REFCLK-TXD) | Output delay time, RMII\_REFCLK high to RMII\_TXD\[1:0\] valid | ns |
|:--- |:--- |:--- |
| td(REFCLK-TXEN) | Output delay time, RMII\_REFCLK high to RMII\_TXEN valid | ns |
| Copyright © 2012-2015, Texas Instruments Incorporated | Peripheral Information and Electrical Specifications | Submit Documentation Feedback |

t d(REFCLK-TXEN) Output delay time, RMII\_REFCLK high to RMII\_TXEN valid ns

Copyright © 2012-2015, Texas Instruments Incorporated *Peripheral* * * *Information and Electrical Specifications* *Submit Documentation Feedback*

# MDCLK **MDIO** **(output)**

# MDCLK **MDIO** **(input)**

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## 7.13.3

***Management*** *** *** ***Data*** *** *** ***Input/Output (MDIO)***

## Figure 7-26. MDIO Input Timing

## Table 7-43. MDIO Input Timing Requirements **NO.** **Parameter** **Value** **Unit**

# MIN **MAX**

| tc(MDCLK) | Cycle time, MDCLK | -- ns |
|:--- |:--- |:--- |
| tw(MDCLK) | Pulse duration, MDCLK high/low | -- ns |
| tt(MDCLK) | Transition time, MDCLK | -- ns |

tw(MDCLK) Pulse duration, MDCLK high/low - - ns tt(MDCLK) Transition time, MDCLK - - ns

tsu(MDIO-MDCLKH) Setup time, MDIO data input valid before MDCLK 33 (1) - - ns High

th(MDCLKH-MDIO) Hold time, MDIO data input valid after MDCLK - - ns High

(1) This is a discrepancy to IEEE 802.3, but is compatible with many PHY devices.

## Figure 7-27. MDIO Output Timing

## Table 7-44. MDIO Output Timing Requirements **NO.** **Parameter** **Value** **Unit**

# MIN **MAX** tc(MDCLK) Cycle time, MDCLK - - ns

td(MDCLKL-MDIO) Delay time, MDCLK low to MDIO data output ns valid

*Peripheral* * * *Information and Electrical Specifications* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## Device and Documentation Support

**8.1** **Device and** ** ** **Development-Support** ** ** **Tool** ** ** **Nomenclature**

To designate the stages in the product development cycle, TI assigns prefixes to the part numbers of all devices and support tools. Each commercial family member has one of three prefixes: TMX, TMP, or TMS (for example,TMS570LS1227). Texas Instruments recommends two of three possible prefix designators for its support tools: TMDX and TMDS. These prefixes represent evolutionary stages of product development from engineering prototypes (TMX/TMDX) through fully qualified production devices/tools (TMS/TMDS). Device development evolutionary flow:

**TMX** Experimental device that is not necessarily representative of the final device's electrical specifications.

**TMP** Final silicon die that conforms to the device's electrical specifications but has not completed quality and reliability verification.

**TMS** Fully-qualified production device. TMX and TMP devices are shipped against the following disclaimer: "Developmental product is intended for internal evaluation purposes." TMS devices have been characterized fully, and the quality and reliability of the device have been demonstrated fully. TI's standard warranty applies. Predictions show that prototype devices (TMX or TMP) have a greater failure rate than the standard production devices. Texas Instruments recommends that these devices not be used in any production system because their expected end-use failure rate still is undefined. Only qualified production devices are to be used.

The figure below illustrates the numbering and symbol nomenclature for the TMS570LS1227.

Copyright © 2012-2015, Texas Instruments Incorporated *Device* * * *and Documentation Support* *Submit Documentation Feedback*

# Full Part # TMS LS B ZWT Q Q1 R Orderable Part # TMX B ZWT Q Q1 R

Prefix: TM TMS = Fully Qualified TMP = Prototype TMX = Samples Core Technology: 570 = Cortex R4F

Architecture: LS = Dual  CPUs in Lockstep (not included in orderable part #)

## Flash Memory Size $$ 12 = 1.25MB $$

## RAM MemorySize $$ 2 = 192kB $$ Peripheral Set: 7 = FlexRay, Ethernet

## Die Revision A = Die Revision A B   = Die Revision B

Package Type: ZWT = 337-Pin Plastic BGA with pb-free solder ball PGE = 144 Pin Plastic Quad Flatpack Temperature Range: $$ Q = -40...+125 C $$ o Quality Designator: Q1 = Automotive Shipping Options: R = Tape and Reel

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## Figure 8-1. TMS570LS1227 Device Numbering Conventions

*Device* * * *and Documentation Support* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

| www.ti.com | SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 |
|:--- |:--- |
| 8.2 | Documentation Support |
| 8.2.1 | Related Documentation from Texas Instruments |

## 8.2 **Documentation Support**

## 8.2.1

***Related*** *** *** ***Documentation from Texas Instruments***

The following documents describe the * * *TMS570LS1227TMS570LS11x/12x* microcontroller..

**SPNU515** ***TMS570LS12x/11x*** *** *** ***16/32-Bit*** *** *** ***RISC*** *** *** ***Flash*** *** *** ***Microcontroller*** *** *** ***Technical*** *** *** ***Reference*** *** *** ***Manual*** details the integration, the environment, the functional description, and the programming models for each peripheral and subsystem in the device.

**SPNZ199** ***TMS570LS12x/11x*** *** *** ***Microcontroller,*** *** *** ***Silicon*** *** *** ***Revision*** *** *** ***B,*** *** *** ***Silicon*** *** *** ***Errata*** describes the usage notes and known exceptions to the functional specifications for the device silicon revision B.

**SPNZ218** ***TMS570LS12x/11x*** *** *** ***Microcontroller,*** *** *** ***Silicon*** *** *** ***Revision*** *** *** ***C,*** *** *** ***Silicon*** *** *** ***Errata*** describes the usage notes and known exceptions to the functional specifications for the device silicon revision C.

## 8.2.2 ***Community*** *** *** ***Resources***

The following links connect to TI community resources. Linked contents are provided "AS IS" by the respective contributors. They do not constitute TI specifications and do not necessarily reflect TI's views; see TI's Terms of Use.

**TI** ** ** **E2E™Online Community** *** *** ***TI's*** *** *** ***Engineer-to-Engineer*** *** *** ***(E2E)*** *** *** ***Community.*** Created to foster collaboration among

engineers. At e2e.ti.com, you can ask questions, share knowledge, explore ideas and help solve problems with fellow engineers.

**TI Embedded Processors** ** ** **Wiki** *** *** ***Texas*** *** *** ***Instruments*** *** *** ***Embedded*** *** *** ***Processors*** *** *** ***Wiki.*** Established to help developers

get started with Embedded Processors from Texas Instruments and to foster innovation and growth of general knowledge about the hardware and software surrounding these devices.

**8.3** **Trademarks** E2E is a trademark of Texas Instruments. CoreSight is a trademark of ARM Limited. ARM, Cortex are registered trademarks of ARM Limited (or its subsidiaries) in the EU and/or elsewhere. All rights reserved. All other trademarks are the property of their respective owners.

| 8.4 | Electrostatic Discharge Caution |
|:--- |:--- |
| This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled with | appropriate precautions. Failure to observe proper handling and installation procedures can cause damage. |
| ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may be more | susceptible to damage because very small parametric changes could cause the device not to meet its published specifications. |
| 8.5 | Glossary |

This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.

ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may be more susceptible to damage because very small parametric changes could cause the device not to meet its published specifications.

## 8.5 **Glossary** SLYZ022 - * TI Glossary*.

This glossary lists and explains terms, acronyms, and definitions.

Copyright © 2012-2015, Texas Instruments Incorporated *Device* * * *and Documentation Support* *Submit Documentation Feedback*

# TMS570LS1227

| SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 | www.ti.com |
|:--- |:--- |
| 8.6 | Device Identification |
| 8.6.1 | Device Identification Code Register |

## 8.6 **Device Identification**

## 8.6.1

***Device Identification*** *** *** ***Code*** *** *** ***Register***

## The device identification code register identifies several aspects of the device including the silicon version.

The details of the device identification code register are shown in Table 8-1. The device identification code register value for this device is: $$ •• Rev A = 0x8046AD05 $$ $$ •• Rev B = 0x8046AD15 $$ $$ •• Rev C = 0x8046AD1D $$

## Figure 8-2. Device ID Bit Allocation Register

# CP-15 UNIQUE ID TECH

# R-1 R-00000000100011 R-0

# TECH

I/O PERIPH FLASH ECC RAM VERSION VOLT PARITY ECC AGE

# R-101 R-0 R-1 R-10 R-1 R-00011 R-1 R-0 R-1

LEGEND: R/W = Read/Write; R = Read only; - *n* = value after reset

## Table 8-1. Device ID Bit Allocation Register Field Descriptions **Bit** **Field** **Value** **Description** CP15 Indicates the presence of coprocessor 15 CP15 present

30-17 UNIQUE ID Unique device identification number This bitfield holds a unique number for a dedicated device configuration (die).

16-13 TECH Process technology on which the device is manufactured.

# F021 I/O VOLTAGE I/O voltage of the device. I/O are 3.3v

PERIPHERAL Peripheral Parity PARITY Parity on peripheral memories

# 10-9 FLASH ECC Flash ECC Program memory with ECC

RAM ECC Indicates if RAM memory ECC is present. ECC implemented 7-3 REVISION Revision of the Device. 2-0 The platform family ID is always 0b101

## 8.6.2

***Die*** *** *** ***Identification*** *** *** ***Registers***

## The two die ID registers at addresses 0xFFFFFF7C and 0xFFFFFF80 form a 64-bit dieid with the information as shown in Table 8-2.

## Table 8-2. Die-ID Registers

**Item** **#** ** ** **of Bits** **Bit** ** ** **Location** X Coordinate on Wafer 0xFFFFFF7C\[11:0\] Y Coordinate on Wafer 0xFFFFFF7C\[23:12\] Wafer # 0xFFFFFF7C\[31:24\]

# Lot # 0xFFFFFF80\[23:0\]

*Device* * * *and Documentation Support* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## Table 8-2. Die-ID Registers (continued)

**Item** **#** ** ** **of Bits** **Bit** ** ** **Location** Reserved 0xFFFFFF80\[31:24\]

Copyright © 2012-2015, Texas Instruments Incorporated *Device* * * *and Documentation Support* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## 8.7 **Module** ** ** **Certifications**

The following communications modules have received certification of adherence to a standard.

*Device* * * *and Documentation Support* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 8.7.1 ***FlexRay™Certifications***

## Figure 8-3. Flexray Certification for ZWT Package

Copyright © 2012-2015, Texas Instruments Incorporated *Device* * * *and Documentation Support* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## Figure 8-4. Flexray Certification for PGE Package

*Device* * * *and Documentation Support* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 8.7.2 ***DCAN*** *** *** ***Certification***

## Figure 8-5. DCAN Certification

Copyright © 2012-2015, Texas Instruments Incorporated *Device* * * *and Documentation Support* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## 8.7.3 ***LIN*** *** *** ***Certification***

## 8.7.3.1 **LIN Master Mode**

## Figure 8-6. LIN Certification - Master Mode

*Device* * * *and Documentation Support* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## 8.7.3.2 **LIN Slave Mode - Fixed Baud Rate**

## Figure 8-7. LIN Certification - Slave Mode - Fixed Baud Rate

Copyright © 2012-2015, Texas Instruments Incorporated *Device* * * *and Documentation Support* *Submit Documentation Feedback*

# TMS570LS1227

# SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015 **<https://www.ti.com**>

## 8.7.3.3 **LIN Slave Mode - Adaptive Baud Rate**

## Figure 8-8. LIN Certification - Slave Mode - Adaptive Baud Rate

*Device* * * *and Documentation Support* Copyright © 2012-2015, Texas Instruments Incorporated *Submit Documentation Feedback*

# TMS570LS1227

# www.ti.com SPNS192B -OCTOBER 2012-REVISED FEBRUARY 2015

## Mechanical Packaging and Orderable Information **9.1** **Packaging** ** ** **Information**

The following pages include mechanical packaging and orderable information. This information is the most current data available for the designated devices. This data is subject to change without notice and without revision of this document. For browser-based versions of this data sheet, refer to the left-hand navigation.

Copyright © 2012-2015, Texas Instruments Incorporated *Mechanical* * * *Packaging and Orderable Information* *Submit Documentation Feedback*

# PACKAGE OPTION ADDENDUM <https://www.ti.com> 10-Nov-2025

# PACKAGING INFORMATION **Orderable part number** **Status** (1) **Material type** (2)

**Package \| Pins** **Package qty \| Carrier** **RoHS** (3) **Lead finish/** **Ball material** (4) **MSL rating/** **Peak reflow** (5) **Op temp (°C)** **Part marking** (6)

| TMS5701227CPGEQQ1 | Active | Production | LQFP (PGE) \\| 144 | 60 \\| JEDEC | TRAY (10+1) |
|:--- |:--- |:--- |:--- |:--- |:--- |
| Yes | NIPDAU | Level-3-260C-168 HR | -40 to 125 | TMS570LS | 1227CPGEQQ1 |
| TMS5701227CPGEQQ1.B | Active | Production | LQFP (PGE) \\| 144 | 60 \\| JEDEC | TRAY (10+1) |
| Yes | NIPDAU | Level-3-260C-168 HR | -40 to 125 | TMS570LS | 1227CPGEQQ1 |
| TMS5701227CZWTQQ1 | Active | Production | NFBGA (ZWT) \\| 337 | 90 \\| JEDEC | TRAY (10+1) |
| Yes | SNAGCU | Level-3-260C-168 HR | -40 to 125 | TMS570LS | 1227CZWTQQ1 |
| TMS5701227CZWTQQ1.B | Active | Production | NFBGA (ZWT) \\| 337 | 90 \\| JEDEC | TRAY (10+1) |
| Yes | SNAGCU | Level-3-260C-168 HR | -40 to 125 | TMS570LS | 1227CZWTQQ1 |

# Yes

NIPDAU Level-3-260C-168 HR -40 to 125 TMS570LS 1227CPGEQQ1

TMS5701227CPGEQQ1.B Active Production LQFP (PGE) \| 144 60 \| JEDEC TRAY (10+1)

# Yes

NIPDAU Level-3-260C-168 HR -40 to 125 TMS570LS 1227CPGEQQ1

TMS5701227CZWTQQ1 Active Production NFBGA (ZWT) \| 337 90 \| JEDEC TRAY (10+1)

# Yes

SNAGCU Level-3-260C-168 HR -40 to 125 TMS570LS 1227CZWTQQ1

TMS5701227CZWTQQ1.B Active Production NFBGA (ZWT) \| 337 90 \| JEDEC TRAY (10+1)

# Yes

SNAGCU Level-3-260C-168 HR -40 to 125 TMS570LS 1227CZWTQQ1

TMS5701227CZWTQQ1R Active Production NFBGA (ZWT) \| 337 1000 \| LARGE T&R Yes SNAGCU Level-3-260C-168 HR -40 to 125 TMS570LS 1227CZWTQQ1

TMS5701227CZWTQQ1R.B Active Production NFBGA (ZWT) \| 337 1000 \| LARGE T&R Yes SNAGCU Level-3-260C-168 HR -40 to 125 TMS570LS 1227CZWTQQ1 **(1)** ** Status: ** For more details on status, see our product life cycle.

**(2)** ** Material type: ** When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance, reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind.

**(3)** ** RoHS values: ** Yes, No, RoHS Exempt. See the TI RoHS Statement for additional information and value definition.

**(4)** ** Lead finish/Ball material: ** Parts may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two lines if the finish value exceeds the maximum column width.

**(5)** ** MSL rating/Peak reflow: ** The moisture sensitivity level ratings and peak solder (reflow) temperatures. In the event that a part has multiple moisture sensitivity ratings, only the lowest level per JEDEC standards is shown. Refer to the shipping label for the actual reflow temperature that will be used to mount the part to the printed circuit board.

**(6)** ** Part marking: ** There may be an additional marking, which relates to the logo, the lot trace code information, or the environmental category of the part. Multiple part markings will be inside parentheses. Only one part marking contained in parentheses and separated by a "~" will appear on a part. If a line is indented then it is a continuation of the previous line and the two combined represent the entire part marking for that device. Addendum-Page 1

# PACKAGE OPTION ADDENDUM <https://www.ti.com> 10-Nov-2025

**Important Information and Disclaimer:** The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release. In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis. Addendum-Page 2

# PACKAGE MATERIALS INFORMATION <https://www.ti.com> 23-May-2025

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

# TMS5701227CZWTQQ1R NFBGA ZWT 330.0 24.4 16.35 16.35 2.35 20.0 24.0 Q1 Pack Materials-Page 1

# PACKAGE MATERIALS INFORMATION <https://www.ti.com> 23-May-2025

# TAPE AND REEL BOX DIMENSIONS ***Width (mm)***

# W

# L

# H \*All dimensions are nominal

**Device** **Package Type** **Package Drawing** **Pins** **SPQ** **Length (mm)** **Width (mm)** **Height (mm)**

# TMS5701227CZWTQQ1R NFBGA ZWT 336.6 336.6 41.3 Pack Materials-Page 2

# PACKAGE MATERIALS INFORMATION <https://www.ti.com> 23-May-2025

# TRAY

## L - Outer tray length without tabs **KO - ** **Outer **

| tray | height |
|:--- |:--- |
| W - | Outer |
| tray | width |

## W **Outer **

## tray **width**

## P1 - Tray unit pocket pitch

## CW - Measurement for tray edge (Y direction) to corner pocket center

## CL - Measurement for tray edge (X direction) to corner pocket center Text

Chamfer on Tray corner indicates Pin 1 orientation of packed units. \*All dimensions are nominal **Device** **Package** **Name** **Package** **Type** **Pins** **SPQ** **Unit array** **matrix** **Max** **temperature** **(°C)** **L (mm)** **W** **(mm)**

| K0 | (µm) |
|:--- |:--- |
| P1 | (mm) |
| CL | (mm) |
| CW | (mm) | **P1** **(mm)** **CL** **(mm)** **CW** **(mm)**

# TMS5701227CPGEQQ1 PGE LQFP 5X12 135.9 25.4 17.8 17.55

# TMS5701227CPGEQQ1.B PGE LQFP 5X12 135.9 25.4 17.8 17.55

# TMS5701227CZWTQQ1 ZWT NFBGA 6 X 15 135.9 17.5 15.45

# TMS5701227CZWTQQ1.B ZWT NFBGA 6 X 15 135.9 17.5 15.45 Pack Materials-Page 3 <https://www.ti.com>

# PACKAGE OUTLINE

# C 1.4 MAX

# TYP 0.45 0.35

# 14.4 TYP

# 14.4 TYP

# 0.8 TYP

# 0.8 TYP

# 337X 0.55 0.45

# B 16.1 15.9 A 16.1 15.9

# (0.8) TYP

# (0.8) TYP

# NFBGA - 1.4 mm max height **ZWT0337A**

# PLASTIC BALL GRID ARRAY

# 4223381/A 02/2017

NOTES: 1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M. 2. This drawing is subject to change without notice. 13 14 15 16 17 18 19

# BALL A1 CORNER

# SEATING PLANE

# BALL TYP 0.12 C

# 0.15 C A B 0.05 C

# SYMM

# SYMM

# BALL A1 CORNER

# W

# C D E F G H J K L M N P R T U V

# 9 10 11 A

# B

# SCALE 0.950 <https://www.ti.com>

# EXAMPLE BOARD LAYOUT

# 337X ( 0.4) (0.8) TYP

# (0.8) TYP

# ( 0.4) METAL

# 0.05 MAX

# SOLDER MASK OPENING

# METAL UNDER SOLDER MASK

# ( 0.4) SOLDER MASK OPENING

# 0.05 MIN

# NFBGA - 1.4 mm max height **ZWT0337A**

# PLASTIC BALL GRID ARRAY

# 4223381/A 02/2017

NOTES: (continued) 3. Final dimensions may vary due to manufacturing tolerance considerations and also routing constraints. For information, see Texas Instruments literature number SPRAA99 (<https://www.ti.com/lit/spraa99).>

# SYMM

# SYMM

# LAND PATTERN EXAMPLE EXPOSED METAL SHOWN SCALE:7X

# B

# A

# W

# V

# U

# T

# R

# P

# N

# M

# L

# K

# J

# H

# G

# F

# E

# D

# C

# NON-SOLDER MASK DEFINED (PREFERRED)

# SOLDER MASK DETAILS NOT TO SCALE

# EXPOSED METAL

# SOLDER MASK DEFINED

# EXPOSED METAL <https://www.ti.com>

# EXAMPLE STENCIL DESIGN

# (0.8) TYP

# (0.8) TYP ( 0.4) TYP

# NFBGA - 1.4 mm max height **ZWT0337A**

# PLASTIC BALL GRID ARRAY

# 4223381/A 02/2017

NOTES: (continued) 4. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release.

# SOLDER PASTE EXAMPLE BASED ON 0.15 mm THICK STENCIL SCALE:7X

# SYMM

# SYMM

# B

# A

# W

# V

# U

# T

# R

# P

# N

# M

# L

# K

# J

# H

# G

# F

# E

# D

# C

# MECHANICAL DATA

** ** ** ** MTQF017A - OCTOBER 1994 - REVISED DECEMBER 1996

# POST OFFICE BOX 655303 • DALLAS, TEXAS 75265

# PGE (S-PQFP-G144) **PLASTIC QUAD FLATPACK**

# 4040147/C 10/96 **0,27** **0,17**

# 0,13 NOM **0,25** **0,75** **0,45**

# 0,05 MIN **Seating Plane** **Gage Plane**

# SQ

# SQ **22,20** **21,80** **19,80**

# 17,50 TYP **20,20** **1,35** **1,45**

# 1,60 MAX

# M **0,08** **0** ° **-7** ° **0,08** **0,50**

NOTES: A. All linear dimensions are in millimeters. B. This drawing is subject to change without notice. C. Falls within JEDEC MS-026

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