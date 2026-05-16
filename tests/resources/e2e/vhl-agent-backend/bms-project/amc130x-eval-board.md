SBAU256C-May 2016-Revised June 2018 *Submit Documentation Feedback*

Copyright © 2016-2018, Texas Instruments Incorporated *AMC130x Evaluation* * * *Module*

(1) All trademarks are the property of their respective owners. (1)

## User's Guide *SBAU256C-May 2016-Revised* * * *June 2018*

# AMC130x Evaluation Module

This user's guide describes the characteristics, operation, and use of the AMC130xEVM. This evaluation module (EVM) is an evaluation and development kit for evaluating the AMC1300 or AMC1301, precision isolation amplifiers. A complete circuit description as well as schematic diagram and bill of materials are included.

The following related documents are available through the Texas Instruments web site at <https://www.ti.com>. **Related** ** ** **Documentation**

| Device | Literature Number |
|:--- |:--- |
| AMC1300 | SBAS895 |
| AMC1301 | SBAS667 |
| AMC1302 | SBAS812 |
| SN6501 | SLLSEA0 |

# AMC1300 SBAS895

# AMC1301 SBAS667

# AMC1302 SBAS812

# SN6501 SLLSEA0

**Contents** EVM Overview............................................................................................................... Analog Interface.............................................................................................................. Power Supplies.............................................................................................................. EVM Operation............................................................................................................... Layout, BOM, and Schematic.............................................................................................. 5 **List** ** ** **of** ** ** **Figures**

AMC130xEVM Schematic: Analog Input Section........................................................................ 2

AMC130xEVM Schematic: Analog Output Section..................................................................... 3

VDD1 Input...................................................................................................................

VDD2 Input Connector......................................................................................................

AMC130x Top Layer Silkscreen........................................................................................... 5

AMC130xEVM Schematic.................................................................................................. **List** ** ** **of** ** ** **Tables**

J1: Analog Inputs............................................................................................................

J2: Isolated Power...........................................................................................................

J3: VDD2 Power.............................................................................................................

J4: Analog Output...........................................................................................................

AMC130xEVM Bill of Materials............................................................................................ 6

# J1 isoGND

# DNP

# C8

# DNP

# C4

# DNP

# C5

# R2

# R1

# IN

# + IN *EVM Overview* <https://www.ti.com> SBAU256C-May 2016-Revised June 2018

*Submit Documentation Feedback* Copyright © 2016-2018, Texas Instruments Incorporated *AMC130x Evaluation* * * *Module* **EVM** ** ** **Overview** ***1.1*** ***Features***

This EVM supports the following features: - • Full-featured evaluation board for the AMC1300, AMC1301, or AMC1302 single-channel precision isolation amplifier - • Screw terminals for easy access to analog inputs and outputs - • Optional isolated power to VDD1 from VDD2 ***1.2*** ***Introduction***

The AMC1300, AMC1301, and AMC1302 are precision isolation amplifiers with an output separated from the input circuitry by a silicon dioxide (SiO 2 ) barrier that is highly resistant to magnetic interference. This barrier has been certified to provide basic galvanic isolation of up to 7000 V PEAK according to UL1577 and IEC60747-5-2 specifications.

For use in high-resolution measurement applications, the input of the AMC1300, AMC1301, and AMC1302 is optimized for direct connection to shunt resistors or other low-level signal sources.

Throughout this document, the abbreviation * * *EVM* and the term * evaluation* * * *module* are synonymous with the AMC130xEVM. **Analog** ** ** **Interface**

The analog inputs to the AMC1300, AMC1301, and AMC1302 are routed from the two-wire screw terminal at J1. These screw terminals provide access to the inverting and noninverting inputs of the AMC130x device installed at U2. ***2.1*** ***Analog*** *** *** ***Inputs***

The analog inputs to the AMC130xEVM printed-circuit board (PCB) consists of optional RC filter circuit. By default, R1 and R2 on the analog input are populated as 0- Ω resistors. Capacitors C4, C5, and C8 are not installed. An example input circuit for the AMC130x is shown in Figure 1.

**Figure 1. AMC130xEVM Schematic:** ** ** **Analog Input Section**

# VDD2

# DGND

# J3 10µF

# C11

# VDD2 VDD1 5Viso

# VDD2 VDD2

# J2

# DGND 4.7µF

# C1 22µF

# C2

# DGND 22µF

# C6

# J3 10µF

# C11 isoGND isoGND isoGND isoGND isoGND 1µF C10 0.1µF

# C3

# D1

# D2

# JP1

# D1

# VCC

# D2

