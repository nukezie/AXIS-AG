# PCB Design Specifications - BLE Swiss Army Knife

## System Architecture Overview

The PCB design consists of four main boards interconnected through high-speed connectors:

1. **Main Processing Board** (8-layer)
2. **RF Frontend Board** (6-layer)
3. **Power Management Board** (4-layer)
4. **User Interface Board** (4-layer)

## Main Processing Board (8-Layer)

### Layer Stackup
```
Layer 1: Signal (Top) - High-speed signals, RF traces
Layer 2: Ground Plane
Layer 3: Signal - Digital signals, control lines
Layer 4: Power Plane - 3.3V, 1.8V, 1.2V
Layer 5: Ground Plane
Layer 6: Signal - Memory interface, USB, Ethernet
Layer 7: Ground Plane
Layer 8: Signal (Bottom) - Low-speed signals, test points
```

### Key Components
- **STM32H743VIT6**: ARM Cortex-M7 microcontroller
- **Memory**: 512MB SPI NOR Flash, 2GB LPDDR3 SDRAM, 32GB eMMC
- **Connectivity**: USB 3.0, Ethernet PHY, WiFi/Bluetooth module
- **Security**: Hardware security module, crypto authentication

### Critical Design Considerations
- **High-Speed Design**: DDR3 interface with length matching
- **RF Shielding**: Ground planes and shielding for RF immunity
- **Thermal Management**: Thermal vias and heat sinks
- **EMI/EMC**: Proper grounding and filtering

### PCB Specifications
- **Size**: 120mm x 80mm
- **Thickness**: 1.6mm
- **Material**: FR4, Tg 170°C
- **Copper Weight**: 1oz (outer), 0.5oz (inner)
- **Minimum Trace Width**: 0.1mm (signal), 0.2mm (power)
- **Minimum Via Size**: 0.2mm drill, 0.4mm pad

## RF Frontend Board (6-Layer)

### Layer Stackup
```
Layer 1: RF Signals (Top) - RF traces, antennas
Layer 2: Ground Plane
Layer 3: Signal - Control signals, SPI, I2C
Layer 4: Power Plane - RF power supplies
Layer 5: Ground Plane
Layer 6: RF Ground (Bottom) - RF ground plane
```

### RF Components Layout
```
┌─────────────────────────────────────────────────────────────┐
│                    Antenna Array                            │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐          │
│  │ 2.4GHz  │ │  5GHz   │ │ Sub-1GHz│ │ MICS    │          │
│  │ Antenna │ │ Antenna │ │ Antenna │ │ Antenna │          │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘          │
├─────────────────────────────────────────────────────────────┤
│                    RF Transceivers                          │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐          │
│  │ CC2652  │ │ CC1312  │ │ CC1101  │ │ CC1101  │          │
│  │ BLE/WiFi│ │ Sub-1GHz│ │ MICS    │ │ WMTS    │          │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘          │
├─────────────────────────────────────────────────────────────┤
│                    RF Switches & Filters                    │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐          │
│  │ RF Sw   │ │ BPF     │ │ LPF     │ │ PA/LNA  │          │
│  │ Array   │ │ Array   │ │ Array   │ │ Array   │          │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘          │
└─────────────────────────────────────────────────────────────┘
```

### RF Design Specifications
- **Impedance Control**: 50Ω for RF traces, 100Ω differential
- **RF Trace Width**: Calculated for 50Ω impedance
- **Ground Plane**: Continuous ground plane under RF traces
- **Via Fencing**: Ground vias around RF traces
- **Component Placement**: Optimized for RF performance

### Multi-Band Support
- **2.4GHz Band**: 2400-2483.5MHz (BLE, WiFi, Zigbee)
- **5GHz Band**: 5150-5850MHz (WiFi, 802.11ac/ax)
- **Sub-1GHz Bands**: 433MHz, 868MHz, 915MHz
- **MICS Band**: 402-405MHz (Medical Implant Communications)
- **WMTS Band**: 608-614MHz (Wireless Medical Telemetry)

## Power Management Board (4-Layer)

### Layer Stackup
```
Layer 1: Power Distribution (Top) - Power traces, components
Layer 2: Ground Plane
Layer 3: Power Plane - Multiple voltage rails
Layer 4: Ground Plane (Bottom) - Ground connections
```

### Power Architecture
```
Input Power (12.6V) → Power Management IC → Multiple Rails
     ↓
┌─────────────┬─────────────┬─────────────┬─────────────┐
│   3.3V      │    1.8V     │    1.2V     │    RF Power │
│ Digital     │ Memory      │ Core        │ ±5V, ±3.3V  │
└─────────────┴─────────────┴─────────────┴─────────────┘
```

### Power Components
- **TPS65217CRSLR**: Main power management IC
- **TPS63070DRCR**: Buck-boost converters
- **TPS7A4700RGWT**: Low-noise LDO regulators
- **BQ25895RTWR**: Battery charger
- **Power MOSFETs**: IRLML6244TRPBF for switching

### Power Specifications
- **Input Voltage**: 12.6V (battery), 19V (external)
- **Output Rails**: 3.3V, 1.8V, 1.2V, ±5V, ±3.3V
- **Current Capacity**: 5A total, 2A per rail
- **Efficiency**: >90% at full load
- **Noise**: <1mV RMS ripple

## User Interface Board (4-Layer)

### Layer Stackup
```
Layer 1: UI Components (Top) - Display, buttons, connectors
Layer 2: Ground Plane
Layer 3: Signal - Control signals, audio
Layer 4: Ground Plane (Bottom) - Ground connections
```

