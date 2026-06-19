# User's Guide

***BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation *** ***Modules***

# ABSTRACT

The BQ79616-Q1 and BQ75614-Q1 Evaluation Modules user's guide describes the general features, theory of operation, hardware setup, and use of the BQ79616EVM and BQ75614EVM. Throughout this user's guide, the abbreviations *BMS021*, *EVM*, and the term *evaluation module* are synonymous with the two different variants of BMS021, *BQ79616-Q1 Evaluation Module* and *BQ75614-Q1 Evaluation Module*, unless otherwise noted. When a difference is noted between the two variants, each variant is differentiated as *BQ79616EVM* for the *BQ79616-Q1 Evaluation Module*, and the *BQ75614EVM* for the *BQ75614-Q1 Evaluation Module*. These EVMs are evaluation boards for the *BQ79616-Q1* and BQ75614-Q1 devices for use in large format lithium-ion battery pack applications to provide monitoring, protecting, balancing, and communications.

**Table of Contents** **General Texas Instruments High Voltage Evaluation (TI HV EVM) User Safety Guidelines**............................................... 2 **1 General Description**................................................................................................................................................................ 4

1.1 Key Features...................................................................................................................................................................... 4 1.2 Key Electrical Parameters.................................................................................................................................................. 4 **2 Theory of Operation - Stackable BQ79616EVM**................................................................................................................... 5

2.1 Single Board....................................................................................................................................................................... 6 2.2 Stacked Systems............................................................................................................................................................... 6 2.3 Configuring the BQ79616-Q1 EVM to be used for Lower Cell Count Applications............................................................ 6 **3 Theory of Operation - Standalone BQ75614EVM**................................................................................................................. 7 **4 Connectors**.............................................................................................................................................................................. 9

4.1 Primary Input and Output Connectors................................................................................................................................ 9 **5 Quick Start Guide**.................................................................................................................................................................. 13

5.1 Required Devices for using the Example Code............................................................................................................... 13 5.2 Power Connections.......................................................................................................................................................... 13 5.3 Connecting the EVM to TMS570 LaunchPad.................................................................................................................. 14 5.4 Stacking BQ79616EVMs.................................................................................................................................................. 14 5.5 Software........................................................................................................................................................................... 14 5.6 GUI................................................................................................................................................................................... 15 **6 Physical Dimensions**............................................................................................................................................................ 16

6.1 Board Dimensions............................................................................................................................................................ 16 6.2 Board Mounting................................................................................................................................................................ 16 **7 BQ79616EVM Schematic, Assembly, Layout, and BOM**................................................................................................... 17

7.1 Schematic........................................................................................................................................................................ 17 7.2 Assembly.......................................................................................................................................................................... 21 7.3 Layout.............................................................................................................................................................................. 23 7.4 BQ79616EVM-021 Bill of Materials (BOM)...................................................................................................................... 32 **8 BQ75614EVM Schematic, Assembly, Layout, and BOM**................................................................................................... 37

8.1 Schematic........................................................................................................................................................................ 37 8.2 Assembly.......................................................................................................................................................................... 41 8.3 Layout.............................................................................................................................................................................. 42 8.4 BQ75614EVM Bill of Materials (BOM)............................................................................................................................. 43 **9 BQ79656EVM Schematic, Assembly, Layout, and BOM**................................................................................................... 48

9.1 Schematic........................................................................................................................................................................ 48 9.2 Assembly.......................................................................................................................................................................... 52 9.3 Layout.............................................................................................................................................................................. 53 9.4 BQ79656EVM Bill of Materials (BOM)............................................................................................................................. 54 <https://www.ti.com> *Table of Contents*

SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules*

**10 Revision History**................................................................................................................................................................. 59 **Trademarks** LaunchPad ™ and Code Composer Studio ™ are trademarks of Texas Instruments. All trademarks are the property of their respective owners. **General Texas Instruments High Voltage Evaluation (TI HV EVM) User Safety Guidelines**

#!

# WARNING

Warning: To minimize risk of fire hazard, always verify and follow any specific safety instructions and application considerations related to the batteries being used in conjunction with this EVM.

Always follow TI's set-up and application instructions, including use of all interface components within their recommended electrical rated voltage and power limits. Always use electrical safety precautions to help ensure your personal safety and the safety of those working around you. Contact TI's Product Information Center http:// support/ti./com for further information.

**Save all warnings and instructions for future reference.**

**Failure to follow warnings and instructions can result in personal injury, property damage, or death due ** **to electrical shock and/or burn hazards. **

The term TI HV EVM refers to an electronic device typically provided as an open framed, unenclosed printedcircuit-board assembly. This is intended strictly for use in development laboratory environments, solely for qualified professional users having training, expertise, and knowledge of electrical safety risks in development and application of high-voltage electrical circuits. Any other use or application are strictly prohibited by Texas Instruments. If you are not suitably qualified, then immediately stop from further use of the HV EVM.

1. **Work Area Safety:** a. Keep work area clean and orderly. b. Qualified observers must be present any time circuits are energized. c. Effective barriers and signage must be present in the area where the TI HV EVM and the interface electronics are energized, indicating operation of accessible high voltages can be present, for the purpose of protecting inadvertent access. d. All interface circuits, power supplies, evaluation modules, instruments, meters, scopes and other related apparatus used in a development environment exceeding 50 V RMS or 75 VDC must be electrically located within a protected Emergency Power Off (EPO) protected power strip. e. Use a stable and non-conductive work surface. f. Use adequately insulated clamps and wires to attach measurement probes and instruments. No freehand testing whenever possible.

2. **Electrical Safety:** As a precautionary measure, a good engineering practice is to assume that the entire EVM can have fully accessible and active high voltages. a. De-energize the TI HV EVM and all the inputs, outputs, and electrical loads before performing any electrical or other diagnostic measurements. Revalidate that TI HV EVM power has been safely deenergized. b. With the EVM confirmed de-energized, proceed with required electrical circuit configurations, wiring, measurement equipment hook-ups and other application needs, while still assuming the EVM circuit and measuring instruments are electrically live. c. Once EVM readiness is complete, energize the EVM as intended. *Trademarks* <https://www.ti.com>

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules* SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

**WARNING** **WARNING: while the EVM is energized, never touch the EVM or the electrical circuits as the ** **EVM or the electrical circuits can be at high voltages capable of causing electrical shock ** **hazard. ** 3. **Personal Safety:** a. Wear personal protective equipment, for example, latex gloves or safety glasses with side shields or protect EVM in an adequate lucent plastic box with interlocks from accidental touch.

4. **Limitation for Safe Use:** a. EVMs are not to be used as all or part of a production unit.

The following warnings and cautions are noted for the safety of anyone using or working close to the BQ79616 EVM. Observe all safety precautions.

#!

**Caution** Do not leave EVM powered when unattended.

#! **Danger High** **Voltage**

The BQ79616EVM is rated as a high voltage EVM, but is not required to operate this EVM at high voltage. If you apply high voltage to this board, then all terminals must be considered high voltage. spacer Electric shock is possible when connecting the board to live wire. The board must be handled with care by a professional. spacer For safety, use of isolated test equipment with overvoltage and overcurrent protection is highly recommended.

# CAUTION

The circuit module has signal traces, components, and component leads on the bottom of the board. This can result in exposed voltages, hot surfaces, or sharp edges. Do not reach under the board during operation.

# CAUTION

The circuit module can be damaged by overtemperature. To avoid damage, monitor the temperature during evaluation and provide cooling, as needed, for your system environment.

# CAUTION

Some power supplies can be damaged by application of external voltages. If using more than 1 power supply, check your equipment requirements and use blocking diodes or other isolation techniques, as needed, to prevent damage to your equipment.

# CAUTION

The communication interface is not isolated on the EVM. Be sure no ground potential exists between the computer and the EVM. Also be aware that the computer is referenced to the Battery-potential of the EVM.

<https://www.ti.com> *General Texas Instruments High Voltage Evaluation (TI HV EVM) User Safety Guidelines*

SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules*

## 1 General Description

TI's *BMS021 Battery Management System* (BMS) is an evaluation board for the *BQ7961X-Q1* family of devices for use in large format lithium-ion battery pack applications to provide monitoring, protecting, balancing, and communications. There are two variants of the evaluation board, the BQ79616EVM and the BQ75614EVM.

Each BQ79616EVM can manage up to 16 cells (80-V max) for Li-ion battery applications. Up to 35 BQ79616EVM modules can be stacked for packs up to 560 series cells.

Each BQ75614EVM can manage 14 or 16 cells (80-V max) for Li-ion battery applications. The standalone BQ75614EVM module includes integrated current sense.

Each system provides fast cell balancing, diagnostics, and module to controller communication. Independent protection circuitry is also provided. Please see the *BQ79616-Q1* or *BQ75614-Q1* data sheet for more details on each respective part.

Each EVM is equipped with precision measurement and synchronous communication to enable a controller to perform *State of Charge* (SOC) and *State of Health* (SOH) estimation. Highly-accurate cell voltages and a fast sampling time for the entire battery pack allows more efficient operation of battery modules and more accurate SOC and SOH calculations. Communication with stacked BQ79616EVMs is via an isolated daisy-chain differential bus. For the standalone BQ75614EVM, SOC and SOH are further assisted by an integrated current sense ADC.

Control a single EVM or multiple stacked EVMs using a PC-hosted GUI. Communication between the PC and the base device in a stack of BQ79616EVM (or a single standalone BQ75614EVM device) is via a USB2ANY UART interface. For a stack of BQ79616EVM devices, communication between all other EVMs in the stack occurs via the isolated, daisy-chain differential communication bus. The PC GUI allows configuration of the EVMs to monitor cells and other analog data channels, control balancing, and monitor details of any faults. **1.1 Key Features** This EVM includes the following features:

- • Internal passive cell balancing - • Isolated differential daisy chain communications with optional ring architecture - • Flexible architecture for 6 to 16 cell applications - • UART interface - • High-accuracy cell voltage measurement - • Diagnostics - • 8 multipurpose GPIOs - • Resistor ladder to simulate cell voltages - • Supports Bus Bar Connection/Measurement - • High-accuracy current sense measurement (only available on the BQ75614EVM). **1.2 Key Electrical Parameters**

The following table identifies the key electrical parameters: **Parameter** **Value**

Maximum battery pack voltage (stacked EVMs) 2400 V

Maximum operating voltage 80 V (depends on series R3, R4 value)

Minimum operating voltage 9 V (depends on series R3, R4 value, by default use at least 18V) Maximum cell open circuit voltage 5 V Ambient temperature -40 °C to 105 °C Nominal operating temperature -20 °C to 60 °C

Cell balancing current Approximately 200 mA @ 80 °C *General Description* <https://www.ti.com>

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules* SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

## 2 Theory of Operation - Stackable BQ79616EVM Figure 2-1 shows the system stack diagram.

**Figure 2-1. System Block Diagram - BQ79616**

The BMS system is designed to prolong the useful life of lithium-ion cells in battery packs through passive balancing. The battery pack is broken into a series of modules, each of which contains up to 16 cells. This system monitors voltages of individual battery cells and dissipates individual cell voltages through the use of internal cell balancing FETs. The BMS allows battery-powered electric machines to use smaller battery packs and fewer charging cycles to perform the same amount of work. The BMS also improves the overall lifetime of Li-ion battery packs by preventing undervoltage and overvoltage damage from occurring.

The typical BMS system with stacked modules has three main sub-systems, as shown in Figure 2-1: - • Host controller - in this case a TMS570 LaunchPad ™ - • A BQ79616-Q1 configured as an isolated communication bridge device - a BQ79600EVM or another  BQ79616EVM can support this - • BQ79616EVM based modules attached to cells - these can be stacked up to 35 total (including the bridge  device)

All commands and data are communicated with a host through either a UART or daisy-chain communication connection. The BQ79616 remains idle until a command is received from the host. The BQ79616 can support a host PC or microcontroller (via the UART connection header) or a daisy-chain interface from a BQ79616-Q1 implemented as a communication bridge.

The typical flow is for the host to go through the following simplified sequence: 1. Wakeup the BQ79616EVM board by sending a WAKEUP pulse when using the UART interface, or sending a WAKE tone when using the BQ79616EVM in a stack of other BQ79616EVM boards for a large battery pack or a BQ79616-Q1 configured as a bridge. Initialize the BQ79616-Q1 to be ready for use. 2. Send a sample command to the BQ79616-Q1 to read the cell measurement results. 3. The host uses the cell measurement data to calculate an average and determine the highest or lowest cells and determine the cells that are balanced. 4. If no stop command is sent, then the BQ79616-Q1 has a built-in timeout (set by the user), after which time the discharge is stopped automatically. 5. The host can then decide to repeat the process (back to step 2) or send commands to shutdown the BQ79616EVM and return later.

<https://www.ti.com> *Theory of Operation - Stackable BQ79616EVM*

SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules* **2.1 Single Board**

As a single board the BMS can passively balance up to 16 cells, up to 80 V of total voltage. Communication to the BQ79616EVM is handled by the daisy-chain communications bus from another BQ79616-Q1 or the UART host interface. **2.2 Stacked Systems**

The boards can be stacked in daisy chain to accommodate larger battery packs than the 16 channels provide on a single board. Communication to the BQ79616EVM is handled by the daisy-chain communications bus from another BQ79616-Q1.

**2.3 Configuring the BQ79616-Q1 EVM to be used for Lower Cell Count Applications**

The BQ79616-Q1 EVM can be configured to support lower cell count applications, especially for users designing with the BQ79614-Q1/BQ79612-Q1 devices. For these cases, the EVM comes fitted with placeholder 0 ohm resistors for shorting together the VC and CB pins of the topmost cells. These can be found in the schematic at the bottom of this user guide, with a note *Resistors for Lower Cell Count Applications*. The user needs to populate the 0 ohm resistors depending on the use of 12 or 14 cells. For 14, the user populates only R24, R28, R22, and R26, whereas for 12 the user populates all 8 of the resistors (R24, R28, R22, R26, R21, R23, R25, R27). The GUI is also implemented with a feature to change the active cell configuration. Navigate to the cell monitor page to *View Poll Settings* and then select their desired active cell configuration by using the dropdown selection below the *No. of cells* column.

*Theory of Operation - Stackable BQ79616EVM* <https://www.ti.com>

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules* SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

## 3 Theory of Operation - Standalone BQ75614EVM Figure 3-1 shows the system block diagram.

**Figure 3-1. System Block Diagram - BQ75614**

The BMS system is designed to prolong the useful life of lithium-ion cells in battery packs through passive balancing, and provide enhanced SOC and SOH measurements using integrated current sense measurement. The device can monitor a battery pack which contains up to 16 cells, or up to 14 cells with the ability to measure fuse and relay voltages. This system monitors voltages of individual battery cells and dissipates individual cell voltages through the use of internal cell balancing FETs. The BMS allows battery-powered electric machines to use smaller battery packs and fewer charging cycles to perform the same amount of work. The BMS also improves the overall lifetime of Li-ion battery packs by preventing undervoltage and overvoltage damage from occurring.

The typical BMS system with integrated current sense has two main sub-systems, as shown in Figure 3-1: - • Host controller - in this case a TMS570 LaunchPad ™ - • BQ75614EVM module attached to cells, and communicating with the host - • Optional: a digital isolator between the host domain and the BQ75614EVM domain

All commands and data are communicated with a host through UART. The BQ75614-Q1 remains idle until a command is received from the host. The BQ75614EVM can support a host PC or microcontroller (via the UART connection header).

<https://www.ti.com> *Theory of Operation - Standalone BQ75614EVM*

SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules*

The typical flow is for the host to go through the following simplified sequence:

1. Wakeup the BQ75614EVM board by sending a WAKEUP pulse when using the UART interface. 2. Send a sample command to the BQ75614-Q1 to read the cell measurement results and current measurement results. 3. The host uses the cell measurement data to calculate an average and determine the highest or lowest cells and determine the cells that are balanced. The host uses the current measurement data to estimate SOC and SOH. 4. If no stop command is sent, then the BQ75614-Q1 has a built-in timeout (set by the user), after which time the discharge is stopped automatically. 5. The host can then decide to repeat the process (back to step 2) or send commands to shutdown the BQ75614EVM and return later.

As a single standalone board, the BQ75614EVM can passively balance up to 16 cells, up to 80 V of total voltage. Communication to the BQ75614EVM is handled by the UART host interface.

*Theory of Operation - Standalone BQ75614EVM* <https://www.ti.com>

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules* SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

## 4 Connectors

## 4.1 Primary Input and Output Connectors

## 4.1.1 Jumper Placements

## Below is a table explaining each of the jumpers available for the user's flexibility.

