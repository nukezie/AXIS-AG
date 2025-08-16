# Conventional IPG MICS Protocol Specification

## Overview

Conventional Implantable Pulse Generator (IPG) systems use the Medical Implant Communications Service (MICS) band (402-405MHz) for communication with external programmer devices. This document provides the reverse engineering specification for conventional IPG communication protocols, building upon the existing BLE Axis MICS capabilities.

## Protocol Characteristics

### Frequency Band
- **Primary Frequency**: 402-405MHz (MICS band)
- **Channel Allocation**: 10 channels × 300kHz each
- **Channel Centers**: 402.15, 402.45, 402.75, 403.05, 403.35, 403.65, 403.95, 404.25, 404.55, 404.85 MHz
- **Power Limit**: 25μW EIRP maximum
- **Duty Cycle**: 0.1% maximum

### Network Architecture
```
┌─────────────────────────────────────────────────────────────┐
│                    Clinician Programmer                     │
│  ┌─────────────┬─────────────┬─────────────┬─────────────┐  │
│  │   MICS      │  Inductive  │   NFC       │  Control    │  │
│  │  Transceiver│  Coupler    │  Interface  │  Logic      │  │
│  └─────────────┴─────────────┴─────────────┴─────────────┘  │
├─────────────────────────────────────────────────────────────┤
│                    MICS Communication                       │
│  ┌─────────────┬─────────────┬─────────────┬─────────────┐  │
│  │   Channel   │   Protocol  │   Security  │   Data      │  │
│  │   Selection │   Stack     │   Layer     │   Layer     │  │
│  └─────────────┴─────────────┴─────────────┴─────────────┘  │
├─────────────────────────────────────────────────────────────┤
│                    Implantable Pulse Generator              │
│  ┌─────────────┬─────────────┬─────────────┬─────────────┐  │
│  │   MICS      │  Switch     │  Stimulation│  Telemetry  │  │
│  │  Receiver   │  Matrix     │  Circuit    │  Circuit    │  │
│  └─────────────┴─────────────┴─────────────┴─────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## MICS Protocol Stack

### Physical Layer
```
┌─────────────────────────────────────────────────────────────┐
│                    MICS Physical Layer                      │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┬─────────────┬─────────────┬─────────────┐  │
│  │   Frequency │   Modulation│   Coding    │   Timing    │  │
│  │   Hopping   │   (FSK)     │   (Manchester)│   Sync    │  │
│  └─────────────┴─────────────┴─────────────┴─────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Data Link Layer
```
┌─────────────────────────────────────────────────────────────┐
│                    MICS Data Link Layer                     │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┬─────────────┬─────────────┬─────────────┐  │
│  │   MAC       │   Error     │   Flow      │   Frame     │  │
│  │   Protocol  │   Control   │   Control   │   Format    │  │
│  └─────────────┴─────────────┴─────────────┴─────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Network Layer
```
┌─────────────────────────────────────────────────────────────┐
│                    MICS Network Layer                       │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┬─────────────┬─────────────┬─────────────┐  │
│  │   Device    │   Session   │   Routing   │   Security  │  │
│  │   Discovery │   Management│   Protocol  │   Protocol  │  │
│  └─────────────┴─────────────┴─────────────┴─────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## Frame Structure

### MICS Frame Format
```
┌─────────────┬─────────────┬─────────────┬─────────────┬─────────────┐
│   Preamble  │   Sync      │   Header    │   Payload   │   CRC       │
│   (32 bits) │   Word      │  (16 bits)  │ (0-256 bytes)│  (16 bits) │
└─────────────┴─────────────┴─────────────┴─────────────┴─────────────┘
```

### Header Format
```
┌─────────────┬─────────────┬─────────────┬─────────────┬─────────────┐
│   Version   │   Type      │   Length    │   Flags     │   Sequence  │
│   (4 bits)  │   (4 bits)  │   (8 bits)  │   (4 bits)  │   Number    │
│             │             │             │             │   (8 bits)  │
└─────────────┴─────────────┴─────────────┴─────────────┴─────────────┘
```

### Message Types
- **0x01**: Device Discovery
- **0x02**: Authentication
- **0x03**: Configuration Read
- **0x04**: Configuration Write
- **0x05**: Stimulation Command
- **0x06**: Telemetry Data
- **0x07**: Status Request
- **0x08**: Error Report

## Communication Protocols