# GND

# GND

# U3

# SN6501DBV

# T1

# DA2303-ALB

# IN

# GND EN

# NC

# OUT U1

# TPS76350DBV

# VOUT+

# VOUT

# J4 <https://www.ti.com> *Analog* * * *Interface*

SBAU256C-May 2016-Revised June 2018 *Submit Documentation Feedback*

Copyright © 2016-2018, Texas Instruments Incorporated *AMC130x Evaluation* * * *Module* ***2.2*** ***Analog*** *** *** ***Outputs***

The analog outputs from the AMC130xEVM board are fully-differential signals centered at VDD2 / 2. The outputs are available on the two screw terminals of J4, as Figure 2 shows.

**Figure 2. AMC130xEVM** ** ** **Schematic:** ** ** **Analog Output** ** ** **Section** **Power** ** ** **Supplies**

The AMC130xEVM require two separate power rails, VDD1 and VDD2. VDD1 is on the high voltage side of the amplifier. VDD2 is on the user side of the amplifier. ***3.1*** ***VDD1*** *** *** ***Input***

J2 provides access to the to the VDD1 supply. For power provided from high-side isolated rails (such as from a gate-drive supply), move the shunt on jumper JP1 to cover pins 1 and 2. Use a voltage between 4.5 VDC and 5.5 VDC for the user-applied VDD1 supply. In the EVM default configuration, VDD1 is provided from VDD2 by means of an isolation transformer and U3, an SN6501 transformer driver. In the default configuration, apply 5 V to VDD2 through J3. The input power is shown in Figure 3. **Figure 3. VDD1 Input** ***3.2*** ***VDD2*** *** *** ***Input***

The user side of the AMC1300, AMC1301, and AMC1302 isolation amplifier is rated for 2.7 V DC to 5.5 V DC and is applied to the amplifier using J3. Figure 4 illustrates the power input for VDD2. **Figure 4. VDD2 Input Connector** *EVM Operation* <https://www.ti.com> SBAU256C-May 2016-Revised June 2018

*Submit Documentation Feedback* Copyright © 2016-2018, Texas Instruments Incorporated *AMC130x Evaluation* * * *Module*

## EVM Operation

## This section describes the general operation of the AMC130xEVM.

## 4.1

***Isolated*** *** *** ***Power*** *** *** ***and*** *** *** ***Analog*** *** *** ***Inputs:*** *** *** ***J1 and*** *** *** ***J2***

## The analog input to the AMC130xEVM board can be applied directly to J1 pins 1 and 2.

# CAUTION

## For the limitations of the analog input range, and to ensure that the appropriate

analog and digital voltages are applied before connecting any analog input to the EVM, see * AMC1301 Fully-Differential* * * *Isolation* * * *Amplifier*.

## Table 1 summarizes the details of J1.

## Table 1. J1: Analog Inputs **Pin Number** **Signal** **Description**

J1.1 IN+ Noninverting input to the AMC1300, AMC1301, or AMC1302 (pin 2)

J1.2 IN- Inverting analog input to the AMC1300, AMC1301, or AMC1302 (pin 3)

## The isolated power input to the AMC130xEVM PCB can be applied directly to J2, pins 1 and 2. Table 2 lists the details of J2.

## Table 2. J2: Isolated Power **Pin Number** **Signal** **Description**

J2.1 GND1 Connection to the AMC1300, AMC1301, or AMC1302 GND1 terminal (pin 4)

J2.2 VDD1 Connection to the AMC1300, AMC1301, or AMC1302 VDD1 terminal (pin 1)

## 4.2

***User Power*** *** *** ***and*** *** *** ***Analog*** *** *** ***Output:*** *** *** ***J3 and*** *** *** ***J4***

## The VDD2 power input to the AMC130xEVM PCB can be applied directly to J3, pins 1 and 2. Table 3 lists the details of J3.

## Table 3. J3: VDD2 Power **Pin Number** **Signal** **Description**

J3.1 GND2 Connection to the AMC1300, AMC1301, or AMC1302 GND2 terminal (pin 5)

J3.2 VDD2 Connection to the AMC1300, AMC1301, or AMC1302 VDD2 terminal (pin 8)

## The analog output from the AMC130xEVM board is applied directly to J4, pins 1 and 2. Table 4 summarizes the details of J4.

## Table 4. J4: Analog Output **Pin Number** **Signal** **Description**

J4.1 VOUT- Inverting analog output from the AMC1300, AMC1301, or AMC1302 (pin 7)

J4.2 VOUT+ Noninverting output from the AMC1300, AMC1301, or AMC1302 (pin 6)

