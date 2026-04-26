# Module Boundary: bms-monitor-module

> **System:** BMS High Level Design (MVP Architecture)  
> **Document Version:** 1.0  
> **Source Documents Ingested:** [BMS-design.md, bq79616-datasheet.md, BQ79616-eval-board.md]  
> **Last Updated:** 2025-05-22  

---

## 1. Identity

| Field | Value |
|:---|:---|
| **Module Name** | bms-monitor-module |
| **Role** | Performs synchronized individual cell voltage measurement, passive balancing, and local temperature sensing for a 16-cell battery stack. |
| **Domain / Zone** | High-Voltage (HV) Domain |
| **Instantiation** | Stackable (minimum 6 modules for 400V battery pack) |
| **Primary Component(s)** | BQ79616 (16-Series Battery Monitor and Balancer IC) |

---


## 2. Port Definition & Pin Mapping

### 2.1 Domain: High-Voltage (Cell Interface)
| Port ID | Direction | Signal Type | Voltage Level | Mapped Resource | Function & Logic |
|:---|:---|:---|:---|:---|:---|
| **P1.1** | Input | Power | 0V - 80V (Max) | BAT | Main power supply input from the top of the 16-cell stack. |
| **P1.2** | Input | Analog | 0V - 5V per cell | VC0 - VC16 | Cell voltage sense inputs for 16 series cells. |
| **P1.3** | Output | Power | 0V - 5V per cell | CB0 - CB16 | Cell balancing control outputs (internal MOSFETs). |
| **P1.4** | Passive | Ground | HV- Ref | AVSS / CVSS | Local module ground reference (negative of the lowest cell). |
| **P1.5** | I/O | Analog | 0V - 5V | GPIO1 - GPIO8 | Configurable for external thermistor (NTC) temperature sensing. |
| **P1.6** | Output | Power | 5V | TSREF | Bias voltage for external NTC thermistor networks. |

### 2.2 Domain: High-Voltage (Communication Daisy Chain)
| Port ID | Direction | Signal Type | Voltage Level | Mapped Resource | Function & Logic |
|:---|:---|:---|:---|:---|:---|
| **P2.1** | I/O | Diff Signal | Isolated | COMHP, COMHN | High-side isolated differential daisy chain interface. |
| **P2.2** | I/O | Diff Signal | Isolated | COMLP, COMLN | Low-side isolated differential daisy chain interface. |

### 2.3 Domain: Module Internal/Supporting
| Port ID | Direction | Signal Type | Voltage Level | Mapped Resource | Function & Logic |
|:---|:---|:---|:---|:---|:---|
| **P3.1** | Output | Power | 5V | CVDD | Regulated 5V output; can be used to power AMC1301 "hot side". |
| **P3.2** | Output | Digital | 0V - 5V | NFAULT | Hardware fault indicator signal. |

---

## 3. Consumed Resources _(what this module needs)_

### 3.1 Power
| Rail / Supply | Voltage | Max Current | Required Quality | Provider (module or external) |
|:---|:---|:---|:---|:---|
| Cell Stack Power | 16-cell (Nom ~59V) | ~250mA (inc. balancing) | Battery Source | External (Battery Pack) |

### 3.2 Signals & Data
| Signal / Bus | Direction | Protocol / Format | Timing Constraint | Provider |
|:---|:---|:---|:---|:---|
| Wake-up Ping | Input | Wake-up tone | Initial boot | Comm Bridge / Prev Module |
| Daisy Chain Data | I/O | Isolated Diff | Up to 1 Mbps | Comm Bridge / Prev Module |

### 3.3 Clock & Synchronisation
| Clock / Trigger | Frequency / Period | Edge / Polarity | Provider |
|:---|:---|:---|:---|
| Global Cell Sample | Command-based | Differential Daisy Chain | MCU (via Comm Bridge) |

### 3.4 Physical & Environmental
| Constraint | Specification | Notes |
|:---|:---|:---|
| Connector / Interface | Daisy chain connectors | Requires isolated differential routing. |
| Thermal dissipation | Passive cooling | Balancing current (240mA) generates heat. |
| Placement / Orientation | Near cell terminals | Minimize sense lead length for accuracy. |
| Creepage / Clearance | 400V system rating | Required between isolated daisy chain ports. |
| Sensing Safety | 100mA SMD Fuses | Required at each sense tap point of contact to prevent thermal events. |
| Wiring | Low-gauge signal wires | For "Taps" connecting ADC inputs to busbar. |