### 1. MICS/MedRadio Protocol
```
┌─────────────────────────────────────────────────────────────┐
│                    MICS/MedRadio Protocol                   │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┬─────────────┬─────────────┬─────────────┐  │
│  │   Frequency │   Channel   │   Timing    │   Protocol  │  │
│  │   Hopping   │   Selection │   Control   │   Stack     │  │
│  └─────────────┴─────────────┴─────────────┴─────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### 2. Inductive Communication
```
┌─────────────────────────────────────────────────────────────┐
│                    Inductive Protocol                       │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┬─────────────┬─────────────┬─────────────┐  │
│  │   Power     │   Data      │   Control   │   Telemetry │  │
│  │   Transfer  │   Transfer  │   Commands  │   Data      │  │
│  └─────────────┴─────────────┴─────────────┴─────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### 3. NFC Communication
```
┌─────────────────────────────────────────────────────────────┐
│                    NFC Protocol                             │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┬─────────────┬─────────────┬─────────────┐  │
│  │   Wake      │   Setup     │   Data      │   Sleep     │  │
│  │   Sequence  │   Sequence  │   Transfer  │   Sequence  │  │
│  └─────────────┴─────────────┴─────────────┴─────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## Security Protocol

### Authentication
- **Method**: Challenge-response with cryptographic keys
- **Algorithm**: AES-128 or stronger
- **Key Management**: Pre-shared keys with rotation
- **Session Management**: Time-based session tokens

### Encryption
- **Payload Encryption**: AES-128 in CBC mode
- **Header Protection**: HMAC-SHA256 for integrity
- **Key Derivation**: PBKDF2 for key generation
- **Random Number Generation**: Hardware RNG

### Security Handshake
```
1. Programmer → IPG: [Discovery Request]
2. IPG → Programmer: [Device Info + Challenge]
3. Programmer → IPG: [Response + Programmer Challenge]
4. IPG → Programmer: [Response + Session Key]
5. Programmer → IPG: [Session Confirm]
```

## Contact Selection and Stimulation

### Switch Matrix Architecture
```
┌─────────────────────────────────────────────────────────────┐
│                    Switch Matrix                            │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┬─────────────┬─────────────┬─────────────┐  │
│  │   Contact   │   Contact   │   Contact   │   Contact   │  │
│  │     1       │     2       │     3       │     N       │  │
│  └─────────────┴─────────────┴─────────────┴─────────────┘  │
├─────────────────────────────────────────────────────────────┤
│                    Stimulation Circuit                      │
│  ┌─────────────┬─────────────┬─────────────┬─────────────┐  │
│  │   Current   │   Voltage   │   Timing    │   Safety    │  │
│  │   Source    │   Monitor   │   Control   │   Circuit   │  │
│  └─────────────┴─────────────┴─────────────┴─────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Stimulation Parameters
- **Current**: 0.1-10mA (programmable)
- **Voltage**: 0.1-10V (programmable)
- **Pulse Width**: 10-1000μs (programmable)
- **Frequency**: 1-200Hz (programmable)
- **Duty Cycle**: 0.1-50% (programmable)

## Reverse Engineering Approach

### Signal Capture
1. **Frequency Sweep**: Scan 402-405MHz for MICS activity
2. **Channel Analysis**: Identify active MICS channels
3. **Protocol Extraction**: Decode MICS protocol stack
4. **Device Enumeration**: Identify IPG devices

### Protocol Decoding
```python
class MICSDecoder:
    def __init__(self):
        self.frequency_range = (402000000, 405000000)  # 402-405MHz
        self.channels = [402.15, 402.45, 402.75, 403.05, 403.35, 
                        403.65, 403.95, 404.25, 404.55, 404.85]
        self.sample_rate = 1000000  # 1MS/s
        
    def decode_frame(self, mics_data):
        # Extract preamble
        preamble = self.extract_preamble(mics_data)
        
        # Decode sync word
        sync = self.decode_sync(mics_data[4:6])
        
        # Extract header
        header = self.decode_header(mics_data[6:8])
        
        # Extract payload
        payload = self.extract_payload(mics_data, header.length)
        
        # Verify CRC
        if self.verify_crc(mics_data):
            return MICSFrame(header, payload)
        return None
```

### Device Identification
```python
class IPGIdentifier:
    def __init__(self):
        self.known_devices = {}
        
    def identify_ipg(self, device_info, signal_characteristics):
        device = {
            'manufacturer': self.identify_manufacturer(device_info),
            'model': self.identify_model(device_info),
            'type': self.identify_type(device_info),
            'security_level': self.assess_security(device_info),
            'capabilities': self.analyze_capabilities(device_info),
            'signal_characteristics': signal_characteristics
        }
        
        self.known_devices[device_info.id] = device
        return device
```

## Hardware Requirements

### MICS Transceiver
- **Frequency Range**: 402-405MHz
- **Channel Spacing**: 300kHz
- **Power Output**: 25μW EIRP maximum
- **Sensitivity**: -120dBm
- **Modulation**: FSK
- **Data Rate**: 250kbps

