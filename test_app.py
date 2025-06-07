import unittest
import requests
import time
import subprocess
import threading
from pycaret.regression import *
import pandas as pd
import numpy as np

class TestPatientChargesApp(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Setup test environment"""
        print("Setting up tests...")
        
    def test_model_loading(self):
        """Test that the model can be loaded successfully"""
        try:
            model = load_model('deployment_28042020')
            self.assertIsNotNone(model)
            print("✅ Model loading test passed")
        except Exception as e:
            self.fail(f"Model loading failed: {str(e)}")
    
    def test_model_prediction(self):
        """Test that the model can make predictions"""
        try:
            model = load_model('deployment_28042020')
            cols = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']
            
            # Test data
            test_data = pd.DataFrame([[39, 'female', 27.9, 0, 'yes', 'southeast']], 
                                   columns=cols)
            
            prediction = predict_model(model, data=test_data, round=0)
            
            # Check that prediction is a DataFrame with expected columns
            self.assertIsInstance(prediction, pd.DataFrame)
            self.assertIn('prediction_label', prediction.columns)
            
            # Check that prediction value is reasonable (positive number)
            pred_value = prediction.prediction_label[0]
            self.assertGreater(pred_value, 0)
            self.assertLess(pred_value, 100000)  # Reasonable upper bound
            
            print(f"✅ Model prediction test passed. Predicted: ${pred_value:.2f}")
            
        except Exception as e:
            self.fail(f"Model prediction failed: {str(e)}")
    
    def test_data_validation(self):
        """Test that the model handles different input types correctly"""
        try:
            model = load_model('deployment_28042020')
            cols = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']
            
            # Test different scenarios
            test_cases = [
                [25, 'male', 22.5, 1, 'no', 'northwest'],
                [45, 'female', 30.0, 2, 'yes', 'southwest'],
                [60, 'male', 25.8, 0, 'no', 'northeast']
            ]
            
            for i, test_case in enumerate(test_cases):
                test_data = pd.DataFrame([test_case], columns=cols)
                prediction = predict_model(model, data=test_data, round=0)
                pred_value = prediction.prediction_label[0]
                
                self.assertGreater(pred_value, 0)
                print(f"✅ Test case {i+1}: Predicted ${pred_value:.2f}")
                
        except Exception as e:
            self.fail(f"Data validation test failed: {str(e)}")
    
    def test_requirements_file(self):
        """Test that requirements.txt exists and has expected dependencies"""
        import os
        
        # Check if requirements.txt exists
        self.assertTrue(os.path.exists('requirements.txt'))
        
        # Read and check content
        with open('requirements.txt', 'r') as f:
            content = f.read()
            
        expected_packages = ['flask', 'pycaret', 'pandas', 'numpy', 'scikit-learn']
        
        for package in expected_packages:
            self.assertIn(package, content.lower())
            
        print("✅ Requirements file validation passed")
    
    def test_dockerfile_exists(self):
        """Test that Dockerfile exists and has basic structure"""
        import os
        
        self.assertTrue(os.path.exists('Dockerfile'))
        
        with open('Dockerfile', 'r') as f:
            content = f.read()
            
        # Check for essential Dockerfile commands
        self.assertIn('FROM', content)
        self.assertIn('WORKDIR', content)
        self.assertIn('COPY', content)
        self.assertIn('RUN', content)
        self.assertIn('CMD', content)
        
        print("✅ Dockerfile validation passed")

if __name__ == '__main__':
    unittest.main(verbosity=2) 