| Pinheader | Contacts | Jumper Connection | Populated by Default? |
|:--- |:--- |:--- |:--- |
| J1 | 1-2 | Rx direct connection to CVDD | No |
| J2 | 1-2 | NFAULT connection to Digital Isolator | Yes |
| J4 | 1-2 | GPIO1 connection to 10k pullup and thermistor | Yes |
| J5 | 1-2 | TSREF pullup to GPIOs | Yes |
| J6 | 1-2 | LED connection on AVDD to indicate the device is | awake | J1 1-2 Rx direct connection to CVDD No

J2 1-2 NFAULT connection to Digital Isolator Yes

J4 1-2 GPIO1 connection to 10k pullup and thermistor Yes J5 1-2 TSREF pullup to GPIOs Yes

J6 1-2 LED connection on AVDD to indicate the device is awake Yes

| J14 | 1-2 | PWR/BAT connection to CELL16 | Yes |
|:--- |:--- |:--- |:--- |
| J16 | 1-2 | CELL0 connection to GND | Yes |
| J18 | 1-2 | CVDD connection to Digital Isolator | Yes |
| J21 | 1-2 | RX to Dig Isolator Connection | Yes | J16 1-2 CELL0 connection to GND Yes

J18 1-2 CVDD connection to Digital Isolator Yes J21 1-2 RX to Dig Isolator Connection Yes

## To set up the EVM as a base or stack device, the following jumper configurations need to be made

## • • If the EVM is being used as a base device, then populate J2, J18, and J21, but remove J1.

- • If the EVM is being used as a stack device, then populate J1, but remove J2, J18, and J21.

## 4.1.2 Battery Connector

## The live battery cell connections are made from connector J15. Cell voltage measurements and balancing

currents use these connections. Alternatively, the user can simulate cell voltages using the on board resistor ladder across each of the cells, which can be utilized by closing switches S1 and S2 and applying a DC voltage across the VSTACK test point and GND. Short unused channels to the top cell connection in the wiring harness to support fewer than 16 cells. At the minimum, the user must support 6 cells. Additional instructions for the connections for wiring J15 to live battery cells can be found in Figure 7-3.

## Figure 4-1. Molex 50-57-9422 (Reference Image Only)

## Table 4-1. Connector Information

**Designator** **Manufacturer** **Part Number** **Mating Connector**

J15 Molex Manufacturer:0705550056 Digi-Key: 0705550056-ND Manufacturer:50-57-9422 Digi-Key:WM2920-ND <https://www.ti.com> *Connectors*

SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules*

## Table 4-2. Pin Description **Pin** **Name** **Comments**

| CELL0/GND | Negative terminal of CELL1, Connected directly to AVSS GND of device |
|:--- |:--- |
| CELL16 | Positive terminal of CELL16, Direct connection to BAT, LDOIN |
| CELL0 | Negative terminal of CELL1, Connected directly to AVSS GND of device |
| CELL0S | Negative terminal of CELL1, Actual sense connnection for VC0 path |
| CELL1 | Positive terminal of CELL1, negative terminal of CELL2 |
| CELL2 | Positive terminal of CELL2, negative terminal of CELL3 |
| CELL3 | Positive terminal of CELL3, negative terminal of CELL4 |
| CELL4 | Positive terminal of CELL4, negative terminal of CELL5 |
| CELL5 | Positive terminal of CELL5, negative terminal of CELL6 |
| CELL6 | Positive terminal of CELL6, negative terminal of CELL7 |
| CELL7 | Positive terminal of CELL7, negative terminal of CELL8 |
| CELL8 | Positive terminal of CELL8, negative terminal of CELL9 |
| CELL9 | Positive terminal of CELL9, negative terminal of CELL10 |
| CELL10 | Positive terminal of CELL10, negative terminal of CELL11 |
| CELL11 | Positive terminal of CELL11, negative terminal of CELL12 |
| CELL12 | Positive terminal of CELL12, negative terminal of CELL13 |
| CELL13 | Positive terminal of CELL13, negative terminal of CELL14 |
| CELL14 | Positive terminal of CELL14, negative terminal of CELL15 |
| CELL15 | Positive terminal of CELL15, negative terminal of CELL16 |
| CELL16S | Positive terminal of CELL16, actual sense connection to VC16 path |
| CELL16 | Positive terminal of CELL16, Direct connection to BAT, LDOIN |
| CELL0/GND | Negative terminal of CELL1, Connected directly to AVSS GND of device |

CELL16 Positive terminal of CELL16, Direct connection to BAT, LDOIN

CELL0 Negative terminal of CELL1, Connected directly to AVSS GND of device

CELL0S Negative terminal of CELL1, Actual sense connnection for VC0 path

CELL1 Positive terminal of CELL1, negative terminal of CELL2

CELL2 Positive terminal of CELL2, negative terminal of CELL3

CELL3 Positive terminal of CELL3, negative terminal of CELL4

CELL4 Positive terminal of CELL4, negative terminal of CELL5

CELL5 Positive terminal of CELL5, negative terminal of CELL6

CELL6 Positive terminal of CELL6, negative terminal of CELL7

CELL7 Positive terminal of CELL7, negative terminal of CELL8

CELL8 Positive terminal of CELL8, negative terminal of CELL9

CELL9 Positive terminal of CELL9, negative terminal of CELL10

CELL10 Positive terminal of CELL10, negative terminal of CELL11

CELL11 Positive terminal of CELL11, negative terminal of CELL12

CELL12 Positive terminal of CELL12, negative terminal of CELL13

CELL13 Positive terminal of CELL13, negative terminal of CELL14

CELL14 Positive terminal of CELL14, negative terminal of CELL15

CELL15 Positive terminal of CELL15, negative terminal of CELL16

CELL16S Positive terminal of CELL16, actual sense connection to VC16 path

CELL16 Positive terminal of CELL16, Direct connection to BAT, LDOIN

CELL0/GND Negative terminal of CELL1, Connected directly to AVSS GND of device

## 4.1.3 Host Interface

## The 10-pin J17 - Serial connector is used to connect the EVM to a PC running the GUI or to a host controller.

Texas Instruments recommends using the USB2ANY that is available to order through TI.com, which includes the proper 10 pin cable.

## Figure 4-2. Samtec Inc. TSW-105-08-L-D-RA (Reference Image Only)

## Table 4-3. Connector Information

**Designator** **Manufacturer** **Part Number** **Mating Connector**

J17 Samtec Inc. Manufacturer: TSW-105-08-L-DRA 10 pin ribbon connector packaged with USB2ANY *Connectors* <https://www.ti.com>

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules* SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

## Table 4-4. Pin Description **Pin** **Name**

# NC

# NC nFAULT signal from BQ79616-Q1 or BQ75614-Q1

# NC

# GND

# USB2ANY 3.3V

# USB2ANY TX ( RX of BQ79616-Q1 or BQ75614-Q1 )

# USB2ANY RX ( TX of BQ79616-Q1 or BQ75614-Q1 )

# NC

# NC

## 4.1.4 GPIO or Thermistor Inputs

## There are 8 GPIO pins, which can either be floated, connected to a thermistor and 10k pullup, or forced to

certain voltage for a measurement. This can be determined by using the J4 header as shown below. Insert a shunt from pins 1 and 2 to connect GPIO1 to the thermistor, pins 3 and 4 to connect GPIO2 and so on for the other GPIOs. Jumper J5 must also be connected to pull the GPIOs up to the TSREF reference voltage for ratiometric NTC measurements.

## Figure 4-3. Sullins Connector Solutions PEC08DAAN (Reference Image Only)

## Table 4-5. Connector Information

**Designator** **Manufacturer** **Part Number** **Mating Connector**

J4 Sullins Connector Solutions Manufacturer: PEC08DAAN N/A <https://www.ti.com> *Connectors*

SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules*

## Table 4-6. Pin Description - J4 **Pin** **Name** **Comments**

| GPIO1 | GPIO1 Pin of BQ79616-Q1 or BQ75614-Q1 |
|:--- |:--- |
| GPIO1\_R | Connection for GPIO1 to 10k pullup and thermistor |
| GPIO2 | GPIO2 Pin of BQ79616-Q1 or BQ75614-Q1 |
| GPIO2\_R | Connection for GPIO2 to 10k pullup and thermistor |
| GPIO3 | GPIO3 Pin of BQ79616-Q1 or BQ75614-Q1 |
| GPIO3\_R | Connection for GPIO3 to 10k pullup and thermistor |
| GPIO4 | GPIO4 Pin of BQ79616-Q1 or BQ75614-Q1 |
| GPIO4\_R | Connection for GPIO4 to 10k pullup and thermistor |
| GPIO5 | GPIO5 Pin of BQ79616-Q1 or BQ75614-Q1 |
| GPIO5\_R | Connection for GPIO5 to 10k pullup and thermistor |
| GPIO6 | GPIO6 Pin of BQ79616-Q1 or BQ75614-Q1 |
| GPIO6\_R | Connection for GPIO6 to 10k pullup and thermistor |
| GPIO7 | GPIO7 Pin of BQ79616-Q1 or BQ75614-Q1 |
| GPIO7\_R | Connection for GPIO7 to 10k pullup and thermistor |
| GPIO8 | GPIO8 Pin of BQ79616-Q1 or BQ75614-Q1 |
| GPIO8\_R | Connection for GPIO8 to 10k pullup and thermistor |

GPIO1\_R Connection for GPIO1 to 10k pullup and thermistor

# GPIO2 GPIO2 Pin of BQ79616-Q1 or BQ75614-Q1

GPIO2\_R Connection for GPIO2 to 10k pullup and thermistor

# GPIO3 GPIO3 Pin of BQ79616-Q1 or BQ75614-Q1

GPIO3\_R Connection for GPIO3 to 10k pullup and thermistor

# GPIO4 GPIO4 Pin of BQ79616-Q1 or BQ75614-Q1

GPIO4\_R Connection for GPIO4 to 10k pullup and thermistor

# GPIO5 GPIO5 Pin of BQ79616-Q1 or BQ75614-Q1

GPIO5\_R Connection for GPIO5 to 10k pullup and thermistor

# GPIO6 GPIO6 Pin of BQ79616-Q1 or BQ75614-Q1

GPIO6\_R Connection for GPIO6 to 10k pullup and thermistor

# GPIO7 GPIO7 Pin of BQ79616-Q1 or BQ75614-Q1

GPIO7\_R Connection for GPIO7 to 10k pullup and thermistor

# GPIO8 GPIO8 Pin of BQ79616-Q1 or BQ75614-Q1

GPIO8\_R Connection for GPIO8 to 10k pullup and thermistor

## 4.1.5 High-Side and Low-Side Communications

## There are two sets of 4-position molex connectors available on each BQ79616EVM board. These are not

available on the BQ75614EVM. These provide high-side (J11) and low-side (J10) communications between stacked EVM devices.

## Table 4-7. Connector Information

**Designator** **Manufacturer** **Part Number** **Mating Connector**

| J10/J11 | Molex |
|:--- |:--- |
| Manufacturer: | Digi-Key: WM14059-ND |
| Manufacturer: | Digi-Key: WM2902-ND | Manufacturer: Digi-Key: WM14059-ND Manufacturer: Digi-Key: WM2902-ND

## Table 4-8. Pin Description - J10 **Pin** **Name** **Comments**

| COML\_N | COM lowside negative |
|:--- |:--- |
| COML\_P | COM lowside positive |
| N/A | Unused |
| N/A | Unused | COML\_P COM lowside positive N/A Unused N/A Unused

## Table 4-9. Pin Description - J11 **Pin** **Name** **Comments**

| N/A | Unused |
|:--- |:--- |
| N/A | Unused |
| COMH\_P | COM highside positive |
| COMH\_N | COM highside negative |
| Connectors | www.ti.com |
| BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules | SLUUC37D - JULY 2019 - REVISED JUNE 2025 | N/A Unused COMH\_P COM highside positive COMH\_N COM highside negative *Connectors* <https://www.ti.com>

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules* SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

## 5 Quick Start Guide

This section includes hardware setup instructions, connection procedures, and software and GUI instructions.

**Figure 5-1. Basic EVM Setup using DC Voltage with Resistor Ladder**

**5.1 Required Devices for using the Example Code**

The system example code is implemented using the TMS570LS12 LaunchPad ™ board (TMS570LS1224 MCU) and the BMS021 via Code Composer Studio.

