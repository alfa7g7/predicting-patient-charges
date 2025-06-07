# 🏥 Patient Charges Prediction - MLOps Pipeline

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-20.0+-blue.svg)](https://www.docker.com/)
[![PyCaret](https://img.shields.io/badge/PyCaret-3.0+-orange.svg)](https://pycaret.org/)
[![Azure](https://img.shields.io/badge/Azure-Live_Demo-blue.svg)](https://patient-charges-webapp-dvbucjebfeb5enhj.eastus2-01.azurewebsites.net)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 Project Overview

An end-to-end Machine Learning Operations (MLOps) pipeline for predicting patient insurance charges based on demographic and health metrics. This project demonstrates a complete MLOps workflow from model development to production deployment using modern DevOps practices.

### 🏆 Business Problem

An insurance company wants to improve its cash flow forecasting by better predicting patient charges using demographic and basic patient health-risk metrics at the time of hospitalization.

### 🔍 Solution

A web application where demographic and health information is entered into a web-based form, which outputs a predicted charge amount in real-time using a trained machine learning pipeline.

## 📊 Dataset

**Source**: [Medical Cost Personal Dataset](https://www.kaggle.com/mirichoi0218/insurance)

**Features**:
- `age`: Age of primary beneficiary
- `sex`: Insurance contractor gender (male/female)
- `bmi`: Body mass index (kg/m²)
- `children`: Number of children covered by health insurance
- `smoker`: Smoking status (yes/no)
- `region`: Beneficiary's residential area (northeast, northwest, southeast, southwest)

**Target**: `charges` - Individual medical costs billed by health insurance

## 🏗️ Architecture & Technology Stack

### **Machine Learning**
- **PyCaret**: AutoML library for model training and pipeline creation
- **Scikit-learn**: Machine learning algorithms and preprocessing
- **Pandas & NumPy**: Data manipulation and numerical computing

### **Web Application**
- **Flask**: Lightweight WSGI web application framework
- **HTML/CSS**: Responsive frontend with modern UI design
- **Jinja2**: Template engine for dynamic content rendering

### **DevOps & Deployment**
- **Docker**: Containerization for consistent deployment
- **Git**: Version control and collaboration
- **Azure Container Registry**: Cloud container hosting (ready)

### **MLOps Pipeline Features**
- ✅ Automated data preprocessing
- ✅ Feature engineering (polynomial, trigonometric features)
- ✅ Model training with cross-validation
- ✅ Pipeline serialization for deployment
- ✅ RESTful API for predictions
- ✅ Web interface for user interaction
- ✅ Containerized deployment
- ✅ Cloud-ready architecture

## 📁 Project Structure

```
predicting-patient-charges/
│
├── 📄 README.md                    # Project documentation
├── 📄 requirements.txt             # Python dependencies
├── 📄 Dockerfile                   # Container configuration
├── 📄 .gitignore                   # Git ignore rules
│
├── 🐍 train_model.py               # Model training script
├── 🐍 app.py                       # Flask web application
│
├── 📁 templates/                   # HTML templates
│   └── 🌐 home.html               # Web interface
│
└── 📁 models/                      # Trained model artifacts (generated)
    └── 🤖 deployment_28042020.pkl # Serialized ML pipeline
```

## 🚀 Quick Start - Two Options Available

Choose one of the following options to try the application:

### 🌐 Option 1: Try the Live Demo (Recommended)

**No installation required!** Access the deployed application directly:

**🔗 Live Demo**: **https://patient-charges-webapp-dvbucjebfeb5enhj.eastus2-01.azurewebsites.net**

Simply visit the link above and start making predictions immediately. The application is deployed on Azure Web App and ready to use.

### 🛠️ Option 2: Run Locally (For Development)

#### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Docker (optional, for containerization)

#### 1. Clone the Repository

```bash
git clone https://github.com/alfa7g7/predicting-patient-charges.git
cd predicting-patient-charges
```

#### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 3. Train the Model

```bash
python train_model.py
```

This will:
- Download the insurance dataset
- Perform feature engineering (normalization, polynomial features, etc.)
- Train a linear regression model
- Save the complete pipeline as `deployment_28042020.pkl`

#### 4. Run the Web Application

```bash
python app.py
```

Navigate to `http://localhost:5000` in your web browser to access the prediction interface.

## 🌐 Web Application Usage

### Main Interface
The web application provides an intuitive form where users can input:

1. **Age**: Patient's age (18-100 years)
2. **Gender**: Male or Female
3. **BMI**: Body Mass Index (10.0-50.0)
4. **Children**: Number of dependents (0-10)
5. **Smoking Status**: Yes or No
6. **Region**: Northeast, Northwest, Southeast, or Southwest

### 📋 Example Use Cases

Test the application with these realistic examples that demonstrate different risk profiles:

#### **Case 1: Low Risk Profile**
- **Age**: 25
- **Gender**: Male
- **BMI**: 22.5
- **Children**: 0
- **Smoker**: No
- **Region**: Southeast
- **Expected Result**: ~$4,435 (Low cost due to young age, healthy BMI, non-smoker)

#### **Case 2: High Risk Profile**
- **Age**: 45
- **Gender**: Female
- **BMI**: 28.0
- **Children**: 2
- **Smoker**: Yes
- **Region**: Northeast
- **Expected Result**: ~$31,528 (High cost due to smoking, elevated BMI, older age)

#### **Case 3: Medium Risk Profile**
- **Age**: 35
- **Gender**: Male
- **BMI**: 25.5
- **Children**: 1
- **Smoker**: No
- **Region**: Northwest
- **Expected Result**: ~$5,977 (Medium cost - balanced risk factors)

### API Endpoints

#### 1. Web Interface
- **URL**: `GET /`
- **Description**: Renders the main prediction form
- **Response**: HTML page with input form

#### 2. Web Prediction
- **URL**: `POST /predict`
- **Description**: Processes form data and returns prediction
- **Input**: Form data
- **Response**: HTML page with prediction result

#### 3. API Prediction
- **URL**: `POST /predict_api`
- **Description**: JSON API for programmatic access
- **Input**: JSON with patient data
- **Response**: JSON with prediction

**Example API Request**:
```bash
curl -X POST https://patient-charges-webapp-dvbucjebfeb5enhj.eastus2-01.azurewebsites.net/predict_api \
  -H "Content-Type: application/json" \
  -d '{
    "age": 30,
    "sex": "male",
    "bmi": 25.0,
    "children": 2,
    "smoker": "no",
    "region": "southwest"
  }'
```

**Example API Response**:
```json
{
  "prediction": 4500.25
}
```

## 🐳 Docker Deployment

### Build Docker Image

```bash
docker build -t patient-charges-predictor .
```

### Run Container Locally

```bash
docker run -d -p 5000:5000 patient-charges-predictor
```

The application will be available at `http://localhost:5000`

### Docker Commands Reference

```bash
# List all images
docker images

# List running containers
docker ps

# Stop a container
docker stop <container_id>

# Remove a container
docker rm <container_id>

# Remove an image
docker rmi <image_name>
```

## ☁️ Cloud Deployment (Azure) - ✅ Successfully Deployed

### 🚀 Live Production Deployment

The application is **currently deployed and running** on Azure Web App:

- **🌐 Production URL**: https://patient-charges-webapp-dvbucjebfeb5enhj.eastus2-01.azurewebsites.net
- **🐳 Container Registry**: `patientchargesacr.azurecr.io`
- **📦 Image**: `patientchargesacr.azurecr.io/patient-charges-app:latest`
- **🏗️ Resource Group**: `patient-charges-rg`
- **💻 App Service Plan**: Basic B1 (Linux)

### Deployment Architecture

```
GitHub Repository
        ↓
    Docker Build
        ↓
Azure Container Registry (ACR)
        ↓
   Azure Web App
        ↓
   Production URL
```

### Azure Resources Created

1. **Container Registry**: `patientchargesacr.azurecr.io`
2. **Resource Group**: `patient-charges-rg`
3. **Web App**: `patient-charges-webapp`
4. **App Service Plan**: `patient-charges-plan` (Basic B1)

### Deployment Commands Used

1. **Create Azure Container Registry**:
```bash
az acr create --resource-group patient-charges-rg \
  --name patientchargesacr --sku Basic
```

2. **Build and Push to ACR**:
```bash
# Build image with ACR tag
docker build -t patientchargesacr.azurecr.io/patient-charges-app:latest .

# Login to ACR
az acr login --name patientchargesacr

# Push image
docker push patientchargesacr.azurecr.io/patient-charges-app:latest
```

3. **Deploy to Azure Web App**:
```bash
az webapp create --resource-group patient-charges-rg \
  --plan patient-charges-plan --name patient-charges-webapp \
  --deployment-container-image-name patientchargesacr.azurecr.io/patient-charges-app:latest
```

### 📊 Live Application Features

✅ **Real-time predictions** - Get insurance charge predictions instantly  
✅ **Responsive design** - Works on desktop and mobile devices  
✅ **Scalable architecture** - Auto-scaling based on demand  
✅ **High availability** - 99.9% uptime SLA  
✅ **SSL encryption** - Secure HTTPS connection  

## 🔄 CI/CD Pipeline

This project includes a comprehensive CI/CD pipeline using **GitHub Actions** that automatically validates, builds, and tests the application.

### Pipeline Features

- **🧪 Automated Testing**: Runs unit tests and model validation
- **🐳 Docker Build**: Builds and tests Docker containers
- **🔒 Security Scanning**: Vulnerability scanning with Trivy
- **📊 Test Coverage**: Comprehensive ML model and application testing
- **🚀 Deployment Simulation**: Production-ready deployment workflow

### Pipeline Stages

1. **Test Stage**
   - Model loading and prediction validation
   - Data validation with multiple test cases
   - Requirements and Dockerfile validation
   - Python 3.10 compatibility testing

2. **Docker Build Stage**
   - Multi-platform Docker image building
   - Container health checks
   - Application responsiveness testing

3. **Security Stage**
   - Vulnerability scanning
   - Security compliance checks

4. **Deploy Stage**
   - Production deployment simulation
   - Deployment summary generation

### Running Tests Locally

```bash
# Install test dependencies
pip install pytest requests

# Run all tests
python test_app.py

# Run with pytest
pytest test_app.py -v
```

### GitHub Actions Triggers

The pipeline automatically runs on:
- Push to main branch
- Pull requests to main branch
- Manual workflow dispatch

[![CI/CD Pipeline](https://github.com/alfa7g7/predicting-patient-charges/actions/workflows/ci-cd-pipeline.yml/badge.svg)](https://github.com/alfa7g7/predicting-patient-charges/actions/workflows/ci-cd-pipeline.yml)

## 🔬 Model Details

### Algorithm
- **Linear Regression** with advanced feature engineering

### Feature Engineering
- **Normalization**: Standardized numerical features
- **Polynomial Features**: Generated interaction terms
- **Trigonometric Features**: Sine/cosine transformations
- **Feature Interaction**: Cross-feature combinations
- **Binning**: Categorical binning for age and BMI

### Model Performance
The model uses PyCaret's automated machine learning capabilities with:
- Cross-validation for robust evaluation
- Automated hyperparameter tuning
- Feature selection optimization
- Pipeline serialization for deployment

### Training Configuration
```python
setup(insurance, target='charges', session_id=123,
      normalize=True,
      polynomial_features=True, 
      trigonometry_features=True,
      feature_interaction=True,
      bin_numeric_features=['age', 'bmi'])
```

## 🛠️ Development

### Running in Development Mode

```bash
# Enable Flask debug mode
export FLASK_ENV=development
python app.py
```

### Project Dependencies

```
flask>=2.0.0
pycaret>=3.0.0
pandas>=1.3.0
numpy>=1.21.0
scikit-learn>=1.0.0
```

### Adding New Features

1. **Model Updates**: Modify `train_model.py`
2. **API Changes**: Update routes in `app.py`
3. **UI Changes**: Edit `templates/home.html`
4. **Dependencies**: Update `requirements.txt`

## 📈 Recent Implementations & Future Enhancements

### ✅ **Recently Implemented (2024)**
- [x] **Azure Cloud Deployment** - Live production application
- [x] **Azure Container Registry** - Centralized container management
- [x] **GitHub Actions CI/CD** - Automated testing and deployment pipeline
- [x] **Docker Containerization** - Consistent deployment across environments
- [x] **Comprehensive Testing Suite** - Model validation and application testing

### 🔄 MLOps Improvements (Next Steps)
- [ ] Automated model retraining pipeline
- [ ] Model performance monitoring with MLflow
- [ ] A/B testing framework
- [ ] Data drift detection with Evidently AI
- [ ] Model versioning and rollback capabilities

### 🔧 Technical Enhancements
- [ ] Database integration for prediction logging
- [ ] User authentication and authorization
- [ ] Rate limiting for API endpoints
- [ ] Comprehensive logging and monitoring
- [ ] Unit and integration tests

### 🎨 UI/UX Improvements
- [ ] Mobile-responsive design
- [ ] Real-time prediction updates
- [ ] Data visualization dashboards
- [ ] Export prediction results
- [ ] Historical prediction tracking

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📋 Testing

### Manual Testing
1. Run the application locally
2. Test various input combinations
3. Verify API responses
4. Check Docker container functionality

### Automated Testing (Future)
```bash
# Run unit tests
python -m pytest tests/

# Run integration tests
python -m pytest tests/integration/

# Run performance tests
python -m pytest tests/performance/
```

## 🐛 Troubleshooting

### Common Issues

1. **Module Not Found**: Ensure all dependencies are installed
   ```bash
   pip install -r requirements.txt
   ```

2. **Port Already in Use**: Change the port in `app.py`
   ```python
   app.run(debug=True, port=5001)
   ```

3. **Model File Missing**: Run the training script first
   ```bash
   python train_model.py
   ```

4. **Docker Build Fails**: Check Dockerfile syntax and dependencies

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [DataCamp](https://www.datacamp.com/) for the comprehensive MLOps tutorial
- [PyCaret](https://pycaret.org/) for the automated machine learning framework
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [Kaggle](https://www.kaggle.com/) for providing the dataset

## 📞 Contact

**Project Maintainer**: alfa7g7  
**GitHub**: [@alfa7g7](https://github.com/alfa7g7)  
**Repository**: [predicting-patient-charges](https://github.com/alfa7g7/predicting-patient-charges)

---

**⚡ Built with modern MLOps practices for production-ready deployment** 