#!/usr/bin/env python3
"""
MICS Device Identification System
BLE Axis - Medical Implant Communications Service Device Identification

This module provides comprehensive identification and analysis of MICS band devices
based on MAC addresses, device characteristics, and communication patterns.

Author: BLE Axis Development Team
License: DoD Authorized Use Only
"""

import json
import sqlite3
import hashlib
import logging
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass, asdict
from enum import Enum
import re

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DeviceType(Enum):
    """MICS Device Types"""
    PACEMAKER = "pacemaker"
    DEFIBRILLATOR = "defibrillator"
    CARDIAC_MONITOR = "cardiac_monitor"
    NEUROSTIMULATOR = "neurostimulator"
    DEEP_BRAIN_STIMULATOR = "deep_brain_stimulator"
    INSULIN_PUMP = "insulin_pump"
    GLUCOSE_MONITOR = "glucose_monitor"
    BONE_GROWTH_STIMULATOR = "bone_growth_stimulator"
    RESEARCH_DEVICE = "research_device"
    UNKNOWN = "unknown"

class DeviceManufacturer(Enum):
    """Known MICS Device Manufacturers"""
    MEDTRONIC = "medtronic"
    BOSTON_SCIENTIFIC = "boston_scientific"
    ABBOTT = "abbott"
    BIOTRONIK = "biotronik"
    ST_JUDE = "st_jude"
    SORIN = "sorin"
    ELA = "ela"
    VITATRON = "vitatron"
    UNKNOWN = "unknown"

