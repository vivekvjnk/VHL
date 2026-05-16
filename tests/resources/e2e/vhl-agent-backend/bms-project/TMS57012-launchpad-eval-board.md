SPNU613-May 2017 *Submit Documentation Feedback*

Copyright © 2017, Texas Instruments Incorporated *Hercules™TMS570LS12x/RM46 LaunchPad™*

## User's Guide

# SPNU613-May 2017

# Hercules™TMS570LS12x/RM46 LaunchPad™

**Contents** Kit Overview.................................................................................................................. Hardware Description....................................................................................................... Software Development.................................................................................................... Appendix A Schematics......................................................................................................... Appendix B Design File Sources............................................................................................... Appendix C Regulatory Information........................................................................................... 29 **List** ** ** **of** ** ** **Figures**

Hercules TMS570LS12224 / RM46L852 PGE LaunchPad............................................................ 2

Hercules TMS570LS12224 / RM46L852 PGE LaunchPad Block Diagram.......................................... 3 **List** ** ** **of** ** ** **Tables**

LAUNCHXL2-TMS57012 and LAUNCHXL2-RM46 Specifications.................................................... 3

# LEDs...........................................................................................................................

Push Button Switches.......................................................................................................

Booster Pack Site 1 - J2 Connections.................................................................................... 6

Booster Pack Site 1 - J3 Connections.................................................................................... 6

Booster Pack Site 1 - J4 Connections.................................................................................... 7

Booster Pack Site 1 - J5 Connections.................................................................................... 7

Booster Pack Site 2 - J6 Connections.................................................................................... 7

Booster Pack Site 2 - J7 Connections.................................................................................... 8

Booster Pack Site 2 - J8 Connections.................................................................................... 8

Booster Pack Site 2 - J9 Connections.................................................................................... 8

Proto Board Header J10 Connections.................................................................................... 9

Proto Board Header J11 Connections................................................................................... 10

External JTAG Debug Header J1........................................................................................ 11

## Trademarks

Hercules, LaunchPad, Code Composer Studio are trademarks of Texas Instruments. ARM, Cortex are registered trademarks of ARM Limited. *Kit Overview* <https://www.ti.com>

SPNU613-May 2017 *Submit Documentation Feedback* Copyright © 2017, Texas Instruments Incorporated *Hercules™TMS570LS12x/RM46 LaunchPad™* **Kit Overview**

The LAUNCHXL2-TMS57012 and LAUNCHXL-RM46 LaunchPad kits from Texas Instruments provide a low cost vehicle to evaluate and develop with members of the Hercules family that are based on either the TMS570LS1224PGE or RM46L852PGE microcontrollers. Both kits are identical except for the Hercules microcontroller that is hosted by the kit. Figure 1 shows a photo of one of these kits with the major components labeled.

Project collateral and source files discussed in this application report can be downloaded from the following URL: <http://www.ti.com/lit/zip/spnu613>.

**Figure 1. Hercules TMS570LS12224 / RM46L852** ** ** **PGE LaunchPad** ***1.1*** ***Kit Contents***

Each Kit Contains: - • One LaunchPad board with: - - On-board XDS110 Debug interface - - Hercules microcontroller with 1280 KB of Flash, 64 KB of data Flash, and 192 KB of SRAM - - LAUNCHXL2-TMS57012 is populated with the 160 MHz TMS570LS1224-PGE microcontroller. - - LAUNCHXL2-RM46 is populated with the 220 MHz RM46L852-PGE microcontroller - • USB micro-B plug to USB-A plug cable - • Hercules LaunchPad Quick Start Guide - • Standard Terms and Conditions for Evaluation Modules <https://www.ti.com> *Kit Overview*

SPNU613-May 2017 *Submit Documentation Feedback*

Copyright © 2017, Texas Instruments Incorporated *Hercules™TMS570LS12x/RM46 LaunchPad™*

## 1.2 ***Specifications***

## Key operating specifications for the LaunchPad are listed in Table 1.

## Table 1. LAUNCHXL2-TMS57012 and LAUNCHXL2-RM46 Specifications **Parameter** **Value**

Board Supply Voltage 4.75 VDC to 5.25 VDC from Micro-B Cable, Booster Pack Headers, or optional power jack J14

Power available to Expansion Boards (Total) Sum of +5 V and +3.3 V Supply Current: 10mA max for USB Bus Powered Operation. 1A Max for power through J14. Dimensions 5.150" x 2.650"

Operating Temperature Range Room Temperature Operation Only

## Hardware Description

## 2.1 ***Block Diagram***

## Figure 2 shows a block diagram of the LaunchPad printed circuit board. The major components of the

board are described in the sections that follow.

## Figure 2. Hercules TMS570LS12224 / RM46L852 PGE LaunchPad Block Diagram

*Hardware* * * *Description* <https://www.ti.com>

SPNU613-May 2017 *Submit Documentation Feedback* Copyright © 2017, Texas Instruments Incorporated *Hercules™TMS570LS12x/RM46 LaunchPad™* ***2.2*** ***Hercules Microcontroller***

# 2.2.1

**TMS570LS1224** ** ** **MCU (LAUNCHXL2-TMS57012)**

The TMS570LS1224 device is a high-performance automotive-grade microcontroller family for safety systems. The safety architecture includes dual CPUs in lockstep, CPU and memory BIST logic, ECC on both the flash and the data SRAM, parity on peripheral memories, and loopback capability on peripheral I/Os.

The TMS570LS1224 device integrates the ARM ® Cortex ® -R4F floating-point CPU that offers an efficient 1.66 DMIPS/MHz, and has configurations that can run up to 180 MHz providing up to 298 DMIPS. The device supports the word-invariant big-endian \[BE32\] format.

The TMS570LS1224 device has 1.25MB of integrated flash and 192KB of data RAM with single-bit error correction and double-bit error detection. The flash memory on this device is a nonvolatile, electrically erasable and programmable memory, implemented with a 64-bit-wide data bus interface. The flash operates on a 3.3-V supply input (same level as I/O supply) for all read, program, and erase operations. When in pipeline mode, the flash operates with a system clock frequency of up to 180 MHz. The SRAM supports single-cycle read and write accesses in byte, halfword, word, and double-word modes throughout the supported frequency range.

For additional information, see the device product folder: <http://www.ti.com/product/tms570ls1224>.

# 2.2.2 **RM46L852 MCU (LAUNCHXL2-RM46)**

The RM46L852 device is a high-performance microcontroller family for safety systems. The safety architecture includes dual CPUs in lockstep, CPU and memory BIST logic, ECC on both the flash and the data SRAM, parity on peripheral memories, and loopback capability on peripheral I/Os.

The RM46L852 device integrates the ARM Cortex-R4F floating-point CPU that offers an efficient 1.66 DMIPS/MHz, and can run up to 220 MHz providing up to 365 DMIPS. The device supports the littleendian \[LE\] format.

