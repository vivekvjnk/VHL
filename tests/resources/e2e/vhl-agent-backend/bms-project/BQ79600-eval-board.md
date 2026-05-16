# User's Guide ***BQ79600-Q1 Evaluation Module***

# ABSTRACT

The BQ79600-Q1 Evaluation Module user's guide describes the general features, theory of operation, hardware setup, and use of the BQ79600EVM. Throughout this user's guide, the abbreviations *EVM*, *BQ79600EVM*, and the term *evaluation module* are synonymous with the *BQ79600-Q1 Evaluation Module*, unless otherwise noted. This EVM is an evaluation board for the *BQ79600-Q1* device used as a bridge IC to interface between a microcontroller and the TI battery monitoring ICs (for example, BQ7961x-Q1 and BQ79606A-Q1). The device translates between the daisy chain interface and SPI/UART interface.

## Table of Contents

**1 General Description**................................................................................................................................................................ 3

1.1 Key Features...................................................................................................................................................................... 3 1.2 Key Electrical Parameters.................................................................................................................................................. 3 **2 Theory of Operation**................................................................................................................................................................ 4

2.1 Compatibility with Battery Monitoring Devices................................................................................................................... 5 **3 Connectors**.............................................................................................................................................................................. 6

3.1 Primary Input and Output Connectors................................................................................................................................ 6 **4 BQ79600EVM Quick Start Guide**.......................................................................................................................................... 11

4.1 Required Devices for Using the Example Code \*Not Available Yet\*................................................................................ 11 4.2 Power Connections.......................................................................................................................................................... 11 4.3 Connecting the BQ79600EVM to TMS570 LaunchPad.................................................................................................... 11 4.4 Connecting BQ79600EVM to BQ79616EVM................................................................................................................... 12 4.5 Connecting BQ79600EVM to BQ79606EVM................................................................................................................... 12 4.6 Software \*Not yet available\*............................................................................................................................................. 13 4.7 GUI................................................................................................................................................................................... 13 **5 Physical Dimensions**............................................................................................................................................................ 14

5.1 Board Dimensions............................................................................................................................................................ 14 5.2 Board Mounting................................................................................................................................................................ 14 **6 Schematics, Assembly, Layout, and Bill of Materials (BOM)**............................................................................................ 15

6.1 Schematics....................................................................................................................................................................... 15 6.2 Assembly.......................................................................................................................................................................... 16 6.3 Layout.............................................................................................................................................................................. 17 6.4 Bill of Materials (BOM)..................................................................................................................................................... 22 **7 Revision History**................................................................................................................................................................... 24

**List of Figures** Figure 2-1. System Block Diagram.............................................................................................................................................. 4 Figure 3-1. Keystone5010 (reference image only)...................................................................................................................... 6 Figure 3-2. Samtec Inc. TSW-105-08-L-D-RA (reference image only)........................................................................................ 7 Figure 3-3. Molex 0022124062 (reference image only)............................................................................................................... 8 Figure 3-4. Samtec SSQ-110-03-T-D (reference image only)...................................................................................................... 8 Figure 4-1. Basic EVM Setup..................................................................................................................................................... 11 Figure 4-2. Connection Between BQ79600EVM and TMS570 LaunchPad.............................................................................. 12 Figure 5-1. Board Dimensions................................................................................................................................................... 14 Figure 6-1. BQ79600EVM Schematic Part 1............................................................................................................................. 15 Figure 6-2. BQ79600EVM Schematic Part 2............................................................................................................................. 16 Figure 6-3. BQ79600EVM Assembly Top.................................................................................................................................. 16 Figure 6-4. BQ79600EVM Assembly Bottom............................................................................................................................ 17 Figure 6-5. BQ79600EVM Top Overlay..................................................................................................................................... 17 Figure 6-6. BQ79600EVM Bottom Overlay................................................................................................................................ 18 <https://www.ti.com> *Table of Contents*

SLUUC57B - OCTOBER 2019 - REVISED AUGUST 2023 *Submit Document Feedback* *BQ79600-Q1 Evaluation Module*

Figure 6-7. BQ79600EVM Top Solder....................................................................................................................................... 18 Figure 6-8. BQ79600EVM Top Layer......................................................................................................................................... 19 Figure 6-9. BQ79600EVM Internal Signal Layer 1 - GND Plane............................................................................................... 19 Figure 6-10. BQ79600EVM Internal Signal Layer 2 - GND Plane............................................................................................. 20 Figure 6-11. BQ79600EVM Bottom Layer................................................................................................................................. 20 Figure 6-12. BQ79600EVM Bottom Solder................................................................................................................................ 21 Figure 6-13. BQ79600EVM Drill Drawing.................................................................................................................................. 21

**List of Tables** Table 1-1. Key Electrical Parameters........................................................................................................................................... 3 Table 3-1. Jumper Placements.................................................................................................................................................... 6 Table 3-2. Pin Description............................................................................................................................................................ 7 Table 3-3. Connector Information................................................................................................................................................ 7 Table 3-4. Pin Description............................................................................................................................................................ 7 Table 3-5. Connector Information................................................................................................................................................ 8 Table 3-6. Connector Information................................................................................................................................................ 8 Table 3-7. Pin Description - J7..................................................................................................................................................... 8 Table 3-8. Pin Description - J9..................................................................................................................................................... 9 Table 3-9. Connector Information.............................................................................................................................................. 10 Table 3-10. Pin Description - J10............................................................................................................................................... 10 Table 3-11. Pin Description - J11............................................................................................................................................... 10 Table 4-1. Connections Between BQ79600EVM High Side and BQ79616EVM Low Side........................................................ 12 Table 4-2. Connections Between BQ79616EVM High Side and BQ79600EVM Low Side (for ring architecture only).............. 12 Table 4-3. Connections Between BQ79600EVM High Side and BQ79606EVM Low Side........................................................ 13 Table 4-4. Connections Between BQ79606EVM High Side and BQ79600EVM Low Side (for ring architecture only).............. 13 Table 6-1. Bill of Materials......................................................................................................................................................... 22

**Trademarks** LaunchPad ™ and Code Composer Studio ™ are trademarks of Texas Instruments. All trademarks are the property of their respective owners. *Trademarks* <https://www.ti.com>

*BQ79600-Q1 Evaluation Module* SLUUC57B - OCTOBER 2019 - REVISED AUGUST 2023 *Submit Document Feedback*

## 1 General Description