### 3.5 State & Configuration
| Config Item | Type | Who sets it | When |
|:---|:---|:---|:---|
| Device Address | Register | MCU (auto-addressing) | During Initialization |
| Fault Thresholds | Register | MCU | During Initialization |

### 3.6 Unresolvable Dependencies _(system boundary surface)_
| Resource | Class | External Source | Specification |
|:---|:---|:---|:---|
| 16-Cell Battery Stack | Power/Sense | Traction Battery | High-voltage battery pack (Case 1-5). |
| Thermistors | Analog Input | NTC Sensors | External temperature sensors for cell monitoring. |

---

## 4. Produced Resources _(what this module offers)_

### 4.1 Power Outputs
| Rail | Voltage | Max Current | Load Regulation | Consumer(s) |
|:---|:---|:---|:---|:---|
| CVDD | 5V | Not specified | LDO | Current Sensing (AMC1301 hot side) |
| TSREF | 5V | Not specified | Precision Ref | External Thermistors |

### 4.2 Signals & Data Outputs
| Signal / Bus | Direction | Protocol / Format | Update Rate | Consumer(s) |
|:---|:---|:---|:---|:---|
| Cell Voltages | Output (Data) | Daisy Chain | <200us sampling | MCU |
| GPIO/Temp Data | Output (Data) | Daisy Chain | Periodic | MCU |
| Fault Status | Output (Data) | Daisy Chain / NFAULT | Continuous heartbeat | MCU / Comm Bridge |

### 4.3 Capability Outputs
| Capability | Trigger Condition | Effect on System | Consumer(s) |
|:---|:---|:---|:---|
| Passive Balancing | Software command / Config | Discharges high-voltage cells | Battery Cells |
| Local Protections | V > OVP or V < UVP | Sets internal fault flag | MCU |

### 4.4 Physical Interfaces Offered
| Interface | Type | Mating Requirement |
|:---|:---|:---|
| Isolated Daisy Chain | Capacitor or Transformer | Differential pair cabling |

---

## 4. Direct Connections

| Connected Module | Resource Exchanged | Direction | Interface Type |
|:---|:---|:---|:---|
| Battery Cells | Voltage/Balancing | Bi-directional | Multi-pin Sense Lead |
| Communication Bridge | Daisy Chain Data | Bi-directional | Isolated Differential |
| BMS Monitor Module (Stack) | Daisy Chain Data | Bi-directional | Isolated Differential |
| Current Sensing | Power (CVDD) | Output | DC Power Rail |

---

## 5. Operational Contracts

### 5.1 Initialisation Contract
- **Preconditions:** Minimum voltage present on BAT pin to power the internal LDOs.
- **Wake-up Sequence:**
    1. Receives wake-up ping from Communication Bridge or previous module.
    2. Sequentially activates the daisy chain for downstream modules.
    3. MCU assigns device address via auto-addressing.
- **Guarantees:** Responds to daisy chain auto-addressing command from host and completes self-diagnostic.

### 5.2 Steady-State Contract
- **Production:** Continuous monitoring of cell voltages with +/-1.5mV accuracy.
- **Timing:** 
    - Completes 16-cell voltage measurement in <200us.
    - Synchronizes ADC conversion with "Global Cell Sample" command from MCU.
- **Communication:** Bi-directional isolated daisy chain at up to 1 Mbps.

### 5.3 Fault Contract
- **Absence of Resource:** If BAT power is lost, module becomes unresponsive.
- **Internal Fault:** 
    - Asserts NFAULT and sets status registers if OVP/UVP/OTP limits are reached.
    - Provides fault signal and heartbeat through the communication line.

---

## 5. Isolation & Domain Boundaries

| Boundary Type | Isolation Method | Rating | Notes |
|:---|:---|:---|:---|
| High Voltage to Logic | Capacitor/Transformer | $1000V_{DC}$ (Reinforced) | Daisy chain communication isolation. |

---

## 6. Open Items

| Item | Type (Dependency / Constraint / Decision) | Status |
|:---|:---|:---|
| Exact daisy chain connector model | Constraint | Unspecified |
| Current limit for CVDD output | Constraint | Unspecified in ingested docs |
