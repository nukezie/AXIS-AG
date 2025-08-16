# Bill of Materials (BOM) - BLE Swiss Army Knife

## System Overview
This BOM covers all components required for the advanced multi-band RF analysis tool, including primary and backup components for redundancy and reliability.

## Main Processing Unit

### Microcontroller
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | STM32H743VIT6 | ARM Cortex-M7 480MHz, 2MB Flash, 1MB RAM | STMicroelectronics | $25.00 | $25.00 |
| 1 | STM32H743VIT6 | Backup MCU (redundancy) | STMicroelectronics | $25.00 | $25.00 |

### Memory & Storage
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | MT25QL512ABB8E12-0SIT | 512MB SPI NOR Flash | Micron | $15.00 | $15.00 |
| 1 | K4F2E3S4HM-MGCJ | 2GB LPDDR3 SDRAM | Samsung | $20.00 | $20.00 |
| 1 | SDINBDG4-32G | 32GB eMMC Storage | Western Digital | $18.00 | $18.00 |

## RF Frontend Components

### Multi-Band Transceivers
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 2 | CC2652R1FRGZR | 2.4GHz BLE/WiFi Transceiver | Texas Instruments | $8.50 | $17.00 |
| 1 | CC1312R1F3RGZR | Sub-1GHz Transceiver (433/868/915MHz) | Texas Instruments | $12.00 | $12.00 |
| 1 | CC1125RHBR | High-Performance Sub-1GHz Transceiver | Texas Instruments | $15.00 | $15.00 |
| 1 | CC1200RHBR | High-Performance Sub-1GHz Transceiver | Texas Instruments | $18.00 | $18.00 |

### MICS Band Transceiver
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | CC1101RGPR | 402-405MHz MICS Band Transceiver | Texas Instruments | $6.50 | $6.50 |
| 1 | Custom Design | MICS Band Power Amplifier | Custom | $45.00 | $45.00 |

### WMTS Band Transceiver
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | CC1101RGPR | 608-614MHz WMTS Band Transceiver | Texas Instruments | $6.50 | $6.50 |
| 1 | Custom Design | WMTS Band Power Amplifier | Custom | $45.00 | $45.00 |

### RF Switches & Filters
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 4 | SKY13317-378LF | SPDT RF Switch, 0.1-6GHz | Skyworks | $3.50 | $14.00 |
| 2 | SKY13318-385LF | SP4T RF Switch, 0.1-6GHz | Skyworks | $4.50 | $9.00 |
| 6 | Custom Design | Bandpass Filters (2.4GHz, 5GHz, 433MHz, 868MHz, 915MHz, MICS, WMTS) | Custom | $25.00 | $150.00 |
| 4 | Custom Design | Low-Pass Filters | Custom | $15.00 | $60.00 |

### Power Amplifiers
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 2 | SKY66112-11 | 2.4GHz Power Amplifier, 20dBm | Skyworks | $8.00 | $16.00 |
| 1 | SKY66113-11 | 5GHz Power Amplifier, 20dBm | Skyworks | $10.00 | $10.00 |
| 2 | Custom Design | Sub-1GHz Power Amplifier, 30dBm | Custom | $35.00 | $70.00 |

### Low Noise Amplifiers
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 2 | SKY67150-396LF | 2.4GHz LNA, 1.5dB NF | Skyworks | $6.50 | $13.00 |
| 1 | SKY67151-396LF | 5GHz LNA, 1.5dB NF | Skyworks | $7.50 | $7.50 |
| 2 | Custom Design | Sub-1GHz LNA, 1.0dB NF | Custom | $25.00 | $50.00 |

## User Interface Components

### Display
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | Custom Design | 7" Capacitive Touchscreen, 1280x720 | Custom | $85.00 | $85.00 |
| 1 | STM32F469NIH6 | Display Controller | STMicroelectronics | $18.00 | $18.00 |

### Controls
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 8 | EVQ-PAD04K | Tactile Pushbuttons | Panasonic | $2.50 | $20.00 |
| 2 | PEC11R-4220F-S0024 | Rotary Encoders | Bourns | $8.00 | $16.00 |
| 1 | Custom Design | Emergency Stop Button | Custom | $15.00 | $15.00 |

### Audio
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | WM8731CLSEFL | Audio Codec | Cirrus Logic | $5.50 | $5.50 |
| 2 | Custom Design | Speakers | Custom | $12.00 | $24.00 |
| 1 | Custom Design | Microphone | Custom | $8.00 | $8.00 |

## Power Management

### Power Supply
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | TPS65217CRSLR | Power Management IC | Texas Instruments | $12.00 | $12.00 |
| 2 | TPS63070DRCR | Buck-Boost Converter | Texas Instruments | $4.50 | $9.00 |
| 4 | TPS7A4700RGWT | Low-Noise LDO Regulator | Texas Instruments | $3.50 | $14.00 |
| 1 | Custom Design | Battery Pack, 12.6V, 10Ah | Custom | $120.00 | $120.00 |
| 1 | BQ25895RTWR | Battery Charger | Texas Instruments | $3.50 | $3.50 |