TI's *BQ79600EVM Battery Management System* (BMS) is an evaluation board for the *BQ79600-Q1* device used as a bridge IC to interface between a microcontroller and the TI battery monitoring ICs (for example, BQ7961xQ1 and BQ79606A-Q1). The BQ79600EVM can be powered through a PMIC device or directly through a 12-V battery. The device has an Auto Host Wake-up function that can be utilized with the BQ7961x-Q1 family to automatically wake up the host when an unmasked fault is detected in the battery monitoring ICs when using ring architecture. See the *BQ79600-Q1 data sheet* for more details.

The BQ79600EVM enables communication between a controller and one or more battery modules to perform State of Charge (SOC) and State of Health (SOH) estimation. The EVM is equipped with an UART/SPI to enable a host device to communicate to the BQ79600-Q1 device and an isolated differential daisy chain interface to enable communication to a stack of battery monitoring ICs. The BQ79600EVM acts as a communication bridge between the host and the battery modules.

The BQ79600EVM is controlled using a PC-hosted GUI. Communication between the PC and the BQ79600EVMs is through an USB2ANY UART interface or an USB2ANY SPI. Communication between the BQ79600EVM and all BQ79616EVMs in the stack is via the isolated, daisy-chain differential communication bus. The GUI allows configuration of the BQ79600EVMs to configure the communication interface to the host (UART/SPI) and to the stacked devices, as well as to enable/disable the automatic host wake-up function. The BQ79616EVMs can also be configured using the GUI to monitor cells and other analog data channels, control balancing, and monitor details of any faults. **1.1 Key Features** This EVM includes the following features:

- • UART interface for communication to the host, configurable through jumpers - • SPI for communication to the host, configurable through jumpers - • Supports host communication through FTDI (UART only), USB2ANY, or TMS57012 microcontroller (direct  connection to XL2-TMS57012 LAUNCHPAD boosterpack) - • Isolated differential daisy chain communications with optional ring architecture - • Jumpers to configure 5-V or 12-V options (use 5-V option when powering through PMIC and 12-V option  when powering directly from 12-V battery and to use automatic host wake-up function) - • LEDs to indicate when the device is awake and when there is an unmasked fault **1.2 Key Electrical Parameters**

The following table identifies the key electrical parameters: **Table 1-1. Key Electrical Parameters**

| Parameter | Value |
|:--- |:--- |
| Maximum operating voltage (BAT pin powered by battery) | 24 V (J1 and J3 shunts placed in 1-2 position) |
| Minimum operating voltage (BAT pin powered by battery) | 5.5 V (J1 and J3 shunts placed in 1-2 position) |
| Maximum operating voltage (BAT pin powered by 5-V regulator) | 5.25 V (J1 and J3 shunts placed in 2-3 position) |
| Minimum operating voltage (BAT pin powered by 5-V regulator) | 4.75 V (J1 and J3 shunts placed in 2-3 position) |
| Ambient temperature | -40 °C to 105 °C |
| SPI clock frequency | 2Mbps to 6Mbps |
| UART baud rate | 1Mbps |
| www.ti.com | General Description |
| SLUUC57B - OCTOBER 2019 - REVISED AUGUST 2023 | Submit Document Feedback |

Maximum operating voltage (BAT pin powered by battery) 24 V (J1 and J3 shunts placed in 1-2 position)

Minimum operating voltage (BAT pin powered by battery) 5.5 V (J1 and J3 shunts placed in 1-2 position)

Maximum operating voltage (BAT pin powered by 5-V regulator) 5.25 V (J1 and J3 shunts placed in 2-3 position)

Minimum operating voltage (BAT pin powered by 5-V regulator) 4.75 V (J1 and J3 shunts placed in 2-3 position) Ambient temperature -40 °C to 105 °C SPI clock frequency 2Mbps to 6Mbps UART baud rate 1Mbps <https://www.ti.com> *General Description*

SLUUC57B - OCTOBER 2019 - REVISED AUGUST 2023 *Submit Document Feedback* *BQ79600-Q1 Evaluation Module*

## 2 Theory of Operation Figure 2-1 shows the system stack diagram. **Figure 2-1. System Block Diagram**

The typical BMS system consists of a Battery Management Unit (BMU) and one or more stacked Cell Monitoring Units (CMU). The BMU must be isolated from the CMU using transformers to keep the high voltage of the stacked battery modules isolated from the BQ79600 bridge device and the microcontroller.

The typical simplified bridge circuit in the BMU system has three main components, as shown in Figure 2-1:

- • Host controller - in this case a TMS570 LaunchPad ™ - • Power management IC (PMIC) - • BQ79600-Q1 isolated communication bridge device - in this case a BQ79600EVM

The BQ79600 device can be powered from the 12-V battery directly or from the PMIC. When powered from the 12-V battery, the reverse wake-up function on the BQ79600 can be used in a ring architecture to wake up the PMIC and the microcontroller with an unmasked fault is detected.

All commands and data between the host and the BQ79600 bridge device are communicated through either a UART or a SPI communication connection. The BQ79600EVM can support a host PC or microcontroller (via the FTDI connection header, the USB2ANY connection header, or the LAUNCHXL2-TMS57012 LaunchPad boosterpack). The BQ79600 remains idle until a command is received from the host. All commands and data between the BQ79600 and the cell monitoring devices, such as BQ79616, is communicated through the daisy chain interface. *Theory of Operation* <https://www.ti.com>

*BQ79600-Q1 Evaluation Module* SLUUC57B - OCTOBER 2019 - REVISED AUGUST 2023 *Submit Document Feedback*

The typical flow for the host to go through is the following simplified sequence:

1. Wake up the BQ79600EVM board by sending a WAKE-UP pulse using the UART/SPI interface. 2. Send a *send wake up* command to the BQ79600EVM to wake up the stacked cell monitoring devices. 3. Autoaddress and initialize bridge and stacked devices. 4. Send a sample command to the BQ79616-Q1 to read the cell measurement results. 5. The host uses the cell measurement data to calculate an average and determine the highest or lowest cells and determine the cells that must be balanced. 6. If no stop command is sent, then the BQ79616-Q1 has a built-in timeout (set by the user), after which time the discharge is stopped automatically. 7. The host can then decide to repeat the process (back to step 4) or return later. When using the BQ79616-Q1 in a ring architecture, the host can enable the sniffer detector on the BQ79600-Q1 and the FAULT tones in the BQ97616-Q1, then send the stacked devices to SLEEP and the bridge and itself to shutdown, and the AUTO reverse wake-up function wakes up the PMIC and MCU if an unmasked fault from the stacked devices is detected by the bridge.

**2.1 Compatibility with Battery Monitoring Devices**

