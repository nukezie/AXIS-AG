# Bill of Materials (BOM) - BLE Axis

## System Overview
This BOM covers all components required for the advanced BLE and MICS band analysis tool, optimized for budget-conscious manufacturing while maintaining high performance and reliability for DoD applications.

## Main Processing Unit

### Microcontroller
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | STM32F405RGT6 | ARM Cortex-M4 168MHz, 1MB Flash, 192KB RAM | STMicroelectronics | $8.50 | $8.50 |

### Memory & Storage
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | W25Q128JVSIQ | 128MB SPI NOR Flash | Winbond | $3.50 | $3.50 |
| 1 | IS42S16400J-7TLI | 64MB SDRAM | ISSI | $4.00 | $4.00 |
| 1 | SDINBDG4-8G | 8GB eMMC Storage | Western Digital | $8.00 | $8.00 |

## RF Frontend Components

### BLE Transceiver
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | CC2652R1FRGZR | 2.4GHz BLE Transceiver | Texas Instruments | $8.50 | $8.50 |

### MICS Band Transceiver
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | CC1101RGPR | 402-405MHz MICS Band Transceiver | Texas Instruments | $6.50 | $6.50 |

### RF Switches & Filters
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 2 | SKY13317-378LF | SPDT RF Switch, 0.1-6GHz | Skyworks | $3.50 | $7.00 |
| 1 | SKY13318-385LF | SP4T RF Switch, 0.1-6GHz | Skyworks | $4.50 | $4.50 |
| 2 | Custom Design | BLE Bandpass Filter (2.4GHz) | Custom | $8.00 | $16.00 |
| 1 | Custom Design | MICS Bandpass Filter (402-405MHz) | Custom | $12.00 | $12.00 |

### Power Amplifiers
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | SKY66112-11 | 2.4GHz Power Amplifier, 20dBm | Skyworks | $8.00 | $8.00 |
| 1 | Custom Design | MICS Band Power Amplifier, 25μW | Custom | $15.00 | $15.00 |

### Low Noise Amplifiers
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | SKY67150-396LF | 2.4GHz LNA, 1.5dB NF | Skyworks | $6.50 | $6.50 |
| 1 | Custom Design | MICS Band LNA, 1.0dB NF | Custom | $12.00 | $12.00 |

## User Interface Components

### Display
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | Custom Design | 3.5" TFT LCD, 480x320, Capacitive Touch | Custom | $25.00 | $25.00 |
| 1 | ST7735S | Display Controller | Sitronix | $2.50 | $2.50 |

### Controls
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 6 | EVQ-PAD04K | Tactile Pushbuttons | Panasonic | $2.50 | $15.00 |
| 1 | PEC11R-4220F-S0024 | Rotary Encoder | Bourns | $8.00 | $8.00 |
| 1 | Custom Design | Emergency Stop Button | Custom | $8.00 | $8.00 |

### Audio
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | WM8731CLSEFL | Audio Codec | Cirrus Logic | $5.50 | $5.50 |
| 1 | Custom Design | Speaker | Custom | $6.00 | $6.00 |
| 1 | Custom Design | Microphone | Custom | $4.00 | $4.00 |

## Power Management

### Power Supply
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | TPS65217CRSLR | Power Management IC | Texas Instruments | $12.00 | $12.00 |
| 2 | TPS63070DRCR | Buck-Boost Converter | Texas Instruments | $4.50 | $9.00 |
| 3 | TPS7A4700RGWT | Low-Noise LDO Regulator | Texas Instruments | $3.50 | $10.50 |
| 1 | Custom Design | Battery Pack, 7.4V, 5Ah | Custom | $45.00 | $45.00 |
| 1 | BQ25895RTWR | Battery Charger | Texas Instruments | $3.50 | $3.50 |

### Power Distribution
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 2 | IRLML6244TRPBF | Power MOSFET | Infineon | $1.50 | $3.00 |
| 1 | Custom Design | Power Distribution Board | Custom | $12.00 | $12.00 |

## Connectivity & Communication

### USB & Network
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | USB3300-EZK-TR | USB 3.0 PHY | Microchip | $8.00 | $8.00 |
| 1 | USB-C Connector | USB-C Receptacle | Various | $2.50 | $2.50 |

