#!/usr/bin/env python3
"""
MICS Device Identification System Test Suite
BLE Axis - Test and Demonstration Script

This script demonstrates the MICS device identification system functionality
with comprehensive test cases and examples.

Author: BLE Axis Development Team
License: DoD Authorized Use Only
"""

import sys
import os
import json
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Any

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from mics_device_identification import (
    MICSDeviceIdentifier, 
    MICSDevice, 
    DeviceSignature,
    DeviceType, 
    DeviceManufacturer, 
    SecurityLevel
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class MICSIdentificationTester:
    """Test suite for MICS Device Identification System"""
    
    def __init__(self):
        """Initialize the test suite"""
        self.identifier = MICSDeviceIdentifier()
        self.test_results = {
            "passed": 0,
            "failed": 0,
            "total": 0
        }
        
    def run_all_tests(self):
        """Run all test cases"""
        logger.info("Starting MICS Device Identification System Tests")
        logger.info("=" * 60)
        
        # Test basic functionality
        self.test_basic_identification()
        self.test_rf_signature_analysis()
        self.test_manufacturer_identification()
        self.test_security_analysis()
        self.test_database_operations()
        self.test_compliance_checking()
        self.test_error_handling()
        self.test_performance()
        
        # Print test summary
        self.print_test_summary()
        
    def test_basic_identification(self):
        """Test basic device identification functionality"""
        logger.info("Testing Basic Device Identification")
        logger.info("-" * 40)
        
        # Test 1: Known device identification
        test_mac = "00:11:22:33:44:55"
        device = self.identifier.identify_device(test_mac)
        
        if device and device.model == "Adapta ADDR01":
            logger.info("✓ Test 1 PASSED: Known device identification")
            self.test_results["passed"] += 1
        else:
            logger.error("✗ Test 1 FAILED: Known device identification")
            self.test_results["failed"] += 1
        self.test_results["total"] += 1
        
        # Test 2: Unknown device identification
        unknown_mac = "00:11:22:33:44:AA"
        device = self.identifier.identify_device(unknown_mac)
        
        if device and device.manufacturer == DeviceManufacturer.MEDTRONIC:
            logger.info("✓ Test 2 PASSED: Unknown device manufacturer identification")
            self.test_results["passed"] += 1
        else:
            logger.error("✗ Test 2 FAILED: Unknown device manufacturer identification")
            self.test_results["failed"] += 1
        self.test_results["total"] += 1
        
        # Test 3: MAC address normalization
        test_macs = [
            "00:11:22:33:44:55",
            "00-11-22-33-44-55",
            "001122334455",
            "00.11.22.33.44.55"
        ]
        
        normalized_macs = []
        for mac in test_macs:
            device = self.identifier.identify_device(mac)
            if device:
                normalized_macs.append(device.mac_address)
        
        if len(set(normalized_macs)) == 1:
            logger.info("✓ Test 3 PASSED: MAC address normalization")
            self.test_results["passed"] += 1
        else:
            logger.error("✗ Test 3 FAILED: MAC address normalization")
            self.test_results["failed"] += 1
        self.test_results["total"] += 1
        
    def test_rf_signature_analysis(self):
        """Test RF signature analysis functionality"""
        logger.info("Testing RF Signature Analysis")
        logger.info("-" * 40)
        
        # Test 1: RF signature creation and analysis
        rf_signature = DeviceSignature(
            mac_address="00:11:22:33:44:66",
            frequency_hopping_pattern=[2, 4, 6, 8, 10],
            packet_structure={"size": 128, "type": "data"},
            timing_characteristics={"interval": 500, "jitter": 10},
            modulation_type="FSK",
            data_rate=100,
            power_variations=[25.0, 24.8, 25.1],
            interference_patterns=[]
        )
        
        device = self.identifier.identify_device("00:11:22:33:44:66", rf_signature)
        
        if device and device.device_type == DeviceType.DEFIBRILLATOR:
            logger.info("✓ Test 1 PASSED: RF signature analysis")
            self.test_results["passed"] += 1
        else:
            logger.error("✗ Test 1 FAILED: RF signature analysis")
            self.test_results["failed"] += 1
        self.test_results["total"] += 1
        
        # Test 2: High data rate device identification
        high_rate_signature = DeviceSignature(
            mac_address="00:11:22:33:44:77",
            frequency_hopping_pattern=[1, 2, 3, 4, 5],
            packet_structure={"size": 256, "type": "monitor"},
            timing_characteristics={"interval": 2000, "jitter": 50},
            modulation_type="FSK",
            data_rate=150,
            power_variations=[20.0, 19.8, 20.2],
            interference_patterns=[]
        )
        
        device = self.identifier.identify_device("00:11:22:33:44:77", high_rate_signature)
        
        if device and device.device_type == DeviceType.CARDIAC_MONITOR:
            logger.info("✓ Test 2 PASSED: High data rate device identification")
            self.test_results["passed"] += 1
        else:
            logger.error("✗ Test 2 FAILED: High data rate device identification")
            self.test_results["failed"] += 1
        self.test_results["total"] += 1
        
    def test_manufacturer_identification(self):
        """Test manufacturer identification functionality"""
        logger.info("Testing Manufacturer Identification")
        logger.info("-" * 40)
        
        # Test different manufacturer MAC prefixes
        manufacturer_tests = [
            ("00:11:22:33:44:55", DeviceManufacturer.MEDTRONIC),
            ("00:11:25:33:44:55", DeviceManufacturer.BOSTON_SCIENTIFIC),
            ("00:11:28:33:44:55", DeviceManufacturer.ABBOTT),
            ("00:11:2B:33:44:55", DeviceManufacturer.BIOTRONIK),
            ("00:11:2E:33:44:55", DeviceManufacturer.ST_JUDE),
            ("00:11:31:33:44:55", DeviceManufacturer.SORIN),
            ("00:11:34:33:44:55", DeviceManufacturer.ELA),
            ("00:11:37:33:44:55", DeviceManufacturer.VITATRON),
        ]
        
        passed = 0
        for mac, expected_manufacturer in manufacturer_tests:
            device = self.identifier.identify_device(mac)
            if device and device.manufacturer == expected_manufacturer:
                passed += 1
            else:
                logger.error(f"✗ Manufacturer identification failed for {mac}")
        
        if passed == len(manufacturer_tests):
            logger.info(f"✓ Test PASSED: Manufacturer identification ({passed}/{len(manufacturer_tests)})")
            self.test_results["passed"] += 1
        else:
            logger.error(f"✗ Test FAILED: Manufacturer identification ({passed}/{len(manufacturer_tests)})")
            self.test_results["failed"] += 1
        self.test_results["total"] += 1
        
    def test_security_analysis(self):
        """Test security analysis functionality"""
        logger.info("Testing Security Analysis")
        logger.info("-" * 40)
        
        # Test 1: Security level determination
        security_tests = [
            ("00:11:22:33:44:66", SecurityLevel.CRITICAL),  # Defibrillator
            ("00:11:22:33:44:55", SecurityLevel.HIGH),      # Pacemaker
            ("00:11:22:33:44:77", SecurityLevel.MEDIUM),    # Cardiac monitor
            ("00:11:22:33:44:BB", SecurityLevel.LOW),       # Glucose monitor
        ]
        
        passed = 0
        for mac, expected_level in security_tests:
            device = self.identifier.identify_device(mac)
            if device and device.security_level == expected_level:
                passed += 1
            else:
                logger.error(f"✗ Security level test failed for {mac}")
        
        if passed == len(security_tests):
            logger.info(f"✓ Test 1 PASSED: Security level determination ({passed}/{len(security_tests)})")
            self.test_results["passed"] += 1
        else:
            logger.error(f"✗ Test 1 FAILED: Security level determination ({passed}/{len(security_tests)})")
            self.test_results["failed"] += 1
        self.test_results["total"] += 1
        
        # Test 2: Security report generation
        report = self.identifier.generate_security_report()
        
        if (report and 
            "total_devices" in report and 
            "security_summary" in report and
            report["total_devices"] > 0):
            logger.info("✓ Test 2 PASSED: Security report generation")
            self.test_results["passed"] += 1
        else:
            logger.error("✗ Test 2 FAILED: Security report generation")
            self.test_results["failed"] += 1
        self.test_results["total"] += 1
        
        # Test 3: Device filtering by security level
        critical_devices = self.identifier.get_devices_by_security_level(SecurityLevel.CRITICAL)
        high_devices = self.identifier.get_devices_by_security_level(SecurityLevel.HIGH)
        
        if len(critical_devices) > 0 and len(high_devices) > 0:
            logger.info("✓ Test 3 PASSED: Device filtering by security level")
            self.test_results["passed"] += 1
        else:
            logger.error("✗ Test 3 FAILED: Device filtering by security level")
            self.test_results["failed"] += 1
        self.test_results["total"] += 1
        
    def test_database_operations(self):
        """Test database operations"""
        logger.info("Testing Database Operations")
        logger.info("-" * 40)
        
        # Test 1: Add new device
        new_device = MICSDevice(
            mac_address="00:11:22:33:44:FF",
            device_type=DeviceType.RESEARCH_DEVICE,
            manufacturer=DeviceManufacturer.ELA,
            model="Test Device",
            serial_number="TEST123",
            firmware_version="1.0.0",
            security_level=SecurityLevel.MEDIUM,
            frequency_channels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            power_level=25.0,
            duty_cycle=0.001,
            last_seen=datetime.now(),
            first_seen=datetime.now(),
            communication_pattern={},
            security_features=["AES-128", "Authentication"],
            vulnerabilities=[],
            compliance_status={"fcc_part_95": True, "fda_approved": False}
        )
        
        self.identifier.add_device(new_device)
        retrieved_device = self.identifier.get_device("00:11:22:33:44:FF")
        
        if retrieved_device and retrieved_device.model == "Test Device":
            logger.info("✓ Test 1 PASSED: Add new device")
            self.test_results["passed"] += 1
        else:
            logger.error("✗ Test 1 FAILED: Add new device")
            self.test_results["failed"] += 1
        self.test_results["total"] += 1
        
        # Test 2: Update device
        updates = {
            "model": "Updated Test Device",
            "firmware_version": "1.1.0"
        }
        self.identifier.update_device("00:11:22:33:44:FF", updates)
        updated_device = self.identifier.get_device("00:11:22:33:44:FF")
        
        if (updated_device and 
            updated_device.model == "Updated Test Device" and
            updated_device.firmware_version == "1.1.0"):
            logger.info("✓ Test 2 PASSED: Update device")
            self.test_results["passed"] += 1
        else:
            logger.error("✗ Test 2 FAILED: Update device")
            self.test_results["failed"] += 1
        self.test_results["total"] += 1
        
        # Test 3: Export database
        export_filename = "test_export.json"
        self.identifier.export_database(export_filename)
        
        if os.path.exists(export_filename):
            logger.info("✓ Test 3 PASSED: Export database")
            self.test_results["passed"] += 1
            # Clean up
            os.remove(export_filename)
        else:
            logger.error("✗ Test 3 FAILED: Export database")
            self.test_results["failed"] += 1
        self.test_results["total"] += 1
        
    def test_compliance_checking(self):
        """Test compliance checking functionality"""
        logger.info("Testing Compliance Checking")
        logger.info("-" * 40)
        
        # Test 1: FCC compliance checking
        fcc_compliant_devices = []
        for device in self.identifier.device_database.values():
            if device.compliance_status.get("fcc_part_95", False):
                fcc_compliant_devices.append(device)
        
        if len(fcc_compliant_devices) > 0:
            logger.info(f"✓ Test 1 PASSED: FCC compliance checking ({len(fcc_compliant_devices)} devices)")
            self.test_results["passed"] += 1
        else:
            logger.error("✗ Test 1 FAILED: FCC compliance checking")
            self.test_results["failed"] += 1
        self.test_results["total"] += 1
        
        # Test 2: FDA approval checking
        fda_approved_devices = []
        for device in self.identifier.device_database.values():
            if device.compliance_status.get("fda_approved", False):
                fda_approved_devices.append(device)
        
        if len(fda_approved_devices) > 0:
            logger.info(f"✓ Test 2 PASSED: FDA approval checking ({len(fda_approved_devices)} devices)")
            self.test_results["passed"] += 1
        else:
            logger.error("✗ Test 2 FAILED: FDA approval checking")
            self.test_results["failed"] += 1
        self.test_results["total"] += 1
        
        # Test 3: HIPAA compliance checking
        hipaa_compliant_devices = []
        for device in self.identifier.device_database.values():
            if device.compliance_status.get("hipaa_compliant", False):
                hipaa_compliant_devices.append(device)
        
        if len(hipaa_compliant_devices) > 0:
            logger.info(f"✓ Test 3 PASSED: HIPAA compliance checking ({len(hipaa_compliant_devices)} devices)")
            self.test_results["passed"] += 1
        else:
            logger.error("✗ Test 3 FAILED: HIPAA compliance checking")
            self.test_results["failed"] += 1
        self.test_results["total"] += 1
        
    def test_error_handling(self):
        """Test error handling functionality"""
        logger.info("Testing Error Handling")
        logger.info("-" * 40)
        
        # Test 1: Invalid MAC address handling
        invalid_macs = [
            "invalid_mac",
            "00:11:22:33:44",  # Too short
            "00:11:22:33:44:55:66",  # Too long
            "GG:11:22:33:44:55",  # Invalid characters
        ]
        
        passed = 0
        for mac in invalid_macs:
            try:
                device = self.identifier.identify_device(mac)
                if device is None:  # Should return None for invalid MACs
                    passed += 1
            except Exception:
                passed += 1  # Exception is also acceptable
        
        if passed == len(invalid_macs):
            logger.info("✓ Test 1 PASSED: Invalid MAC address handling")
            self.test_results["passed"] += 1
        else:
            logger.error("✗ Test 1 FAILED: Invalid MAC address handling")
            self.test_results["failed"] += 1
        self.test_results["total"] += 1
        
        # Test 2: Database error handling
        try:
            # Try to access non-existent device
            device = self.identifier.get_device("FF:FF:FF:FF:FF:FF")
            if device is None:
                logger.info("✓ Test 2 PASSED: Non-existent device handling")
                self.test_results["passed"] += 1
            else:
                logger.error("✗ Test 2 FAILED: Non-existent device handling")
                self.test_results["failed"] += 1
        except Exception as e:
            logger.error(f"✗ Test 2 FAILED: Database error handling - {e}")
            self.test_results["failed"] += 1
        self.test_results["total"] += 1
        
    def test_performance(self):
        """Test performance characteristics"""
        logger.info("Testing Performance")
        logger.info("-" * 40)
        
        import time
        
        # Test 1: Device identification performance
        start_time = time.time()
        for i in range(100):
            mac = f"00:11:22:33:44:{i:02X}"
            self.identifier.identify_device(mac)
        end_time = time.time()
        
        identification_time = end_time - start_time
        if identification_time < 1.0:  # Should complete in less than 1 second
            logger.info(f"✓ Test 1 PASSED: Device identification performance ({identification_time:.3f}s)")
            self.test_results["passed"] += 1
        else:
            logger.error(f"✗ Test 1 FAILED: Device identification performance ({identification_time:.3f}s)")
            self.test_results["failed"] += 1
        self.test_results["total"] += 1
        
        # Test 2: Database query performance
        start_time = time.time()
        for i in range(50):
            self.identifier.get_devices_by_type(DeviceType.PACEMAKER)
            self.identifier.get_devices_by_manufacturer(DeviceManufacturer.MEDTRONIC)
            self.identifier.get_devices_by_security_level(SecurityLevel.HIGH)
        end_time = time.time()
        
        query_time = end_time - start_time
        if query_time < 0.5:  # Should complete in less than 0.5 seconds
            logger.info(f"✓ Test 2 PASSED: Database query performance ({query_time:.3f}s)")
            self.test_results["passed"] += 1
        else:
            logger.error(f"✗ Test 2 FAILED: Database query performance ({query_time:.3f}s)")
            self.test_results["failed"] += 1
        self.test_results["total"] += 1
        
    def print_test_summary(self):
        """Print test results summary"""
        logger.info("=" * 60)
        logger.info("TEST SUMMARY")
        logger.info("=" * 60)
        logger.info(f"Total Tests: {self.test_results['total']}")
        logger.info(f"Passed: {self.test_results['passed']}")
        logger.info(f"Failed: {self.test_results['failed']}")
        logger.info(f"Success Rate: {(self.test_results['passed'] / self.test_results['total'] * 100):.1f}%")
        
        if self.test_results['failed'] == 0:
            logger.info("🎉 ALL TESTS PASSED! 🎉")
        else:
            logger.warning(f"⚠️  {self.test_results['failed']} TESTS FAILED ⚠️")
        
        logger.info("=" * 60)

def demonstrate_system_capabilities():
    """Demonstrate system capabilities with real examples"""
    logger.info("MICS Device Identification System Demonstration")
    logger.info("=" * 60)
    
    identifier = MICSDeviceIdentifier()
    
    # Demonstrate device identification
    logger.info("1. Device Identification Examples:")
    test_devices = [
        "00:11:22:33:44:55",  # Medtronic pacemaker
        "00:11:22:33:44:66",  # Boston Scientific defibrillator
        "00:11:22:33:44:77",  # Medtronic cardiac monitor
        "00:11:22:33:44:88",  # Abbott neurostimulator
        "00:11:22:33:44:99",  # Medtronic deep brain stimulator
    ]
    
    for mac in test_devices:
        device = identifier.identify_device(mac)
        if device:
            logger.info(f"   {mac} -> {device.manufacturer.value} {device.model} ({device.device_type.value})")
    
    # Demonstrate security analysis
    logger.info("\n2. Security Analysis:")
    report = identifier.generate_security_report()
    logger.info(f"   Total devices: {report['total_devices']}")
    logger.info(f"   Critical security: {report['security_summary']['critical']}")
    logger.info(f"   High security: {report['security_summary']['high']}")
    logger.info(f"   Medium security: {report['security_summary']['medium']}")
    logger.info(f"   Low security: {report['security_summary']['low']}")
    
    # Demonstrate device filtering
    logger.info("\n3. Device Filtering Examples:")
    pacemakers = identifier.get_devices_by_type(DeviceType.PACEMAKER)
    logger.info(f"   Pacemakers: {len(pacemakers)} devices")
    
    medtronic_devices = identifier.get_devices_by_manufacturer(DeviceManufacturer.MEDTRONIC)
    logger.info(f"   Medtronic devices: {len(medtronic_devices)} devices")
    
    critical_devices = identifier.get_devices_by_security_level(SecurityLevel.CRITICAL)
    logger.info(f"   Critical security devices: {len(critical_devices)} devices")
    
    # Demonstrate compliance checking
    logger.info("\n4. Compliance Status:")
    fcc_compliant = sum(1 for device in identifier.device_database.values() 
                       if device.compliance_status.get("fcc_part_95", False))
    fda_approved = sum(1 for device in identifier.device_database.values() 
                      if device.compliance_status.get("fda_approved", False))
    hipaa_compliant = sum(1 for device in identifier.device_database.values() 
                         if device.compliance_status.get("hipaa_compliant", False))
    
    logger.info(f"   FCC Part 95 compliant: {fcc_compliant} devices")
    logger.info(f"   FDA approved: {fda_approved} devices")
    logger.info(f"   HIPAA compliant: {hipaa_compliant} devices")

if __name__ == "__main__":
    # Run demonstration
    demonstrate_system_capabilities()
    
    print("\n" + "=" * 60)
    
    # Run test suite
    tester = MICSIdentificationTester()
    tester.run_all_tests()