class SecurityLevel(Enum):
    """Device Security Levels"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

@dataclass
class MICSDevice:
    """MICS Device Information"""
    mac_address: str
    device_type: DeviceType
    manufacturer: DeviceManufacturer
    model: str
    serial_number: str
    firmware_version: str
    security_level: SecurityLevel
    frequency_channels: List[int]
    power_level: float  # in μW
    duty_cycle: float   # percentage
    last_seen: datetime
    first_seen: datetime
    communication_pattern: Dict[str, Any]
    security_features: List[str]
    vulnerabilities: List[str]
    compliance_status: Dict[str, bool]
    notes: str = ""

@dataclass
class DeviceSignature:
    """Device RF Signature for Identification"""
    mac_address: str
    frequency_hopping_pattern: List[int]
    packet_structure: Dict[str, Any]
    timing_characteristics: Dict[str, float]
    modulation_type: str
    data_rate: int
    power_variations: List[float]
    interference_patterns: List[Dict[str, Any]]

class MICSDeviceIdentifier:
    """MICS Device Identification and Analysis System"""
    
    def __init__(self, database_path: str = "mics_devices.db"):
        """Initialize the MICS Device Identifier"""
        self.database_path = database_path
        self.device_database = {}
        self.signature_database = {}
        self.manufacturer_patterns = {}
        self.device_patterns = {}
        
        # Initialize databases
        self._init_database()
        self._load_known_devices()
        self._load_manufacturer_patterns()
        
    def _init_database(self):
        """Initialize SQLite database for device storage"""
        try:
            with sqlite3.connect(self.database_path) as conn:
                cursor = conn.cursor()
                
                # Create devices table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS mics_devices (
                        mac_address TEXT PRIMARY KEY,
                        device_type TEXT NOT NULL,
                        manufacturer TEXT NOT NULL,
                        model TEXT,
                        serial_number TEXT,
                        firmware_version TEXT,
                        security_level TEXT,
                        frequency_channels TEXT,
                        power_level REAL,
                        duty_cycle REAL,
                        last_seen TEXT,
                        first_seen TEXT,
                        communication_pattern TEXT,
                        security_features TEXT,
                        vulnerabilities TEXT,
                        compliance_status TEXT,
                        notes TEXT
                    )
                ''')
                
                # Create signatures table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS device_signatures (
                        mac_address TEXT PRIMARY KEY,
                        frequency_hopping_pattern TEXT,
                        packet_structure TEXT,
                        timing_characteristics TEXT,
                        modulation_type TEXT,
                        data_rate INTEGER,
                        power_variations TEXT,
                        interference_patterns TEXT
                    )
                ''')
                
                # Create manufacturer patterns table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS manufacturer_patterns (
                        manufacturer TEXT PRIMARY KEY,
                        mac_prefixes TEXT,
                        device_patterns TEXT,
                        security_features TEXT,
                        known_vulnerabilities TEXT
                    )
                ''')
                
                conn.commit()
                logger.info("Database initialized successfully")
                
        except Exception as e:
            logger.error(f"Database initialization failed: {e}")
            raise
    
    def _load_known_devices(self):
        """Load known MICS devices from JSON database"""
        try:
            with open("mics_device_database.json", "r") as f:
                devices_data = json.load(f)
                
            for device_data in devices_data.get("devices", []):
                device = MICSDevice(
                    mac_address=device_data["mac_address"],
                    device_type=DeviceType(device_data["device_type"]),
                    manufacturer=DeviceManufacturer(device_data["manufacturer"]),
                    model=device_data["model"],
                    serial_number=device_data["serial_number"],
                    firmware_version=device_data["firmware_version"],
                    security_level=SecurityLevel(device_data["security_level"]),
                    frequency_channels=device_data["frequency_channels"],
                    power_level=device_data["power_level"],
                    duty_cycle=device_data["duty_cycle"],
                    last_seen=datetime.fromisoformat(device_data["last_seen"]),
                    first_seen=datetime.fromisoformat(device_data["first_seen"]),
                    communication_pattern=device_data["communication_pattern"],
                    security_features=device_data["security_features"],
                    vulnerabilities=device_data["vulnerabilities"],
                    compliance_status=device_data["compliance_status"],
                    notes=device_data.get("notes", "")
                )
                self.device_database[device.mac_address] = device
                
            logger.info(f"Loaded {len(self.device_database)} known devices")
            
        except FileNotFoundError:
            logger.warning("MICS device database not found, creating new one")
            self._create_default_database()
        except Exception as e:
            logger.error(f"Error loading device database: {e}")
    
    def _create_default_database(self):
        """Create default MICS device database with known devices"""
        default_devices = {
            "devices": [
                {
                    "mac_address": "00:11:22:33:44:55",
                    "device_type": "pacemaker",
                    "manufacturer": "medtronic",
                    "model": "Adapta ADDR01",
                    "serial_number": "MDT001234",
                    "firmware_version": "2.1.3",
                    "security_level": "high",
                    "frequency_channels": [1, 3, 5, 7, 9],
                    "power_level": 25.0,
                    "duty_cycle": 0.001,
                    "last_seen": datetime.now().isoformat(),
                    "first_seen": datetime.now().isoformat(),
                    "communication_pattern": {
                        "packet_size": 64,
                        "transmission_interval": 1000,
                        "acknowledgment_required": True
                    },
                    "security_features": ["AES-128", "Authentication", "Frequency Hopping"],
                    "vulnerabilities": [],
                    "compliance_status": {
                        "fcc_part_95": True,
                        "fda_approved": True,
                        "hipaa_compliant": True
                    },
                    "notes": "Standard Medtronic pacemaker with enhanced security"
                },
                {
                    "mac_address": "00:11:22:33:44:66",
                    "device_type": "defibrillator",
                    "manufacturer": "boston_scientific",
                    "model": "Cognis CRT-D",
                    "serial_number": "BSC005678",
                    "firmware_version": "1.8.2",
                    "security_level": "critical",
                    "frequency_channels": [2, 4, 6, 8, 10],
                    "power_level": 25.0,
                    "duty_cycle": 0.001,
                    "last_seen": datetime.now().isoformat(),
                    "first_seen": datetime.now().isoformat(),
                    "communication_pattern": {
                        "packet_size": 128,
                        "transmission_interval": 500,
                        "acknowledgment_required": True
                    },
                    "security_features": ["AES-256", "Multi-factor Authentication", "Frequency Hopping", "Encrypted Telemetry"],
                    "vulnerabilities": [],
                    "compliance_status": {
                        "fcc_part_95": True,
                        "fda_approved": True,
                        "hipaa_compliant": True
                    },
                    "notes": "Boston Scientific defibrillator with advanced security features"
                }
            ]
        }
        
        with open("mics_device_database.json", "w") as f:
            json.dump(default_devices, f, indent=2, default=str)
        
        logger.info("Created default MICS device database")
    
    def _load_manufacturer_patterns(self):
        """Load manufacturer identification patterns"""
        self.manufacturer_patterns = {
            DeviceManufacturer.MEDTRONIC: {
                "mac_prefixes": ["00:11:22", "00:11:23", "00:11:24"],
                "device_patterns": {
                    "pacemaker": r"Adapta|Sensia|Versa",
                    "defibrillator": r"Evera|Viva|Primo",
                    "monitor": r"CareLink|Reveal"
                },
                "security_features": ["AES-128", "Authentication", "Frequency Hopping"],
                "known_vulnerabilities": []
            },
            DeviceManufacturer.BOSTON_SCIENTIFIC: {
                "mac_prefixes": ["00:11:25", "00:11:26", "00:11:27"],
                "device_patterns": {
                    "pacemaker": r"Cognis|Altrua|Ingenio",
                    "defibrillator": r"Cognis|Teligen|Livian",
                    "monitor": r"Latitude|Tachy"
                },
                "security_features": ["AES-256", "Multi-factor Authentication", "Frequency Hopping"],
                "known_vulnerabilities": []
            },
            DeviceManufacturer.ABBOTT: {
                "mac_prefixes": ["00:11:28", "00:11:29", "00:11:2A"],
                "device_patterns": {
                    "pacemaker": r"Assurity|Endurity|Zephyr",
                    "defibrillator": r"Fortify|Ellipse|Unify",
                    "monitor": r"Merlin"
                },
                "security_features": ["AES-128", "Authentication", "Frequency Hopping"],
                "known_vulnerabilities": []
            }
        }
    
    def identify_device(self, mac_address: str, rf_signature: Optional[DeviceSignature] = None) -> Optional[MICSDevice]:
        """Identify a MICS device based on MAC address and RF signature"""
        try:
            # Normalize MAC address
            mac_address = self._normalize_mac_address(mac_address)
            
            # Check if device is in database
            if mac_address in self.device_database:
                device = self.device_database[mac_address]
                device.last_seen = datetime.now()
                return device
            
            # Try to identify based on manufacturer patterns
            manufacturer = self._identify_manufacturer(mac_address)
            device_type = self._identify_device_type(mac_address, rf_signature)
            
            if manufacturer and device_type:
                # Create new device entry
                device = MICSDevice(
                    mac_address=mac_address,
                    device_type=device_type,
                    manufacturer=manufacturer,
                    model="Unknown",
                    serial_number="",
                    firmware_version="Unknown",
                    security_level=self._determine_security_level(device_type, manufacturer),
                    frequency_channels=[1, 3, 5, 7, 9],  # Default channels
                    power_level=25.0,  # Default MICS power limit
                    duty_cycle=0.001,  # Default duty cycle
                    last_seen=datetime.now(),
                    first_seen=datetime.now(),
                    communication_pattern={},
                    security_features=self.manufacturer_patterns.get(manufacturer, {}).get("security_features", []),
                    vulnerabilities=[],
                    compliance_status={"fcc_part_95": True, "fda_approved": False, "hipaa_compliant": False},
                    notes=f"Auto-identified {device_type.value} from {manufacturer.value}"
                )
                
                # Add to database
                self.device_database[mac_address] = device
                self._save_device_to_database(device)
                
                return device
            
            return None
            
        except Exception as e:
            logger.error(f"Error identifying device {mac_address}: {e}")
            return None
    
    def _normalize_mac_address(self, mac_address: str) -> str:
        """Normalize MAC address format"""
        # Remove separators and convert to uppercase
        mac = re.sub(r'[:\-\.]', '', mac_address).upper()
        
        # Add colons every 2 characters
        return ':'.join([mac[i:i+2] for i in range(0, len(mac), 2)])
    
    def _identify_manufacturer(self, mac_address: str) -> Optional[DeviceManufacturer]:
        """Identify manufacturer based on MAC address prefix"""
        mac_prefix = mac_address[:8]  # First 3 bytes
        
        for manufacturer, patterns in self.manufacturer_patterns.items():
            if mac_prefix in patterns["mac_prefixes"]:
                return manufacturer
        
        return DeviceManufacturer.UNKNOWN
    
    def _identify_device_type(self, mac_address: str, rf_signature: Optional[DeviceSignature]) -> DeviceType:
        """Identify device type based on MAC address and RF signature"""
        # This would be enhanced with machine learning and pattern recognition
        # For now, use simple heuristics
        
        if rf_signature:
            # Analyze RF signature for device type indicators
            if rf_signature.data_rate > 100:
                return DeviceType.CARDIAC_MONITOR
            elif len(rf_signature.frequency_hopping_pattern) > 5:
                return DeviceType.DEFIBRILLATOR
            else:
                return DeviceType.PACEMAKER
        
        # Fallback to MAC address analysis
        return DeviceType.UNKNOWN
    
    def _determine_security_level(self, device_type: DeviceType, manufacturer: DeviceManufacturer) -> SecurityLevel:
        """Determine security level based on device type and manufacturer"""
        if device_type in [DeviceType.DEFIBRILLATOR, DeviceType.DEEP_BRAIN_STIMULATOR]:
            return SecurityLevel.CRITICAL
        elif device_type in [DeviceType.PACEMAKER, DeviceType.NEUROSTIMULATOR]:
            return SecurityLevel.HIGH
        elif device_type in [DeviceType.INSULIN_PUMP, DeviceType.GLUCOSE_MONITOR]:
            return SecurityLevel.MEDIUM
        else:
            return SecurityLevel.LOW
    
    def _save_device_to_database(self, device: MICSDevice):
        """Save device to SQLite database"""
        try:
            with sqlite3.connect(self.database_path) as conn:
                cursor = conn.cursor()
                
                cursor.execute('''
                    INSERT OR REPLACE INTO mics_devices 
                    (mac_address, device_type, manufacturer, model, serial_number, 
                     firmware_version, security_level, frequency_channels, power_level, 
                     duty_cycle, last_seen, first_seen, communication_pattern, 
                     security_features, vulnerabilities, compliance_status, notes)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    device.mac_address,
                    device.device_type.value,
                    device.manufacturer.value,
                    device.model,
                    device.serial_number,
                    device.firmware_version,
                    device.security_level.value,
                    json.dumps(device.frequency_channels),
                    device.power_level,
                    device.duty_cycle,
                    device.last_seen.isoformat(),
                    device.first_seen.isoformat(),
                    json.dumps(device.communication_pattern),
                    json.dumps(device.security_features),
                    json.dumps(device.vulnerabilities),
                    json.dumps(device.compliance_status),
                    device.notes
                ))
                
                conn.commit()
                
        except Exception as e:
            logger.error(f"Error saving device to database: {e}")
    
    def add_device(self, device: MICSDevice):
        """Add a new device to the database"""
        try:
            self.device_database[device.mac_address] = device
            self._save_device_to_database(device)
            logger.info(f"Added device {device.mac_address} to database")
        except Exception as e:
            logger.error(f"Error adding device: {e}")
    
    def update_device(self, mac_address: str, updates: Dict[str, Any]):
        """Update device information"""
        try:
            if mac_address in self.device_database:
                device = self.device_database[mac_address]
                
                # Update device attributes
                for key, value in updates.items():
                    if hasattr(device, key):
                        setattr(device, key, value)
                
                device.last_seen = datetime.now()
                self._save_device_to_database(device)
                logger.info(f"Updated device {mac_address}")
                
        except Exception as e:
            logger.error(f"Error updating device: {e}")
    
    def get_device(self, mac_address: str) -> Optional[MICSDevice]:
        """Get device by MAC address"""
        return self.device_database.get(mac_address)
    
    def get_devices_by_type(self, device_type: DeviceType) -> List[MICSDevice]:
        """Get all devices of a specific type"""
        return [device for device in self.device_database.values() 
                if device.device_type == device_type]
    
    def get_devices_by_manufacturer(self, manufacturer: DeviceManufacturer) -> List[MICSDevice]:
        """Get all devices from a specific manufacturer"""
        return [device for device in self.device_database.values() 
                if device.manufacturer == manufacturer]
    
    def get_devices_by_security_level(self, security_level: SecurityLevel) -> List[MICSDevice]:
        """Get all devices with a specific security level"""
        return [device for device in self.device_database.values() 
                if device.security_level == security_level]
    
    def export_database(self, filename: str = "mics_devices_export.json"):
        """Export device database to JSON file"""
        try:
            export_data = {
                "export_date": datetime.now().isoformat(),
                "total_devices": len(self.device_database),
                "devices": [asdict(device) for device in self.device_database.values()]
            }
            
            with open(filename, "w") as f:
                json.dump(export_data, f, indent=2, default=str)
            
            logger.info(f"Exported {len(self.device_database)} devices to {filename}")
            
        except Exception as e:
            logger.error(f"Error exporting database: {e}")
    
    def generate_security_report(self) -> Dict[str, Any]:
        """Generate security analysis report"""
        try:
            report = {
                "report_date": datetime.now().isoformat(),
                "total_devices": len(self.device_database),
                "security_summary": {
                    "critical": len(self.get_devices_by_security_level(SecurityLevel.CRITICAL)),
                    "high": len(self.get_devices_by_security_level(SecurityLevel.HIGH)),
                    "medium": len(self.get_devices_by_security_level(SecurityLevel.MEDIUM)),
                    "low": len(self.get_devices_by_security_level(SecurityLevel.LOW))
                },
                "manufacturer_summary": {},
                "device_type_summary": {},
                "compliance_summary": {
                    "fcc_compliant": 0,
                    "fda_approved": 0,
                    "hipaa_compliant": 0
                },
                "vulnerabilities": []
            }
            
            # Analyze devices
            for device in self.device_database.values():
                # Manufacturer summary
                manufacturer = device.manufacturer.value
                if manufacturer not in report["manufacturer_summary"]:
                    report["manufacturer_summary"][manufacturer] = 0
                report["manufacturer_summary"][manufacturer] += 1
                
                # Device type summary
                device_type = device.device_type.value
                if device_type not in report["device_type_summary"]:
                    report["device_type_summary"][device_type] = 0
                report["device_type_summary"][device_type] += 1
                
                # Compliance summary
                if device.compliance_status.get("fcc_part_95", False):
                    report["compliance_summary"]["fcc_compliant"] += 1
                if device.compliance_status.get("fda_approved", False):
                    report["compliance_summary"]["fda_approved"] += 1
                if device.compliance_status.get("hipaa_compliant", False):
                    report["compliance_summary"]["hipaa_compliant"] += 1
                
                # Vulnerabilities
                report["vulnerabilities"].extend(device.vulnerabilities)
            
            return report
            
        except Exception as e:
            logger.error(f"Error generating security report: {e}")
            return {}

# Example usage and testing
if __name__ == "__main__":
    # Initialize the identifier
    identifier = MICSDeviceIdentifier()
    
    # Test device identification
    test_mac = "00:11:22:33:44:55"
    device = identifier.identify_device(test_mac)
    
    if device:
        print(f"Identified device: {device.model} from {device.manufacturer.value}")
        print(f"Device type: {device.device_type.value}")
        print(f"Security level: {device.security_level.value}")
    
    # Generate security report
    report = identifier.generate_security_report()
    print(f"Security report: {report}")
    
    # Export database
    identifier.export_database()