The BQ79600-Q1 is fully compatible with the BQ7961x-Q1 family, supporting automatic host wake up through the INH pin when an unmasked fault is detected in the high voltage battery pack. The BQ79600-Q1 is also compatible with BQ79606A-Q1 devices without the fault interface. <https://www.ti.com> *Theory of Operation*

SLUUC57B - OCTOBER 2019 - REVISED AUGUST 2023 *Submit Document Feedback* *BQ79600-Q1 Evaluation Module*

## 3 Connectors **3.1 Primary Input and Output Connectors**

## 3.1.1 Jumper Placements

## The following table explains each of the jumpers available for user flexibility.

## Table 3-1. Jumper Placements

**Pinheader** **Contacts** **Jumper Connection** **Populated by Default?**

J1 1-2, 2-3 INH connection to 100-k pulldown for 12-V operation (1-2), or to BAT for 5-V operation (2-3) Yes (2-3)

J3 1-2, 2-3 BAT connection to 12-V power supply (1-2), or to CVDD and 5-V power supply (2-3) Yes (2-3)

J5 1-2 LED connection on DVDD to indicate the device is awake Yes

J6 1-2, 2-3 VIO connection to 3.3-V supply from MCU (1-2) or to 5-V supply from MCU (2-3) Yes (1-2)

J8 1-2 LED connection on nFAULT AVDD to indicate a fault on NFAULT pin (must have J13 shunt connected) Yes

J10 1-2, 2-3 nUART\_SPIRDY pullup to VIO for SPI (1-2), or pulldown to GND for UART (2-3) Yes (2-3)

J11 1-2, 2-3 nCS pullup to VIO for SPI (1-2), or pulldown to GND for UART (2-3) Yes (2-3)

J12 1-2, 2-3 SCLK pullup to VIO (1-2) or pulldown to GND for SPI/UART (2-3) Yes (2-3) J13 1-2 NFAULT pullup to VIO Yes

## 3.1.2 Power Supply

## The power supply connection is made from either the 5-V test point or 12-V test point. When powering the EVM

directly through the 12-V battery, configure jumpers J1 and J3 in the "12V" configuration and connect the 12-V battery to the 12-V test point. If the EVM is powered up through a PMIC, configure jumpers J1 and J3 in the "5V" configuration and connect the PMIC 5-V output to the 5-V test point.

## Figure 3-1. Keystone5010 (reference image only) *Connectors* <https://www.ti.com>

*BQ79600-Q1 Evaluation Module* SLUUC57B - OCTOBER 2019 - REVISED AUGUST 2023 *Submit Document Feedback*

## Table 3-2. Pin Description **Pin** **Name** **Comments**

| DVDD | 1.8-V regulated output. DVDD supplies the internal digital circuits |
|:--- |:--- |
| NFAULT | Fault indication output |
| VIO | Power supply input for UART/SPI input/output pins |
| RX/MOSI | UART receiver input or SPI controller out peripheral in |
| TX/MISO | UART transmitter output or SPI controller in peripheral out |
| SCLK | SPI clock input |
| nCS | Active low chip select pin for SPI | NFAULT Fault indication output

VIO Power supply input for UART/SPI input/output pins

RX/MOSI UART receiver input or SPI controller out peripheral in

TX/MISO UART transmitter output or SPI controller in peripheral out SCLK SPI clock input nCS Active low chip select pin for SPI

nUART/SPI (SPI\_RDY) This pin is used as an input pin to select SPI or UART interface before device finishes wakeup/ reset initialization

| GND | Ground |
|:--- |:--- |
| COMLP | AC coupled bi-directional I/O pin for daisy chain (VIF) communication |
| COMLN | AC coupled bi-directional I/O pin for daisy chain (VIF) communication |
| COMHP | AC coupled bi-directional I/O pin for daisy chain (VIF) communication |
| COMHN | AC coupled bi-directional I/O pin for daisy chain (VIF) communication |
| CVDD | Dedicated 5-V supply used for the daisy chain communications |
| BAT | Battery supply Input |
| INH | Inhibit pin to control system voltage regulators |

COMLP AC coupled bi-directional I/O pin for daisy chain (VIF) communication

COMLN AC coupled bi-directional I/O pin for daisy chain (VIF) communication

COMHP AC coupled bi-directional I/O pin for daisy chain (VIF) communication

COMHN AC coupled bi-directional I/O pin for daisy chain (VIF) communication

CVDD Dedicated 5-V supply used for the daisy chain communications BAT Battery supply Input

INH Inhibit pin to control system voltage regulators

## 3.1.3 Host Interface

## There are three different ways for the host to connect to the BQ79600EVM: using the USB2ANY interface

adaptor, the UART FTDI cable ( to communicate through UART only), or using the LAUNCHXL2-TMS57012 microcontroller BoosterPack connector.

## The 10-pin J4 - serial connector is used to connect the BQ79600EVM to a PC running the GUI or to a host

controller. Texas Instruments recommends using the USB2ANY interface adaptor which includes the proper 10-pin cable.

## Figure 3-2. Samtec Inc. TSW-105-08-L-D-RA (reference image only)

## Table 3-3. Connector Information

**Designator** **Manufacturer** **Part Number** **Mating Connector** J4 Samtec Inc. Manufacturer: TSW-105-08-LD-RA 10-pin ribbon connector packaged with USB2ANY

## Table 3-4. Pin Description **Pin** **Name**

# NC nUART/SPI (SPI\_RDY) signal from BQ79600-Q1 <https://www.ti.com> *Connectors*

SLUUC57B - OCTOBER 2019 - REVISED AUGUST 2023 *Submit Document Feedback* *BQ79600-Q1 Evaluation Module*

## Table 3-4. Pin Description (continued) **Pin** **Name**

# USB2ANY SCLK (SCLK of BQ79600-Q1) nFAULT signal from BQ79600-Q1

# GND

# USB2ANY 3.3 V

# USB2ANY TX (MOSI\_RX of BQ79600-Q1)

# USB2ANY RX (MISO\_TX of BQ79600-Q1)

# USB2ANY CS (nCS of BQ79600-Q1)

# NC

## The 6-pin J2 - serial connector is used to connect the BQ79600EVM to a PC running the GUI or to a host

controller through a TTL-232R-5V FTTI cable. Only UART is supported.

## Figure 3-3. Molex 0022124062 (reference image only)

## Table 3-5. Connector Information

**Designator** **Manufacturer** **Part Number** **Mating Connector**

J2 Molex Manufacturer: 0022124062 6-pin connector in TTL-232R-5V FTTI cable