### Wireless Connectivity
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | ESP32-WROOM-32 | WiFi/Bluetooth Module | Espressif | $8.00 | $8.00 |

## Sensors & Monitoring

### Environmental Sensors
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | BME280 | Temperature/Humidity/Pressure | Bosch | $3.50 | $3.50 |
| 1 | MPU6050 | Accelerometer/Gyroscope | InvenSense | $4.50 | $4.50 |

### RF Monitoring
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | ADL5511 | RF Power Detector | Analog Devices | $12.00 | $12.00 |
| 1 | AD8318 | Logarithmic Amplifier | Analog Devices | $15.00 | $15.00 |
| 1 | Custom Design | Spectrum Analyzer Frontend | Custom | $35.00 | $35.00 |

## Security & Authentication

### Security Components
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | ATECC608A-MAHDA-T | Crypto Authentication | Microchip | $6.50 | $6.50 |
| 1 | Custom Design | Hardware Security Module | Custom | $25.00 | $25.00 |

## Mechanical & Enclosure

### Enclosure Components
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | Custom Design | Main Enclosure | Custom | $35.00 | $35.00 |
| 1 | Custom Design | RF Shielded Cover | Custom | $25.00 | $25.00 |
| 2 | Custom Design | Antenna Mounts | Custom | $8.00 | $16.00 |
| 1 | Custom Design | Cooling System | Custom | $15.00 | $15.00 |

### Antennas
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | Custom Design | 2.4GHz BLE Antenna | Custom | $12.00 | $12.00 |
| 1 | Custom Design | MICS Band Antenna | Custom | $18.00 | $18.00 |

## PCB & Assembly

### PCB Components
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | Custom Design | Main PCB (6-layer) | Custom | $85.00 | $85.00 |
| 1 | Custom Design | RF Frontend PCB (4-layer) | Custom | $45.00 | $45.00 |
| 1 | Custom Design | Power Management PCB (2-layer) | Custom | $25.00 | $25.00 |

### Passive Components
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 150+ | Various | Resistors, Capacitors, Inductors | Various | $0.30 | $45.00 |
| 30+ | Various | RF Components (Baluns, Couplers, etc.) | Various | $1.50 | $45.00 |

## Development & Testing

### Development Tools
| Qty | Part Number | Description | Manufacturer | Unit Cost | Total Cost |
|-----|-------------|-------------|--------------|-----------|------------|
| 1 | ST-LINK/V2 | Debug Interface | STMicroelectronics | $25.00 | $25.00 |
| 1 | Custom Design | RF Test Fixture | Custom | $35.00 | $35.00 |

## Cost Summary

### Component Categories
| Category | Total Cost |
|----------|------------|
| Main Processing Unit | $24.00 |
| RF Frontend Components | $108.50 |
| User Interface Components | $69.00 |
| Power Management | $95.00 |
| Connectivity & Communication | $10.50 |
| Sensors & Monitoring | $71.00 |
| Security & Authentication | $31.50 |
| Mechanical & Enclosure | $111.00 |
| PCB & Assembly | $200.00 |
| Development & Testing | $60.00 |

### Total BOM Cost: $780.50

## Budget Optimization Notes

### Cost Reduction Strategies
1. **Component Consolidation**: Using single-chip solutions where possible
2. **Standard Components**: Leveraging off-the-shelf components for custom designs
3. **Volume Pricing**: Assuming 100+ unit production quantities
4. **Alternative Sources**: Using alternative suppliers for better pricing
5. **Simplified Design**: Reducing complexity while maintaining functionality

### Manufacturing Considerations
- **Assembly Cost**: Estimated $50-75 per unit
- **Testing Cost**: Estimated $25-35 per unit
- **Packaging Cost**: Estimated $15-25 per unit
- **Total Manufacturing Cost**: ~$165 per unit

### Target Pricing
- **BOM Cost**: $780.50
- **Manufacturing Cost**: $165.00
- **Total Unit Cost**: $945.50
- **Target Retail Price**: $1,200-1,500

## Notes
- All prices are estimated for 100+ unit quantities
- Custom components require additional development costs
- Assembly and testing costs are included in manufacturing estimate
- All components selected for military-grade reliability
- MICS band compliance requires special attention to power levels
- BLE components optimized for latest Bluetooth 5.2+ standards