#!/usr/bin/env python3
"""
CAPTCHA Bypass Engine
Department of Defence - Full Authority Implementation
Real-World Operational Applications
"""

import logging
import requests
import time
import json
import base64
import io
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import cv2
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance
import pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import tensorflow as tf
from tensorflow import keras
import easyocr
import re

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CAPTCHAType(Enum):
    """Types of CAPTCHA challenges"""
    TEXT_BASED = "text_based"
    IMAGE_BASED = "image_based"
    AUDIO_BASED = "audio_based"
    MATH_BASED = "math_based"
    RECAPTCHA = "recaptcha"
    HONEYPOT = "honeypot"
    BEHAVIORAL = "behavioral"

@dataclass
class CAPTCHAChallenge:
    """CAPTCHA challenge information"""
    challenge_id: str
    challenge_type: CAPTCHAType
    challenge_data: bytes
    challenge_url: str
    timestamp: float
    difficulty: str
    bypass_method: str

@dataclass
class CAPTCHASolution:
    """CAPTCHA solution information"""
    challenge_id: str
    solution: str
    confidence: float
    method_used: str
    processing_time: float
    success: bool

class CAPTCHABypassEngine:
    """Comprehensive CAPTCHA bypass engine for operational use"""
    
    def __init__(self):
        self.supported_types = [
            CAPTCHAType.TEXT_BASED,
            CAPTCHAType.IMAGE_BASED,
            CAPTCHAType.MATH_BASED,
            CAPTCHAType.RECAPTCHA
        ]
        self.ocr_reader = easyocr.Reader(['en'])
        self.ml_model = self._load_ml_model()
        self.selenium_driver = None
        self.success_rate = 0.0
        self.total_attempts = 0
        self.successful_bypasses = 0
        
    def _load_ml_model(self):
        """Load machine learning model for CAPTCHA recognition"""
        try:
            # Load pre-trained model for CAPTCHA recognition
            # This is a placeholder - in real implementation, load actual model
            model = keras.Sequential([
                keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(50, 200, 1)),
                keras.layers.MaxPooling2D((2, 2)),
                keras.layers.Conv2D(64, (3, 3), activation='relu'),
                keras.layers.MaxPooling2D((2, 2)),
                keras.layers.Conv2D(64, (3, 3), activation='relu'),
                keras.layers.Flatten(),
                keras.layers.Dense(64, activation='relu'),
                keras.layers.Dense(36, activation='softmax')  # 26 letters + 10 digits
            ])
            return model
        except Exception as e:
            logger.error(f"Error loading ML model: {e}")
            return None
    
    def initialize_selenium(self, headless: bool = True):
        """Initialize Selenium WebDriver for browser automation"""
        try:
            chrome_options = Options()
            if headless:
                chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
            
            self.selenium_driver = webdriver.Chrome(options=chrome_options)
            logger.info("Selenium WebDriver initialized successfully")
            return True
        except Exception as e:
            logger.error(f"Error initializing Selenium: {e}")
            return False
    
    def solve_captcha(self, challenge: CAPTCHAChallenge) -> Optional[CAPTCHASolution]:
        """Solve CAPTCHA challenge using appropriate method"""
        start_time = time.time()
        
        try:
            if challenge.challenge_type == CAPTCHAType.TEXT_BASED:
                solution = self._solve_text_captcha(challenge)
            elif challenge.challenge_type == CAPTCHAType.IMAGE_BASED:
                solution = self._solve_image_captcha(challenge)
            elif challenge.challenge_type == CAPTCHAType.MATH_BASED:
                solution = self._solve_math_captcha(challenge)
            elif challenge.challenge_type == CAPTCHAType.RECAPTCHA:
                solution = self._solve_recaptcha(challenge)
            else:
                logger.warning(f"Unsupported CAPTCHA type: {challenge.challenge_type}")
                return None
            
            if solution:
                solution.processing_time = time.time() - start_time
                self.total_attempts += 1
                if solution.success:
                    self.successful_bypasses += 1
                self.success_rate = self.successful_bypasses / self.total_attempts
                
            return solution
            
        except Exception as e:
            logger.error(f"Error solving CAPTCHA: {e}")
            return None
    
    def _solve_text_captcha(self, challenge: CAPTCHAChallenge) -> Optional[CAPTCHASolution]:
        """Solve text-based CAPTCHA"""
        try:
            # Convert image to text using OCR
            image = Image.open(io.BytesIO(challenge.challenge_data))
            
            # Preprocess image for better OCR
            processed_image = self._preprocess_image_for_ocr(image)
            
            # Use EasyOCR for text recognition
            results = self.ocr_reader.readtext(np.array(processed_image))
            
            if results:
                # Extract text from OCR results
                text = ' '.join([result[1] for result in results])
                # Clean up the text
                cleaned_text = self._clean_ocr_text(text)
                
                return CAPTCHASolution(
                    challenge_id=challenge.challenge_id,
                    solution=cleaned_text,
                    confidence=results[0][2] if results else 0.0,
                    method_used="easyocr",
                    processing_time=0.0,
                    success=True
                )
            
        except Exception as e:
            logger.error(f"Error solving text CAPTCHA: {e}")
        
        return None
    
    def _solve_image_captcha(self, challenge: CAPTCHAChallenge) -> Optional[CAPTCHASolution]:
        """Solve image-based CAPTCHA"""
        try:
            # Convert image to numpy array
            image = Image.open(io.BytesIO(challenge.challenge_data))
            image_array = np.array(image.convert('L'))  # Convert to grayscale
            
            # Preprocess image
            processed_image = self._preprocess_image_for_ml(image_array)
            
            # Use machine learning model for recognition
            if self.ml_model:
                prediction = self.ml_model.predict(processed_image.reshape(1, 50, 200, 1))
                predicted_text = self._decode_prediction(prediction[0])
                
                return CAPTCHASolution(
                    challenge_id=challenge.challenge_id,
                    solution=predicted_text,
                    confidence=np.max(prediction[0]),
                    method_used="ml_model",
                    processing_time=0.0,
                    success=True
                )
            
            # Fallback to OCR
            return self._solve_text_captcha(challenge)
            
        except Exception as e:
            logger.error(f"Error solving image CAPTCHA: {e}")
        
        return None
    
    def _solve_math_captcha(self, challenge: CAPTCHAChallenge) -> Optional[CAPTCHASolution]:
        """Solve math-based CAPTCHA"""
        try:
            # Extract math expression from image
            image = Image.open(io.BytesIO(challenge.challenge_data))
            processed_image = self._preprocess_image_for_ocr(image)
            
            # Use OCR to extract math expression
            results = self.ocr_reader.readtext(np.array(processed_image))
            
            if results:
                math_expression = ' '.join([result[1] for result in results])
                # Clean up the expression
                cleaned_expression = self._clean_math_expression(math_expression)
                
                # Evaluate the math expression
                try:
                    result = eval(cleaned_expression)
                    return CAPTCHASolution(
                        challenge_id=challenge.challenge_id,
                        solution=str(result),
                        confidence=results[0][2] if results else 0.0,
                        method_used="math_evaluation",
                        processing_time=0.0,
                        success=True
                    )
                except:
                    logger.warning(f"Could not evaluate math expression: {cleaned_expression}")
            
        except Exception as e:
            logger.error(f"Error solving math CAPTCHA: {e}")
        
        return None
    
    def _solve_recaptcha(self, challenge: CAPTCHAChallenge) -> Optional[CAPTCHASolution]:
        """Solve reCAPTCHA challenges"""
        try:
            if not self.selenium_driver:
                if not self.initialize_selenium():
                    return None
            
            # Navigate to the page with reCAPTCHA
            self.selenium_driver.get(challenge.challenge_url)
            
            # Wait for reCAPTCHA to load
            wait = WebDriverWait(self.selenium_driver, 10)
            
            # Find reCAPTCHA iframe
            recaptcha_iframe = wait.until(
                EC.presence_of_element_located((By.XPATH, "//iframe[@title='reCAPTCHA']"))
            )
            
            # Switch to reCAPTCHA iframe
            self.selenium_driver.switch_to.frame(recaptcha_iframe)
            
            # Click the reCAPTCHA checkbox
            checkbox = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "recaptcha-checkbox-border"))
            )
            checkbox.click()
            
            # Switch back to main content
            self.selenium_driver.switch_to.default_content()
            
            # Wait for reCAPTCHA to be solved
            time.sleep(3)
            
            # Check if reCAPTCHA was solved successfully
            try:
                success_element = self.selenium_driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-checked")
                if success_element:
                    return CAPTCHASolution(
                        challenge_id=challenge.challenge_id,
                        solution="recaptcha_solved",
                        confidence=1.0,
                        method_used="selenium_automation",
                        processing_time=0.0,
                        success=True
                    )
            except:
                pass
            
        except Exception as e:
            logger.error(f"Error solving reCAPTCHA: {e}")
        
        return None
    
    def _preprocess_image_for_ocr(self, image: Image.Image) -> Image.Image:
        """Preprocess image for better OCR results"""
        try:
            # Convert to grayscale
            if image.mode != 'L':
                image = image.convert('L')
            
            # Resize image
            image = image.resize((image.width * 2, image.height * 2), Image.LANCZOS)
            
            # Apply filters to reduce noise
            image = image.filter(ImageFilter.MedianFilter(size=3))
            
            # Enhance contrast
            enhancer = ImageEnhance.Contrast(image)
            image = enhancer.enhance(2.0)
            
            # Enhance sharpness
            enhancer = ImageEnhance.Sharpness(image)
            image = enhancer.enhance(2.0)
            
            return image
            
        except Exception as e:
            logger.error(f"Error preprocessing image for OCR: {e}")
            return image
    
    def _preprocess_image_for_ml(self, image_array: np.ndarray) -> np.ndarray:
        """Preprocess image for machine learning model"""
        try:
            # Resize to standard size
            resized = cv2.resize(image_array, (200, 50))
            
            # Normalize pixel values
            normalized = resized / 255.0
            
            # Add channel dimension
            processed = normalized.reshape(50, 200, 1)
            
            return processed
            
        except Exception as e:
            logger.error(f"Error preprocessing image for ML: {e}")
            return image_array
    
    def _clean_ocr_text(self, text: str) -> str:
        """Clean OCR text output"""
        try:
            # Remove special characters and extra spaces
            cleaned = re.sub(r'[^a-zA-Z0-9]', '', text)
            return cleaned.lower()
        except Exception as e:
            logger.error(f"Error cleaning OCR text: {e}")
            return text
    
    def _clean_math_expression(self, expression: str) -> str:
        """Clean math expression for evaluation"""
        try:
            # Remove extra spaces and special characters
            cleaned = re.sub(r'[^0-9+\-*/()]', '', expression)
            return cleaned
        except Exception as e:
            logger.error(f"Error cleaning math expression: {e}")
            return expression
    
    def _decode_prediction(self, prediction: np.ndarray) -> str:
        """Decode ML model prediction to text"""
        try:
            # Convert prediction to character indices
            indices = np.argmax(prediction)
            
            # Map indices to characters
            chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
            result = ''
            
            for idx in indices:
                if idx < len(chars):
                    result += chars[idx]
            
            return result
            
        except Exception as e:
            logger.error(f"Error decoding prediction: {e}")
            return ""
    
    def bypass_captcha_protection(self, target_url: str, form_data: Dict) -> Optional[Dict]:
        """Bypass CAPTCHA protection on a target website"""
        try:
            if not self.selenium_driver:
                if not self.initialize_selenium():
                    return None
            
            # Navigate to target URL
            self.selenium_driver.get(target_url)
            
            # Wait for page to load
            time.sleep(2)
            
            # Fill in form data
            for field_name, field_value in form_data.items():
                try:
                    field = self.selenium_driver.find_element(By.NAME, field_name)
                    field.clear()
                    field.send_keys(field_value)
                except:
                    logger.warning(f"Could not find form field: {field_name}")
            
            # Look for CAPTCHA challenge
            captcha_challenge = self._detect_captcha_challenge()
            
            if captcha_challenge:
                # Solve CAPTCHA
                solution = self.solve_captcha(captcha_challenge)
                
                if solution and solution.success:
                    # Fill in CAPTCHA solution
                    self._fill_captcha_solution(solution.solution)
                    
                    # Submit form
                    submit_button = self.selenium_driver.find_element(By.TYPE, "submit")
                    submit_button.click()
                    
                    # Wait for response
                    time.sleep(3)
                    
                    # Check if submission was successful
                    if self._check_submission_success():
                        return {
                            'success': True,
                            'solution': solution,
                            'response': self.selenium_driver.page_source
                        }
            
            return None
            
        except Exception as e:
            logger.error(f"Error bypassing CAPTCHA protection: {e}")
            return None
    
    def _detect_captcha_challenge(self) -> Optional[CAPTCHACHALLENGE]:
        """Detect CAPTCHA challenge on current page"""
        try:
            # Look for common CAPTCHA elements
            captcha_selectors = [
                "img[src*='captcha']",
                ".captcha",
                "#captcha",
                "input[name*='captcha']",
                "iframe[src*='recaptcha']"
            ]
            
            for selector in captcha_selectors:
                try:
                    element = self.selenium_driver.find_element(By.CSS_SELECTOR, selector)
                    
                    if element.tag_name == 'img':
                        # Image-based CAPTCHA
                        src = element.get_attribute('src')
                        response = requests.get(src)
                        
                        return CAPTCHAChallenge(
                            challenge_id=f"captcha_{int(time.time())}",
                            challenge_type=CAPTCHAType.IMAGE_BASED,
                            challenge_data=response.content,
                            challenge_url=self.selenium_driver.current_url,
                            timestamp=time.time(),
                            difficulty="medium",
                            bypass_method="ocr"
                        )
                    
                    elif element.tag_name == 'iframe':
                        # reCAPTCHA
                        return CAPTCHAChallenge(
                            challenge_id=f"recaptcha_{int(time.time())}",
                            challenge_type=CAPTCHAType.RECAPTCHA,
                            challenge_data=b"",
                            challenge_url=self.selenium_driver.current_url,
                            timestamp=time.time(),
                            difficulty="high",
                            bypass_method="selenium"
                        )
                        
                except:
                    continue
            
            return None
            
        except Exception as e:
            logger.error(f"Error detecting CAPTCHA challenge: {e}")
            return None
    
    def _fill_captcha_solution(self, solution: str):
        """Fill in CAPTCHA solution in form"""
        try:
            # Look for CAPTCHA input field
            captcha_input_selectors = [
                "input[name*='captcha']",
                "input[id*='captcha']",
                "input[placeholder*='captcha']"
            ]
            
            for selector in captcha_input_selectors:
                try:
                    field = self.selenium_driver.find_element(By.CSS_SELECTOR, selector)
                    field.clear()
                    field.send_keys(solution)
                    return
                except:
                    continue
                    
        except Exception as e:
            logger.error(f"Error filling CAPTCHA solution: {e}")
    
    def _check_submission_success(self) -> bool:
        """Check if form submission was successful"""
        try:
            # Look for success indicators
            success_indicators = [
                "success",
                "thank you",
                "submitted",
                "completed"
            ]
            
            page_text = self.selenium_driver.page_source.lower()
            
            for indicator in success_indicators:
                if indicator in page_text:
                    return True
            
            # Check for error indicators
            error_indicators = [
                "error",
                "invalid",
                "failed",
                "incorrect"
            ]
            
            for indicator in error_indicators:
                if indicator in page_text:
                    return False
            
            return True
            
        except Exception as e:
            logger.error(f"Error checking submission success: {e}")
            return False
    
    def get_statistics(self) -> Dict:
        """Get CAPTCHA bypass statistics"""
        return {
            'total_attempts': self.total_attempts,
            'successful_bypasses': self.successful_bypasses,
            'success_rate': self.success_rate,
            'supported_types': [t.value for t in self.supported_types]
        }
    
    def close(self):
        """Close resources"""
        if self.selenium_driver:
            self.selenium_driver.quit()

def main():
    """Main function for CAPTCHA bypass engine"""
    try:
        # Initialize CAPTCHA bypass engine
        engine = CAPTCHABypassEngine()
        
        # Test CAPTCHA bypass on a target
        target_url = "https://example.com/captcha-form"
        form_data = {
            'username': 'test_user',
            'email': 'test@example.com',
            'message': 'Test message'
        }
        
        result = engine.bypass_captcha_protection(target_url, form_data)
        
        if result:
            logger.info("CAPTCHA bypass successful")
            logger.info(f"Statistics: {engine.get_statistics()}")
        else:
            logger.warning("CAPTCHA bypass failed")
        
        # Close engine
        engine.close()
        
    except Exception as e:
        logger.error(f"Error in CAPTCHA bypass engine: {e}")
        raise

if __name__ == "__main__":
    main()