### Power Distribution
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 4 | IRLML6244TRPBF | Power MOSFET | Infineon | $1.50 | $6.00 |
| 2 | Custom Design | Power Distribution Board | Custom | $25.00 | $50.00 |

## Connectivity & Communication

### USB & Network
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | USB3300-EZK-TR | USB 3.0 PHY | Microchip | $8.00 | $8.00 |
| 1 | LAN8720AI-CP-TR | Ethernet PHY | Microchip | $4.50 | $4.50 |
| 2 | USB-C Connector | USB-C Receptacle | Various | $2.50 | $5.00 |
| 1 | RJ45 Connector | Ethernet Jack | Various | $1.50 | $1.50 |

### Wireless Connectivity
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | ESP32-WROOM-32 | WiFi/Bluetooth Module | Espressif | $8.00 | $8.00 |
| 1 | SIM7600CE | 4G LTE Module | SIMCom | $45.00 | $45.00 |

## Sensors & Monitoring

### Environmental Sensors
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | BME280 | Temperature/Humidity/Pressure | Bosch | $3.50 | $3.50 |
| 1 | MPU6050 | Accelerometer/Gyroscope | InvenSense | $4.50 | $4.50 |
| 1 | HMC5883L | Magnetometer | Honeywell | $3.00 | $3.00 |

### RF Monitoring
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 2 | ADL5511 | RF Power Detector | Analog Devices | $12.00 | $24.00 |
| 1 | AD8318 | Logarithmic Amplifier | Analog Devices | $15.00 | $15.00 |
| 1 | Custom Design | Spectrum Analyzer Frontend | Custom | $180.00 | $180.00 |

## Security & Authentication

### Security Components
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | ATECC608A-MAHDA-T | Crypto Authentication | Microchip | $6.50 | $6.50 |
| 1 | Custom Design | Hardware Security Module | Custom | $95.00 | $95.00 |
| 1 | Custom Design | Biometric Reader | Custom | $45.00 | $45.00 |

## Mechanical & Enclosure

### Enclosure Components
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | Custom Design | Main Enclosure | Custom | $85.00 | $85.00 |
| 1 | Custom Design | RF Shielded Cover | Custom | $65.00 | $65.00 |
| 4 | Custom Design | Antenna Mounts | Custom | $12.00 | $48.00 |
| 1 | Custom Design | Cooling System | Custom | $35.00 | $35.00 |

### Antennas
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 2 | Custom Design | 2.4GHz/5GHz Antennas | Custom | $25.00 | $50.00 |
| 2 | Custom Design | Sub-1GHz Antennas | Custom | $35.00 | $70.00 |
| 1 | Custom Design | MICS Band Antenna | Custom | $45.00 | $45.00 |
| 1 | Custom Design | WMTS Band Antenna | Custom | $45.00 | $45.00 |

## PCB & Assembly

### PCB Components
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | Custom Design | Main PCB (8-layer) | Custom | $180.00 | $180.00 |
| 1 | Custom Design | RF Frontend PCB (6-layer) | Custom | $120.00 | $120.00 |
| 1 | Custom Design | Power Management PCB (4-layer) | Custom | $85.00 | $85.00 |
| 1 | Custom Design | Interface PCB (4-layer) | Custom | $65.00 | $65.00 |

### Passive Components
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 200+ | Various | Resistors, Capacitors, Inductors | Various | $0.50 | $100.00 |
| 50+ | Various | RF Components (Baluns, Couplers, etc.) | Various | $2.50 | $125.00 |

## Development & Testing

### Development Tools
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | ST-LINK/V2 | Debug Interface | STMicroelectronics | $25.00 | $25.00 |
| 1 | Custom Design | RF Test Fixture | Custom | $150.00 | $150.00 |
| 1 | Custom Design | Environmental Test Chamber | Custom | $250.00 | $250.00 |

## Cost Summary

### Component Categories
| Category | Total Cost |
|----------|------------|
| Main Processing Unit | $103.00 |
| RF Frontend Components | $1,247.50 |
| User Interface Components | $183.50 |
| Power Management | $218.00 |
| Connectivity & Communication | $63.00 |
| Sensors & Monitoring | $227.00 |
| Security & Authentication | $146.50 |
| Mechanical & Enclosure | $348.00 |
| PCB & Assembly | $450.00 |
| Development & Testing | $425.00 |

### Total BOM Cost: $3,411.50

## Notes
- All prices are estimated and subject to change based on volume and availability
- Custom components require additional development and tooling costs
- Assembly and testing costs are not included in this BOM
- Redundancy components are included for critical systems
- All components are selected for military-grade reliability and performance