Copyright © 2017, Texas Instruments Incorporated <https://www.ti.com> *EVM* * * *Operation*

SBAU256C-May 2016-Revised June 2018 *Submit Documentation Feedback*

Copyright © 2016-2018, Texas Instruments Incorporated *AMC130x Evaluation* * * *Module* ***4.3*** ***Device Operation***

After the VDD1 and VDD2 power is applied to the AMC130xEVM, the analog outputs are available with a fixed gain and a dc offset equal to 1.44 V.

An analog input signal may be applied directly at screw terminal J2. Refer to Figure 1 and Table 1 for details. For the AMC1300EVM and AMC1301EVM the differential analog input range, (VIN+) - (VIN-), is specified at ±250 mV with a maximum of ±320 mV before clipping occurs.

The analog output has a nominal gain of 8 through the AMC1300 or AMC1301 isolation amplifier. With an input voltage of ±250 mV, the nominal output is therefore ±2.0 V.

For the AMC1302EVM, the differential analog input range is specified at ±50 mV with a maximum of ±64 mV with a fixed gain of 41 V/V. With an input voltage of ±50 mV, the nominal output is also ±2.0 V. The output voltage of the AMC130xEVM is centered on VDD / 2 and provides a convenient analog input range to the embedded analog-to-digital converters (ADCs) of the MSP430 and TMS320C2000 series of digital processors.

**Layout, BOM,** ** ** **and** ** ** **Schematic**

This sections contains the PCB layout, bill of materials, and schematic of the AMC130xEVM. ***5.1*** ***Layout*** Figure 5 shows the AMC130xEVM PCB layout.

**NOTE:** Board layout is not to scale. This figure is intended to show how the board is laid out; it is not intended to be used for manufacturing AMC130xEVM PCBs.

**Figure 5. AMC130x** ** ** **Top Layer Silkscreen**

*Layout, BOM,* * * *and Schematic* <https://www.ti.com> SBAU256C-May 2016-Revised June 2018

*Submit Documentation Feedback* Copyright © 2016-2018, Texas Instruments Incorporated *AMC130x Evaluation* * * *Module*

## 5.2 ***Bill of Material***

## The bills of material is listed in Table 5.

**NOTE:** All components should be RoHS compliant. Some part numbers may be either leaded or RoHS. Verify that purchased components are RoHS compliant.

## Table 5. AMC130xEVM Bill of Materials

**Item** **Qty** **Ref** ** ** **Des** **Description** **Manufacturer** **Part Number**

| C1 | CAP, CERM, 4.7uF, 50V, +/-10%, X5R, 0805 | TDK | C2012X5R1H475K125AB |
|:--- |:--- |:--- |:--- |
| C2, C6 | CAP, CERM, 22uF, 6.3V, +/-20%, X5R, 0805 | Taiyo Yuden | JMK212BJ226MG-T |
| C3, C7, C9 | CAP, CERM, 0.1uF, 25V, +/-10%, X7R, 0603 | TDK | C1608X7R1E104K |
| C10 | CAP, CERM, 1uF, 16V, +/-10%, X5R, 0603 | TDK | C1608X5R1C105K |
| C11 | CAP, CERM, 10uF, 10V, +/-10%, X5R, 0805 | Murata | GRM219R61A106KE44D |

# C2, C6

CAP, CERM, 22uF, 6.3V, +/-20%, X5R, 0805 Taiyo Yuden JMK212BJ226MG-T

# C3, C7, C9

CAP, CERM, 0.1uF, 25V, +/-10%, X7R, 0603 TDK C1608X7R1E104K

# C10

CAP, CERM, 1uF, 16V, +/-10%, X5R, 0603 TDK C1608X5R1C105K

# C11

CAP, CERM, 10uF, 10V, +/-10%, X5R, 0805 Murata GRM219R61A106KE44D

D1, D2 Diode, Schottky, 20V, 0.5A, SOD-123 ON Semiconductor MBR0520LT1G

J1, J2, J3, J4 Terminal Block, 6A, 3.5mm Pitch, 2-Pos, TH On-Shore Technology ED555/2DS

| JP1 | 3x1 2mm male header | Samtec | TMM-103-01-T-S |
|:--- |:--- |:--- |:--- |
| R1, R2 | RES, 0 ohm, 5%, 0.1W, 0603 | Rohm | MCR03EZPJ000 |
| T1 | Isolation Transformer | Coilcraft | DA2303-ALB |
| U1 | TPS76350DBV | TI | TPS76350DBV |