## The 20-pin J7 - serial connector and the 20-pin J9-serial connector are used to connect the BQ79600EVM to a

host controller. The BoosterPack in the LAUNCHXL2-TMS57012 LaunchPad ™ can be directly plugged into the J7 and J9 connectors.

## Figure 3-4. Samtec SSQ-110-03-T-D (reference image only)

## Table 3-6. Connector Information

**Designator** **Manufacturer** **Part Number** **Mating Connector**

J7, J9 Samtec Manufacturer: SSQ-110-03-T-D 20-pin connector 0.100" (2.54mm) in TMS570LS12x LaunchPad ™

## Table 3-7. Pin Description - J7 **Pin** **Name**

# MCU 3.3 V *Connectors* <https://www.ti.com>

*BQ79600-Q1 Evaluation Module* SLUUC57B - OCTOBER 2019 - REVISED AUGUST 2023 *Submit Document Feedback*

## Table 3-7. Pin Description - J7 (continued) **Pin** **Name**

# MCU 5 V

# NC

# GND

# MCU RX (MISO\_TX of BQ79600-Q1)

# NC

# MCU TX (MOSI\_RX of BQ79600-Q1)

# NC

# NC

# NC

# NC

# NC

# MCU SCLK (SCLK of BQ79600-Q1)

# NC

# NC

# NC

# NC

# NC

# NC

# NC

## Table 3-8. Pin Description - J9 **Pin** **Name**

# NC

# GND

# NC

# NC

# NC

# MCU CS (nCS of BQ79600-Q1)

# NC

# NC

# NC

# NC

# NC

# MCU SPI3SIMO ( MOSI\_RX of BQ79600-Q1 )

# NC

# MCU SPI3SOMI ( MISO\_TX of BQ79600-Q1 )

# NC

# NC nUART/SPI (SPI\_RDY) signal from BQ79600-Q1

# NC nFAULT signal from BQ79600-Q1

# NC <https://www.ti.com> *Connectors*

SLUUC57B - OCTOBER 2019 - REVISED AUGUST 2023 *Submit Document Feedback* *BQ79600-Q1 Evaluation Module*

## 3.1.4 High-Side and Low-Side Communications

## There are two sets of 4-position molex connectors available on each board. These provide high-side (J11) and

low-side (J10) communications between stacked EVM devices.

## Table 3-9. Connector Information

**Designator** **Manufacturer** **Part Number** **Mating Connector**

J10/J11 Molex Manufacturer: Digi-Key: WM14059-ND Manufacturer: Digi-Key: WM2902-ND

## Table 3-10. Pin Description - J10 **Pin** **Name** **Comments**

| COML\_N | COM lowside negative |
|:--- |:--- |
| COML\_P | COM lowside positive |
| N/A | Unused |
| N/A | Unused | COML\_P COM lowside positive N/A Unused N/A Unused

## Table 3-11. Pin Description - J11 **Pin** **Name** **Comments**

| N/A | Unused |
|:--- |:--- |
| N/A | Unused |
| COMH\_P | COM highside positive |
| COMH\_N | COM highside negative |
| Connectors | www.ti.com |
| BQ79600-Q1 Evaluation Module | SLUUC57B - OCTOBER 2019 - REVISED AUGUST 2023 | N/A Unused COMH\_P COM highside positive COMH\_N COM highside negative *Connectors* <https://www.ti.com>

*BQ79600-Q1 Evaluation Module* SLUUC57B - OCTOBER 2019 - REVISED AUGUST 2023 *Submit Document Feedback*

## 4 BQ79600EVM Quick Start Guide

This section includes hardware setup instructions, connection procedures, and software and GUI instructions. **Figure 4-1. Basic EVM Setup**

**4.1 Required Devices for Using the Example Code \*Not Available Yet\***

The system example code is implemented using the LAUNCHXL2-TMS57012 LaunchPad ™ board (TMS570LS1224 MCU), the BQ79600EVM, and the BQ79616EVM via Code Composer Studio.

