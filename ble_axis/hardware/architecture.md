# Hardware Architecture - BLE Axis

## System Overview
The BLE Axis hardware architecture is designed for high-performance, dual-band RF analysis and manipulation across BLE (2.4GHz) and MICS (402-405MHz) frequency bands. The system is optimized for budget-conscious manufacturing while maintaining advanced capabilities for authorized DoD operations.

## System Block Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        BLE Axis System                         │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐            │
│  │   3.5" LCD  │  │   Touch     │  │   Audio     │            │
│  │   Display   │  │  Interface  │  │   System    │            │
│  └─────────────┘  └─────────────┘  └─────────────┘            │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐            │
│  │   STM32F405 │  │   Security  │  │   Power     │            │
│  │   Cortex-M4 │  │   Module    │  │ Management  │            │
│  └─────────────┘  └─────────────┘  └─────────────┘            │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐            │
│  │    BLE      │  │    MICS     │  │   RF        │            │
│  │ Transceiver │  │ Transceiver │  │ Frontend    │            │
│  │ CC2652R1    │  │  CC1101     │  │  Control    │            │
│  └─────────────┘  └─────────────┘  └─────────────┘            │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐            │
│  │   BLE       │  │   MICS      │  │   RF        │            │
│  │  Antenna    │  │   Antenna   │  │  Switches   │            │
│  └─────────────┘  └─────────────┘  └─────────────┘            │
└─────────────────────────────────────────────────────────────────┘
```

## Core Processing Unit

### Microcontroller Selection
- **Part Number**: STM32F405RGT6
- **Architecture**: ARM Cortex-M4
- **Frequency**: 168MHz
- **Flash**: 1MB
- **RAM**: 192KB
- **Package**: LQFP64
- **Cost**: $8.50

### Key Features
- **High Performance**: 168MHz with DSP instructions
- **Rich Peripherals**: Multiple UART, SPI, I2C, USB, CAN
- **Memory**: Large flash and RAM for complex applications
- **Cost Effective**: Excellent price/performance ratio
- **Ecosystem**: Extensive development tools and libraries

### Memory Architecture
```
┌─────────────────────────────────────────────────────────────┐
│                    Memory Map                               │
├─────────────────────────────────────────────────────────────┤
│ 0x08000000 - 0x080FFFFF │ 1MB Flash Memory                 │
│ 0x20000000 - 0x2002FFFF │ 192KB SRAM                       │
│ 0x40000000 - 0x4FFFFFFF │ Peripherals                      │
│ 0x60000000 - 0x6FFFFFFF │ External Memory Interface        │
└─────────────────────────────────────────────────────────────┘
```

## RF Frontend Architecture

### Dual-Band RF System
```
┌─────────────────────────────────────────────────────────────┐
│                    RF Frontend                              │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │   BLE       │  │   MICS      │  │   RF        │        │
│  │ Transceiver │  │ Transceiver │  │  Switches   │        │
│  │ CC2652R1    │  │  CC1101     │  │             │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │   BLE       │  │   MICS      │  │   Power     │        │
│  │   LNA       │  │   LNA       │  │ Amplifiers  │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │   BLE       │  │   MICS      │  │   Bandpass  │        │
│  │  Filter     │  │  Filter     │  │   Filters   │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
└─────────────────────────────────────────────────────────────┘
```

### BLE Transceiver (CC2652R1FRGZR)
- **Frequency Range**: 2.4GHz ISM Band
- **Protocols**: Bluetooth 5.2, IEEE 802.15.4, Proprietary
- **Sensitivity**: -100dBm
- **Output Power**: Up to 5dBm
- **Package**: VQFN48
- **Cost**: $8.50

### MICS Transceiver (CC1101RGPR)
- **Frequency Range**: 402-405MHz MICS Band
- **Protocols**: Custom MICS protocols
- **Sensitivity**: -110dBm
- **Output Power**: Up to 10dBm (MICS compliant)
- **Package**: QLP20
- **Cost**: $6.50

### RF Switches
- **SKY13317-378LF**: SPDT RF Switch (0.1-6GHz)
- **SKY13318-385LF**: SP4T RF Switch (0.1-6GHz)
- **Insertion Loss**: <0.5dB
- **Isolation**: >30dB
- **Switching Speed**: <50ns

### Power Amplifiers
- **BLE PA**: SKY66112-11 (2.4GHz, 20dBm)
- **MICS PA**: Custom design (402-405MHz, 25μW)
- **Efficiency**: >30%
- **Linear Operation**: Class A/B

### Low Noise Amplifiers
- **BLE LNA**: SKY67150-396LF (2.4GHz, 1.5dB NF)
- **MICS LNA**: Custom design (402-405MHz, 1.0dB NF)
- **Gain**: 15-20dB
- **Noise Figure**: <2dB

## User Interface System

### Display System
```
┌─────────────────────────────────────────────────────────────┐
│                    Display System                           │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │   3.5" TFT  │  │   ST7735S   │  │   Touch     │        │
│  │   LCD       │  │ Controller  │  │ Controller  │        │
│  │ 480x320     │  │             │  │             │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │   Audio     │  │   Speaker   │  │ Microphone  │        │
│  │   Codec     │  │             │  │             │        │
│  │  WM8731     │  │             │  │             │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
└─────────────────────────────────────────────────────────────┘
```

### Display Specifications
- **Size**: 3.5" TFT LCD
- **Resolution**: 480x320 pixels
- **Interface**: SPI with RGB565 color
- **Touch**: Capacitive touch overlay
- **Controller**: ST7735S
- **Cost**: $25.00

### Control Interface
- **6x Tactile Pushbuttons**: EVQ-PAD04K
- **1x Rotary Encoder**: PEC11R-4220F-S0024
- **1x Emergency Stop**: Custom design
- **Interface**: GPIO with debouncing

### Audio System
- **Codec**: WM8731CLSEFL
- **Speaker**: Custom 8Ω, 1W
- **Microphone**: Electret condenser
- **Interface**: I2S

## Power Management System

### Power Architecture
```
┌─────────────────────────────────────────────────────────────┐
│                    Power Management                         │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │   Battery   │  │   Charger   │  │   Power     │        │
│  │   7.4V      │  │  BQ25895    │  │ Management  │        │
│  │   5Ah       │  │             │  │    IC       │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │   Buck-     │  │   LDO       │  │   Power     │        │
│  │   Boost     │  │ Regulators  │  │ Distribution│        │
│  │ Converters  │  │             │  │             │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
└─────────────────────────────────────────────────────────────┘
```

### Power Supply Components
- **Battery**: 7.4V Li-ion, 5Ah
- **Charger**: BQ25895RTWR (USB-C charging)
- **Power Management**: TPS65217CRSLR
- **Buck-Boost**: 2x TPS63070DRCR
- **LDO Regulators**: 3x TPS7A4700RGWT

### Power Distribution
- **3.3V Digital**: Main logic supply
- **1.8V Digital**: Memory and high-speed logic
- **5V Analog**: RF frontend supply
- **3.3V RF**: RF transceivers
- **Battery Monitoring**: Voltage and current sensing

## Security System

### Security Architecture
```
┌─────────────────────────────────────────────────────────────┐
│                    Security System                          │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │   Crypto    │  │   Hardware  │  │   Secure    │        │
│  │   Auth      │  │   Security  │  │   Storage   │        │
│  │  ATECC608A  │  │   Module    │  │             │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │   Key       │  │   Certificate│  │   Audit     │        │
│  │ Management  │  │   Manager   │  │   Logger    │        │
│  │             │  │             │  │             │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
└─────────────────────────────────────────────────────────────┘
```

### Security Components
- **Crypto Authentication**: ATECC608A-MAHDA-T
- **Hardware Security Module**: Custom design
- **Secure Storage**: Encrypted flash memory
- **Key Management**: Hardware-based key storage

## Sensor System

### Environmental Sensors
- **Temperature/Humidity/Pressure**: BME280
- **Accelerometer/Gyroscope**: MPU6050
- **Interface**: I2C

### RF Monitoring Sensors
- **RF Power Detector**: ADL5511
- **Logarithmic Amplifier**: AD8318
- **Spectrum Analyzer Frontend**: Custom design

## Connectivity System

### Communication Interfaces
- **USB 3.0**: USB3300-EZK-TR PHY
- **USB-C Connector**: Reversible connector
- **WiFi/Bluetooth**: ESP32-WROOM-32 module

### Data Interfaces
- **SPI**: High-speed data transfer
- **I2C**: Sensor and peripheral communication
- **UART**: Debug and external communication
- **GPIO**: Control and status signals

## Mechanical Design

### Enclosure System
```
┌─────────────────────────────────────────────────────────────┐
│                    Enclosure Design                         │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │   Main      │  │   RF        │  │   Cooling   │        │
│  │ Enclosure   │  │ Shielded    │  │   System    │        │
│  │             │  │   Cover     │  │             │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │   Antenna   │  │   Power     │  │   Interface │        │
│  │   Mounts    │  │   Connector │  │   Panel     │        │
│  │             │  │             │  │             │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
└─────────────────────────────────────────────────────────────┘
```

### Enclosure Specifications
- **Material**: Aluminum alloy with RF shielding
- **Dimensions**: 150mm x 100mm x 30mm
- **Weight**: <500g
- **IP Rating**: IP54 (dust and splash resistant)
- **Thermal Management**: Passive cooling with heat sinks

### Antenna System
- **BLE Antenna**: Custom 2.4GHz dipole
- **MICS Antenna**: Custom 402-405MHz monopole
- **Mounting**: SMA connectors
- **Gain**: 2-3dBi (BLE), 1-2dBi (MICS)

## PCB Design

### PCB Stackup
```
┌─────────────────────────────────────────────────────────────┐
│                    PCB Architecture                         │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │   Main      │  │   RF        │  │   Power     │        │
│  │   PCB       │  │ Frontend    │  │ Management  │        │
│  │  (6-layer)  │  │  (4-layer)  │  │  (2-layer)  │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │   Digital   │  │   RF        │  │   Power     │        │
│  │   Section   │  │   Section   │  │   Section   │        │
│  │             │  │             │  │             │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
└─────────────────────────────────────────────────────────────┘
```

### Main PCB (6-layer)
- **Layer 1**: Signal routing and components
- **Layer 2**: Ground plane
- **Layer 3**: Signal routing
- **Layer 4**: Power plane
- **Layer 5**: Signal routing
- **Layer 6**: Ground plane

### RF Frontend PCB (4-layer)
- **Layer 1**: RF components and traces
- **Layer 2**: Ground plane
- **Layer 3**: Power plane
- **Layer 4**: Ground plane

### Power Management PCB (2-layer)
- **Layer 1**: Power components and routing
- **Layer 2**: Ground plane

## Thermal Management

### Thermal Design
- **Heat Sources**: RF amplifiers, microcontroller, power regulators
- **Heat Sinks**: Aluminum heat sinks on high-power components
- **Thermal Interface**: Thermal pads and grease
- **Ventilation**: Passive cooling with ventilation holes

### Temperature Monitoring
- **Sensors**: BME280 temperature sensor
- **Monitoring**: Real-time temperature tracking
- **Protection**: Thermal shutdown for critical components

## EMI/EMC Design

### EMI Shielding
- **RF Shielding**: Conductive enclosure with RF gaskets
- **Component Shielding**: Individual RF component shields
- **Grounding**: Comprehensive grounding strategy

### EMC Compliance
- **FCC Compliance**: Part 15 and Part 95 (MICS)
- **EMI Testing**: Radiated and conducted emissions
- **Immunity Testing**: ESD, EFT, surge immunity

## Manufacturing Considerations

### Assembly Process
- **SMT Assembly**: Automated pick-and-place
- **Through-hole**: Manual assembly for connectors
- **Testing**: In-circuit and functional testing
- **Programming**: Flash programming and calibration

### Quality Control
- **Component Inspection**: Visual and electrical testing
- **PCB Testing**: Continuity and isolation testing
- **Functional Testing**: Full system validation
- **Environmental Testing**: Temperature and humidity cycling

## Cost Optimization Strategies

### Component Selection
- **Standard Components**: Use off-the-shelf components where possible
- **Volume Pricing**: Leverage volume discounts
- **Alternative Sources**: Multiple supplier options
- **Simplified Design**: Reduce complexity while maintaining functionality

### Manufacturing Optimization
- **Panel Design**: Optimize PCB panel utilization
- **Assembly Efficiency**: Minimize assembly steps
- **Test Automation**: Automated testing procedures
- **Packaging**: Efficient packaging and shipping

This hardware architecture provides a comprehensive foundation for the BLE Axis tool, ensuring high performance, reliability, and security while maintaining budget constraints for authorized DoD operations.