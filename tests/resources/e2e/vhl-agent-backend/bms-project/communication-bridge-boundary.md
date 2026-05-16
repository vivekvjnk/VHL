# Module Boundary: Communication Bridge

> **System:** Battery Management System (BMS)  
> **Document Version:** 1.0  
> **Source Documents Ingested:** 
> - BMS-design.md
> - bq79600-q1-datasheet.md
> - BQ79600-eval-board.md
> **Last Updated:** 2025-05-24

---

## 1. Identity

| Field | Value |
|:---|:---|
| **Module Name** | Communication Bridge |
| **Role** | Translates standard UART/SPI from the Microcontroller into the robust, isolated differential signal required by the BQ79616 high-voltage daisy chain. |
| **Domain / Zone** | Isolation Boundary (Spans Low-Voltage and High-Voltage/Daisy-Chain domains) |
| **Instantiation** | Singleton |
| **Primary Component(s)** | BQ79600-Q1 |

---

## 2. Port Definition & Pin Mapping

### 2.1 Domain: Isolated Daisy Chain Interface (Hot Side)
| Port ID | Direction | Signal Type | Voltage Level | Mapped Resource | Function & Logic |
|:---|:---|:---|:---|:---|:---|
| **P1.1** | Bi-dir | AC-I/O | Differential | COMHP / COMHN | Isolated differential daisy chain (High side connection to stack). |
| **P1.2** | Bi-dir | AC-I/O | Differential | COMLP / COMLN | Isolated differential daisy chain (Low side connection for ring). |
| **P1.3** | Output | Power | 5V | CVDD | Dedicated 5V supply for daisy chain communications. |

### 2.2 Domain: Host & Power Interface (Cold Side)
| Port ID | Direction | Signal Type | Voltage Level | Mapped Resource | Function & Logic |
|:---|:---|:---|:---|:---|:---|
| **P2.1** | Input | Power | 4.75V - 40V | BAT | Main supply input, derived from PMIC (12V rail). |
| **P2.2** | Input | Power | 1.71V - 5.5V | VIO | IO supply for UART/SPI pins, derived from PMIC (3.3V/5V rail). |
| **P2.3** | Passive | Ground | LV GND | GND | System-level digital ground reference. |
| **P2.4** | Input | Digital | 0V - VIO | SCLK | SPI clock input. |
| **P2.5** | Input | Digital | 0V - VIO | nCS | Active low chip select for SPI / UART mode select. |
| **P2.6** | Input | Digital | 0V - VIO | RX / MOSI | UART receiver input or SPI master-out-slave-in. |
| **P2.7** | Output | Digital | 0V - VIO | TX / MISO | UART transmitter output or SPI master-in-slave-out. |
| **P2.8** | Bi-dir | Digital | 0V - VIO | nUART/SPI (SPI_RDY) | Interface selection (Input) / SPI Ready (Output). |
| **P2.9** | Output | Digital | 0V - VIO | NFAULT | Fault indication output (Open-drain, active low). |
| **P2.10** | Output | High-Voltage | Up to BAT | INH | Inhibit pin to control system voltage regulators (Wakeup signal). |
| **P2.11** | Output | Power | 1.8V | DVDD | Internal 1.8V regulated output for digital logic. |

---

## 3. Consumed Resources

### 3.1 Power
| Rail / Supply | Voltage | Max Current | Required Quality | Provider (module or external) |
|:---|:---|:---|:---|:---|
| BAT Supply | 12V (nom) | TBD | Stable | Low-Voltage Power Supply Module |
| VIO Supply | 3.3V / 5V | TBD | Digital grade | Low-Voltage Power Supply Module |

### 3.2 Signals & Data
| Signal / Bus | Direction | Protocol / Format | Timing Constraint | Provider |
|:---|:---|:---|:---|:---|
| Host Comm | Input | UART / SPI | UART < 1Mbps; SPI < 12MHz | Microcontroller Module |
| Daisy Chain | Input | Isolated Diff | Synchronized | BMS Monitor Module |

### 3.3 Clock & Synchronisation
| Clock / Trigger | Frequency / Period | Edge / Polarity | Provider |
|:---|:---|:---|:---|
| SCLK | Up to 12 MHz | Rising/Falling (SPI) | Microcontroller Module |