The part numbers of the evaluation modules are LAUNCHXL2-TMS57012 and BQ79616EVM-021 (for BQ79616-Q1 evaluation) or BQ75614EVM-021 (for BQ75614-Q1 evaluation). These boards are available from the TI eStore ( <https://estore.ti.com/> ) or from your local TI sales representative. For more details and information related to the LaunchPad modules, see the specific module user's guide. **5.2 Power Connections**

If powering the EVM using the included resistor ladder as cells, simply ensure that the power supply positive terminal is connected to the "VSTACK" or "PWR" testpoints provided on the board, and the power supply negative terminal is connected to the "GND" or "Cell0" testpoints provided on the board, or any "GND" standoff provided.

If not using the resistor ladder, the power supply positive terminal must be connected to the "PWR" testpoint, and the power supply negative terminal must be connected to the "Cell0" testpoint.

Also ensure that headers J16 and J14 are both jumpered, to allow for power and ground to be supplied from the "battery stack" (resistor ladder). <https://www.ti.com> *Quick Start Guide*

SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules*

***5.2.1 On-Board Resistor Ladder - Power Supply***

Each EVM utilizes an on-board resistor ladder to simplify the evaluation process. Each of the sixteen resistors is nominally 100 Ω, resulting in roughly one-sixteenth of the module voltage at each cell connection. For the BQ75614EVM, this is one-fourteenth the module voltage as the board does not use the top two cells. By default, all actuators of S1, S2 are positioned closest to the IC, which is the "ON" or "closed" state. In this state, all of the resistors are connected to the EVM sense and balance connections and allow easy start up with a DC voltage connection across VSTACK and GND.

To simulate connected cells to the sense and balance connections (using a power supply), ALL switch actuators on S1, S2 must be moved away from the module connector J15 if not already done. Moving the actuators in this manner connects the EVM to the resistor ladder, and allows for simulated cell measurements. ***5.2.2 Using Actual Battery Cells***

When using actual battery cells, disconnect the resistor ladder by moving ALL switch actuators on S1, S2 to the "OFF" or open position (away from the IC and towards J15).

**5.3 Connecting the EVM to TMS570 LaunchPad**

The EVMs are connected using a standard wire jumper; Table 5-1 shows the connections between the two EVMs. By default, the TMS570 LaunchPad is powered by the USB port on the host computer.

**Table 5-1. \*Connections Between EVM and TMS570 LaunchPad**

| Connection Name | EVM | TMS570 LaunchPad |
|:--- |:--- |:--- |
| TX | J17 Pin | J2 pin 3 (UARX) |
| RX | J17 | J2 pin 4 (UATX) |
| nFAULT | J17 | J2 pin 5 (PA7) |
| GND | J17 | J3 pin 2 (GND) | TX J17 Pin J2 pin 3 (UARX)

# RX J17 J2 pin 4 (UATX) nFAULT J17 J2 pin 5 (PA7)

# GND J17 J3 pin 2 (GND) **5.4 Stacking BQ79616EVMs**

**Note** This section does not apply to BQ75614EVMs.

The BQ79616EVMs are connected using 4-position Molex connectors. There is a high side (J11) and low side (J10) communication connector available on each device. By default, the isolation filters for the vertical interface are set to cap only configuration. The user can change this by populating/depopulating components. For example, the user can depopulate resistors R69, R79, R72, and R74 to use the on board choke in series with the capacitors. There are also footprints to populate a transformer on the bottom of the PCB board. More details can be found in the schematic near the bottom of this user guide.

**Table 5-2. Connections Between High-Side/Low-Side BQ79616EVMs**

| Connection Name | BQ79616EVM High Side | BQ79616EVM Low Side |
|:--- |:--- |:--- |
| COMH\_N/COML\_N | J11 pin 4 | J10 pin 1 |
| COMH\_P/COML\_P | J11 pin 3 | J10 pin 2 | COMH\_N/COML\_N J11 pin 4 J10 pin 1 COMH\_P/COML\_P J11 pin 3 J10 pin 2 **5.5 Software**

The software provides a command API and drivers that are capable of implementing the examples provided in *BQ79616-Q1 Software Design Reference*.

The example code only provides a control interface to the BQ79616-Q1 and does not provide any other communications interface to the outside world. The customer is expected to develop their own communication implementation. Examples of communications interfaces available to the TMS570 are SPI, CAN, or UART. For the TMS570 example code, UART is the communication protocol used between the microcontroller and BQ79616-Q1 device.

This firmware provided with this application note provides source code examples of the command sequences described in the *BQ79616-Q1 Software Design Reference*. *Quick Start Guide* <https://www.ti.com>

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules* SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

Importing a project into Code Composer Studio ™: 1. Launch the provided file: *BQ79616-Q1 Example Code 0.1 Installer.exe* and extract files to the default path provided ( C:\\ti\\bq79616-Q1 Example Code 0.1 ). 2. Launch *Code Composer Studio* (CCS): **Start** → **Programs** → **Texas Instruments** → **Code Composer Studio v8** → **Code Composer Studio v8**. 3. When *Code Composer Studio* launches, CCS requests a workspace is selected, choose "C:\\myWorkspace". Once CCS loads, go to: **Project** → **Import** **CSS Projects...** → **Select search-directory**. 4. In Select search-directory, browse to the folder: C:\\ti\\bq79616-Q1 Example Code 0.1. 5. In *Discovered projects:*, check BQ79616-Q1 example code.

# 5.6 GUI

An initial evaluation can be more beneficial to use the graphical user's interface (GUI), which provides a *point * *and click* interface to become familiar with the BQ79616-Q1 or BQ75614-Q1. During the initial sampling phase, please contact your local TI FAE to get the latest GUI version.

To get started with the GUI, please refer to the *BQ79616 GUI User Guide* ( SLUUC36 ) document. ***5.6.1 GUI UART Connection***

The physical setup for the GUI is the same as for the microcontroller, but uses an USB2ANY interface and 10 pin cable for the UART connections on J17 instead. The USB2ANY has a USB Mini-B connector on the right side. Plug the provided USB cable (or any USB cable with a Mini-B connector) into the USB2ANY. Plug the other end of the cable (USB 'A') into the computer. Then connect the 10 pin connector cable to J4 of the USB2ANY (middle most connector). The key side must be facing upwards when connecting to the EVM header J17. Please refer to the picture below and this is explained in more detail in the USB2ANY user's guide ( SNAU228 ) and the BQ79616-Q1 GUI User's Guide ( SLUUC36 ). <https://www.ti.com> *Quick Start Guide*

SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules*

## 6 Physical Dimensions **6.1 Board Dimensions** Board dimensions: 4.400 in \times 5.500 in

Board height: - • Top - Tallest component (GPIO, Shunts) is 0.35 in (8.8 mm) above PCB. - • Bottom - Tallest component if populated (Transformers) is 0.41 in (10.5 mm) above PCB (Depopulated by  default). **6.2 Board Mounting**

Figure 6-1 illustrates the EVM dimension drawing. **Figure 6-1. Board Dimensions** *Physical Dimensions* <https://www.ti.com>

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules* SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

# 7 BQ79616EVM Schematic, Assembly, Layout, and BOM

# Provided are the BQ79616EVM schematic, assembly, layout and BOM in their respective sections.

# 7.1 Schematic

# PWR

# CB1

# CB14

# CB15

# CB16

# VC0

# VC1

# VC2

# VC3

# VC4

# VC5

# VC6

# VC7

# VC8

# VC9

# VC10

# VC11

# VC12

# VC13

# VC14

# VC15

# VC16

# CB2

# CB3

# CB4

# CB5

# CB6

# CB7

# CB8

# CB9

# CB10

# CB11

# CB12

# CB13

# COMLN

# COMLP COMHN

# COMHP

# CB0

| BBP\_CELL | BBN\_CELL |
|:--- |:--- |
| bq79616 | BMS021E3\_bq79616.SchDoc |
| Hardware | BMS021E3\_EVM\_Hardware.SchDoc | bq79616 BMS021E3\_bq79616.SchDoc Hardware BMS021E3\_EVM\_Hardware.SchDoc

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

# PWR

# CELL1

# CELL2

# CELL3

# CELL4

# CELL5

# CELL6

# CELL7

# CELL8

# CELL9

# CELL10

# CELL11

# CELL12

# CELL13

# CELL14

# CELL15

# CELL16S

# CB0 CELL0

# VSTACK Battery Connector BMS021E3\_VC\_CB.SchDoc

# COMLP COMHN

# COMLN

# COMHP

Daisy Chain Isolation BMS021E3\_Communications.SchDoc

# CELL1

# CELL2

# CELL3

# CELL4

# CELL5

# CELL6

# CELL7

# CELL8

# CELL9

# CELL10

# CELL11

# CELL12

# CELL13

# CELL14

# CELL15

# CELL16S

# CELL0

# BBP\_CELL BBN\_CELL

# VSTACK Cell Simulator BMS021E3\_CellSimulator.SchDoc

# Figure 7-1. BQ79616EVM Schematic Block Diagram

# www.ti.com

*BQ79616EVM Schematic, Assembly, Layout, and BOM*

# SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

# BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules

# ALL DECOUPLING CAPS ARE AS CLOSE TO THE CHIP AS POSSIBLE

GND tied to CELL0 at connector via a thick trace.

# GPIO6 GPIO7 GPIO8

# GPIO1 GPIO2 GPIO3 GPIO4 GPIO5

# CB0

CB1 CB2 CB3 CB4 CB5 CB6 CB7 CB8 CB9 CB10 CB11 CB12 CB13 CB14 CB15

# COMHP

# CB16

# COMHN

# COMLP COMLN

# NFAULT

# TX RX

# BBN BBP

# VC16

VC15 VC14 VC13 VC12 VC11 VC10 VC9 VC8 VC7 VC6 VC5 VC4 VC3 VC2 VC1 VC0

# DVDD CVDD AVDD

# REFHP

# BAT

# LDOIN

# NPNB

# NEG5V

# TSREF

# BQ79616PAPQ1

# GPIO5 GPIO4

# GPIO1

# GPIO6

# BBN BBP

# FAULT

# GPIO7

# GPIO2

# GPIO3

# VC14

# CB13

# VC12

# CB14

# VC11

# CB10

# CB11

# VC15

# CB12

# VC13

# VC9

# CB8

# VC7

# CB9

# VC6

# CB5

# CB6

# VC10

# CB7

# VC8

# REFHP

# AVDD

# COMLP

# REFHM

# COMHN

# COMHP

# COMLN

# VC0

# NEG5V

# AVSS

# LDOIN

# NPNB

# TSREF

# CVSS TX

# GPIO8

# RX

# CVDD

# DVSS

# DVDD

# VC4

# CB3

# VC2

# CB4

# VC1

# CB0

# CB1

# VC5

# CB2

# VC3

# BAT

# VC16

# CB15 CB16

# PAD

# U1 10nF C5

# GND

# GND 1µF C6 1µF

# C9 4.7µF

# C7 1µF C8 1µF C2

# GND

# GND

# GND

# GND 0.1uF

# C3 GND

# GND

# VC0

VC1 VC2 VC3 VC4 VC5 VC6 VC7 VC8 VC9 VC10 VC11 VC12 VC13 VC14 VC15 VC16

# CB0

CB1 CB2 CB3 CB4 CB5 CB6 CB7 CB8 CB9 CB10 CB11 CB12 CB13 CB14 CB15 CB16

| COMHP | COMHN |
|:--- |:--- |
| COMLP | COMLN |
| 30.0 | PWR |

# COMLP COMLN

# 30.0 PWR

# R5 Green

# PWR

# D1

# J6

# GND 1.0k

# R121

# GND

# LDOIN

# R3

# R4 0.22µF

# C1

# GND

# PWR NPN Power Supply

# TP14

# GND

# GND

# TP13

# GND

# DVDD BBN NFAULT Test Points

# TP1

# TSREF

# TP2

# LDOIN

# TP3

# NEG5V

# TP4

# NPNB

# TP5

# CVDD

# TP6

# AVDD

# TP7

# REFHP

# TP8

# BAT

# TP43

# NFAULT

# TP11

# BBN

# TP10

# BBP

# TP9

# DVDD

# BBN

# BBP

# R9

# R12 0.47uF

# C10

# R24

# DNP

# BBN\_CELL

# BBP\_CELL

# BBP\_CELL

# BBN\_CELL

# R23

# DNP

# R28

# DNP R27

# DNP

# VC16

# VC15

# VC14

# VC13

# VC12

# R22

# DNP

# R26

# DNP

# CB16

# CB15

# R21

# DNP

# R25

# DNP

# CB14

# CB13

# CB12

Resistors for Lower Cell Count Applications (614, 612) BBP/BBN Bus Bar

# TP16

# TP17

# R13

# DNP

# R10

# DNP

# BBN

# BBP

# 0.47uF DNP C11 TP19 SRN\_S

# TP18 SRP\_S SRP/SRN Current Sense

# GPIO8\_R

# GPIO5\_R GPIO6\_R GPIO7\_R

# GPIO4\_R GPIO3\_R GPIO2\_R GPIO1\_C

# J4

# GPIO8

| GPIO6 | GPIO7 |
|:--- |:--- |
| GPIO5 | GPIO4 |
| GPIO2 | GPIO1 |

# GPIO5 GPIO4

# GPIO2 GPIO1

# GPIO3

# J5

# TSREF

Jumpers to connect GPIOs to resistor divider and thermistor for temperature measurements.

Jumpers to connect TSREF to ratiometric circuit. Low side NTC circuit. 10k

## t°

# RT7 10k

## t

## ° RT5 10k

## t

## °

# RT4 10k

## t

## °

# RT2 10k

## t

## °

# RT6 10k

## t

## °

# RT1

## 10k t °

# RT8 10k

## t°

# RT3 10.0k

# R11 10.0k

# R19 10.0k

# R8 10.0k

# R18 10.0k

# R7 10.0k

# R16 10.0k

# R15 10.0k

# R14

# GND

# PULLUP

# PULLUP

# GPIO1\_R

# GPIO2\_R

# GPIO3\_R

# GPIO4\_R

# GPIO5\_R

# GPIO6\_R

# GPIO7\_R

# GPIO8\_R

# GPIOs

# C12 DNP 1uF 100k

# R20

# DNP

# DNP 1

# Q2 2,4

# NPNB

# R17 DN 0 P

# Q1

# NPNB

# BAT REFHP

# BBP

# AVDD

# TSREF LDOIN NEG5V NPNB

# CVDD

# GND

# TP15

# GND

# GND

# J3 UART Communication

J3 Pin Desc ription 5 TX - to microcontroller UART RX 4 RX - to microcontroller UART TX 2 FAULTn - to microcontroller GPIO 1 GND - shared GND with microcontroller

# J1

# TX

# J2 100k R2

# CVDD

# NFAULT 100k R120

# J17A

# R119

# RX\_C

# J17B 0.1uF

# C59 0.1uF

# C4

# GND

# RX

# INA

J17 Pin Des cription 8 TX - to microcontroller UART RX 7 RX - to microcontroller UART TX 3 FAULTn - to microcontroller GPIO 5 GND - shared GND with microcontroller 6  USB2ANY 3.3V

# INB

# INC

# IND

# OUTA

# OUTB

# OUTC

# OUTD

# EN1 EN2

# VCC1 VCC2

# GND1 GND2 GND1 GND2

# U2

# ISO7342CQDWRQ1

# GND\_ISO 0.1uF

# C57 0.1uF

# C58

# USB2ANY\_TX\_3.3 100k R123

# GND\_ISO 1.0k

# R128 GPIO1\_R

# TP42

# TX

# TP12

# RX

# CVDD

# NFAULT\_C

# CVDD\_CO

# NFAULT\_C

# USB2ANY\_3.3V

# USB2ANY\_TX\_3.3

# USB2ANY\_RX\_3.3

# USB2ANY\_3.3V

# CVDD\_CO

# TX

# RX\_CO

# NF\_J

# GND GND\_ISO

# RX

# TX

# USB2ANY\_RX\_3.3

# USB2ANY\_3.3V

# J18

# GND

# GND

# J21

# RX 1uF C60

# GND

# TP44

# GPIO1\_R

# 24V

# D3

# NF\_J

# Figure 7-2. BQ79616EVM Schematic Part 1

# BQ79616EVM Schematic, Assembly, Layout, and BOM <https://www.ti.com>

# BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules SLUUC37D - JULY 2019 - REVISED JUNE 2025

# Submit Document Feedback

## Figure 7-3. BQ79616EVM Schematic Part 2

<https://www.ti.com> *BQ79616EVM Schematic, Assembly, Layout, and BOM*

SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules*

# CELL5 CELL4 CELL3 CELL2 CELL1

# R48

# R47

# R46

# R45

# R44

# R43

# CELL6

# CELL0

# C4\_L C3\_L C2\_L C1\_L

# C6\_R C5\_R C4\_R C3\_R C2\_R C1\_R

# R49 CELL0

# GND

# S2

# C5\_L C6\_L

# R42

# R37

# C7\_L C8\_L

# CELL7 CELL8 C7\_R C8\_R

# R35

# R34

# R33

# R36

# R30

# R29

# R32

# R31

# S1

# C16\_R C15\_R C14\_R C13\_R C12\_R C11\_R

# C14\_L C13\_L C12\_L C11\_L

# C15\_L C16\_L

# C10\_L C9\_L C10\_R C9\_R CELL9 CELL10

# CELL15 CELL14 CELL13 CELL12 CELL11

# CELL16S

# J8

# J7

# C5\_R C4\_R C3\_R C2\_R C1\_R C7\_R C8\_R

# C11\_R C10\_R C9\_R

# J9

# C16\_R C15\_R C14\_R C13\_R C6\_R C12\_R

# CELL8 CELL7 CELL6 CELL5 CELL4 CELL3 CELL2 CELL1

# CELL14 CELL13 CELL12 CELL11 CELL10 CELL9

# CELL15 CELL16S

# CELL0

# TP38

# GND

# TP39

# CELL0

# R40

# BBN\_CELL

## 0.1

# BBP\_CELL

# R39

# R38

# DNP

# R41

# DNP

# TP40

# VSTACK

# VSTACK

# Figure 7-4. BQ79616EVM Schematic Part 3

# 24V

# D5

# COMHN

# COMHP

# J11

# ISO\_COMMH\_N ISO\_COMMH\_P

# J10

# COMML\_P

# GND

# COMML\_N

# GND

# ISO\_COMML\_N ISO\_COMML\_P

# 24V

# D2

# GND

# ISO\_COMML\_P

# GND

# ISO\_COMML\_N 100pF

# ISO\_COMMH\_P

# C13 220pF C15 220pF C16 220pF C17 220pF C18 100pF C14 2200pF

# C20 2200pF

# C21 470uH

# L2 2200pF

# C22 2200pF

# C19 470uH

# L1

# COMML\_P\_OPT

# COMML\_P\_OPT

# COMML\_N\_OPT

# COMML\_N\_OPT

# ISO\_COMML\_P

# ISO\_COMML\_N COMMH\_N\_OPT

# COMMH\_P\_OPT ISO\_COMMH\_P

# ISO\_COMMH\_N

# R53

# R57

# R52

# R56

# R70

# R76

# R71

# R77

# R79

# R69

# R73

# R75

# R78

# R74

# R72

# R68

# R54

# R50

# R51

# R55

# TP41

# GND

# R60

# R66

# R59

# R65

# R58

# R64

# R61

# R67

# COMML\_N\_OPT

# COMML\_P\_OPT

# COMMH\_P\_OPT

# COMMH\_P\_OPT

# COMMH\_N\_OPT

# COMMH\_N\_OPT

# COMMH\_P

# COMMH\_N

# ISO\_COMMH\_N

# COMLN

# GND

# COMLP

# GND

# J13

# J12

| R115 | P499 | DN |
|:--- |:--- |:--- |
| R117 | P499 | DN |
| R116 | P499 | DN |

# R117 P 499 DN

# R116 P 499 DN

# R118 P 499 DN 10nF

# C62

# DNP 10nF

# C61

# DNP 1.00k R62

# GND 1.00k R63

# J19

# J20

# GND COMMH\_N COMMH\_P

# GND COMML\_N COMML\_P

# T1

# DNP

# HMU1228NL

# T2

# DNP

# HMU1228NL

# Figure 7-5. BQ79616EVM Schematic Part 4

# BQ79616EVM Schematic, Assembly, Layout, and BOM <https://www.ti.com>

# BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules SLUUC37D - JULY 2019 - REVISED JUNE 2025

# Submit Document Feedback

## 7.2 Assembly

## Figure 7-6. BQ79616EVM Assembly Top

<https://www.ti.com> *BQ79616EVM Schematic, Assembly, Layout, and BOM*

SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules*

## Figure 7-7. BQ79616EVM Assembly Bottom

*BQ79616EVM Schematic, Assembly, Layout, and BOM* <https://www.ti.com>

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules* SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

## 7.3 Layout

## Figure 7-8. BQ79616EVM Top Overlay

<https://www.ti.com> *BQ79616EVM Schematic, Assembly, Layout, and BOM*

SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules*

## Figure 7-9. BQ79616EVM Bottom Overlay

*BQ79616EVM Schematic, Assembly, Layout, and BOM* <https://www.ti.com>

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules* SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

## Figure 7-10. BQ79616EVM Top Solder

<https://www.ti.com> *BQ79616EVM Schematic, Assembly, Layout, and BOM*

SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules*

## Figure 7-11. BQ79616EVM Top Layer

*BQ79616EVM Schematic, Assembly, Layout, and BOM* <https://www.ti.com>

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules* SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

## Figure 7-12. BQ79616EVM Internal Signal Layer 1 - GND Plane

<https://www.ti.com> *BQ79616EVM Schematic, Assembly, Layout, and BOM*

SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules*

## Figure 7-13. BQ79616EVM Internal Signal Layer 2

*BQ79616EVM Schematic, Assembly, Layout, and BOM* <https://www.ti.com>

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules* SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

## Figure 7-14. BQ79616EVM Bottom Layer

<https://www.ti.com> *BQ79616EVM Schematic, Assembly, Layout, and BOM*

SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules*

## Figure 7-15. BQ79616EVM Bottom Solder

*BQ79616EVM Schematic, Assembly, Layout, and BOM* <https://www.ti.com>

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules* SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

## Figure 7-16. BQ79616EVM Drill Drawing

<https://www.ti.com> *BQ79616EVM Schematic, Assembly, Layout, and BOM*

SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules*

## 7.4 BQ79616EVM-021 Bill of Materials (BOM)

## Table 7-1. BQ79616EVM-021 BOM

**Designator** **Qty** **Value** **Description** **Package ** **Reference** **Part Number** **Manufacturer** **Alternate** **Alternate ** **Manufacturer**!PCB1 Printed Circuit Board BMS021 Any

C1 Multilayer Ceramic Capacitors MLCC - SMD/SMT 1206 0.22uF 100volts  X7R +/-10%

# GCM31MR72A224K A37L Murata

# C2, C6, C8, C9

CAP CER 0603 1UF 10 V X7R 10% 0603 (1608 Metric) C0603C105K8RACA UTO

# KEMET

# C3, C4, C57, C58, C59

# 0.1uF

CAP, CERM, 0.1 uF, 10 V, +/- 10%, X7R, AEC-Q200 Grade 1, 0402

# GCM155R71A104KA 55D MuRata

# C5

0.01uF CAP, CERM, 0.01 µF, 100 V,+/- 10%, X7R, AEC-Q200 Grade 1, 0603

# GCM188R72A103KA 37J MuRata

# C7

4.7uF CAP, CERM, 4.7 uF, 10 V, +/- 20%, X7R, 0805

# C2012X7R1A475M1 25AC

# TDK

# C10, C23, C24,

C25, C26, C27, C28, C29, C30, C31, C32, C33, C34, C35, C36, C37, C38, C39, C40, C41, C42, C43, C44, C45, C46, C47, C48, C49, C50, C51, C52, C53, C54, C55, C56

# 0.47uF

CAP, CERM, 0.47 uF, 16 V, +/- 10%, X7R, AEC-Q200 Grade 1, 0603

# GCM188R71C474KA 55D MuRata

# C13, C14

100 pF CAP, CERM, 100 pF, 50 V,+/- 5%, C0G/NP0, AEC-Q200 Grade 1, 0603

# GCM1885C1H101JA 16J MuRata

# C15, C16, C17, C18

# 220 pF CAP, CERM, 220 pF, 50 V,+/- 5%, X7R, 0603 CL10B221JB8NNNC Samsung ElectroMechanics

# C19, C20, C21, C22

# 2200 pF

CAP, CERM, 2200 pF, 2000 V,+/- 10%, X7R, AEC-Q200 Grade 1, 1206 1206J2K00222KXR Knowles Capacitors

# C60

1uF CAP, CERM, 1 uF, 16 V, +/- 10%, X7R, AEC-Q200 Grade 1, 0603

# GCM188R71C105KA 64D MuRata

D1 Green LED, Green, SMD LED\_0805 LTST-C170KGKT Lite-On

# D2, D3, D5

24 V Diode, TVS, Bi, 24 V, 70 Vc, AECQ101, SOT-23 SOT-23 PESD1CAN,215 NXP Semiconductor ESD562-Q1 Texas Instruments

# FID1, FID2, FID3, FID4, FID5, FID6

Fiducial mark. There is nothing to buy or mount.

# N/A N/A N/A

*BQ79616EVM Schematic, Assembly, Layout, and BOM* <https://www.ti.com>

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules* SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

## Table 7-1. BQ79616EVM-021 BOM (continued)

**Designator** **Qty** **Value** **Description** **Package ** **Reference** **Part Number** **Manufacturer** **Alternate** **Alternate ** **Manufacturer**

H1, H2, H3, H4 Machine Screw, Round, #4-40 x 1/4, Nylon, Philips panhead Screw NY PMS 440 0025 PH B&F Fastener Supply

H5, H6, H7, H8 Standoff, Hex, 0.5"L #4-40 Nylon Standoff 1902C Keystone

# H9 CONN HOUSING 22POS.100 W / LATCH 50-57-9422 Molex

H11, H12 Rectangular Housing Connector, 4 Pos, 2.54mm 50-57-9404 Molex

# J1, J2, J5, J6, J18, J21

Header, 2.54mm, 1x2, Tin, Black, TH Header, 2.54mm, 2x1, TH PEC01DAAN Sullins Connector Solutions

J3 Header, 0.5mm, 6x1, R/A, Gold, TH Header, 0.5mm, 6x1, R/A, TH 22-12-4062 Molex J4 Header, 2.54 mm, 8x2, Tin, Vertical, TH Header, 2.54 mm, 8x2, TH PEC08DAAN Sullins Connector Solutions

J7, J8, J9 Header, 100mil, 6x1, Tin, TH TH, 6-Leads, Body 608x100mil, Pitch 100mil

| PEC06SAAN | Sullins Connector | Solutions |
|:--- |:--- |:--- |
| J10, J11 | Header(shrouded), 2.54mm, 4x1, | R/A, Gold, TH |
| Header(shrouded), | 2.54mm, 4x1, R/A, | TH |

J10, J11 Header(shrouded), 2.54mm, 4x1, R/A, Gold, TH Header(shrouded), 2.54mm, 4x1, R/A, TH 70551-0038 Molex

# J12, J13, J14, J16

Header, 100mil, 2x1, Tin, TH Header, 2 PIN, 100mil, Tin PEC02SAAN Sullins Connector Solutions

J15 Connector Header Through Hole, Right Angle 22 position 0.100" (2.54mm) HDR22 Molex

# J17 CONN HEADER 10POS.100 DL R/A AU HDR10 TSW-105-08-L-D-RA Samtec

J19, J20 Header, 100mil, 3x1, Tin, TH Header, 3 PIN, 100mil, Tin PEC03SAAN Sullins Connector Solutions

L1, L2 470uH Coupled inductor, 470 uH, 0.4 A, 0.35 ohm, SMD 5x3.3mm Wurth Elektronik

LBL1 Thermal Transfer Printable Labels, 0.650" W x 0.200" H - 10,000 per roll PCB Label 0.650 x 0.200 inch THT-14-423-10 Brady

Q1 150 V Transistor, NPN, 150 V, 1 A, AECQ101, DPAK DPAK ZXTN4004KTC Diodes Inc.

R2, R120, R123 100k RES, 100 k, 5%, 0.1 W, AEC-Q200 Grade 0, 0603

# CRCW0603100KJNE A Vishay-Dale

# R3 RES, 100, 1%, 0.75 W, AEC-Q200 Grade 0, 2010

# CRCW2010100RFK EF Vishay-Dale

# R4 RES, 200, 1%, 0.75 W, AEC-Q200 Grade 0, 2010

# CRCW2010200RFK EF Vishay-Dale

<https://www.ti.com> *BQ79616EVM Schematic, Assembly, Layout, and BOM*

SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules*

## Table 7-1. BQ79616EVM-021 BOM (continued)

**Designator** **Qty** **Value** **Description** **Package ** **Reference** **Part Number** **Manufacturer** **Alternate** **Alternate ** **Manufacturer**

# R5

30.0 RES, 30.0, 1%, 0.1 W, AEC-Q200 Grade 0, 0603 ERJ-3EKF30R0V Panasonic

# R7, R8, R11, R14, R15, R16, R18, R19

10.0k RES, 10.0 k, 1%, 0.1 W, AEC-Q200 Grade 0, 0603

# CRCW060310K0FKE A Vishay-Dale

# R9, R12 RES, 402, 1%, 0.1 W, AEC-Q200 Grade 0, 0603

# CRCW0603402RFK EA Vishay-Dale

# R29, R30, R31,

R32, R33, R34, R35, R36, R37, R42, R43, R44, R45, R46, R47, R48 RES, 100, 1%, 1 W, AEC-Q200 Grade 0, 2512

# CRCW2512100RFK EG Vishay-Dale

# R39

0.1 RES, 0.1, 5%, 0.1 W, 0603 CRL0603-JWR100ELF Bourns

# R40, R49 RES, 0, 5%, 0.25 W, AEC-Q200 Grade 0, 1206 ERJ-8GEY0R00V Panasonic

# R50, R51, R52,

R53, R54, R55, R56, R57, R68, R69, R70, R71, R72, R73, R74, R75, R76, R77, R78, R79 RES, 0, 5%, 0.333 W, AEC-Q200 Grade 0, 0805

# CRCW08050000Z0E AHP Vishay-Dale

# R58, R61, R64, R67

# RES, 0, 5%, 0.1 W, 0603 RC0603JR-070RL Yageo

| R59, R60, R65, | R66 |
|:--- |:--- |
| RES, 51, 5%, 0.1 W, AEC-Q200 | Grade 0, 0603 |
| CRCW060351R0JNE | A | RES, 51, 5%, 0.1 W, AEC-Q200 Grade 0, 0603

# CRCW060351R0JNE A Vishay-Dale

R62, R63 1.00k RES, 1.00 k, 1%, 0.1 W, 0603 ERJ-3EKF1001V Panasonic

# R80, R81, R84,

R85, R89, R90, R93, R94, R97, R98, R101, R102, R105, R106, R109, R110, R113 RES, 100, 0.1%, 0.1 W, AEC-Q200 Grade 0, 0603 ERA-3AEB101V Panasonic

# R82, R83, R86,

R87, R91, R92, R95, R96, R99, R100, R103, R104, R107, R108, R111, R112, R114

10.0 RES, 10.0, 1%, 0.75 W, AEC-Q200 Grade 0, 1210

# CRCW121010R0FK EAHP Vishay-Dale

*BQ79616EVM Schematic, Assembly, Layout, and BOM* <https://www.ti.com>

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules* SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

## Table 7-1. BQ79616EVM-021 BOM (continued)

**Designator** **Qty** **Value** **Description** **Package ** **Reference** **Part Number** **Manufacturer** **Alternate** **Alternate ** **Manufacturer**

# R88 RES, 0, 5%, 0.1 W, AEC-Q200 Grade 0, 0603

# CRCW06030000Z0E A Vishay-Dale

# R119 RES, 100, 5%, 0.25 W, AEC-Q200 Grade 0, 0603

# ESR03EZPJ101 Rohm

R121, R128 1.0k RES, 1.0 k, 5%, 0.1 W, AEC-Q200 Grade 0, 0603

# CRCW06031K00JNE A Vishay-Dale

# RT1, RT2, RT3, RT4, RT5, RT6, RT7, RT8

10k Thermistor NTC, 10k ohm, 2%, 0603 ERT-J1VG103GA Panasonic

S1, S2 Switch, SPST 8Pos, Rocker, TH 9.65X8X22.4mm 76SB08ST Grayhill

# SH1, SH2, SH3, SH4, SH5, SH6, SH7, SH8

Shunt, 100mil, Gold plated, Black Shunt 2 pos. 100 mil 881545-2 TE Connectivity

# TP1, TP2, TP3,

TP4, TP5, TP6, TP7, TP8, TP9, TP10, TP11, TP12, TP16, TP17, TP18, TP19, TP21, TP22, TP23, TP24, TP25, TP26, TP27, TP28, TP29, TP30, TP31, TP32, TP33, TP34, TP35, TP36, TP42, TP43, TP44

Test Point, Multipurpose, White, TH White Multipurpose Testpoint Keystone

# TP13, TP14, TP15

Terminal, Turret, TH, Triple Keystone1598-2 1598-2 Keystone

# TP20, TP38, TP39

Test Point, Multipurpose, Black, TH Black Multipurpose Testpoint Keystone

TP37, TP40 Test Point, Multipurpose, Red, TH Red Multipurpose Testpoint Keystone

U1 SafeTI™ Precision Monitor With Integrated Hardware Protector for Lithium-Ion, Lithium Phosphate, Lithium Titanate Battery Pack, PAP0064F (HTQFP-64)

PAP0064F BQ79616PAPQ1 Texas Instruments Texas Instruments

U2 Automotive, Low Power, QuadChannel 2/2 Digital Isolator, DW0016B (SOIC-16)

DW0016B ISO7342CQDWRQ1 Texas Instruments ISO7342CQDWQ1 Texas Instruments

<https://www.ti.com> *BQ79616EVM Schematic, Assembly, Layout, and BOM*

SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules*

## Table 7-1. BQ79616EVM-021 BOM (continued)

**Designator** **Qty** **Value** **Description** **Package ** **Reference** **Part Number** **Manufacturer** **Alternate** **Alternate ** **Manufacturer**

# C11

0.47uF CAP, CERM, 0.47 uF, 16 V, +/- 10%, X7R, AEC-Q200 Grade 1, 0603

# GCM188R71C474KA 55D MuRata

# C12

1uF CAP, CERM, 1 uF, 16 V, +/- 10%, X7R, AEC-Q200 Grade 1, 0603

# GCM188R71C105KA 64D MuRata

# C61, C62

0.01uF CAP, CERM, 0.01 uF, 50 V, +/- 10%, X7R, 0603 CL10B103KB8NCNC Samsung ElectroMechanics

D4 75 V Diode, TVS, Uni, 75 V, 121 Vc, 400 W, 3.3 A, SMA SMA SMAJ75A Littelfuse

Q2 80 V Transistor, NPN, 80 V, 1 A, AECQ101, SOT-223 SOT-223 BCP56T1G ON Semiconductor

| R10, R13, R17, | R122 |
|:--- |:--- |
| RES, 0, 5%, 0.25 W, AEC-Q200 | Grade 0, 1206 |
| ERJ-8GEY0R00V | Panasonic | RES, 0, 5%, 0.25 W, AEC-Q200 Grade 0, 1206 ERJ-8GEY0R00V Panasonic

R20 100k RES, 100 k, 5%, 0.1 W, AEC-Q200 Grade 0, 0603

# CRCW0603100KJNE A Vishay-Dale

# R21, R22, R23, R24, R25, R26, R27, R28, R38, R41 RES, 0, 5%, 0.1 W, AEC-Q200 Grade 0, 0603

# CRCW06030000Z0E A Vishay-Dale

# R115, R116, R117, R118

# RES, 499, 1%, 0.1 W, 0603 RC0603FR-07499RL Yageo

# T1, T2

BMS TRANSFORMER SMT\_TRANSFOR MER\_8MM89\_10M M09

| HMU1228NL | Pulse |
|:--- |:--- |
| BQ79616EVM Schematic, Assembly, Layout, and BOM | www.ti.com |
| BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules | SLUUC37D - JULY 2019 - REVISED JUNE 2025 |

*BQ79616EVM Schematic, Assembly, Layout, and BOM* <https://www.ti.com>

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules* SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

# 8 BQ75614EVM Schematic, Assembly, Layout, and BOM

# Provided are the BQ75614EVM schematic, assembly, layout and BOM in their respective sections.

# 8.1 Schematic

# ALL DECOUPLING

# CAPS ARE AS CLOSE TO THE CHIP AS POSSIBLE GND tied to CELL0 at connector via a thick trace.

# GPIO6 GPIO7 GPIO8

# GPIO1 GPIO2 GPIO3 GPIO4 GPIO5

# CB0

CB1 CB2 CB3 CB4 CB5 CB6 CB7 CB8 CB9 CB10 CB11 CB12 CB13 CB14 CB15 CB16

# COMHP COMHN

# COMLP COMLN

# GND

# REFHM

# AVSS CVSS DVSS NFAULT

# TX RX

# BBN BBP

# VC16

VC15 VC14 VC13 VC12 VC11 VC10 VC9 VC8 VC7 VC6 VC5 VC4 VC3 VC2 VC1 VC0

# DVDD CVDD AVDD

# REFHP

# BAT

# NPNB

# LDOIN

# NEG5V

# TSREF

# GPIO5 GPIO4

# GPIO1

# GPIO6

# SRN SRP

# FAULT

# GPIO7

# GPIO2

# GPIO3

# VC14

# CB13

# VC12

# CB14

# VC11

# CB10

# CB11

# VC15

# CB12

# VC13

# VC9

# CB8

# VC7

# CB9

# VC6

# CB5

# CB6

# VC10

# CB7

# VC8

# REFHP

# AVDD

# COMLP

# REFHM

# COMHN COMHP

# COMLN

# VC0

# NEG5V

# AVSS

# LDOIN

# NPNB

# TSREF

# CVSS TX

# GPIO8

# RX

# CVDD

# DVSS

# DVDD

# VC4

# CB3

# VC2

# CB4

# VC1

# CB0

# CB1

# VC5

# CB2

# VC3

# BAT

# VC16

# CB15

# CB16

# PAD

# BQ75614PAPRQ1

# U1 10nF C5

# GND

# GND

# GND 1 µ F C6 1 µ F

# C9

| 1µF | C7 |
|:--- |:--- |
| 1µF | C8 |
| 1µF | C2 | 1 µ F C8 1 µ F C2

# GND

# GND

# GND

# GND 0.1uF

# C3 GND

# GND

# VC0

VC1 VC2 VC3 VC4 VC5 VC6 VC7 VC8 VC9 VC10 VC11 VC12 VC13 VC14 VC15 VC16

# CB0

CB1 CB2 CB3 CB4 CB5 CB6 CB7 CB8 CB9 CB10 CB11 CB12 CB13 CB14 CB15 CB16

# COMHP COMHN

# COMLP COMLN

# PWR 30.0

# R5 PWR Green

# D1

# J6

# GND 1.0k

# R121

# GND

# LDOIN

# R3

# R4 0.22 µ F

# C1

# GND

# PWR NPN Power Supply

# TP14

# GND

# GND

# TP13

# GND

# DVDD BBN NFAULT Test Points

# TP1

# TSREF

# TP2

# LDOIN

# TP3

# NEG5V

# TP4

# NPNB

# TP5

# CVDD

# TP6

# AVDD

# TP7

# REFHP

# TP8

# BAT

# TP12

# NFAULT

# TP11

# BBN

# TP10

# BBP

# TP9

# DVDD

# BBN

# BBP

# R9

# R12 0.47uF

# C10

# BBP\_CELL

# BBN\_CELL

# R24

# DNP

# R23

# DNP

# R28

# DNP

# R27

# DNP

# VC16

# VC15

# VC14

# VC13

# VC12

# R22

# DNP

# R26

# DNP

# CB16

# CB15

# R21

# DNP

# R25

# DNP

# CB14

# CB13

# CB12 Resistors for Lower Cell Count Applications (614, 612) BBP/BBN Bus Bar

# TP16 BBN\_CELL

# TP17 BBP\_CELL

# R13

# DNP

# R10

# DNP

# BBN

# BBP

# 0.47uF C11 TP19

# SRN\_S

# TP18

# SRP\_S SRP/SRN Current Sense

# GPIO8\_R

# GPIO5\_R GPIO6\_R GPIO7\_R

# GPIO4\_R GPIO3\_R GPIO2\_R GPIO1\_R

# J4

# GPIO8

| GPIO6 | GPIO7 |
|:--- |:--- |
| GPIO5 | GPIO4 |
| GPIO2 | GPIO1 |

# GPIO5 GPIO4

# GPIO2 GPIO1

# GPIO3

# J5

# TSREF

Jumpers to connect GPIOs to resistor divider and thermistor for temperature measurements. Jumpers to connect TSREF to ratiometric circuit. Low side NTC circuit. 10k

## t °

# RT7 10k

## t ° RT5 10k

## t °

# RT4 10k

## t °

# RT2 10k

## t °

# RT6 10k

## t °

# RT1

## 10k t °

# RT8 10k

## t °

# RT3 10.0k

# R11 10.0k

# R19 10.0k

# R8 10.0k

# R18 10.0k

# R7 10.0k

# R16 10.0k

# R15 10.0k

# R14

# GND

# PULLUP

# PULLUP

# GPIO1\_R

# GPIO2\_R

# GPIO3\_R

# GPIO4\_R

# GPIO5\_R

# GPIO6\_R

# GPIO7\_R

# GPIO8\_R

# GPIOs

# 1uF C12 **DNP** 100k

# R20

# DNP 2,4

# Q2

# DNP NPNB

# R17 **DNP**

# Q1

# NPNB

# REFHP BAT

# BBP

# AVDD

# TSREF LDOIN NEG5V NPNB

# CVDD

# GND

# TP15

# GND

# GND

# J3

**J3 Pin Description** 5 TX - to microcontroller UART RX 4 RX - to microcontroller UART TX 2 FAULTn - to microcontroller GPIO 1 GND - shared GND with microcontroller UART Communication

# J1

# TX

# J2 100k R2

# CVDD

# NFAULT 100k R120

# J17A

# R119

# RX\_C

# J17B

# GND

**J17 Pin Description** 8 TX - to microcontroller UART RX 7 RX - to microcontroller UART TX 3 FAULTn - to microcontroller GPIO 5 GND - shared GND with microcontroller

# USB2ANY\_TX\_3.3 0.1uF

# C59

# B2

# GND VCCA

# A2 A1 OE

# VCCB

# B1

# TXB0102DCUR

# U2

# GND

# TX

# CVDD USB2ANY\_3.3V

# J18 0.1uF

# C4

# GND

# USB2ANY\_RX\_3.3 100k R1

# USB2ANY\_3.3V

# 6 USB2ANY 3.3V

# 100k R6 **DNP**

# GND

# RX

# RX\_C

# USB2ANY\_3.3V

# Figure 8-1. BQ75614EVM Schematic Part 1

# www.ti.com

*BQ75614EVM Schematic, Assembly, Layout, and BOM*

# SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

# BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules

# CELL2

# CELL1

# CELL3

# CELL4

# CELL6

| 0.47uF | C39 |
|:--- |:--- |
| 0.47uF | C43 |
| 0.47uF | C55 |
| 0.47uF | C31 |
| 0.47uF | C35 |
| 0.47uF | C47 |
| 0.47uF | C51 |
| 0.47uF | C33 |
| 0.47uF | C37 |
| 0.47uF | C49 |
| 0.47uF | C53 |
| 0.47uF | C45 |
| 0.47uF | C41 | 0.47uF C43 0.47uF C55 0.47uF C31 0.47uF C35 0.47uF C47 0.47uF C51 0.47uF C33 0.47uF C37 0.47uF C49 0.47uF C53 0.47uF C45 0.47uF C41

# CELL0S 0.47uF C56

# CELL7 0.47uF C27 0.47uF C29

# CELL8 0.47uF C23 0.47uF C25

# CELL9 0.47uF C52 0.47uF C54

# CB8

# VC8

# CB8 VC8

# CELL10 0.47uF C48 0.47uF C50

# CELL11 0.47uF C44 0.47uF C46

# CELL12 0.47uF C40 0.47uF C42

# CELL13 0.47uF C36 0.47uF C38

# CELL14 0.47uF C32 0.47uF C34

# CELL15 0.47uF C28 0.47uF C30

# CELL16S 0.47uF C24 0.47uF C26

# CB6

# CB5

# CB4

# CB3

# CB2

# CB1

# CB16

# CB15

# CB14

# CB13

# CB12

# CB11

# CB10

# CB9

# R110

# R106

# R102

# R98

# R94

# R90

# R85

# R81

# R109

# R105

# R101

# R97

# R93

# R89

# R84

# R80

# R113

| 10.0 | R114 |
| ---: |:--- |
| 10.0 | R111 |
| 10.0 | R82 |
| 10.0 | R86 |
| 10.0 | R91 |
| 10.0 | R95 |
| 10.0 | R99 |
| 10.0 | R103 |
| 10.0 | R107 |
| 10.0 | R83 |
| 10.0 | R87 |
| 10.0 | R92 |
| 10.0 | R96 |
| 10.0 | R100 |
| 10.0 | R104 |
| 10.0 | R108 |
| 10.0 | R112 |

# 10.0 R111

# 10.0 R82

# 10.0 R86

# 10.0 R91

# 10.0 R95

# 10.0 R99

# 10.0 R103

# 10.0 R107

# 10.0 R83

# 10.0 R87

# 10.0 R92

# 10.0 R96

# 10.0 R100

# 10.0 R104

# 10.0 R108

# 10.0 R112

# J15

# PWR

# CB0

# CB1

# VC0

# VC1

# CB3

# CB2

# CB4

# VC1

# VC2

# VC3

# VC4

# VC5

# VC6

# VC7

# CB5

# CB6

# CB7

# CB8

# VC2

# VC3

# VC4

# VC5

# VC6

# VC7

# VC8 VC16

# VC15

# VC14

# VC13

# VC12

# VC11

# VC10

# VC9 VC9

# VC10

# VC11

# VC12

# VC13

# VC14

# VC15

# VC16

# CB16

# CB15

# CB14

# CB13

# CB12

# CB11

# CB10

# CB9

# CELL1

# CELL2

# CELL3

# CELL4

# CELL5

# CELL6

# CELL7

# CELL8

# CELL15

# CELL14

# CELL13

# CELL12

# CELL11

# CELL10

# CELL9

# CB0

# GND

# GND

# R88 CB7

# TP21

# CELL1

# TP22

# CELL2

# TP23

# CELL3

# TP24

# CELL4

# TP25

# CELL5

# TP26

# CELL6

# TP27

# CELL7

# TP28

# CELL8

# TP36

# CELL16S

# TP35

# CELL15

# TP34

# CELL14

# TP33

# CELL13

# TP32

# CELL12

# TP31

# CELL11

# TP30

# CELL10

# TP29

# CELL9

# TP37

# PWR

# TP20

# CELL0S

# CELL16

# CELL0 CELL0

# 75V

# D4 **DNP**

# J14

# J16

# CELL0

# CELL0

# CELL16

# CELL16S

# CELL15

# CELL14

# CELL13

# CELL12

# CELL11

# CELL10

# CELL9

# CELL8

# CELL7

# CELL6

# CELL5

# CELL4

# CELL3

# CELL2

# CELL1

# CELL0S

# CELL0

# CELL16

# CELL0

# CELL5

# VC0

# R122 CELL14

# VSTACK

# CELL16S

# PWR

# Figure 8-2. BQ75614EVM Schematic Part 2

# BQ75614EVM Schematic, Assembly, Layout, and BOM <https://www.ti.com>

# BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules SLUUC37D - JULY 2019 - REVISED JUNE 2025

# Submit Document Feedback

# CELL5 CELL4 CELL3 CELL2 CELL1

# R48

# R47

# R46

# R45

# R44

# R43

# CELL6

# CELL0

# C4\_L C3\_L C2\_L C1\_L

# C6\_R C5\_R C4\_R C3\_R C2\_R C1\_R

# R49 CELL0

# GND

# S2

# C5\_L C6\_L

# R42

# R37

# C7\_L C8\_L

# CELL7 CELL8 C7\_R C8\_R

# R35

# R34

# R33

# R36

# R30 **DNP**

# R29 **DNP**

# R32

# R31

# S1

# C16\_R C15\_R C14\_R C13\_R C12\_R C11\_R

# C14\_L C13\_L C12\_L C11\_L

# C15\_L C16\_L

# C10\_L C9\_L

# C10\_R C9\_R CELL9 CELL10

# CELL15 CELL14 CELL13 CELL12 CELL11

# CELL16S

# J8

# J7

# GND

# C5\_R C4\_R C3\_R C2\_R C1\_R C7\_R C8\_R

# C11\_R C10\_R C9\_R

# J9

# C16\_R C15\_R C14\_R C13\_R C6\_R C12\_R

# CELL1 CELL2 CELL3 CELL4 CELL5 CELL6 CELL7 CELL8

# CELL9

CELL10 CELL11 CELL12 CELL13 CELL14 CELL15 CELL16S

# CELL0

# TP38

# GND

# TP39

# CELL0

# R40

# BBN\_CELL

# BBP\_CELL

# 0.1 R39

# R38

# DNP

# R41

# DNP

# TP40

# VSTACK

# VSTACK

# Figure 8-3. BQ75614EVM Schematic Part 3

# www.ti.com

*BQ75614EVM Schematic, Assembly, Layout, and BOM*

# SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

# BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules

# 24V

# D3 **DNP**

# COMHN

# COMHP

# J11

# DNP

# ISO\_COMMH\_N ISO\_COMMH\_P

# J10

# DNP

# COMML\_P

# COMML\_N

# GND

# GND

# ISO\_COMML\_N ISO\_COMML\_P

# 24V

# D2 **DNP**

# T1

# DNP

# GND

# ISO\_COMML\_P

# ISO\_COMML\_N

# T2

# DNP

# GND

# ISO\_COMMH\_P

| 220pF | C13 | DNP |
|:--- |:--- |:--- |
| 220pF | C15 | DNP |
| 220pF | C16 | DNP |
| 220pF | C17 | DNP |
| 220pF | C18 | DNP |
| 220pF | C14 | DNP |

# 220pF C15 **DNP**

# 220pF C16 **DNP**

# 220pF C17 **DNP**

# 220pF C18 **DNP**

# 220pF C14 **DNP** 2200pF

# C20

# DNP 2200pF

# C21

# DNP 470uH

# L2

# DNP 2200pF

# C22

# DNP 2200pF

# C19

# DNP 470uH

# L1

# DNP

# COMML\_P\_OPT

# COMML\_P\_OPT

# COMML\_N\_OPT

# COMML\_N\_OPT

# ISO\_COMML\_P

# ISO\_COMML\_N COMMH\_N\_OPT

# COMMH\_P\_OPT ISO\_COMMH\_P

# ISO\_COMMH\_N

# R53

# DNP

# R57

# DNP

# R52

# DNP

# R56

# DNP

# R70

# DNP

# R76

# DNP

# R71

# DNP

# R77

# DNP

# R79

# DNP

# R69

# DNP

# R73

# DNP

# R75

# DNP

# R78

# DNP

# R74

# DNP

# R72

# DNP

# R68

# DNP

# R54

# DNP

# R50

# DNP

# R51

# DNP

# R55

# DNP

# TP41

# GND

# R60

# DNP

# R66

# DNP

# R59

# DNP

# R65

# DNP

# R58

# DNP

# R64

# DNP

# R61

# DNP

# R67

# DNP

# COMML\_N\_OPT

# COMML\_P\_OPT

# COMMH\_P\_OPT

# COMMH\_P\_OPT

# COMMH\_N\_OPT

# COMMH\_N\_OPT

# COMMH\_P

# COMMH\_N

# ISO\_COMMH\_N

# COMLN

# COMLP

# GND

# GND

# J13

# DNP J12

# DNP

| R115 | DNP |
|:--- |:--- |
| R117 | DNP |
| R116 | DNP |

# R117 **DNP**

# R116 **DNP**

# R118 **DNP** 10nF

# C58

# DNP 10nF

# C57

# DNP 10.0k R62 **DNP**

# GND

# 10.0k R63 **DNP**

# J19

# DNP

# J20

# DNP

# GND COMMH\_N COMMH\_P

# GND COMML\_N COMML\_P

# Figure 8-4. BQ75614EVM Schematic Part 4

# BQ75614EVM Schematic, Assembly, Layout, and BOM <https://www.ti.com>

# BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules SLUUC37D - JULY 2019 - REVISED JUNE 2025

# Submit Document Feedback

## 8.2 Assembly

## Figure 8-5. BQ75614EVM Assembly Top

<https://www.ti.com> *BQ75614EVM Schematic, Assembly, Layout, and BOM*

SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules*

## Figure 8-6. BQ75614EVM Assembly Bottom

## 8.3 Layout

## See section 7.3 for same drawings as for BQ79616.

*BQ75614EVM Schematic, Assembly, Layout, and BOM* <https://www.ti.com>

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules* SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

## 8.4 BQ75614EVM Bill of Materials (BOM)

## Table 8-1. BQ75614EVM Bill of Materials

**Designator** **Qty** **Value** **Description** **Package ** **Reference** **Part Number** **Manufacturer** **Alternate Part ** **Number** **Alternate ** **Manufacturer**!PCB1 Printed Circuit Board BMS021 Any

C1 Multilayer Ceramic Capacitors MLCC - SMD/SMT 1206 0.22uF 100volts X7R +/-10%

# GCM31MR72A224KA 37L Murata

# C2, C6, C8, C9 CAP CER 0603 1UF 10 V X7R 10% 0603 (1608 Metric) C0603C105K8RACA UTO

# KEMET

# C3, C4, C57, C58, C59

# 0.1uF

CAP, CERM, 0.1 uF, 10 V, +/- 10%, X7R, AEC-Q200 Grade 1, 0402

# GCM155R71A104KA 55D MuRata

# C5

0.01uF CAP, CERM, 0.01 µF, 100 V,+/- 10%, X7R, AEC-Q200 Grade 1,

# GCM188R72A103KA 37J MuRata

# C7

4.7uF CAP, CERM, 4.7 uF, 10 V, +/- 20%, X7R, 0805

# C2012X7R1A475M12 5AC

# TDK

# C10, C11, C23,

C24, C25, C26, C27, C28, C29, C30, C31, C32, C33, C34, C35, C36, C37, C38, C39, C40, C41, C42, C43, C44, C45, C46, C47, C48, C49, C50, C51, C52, C53, C54, C55, C56

# 0.47uF

CAP, CERM, 0.47 uF, 16 V, +/- 10%, X7R, AEC-Q200 Grade 1,

# GCM188R71C474KA 55D MuRata

# C12, C60

1uF CAP, CERM, 1 uF, 16 V, +/- 10%, X7R, AEC-Q200 Grade 1, 0603

# GCM188R71C105KA 64D MuRata

D1 Green LED, Green, SMD LED\_0805 LTST-C170KGKT Lite-On

# D3

24 V Diode, TVS, Bi, 24 V, 70 Vc, AECQ101, SOT-23

SOT-23 PESD1CAN,215 NXP Semiconductor ESD562-Q1 Texas Instruments

# FID1, FID2, FID3, FID4, FID5, FID6

Fiducial mark. There is nothing to buy or mount.

| N/A | N/A | N/A |
|:--- |:--- |:--- |
| H1, H2, H3, H4 | Machine Screw, Round, #4-40 x | 1/4, Nylon, Philips panhead |
| Screw | NY PMS 440 0025 | PH |

H1, H2, H3, H4 Machine Screw, Round, #4-40 x 1/4, Nylon, Philips panhead Screw NY PMS 440 0025 PH B&F Fastener Supply

H5, H6, H7, H8 Standoff, Hex, 0.5"L #4-40 Nylon Standoff 1902C Keystone

# H9 CONN HOUSING 22POS.100 W / LATCH 50-57-9422 Molex

H11, H12 Rectangular Housing Connector, 4 Pos, 2.54mm

| 50-57-9404 | Molex |
|:--- |:--- |
| www.ti.com | BQ75614EVM Schematic, Assembly, Layout, and BOM |
| SLUUC37D - JULY 2019 - REVISED JUNE 2025 | Submit Document Feedback |

<https://www.ti.com> *BQ75614EVM Schematic, Assembly, Layout, and BOM*

SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules*

## Table 8-1. BQ75614EVM Bill of Materials (continued)

**Designator** **Qty** **Value** **Description** **Package ** **Reference** **Part Number** **Manufacturer** **Alternate Part ** **Number**

| Alternate | Manufacturer |
|:--- |:--- |
| J1, J2, J5, J6, J18, | J21 |
| Header, 2.54mm, 1x2, Tin, Black, | TH |
| Header, 2.54mm, | 2x1, TH |

# J1, J2, J5, J6, J18, J21 Header, 2.54mm, 1x2, Tin, Black, TH Header, 2.54mm, 2x1, TH PEC01DAAN Sullins Connector Solutions

J3 Header, 0.5mm, 6x1, R/A, Gold, TH Header, 0.5mm, 6x1, R/A, TH 22-12-4062 Molex J4 Header, 2.54 mm, 8x2, Tin, Vertical, TH Header, 2.54 mm, 8x2, TH PEC08DAAN Sullins Connector Solutions

J7, J8, J9 Header, 100mil, 6x1, Tin, TH TH, 6-Leads, Body 608x100mil, Pitch 100mil PEC06SAAN Sullins Connector Solutions

J14, J16 Header, 100mil, 2x1, Tin, TH Header, 2 PIN, 100mil, Tin PEC02SAAN Sullins Connector Solutions

J15 Connector Header Through Hole, Right Angle 22 position 0.100" (2.54mm) HDR22 Molex

# J17 CONN HEADER 10POS.100 DL R/A AU HDR10 TSW-105-08-L-D-RA Samtec

LBL1 Thermal Transfer Printable Labels, 0.650" W x 0.200" H - 10,000 per roll PCB Label 0.650 x 0.200 inch THT-14-423-10 Brady

Q1 150 V Transistor, NPN, 150 V, 1 A, AECQ101, DPAK DPAK ZXTN4004KTC Diodes Inc.

R2, R120, R123 100k RES, 100 k, 5%, 0.1 W, AEC-Q200 Grade 0, 0603

# CRCW0603100KJNE A Vishay-Dale

# R3 RES, 100, 1%, 0.75 W, AEC-Q200 Grade 0, 2010

# CRCW2010100RFKE F Vishay-Dale

# R4 RES, 200, 1%, 0.75 W, AEC-Q200 Grade 0, 2010

# CRCW2010200RFKE F Vishay-Dale

# R5

30.0 RES, 30.0, 1%, 0.1 W, AEC-Q200 Grade 0, 0603 ERJ-3EKF30R0V Panasonic

# R7, R8, R11, R14, R15, R16, R18, R19

10.0k RES, 10.0 k, 1%, 0.1 W, AECQ200 Grade 0, 0603

# CRCW060310K0FKE A Vishay-Dale

# R9, R12 RES, 402, 1%, 0.1 W, AEC-Q200 Grade 0, 0603

# CRCW0603402RFKE A Vishay-Dale

# R31, R32, R33,

R34, R35, R36, R37, R42, R43, R44, R45, R46, R47, R48 RES, 100, 1%, 1 W, AEC-Q200 Grade 0, 2512

# CRCW2512100RFKE G Vishay-Dale

*BQ75614EVM Schematic, Assembly, Layout, and BOM* <https://www.ti.com>

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules* SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

## Table 8-1. BQ75614EVM Bill of Materials (continued)

**Designator** **Qty** **Value** **Description** **Package ** **Reference** **Part Number** **Manufacturer** **Alternate Part ** **Number** **Alternate ** **Manufacturer**

# R39

0.1 RES, 0.1, 5%, 0.1 W, 0603 CRL0603-JWR100ELF Bourns

# R40, R49, R122 RES, 0, 5%, 0.25 W, AEC-Q200 Grade 0, 1206 ERJ-8GEY0R00V Panasonic

# R80, R81, R84,

R85, R89, R90, R93, R94, R97, R98, R101, R102, R105, R106, R109, R110, R113 RES, 100, 0.1%, 0.1 W, AEC-Q200 Grade 0, 0603 ERA-3AEB101V Panasonic

# R82, R83, R86,

R87, R91, R92, R95, R96, R99, R100, R103, R104, R107, R108, R111, R112, R114

10.0 RES, 10.0, 1%, 0.75 W, AEC-Q200 Grade 0, 1210

# CRCW121010R0FKE AHP Vishay-Dale

# R88 RES, 0, 5%, 0.1 W, AEC-Q200 Grade 0, 0603

# CRCW06030000Z0E A Vishay-Dale

# R119 RES, 100, 5%, 0.25 W, AEC-Q200 Grade 0, 0603

# ESR03EZPJ101 Rohm

R121, R128 1.0k RES, 1.0 k, 5%, 0.1 W, AEC-Q200 Grade 0, 0603

# CRCW06031K00JNE A Vishay-Dale

# RT1, RT2, RT3, RT4, RT5, RT6, RT7, RT8 10k Thermistor NTC, 10k ohm, 2%, ERT-J1VG103GA Panasonic

S1, S2 Switch, SPST 8Pos, Rocker, TH 9.65X8X22.4mm 76SB08ST Grayhill

# SH1, SH2, SH3, SH4, SH5, SH6, SH7, SH8

Shunt, 100mil, Gold plated, Black Shunt 2 pos. 100 mil 881545-2 TE Connectivity

<https://www.ti.com> *BQ75614EVM Schematic, Assembly, Layout, and BOM*

SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules*

## Table 8-1. BQ75614EVM Bill of Materials (continued)

**Designator** **Qty** **Value** **Description** **Package ** **Reference** **Part Number** **Manufacturer** **Alternate Part ** **Number** **Alternate ** **Manufacturer**

# TP1, TP2, TP3,

TP4, TP5, TP6, TP7, TP8, TP9, TP10, TP11, TP12, TP16, TP17, TP18, TP19, TP21, TP22, TP23, TP24, TP25, TP26, TP27, TP28, TP29, TP30, TP31, TP32, TP33, TP34, TP35, TP36, TP42, TP43, TP44

Test Point, Multipurpose, White, TH White Multipurpose Testpoint Keystone

TP13, TP14, TP15 Terminal, Turret, TH, Triple Keystone1598-2 1598-2 Keystone

TP20, TP38, TP39 Test Point, Multipurpose, Black, TH Black Multipurpose Testpoint Keystone

TP37, TP40 Test Point, Multipurpose, Red, TH Red Multipurpose Testpoint Keystone

# U1 BQ75614-Q1, PAP0064F (HTQFP-64)

| PAP0064F | BQ75614PAPRQ1 | Texas Instruments | Texas Instruments |
|:--- |:--- |:--- |:--- |
| U2 | Automotive, Low Power, Quad- | Channel 2/2 Digital Isolator, | DW0016B (SOIC-16) |
| DW0016B | ISO7342CQDWRQ1 | Texas Instruments | ISO7342CQDWQ |

U2 Automotive, Low Power, QuadChannel 2/2 Digital Isolator, DW0016B (SOIC-16)

DW0016B ISO7342CQDWRQ1 Texas Instruments ISO7342CQDWQ Texas Instruments

# C13, C14

100 pF CAP, CERM, 100 pF, 50 V,+/- 5%, C0G/NP0, AEC-Q200 Grade 1, 0603

# GCM1885C1H101JA 16J MuRata

# C15, C16, C17, C18

# 220 pF CAP, CERM, 220 pF, 50 V,+/- 5%, X7R, 0603 CL10B221JB8NNNC Samsung ElectroMechanics

# C19, C20, C21, C22

# 2200 pF

CAP, CERM, 2200 pF, 2000 V,+/- 10%, X7R, AEC-Q200 Grade 1, 1206J2K00222KXR Knowles Capacitors

# C61, C62

0.01uF CAP, CERM, 0.01 uF, 50 V, +/- 10%, X7R, 0603 CL10B103KB8NCNC Samsung ElectroMechanics

| D2, D5 | 24 V | Diode, TVS, Bi, 24 V, 70 Vc, AEC- | Q101, SOT-23 |
|:--- |:--- |:--- |:--- |
| SOT-23 | PESD1CAN,215 | NXP Semiconductor ESD562-Q1 | Texas Instruments |
| D4 | 75 V | Diode, TVS, Uni, 75 V, 121 Vc, 400 | W, 3.3 A, SMA |

SOT-23 PESD1CAN,215 NXP Semiconductor ESD562-Q1 Texas Instruments

D4 75 V Diode, TVS, Uni, 75 V, 121 Vc, 400 W, 3.3 A, SMA SMA SMAJ75A Littelfuse

*BQ75614EVM Schematic, Assembly, Layout, and BOM* <https://www.ti.com>

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules* SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

## Table 8-1. BQ75614EVM Bill of Materials (continued)

**Designator** **Qty** **Value** **Description** **Package ** **Reference** **Part Number** **Manufacturer** **Alternate Part ** **Number** **Alternate ** **Manufacturer**

J10, J11 Header(shrouded), 2.54mm, 4x1, R/A, Gold, TH Header(shrouded), 2.54mm, 4x1, R/A, TH 70551-0038 Molex

J12, J13 Header, 100mil, 2x1, Tin, TH Header, 2 PIN, 100mil, Tin PEC02SAAN Sullins Connector Solutions

J19, J20 Header, 100mil, 3x1, Tin, TH Header, 3 PIN, 100mil, Tin PEC03SAAN Sullins Connector Solutions

L1, L2 470uH Coupled inductor, 470 uH, 0.4 A, 0.35 ohm, SMD 5x3.3mm Wurth Elektronik

Q2 80 V Transistor, NPN, 80 V, 1 A, AECQ101, SOT-223 SOT-223 BCP56T1G ON Semiconductor

# R10, R13, R17 RES, 0, 5%, 0.25 W, AEC-Q200 Grade 0, 1206 ERJ-8GEY0R00V Panasonic

R20 100k RES, 100 k, 5%, 0.1 W, AEC-Q200 Grade 0, 0603

# CRCW0603100KJNE A Vishay-Dale

# R21, R22, R23, R24, R25, R26, R27, R28, R38, R41 RES, 0, 5%, 0.1 W, AEC-Q200 Grade 0, 0603

# CRCW06030000Z0E A Vishay-Dale

# R29, R30 RES, 100, 1%, 1 W, AEC-Q200 Grade 0, 2512

# CRCW2512100RFKE G Vishay-Dale

# R50, R51, R52,

R53, R54, R55, R56, R57, R68, R69, R70, R71, R72, R73, R74, R75, R76, R77, R78, R79 RES, 0, 5%, 0.333 W, AEC-Q200 Grade 0, 0805

# CRCW08050000Z0E AHP Vishay-Dale

# R58, R61, R64, R67

# RES, 0, 5%, 0.1 W, 0603 RC0603JR-070RL Yageo

| R59, R60, R65, | R66 |
|:--- |:--- |
| RES, 51, 5%, 0.1 W, AEC-Q200 | Grade 0, 0603 |
| CRCW060351R0JNE | A | RES, 51, 5%, 0.1 W, AEC-Q200 Grade 0, 0603

# CRCW060351R0JNE A Vishay-Dale

R62, R63 1.00k RES, 1.00 k, 1%, 0.1 W, 0603 ERJ-3EKF1001V Panasonic

# R115, R116, R117, R118

# RES, 499, 1%, 0.1 W, 0603 RC0603FR-07499RL Yageo

# T1, T2

BMS TRANSFORMER SMT\_TRANSFORM ER\_8MM89\_10MM

| HMU1228NL | Pulse |
|:--- |:--- |
| www.ti.com | BQ75614EVM Schematic, Assembly, Layout, and BOM |
| SLUUC37D - JULY 2019 - REVISED JUNE 2025 | Submit Document Feedback |

<https://www.ti.com> *BQ75614EVM Schematic, Assembly, Layout, and BOM*

SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules*

# 9 BQ79656EVM Schematic, Assembly, Layout, and BOM

# Provided are the BQ79656EVM schematic, assembly, and BOM in their respective sections.

# 9.1 Schematic

# PWR

# CB1

# CB14

# CB15

# CB16

# VC0

# VC1

# VC2

# VC3

# VC4

# VC5

# VC6

# VC7

# VC8

# VC9

# VC10

# VC11

# VC12

# VC13

# VC14

# VC15

# VC16

# CB2

# CB3

# CB4

# CB5

# CB6

# CB7

# CB8

# CB9

# CB10

# CB11

# CB12

# CB13

# COMLN

# COMLP COMHN

# COMHP

# CB0

| BBP\_CELL | BBN\_CELL |
|:--- |:--- |
| bq79616 | BMS021E3\_bq79616.SchDoc |
| Hardware | BMS021E3\_EVM\_Hardware.SchDoc | bq79616 BMS021E3\_bq79616.SchDoc Hardware BMS021E3\_EVM\_Hardware.SchDoc

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

# PWR

# CELL1

# CELL2

# CELL3

# CELL4

# CELL5

# CELL6

# CELL7

# CELL8

# CELL9

# CELL10

# CELL11

# CELL12

# CELL13

# CELL14

# CELL15

# CELL16S

# CB0 CELL0

# VSTACK Battery Connector BMS021E3\_VC\_CB.SchDoc

# COMLP COMHN

# COMLN

# COMHP

Daisy Chain Isolation BMS021E3\_Communications.SchDoc

# CELL1

# CELL2

# CELL3

# CELL4

# CELL5

# CELL6

# CELL7

# CELL8

# CELL9

# CELL10

# CELL11

# CELL12

# CELL13

# CELL14

# CELL15

# CELL16S

# CELL0

# BBP\_CELL BBN\_CELL

# VSTACK Cell Simulator BMS021E3\_CellSimulator.SchDoc

# Figure 9-1. BQ79656EVM Schematic Block Diagram

# BQ79656EVM Schematic, Assembly, Layout, and BOM <https://www.ti.com>

# BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules SLUUC37D - JULY 2019 - REVISED JUNE 2025

# Submit Document Feedback

# ALL DECOUPLING

# CAPS ARE AS CLOSE TO THE CHIP AS POSSIBLE GND tied to CELL0 at connector via a thick trace.

# GPIO6 GPIO7 GPIO8

# GPIO1 GPIO2 GPIO3 GPIO4 GPIO5

# CB0

CB1 CB2 CB3 CB4 CB5 CB6 CB7 CB8 CB9 CB10 CB11 CB12 CB13 CB14 CB15 CB16

# COMHP COMHN

# COMLP COMLN

# NFAULT

# TX RX

# BBN BBP

# VC16

VC15 VC14 VC13 VC12 VC11 VC10 VC9 VC8 VC7 VC6 VC5 VC4 VC3 VC2 VC1 VC0

# DVDD CVDD AVDD

# REFHP

# BAT

# NPNB

# LDOIN

# NEG5V

# TSREF

# GPIO5 GPIO4

# GPIO1

# GPIO6

# SRN SRP

# FAULT

# GPIO7

# GPIO2

# GPIO3

# VC14

# CB13

# VC12

# CB14

# VC11

# CB10

# CB11

# VC15

# CB12

# VC13

# VC9

# CB8

# VC7

# CB9

# VC6

# CB5

# CB6

# VC10

# CB7

# VC8

# REFHP

# AVDD

# COMLP

# REFHM

# COMHN COMHP

# COMLN

# VC0

# NEG5V

# AVSS

# LDOIN

# NPNB

# TSREF

# CVSS TX

# GPIO8

# RX

# CVDD

# DVSS

# DVDD

# VC4

# CB3

# VC2

# CB4

# VC1

# CB0

# CB1

# VC5

# CB2

# VC3

# BAT

# VC16

# CB15

# CB16

# PAD

# BQ79656PAPQ1

# U1 10nF C5

# GND

# GND 1µF C6 1µF

# C9 4.7µF

# C7 1µF C8 1µF C2

# GND

# GND

# GND

# GND 0.1uF

# C3 GND

# GND

# VC0

VC1 VC2 VC3 VC4 VC5 VC6 VC7 VC8 VC9 VC10 VC11 VC12 VC13 VC14 VC15 VC16

# CB0

CB1 CB2 CB3 CB4 CB5 CB6 CB7 CB8 CB9 CB10 CB11 CB12 CB13 CB14 CB15 CB16

# COMHP COMHN

# COMLP COMLN

# PWR 30.0

# R5 PWR Green

# D1

# J6

# GND 1.0k

# R121

# GND

# LDOIN

# R3

# R4 0.22µF

# C1

# GND

# PWR NPN Power Supply

# TP14

# GND

# GND

# TP13

# GND

# DVDD BBN NFAULT Test Points

# TP1

# TSREF

# TP2

# LDOIN

# TP3

# NEG5V

# TP4

# NPNB

# TP5

# CVDD

# TP6

# AVDD

# TP7

# REFHP

# TP8

# BAT

# TP43

# NFAULT

# TP11

# BBN

# TP10

# BBP

# TP9

# DVDD

# BBN

# BBP

# R9

# R12 0.47uF

# C10

# BBP\_CELL

# BBN\_CELL

# R24

# DNP

# R23

# DNP

# R28

# DNP

# R27

# DNP

# VC16

# VC15

# VC14

# VC13

# VC12

# R22

# DNP

# R26

# DNP

# CB16

# CB15

# R21

# DNP

# R25

# DNP

# CB14

# CB13

# CB12 Resistors for Lower Cell Count Applications (614, 612) BBP/BBN Bus Bar

# TP16 BBN\_CELL

# TP17 BBP\_CELL

# R13

# DNP

# R10

# DNP

# BBN

# BBP

# 0.47uF C11 TP19

# SRN\_S

# TP18

# SRP\_S SRP/SRN Current Sense

# GPIO8\_R

# GPIO5\_R GPIO6\_R GPIO7\_R

# GPIO4\_R GPIO3\_R GPIO2\_R GPIO1\_C

# J4

# GPIO8

| GPIO6 | GPIO7 |
|:--- |:--- |
| GPIO5 | GPIO4 |
| GPIO2 | GPIO1 |

# GPIO5 GPIO4

# GPIO2 GPIO1

# GPIO3

# J5

# TSREF

Jumpers to connect GPIOs to resistor divider and thermistor for temperature measurements. Jumpers to connect TSREF to ratiometric circuit. Low side NTC circuit. 10k

## t°

# RT7 10k

## t° RT5 10k

## t°

# RT4 10k

## t°

# RT2 10k

## t°

# RT6 10k

## t°

# RT1

## 10k t°

# RT8 10k

## t°

# RT3 10.0k

# R11 10.0k

# R19 10.0k

# R8 10.0k

# R18 10.0k

# R7 10.0k

# R16 10.0k

# R15 10.0k

# R14

# GND

# PULLUP

# PULLUP

# GPIO1\_R

# GPIO2\_R

# GPIO3\_R

# GPIO4\_R

# GPIO5\_R

# GPIO6\_R

# GPIO7\_R

# GPIO8\_R

# GPIOs 1uF C12 100k

# R20

# DNP 2,4

# Q2

# DNP NPNB

# R17 DNP

# Q1

# NPNB

# REFHP BAT

# BBP

# AVDD

# TSREF LDOIN NEG5V NPNB

# CVDD

# GND

# TP15

# GND

# GND

# J3

J3 Pin Description 5 TX - to microcontroller UART RX 4 RX - to microcontroller UART TX 2 FAULTn - to microcontroller GPIO 1 GND - shared GND with microcontroller UART Communication

# J1

# TX

# J2 100k R2

# CVDD

# NFAULT 100k R120

# J17A

# R119

# RX\_C

# J17B

J17 Pin Description 8 TX - to microcontroller UART RX 7 RX - to microcontroller UART TX 3 FAULTn - to microcontroller GPIO 5 GND - shared GND with microcontroller 0.1uF

# C59 0.1uF

# C4

# GND 6 USB2ANY 3.3V

# RX

# INA

# INB

# INC

# IND

# OUTA

# OUTB

# OUTC

# OUTD

| EN1 | EN2 |
|:--- |:--- |
| VCC1 | VCC2 |
| GND1 | GND2 |
| GND1 | GND2 |

# VCC1 VCC2

# GND1 GND2

# GND1 GND2

# ISO7342CQDWRQ1

# U2

# GND\_ISO 0.1uF

# C57 0.1uF

# C58

# USB2ANY\_TX\_3.3 100k R123

# GND\_ISO 1.0k

# R128 GPIO1\_R

# TP42

# TX

# TP12

# RX

# CVDD CVDD\_CO

# NFAULT\_C

# NFAULT\_C

# USB2ANY\_TX\_3.3

# USB2ANY\_3.3V

# USB2ANY\_3.3V

# USB2ANY\_RX\_3.3

# USB2ANY\_RX\_3.3

# CVDD\_CO

# RX\_CO

# TX

# NF\_J

# GND GND\_ISO

# USB2ANY\_3.3V

# RX

# TX

# J18

# GND

# GND

# J21

# RX 1uF C60

# GND

# TP44

# GPIO1\_R

# 24V

# D3

# NF\_J

# Figure 9-2. BQ79656EVM Schematic Part 1

# www.ti.com

*BQ79656EVM Schematic, Assembly, Layout, and BOM*

# SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

# BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules

# CELL2

# CELL1

# CELL3

# CELL4

# CELL6

| 0.47uF | C39 |
|:--- |:--- |
| 0.47uF | C43 |
| 0.47uF | C55 |
| 0.47uF | C31 |
| 0.47uF | C35 |
| 0.47uF | C47 |
| 0.47uF | C51 |
| 0.47uF | C33 |
| 0.47uF | C37 |
| 0.47uF | C49 |
| 0.47uF | C53 |
| 0.47uF | C45 |
| 0.47uF | C41 | 0.47uF C43 0.47uF C55 0.47uF C31 0.47uF C35 0.47uF C47 0.47uF C51 0.47uF C33 0.47uF C37 0.47uF C49 0.47uF C53 0.47uF C45 0.47uF C41

# CELL0S 0.47uF C56

# CELL7 0.47uF C27 0.47uF C29

# CELL8 0.47uF C23 0.47uF C25

# CELL9 0.47uF C52 0.47uF C54

# CB8

# VC8

# CB8 VC8

# CELL10 0.47uF C48 0.47uF C50

# CELL11 0.47uF C44 0.47uF C46

# CELL12 0.47uF C40 0.47uF C42

# CELL13 0.47uF C36 0.47uF C38

# CELL14 0.47uF C32 0.47uF C34

# CELL15 0.47uF C28 0.47uF C30

# CELL16S 0.47uF C24 0.47uF C26

# CB6

# CB5

# CB4

# CB3

# CB2

# CB1

# CB16

# CB15

# CB14

# CB13

# CB12

# CB11

# CB10

# CB9

# R110

# R106

# R102

# R98

# R94

# R90

# R85

# R81

# R109

# R105

# R101

# R97

# R93

# R89

# R84

# R80

# R113

| 10.0 | R114 |
| ---: |:--- |
| 10.0 | R111 |
| 10.0 | R82 |
| 10.0 | R86 |
| 10.0 | R91 |
| 10.0 | R95 |
| 10.0 | R99 |
| 10.0 | R103 |
| 10.0 | R107 |
| 10.0 | R83 |
| 10.0 | R87 |
| 10.0 | R92 |
| 10.0 | R96 |
| 10.0 | R100 |
| 10.0 | R104 |
| 10.0 | R108 |
| 10.0 | R112 |

# 10.0 R111

# 10.0 R82

# 10.0 R86

# 10.0 R91

# 10.0 R95

# 10.0 R99

# 10.0 R103

# 10.0 R107

# 10.0 R83

# 10.0 R87

# 10.0 R92

# 10.0 R96

# 10.0 R100

# 10.0 R104

# 10.0 R108

# 10.0 R112

# J15

# PWR

# CB0

# CB1

# VC0

# VC1

# CB3

# CB2

# CB4

# VC1

# VC2

# VC3

# VC4

# VC5

# VC6

# VC7

# CB5

# CB6

# CB7

# CB8

# VC2

# VC3

# VC4

# VC5

# VC6

# VC7

# VC8 VC16

# VC15

# VC14

# VC13

# VC12

# VC11

# VC10

# VC9 VC9

# VC10

# VC11

# VC12

# VC13

# VC14

# VC15

# VC16

# CB16

# CB15

# CB14

# CB13

# CB12

# CB11

# CB10

# CB9

# CELL1

# CELL2

# CELL3

# CELL4

# CELL5

# CELL6

# CELL7

# CELL8

# CELL15

# CELL14

# CELL13

# CELL12

# CELL11

# CELL10

# CELL9

# CB0

# GND

# GND

# R88 CB7

# TP21

# CELL1

# TP22

# CELL2

# TP23

# CELL3

# TP24

# CELL4

# TP25

# CELL5

# TP26

# CELL6

# TP27

# CELL7

# TP28

# CELL8

# TP36

# CELL16S

# TP35

# CELL15

# TP34

# CELL14

# TP33

# CELL13

# TP32

# CELL12

# TP31

# CELL11

# TP30

# CELL10

# TP29

# CELL9

# TP37

# PWR

# TP20

# CELL0S

# CELL16

# CELL0 CELL0

# 75V

# D4 DNP

# J14

# J16

# CELL0

# CELL0

# CELL16

# CELL16S

# CELL15

# CELL14

# CELL13

# CELL12

# CELL11

# CELL10

# CELL9

# CELL8

# CELL7

# CELL6

# CELL5

# CELL4

# CELL3

# CELL2

# CELL1

# CELL0S

# CELL0

# CELL16

# CELL0

# CELL5

# VC0

# R122

# DNP CELL14

# VSTACK

# CELL16S

# PWR

# Figure 9-3. BQ79656EVM Schematic Part 2

# BQ79656EVM Schematic, Assembly, Layout, and BOM <https://www.ti.com>

# BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules SLUUC37D - JULY 2019 - REVISED JUNE 2025

# Submit Document Feedback

# CELL5 CELL4 CELL3 CELL2 CELL1

# R48

# R47

# R46

# R45

# R44

# R43

# CELL6

# CELL0

# C4\_L C3\_L C2\_L C1\_L

# C6\_R C5\_R C4\_R C3\_R C2\_R C1\_R

# R49 CELL0

# GND

# S2

# C5\_L C6\_L

# R42

# R37

# C7\_L C8\_L

# CELL7 CELL8 C7\_R C8\_R

# R35

# R34

# R33

# R36

# R30

# R29

# R32

# R31

# S1

# C16\_R C15\_R C14\_R C13\_R C12\_R C11\_R

# C14\_L C13\_L C12\_L C11\_L

# C15\_L C16\_L

# C10\_L C9\_L

# C10\_R C9\_R CELL9 CELL10

# CELL15 CELL14 CELL13 CELL12 CELL11

# CELL16S

# J8

# J7

# GND

# C5\_R C4\_R C3\_R C2\_R C1\_R C7\_R C8\_R

# C11\_R C10\_R C9\_R

# J9

# C16\_R C15\_R C14\_R C13\_R C6\_R C12\_R

# CELL1 CELL2 CELL3 CELL4 CELL5 CELL6 CELL7 CELL8

# CELL9

CELL10 CELL11 CELL12 CELL13 CELL14 CELL15 CELL16S

# CELL0

# TP38

# GND

# TP39

# CELL0

# R40

# BBN\_CELL

# BBP\_CELL

# 0.1 R39

# R38

# DNP

# R41

# DNP

# TP40

# VSTACK

# VSTACK

# Figure 9-4. BQ79656EVM Schematic Part 3

# 24V

# D5

# COMHN

# COMHP

# J11

# ISO\_COMMH\_N ISO\_COMMH\_P

# J10

# COMML\_P

# COMML\_N

# GND

# GND

# ISO\_COMML\_N ISO\_COMML\_P

# 24V

# D2

# GND

# ISO\_COMML\_P

# ISO\_COMML\_N

# GND

# ISO\_COMMH\_P

| 100pF | C13 |
|:--- |:--- |
| 220pF | C15 |
| 220pF | C16 |
| 220pF | C17 |
| 220pF | C18 |
| 100pF | C14 | 220pF C15 220pF C16 220pF C17 220pF C18 100pF C14 2200pF

# C20 2200pF

# C21 470uH

# L2 2200pF

# C22 2200pF

# C19 470uH

# L1

# COMML\_P\_OPT

# COMML\_P\_OPT

# COMML\_N\_OPT

# COMML\_N\_OPT

# ISO\_COMML\_P

# ISO\_COMML\_N COMMH\_N\_OPT

# COMMH\_P\_OPT ISO\_COMMH\_P

# ISO\_COMMH\_N

# R53

# R57

# R52

# R56

# R70

# R76

# R71

# R77

# R79

# R69

# R73

# R75

# R78

# R74

# R72

# R68

# R54

# R50

# R51

# R55

# TP41

# GND

# R60

# R66

# R59

# R65

# R58

# R64

# R61

# R67

# COMML\_N\_OPT

# COMML\_P\_OPT

# COMMH\_P\_OPT

# COMMH\_P\_OPT

# COMMH\_N\_OPT

# COMMH\_N\_OPT

# COMMH\_P

# COMMH\_N

# ISO\_COMMH\_N

# COMLN

# COMLP

# GND

# GND

# J13

# J12

| R115 | DNP |
|:--- |:--- |
| R117 | DNP |
| R116 | DNP |

# R117 DNP

# R116 DNP

# R118 DNP 10nF

# C62

# DNP 10nF

# C61

# DNP 1.00k R62

# GND 1.00k R63

# J19

# J20

# GND COMMH\_N COMMH\_P

# GND COMML\_N COMML\_P

# T1

# HMU1228NL

# DNP

# T2

# HMU1228NL

# DNP

# Figure 9-5. BQ79656EVM Schematic Part 4

# www.ti.com

*BQ79656EVM Schematic, Assembly, Layout, and BOM*

# SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

# BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules

## 9.2 Assembly

Components marked 'DNP' must not be populated.

## Figure 9-6. BQ79656EVM Assembly Top

*BQ79656EVM Schematic, Assembly, Layout, and BOM* <https://www.ti.com>

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules* SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

Components marked 'DNP' must not be populated.

## Figure 9-7. BQ79656EVM Assembly Bottom

## 9.3 Layout

## See section 7.3 for same drawings as for BQ79616.

<https://www.ti.com> *BQ79656EVM Schematic, Assembly, Layout, and BOM*

SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules*

## 9.4 BQ79656EVM Bill of Materials (BOM)

## Table 9-1. BQ79656EVM BOM

**Designator** **Qty** **Value** **Description** **Package ** **Reference** **Part Number** **Manufacturer** **Alternate Part ** **Number** (1) **Alternate ** **Manufacturer**!PCB1 Printed Circuit Board BMS021 Any

# C1

Multilayer Ceramic Capacitors MLCC - SMD/SMT 1206 0.22uF 100volts  X7R +/-10% GCM31MR72A224 KA37L Murata

# C2, C6, C8, C9

CAP CER 0603 1UF 10 V X7R 10% 0603 (1608 Metric) C0603C105K8RA CAUTO KEMET

# C3, C4, C57, C58,

C59 0.1uF CAP, CERM, 0.1 uF, 10 V, +/- 10%, X7R, AEC-Q200 Grade 1, 0402 GCM155R71A104 KA55D MuRata

# C5

0.01uF CAP, CERM, 0.01 µF, 100 V,+/- 10%, X7R, AEC-Q200 Grade 1, 0603 GCM188R72A103 KA37J MuRata

# C7

4.7uF CAP, CERM, 4.7 uF, 10 V, +/- 20%, X7R, 0805 C2012X7R1A475 M125AC TDK

# C10, C11, C23,

C24, C25, C26, C27, C28, C29, C30, C31, C32, C33, C34, C35, C36, C37, C38, C39, C40, C41, C42, C43, C44, C45, C46, C47, C48, C49, C50, C51, C52, C53, C54, C55, C56

# 0.47uF

CAP, CERM, 0.47 uF, 16 V, +/- 10%, X7R, AEC-Q200 Grade 1, 0603 GCM188R71C474 KA55D MuRata

# C12, C60

1uF CAP, CERM, 1 uF, 16 V, +/- 10%, X7R, AEC-Q200 Grade 1, 0603 GCM188R71C105 KA64D MuRata

# C13, C14

100 pF CAP, CERM, 100 pF, 50 V,+/- 5%, C0G/NP0, AEC-Q200 Grade 1, 0603 GCM1885C1H101 JA16J MuRata

# C15, C16, C17,

C18 220 pF CAP, CERM, 220 pF, 50 V,+/- 5%, X7R, 0603 CL10B221JB8NN NC Samsung ElectroMechanics

C19, C20, C21, C22 2200 pF CAP, CERM, 2200 pF, 2000 V,+/- 10%, X7R, AEC-Q200 Grade 1, 1206 1206 1206J2K00222KX R Knowles Capacitors

D1 Green LED, Green, SMD LED\_0805 LTST-C170KGKT Lite-On

D2, D3, D5 24 V Diode, TVS, Bi, 24 V, 70 Vc, AECQ101, SOT-23 SOT-23 PESD1CAN,215 NXP Semiconductor ESD562-Q1 Texas Instruments

FID1, FID2, FID3, FID4, FID5, FID6 Fiducial mark. There is nothing to buy or mount. N/A N/A N/A

H1, H2, H3, H4 Machine Screw, Round, #4-40 x 1/4, Nylon, Philips panhead Screw NY PMS 440 0025 PH

| B&F Fastener | Supply |
|:--- |:--- |
| BQ79656EVM Schematic, Assembly, Layout, and BOM | www.ti.com |
| BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules | SLUUC37D - JULY 2019 - REVISED JUNE 2025 |

*BQ79656EVM Schematic, Assembly, Layout, and BOM* <https://www.ti.com>

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules* SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

## Table 9-1. BQ79656EVM BOM (continued)

**Designator** **Qty** **Value** **Description** **Package ** **Reference** **Part Number** **Manufacturer** **Alternate Part ** **Number** (1) **Alternate ** **Manufacturer**

| H5, H6, H7, H8 | Standoff, Hex, 0.5"L #4-40 Nylon | Standoff | 1902C | Keystone |
|:--- |:--- |:--- |:--- |:--- |
| H9 | CONN HOUSING 22POS.100 W / | LATCH | 50-57-9422 | Molex |
| H11, H12 | Rectangular Housing Connector, 4 | Pos, 2.54mm | 50-57-9404 | Molex |

# H9

CONN HOUSING 22POS.100 W / LATCH 50-57-9422 Molex

H11, H12 Rectangular Housing Connector, 4 Pos, 2.54mm 50-57-9404 Molex

J1, J2, J5, J6, J18, J21 Header, 2.54mm, 1x2, Tin, Black, TH Header, 2.54mm, 2x1, TH PEC01DAAN Sullins Connector Solutions

J3 Header, 0.5mm, 6x1, R/A, Gold, TH Header, 0.5mm, 6x1, R/A, TH 22-12-4062 Molex J4 Header, 2.54 mm, 8x2, Tin, Vertical, TH

Header, 2.54 mm, 8x2, TH PEC08DAAN Sullins Connector Solutions J7, J8, J9 Header, 100mil, 6x1, Tin, TH

| TH, 6-Leads, Body | 608x100mil, Pitch | 100mil |
|:--- |:--- |:--- |
| PEC06SAAN | Sullins Connector | Solutions |
| J10, J11 | Header(shrouded), 2.54mm, 4x1, | R/A, Gold, TH |
| Header(shrouded), | 2.54mm, 4x1, R/A, | TH | PEC06SAAN Sullins Connector Solutions

J10, J11 Header(shrouded), 2.54mm, 4x1, R/A, Gold, TH Header(shrouded), 2.54mm, 4x1, R/A, TH 70551-0038 Molex

J12, J13, J14, J16 Header, 100mil, 2x1, Tin, TH Header, 2 PIN, 100mil, Tin PEC02SAAN Sullins Connector Solutions

# J15

Connector Header Through Hole, Right Angle 22 position 0.100" (2.54mm) HDR22 Molex

# J17

CONN HEADER 10POS.100 DL R/A AU HDR10 TSW-105-08-L-DRA Samtec

J19, J20 Header, 100mil, 3x1, Tin, TH Header, 3 PIN, 100mil, Tin PEC03SAAN Sullins Connector Solutions

L1, L2 470uH Coupled inductor, 470 uH, 0.4 A, 0.35 ohm, SMD 5x3.3mm Wurth Elektronik

LBL1 Thermal Transfer Printable Labels, 0.650" W x 0.200" H - 10,000 per roll

PCB Label 0.650 x 0.200 inch THT-14-423-10 Brady

Q1 150 V Transistor, NPN, 150 V, 1 A, AECQ101, DPAK DPAK ZXTN4004KTC Diodes Inc.

R2, R120, R123 100k RES, 100 k, 5%, 0.1 W, AEC-Q200 Grade 0, 0603 CRCW0603100KJ NEA Vishay-Dale

| R3 | RES, 100, 1%, 0.75 W, AEC-Q200 | Grade 0, 2010 | CRCW2010100RF | KEF | Vishay-Dale |
|:--- |:--- |:--- |:--- |:--- |:--- |
| R4 | RES, 200, 1%, 0.75 W, AEC-Q200 | Grade 0, 2010 | CRCW2010200RF | KEF | Vishay-Dale |
| R5 | 30.0 | RES, 30.0, 1%, 0.1 W, AEC-Q200 | Grade 0, 0603 | ERJ-3EKF30R0V | Panasonic |

R4 RES, 200, 1%, 0.75 W, AEC-Q200 Grade 0, 2010 CRCW2010200RF KEF Vishay-Dale

R5 30.0 RES, 30.0, 1%, 0.1 W, AEC-Q200 Grade 0, 0603 ERJ-3EKF30R0V Panasonic

<https://www.ti.com> *BQ79656EVM Schematic, Assembly, Layout, and BOM*

SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules*

## Table 9-1. BQ79656EVM BOM (continued)

**Designator** **Qty** **Value** **Description** **Package ** **Reference** **Part Number** **Manufacturer** **Alternate Part ** **Number** (1) **Alternate ** **Manufacturer**

# R7, R8, R11, R14, R15, R16, R18, R19

| 10.0k | RES, 10.0 k, 1%, 0.1 W, AEC-Q200 | Grade 0, 0603 | CRCW060310K0F | KEA | Vishay-Dale |
|:--- |:--- |:--- |:--- |:--- |:--- |
| R9, R12 | RES, 402, 1%, 0.1 W, AEC-Q200 | Grade 0, 0603 | CRCW0603402RF | KEA | Vishay-Dale |
| R29, R30, R31, | R32, R33, R34, | R35, R36, R37, | R42, R43, R44, | R45, R46, R47, | R48 |

R9, R12 RES, 402, 1%, 0.1 W, AEC-Q200 Grade 0, 0603 CRCW0603402RF KEA Vishay-Dale

# R29, R30, R31,

R32, R33, R34, R35, R36, R37, R42, R43, R44, R45, R46, R47, R48

RES, 100, 1%, 1 W, AEC-Q200 Grade 0, 2512 CRCW2512100RF KEG Vishay-Dale

# R39

0.1 RES, 0.1, 5%, 0.1 W, 0603 CRL0603-JWR100ELF Bourns

R40, R49 RES, 0, 5%, 0.25 W, AEC-Q200 Grade 0, 1206 ERJ-8GEY0R00V Panasonic

# R50, R51, R52,

R53, R54, R55, R56, R57, R68, R69, R70, R71, R72, R73, R74, R75, R76, R77, R78, R79

RES, 0, 5%, 0.333 W, AEC-Q200 Grade 0, 0805 CRCW08050000Z 0EAHP Vishay-Dale

# R58, R61, R64,

R67 RES, 0, 5%, 0.1 W, 0603 RC0603JR-070RL Yageo

R59, R60, R65, R66 RES, 51, 5%, 0.1 W, AEC-Q200 Grade 0, 0603 CRCW060351R0J NEA Vishay-Dale

R62, R63 1.00k RES, 1.00 k, 1%, 0.1 W, 0603 ERJ-3EKF1001V Panasonic

# R80, R81, R84,

R85, R89, R90, R93, R94, R97, R98, R101, R102, R105, R106, R109, R110, R113

RES, 100, 0.1%, 0.1 W, AEC-Q200 Grade 0, 0603 ERA-3AEB101V Panasonic

# R82, R83, R86,

R87, R91, R92, R95, R96, R99, R100, R103, R104, R107, R108, R111, R112, R114

10.0 RES, 10.0, 1%, 0.75 W, AEC-Q200 Grade 0, 1210 CRCW121010R0F KEAHP Vishay-Dale

R88 RES, 0, 5%, 0.1 W, AEC-Q200 Grade 0, 0603 CRCW06030000Z 0EA Vishay-Dale

*BQ79656EVM Schematic, Assembly, Layout, and BOM* <https://www.ti.com>

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules* SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

## Table 9-1. BQ79656EVM BOM (continued)

**Designator** **Qty** **Value** **Description** **Package ** **Reference** **Part Number** **Manufacturer** **Alternate Part ** **Number** (1) **Alternate ** **Manufacturer**

# R119

RES, 100, 5%, 0.25 W, AEC-Q200 Grade 0, 0603 ESR03EZPJ101 Rohm

R121, R128 1.0k RES, 1.0 k, 5%, 0.1 W, AEC-Q200 Grade 0, 0603 CRCW06031K00J NEA Vishay-Dale

# RT1, RT2, RT3, RT4, RT5, RT6, RT7, RT8

10k Thermistor NTC, 10k ohm, 2%, 0603 ERT-J1VG103GA Panasonic

S1, S2 Switch, SPST 8Pos, Rocker, TH 9.65X8X22.4mm 76SB08ST Grayhill

# SH1, SH2, SH3, SH4, SH5, SH6, SH7, SH8

Shunt, 100mil, Gold plated, Black Shunt 2 pos. 100 mil 881545-2 TE Connectivity

# TP1, TP2, TP3,

TP4, TP5, TP6, TP7, TP8, TP9, TP10, TP11, TP12, TP16, TP17, TP18, TP19, TP21, TP22, TP23, TP24, TP25, TP26, TP27, TP28, TP29, TP30, TP31, TP32, TP33, TP34, TP35, TP36, TP42, TP43, TP44 Test Point, Multipurpose, White, TH White Multipurpose Testpoint Keystone

| TP13, TP14, TP15 | Terminal, Turret, TH, Triple | Keystone1598-2 | 1598-2 | Keystone |
|:--- |:--- |:--- |:--- |:--- |
| TP20, TP38, TP39 | Test Point, Multipurpose, Black, TH | Black Multipurpose | Testpoint | Keystone |
| TP37, TP40 | Test Point, Multipurpose, Red, TH | Red Multipurpose | Testpoint | Keystone |

TP20, TP38, TP39 Test Point, Multipurpose, Black, TH Black Multipurpose Testpoint Keystone

TP37, TP40 Test Point, Multipurpose, Red, TH Red Multipurpose Testpoint Keystone

# U1

14S or 16S Standalone Precision Automotive Battery Monitor, Balancer and Integrated Current Sense with up to SafeTITM-26262 ASIL-D ASIL-D Compliance HTQPF64 BQ79656PAPQ1 Texas Instruments

# U2

Automotive, Low-power, QuadChannel 2/2 Digital Isolator, DW0016B (SOIC-16)

DW0016B ISO7342CQDWR Q1 Texas Instruments ISO7342CQDWQ1 Texas Instruments

# C61, C62

0.01uF CAP, CERM, 0.01 uF, 50 V, +/- 10%, X7R, 0603 CL10B103KB8NC NC

| Samsung Electro- | Mechanics |
|:--- |:--- |
| www.ti.com | BQ79656EVM Schematic, Assembly, Layout, and BOM |
| SLUUC37D - JULY 2019 - REVISED JUNE 2025 | Submit Document Feedback |

<https://www.ti.com> *BQ79656EVM Schematic, Assembly, Layout, and BOM*

SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules*

## Table 9-1. BQ79656EVM BOM (continued)

**Designator** **Qty** **Value** **Description** **Package ** **Reference** **Part Number** **Manufacturer** **Alternate Part ** **Number** (1) **Alternate ** **Manufacturer**

D4 75 V Diode, TVS, Uni, 75 V, 121 Vc, 400 W, 3.3 A, SMA SMA SMAJ75A Littelfuse

Q2 80 V Transistor, NPN, 80 V, 1 A, AECQ101, SOT-223 SOT-223 BCP56T1G ON Semiconductor

R10, R13, R17, R122 RES, 0, 5%, 0.25 W, AEC-Q200 Grade 0, 1206 ERJ-8GEY0R00V Panasonic

R20 100k RES, 100 k, 5%, 0.1 W, AEC-Q200 Grade 0, 0603 CRCW0603100KJ NEA Vishay-Dale

# R21, R22, R23, R24, R25, R26, R27, R28, R38, R41

RES, 0, 5%, 0.1 W, AEC-Q200 Grade 0, 0603 CRCW06030000Z 0EA Vishay-Dale

# R115, R116, R117,

R118 RES, 499, 1%, 0.1 W, 0603 RC0603FR-07499 RL Yageo

# T1, T2 BMS TRANSFORMER

# SMT\_TRANSFOR MER\_8MM89\_10 MM09

| HMU1228NL | Pulse |
|:--- |:--- |
| (1) | Unless otherwise noted in the Alternate PartNumber and/or Alternate Manufacturer columns, all parts can be substituted with equivalents. |
| BQ79656EVM Schematic, Assembly, Layout, and BOM | www.ti.com |
| BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules | SLUUC37D - JULY 2019 - REVISED JUNE 2025 |

(1) Unless otherwise noted in the Alternate PartNumber and/or Alternate Manufacturer columns, all parts can be substituted with equivalents.

*BQ79656EVM Schematic, Assembly, Layout, and BOM* <https://www.ti.com>

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules* SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

**10 Revision History** NOTE: Page numbers for previous revisions may differ from page numbers in the current version.

**Changes from Revision C (August 2023) to Revision D (June 2025)** **Page** - • Added ESD562-Q1 as an alternate ESD diode................................................................................................ 32 - • Added ESD562-Q1 as an alternate ESD diode................................................................................................ 43 - • Added ESD562-Q1 as an alternate ESD diode................................................................................................ 54

**Changes from Revision B (October 2020) to Revision C (August 2023)** **Page** - • Changed all instances of legacy terminology to controller and peripheral where SPI is mentioned.................. 1 - • Added information about the shunt configurations............................................................................................. 9

**Changes from Revision A (October 2019) to Revision B (October 2020)** **Page** - • Updated the numbering format for tables, figures, and cross-references throughout the document................. 2 - • Added BQ79656EVM Schematic, Assembly, Layout, and BOM...................................................................... 53

**Changes from Revision \* (July 2019) to Revision A (October 2019)** **Page** - • Changed instances of BQ79606/BQ79606-Q1 to BQ79606A/BQ79606A-Q1................................................... 2 - • Corrected EVM device typographical errors in the General Description and Host Interface sections................ 4 - • Added Section 3................................................................................................................................................ 7 - • Added cross reference to additional wiring instructions for J15......................................................................... 9 - • Changed contents of the *Name* column in the *Pin Description* table................................................................. 9 - • Added Section 8.............................................................................................................................................. 37 <https://www.ti.com> *Revision History*

SLUUC37D - JULY 2019 - REVISED JUNE 2025 *Submit Document Feedback*

*BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules*

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

Mailing Address: Texas Instruments, Post Office Box 655303, Dallas, Texas 75265

Copyright © 2025, Texas Instruments Incorporated