### UI Components Layout
```
┌─────────────────────────────────────────────────────────────┐
│                    7" Touchscreen Display                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                                                   │   │
│  │             1280x720 Resolution                   │   │
│  │              Capacitive Touch                     │   │
│  │                                                   │   │
│  └─────────────────────────────────────────────────────┘   │
├─────────────────────────────────────────────────────────────┤
│                    Control Panel                           │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐         │
│  │ BTN1│ │ BTN2│ │ BTN3│ │ BTN4│ │ BTN5│ │ BTN6│         │
│  └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘         │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐         │
│  │  Encoder 1  │ │  Encoder 2  │ │ Emergency   │         │
│  │             │ │             │ │   Stop      │         │
│  └─────────────┘ └─────────────┘ └─────────────┘         │
└─────────────────────────────────────────────────────────────┘
```

### Audio System
- **WM8731CLSEFL**: Audio codec
- **Speakers**: 2x custom speakers
- **Microphone**: Built-in microphone
- **Audio Interface**: 3.5mm headphone jack

## Interconnect Design

### Board-to-Board Connectors
```
Main Board ↔ RF Frontend Board: High-speed connector (40-pin)
Main Board ↔ Power Board: Power connector (8-pin)
Main Board ↔ UI Board: Display connector (30-pin)
```

### Connector Specifications
- **High-Speed**: Samtec QSE/QTE series
- **Power**: Molex Mini-Fit Jr.
- **Display**: FFC/FPC connector
- **RF**: SMA connectors for external antennas

## RF Design Guidelines

### Transmission Line Design
```c
// Microstrip line impedance calculation
Z0 = (87 / sqrt(εr + 1.41)) * ln(5.98 * h / (0.8 * w + t))

Where:
Z0 = Characteristic impedance (50Ω)
εr = Relative permittivity of substrate
h = Substrate thickness
w = Trace width
t = Trace thickness
```

### RF Component Placement
- **Antennas**: Corner placement for maximum radiation
- **RF ICs**: Close to antennas, minimal trace length
- **Filters**: Between RF ICs and antennas
- **Amplifiers**: After filters, before antennas

### Ground Plane Design
- **RF Ground**: Continuous ground plane under RF traces
- **Ground Vias**: Placed every λ/10 along RF traces
- **Ground Isolation**: Separate RF and digital grounds
- **Ground Connection**: Single point connection between grounds

## Thermal Management

### Heat Dissipation Analysis
```
Component Power Dissipation:
- STM32H743: 2W @ 480MHz
- RF Transceivers: 1.5W total
- Power Amplifiers: 3W total
- Display: 1W
- Total: ~7.5W
```

### Thermal Design
- **Heat Sinks**: Aluminum heat sinks on high-power components
- **Thermal Vias**: Array of thermal vias under hot components
- **Air Flow**: Ventilation holes in enclosure
- **Thermal Monitoring**: Temperature sensors for protection

## EMI/EMC Design

### Shielding Strategy
- **RF Shielding**: Metal cans over RF components
- **Board Shielding**: Ground plane isolation
- **Cable Shielding**: Shielded cables for external connections
- **Enclosure Shielding**: RF-shielded enclosure

### Filtering
- **Power Filtering**: LC filters on power rails
- **Signal Filtering**: RC filters on control signals
- **RF Filtering**: Bandpass and low-pass filters
- **EMI Filtering**: Ferrite beads on I/O lines

## Manufacturing Considerations

### Design for Manufacturing (DFM)
- **Component Placement**: Automated assembly friendly
- **Test Points**: Accessible test points for debugging
- **Fiducials**: Alignment marks for pick-and-place
- **Panelization**: Efficient board layout for production

### Quality Control
- **Impedance Testing**: RF trace impedance verification
- **Continuity Testing**: Open/short circuit testing
- **Functional Testing**: Full system functionality test
- **Environmental Testing**: Temperature, humidity, vibration

## Design Tools and Standards

### CAD Software
- **Schematic Capture**: KiCad or Altium Designer
- **PCB Layout**: KiCad or Altium Designer
- **3D Modeling**: FreeCAD or SolidWorks
- **Simulation**: ADS for RF simulation

### Design Standards
- **IPC Standards**: IPC-2221, IPC-7351
- **RF Standards**: IEEE 802.11, Bluetooth SIG
- **Safety Standards**: UL, CE, FCC
- **Military Standards**: MIL-STD-810, MIL-STD-461

## Cost Optimization

### Component Selection
- **Standard Components**: Use standard package sizes
- **Volume Pricing**: Optimize for volume production
- **Alternative Sources**: Multiple suppliers for critical components
- **Lifecycle Management**: Long-term availability consideration

### PCB Optimization
- **Layer Count**: Minimize layer count where possible
- **Board Size**: Optimize board size for panel utilization
- **Via Count**: Minimize via count for cost reduction
- **Material Selection**: Standard FR4 material

## Testing and Validation

### Electrical Testing
- **Continuity Test**: Verify all connections
- **Power Test**: Verify all power rails
- **Signal Test**: Verify high-speed signals
- **RF Test**: Verify RF performance

### Environmental Testing
- **Temperature Test**: -40°C to +85°C
- **Humidity Test**: 95% RH non-condensing
- **Vibration Test**: 20-2000Hz, 10g
- **Shock Test**: 50g, 11ms half-sine

### RF Performance Testing
- **Frequency Response**: Verify frequency coverage
- **Power Output**: Verify transmit power levels
- **Sensitivity**: Verify receive sensitivity
- **Spurious Emissions**: Verify compliance with regulations

This comprehensive PCB design specification ensures a robust, high-performance, and manufacturable design for the BLE Swiss Army Knife tool.