### 3.4 Physical & Environmental
| Constraint | Specification | Notes |
|:---|:---|:---|
| Connector / Interface | TSSOP-16 | IC Package. |
| Thermal dissipation | -40°C to +125°C | Ambient operating temperature range. |
| Creepage / Clearance | 400V System level | Required for galvanic isolation boundary across transformers. |

### 3.5 State & Configuration
| Config Item | Type | Who sets it | When |
|:---|:---|:---|:---|
| Interface Mode | Hardware Pin | Hardware Design | At Boot (via nUART/SPI and nCS) |
| Fault Masking | Register | Microcontroller | Post-initialization |

### 3.6 Unresolvable Dependencies
| Resource | Class | External Source | Specification |
|:---|:---|:---|:---|
| 12V Aux Power | Power | Vehicle 12V Battery | Primary source for BAT rail in automotive applications. |

---

## 4. Produced Resources

### 4.1 Power Outputs
| Rail | Voltage | Max Current | Load Regulation | Consumer(s) |
|:---|:---|:---|:---|:---|
| DVDD | 1.8V | TBD | Internal | Internal digital circuits |
| CVDD | 5V | TBD | TBD | Isolated Communication Interface |

### 4.2 Signals & Data Outputs
| Signal / Bus | Direction | Protocol / Format | Update Rate | Consumer(s) |
|:---|:---|:---|:---|:---|
| Daisy Chain Out | Output | Isolated Diff | Synchronized | BMS Monitor Module |
| Host Response | Output | UART / SPI | Per host request | Microcontroller Module |
| NFAULT | Output | Discrete Low | Asynchronous | Microcontroller Module |

### 4.3 Capability Outputs
| Capability | Trigger Condition | Effect on System | Consumer(s) |
|:---|:---|:---|:---|
| Protocol Translation | Valid Host/Chain data | Bidirectional data flow between domains | MCU, BMS Monitor |
| System Wake-up | Wake-up ping or Fault | Powers up daisy chain and PMIC | BMS Monitor, PMIC |
| Galvanic Isolation | Hardware Design | Protects LV logic from HV stack | System-wide |

### 4.4 Physical Interfaces Offered
| Interface | Type | Mating Requirement |
|:---|:---|:---|
| Serial Connector (J4) | 10-pin Header | Samtec TSW-105-08-L-D-RA (Evaluation Mode) |
| Daisy Chain Interface | Differential | Isolated cable / Transformer coupling |

---

## 4. Direct Connections

| Connected Module | Resource Exchanged | Direction | Interface Type |
|:---|:---|:---|:---|
| Microcontroller Module | UART/SPI Data, Fault, Wakeup | Bi-directional | Digital IO / Serial |
| BMS Monitor Module | Isolated Daisy Chain Data | Bi-directional | Differential Isolated |
| Low-Voltage Power Supply | Power (12V, 3.3/5V), Enable | Input/Output | Power / Discrete |

---

## 5. Operational Contracts

### 5.1 Initialisation Contract
- **Preconditions:** VIO and BAT must be stable; VIO must be powered before IO pins are driven by the host.
- **Guarantees:** Asserts SPI_RDY (if in SPI mode) after internal reset; ready to translate host wake-up command.

### 5.2 Steady-State Contract
- **Guarantees:** Bi-directional translation of UART/SPI frames to Daisy Chain protocol.
- **Accuracy:** Bit-perfect data translation; supports robust comms in high-noise environments.

### 5.3 Fault Contract
- **Conditions:** Unmasked fault detected in daisy chain or internal IC error.
- **Action:** Asserts NFAULT active low; can trigger system-wide wake-up via INH if configured.

---

## 5. Isolation & Domain Boundaries

| Boundary Type | Isolation Method | Rating | Notes |
|:---|:---|:---|:---|
| LV to HV | Transformer / Capacitor | 400V (System) | Isolation is achieved via external coupling on COM lines. |
| Logic Board to Stack | Silicon Bridge | Reinforced | Acts as primary galvanic firewall for the logic board. |

---

## 6. Open Items

| Item | Type (Dependency / Constraint / Decision) | Status |
|:---|:---|:---|
| Host Driver implementation | Dependency | TBD |
| Specific propagation latency | Constraint | TBD |
| Maximum UART baud rate | Constraint | TBD (Typ 1Mbps) |