The RM46L852 device has 1.25MB of integrated flash and 192KB of data RAM with single-bit error correction and double-bit error detection. The flash memory on this device is a nonvolatile, electrically erasable and programmable memory, implemented with a 64-bit-wide data bus interface. The flash operates on a 3.3-V supply input (same level as I/O supply) for all read, program, and erase operations. When in pipeline mode, the flash operates with a system clock frequency of up to 220 MHz. The SRAM supports single-cycle read and write accesses in byte, halfword, word, and double-word modes throughout the supported frequency range.

For additional information, see the device product folder: <http://www.ti.com/product/rm46l852>.

***2.3*** ***XDS110 JTAG*** *** *** ***Debugger and*** *** *** ***USB*** *** *** ***Serial Port***

An XDS110 Debug Probe is integrated onto the to make getting started with the LaunchPad as seamless as possible. This emulator is supported by Code Composer Studio™and other third party IDEs.

The XDS110 is a USB composite device consisting of two functions: - • TI XDS100 debug probe - • A USB Serial Port

Each function may be used independently, for example, it is possible to use the XDS110 debug probe with Code Composer Studio and at the same time connect to the USB Serial Port with any terminal program. The USB serial port provides a convenient method to interact with the Hercules microcontroller through the microcontroller LIN/SCI peripheral.

<https://www.ti.com> *Hardware* * * *Description*

SPNU613-May 2017 *Submit Documentation Feedback*

Copyright © 2017, Texas Instruments Incorporated *Hercules™TMS570LS12x/RM46 LaunchPad™*

***2.4*** ***Voltage*** *** *** ***Regulator***

The LaunchPad includes an on-board Low Dropout Voltage Regulator ( LM26420XMHX/NOPB ) that supplies the 3.3 V and 1.2 V power rails required by the MCU and XDS110 from the USB Bus. In normal operation, the LaunchPad operates as a USB bus powered device.

The on-board LDO is rated for up to 2A on the 3.3 V rail, but USB bus powered devices are limited to drawing less than 500 mA from the USB Bus. If BoosterPacks are added to the LaunchPad and more current is required by the booster packs than is specified in Table 1, then the LaunchPad should be converted so that it operates as a self-powered USB device. In this case, it is recommended to:

- • Remove Jumper J6 so that the LaunchPad (when operating as a self powered device) does not back power the USB bus VBUS rail. - • Install a barrel jack in location J14 - • Supply the LaunchPad with +5 V supply that is current limited to 1.5A. - • Use the +3.3 V IO rail provided by the LaunchPad on-board voltage regulator and available on J2 and J6 to power any interface logic between the MCU and booster packs. - • Avoid supplying a regulated +3.3 V rail from the BoosterPack as this would conflict with the LaunchPad on-board LDO regulator. Because some booster packs may require their own power supply and this may conflict with the onboard power supply of the LaunchPad, jumpers JP2, JP3, JP4, and JP5 allow the +3.3V and +5V connections between LaunchPad and Booster Packs to be disconnected if necessary to avoid a conflict.

# 2.5 ***LEDs***

There are eight LEDs on the LaunchPad. Two of the LEDs are available for use by application code running on the MCU (D11, D12). Table 2 contains a summary of the LaunchPad LEDs and their purpose. **Table 2. LEDs**

| LED | Color | Driver | Description |
|:--- |:--- |:--- |:--- |
| LED1 | Red | MCU nERROR Pin | Indicates Error Detected by MCU ESM Module |
| LED2 | Green | GIOB\[1\] | General Purpose Indicator LED. Drive pin to logic high to light LED. |
| LED3 | Green | GIOB\[2\] | General Purpose Indicator LED. Drive pin to logic high to light LED. |
| LED4 | Green | +3.3V | +3.3 V Power Indicator |
| LED5 | Green | +5 V | +5 V Power Indicator |

LED1 Red MCU nERROR Pin Indicates Error Detected by MCU ESM Module

LED2 Green GIOB\[1\] General Purpose Indicator LED. Drive pin to logic high to light LED.

LED3 Green GIOB\[2\] General Purpose Indicator LED. Drive pin to logic high to light LED. LED4 Green +3.3V +3.3 V Power Indicator LED5 Green +5 V +5 V Power Indicator LED7 Green XDS110 XDS110 Status LED8 Green ***2.6*** ***Push Buttons***

There are four pushbutton switches on the LaunchPad, described in Table 3. There are many subtle differences between a warm reset (S2) and power on reset (S3) but the main difference involves certain error and reset status flags that are only cleared during a power on reset. **Table 3. Push Button Switches**

| Switch | MCU Pin | Description |
|:--- |:--- |:--- |
| S1 | nPORRST | Pressing the button asserts a power on reset (nPORRST). |
| S2 | nRST | Pressing the button asserts a warm reset (nRST). |

S1 nPORRST Pressing the button asserts a power on reset (nPORRST).

S2 nRST Pressing the button asserts a warm reset (nRST).

S3 MIBSPI3NCS\_0/AD2EVT/GIOB\_2/EQEP1I General Purpose User Input. Pin reads '0' when pressed, '1' when released. S4 N2HET1\_15/MIBSPI1NCS\_4/ECAP1

*Hardware* * * *Description* <https://www.ti.com>

SPNU613-May 2017 *Submit Documentation Feedback* Copyright © 2017, Texas Instruments Incorporated *Hercules™TMS570LS12x/RM46 LaunchPad™*

| 2.7 | Light Sensor |
|:--- |:--- |
| To demonstrate the capabilities of the TMS570LS1224 / RM42 A/D Converter, the LaunchPad includes an | Ambient Light Sensor (Vishay TEMT6000). The light sensor is tied to AD1IN\[6\]. |
| 2.8 | Oscillator Failure Jumper |

To demonstrate the capabilities of the TMS570LS1224 / RM42 A/D Converter, the LaunchPad includes an Ambient Light Sensor (Vishay TEMT6000). The light sensor is tied to AD1IN\[6\].

***2.8*** ***Oscillator*** *** *** ***Failure*** *** *** ***Jumper***

The MCU is capable of detecting a failure on its external oscillator and of automatically switching to an on chip oscillator so that the MCU may continue to operate in the event of such a failure. To demonstrate this capability, a shunt installed on jumper JP1 will short the oscillator to ground causing it to 'fail'. This jumper should be removed for normal operation.

***2.9*** ***Booster*** *** *** ***Pack Headers***