# R1, R2 RES, 0 ohm, 5%, 0.1W, 0603 Rohm MCR03EZPJ000 T1 Isolation Transformer Coilcraft DA2303-ALB

# U1 TPS76350DBV TI TPS76350DBV

# U2

AMC1300BDWV or AMC1301BDWV TI AMC1300BDWV or AMC1301BDWV

# U3 SN6501DBV TI SN6501DBV

# C4, C5

DNP - Optional CAP, CERM, 10pF, 50V, +/5%, C0G/NP0, 0603 AVX 06035A100JAT2A

# C8

DNP - Optional CAP, CERM, 330pF, 50V, +/5%, C0G/NP0, 0603 TDK C1608C0G1H331J N/A Shunt Samtec 2SN-BK-G

| D | D |
|:--- |:--- |
| C | C |
| B | B |
| A | A |

# C C

# B B

# A A 2/25/2016 PA023\_AMC1301\_sch\_A.SchDoc Sheet Title: Size: Mod. Date:

File: Sheet: of B <http://www.ti.com> Contact: <http://www.ti.com/support>

AMC1301EVM Project Title: Designed for: Public Release Assembly Variant: \[No Variations\]

© Texas Instruments 2016 Drawn By: Engineer: Tom Hendrick

Texas Instruments and/or its licensors do not warrant the ac curacy or completeness of this specification or any informa tion contained therein. Texas Instruments and/or its licen sors do not warrant that this design will meet the specifications, will be suitable for your application or fit for any particular pu rpose, or will operate in an implementation. Texas Instrume nts and/or its licensors do not warrant that the design is production worth - You should completely validate and test your design imple mentation to confirm the system functionality for your appl icatio Version control disabled SVN Rev: PA0023 Number: Rev: E1

# VDD2

| VDD1 | 5Viso |
|:--- |:--- |
| 5Viso | VDD2 |
| VDD2 | VDD2 | 5Viso VDD2

# VDD2 VDD2

# J2

# DGND 4.7µF

# C1 22µF

# C2

# DGND

# J1 22µF

# C6

# J4

# J3 10µF

# C11 isoGND isoGND isoGND isoGND isoGND isoGND isoGND

# DGND 1µF C10 isoGND

# DNP

# C8

# DNP

# C4

# DNP

# C5

# DGND 0.1µF

# C3 0.1µF C7 0.1µF C9

# D1

# D2

# JP1

# D1

# VCC

# D2

# GND

# GND

# U3

# SN6501DBV

# T1

# DA2303-ALB

# IN

# GND EN

# NC

# OUT U1

# TPS76350DBV

# R2

# R1

# VDD1

# VINP

# VINN

# GND1 GND2

# VOUTN

# VOUTP

# VDD2

# U2

# AMC1301DWVR

# Copyright © 2016, Texas Instruments Incorporated

# www.ti.com *Layout, BOM,* * * *and Schematic*

# SBAU256C-May 2016-Revised June 2018 *Submit Documentation Feedback*

# Copyright © 2016-2018, Texas Instruments Incorporated

# AMC130x Evaluation Module

# 5.3 ***Schematic***

# Figure 6 shows the AMC130xEVM schematic.

# Figure 6. AMC130xEVM Schematic *Revision* * * *History* <https://www.ti.com> SBAU256C-May 2016-Revised June 2018

*Submit Documentation Feedback* Copyright © 2016-2018, Texas Instruments Incorporated *Revision History*

**Revision History** NOTE: Page numbers for previous revisions may differ from page numbers in the current version.

**Changes** ** ** **from** ** ** **B** ** ** **Revision** ** ** **(May 2018) to** ** ** **C** ** ** **Revision**...................................................................................................... ** ** **Page**

- • Added AMC1302 device to user's guide............................................................................................... - • Changed * Device Operation* section to differentiate between the AMC1300EVM and AMC1301EVM functionality and the AMC1302EVM functionality..............................................................................................................

## Revision History

**Changes** ** ** **from** ** ** **A** ** ** **Revision** ** ** **(August** ** ** **2016) to** ** ** **B** ** ** **Revision**................................................................................................ ** ** **Page**

- • Changed user's guide title from AMC1301EVM to AMC130xEVM to include additional devices.............................. 1 - • Added AMC1300 device to user's guide...............................................................................................

## Revision History

**Changes** ** ** **from** ** ** **Original** ** ** **(May 2016) to** ** ** **A** ** ** **Revision**........................................................................................................... ** ** **Page**

- • Changed dc offset statement in first paragraph of the * Device Operation* section................................................ 5

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

Copyright © 2018, Texas Instruments Incorporated