### Inductive Coupler
- **Frequency**: 100-500kHz
- **Coupling**: Magnetic field coupling
- **Distance**: 1-10cm
- **Power Transfer**: 1-100mW
- **Data Rate**: 10-100kbps

### NFC Interface
- **Frequency**: 13.56MHz
- **Standard**: ISO/IEC 14443
- **Distance**: 1-4cm
- **Data Rate**: 106-424kbps
- **Power**: Passive or active

### Signal Processing
- **ADC Resolution**: 12-bit minimum
- **Sample Rate**: 1MS/s minimum
- **Processing Power**: ARM Cortex-M4 or equivalent
- **Memory**: 256KB RAM, 1MB Flash

## Implementation Strategy

### Phase 1: MICS Protocol Analysis
1. **Frequency Analysis**: Identify active MICS channels
2. **Protocol Decoding**: Decode MICS protocol stack
3. **Device Discovery**: Identify IPG devices
4. **Security Analysis**: Analyze authentication mechanisms

### Phase 2: Inductive Protocol Analysis
1. **Coupling Analysis**: Analyze inductive coupling characteristics
2. **Power Transfer**: Monitor power transfer patterns
3. **Data Transfer**: Decode inductive data protocols
4. **Timing Analysis**: Analyze communication timing

### Phase 3: NFC Protocol Analysis
1. **Wake Sequence**: Analyze NFC wake patterns
2. **Setup Sequence**: Decode NFC setup protocols
3. **Data Transfer**: Analyze NFC data transfer
4. **Security**: Assess NFC security mechanisms

### Phase 4: Stimulation Analysis
1. **Contact Selection**: Analyze switch matrix operation
2. **Parameter Extraction**: Extract stimulation parameters
3. **Safety Analysis**: Analyze safety circuit operation
4. **Telemetry**: Monitor telemetry data

## Testing and Validation

### Test Scenarios
1. **MICS Compliance**: Test MICS band compliance
2. **Protocol Compliance**: Verify protocol stack operation
3. **Security Testing**: Test authentication and encryption
4. **Safety Testing**: Verify safety circuit operation

### Validation Metrics
- **Detection Accuracy**: >99% device detection success
- **Protocol Decoding**: >95% protocol decode success
- **Security Assessment**: Complete vulnerability analysis
- **Safety Compliance**: Meet all safety standards

## Security Analysis

### MICS Security
- **Frequency Hopping**: Dynamic channel selection
- **Authentication**: Strong cryptographic authentication
- **Encryption**: AES-128 or stronger encryption
- **Access Control**: Role-based access control

### Physical Security
- **Proximity Requirement**: Close proximity needed for control
- **Inductive Coupling**: Magnetic field coupling security
- **NFC Security**: ISO/IEC 14443 security features
- **Tamper Detection**: Hardware tamper detection

## Legal and Ethical Considerations

### Compliance Requirements
- **FCC Regulations**: MICS band compliance (Part 95)
- **FDA Regulations**: Medical device safety compliance
- **Medical Privacy**: HIPAA compliance for patient data
- **Authorization**: DoD authorization required

### Safety Considerations
- **Medical Device Safety**: Ensure no interference with devices
- **Patient Safety**: Maintain patient safety standards
- **Data Protection**: Secure handling of medical data
- **Authorized Use**: Only for authorized research and security assessment

## Integration with BLE Axis

### Existing MICS Capabilities
The BLE Axis project already includes comprehensive MICS capabilities:

1. **MICS Device Identification**: Complete device database and identification system
2. **Frequency Monitoring**: All 10 MICS channels (402-405MHz)
3. **Protocol Analysis**: MICS protocol stack analysis
4. **Security Assessment**: Device security analysis and compliance monitoring

### Enhanced Capabilities
This extension adds:

1. **Inductive Protocol Analysis**: Analysis of inductive coupling protocols
2. **NFC Protocol Analysis**: NFC communication protocol analysis
3. **Stimulation Analysis**: Contact selection and stimulation parameter analysis
4. **Advanced Security**: Enhanced security assessment tools

## References

1. "Medical Implant Communications Service (MICS) Federal Register" - FCC
2. "MICS Band Medical Device Communication Protocols" - IEEE 802.15.6
3. "Implantable Medical Device Security" - FDA Guidance
4. "MICS Device Identification and Analysis" - BLE Axis Project

---

**Note**: This specification builds upon the existing BLE Axis MICS capabilities and extends them for comprehensive IPG analysis. All reverse engineering activities must be conducted in compliance with applicable laws and regulations, particularly regarding medical device safety and patient privacy.