The LaunchPad supports two Booster Pack sites through headers J2, J3, J4, and J5 (Booster Pack #1) and J6, J7, J8, and J9 (Booster Pack 2). The pinout of each header is described in Table 4 - Table 11.

The official TI list of BoosterPacks can be found at <https://www.ti.com/boosterpacks>.

The ADC inputs on the BoosterPack are limited to the range of 0 V DC - +3.3 V DC by default; however resistors R1, R2, R3, R4 on the LaunchPad can be arranged to allow for an ADC input range of 0 V DC - +5 V DC.

All of the digital I/O on the BoosterPack (and Expansion) headers are 3.3 V LVCMOS. A transceiver is usually required before connecting to a serial bus (ex. CAN or RS-232). There are no transceivers on the LaunchPad itself.

**Table 4. Booster Pack Site** ** ** **1 - J2 Connections**

**Header** **Header Pin** **MCU** **MCU** ** ** **Pin** **Description**

| J2 | +3.3 V Booster Pack - Default Connection to LaunchPad +3.3 V When JP4 Is | Installed |
|:--- |:--- |:--- |
| J2 | U1 | AD1IN\[16\]/AD2IN\[0\] |
| J2 | U1 | N2HET1\[6\]/SCIRX/EPWM5A |
| J2 | U1 | N2HET1\[13\]/SCITX/EPWM5B |
| J2 | U1 | GIOA\[7\]/N2HET2\[6\]/EPWM2A |
| J2 | U1 | AD1IN\[17\]/AD2IN\[1\] |
| J2 | U1 | MIBSPI3CLK/AWM\_EXT\_SEL\[1\]/EQEP1A |
| J2 | U1 | GIOA\[6\]/N2HET2\[4\]/EPWM1B |
| J2 | U1 | N2HET1\[4\]/EPWM4B |
| J2 | U1 | N2HET1\[9\]/N2HET2\[16\]/EPWM7A |

# J2 U1 AD1IN\[16\]/AD2IN\[0\]

# J2 U1 N2HET1\[6\]/SCIRX/EPWM5A

# J2 U1 N2HET1\[13\]/SCITX/EPWM5B

# J2 U1 GIOA\[7\]/N2HET2\[6\]/EPWM2A

# J2 U1 AD1IN\[17\]/AD2IN\[1\]

# J2 U1 MIBSPI3CLK/AWM\_EXT\_SEL\[1\]/EQEP1A

# J2 U1 GIOA\[6\]/N2HET2\[4\]/EPWM1B

# J2 U1 N2HET1\[4\]/EPWM4B

# J2 U1 N2HET1\[9\]/N2HET2\[16\]/EPWM7A

**Table 5. Booster Pack Site** ** ** **1 - J3 Connections**

**Header** **Header Pin** **MCU** **MCU** ** ** **Pin** **Description**

J3 +5V Booster Pack - Default Connection to LaunchPad +5V When JP3 Is Installed

# J3 GND

| J3 | U1 | AD1IN\[0\] |
|:--- |:--- |:--- |
| J3 | U1 | AD1IN\[7\] |
| J3 | U1 | AD1IN\[18\]/AD2IN\[2\] |
| J3 | U1 | AD1IN\[19\]/AD2IN\[3\] |
| J3 | U1 | AD1IN\[20\]/AD2IN\[4\] |
| J3 | U1 | AD1IN\[21\]/AD2IN\[5\] |

# J3 U1 AD1IN\[7\]

# J3 U1 AD1IN\[18\]/AD2IN\[2\]

# J3 U1 AD1IN\[19\]/AD2IN\[3\]

# J3 U1 AD1IN\[20\]/AD2IN\[4\]

# J3 U1 AD1IN\[21\]/AD2IN\[5\]

<https://www.ti.com> *Hardware* * * *Description*

SPNU613-May 2017 *Submit Documentation Feedback*

Copyright © 2017, Texas Instruments Incorporated *Hercules™TMS570LS12x/RM46 LaunchPad™*

## Table 6. Booster Pack Site 1 - J4 Connections

**Header** **Header Pin** **MCU** **MCU** ** ** **Pin** **Description**

| J4 | U1 | N2HET1\[20\]/EPWM6B |
|:--- |:--- |:--- |
| J4 | U1 | N2HET1\[18\]/EPWM6A |
| J4 | U1 | N2HET1\[16\]/EPWM1SYNCI/EPWM1SYNCO |
| J4 | U1 | N2HET1\[30\]/MII\_RX\_DV/EQEP2S |
| J4 | U1 | N2HET1\[14\] |
| J4 | U1 | N2HET1\[12\]/MII\_CRS/RMII\_CRS\_DV |
| J4 | U1 | GIOA\[5\]/EXTCLKIN/EPWM1A |
| J4 | U1 | GIOA\[2\]/N2HET2\[0\]/EQEP2I |
| J4 | U1 | GIOA\[1\] |
| J4 | U1 | GIOA\[0\] |

# J4 U1 N2HET1\[18\]/EPWM6A

# J4 U1 N2HET1\[16\]/EPWM1SYNCI/EPWM1SYNCO

# J4 U1 N2HET1\[30\]/MII\_RX\_DV/EQEP2S

# J4 U1 N2HET1\[14\]

# J4 U1 N2HET1\[12\]/MII\_CRS/RMII\_CRS\_DV

# J4 U1 GIOA\[5\]/EXTCLKIN/EPWM1A

# J4 U1 GIOA\[2\]/N2HET2\[0\]/EQEP2I

# J4 U1 GIOA\[1\]

# J4 U1 GIOA\[0\]

## Table 7. Booster Pack Site 1 - J5 Connections

**Header** **Header Pin** **MCU** **MCU** ** ** **Pin** **Description**

# J5 GND

| J5 | U1 | N2HET1\[22\] |
|:--- |:--- |:--- |
| J5 | U1 | MIBSPI3NCS\[1\]/N2HET1\[25\]/MDCLK |
| J5 | U1 | GIOB\[3\] |
| J5 | U1 | HERCULES\_NRST |
| J5 | U1 | MIBSPI3SIMO/AWM\_EXT\_SEL\[0\]/ECAP3 |
| J5 | U1 | MIBSPI3SOMI/AWM\_EXT\_ENA/ECAP2 |
| J5 | U1 | MIBSPI3NCS\[2\]/I2C\_SDA/N2HET1\[27\]/NTZ2 |
| J5 | U1 | MIBSPI3NCS\[3\]/I2C\_SCL/N2HET1\[29\]/NTZ1 |
| J5 | U1 | GIOB\[2\] |

# J5 U1 MIBSPI3NCS\[1\]/N2HET1\[25\]/MDCLK

# J5 U1 GIOB\[3\]

# J5 U1 HERCULES\_NRST

# J5 U1 MIBSPI3SIMO/AWM\_EXT\_SEL\[0\]/ECAP3

# J5 U1 MIBSPI3SOMI/AWM\_EXT\_ENA/ECAP2

# J5 U1 MIBSPI3NCS\[2\]/I2C\_SDA/N2HET1\[27\]/NTZ2

# J5 U1 MIBSPI3NCS\[3\]/I2C\_SCL/N2HET1\[29\]/NTZ1

# J5 U1 GIOB\[2\]

## Table 8. Booster Pack Site 2 - J6 Connections

**Header** **Header Pin** **MCU** **MCU** ** ** **Pin** **Description**

| J6 | +3.3 V Booster Pack - Default Connection to LaunchPad +3.3 V When JP4 Is | Installed |
|:--- |:--- |:--- |
| J6 | U1 | AD1IN\[9\]/AD2IN\[9\] |
| J6 | U1 | HERCULES\_LIN1\_RXD |
| J6 | U1 | HERCULES\_LIN1\_TXD |
| J6 | U1 | MIBSPI3NCS\[0\]/AD2EVT/GIOB\[2\]/EQEP1I |
| J6 | U1 | AD1IN\[1\] |
| J6 | U1 | MIBSPI1CLK |
| J6 | U1 | MIBSPI3NENA/MIBSPI3NCS\[5\]/N2HET1\[31\]/EQEP1B |
| J6 | U1 | N2HET1\[24\]/MIBSPI1NCS\[5\]/MII\_RXD\[0\]/RMII\_RXD\[0\] |
| J6 | U1 | N2HET1\[26\]/MII\_RXD\[1\]/RMII\_RXD\[1\] |

# J6 U1 AD1IN\[9\]/AD2IN\[9\]

# J6 U1 HERCULES\_LIN1\_RXD

# J6 U1 HERCULES\_LIN1\_TXD

# J6 U1 MIBSPI3NCS\[0\]/AD2EVT/GIOB\[2\]/EQEP1I

# J6 U1 AD1IN\[1\]

# J6 U1 MIBSPI1CLK

# J6

U1 MIBSPI3NENA/MIBSPI3NCS\[5\]/N2HET1\[31\]/EQEP1B

# J6

U1 N2HET1\[24\]/MIBSPI1NCS\[5\]/MII\_RXD\[0\]/RMII\_RXD\[0\]

# J6 U1 N2HET1\[26\]/MII\_RXD\[1\]/RMII\_RXD\[1\]

*Hardware* * * *Description* <https://www.ti.com>

SPNU613-May 2017 *Submit Documentation Feedback* Copyright © 2017, Texas Instruments Incorporated *Hercules™TMS570LS12x/RM46 LaunchPad™*

## Table 9. Booster Pack Site 2 - J7 Connections

**Header** **Header Pin** **MCU** **MCU** ** ** **Pin** **Description**

J7 +5 V Booster Pack - Default Connection to LaunchPad +5 V When JP5 Is Installed

# J7 GND

| J7 | U1 | AD1IN\[10\]/AD2IN\[10\] |
|:--- |:--- |:--- |
| J7 | U1 | AD1IN\[2\] |
| J7 | U1 | AD1IN\[3\] |
| J7 | U1 | AD1IN\[11\]/AD2IN\[11\] |
| J7 | U1 | AD1IN\[4\] |
| J7 | U1 | AD1IN\[12\]/AD2IN\[12\] |

# J7 U1 AD1IN\[2\]

# J7 U1 AD1IN\[3\]

# J7 U1 AD1IN\[11\]/AD2IN\[11\]

# J7 U1 AD1IN\[4\]

# J7 U1 AD1IN\[12\]/AD2IN\[12\]

## Table 10. Booster Pack Site 2 - J8 Connections

**Header** **Header Pin** **MCU** **MCU** ** ** **Pin** **Description**

| J8 | U1 | N2HET1\[10\]/MII\_TX\_CLK/MII\_TX\_AVCLK4/NTZ3 |
|:--- |:--- |:--- |
| J8 | U1 | N2HET1\[28\]/MII\_RXCLK/RMII\_REFCLK/MII\_RX\_AVCLK4 |
| J8 | U1 | N2HET1\[8\]/MIBSPI1SIMO\[1\]/MII\_TXD\[3\] |
| J8 | U1 | MIBSPI1NENA/N2HET1\[23\]/MII\_RXD\[2\]/ECAP4 |
| J8 | U1 | MIBSPI5NENA/MII\_RXD\[3\]/MIBSPI5SOMI\[1\]/ECAP5 |
| J8 | U1 | N2HET1\[11\]/MIBSPI3NCS\[4\]/N2HET2\[18\]/EPWM1SYNCO |
| J8 | U1 | GIOB\[1\] |
| J8 | U1 | GIOB\[0\] |
| J8 | U1 | AD1EVT/MII\_RX\_ER/RMII\_RX\_ER |
| J8 | U1 | MIBSPI5CLK/MII\_TXEN/RMII\_TXEN |

# J8

U1 N2HET1\[28\]/MII\_RXCLK/RMII\_REFCLK/MII\_RX\_AVCLK4

# J8 U1 N2HET1\[8\]/MIBSPI1SIMO\[1\]/MII\_TXD\[3\]

# J8

U1 MIBSPI1NENA/N2HET1\[23\]/MII\_RXD\[2\]/ECAP4

# J8

U1 MIBSPI5NENA/MII\_RXD\[3\]/MIBSPI5SOMI\[1\]/ECAP5

# J8

U1 N2HET1\[11\]/MIBSPI3NCS\[4\]/N2HET2\[18\]/EPWM1SYNCO

# J8 U1 GIOB\[1\]

# J8 U1 GIOB\[0\]

# J8 U1 AD1EVT/MII\_RX\_ER/RMII\_RX\_ER

# J8 U1 MIBSPI5CLK/MII\_TXEN/RMII\_TXEN

## Table 11. Booster Pack Site 2 - J9 Connections

**Header** **Header Pin** **MCU** **MCU** ** ** **Pin** **Description**

# J9 GND

| J9 | U1 | N2HET1\[1\]/SPI4NENA/N2HET2\[8\]/EQEP2A |
|:--- |:--- |:--- |
| J9 | U1 | MIBSPI1NCS\[0\]/MIBSPI1SOMI\[1\]/MII\_TXD\[2\]/ECAP6 |
| J9 | U1 | MIBSPI5SIMO\[0\]/MII\_TXD\[1\]/RMII\_TXD\[1\]/MIBSPI5SOMI\[2\] |
| J9 | U1 | HERCULES\_NRST |
| J9 | U1 | MIBSPI1SIMO |
| J9 | U1 | MIBSPI1SOMI |
| J9 | U1 | MIBSPI1NCS\[1\]/N2HET1\[17\]/MII\_COL/EQEP1S |
| J9 | U1 | MIBSPI1NCS\[2\]/N2HET1\[19\]/MDIO |
| J9 | U1 | MIBSPI5SOMI\[0\]/MII\_TXD\[0\]/RMII\_TXD\[0\] |

# J9

U1 MIBSPI1NCS\[0\]/MIBSPI1SOMI\[1\]/MII\_TXD\[2\]/ECAP6

# J9

U1 MIBSPI5SIMO\[0\]/MII\_TXD\[1\]/RMII\_TXD\[1\]/MIBSPI5SOMI\[2\]

# J9 U1 HERCULES\_NRST

# J9 U1 MIBSPI1SIMO

# J9 U1 MIBSPI1SOMI

# J9

U1 MIBSPI1NCS\[1\]/N2HET1\[17\]/MII\_COL/EQEP1S

# J9 U1 MIBSPI1NCS\[2\]/N2HET1\[19\]/MDIO

# J9

U1 MIBSPI5SOMI\[0\]/MII\_TXD\[0\]/RMII\_TXD\[0\]

<https://www.ti.com> *Hardware* * * *Description*

SPNU613-May 2017 *Submit Documentation Feedback*

Copyright © 2017, Texas Instruments Incorporated *Hercules™TMS570LS12x/RM46 LaunchPad™*

## 2.10

***Proto*** *** *** ***Board*** *** *** ***Headers***

## The MCU IO pins that are not routed to the Booster Pack headers are available on proto board headers

J10 and J11. These are not installed by default and are each a single row of 50 pins on 0.100" pitch. The orientation layout of these signals allows a row of 0.100", 0.039" square post pin strips to be soldered into the LaunchPad so that it can be plugged into a 0.100" pitch solder-less breadboard for easy prototyping. Table 12 and Table 13 list the signals available on the prototyping headers.

## Table 12. Proto Board Header J10 Connections

**Header** **Header Pin** **MCU** **MCU** ** ** **Pin** **Description**

| J10 | +5 V |
|:--- |:--- |
| J10 | GND |
| J10 | +3V3 |
| J10 | GND |

# J10 GND

# J10 +3V3

# J10 GND

| J10 | U1 | N2HET1\[20\]/EPWM6B |
|:--- |:--- |:--- |
| J10 | U1 | N2HET1\[18\]/EPWM6A |
| J10 | U1 | N2HET1\[16\]/EPWM1SYNCI/EPWM1SYNCO |
| J10 | U1 | GIOB\[1\] |
| J10 | U1 | HERCULES\_LIN1\_TXD |
| J10 | U1 | HERCULES\_LIN1\_RXD |
| J10 | U1 | MIBSPI1NCS\[1\]/N2HET1\[17\]/MII\_COL/EQEP1S |
| J10 | U1 | DCAN2RX |
| J10 | U1 | DCAN2TX |
| J10 | U1 | N2HET1\[30\]/MII\_RX\_DV/EQEP2S |
| J10 | U1 | GIOB\[0\] |

# J10 U1 N2HET1\[18\]/EPWM6A

# J10 U1 N2HET1\[16\]/EPWM1SYNCI/EPWM1SYNCO

# J10 U1 GIOB\[1\]

# J10 U1 HERCULES\_LIN1\_TXD

# J10 U1 HERCULES\_LIN1\_RXD

# J10

U1 MIBSPI1NCS\[1\]/N2HET1\[17\]/MII\_COL/EQEP1S

# J10 U1 DCAN2RX

# J10 U1 DCAN2TX

# J10 U1 N2HET1\[30\]/MII\_RX\_DV/EQEP2S

# J10 U1 GIOB\[0\]

# J10 GND

# J10 U1 N2HET1\[14\]

# J10 U1 N2HET1\[12\]/MII\_CRS/RMII\_CRS\_DV

# J10 ECLK1T

| J10 | U1 | N2HET1\[10\]/MII\_TX\_CLK/MII\_TX\_AVCLK4/NTZ3 |
|:--- |:--- |:--- |
| J10 | U1 | NERROR |
| J10 | U1 | HERCULES\_NRST |
| J10 | U1 | N2HET1\[28\]/MII\_RXCLK/RMII\_REFCLK/MII\_RX\_AVCLK4 |
| J10 | U1 | N2HET1\[8\]/MIBSPI1SIMO\[1\]/MII\_TXD\[3\] |

# J10 U1 NERROR

# J10 U1 HERCULES\_NRST

# J10

U1 N2HET1\[28\]/MII\_RXCLK/RMII\_REFCLK/MII\_RX\_AVCLK4

# J10 U1 N2HET1\[8\]/MIBSPI1SIMO\[1\]/MII\_TXD\[3\]

# J10 GND

| J10 | U1 | MIBSPI1NCS\[0\]/MIBSPI1SOMI\[1\]/MII\_TXD\[2\]/ECAP6 |
|:--- |:--- |:--- |
| J10 | U1 | MIBSPI5CLK/MII\_TXEN/RMII\_TXEN |
| J10 | U1 | MIBSPI5SIMO\[0\]/MII\_TXD\[1\]/RMII\_TXD\[1\]/MIBSPI5SOMI\[2\] |
| J10 | U1 | MIBSPI5SOMI\[0\]/MII\_TXD\[0\]/RMII\_TXD\[0\] |
| J10 | U1 | MIBSPI5NENA/MII\_RXD\[3\]/MIBSPI5SOMI\[1\]/ECAP5 |
| J10 | U1 | MIBSPI1NENA/N2HET1\[23\]/MII\_RXD\[2\]/ECAP4 |
| J10 | U1 | MIBSPI1CLK |
| J10 | U1 | MIBSPI1SOMI |

# J10 U1 MIBSPI5CLK/MII\_TXEN/RMII\_TXEN

# J10

U1 MIBSPI5SIMO\[0\]/MII\_TXD\[1\]/RMII\_TXD\[1\]/MIBSPI5SOMI\[2\]

# J10

U1 MIBSPI5SOMI\[0\]/MII\_TXD\[0\]/RMII\_TXD\[0\]

# J10

U1 MIBSPI5NENA/MII\_RXD\[3\]/MIBSPI5SOMI\[1\]/ECAP5

# J10

U1 MIBSPI1NENA/N2HET1\[23\]/MII\_RXD\[2\]/ECAP4

# J10 U1 MIBSPI1CLK

# J10 U1 MIBSPI1SOMI

# J10 GND

| J10 | U1 | MIBSPI1SIMO |
|:--- |:--- |:--- |
| J10 | U1 | N2HET1\[26\]/MII\_RXD\[1\]/RMII\_RXD\[1\] |
| J10 | U1 | N2HET1\[24\]/MIBSPI1NCS\[5\]/MII\_RXD\[0\]/RMII\_RXD\[0\] |
| J10 | U1 | DCAN1RX |
| J10 | U1 | DCAN1TX |
| J10 | U1 | AD1EVT/MII\_RX\_ER/RMII\_RX\_ER |
| J10 | U1 | AD1IN\[15\]/AD2IN\[15\] |

# J10 U1 N2HET1\[26\]/MII\_RXD\[1\]/RMII\_RXD\[1\]

# J10

U1 N2HET1\[24\]/MIBSPI1NCS\[5\]/MII\_RXD\[0\]/RMII\_RXD\[0\]

# J10 U1 DCAN1RX

# J10 U1 DCAN1TX

# J10 U1 AD1EVT/MII\_RX\_ER/RMII\_RX\_ER

# J10 U1 AD1IN\[15\]/AD2IN\[15\]

*Hardware* * * *Description* <https://www.ti.com>

SPNU613-May 2017 *Submit Documentation Feedback* Copyright © 2017, Texas Instruments Incorporated *Hercules™TMS570LS12x/RM46 LaunchPad™*

## Table 12. Proto Board Header J10 Connections (continued)

**Header** **Header Pin** **MCU** **MCU** ** ** **Pin** **Description**

| J10 | U1 | AD1IN\[23\]/AD2IN\[7\] |
|:--- |:--- |:--- |
| J10 | U1 | AD1IN\[8\]/AD2IN\[8\] |
| J10 | U1 | AD1IN\[14\]/AD2IN\[14\] |
| J10 | U1 | AD1IN\[22\]/AD2IN\[6\] |
| J10 | U1 | AD1IN\[13\]/AD2IN\[13\] |
| J10 | U1 | AD1IN\[5\] |
| J10 | U1 | AD1IN\[6\] |
| J10 | U1 | AD1IN\[12\]/AD2IN\[12\] |
| J10 | U1 | AD1IN\[11\]/AD2IN\[11\] |

# J10 U1 AD1IN\[8\]/AD2IN\[8\]

# J10 U1 AD1IN\[14\]/AD2IN\[14\]

# J10 U1 AD1IN\[22\]/AD2IN\[6\]

# J10 U1 AD1IN\[13\]/AD2IN\[13\]

# J10 U1 AD1IN\[5\]

# J10 U1 AD1IN\[6\]

# J10 U1 AD1IN\[12\]/AD2IN\[12\]

# J10 U1 AD1IN\[11\]/AD2IN\[11\]

## Table 13. Proto Board Header J11 Connections

**Header** **Header Pin** **MCU** **MCU** ** ** **Pin** **Description**

| J11 | +5 V |
|:--- |:--- |
| J11 | GND |
| J11 | +3V3 |
| J11 | GND |

# J11 GND

# J11 +3V3

# J11 GND

| J11 | U1 | GIOB\[2\] |
|:--- |:--- |:--- |
| J11 | U1 | GIOB\[3\] |
| J11 | U1 | GIOA\[0\] |
| J11 | U1 | MIBSPI3NCS\[3\]/I2C\_SCL/N2HET1\[29\]/NTZ1 |
| J11 | U1 | MIBSPI3NCS\[2\]/I2C\_SDA/N2HET1\[27\]/NTZ2 |
| J11 | U1 | GIOA\[1\] |
| J11 | U1 | N2HET1\[11\]/MIBSPI3NCS\[4\]/N2HET2\[18\]/EPWM1SYNCO |
| J11 | U1 | GIOA\[2\]/N2HET2\[0\]/EQEP2I |
| J11 | U1 | DCAN3RX |

# J11 U1 GIOB\[3\]

# J11 U1 GIOA\[0\]

# J11 U1 MIBSPI3NCS\[3\]/I2C\_SCL/N2HET1\[29\]/NTZ1

# J11 U1 MIBSPI3NCS\[2\]/I2C\_SDA/N2HET1\[27\]/NTZ2

# J11 U1 GIOA\[1\]

# J11

U1 N2HET1\[11\]/MIBSPI3NCS\[4\]/N2HET2\[18\]/EPWM1SYNCO

# J11 U1 GIOA\[2\]/N2HET2\[0\]/EQEP2I

# J11 U1 DCAN3RX

# J11 GND

| J11 | U1 | DCAN3TX |
|:--- |:--- |:--- |
| J11 | U1 | GIOA\[5\]/EXTCLKIN/EPWM1A |
| J11 | U1 | N2HET1\[22\] |
| J11 | U1 | GIOA\[6\]/N2HET2\[4\]/EPWM1B |
| J11 | U1 | GIOA\[7\]/N2HET2\[6\]/EPWM2A |
| J11 | U1 | N2HET1\[0\]/SPI4CLK/EPWM2B |
| J11 | U1 | N2HET1\[1\]/SPI4NENA/N2HET2\[8\]/EQEP2A |
| J11 | U1 | N2HET1\[3\]/SPI4NCS\[0\]/N2HET2\[10\]/EQEP2B |

# J11 U1 GIOA\[5\]/EXTCLKIN/EPWM1A

# J11 U1 N2HET1\[22\]

# J11 U1 GIOA\[6\]/N2HET2\[4\]/EPWM1B

# J11 U1 GIOA\[7\]/N2HET2\[6\]/EPWM2A

# J11 U1 N2HET1\[0\]/SPI4CLK/EPWM2B

# J11 U1 N2HET1\[1\]/SPI4NENA/N2HET2\[8\]/EQEP2A

# J11

U1 N2HET1\[3\]/SPI4NCS\[0\]/N2HET2\[10\]/EQEP2B

# J11 GND

| J11 | U1 | N2HET1\[2\]/SPI4SIMO/EPWM3A |
|:--- |:--- |:--- |
| J11 | U1 | N2HET1\[5\]/SPI4SOMI/N2HET2\[12\]/EPWM3B |
| J11 | U1 | MIBSPI5NCS\[0\]/EPWM4A |
| J11 | U1 | N2HET1\[4\]/EPWM4B |
| J11 | U1 | N2HET1\[7\]/N2HET2\[14\]/EPWM7B |
| J11 | U1 | N2HET1\[9\]/N2HET2\[16\]/EPWM7A |
| J11 | U1 | MIBSPI3NCS\[1\]/N2HET1\[25\]/MDCLK |
| J11 | U1 | MIBSPI1NCS\[2\]/N2HET1\[19\]/MDIO |

# J11 U1 N2HET1\[5\]/SPI4SOMI/N2HET2\[12\]/EPWM3B

# J11 U1 MIBSPI5NCS\[0\]/EPWM4A

# J11 U1 N2HET1\[4\]/EPWM4B

# J11 U1 N2HET1\[7\]/N2HET2\[14\]/EPWM7B

# J11 U1 N2HET1\[9\]/N2HET2\[16\]/EPWM7A

# J11 U1 MIBSPI3NCS\[1\]/N2HET1\[25\]/MDCLK

# J11 U1 MIBSPI1NCS\[2\]/N2HET1\[19\]/MDIO

# J11 GND

# J11 U1 N2HET1\[6\]/SCIRX/EPWM5A

# J11 U1 N2HET1\[13\]/SCITX/EPWM5B

<https://www.ti.com> *Hardware* * * *Description*

SPNU613-May 2017 *Submit Documentation Feedback*

Copyright © 2017, Texas Instruments Incorporated *Hercules™TMS570LS12x/RM46 LaunchPad™*

## Table 13. Proto Board Header J11 Connections (continued)

**Header** **Header Pin** **MCU** **MCU** ** ** **Pin** **Description**

| J11 | U1 | N2HET1\[15\]/MIBSPI1NCS\[4\]/ECAP1 |
|:--- |:--- |:--- |
| J11 | U1 | MIBSPI3SOMI/AWM\_EXT\_ENA/ECAP2 |
| J11 | U1 | MIBSPI3SIMO/AWM\_EXT\_SEL\[0\]/ECAP3 |
| J11 | U1 | MIBSPI3CLK/AWM\_EXT\_SEL\[1\]/EQEP1A |
| J11 | U1 | MIBSPI3NENA/MIBSPI3NCS\[5\]/N2HET1\[31\]/EQEP1B |
| J11 | U1 | MIBSPI3NCS\[0\]/AD2EVT/GIOB\[2\]/EQEP1I |
| J11 | U1 | AD1IN\[16\]/AD2IN\[0\] |
| J11 | U1 | AD1IN\[17\]/AD2IN\[1\] |
| J11 | U1 | AD1IN\[18\]/AD2IN\[2\] |
| J11 | U1 | AD1IN\[19\]/AD2IN\[3\] |
| J11 | U1 | AD1IN\[20\]/AD2IN\[4\] |
| J11 | U1 | AD1IN\[21\]/AD2IN\[5\] |
| J11 | U1 | ADREFHI |
| J11 | U1 | ADREFLO |
| J11 | U1 | AD1IN\[9\]/AD2IN\[9\] |
| J11 | U1 | AD1IN\[10\]/AD2IN\[10\] |

# J11 U1 MIBSPI3SOMI/AWM\_EXT\_ENA/ECAP2

# J11 U1 MIBSPI3SIMO/AWM\_EXT\_SEL\[0\]/ECAP3

# J11 U1 MIBSPI3CLK/AWM\_EXT\_SEL\[1\]/EQEP1A

# J11

U1 MIBSPI3NENA/MIBSPI3NCS\[5\]/N2HET1\[31\]/EQEP1B

# J11 U1 MIBSPI3NCS\[0\]/AD2EVT/GIOB\[2\]/EQEP1I

# J11 U1 AD1IN\[16\]/AD2IN\[0\]

# J11 U1 AD1IN\[17\]/AD2IN\[1\]

# J11 U1 AD1IN\[18\]/AD2IN\[2\]

# J11 U1 AD1IN\[19\]/AD2IN\[3\]

# J11 U1 AD1IN\[20\]/AD2IN\[4\]

# J11 U1 AD1IN\[21\]/AD2IN\[5\]

# J11 U1 ADREFHI

# J11 U1 ADREFLO

# J11 U1 AD1IN\[9\]/AD2IN\[9\]

# J11 U1 AD1IN\[10\]/AD2IN\[10\]

## 2.11 ***External JTAG*** *** *** ***Header***

## Header J1 allows the use of an external (presumably faster or more convenient) JTAG controller with the LaunchPad, in place of the on-board XDS100v2.

## This header is not populated. The footprint supports a 20-pin TI JTAG header. You can install a header

such as the Samtec FTR-110-51-S-D-06 in this footprint. Make sure that pin 6 of the header you install is removed as this is used as a key.

## The LaunchPad on-board XDS110 will detect the external emulator by sensing that pin J1-8 is pulled to

ground and this will cause it to automatically 3-state its drive of the MCU JTAG lines and allow the external JTAG emulator to take control of the MCU.

## Table 14. External JTAG Debug Header J1

**Header** **Header Pin** **MCU** **MCU** ** ** **Pin** **Description**

| J1 | U1 | TMS |
|:--- |:--- |:--- |
| J1 | U1 | NTRST |
| J1 | U1 | TDI |

# J1 U1 NTRST

# J1 U1 TDI

# J1 GND

# J1 +3V3

# J1 U1 TDO

J1 EXTERNAL\_DEBUG (XDS110 Senses External Debugger through This Pin)

# J1 U1 RTCK

# J1 GND

# J1 U1 TCK

| J1 | GND |
|:--- |:--- |
| J1 | MR\_PB (Tied to Power On Reset Push Button) |
| J1 | GND |
| J1 | GND |

J1 MR\_PB (Tied to Power On Reset Push Button)

# J1 GND

# J1 GND

*Software* * * *Development* <https://www.ti.com>

SPNU613-May 2017 *Submit Documentation Feedback* Copyright © 2017, Texas Instruments Incorporated *Hercules™TMS570LS12x/RM46 LaunchPad™* **Software** ** ** **Development**

***3.1*** ***Getting*** *** *** ***Started Demonstration Programs***

The LaunchPad wiki pages contain a few simple projects that help you get started with software development these platforms. The wiki pages are: <http://processors.wiki.ti.com/index.php/LAUNCHXL2TMS57012> for LAUNCHXL2-TMS570LS012 and <http://processors.wiki.ti.com/index.php/LAUNCHXL2RM46> for LAUNCHXL2-RM46

***3.2*** ***Hardware*** *** *** ***Abstraction Layer*** *** *** ***Code*** *** *** ***Generator*** *** *** ***for Hercules MCUs (HALOGEN)***

HALOGEN provides a graphical user interface that allows the user to configure peripherals, interrupts, clocks, and other microcontroller parameters. Once the device is configured, the user can generate peripheral initialization and driver code, which can be imported into CCS, IAR Workbench, or Keil uVision.

HALCoGen is available from <http://www.ti.com/tool/halcogen>. The files that are generated by HalCoGen are distributed under an open-source (BSD style) license.

***3.3*** ***Code*** *** *** ***Composer Studio***

Code Composer Studio includes an optimizing C/C++ compiler, source code editor, project build environment, debugger, profiler, and many other features. It is available for download from <http://www.ti.com/tool/ccstudio-safety>.

***3.4*** ***Other*** *** *** ***Tools and*** *** *** ***Software***

Other available tools and software for Hercules MCUs can be found on the "Tools & Software" tab in the MCU Product folder, or <http://www.ti.com/lsds/ti/microcontrollers\_16-bit\_32bit/c2000\_performance/safety/tools\_software.page>.

SPNU613-May 2017 *Submit Documentation Feedback*

Copyright © 2017, Texas Instruments Incorporated *Schematics*

# Appendix A

# SPNU613-May 2017

# Schematics

## A.1 ***Schematics*** *Schematics* <https://www.ti.com>

SPNU613-May 2017 *Submit* * * *Documentation Feedback*

Copyright © 2017, Texas Instruments Incorporated *Schematics* <https://www.ti.com> *Schematics*

SPNU613-May 2017 *Submit Documentation Feedback*

Copyright © 2017, Texas Instruments Incorporated *Schematics* *Schematics* <https://www.ti.com>

SPNU613-May 2017 *Submit* * * *Documentation Feedback*

Copyright © 2017, Texas Instruments Incorporated *Schematics* <https://www.ti.com> *Schematics*

SPNU613-May 2017 *Submit Documentation Feedback*

Copyright © 2017, Texas Instruments Incorporated *Schematics* *Schematics* <https://www.ti.com>

SPNU613-May 2017 *Submit* * * *Documentation Feedback*

Copyright © 2017, Texas Instruments Incorporated *Schematics* <https://www.ti.com> *Schematics*

SPNU613-May 2017 *Submit Documentation Feedback*

Copyright © 2017, Texas Instruments Incorporated *Schematics* *Schematics* <https://www.ti.com>

SPNU613-May 2017 *Submit* * * *Documentation Feedback*

Copyright © 2017, Texas Instruments Incorporated *Schematics* <https://www.ti.com> *Schematics*

SPNU613-May 2017 *Submit Documentation Feedback*

Copyright © 2017, Texas Instruments Incorporated *Schematics* *Schematics* <https://www.ti.com>

SPNU613-May 2017 *Submit* * * *Documentation Feedback*

Copyright © 2017, Texas Instruments Incorporated *Schematics* <https://www.ti.com> *Schematics*

SPNU613-May 2017 *Submit Documentation Feedback*

Copyright © 2017, Texas Instruments Incorporated *Schematics* *Schematics* <https://www.ti.com>

SPNU613-May 2017 *Submit* * * *Documentation Feedback*

Copyright © 2017, Texas Instruments Incorporated *Schematics* <https://www.ti.com> *Schematics*

SPNU613-May 2017 *Submit Documentation Feedback*

Copyright © 2017, Texas Instruments Incorporated *Schematics* *Schematics* <https://www.ti.com>

SPNU613-May 2017 *Submit* * * *Documentation Feedback*

Copyright © 2017, Texas Instruments Incorporated *Schematics* <https://www.ti.com> *Schematics*

SPNU613-May 2017 *Submit Documentation Feedback*

Copyright © 2017, Texas Instruments Incorporated *Schematics*

SPNU613-May 2017 *Submit Documentation Feedback* Copyright © 2017, Texas Instruments Incorporated *Design* * * *File* * * *Sources*

## Appendix B

# SPNU613-May 2017

# Design File Sources

## B.1 ***Design File*** *** *** ***Sources***

Design file sources are available for download from: <http://www.ti.com/lit/zip/spnu613>.

SPNU613-May 2017 *Submit Documentation Feedback*

Copyright © 2017, Texas Instruments Incorporated *Regulatory Information*

# Appendix C

# SPNU613-May 2017

# Regulatory Information

## C.1 ***EMC Compliance***

## This is a class A product as defined by standard EN 61326-1:2013. For important information regarding

the use of this product in a domestic environment, see the attached "STANDARD TERMS FOR EVALUATION MODULES".

## C.2

***Electrostatic*** *** *** ***Discharge Caution***

This EVM can be damaged by ESD. Texas Instruments recommends this EVM be handled with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage. ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may be more susceptible to damage because very small parametric changes could cause the device not to meet its published specifications. For more information on proper handling, see Electrostatic Discharge (ESD).

# IMPORTANT NOTICE FOR TI DESIGN INFORMATION AND RESOURCES

Texas Instruments Incorporated ('TI") technical, application or other design advice, services or information, including, but not limited to, reference designs and materials relating to evaluation modules, (collectively, "TI Resources") are intended to assist designers who are developing applications that incorporate TI products; by downloading, accessing or using any particular TI Resource in any way, you (individually or, if you are acting on behalf of a company, your company) agree to use it solely for this purpose and subject to the terms of this Notice.

TI's provision of TI Resources does not expand or otherwise alter TI's applicable published warranties or warranty disclaimers for TI products, and no additional obligations or liabilities arise from TI providing such TI Resources. TI reserves the right to make corrections, enhancements, improvements and other changes to its TI Resources.

You understand and agree that you remain responsible for using your independent analysis, evaluation and judgment in designing your applications and that you have full and exclusive responsibility to assure the safety of your applications and compliance of your applications (and of all TI products used in or for your applications) with all applicable regulations, laws and other applicable requirements. You represent that, with respect to your applications, you have all the necessary expertise to create and implement safeguards that (1) anticipate dangerous consequences of failures, (2) monitor failures and their consequences, and (3) lessen the likelihood of failures that might cause harm and take appropriate actions. You agree that prior to using or distributing any applications that include TI products, you will thoroughly test such applications and the functionality of such TI products as used in such applications. TI has not conducted any testing other than that specifically described in the published documentation for a particular TI Resource.

You are authorized to use, copy and modify any individual TI Resource only in connection with the development of applications that include the TI product(s) identified in such TI Resource. NO OTHER LICENSE, EXPRESS OR IMPLIED, BY ESTOPPEL OR OTHERWISE TO ANY OTHER TI INTELLECTUAL PROPERTY RIGHT, AND NO LICENSE TO ANY TECHNOLOGY OR INTELLECTUAL PROPERTY RIGHT OF TI OR ANY THIRD PARTY IS GRANTED HEREIN, including but not limited to any patent right, copyright, mask work right, or other intellectual property right relating to any combination, machine, or process in which TI products or services are used. Information regarding or referencing third-party products or services does not constitute a license to use such products or services, or a warranty or endorsement thereof. Use of TI Resources may require a license from a third party under the patents or other intellectual property of the third party, or a license from TI under the patents or other intellectual property of TI.

# TI RESOURCES ARE PROVIDED "AS IS" AND WITH ALL FAULTS. TI DISCLAIMS ALL OTHER WARRANTIES OR

REPRESENTATIONS, EXPRESS OR IMPLIED, REGARDING TI RESOURCES OR USE THEREOF, INCLUDING BUT NOT LIMITED TO ACCURACY OR COMPLETENESS, TITLE, ANY EPIDEMIC FAILURE WARRANTY AND ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT OF ANY THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.

# TI SHALL NOT BE LIABLE FOR AND SHALL NOT DEFEND OR INDEMNIFY YOU AGAINST ANY CLAIM, INCLUDING BUT NOT

LIMITED TO ANY INFRINGEMENT CLAIM THAT RELATES TO OR IS BASED ON ANY COMBINATION OF PRODUCTS EVEN IF DESCRIBED IN TI RESOURCES OR OTHERWISE. IN NO EVENT SHALL TI BE LIABLE FOR ANY ACTUAL, DIRECT, SPECIAL, COLLATERAL, INDIRECT, PUNITIVE, INCIDENTAL, CONSEQUENTIAL OR EXEMPLARY DAMAGES IN CONNECTION WITH OR ARISING OUT OF TI RESOURCES OR USE THEREOF, AND REGARDLESS OF WHETHER TI HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

You agree to fully indemnify TI and its representatives against any damages, costs, losses, and/or liabilities arising out of your noncompliance with the terms and provisions of this Notice.

This Notice applies to TI Resources. Additional terms apply to the use and purchase of certain types of materials, TI products and services. These include; without limitation, TI's standard terms for semiconductor products <http://www.ti.com/sc/docs/stdterms.htm> ), evaluation modules, and samples ( <http://www.ti.com/sc/docs/sampterms.htm> ).

Mailing Address: Texas Instruments, Post Office Box 655303, Dallas, Texas 75265

Copyright © 2017, Texas Instruments Incorporated