The part numbers of the evaluation modules are LAUNCHXL2-TMS57012, BQ79600EVM-030, BQ79616EVM-021. These boards are available from the TI eStore ( <https://estore.ti.com/> ) or from your local TI sales representative. For more details and information related to the LaunchPad ™ modules, see the specific module user's guide. **4.2 Power Connections**

The BQ79600EVM can be powered up either using a 5-V supply or a 12-V supply. To use the 5-V option, make sure that jumpers J1 and J3 are connected in the "5V" position as labeled in the board, and then connect the positive terminal of the 5-V supply to the "5V" testpoint provided on the board, and the power supply negative terminal to the "GND" testpoint provided on the board, or any "GND" standoff provided. To use the 12-V option, verify that jumpers J1 and J3 are connected in the "12V" position as labeled in the board, and then connect the positive terminal of the 12-V supply to the "12V" testpoint provided on the board, and the power supply negative terminal to the "GND" testpoint provided on the board, or any "GND" standoff provided.

**4.3 Connecting the BQ79600EVM to TMS570 LaunchPad**

The EVMs are connected using the female connectors J7 and J9 on the bottom side of the BQ79600EVM and the male connectors J2, J3, J4, and J5 on the top side of the LAUNCHXL2-TMS57012 LaunchPad ™. Connect the J7 20-pin female connector on the bottom side of the BQ79600EVM to the J2 and J3 10-pin male connectors on top side of the LAUNCHXL2-TMS57012 LaunchPad ™, and J9 20-pin female connector on the bottom side of the BQ79600EVM to the J4 and J5 10-pin male connectors on the top side of the LAUNCHXL2-TMS57012 LaunchPad ™, as shown in the following figure. By default, the TMS570 LaunchPad is powered by the USB port on the host computer. Remove JP1 from the LaunchPad for correct operation.

The microcontroller is used to supply VIO voltage to the device. The user can select either the 3.3-V or 5-V option. To use 3.3 V, make sure that JP2 on the microcontroller LaunchPad is connected and set jumper J6 in

<https://www.ti.com> *BQ79600EVM Quick Start Guide*

SLUUC57B - OCTOBER 2019 - REVISED AUGUST 2023 *Submit Document Feedback* *BQ79600-Q1 Evaluation Module*

## the 1-2 position (this is the default configuration on the EVM). To use 5 V, verify that JP3 on the microcontroller

LaunchPad is connected and set jumper J6 in the 2-3 position.

## Figure 4-2. Connection Between BQ79600EVM and TMS570 LaunchPad

## 4.4 Connecting BQ79600EVM to BQ79616EVM

## The EVMs are connected using 4-position Molex connectors. The BQ79600EVM has a high side (J15)and low

side (J14) communication connector available on each board. By default the isolation filters for the vertical interface on the BQ79600EVM are set to transformer isolation. There are also footprints on the board to populate a different transformer model. More details can be found in the schematic near the end of this user guide. To connect the BQ79600EVM to the BQ79616EVM using NORTH direction for communication, connect J15 on the BQ79600EVM to J10 on the BQ79616EVM. If several BQ79616EVMs are stacked, connect them as indicated in the EVM user's guide for the device. If using ring architecture, connect J11 of the top most BQ79616EVM to J14 on the BQ79600EVM.

## Table 4-1. Connections Between BQ79600EVM High Side and BQ79616EVM Low Side

| Connection Name | BQ79600EVM High Side | BQ79616EVM Low Side |
|:--- |:--- |:--- |
| COMH\_N to COML\_N | J15 pin 4 | J10 pin 1 |
| COMH\_P to COML\_P | J15 pin 3 | J10 pin 2 | COMH\_N to COML\_N J15 pin 4 J10 pin 1 COMH\_P to COML\_P J15 pin 3 J10 pin 2

## Table 4-2. Connections Between BQ79616EVM High Side and BQ79600EVM Low Side (for ring **architecture only)**

| Connection Name | BQ79600EVM Low Side | BQ79616EVM High Side |
|:--- |:--- |:--- |
| COML\_N to COMH\_N | J14 pin 1 | J11 pin 4 |
| COML\_P to COMH\_P | J14 pin 2 | J11 pin 3 | COML\_N to COMH\_N J14 pin 1 J11 pin 4 COML\_P to COMH\_P J14 pin 2 J11 pin 3

## 4.5 Connecting BQ79600EVM to BQ79606EVM

## The EVMs are connected using 4-position Molex connectors. The BQ79600EVM has a high side (J15) and

low side (J14) communication connector available on each board. To connect the BQ79600EVM to the BQ79606EVM using NORTH direction for communication, connect J15 on the BQ79600EVM to J5 on the BQ79606EVM. If several BQ79606EVMs are stacked, connect them as indicated in the EVM user's guide for the device. If using ring architecture, connect J6 of the top most BQ79606EVM to J14 on the BQ79600EVM.

*BQ79600EVM Quick Start Guide* <https://www.ti.com>

*BQ79600-Q1 Evaluation Module* SLUUC57B - OCTOBER 2019 - REVISED AUGUST 2023 *Submit Document Feedback*

**Table 4-3. Connections Between BQ79600EVM High Side and BQ79606EVM Low Side**

| Connection Name | BQ79600EVM High Side | BQ79606EVM Low Side |
|:--- |:--- |:--- |
| COMH\_N to COML\_N | J15 pin 4 | J5 pin 1 |
| COMH\_P to COML\_P | J15 pin 3 | J5 pin 2 | COMH\_N to COML\_N J15 pin 4 J5 pin 1 COMH\_P to COML\_P J15 pin 3 J5 pin 2

**Table 4-4. Connections Between BQ79606EVM High Side and BQ79600EVM Low Side (for ring ** **architecture only)**

| Connection Name | BQ79600EVM Low Side | BQ79606EVM High Side |
|:--- |:--- |:--- |
| COML\_N to COMH\_N | J14 pin 1 | J6 pin 4 |
| COML\_P to COMH\_P | J14 pin 2 | J6 pin 3 | COML\_N to COMH\_N J14 pin 1 J6 pin 4 COML\_P to COMH\_P J14 pin 2 J6 pin 3 **4.6 Software \*Not yet available\***

The example code only provides a control interface to the BQ79600-Q1 and BQ79616-Q1 and does not provide any other communications interface to the outside world. The customer is expected to develop their own communication implementation. Examples of communications interfaces available to the TMS570 are SPI, CAN, or UART. For the TMS570 example code, UART is the communication protocol used between the microcontroller and BQ79600-Q1 device.

Importing a project into Code Composer Studio ™:

1. Launch the provided file: *BQ79600-Q1 Example Code 0.1 Installer.exe* and extract files to the default path provided ( C:\\ti\\bq79600-Q1 Example Code 0.1 ). 2. Launch *Code Composer Studio* (CCS): **Start** → **Programs** → **Texas Instruments** → **Code Composer Studio v8** → **Code Composer Studio v8** 3. When Code Composer Studio v8 launches, CCS requests a workspace is selected, choose "C:\\myWorkspace". Once CCS loads, go to: **Project** → **Import** **CSS Projects...** → **Select search-directory** 4. In Select search-directory, browse to the folder: C:\\ti\\bq79600-Q1 Example Code 0.1 5. In *Discovered projects:*, check BQ79600-Q1 example code

# 4.7 GUI

For initial evaluation, using the graphical user's interface (GUI) can be beneficial. The GUI provides a *point and * *click* interface to become familiar with the BQ79600. During the initial sampling phase, contact your local TI FAE to get the latest GUI version.

To get started with the GUI, refer to the *BQAutoEval GUI User Guide* document. **4.7.1 GUI UART Connection**

The physical setup for the GUI is the same as for the microcontroller, but instead uses an USB2ANY interface and 10-pin cable for the UART/SPI connections on J4. The USB2ANY has a USB Mini-B connector on the right side. Plug the provided USB cable (or any USB cable with a Mini-B connector) into the USB2ANY. Plug the other end of the cable (USB 'A') into the computer. Then connect the 10-pin connector cable to J4 of the USB2ANY (middle most connector) and the key side must be facing upwards when connecting to the EVM header J4. Refer to the figure below and this is explained in more detail in the USB2ANY user guide and the BQAutoEval GUI user guide.

<https://www.ti.com> *BQ79600EVM Quick Start Guide*

SLUUC57B - OCTOBER 2019 - REVISED AUGUST 2023 *Submit Document Feedback* *BQ79600-Q1 Evaluation Module*

## 5 Physical Dimensions **5.1 Board Dimensions** Board dimensions: 2.300 in. \times 5.130 in. Board height:

- • Top - Tallest component (shunts) is 0.35 in. (8.8 mm) above PCB. - • Bottom - Tallest component (transformers) is 0.41 in. (10.5 mm) above PCB. **5.2 Board Mounting**

Figure 5-1 illustrates the EVM board dimensions. **Figure 5-1. Board Dimensions** *Physical Dimensions* <https://www.ti.com>

*BQ79600-Q1 Evaluation Module* SLUUC57B - OCTOBER 2019 - REVISED AUGUST 2023 *Submit Document Feedback*

# 6 Schematics, Assembly, Layout, and Bill of Materials (BOM)

# The BQ79600EVM schematics, assembly, layout, and BOM are provided in their respective sections.

# 6.1 Schematics

# BQ79600PWQ1

# DVDD

# MOSI/RX

# MISO/TX

# GND

# SCLK

# COMHN

# nUART/SPI (SPI\_RDY)

# FAULT

# CS

# CVDD

# COMHP

# COMLN COMLP

# BAT

# VIO

# INH

# U1

# GND

# BAT

# INH

# CVDD

# VIO

# MOSI\_RX MISO\_TX

# SCLK nCS

# nFAULT

# nUART\_SPIRDY

# COMHP COMHN

# COMLP COMLN DVDD

# VIO

# MOSI\_RX

# MISO\_TX

# nFAULT

# J10

# J11

# SCLK nUART\_SPIRDY nCS

# J13 J2 100k R4

# J1

# INH BAT

# GND

# GND

# COMHN

# COMLP COMLN

# COMHP

# J4A

# J4B

# GND

# MOSI\_RX

# MISO\_TX 470nF C2 470nF C3

# GND 0.1uF C4

# GND 10.0k R16 10.0k R14 10.0k R13 100k R12

# SCLK UART/SPI Connection

Power supply and reverse wakeup (BAT and INH connection)

# GND

**Pin Description** 5 TX - to microcontroller UART RX 4 RX - to microcontroller UART TX

2 FAULTn - to microcontroller GPIO 1 GND - shared GND with microcontroller

**Pin Description** 8 TX - to microcontroller UART RX 7 RX - to microcontroller UART TX 4 FAULTn - to microcontroller GPIO 5 GND - shared GND with microcontroller

# GND Green

# D2

# R11

# J8

# TP16

# GND

# TP17

# GND

# DVDD nFAULT

# TP1

# VIO

# TP2

# sCLK

# TP3

# RX

# TP4

# TX

# TP5 nCS

# TP6

# SPI\_RDY

# TP7

# CVDD

# TP10

# BAT

# TP12

# NFAULT

# TP11

# DVDD

# CVDD

# BAT

# nUART\_SPIRDY VIO SCLK MOSI\_RX MISO\_TX nCS

# GND

# R5

# Q1

# GND

# 10M R6

# GND

# J5

# DVDD

# GND

# nFAULT\_P

# VIO

# MOSI\_RX

# MISO\_TX 3 VIO- to microcontroller 3.3/5V

# GND

| 100k | R18 |
|:--- |:--- |
| 100k | R19 |
| 100k | R20 | 100k R19 100k R20

# VIO

# nFAULT\_P

# nUART\_SPIRDY nCS

9 nCS - CS pin 3 SCLK - clock pin 2 nUART\_SPIRDY - SPI\_RDY pin

# J3 CVDD

# BAT Test points (all except COMH/COML)

# TP13

# INH

# INH

# TP15

# GND

# R1

| 10.0k | R15 |
|:--- |:--- |
| 3.3V | 5V |
| MCU\_UART\_RX | MCU\_UART\_TX |

# 3.3V 5V

# MCU\_UART\_RX MCU\_UART\_TX

# SCLK nCS

1: MCU +3V3 to VIO selection jumper 5: MCU RX to BQ79600 MISO\_TX 7: MCU TX to BQ79600 MOSI\_RX

# 13: MCU SPI3CLK to BQ79600 SCLK

2: MCU 5V to VIO selection jumper 4: MCU GND to BQ79600 GND

# 17: MCU GIOA1 to BQ79600 nUART\_SPIRDY

19: MCU GIOA0 to BQ79600 nFAULT\_P nUART\_SPIRDY

| MCU\_SPI3SIMO | MCU\_SPI3SOMI |
|:--- |:--- |
| J6 | VIO selection from MCU |
| VIO | 3.3V | J6 VIO selection from MCU

# VIO 3.3V

# 5V FTDI / USB2ANY / MCU connection

# nFAULT\_P

# GND

## UART FTDI connection circuit

## USB2ANY UART/SPI connection

## TMS570LS04x/03x launchpad connection

## Pin Description **Pin Description**

## Pin Description

# nFAULT\_P J12 10.0k R17

# 12: MCU SPI3SIMO to BQ79600 MOSI\_RX

# 2: MCU GND to BQ79600 GND 4: 6: MCU SP31CS1 to BQ79600 nCS

# 14: MCU SPI3SOMI to BQ79600 MISO\_TX

## Pin Description

# R8

# R10

# R9

# R7 MOSI\_RX MCU\_UART\_TX

# MISO\_TX MCU\_UART\_RX

# MOSI\_RX

# MISO\_TX

# MCU\_SPI3SIMO

# MCU\_SPI3SOMI

# J7

# SSQ-110-03-T-D

# J9

# SSQ-110-03-T-D

# TP14

# INH\_OUT

# INH\_OUT

# 1.00M R3

# 5.1V

# D1

# SZMM3Z5V1ST1G 100k

# R2 INH\_OUT Red

# D3

# TP18

# GND

# TP9

# 5V

# TP8

# 12V

| 100nF | C1 |
|:--- |:--- |
| GND | GND |
| GND | GND |

# GND GND

# GND GND

# Figure 6-1. BQ79600EVM Schematic Part 1

# www.ti.com

*Schematics, Assembly, Layout, and Bill of Materials (BOM)*

# SLUUC57B - OCTOBER 2019 - REVISED AUGUST 2023 *Submit Document Feedback*

# BQ79600-Q1 Evaluation Module

# COMHN

# COMHP

# J15

# ISO\_COMHN ISO\_COMHP

# J14

# COMLP

# COMLN

# ISO\_COMLN ISO\_COMLP

# T3 ISO\_COMLP

# ISO\_COMLN

# T4

# ISO\_COMHP 100pF C13 100pF C14 2200pF

# C15 2200pF

# C17 470uH

# L2 2200pF

# C18 2200pF

# C16 470uH

# L1

# COMLP\_OPT

# COMLN\_OPT

# COMLN\_OPT

# COMLP\_OPT

# ISO\_COMLN

# ISO\_COMLP COMHP\_OPT

# COMHN\_OPT ISO\_COMHN

# ISO\_COMHP

# R56

# R46

# R55

# R45

# COMHP

# ISO\_COMHN

# COMLN

# COMLP

# J17

# J16

# R27

# R29

# R28

# R30

# J19

# J18

# COMHN COMHP COMLN COMLP 100pF C11 100pF C12 100pF C10 100pF C9

# D4

# D5

# T1

# HMU1228NL

# T2

# HMU1228NL COML/COMH Test points

# R23

# R33

# R24

# R34

Capacitor + choke isolation option (COML) Capacitor + choke isolation configuration (COMH)

Tranformer isolation options (COML) Tranformer isolation options (COMH)

# COMHN

# ISO\_COMLP

# ISO\_COMLN 100pF C7

# ISO\_COMHP

# ISO\_COMHN

# COMHP\_OPT

# COMHN\_OPT 100pF C8

# R37

# R41

# R38

# R42

# R21

# R31

# R22

# R35

# R39

# R40

# R43

# R44

# R25

# R26

# R36

# R32

# R47

# R51

# R48

# R52

# R49

# R53

# R50

# R54

# COMLP\_OPT

# COMLN\_OPT

# COMHP\_OPT

# COMHN\_OPT 10nF

# C5 10nF

# C6

# GND

# GND GND

# GND

# GND GND

# GND

# GND GND

# GND GND

# Figure 6-2. BQ79600EVM Schematic Part 2

# 6.2 Assembly

# Figure 6-3. BQ79600EVM Assembly Top

# Schematics, Assembly, Layout, and Bill of Materials (BOM) <https://www.ti.com>

# BQ79600-Q1 Evaluation Module SLUUC57B - OCTOBER 2019 - REVISED AUGUST 2023

# Submit Document Feedback

## Figure 6-4. BQ79600EVM Assembly Bottom

## 6.3 Layout

## Figure 6-5. BQ79600EVM Top Overlay

<https://www.ti.com> *Schematics, Assembly, Layout, and Bill of Materials (BOM)*

SLUUC57B - OCTOBER 2019 - REVISED AUGUST 2023 *Submit Document Feedback* *BQ79600-Q1 Evaluation Module*

## Figure 6-6. BQ79600EVM Bottom Overlay

## Figure 6-7. BQ79600EVM Top Solder

*Schematics, Assembly, Layout, and Bill of Materials (BOM)* <https://www.ti.com>

*BQ79600-Q1 Evaluation Module* SLUUC57B - OCTOBER 2019 - REVISED AUGUST 2023 *Submit Document Feedback*

## Figure 6-8. BQ79600EVM Top Layer

## Figure 6-9. BQ79600EVM Internal Signal Layer 1 - GND Plane

<https://www.ti.com> *Schematics, Assembly, Layout, and Bill of Materials (BOM)*

SLUUC57B - OCTOBER 2019 - REVISED AUGUST 2023 *Submit Document Feedback* *BQ79600-Q1 Evaluation Module*

## Figure 6-10. BQ79600EVM Internal Signal Layer 2 - GND Plane

## Figure 6-11. BQ79600EVM Bottom Layer

*Schematics, Assembly, Layout, and Bill of Materials (BOM)* <https://www.ti.com>

*BQ79600-Q1 Evaluation Module* SLUUC57B - OCTOBER 2019 - REVISED AUGUST 2023 *Submit Document Feedback*

## Figure 6-12. BQ79600EVM Bottom Solder

## Figure 6-13. BQ79600EVM Drill Drawing

<https://www.ti.com> *Schematics, Assembly, Layout, and Bill of Materials (BOM)*

SLUUC57B - OCTOBER 2019 - REVISED AUGUST 2023 *Submit Document Feedback* *BQ79600-Q1 Evaluation Module*

## 6.4 Bill of Materials (BOM)

## Table 6-1 lists the bill of materials for BQ79600EVM.

## Table 6-1. Bill of Materials

**Designator** **Qty** **Value** **Description** **Package ** **Reference** **Part Number** **Manufacturer**!PCB1 Printed Circuit Board BMS030 Any

# C1

0.1µF CAP, CERM, 0.1 µF, 50 V, \pm5%, X7R, 0603

# C0603C104J5RACT U Kemet

# C2, C3

0.47µF CAP, CERM, 0.47 µF, 16 V, \pm10%, X7R, AEC-Q200 Grade 1, 0603

# GCM188R71C474KA 55D MuRata

C4 0.1µF CAP, CERM, 0.1 µF, 10 V, \pm10%, X7R, AEC-Q200 Grade 1, 0402

# GCM155R71A104KA 55D MuRata

# C7, C8, C9, C10, C11, C12, C13, C14

# 100 pF

CAP, CERM, 100 pF, 50 V,\pm5%, C0G/NP0, AEC-Q200 Grade 1,

# GCM1885C1H101JA 16J MuRata

D2 Green LED, Green, SMD LED\_0805 LTST-C170KGKT Lite-On

# D3

Red LED, Red, SMD Red 0805 LED LTST-C170KRKT Lite-On

| D4, D5 | 28 V Clamp 13 A (8/20µs) Ipp Tvs | Diode Surface Mount TO-236AB |
|:--- |:--- |:--- |
| SOT23-3 | PESD5V0L2BT,215 | Nexperia |
| H1, H2, H3 | Machine Screw, Round, #4-40 x | 1/4, Nylon, Philips panhead |
| Screw | NY PMS 440 0025 | PH | SOT23-3 PESD5V0L2BT,215 Nexperia

H1, H2, H3 Machine Screw, Round, #4-40 x 1/4, Nylon, Philips panhead Screw NY PMS 440 0025 PH B&F Fastener Supply

H4, H5, H6 Standoff, Hex, 0.5"L #4-40 Nylon Standoff 1902C Keystone

# J1, J3, J6, J10, J11, J12

Header, 100mil, 3x1, TH Header, 3x1, 100mil, TH 800-10-003-10-0010 Mill-Max J2 Header, 0.5mm, 6x1, R/A, Gold, TH Header, 0.5mm, 6x1, R/A, TH 22-12-4062 Molex

| J4 | CONN HEADER 10POS.100 DL | R/A AU |
|:--- |:--- |:--- |
| HDR10 | TSW-105-08-L-D-RA | Samtec |
| J5, J8, J13 | Header, 2.54mm, 1x2, Tin, Black, | TH | HDR10 TSW-105-08-L-D-RA Samtec

J5, J8, J13 Header, 2.54mm, 1x2, Tin, Black, TH Header, 2.54mm, 2x1, TH

| PEC01DAAN | Sullins Connector | Solutions |
|:--- |:--- |:--- |
| J7, J9 | Receptacle, 2.54mm, 10x2, Tin, | TH |
| Receptacle, | 2.54mm, 10x2, | TH | J7, J9 Receptacle, 2.54mm, 10x2, Tin, TH Receptacle, 2.54mm, 10x2, TH SSQ-110-03-T-D Samtec

J14, J15 Header(shrouded), 2.54mm, 4x1, R/A, Gold, TH Header(shroude d), 2.54mm, 4x1, R/A, TH 70551-0038 Molex

J16, J17 Header, 100mil, 2x1, Tin, TH Header, 2 PIN, 100mil, Tin PEC02SAAN Sullins Connector Solutions

J18, J19 Header, 100mil, 3x1, Tin, TH Header, 3 PIN, 100mil, Tin PEC03SAAN Sullins Connector Solutions

LBL1 Thermal Transfer Printable Labels, 0.650" W x 0.200" H - 10,000 per roll PCB Label 0.650 x 0.200 inch THT-14-423-10 Brady

# Q1

20 V MOSFET, N-CH, 20 V, 0.2 A, AEC-Q101, SC-89

# SC-89 RE1C002UNTCL Rohm

# R1 RES, 10, 5%, 0.1 W, AEC-Q200 Grade 0, 0603

# CRCW060310R0JNE A Vishay-Dale

# R4, R12, R18, R19, R20

100k RES, 100 k, 1%, 0.1 W, AECQ200 Grade 0, 0603

# CRCW0603100KFKE A Vishay-Dale

# R5, R11 RES, 200, 5%, 0.1 W, AEC-Q200 Grade 0, 0603

# CRCW0603200RJNE A Vishay-Dale

R6 10Meg RES, 10 M, 5%, 0.1 W, AEC-Q200 Grade 0, 0603

# CRCW060310M0JN EA Vishay-Dale

# R7, R9, R37, R38, R39, R40, R41, R42, R43, R44

# RES, 0, 5%, 0.1 W, 0603 RC0603JR-070RL Yageo

*Schematics, Assembly, Layout, and Bill of Materials (BOM)* <https://www.ti.com>

*BQ79600-Q1 Evaluation Module* SLUUC57B - OCTOBER 2019 - REVISED AUGUST 2023 *Submit Document Feedback*

## Table 6-1. Bill of Materials (continued)

**Designator** **Qty** **Value** **Description** **Package ** **Reference** **Part Number** **Manufacturer**

# R13, R14, R15, R16, R17

10.0k RES, 10.0 k, 1%, 0.1 W, AECQ200 Grade 0, 0603

# CRCW060310K0FKE A Vishay-Dale

| R23, R24, R33, | R34 |
|:--- |:--- |
| RES, 51, 5%, 0.1 W, AEC-Q200 | Grade 0, 0603 |
| CRCW060351R0JNE | A | RES, 51, 5%, 0.1 W, AEC-Q200 Grade 0, 0603

# CRCW060351R0JNE A Vishay-Dale

# R27, R28, R29, R30

# RES, 499, 1%, 0.1 W, 0603 RC0603FR-07499RL Yageo

# SH1, SH2, SH3, SH4, SH5, SH6, SH7, SH8, SH9

Shunt, 100mil, Gold plated, Black Shunt 2 pos. 100 mil 881545-2 TE Connectivity

T3, T4 Transformer, 618 uH, SMT 9.7x9.5mm CEP99 Sumida

# TP1, TP2, TP3, TP4, TP5, TP6, TP7, TP10, TP11, TP12, TP13 Test Point, Multipurpose, White, TH White Multipurpose Testpoint Keystone

TP8, TP9 Test Point, Multipurpose, Red, TH Red Multipurpose Testpoint Keystone

# TP15, TP16, TP17

Terminal, Turret, TH, Triple Keystone1598-2 1598-2 Keystone TP18 Test Point, Multipurpose, Black, TH Black Multipurpose Testpoint Keystone

# U1 BQ79600PWQ1, PW0016A (TSSOP-16) PW0016A BQ79600PWQ1 Texas Instruments

# C5, C6

0.01µF CAP, CERM, 0.01 µF, 50 V, \pm10%, X7R, 0603 CL10B103KB8NCNC Samsung ElectroMechanics

# C15, C16, C17, C18

2200 pF CAP, CERM, 2200 pF, 2000 V, \pm10%, X7R, AEC-Q200 Grade 1, 1206J2K00222KXR Knowles Capacitors

D1 5.1V Diode, Zener, 5.1 V, 300 mW, AEC-Q101, SOD-323 SOD-323 SZMM3Z5V1ST1G ON Semiconductor

# FID1, FID2, FID3, FID4, FID5, FID6

Fiducial mark. There is nothing to buy or mount.

# N/A N/A N/A

L1, L2 470 µH Coupled inductor, 470 µH, 0.4 A, 0.35 ohm, SMD 5x3.3mm Wurth Elektronik

R2 100k RES, 100 k, 1%, 0.1 W, AECQ200 Grade 0, 0603

# CRCW0603100KFKE A Vishay-Dale

# R3

1.00Meg RES, 1.00 M, 1%, 0.1 W, 0603 RC0603FR-071ML Yageo

# R8, R10, R21,

R22, R25, R26, R31, R32, R35, R36, R47, R48, R49, R50, R51, R52, R53, R54

# RES, 0, 5%, 0.1 W, 0603 RC0603JR-070RL Yageo

| R45, R46, R55, | R56 |
|:--- |:--- |
| RES, 0, 5%, 0.333 W, AEC-Q200 | Grade 0, 0805 |
| CRCW08050000Z0E | AHP | RES, 0, 5%, 0.333 W, AEC-Q200 Grade 0, 0805

# CRCW08050000Z0E AHP Vishay-Dale

# T1, T2

BMS TRANSFORMER SMT\_TRANSFO RMER\_8MM89\_ 10MM09 HMU1228NL Pulse TP14 Test Point, Multipurpose, White, TH White Multipurpose Testpoint Keystone

<https://www.ti.com> *Schematics, Assembly, Layout, and Bill of Materials (BOM)*

SLUUC57B - OCTOBER 2019 - REVISED AUGUST 2023 *Submit Document Feedback* *BQ79600-Q1 Evaluation Module*

**7 Revision History** NOTE: Page numbers for previous revisions may differ from page numbers in the current version.

**Changes from Revision A (June 2020) to Revision B (August 2023)** **Page** - • Changed all instances of legacy terminology to controller and peripheral where SPI is mentioned.................. 1

**Changes from Revision \* (October 2019) to Revision A (June 2020)** **Page** - • Changed from *Advance Information* to *Production Data* release....................................................................... 1 *Revision History* <https://www.ti.com>

*BQ79600-Q1 Evaluation Module* SLUUC57B - OCTOBER 2019 - REVISED AUGUST 2023 *Submit Document Feedback*

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