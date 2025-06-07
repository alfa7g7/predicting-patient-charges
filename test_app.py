import unittest
import os
import pickle
import subprocess
import sys

class TestPatientChargesApp(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Setup test environment"""
        print("Setting up tests...")
    
    def test_model_file_exists(self):
        """Test that the model file exists"""
        model_path = 'models/deployment_28042020.pkl'
        self.assertTrue(os.path.exists(model_path), f"Model file {model_path} not found")
        print("✅ Model file exists")
    
    def test_model_file_loadable(self):
        """Test that the model file can be loaded with pickle"""
        try:
            with open('models/deployment_28042020.pkl', 'rb') as f:
                model = pickle.load(f)
            self.assertIsNotNone(model)
            print("✅ Model file is loadable with pickle")
        except Exception as e:
            self.fail(f"Model file loading failed: {str(e)}")
    
    def test_python_imports(self):
        """Test that required Python packages can be imported"""
        required_packages = [
            'flask',
            'pandas', 
            'numpy',
            'sklearn',
            'pycaret'
        ]
        
        for package in required_packages:
            try:
                __import__(package)
                print(f"✅ {package} import successful")
            except ImportError:
                self.fail(f"Failed to import {package}")
    
    def test_app_file_exists(self):
        """Test that app.py exists and has basic Flask structure"""
        self.assertTrue(os.path.exists('app.py'))
        
        with open('app.py', 'r') as f:
            content = f.read()
            
        # Check for essential Flask components
        self.assertIn('Flask', content)
        self.assertIn('@app.route', content)
        self.assertIn('load_model', content)
        
        print("✅ Flask app file validation passed")
    
    def test_train_model_file_exists(self):
        """Test that train_model.py exists"""
        self.assertTrue(os.path.exists('train_model.py'))
        
        with open('train_model.py', 'r') as f:
            content = f.read()
            
        # Check for essential training components
        self.assertIn('pycaret', content)
        self.assertIn('save_model', content)
        
        print("✅ Training script validation passed")
    
    def test_requirements_file(self):
        """Test that requirements.txt exists and has expected dependencies"""
        self.assertTrue(os.path.exists('requirements.txt'))
        
        with open('requirements.txt', 'r') as f:
            content = f.read()
            
        expected_packages = ['flask', 'pycaret', 'pandas', 'numpy', 'scikit-learn']
        
        for package in expected_packages:
            self.assertIn(package, content.lower())
            
        print("✅ Requirements file validation passed")
    
    def test_dockerfile_exists(self):
        """Test that Dockerfile exists and has basic structure"""
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
    
    def test_templates_directory(self):
        """Test that templates directory exists with home.html"""
        self.assertTrue(os.path.exists('templates'))
        self.assertTrue(os.path.exists('templates/home.html'))
        print("✅ Templates directory validation passed")
    
    def test_models_directory(self):
        """Test that models directory exists with deployment model"""
        self.assertTrue(os.path.exists('models'))
        self.assertTrue(os.path.exists('models/deployment_28042020.pkl'))
        print("✅ Models directory validation passed")

if __name__ == '__main__':
    unittest.main(verbosity=2) 