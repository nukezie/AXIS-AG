# Enclosure Design Specifications - BLE Swiss Army Knife

## Design Overview

The enclosure design prioritizes functionality, durability, and RF performance while maintaining a professional appearance suitable for military and defense applications. The design incorporates advanced thermal management, RF shielding, and ergonomic considerations.

## Enclosure Architecture

### Main Enclosure Structure
```
┌─────────────────────────────────────────────────────────────┐
│                    Top Cover (RF Shielded)                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │             7" Touchscreen Display                  │   │
│  │             1280x720 Resolution                     │   │
│  │              Capacitive Touch Interface             │   │
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

### Side Panel Layout
```
┌─────────────────────────────────────────────────────────────┐
│                    Left Side Panel                          │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐          │
│  │ USB-C   │ │ USB-C   │ │ Ethernet│ │ Power   │          │
│  │ Port 1  │ │ Port 2  │ │ Port    │ │ Input   │          │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘          │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐          │
│  │ Audio   │ │ Debug   │ │ SIM     │ │ SD Card │          │
│  │ Jack    │ │ Port    │ │ Card    │ │ Slot    │          │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘          │
└─────────────────────────────────────────────────────────────┘
```

### Right Side Panel Layout
```
┌─────────────────────────────────────────────────────────────┐
│                    Right Side Panel                         │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐          │
│  │ 2.4GHz  │ │  5GHz   │ │ Sub-1GHz│ │ MICS    │          │
│  │ Antenna │ │ Antenna │ │ Antenna │ │ Antenna │          │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘          │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐          │
│  │ WMTS    │ │ External│ │ Cooling │ │ Status  │          │
│  │ Antenna │ │ Antenna │ │ Fan     │ │ LED     │          │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘          │
└─────────────────────────────────────────────────────────────┘
```

## Material Specifications

### Primary Materials
| Component | Material | Thickness | Properties |
|-----------|----------|-----------|------------|
| Main Body | 6061-T6 Aluminum | 3mm | High strength, RF shielding |
| Top Cover | 6061-T6 Aluminum | 2mm | RF shielding, thermal conductivity |
| Side Panels | 6061-T6 Aluminum | 2mm | RF shielding, corrosion resistance |
| Bottom Panel | 6061-T6 Aluminum | 3mm | Structural support, RF shielding |
| Display Bezel | 6061-T6 Aluminum | 1.5mm | RF shielding, aesthetic finish |

### RF Shielding Materials
| Component | Material | Thickness | Shielding Effectiveness |
|-----------|----------|-----------|------------------------|
| RF Shield | Copper | 0.1mm | >60dB @ 2.4GHz |
| Gasket Material | Conductive Silicone | 2mm | >40dB @ 2.4GHz |
| Ventilation | RF Mesh | 0.5mm | >30dB @ 2.4GHz |

### Thermal Management Materials
| Component | Material | Properties |
|-----------|----------|------------|
| Heat Sinks | 6063-T5 Aluminum | High thermal conductivity |
| Thermal Interface | Graphite Pad | Low thermal resistance |
| Cooling Fan | PBT + Glass Fiber | High temperature resistance |

## Dimensional Specifications

### Overall Dimensions
- **Length**: 200mm (7.87 inches)
- **Width**: 150mm (5.91 inches)
- **Height**: 35mm (1.38 inches)
- **Weight**: ~1.2kg (2.65 lbs)

### Internal Dimensions
- **PCB Clearance**: 5mm minimum
- **Component Height**: 25mm maximum
- **Cable Routing**: 10mm channels
- **Ventilation**: 15mm clearance

### Antenna Mounting
- **Antenna Spacing**: 50mm minimum (λ/2 at 2.4GHz)
- **Antenna Height**: 20mm maximum
- **Ground Plane**: 100mm x 100mm minimum
- **Mounting Thread**: M3 x 0.5mm

## RF Shielding Design

### Shielding Architecture
```
┌─────────────────────────────────────────────────────────────┐
│                    RF Shielded Enclosure                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              RF Shielded Top Cover                  │   │
│  │  ┌─────────────────────────────────────────────┐   │   │
│  │  │            Display Window (RF Transparent)  │   │   │
│  │  └─────────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────────┘   │
├─────────────────────────────────────────────────────────────┤
│                    RF Shielded Side Panels                 │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐          │
│  │ RF Mesh │ │ RF Mesh │ │ RF Mesh │ │ RF Mesh │          │
│  │ Vents   │ │ Vents   │ │ Vents   │ │ Vents   │          │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘          │
└─────────────────────────────────────────────────────────────┘
```

### Shielding Effectiveness
| Frequency Band | Shielding Effectiveness | Compliance |
|----------------|------------------------|------------|
| 2.4GHz (BLE/WiFi) | >60dB | FCC Part 15 |
| 5GHz (WiFi) | >55dB | FCC Part 15 |
| Sub-1GHz | >70dB | FCC Part 15 |
| MICS (402-405MHz) | >80dB | Medical Device |
| WMTS (608-614MHz) | >80dB | Medical Device |

### RF Mesh Specifications
- **Material**: Phosphor Bronze
- **Mesh Size**: 0.5mm x 0.5mm
- **Open Area**: 60%
- **Thickness**: 0.1mm
- **Shielding**: >30dB @ 2.4GHz

## Thermal Management Design

### Heat Dissipation Analysis
```
Component Heat Generation:
- STM32H743: 2W @ 480MHz
- RF Transceivers: 1.5W total
- Power Amplifiers: 3W total
- Display: 1W
- Total Heat: ~7.5W
```

### Thermal Design Features
- **Heat Sinks**: Aluminum heat sinks on high-power components
- **Thermal Vias**: PCB thermal vias for heat transfer
- **Cooling Fan**: 40mm x 40mm x 10mm, 12V, 0.1A
- **Ventilation**: RF mesh vents for airflow
- **Thermal Monitoring**: Temperature sensors for protection

### Airflow Design
```
┌─────────────────────────────────────────────────────────────┐
│                    Airflow Path                             │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐          │
│  │ Intake  │ │ Intake  │ │ Intake  │ │ Intake  │          │
│  │ Vents   │ │ Vents   │ │ Vents   │ │ Vents   │          │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘          │
│                    ↓                                       │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              Cooling Fan (40mm)                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                    ↓                                       │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐          │
│  │ Exhaust │ │ Exhaust │ │ Exhaust │ │ Exhaust │          │
│  │ Vents   │ │ Vents   │ │ Vents   │ │ Vents   │          │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘          │
└─────────────────────────────────────────────────────────────┘
```

## Mechanical Design

### Assembly Method
- **Fasteners**: M3 x 0.5mm stainless steel screws
- **Threaded Inserts**: Press-fit brass inserts
- **Gaskets**: Conductive silicone gaskets for RF sealing
- **Alignment**: Dowel pins for precise alignment

### Structural Analysis
- **Static Load**: 50kg compressive load
- **Impact Resistance**: 1.5m drop test
- **Vibration**: 20-2000Hz, 10g
- **Shock**: 50g, 11ms half-sine

### Environmental Protection
- **Ingress Protection**: IP54 (dust and splash resistant)
- **Operating Temperature**: -40°C to +85°C
- **Storage Temperature**: -55°C to +125°C
- **Humidity**: 95% RH non-condensing

## User Interface Design

### Display Integration
- **Display Type**: 7" TFT LCD with capacitive touch
- **Resolution**: 1280x720 (HD)
- **Brightness**: 400 nits (adjustable)
- **Viewing Angle**: 170° horizontal, 160° vertical
- **Touch Technology**: Projected capacitive, 10-point touch

### Control Panel Design
- **Button Type**: Tactile pushbuttons with LED backlighting
- **Button Force**: 200-400g actuation force
- **Button Life**: >1,000,000 cycles
- **Encoder Type**: Optical encoder with detents
- **Emergency Stop**: Mushroom head, red color, latching

### Audio System
- **Speakers**: 2x 1W speakers, 8Ω impedance
- **Microphone**: MEMS microphone, -38dB sensitivity
- **Audio Jack**: 3.5mm TRRS connector
- **Volume Control**: Digital volume control

## Connector and Port Design

### External Connectors
| Connector Type | Quantity | Location | Specifications |
|----------------|----------|----------|----------------|
| USB-C | 2 | Left Side | USB 3.0, 5Gbps |
| Ethernet | 1 | Left Side | RJ45, 100/1000Mbps |
| Power Input | 1 | Left Side | DC 19V, 3A |
| Audio Jack | 1 | Left Side | 3.5mm TRRS |
| Debug Port | 1 | Left Side | 10-pin header |
| SD Card | 1 | Left Side | microSD, UHS-I |
| SIM Card | 1 | Left Side | nano-SIM |

### Antenna Connectors
| Antenna Type | Quantity | Location | Specifications |
|--------------|----------|----------|----------------|
| 2.4GHz | 1 | Right Side | SMA-F, 50Ω |
| 5GHz | 1 | Right Side | SMA-F, 50Ω |
| Sub-1GHz | 1 | Right Side | SMA-F, 50Ω |
| MICS | 1 | Right Side | SMA-F, 50Ω |
| WMTS | 1 | Right Side | SMA-F, 50Ω |
| External | 1 | Right Side | SMA-F, 50Ω |

## Manufacturing Considerations

### Manufacturing Process
- **CNC Machining**: Aluminum parts precision machined
- **Sheet Metal**: RF mesh and brackets
- **Injection Molding**: Plastic components (buttons, bezels)
- **Surface Treatment**: Anodizing for corrosion resistance
- **Assembly**: Manual assembly with jigs and fixtures

### Quality Control
- **Dimensional Inspection**: CMM measurement of critical dimensions
- **RF Testing**: Shielding effectiveness verification
- **Environmental Testing**: Temperature, humidity, vibration
- **Functional Testing**: Full system integration test

### Cost Optimization
- **Material Selection**: Standard aluminum alloys
- **Manufacturing**: Optimized for CNC machining
- **Assembly**: Minimize manual operations
- **Standardization**: Use standard fasteners and components

## Safety and Compliance

### Safety Features
- **Emergency Stop**: Redundant emergency stop functionality
- **Thermal Protection**: Temperature monitoring and shutdown
- **Electrical Safety**: Double insulation, grounding
- **Mechanical Safety**: Rounded corners, no sharp edges

### Regulatory Compliance
- **FCC Part 15**: RF emissions and immunity
- **CE Marking**: European safety standards
- **UL Listing**: Safety certification
- **Military Standards**: MIL-STD-810, MIL-STD-461

### Environmental Compliance
- **RoHS**: Lead-free materials
- **REACH**: Chemical substance compliance
- **WEEE**: Waste electrical equipment directive
- **Conflict Minerals**: Conflict-free sourcing

## Maintenance and Serviceability

### Service Access
- **Top Cover**: Removable for PCB access
- **Side Panels**: Removable for connector access
- **Bottom Panel**: Removable for battery access
- **Modular Design**: Easy component replacement

### Maintenance Features
- **Filter Access**: Removable air filters
- **Battery Access**: Easy battery replacement
- **Cable Management**: Organized cable routing
- **Test Points**: Accessible test points for debugging

### Spare Parts
- **Fasteners**: Standard M3 screws and nuts
- **Gaskets**: Replaceable RF gaskets
- **Filters**: Replaceable air filters
- **Battery**: Standard battery pack

## Documentation and Labeling

### Required Labels
- **Model Number**: BLE-SAK-001
- **Serial Number**: Unique serial number
- **Power Rating**: Input voltage and current
- **Safety Warnings**: RF exposure warnings
- **Compliance Marks**: FCC, CE, UL marks

### Documentation
- **User Manual**: Operating instructions
- **Service Manual**: Maintenance procedures
- **Technical Manual**: Technical specifications
- **Safety Manual**: Safety procedures

This comprehensive enclosure design ensures a robust, RF-shielded, and user-friendly housing for the BLE Swiss Army Knife tool, meeting all military and defense requirements.