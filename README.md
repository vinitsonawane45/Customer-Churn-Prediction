# 📉 Customer Churn Prediction

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikit-learn" />
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-green?style=for-the-badge&logo=pandas" />
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge" />
</p>

> A machine learning project to predict whether a customer will churn (leave) a telecom service, enabling businesses to take proactive retention measures.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Dataset](#-dataset)
- [Project Structure](#-project-structure)
- [Technologies Used](#-technologies-used)
- [Workflow](#-workflow)
- [Models & Results](#-models--results)
- [Key Insights](#-key-insights)
- [Installation & Usage](#-installation--usage)
- [Contributing](#-contributing)

---

## 🔍 Overview

Customer churn refers to when a customer stops doing business with a company. In the telecom industry, retaining existing customers is far more cost-effective than acquiring new ones. This project builds a **binary classification model** to predict if a customer is likely to churn, based on their usage behavior, demographics, and subscription details.

---

## ❓ Problem Statement

Given historical customer data, can we:
1. Identify customers who are **at risk of churning**?
2. Understand **what factors** drive churn?
3. Enable the business to apply **targeted retention strategies**?

---

## 📊 Dataset

The dataset contains customer information from a telecommunications company with the following features:

| Feature | Description |
|---|---|
| `CustomerID` | Unique identifier for each customer |
| `Gender` | Male / Female |
| `SeniorCitizen` | Whether the customer is a senior citizen (0 / 1) |
| `Partner` | Whether the customer has a partner |
| `Dependents` | Whether the customer has dependents |
| `Tenure` | Number of months the customer has stayed |
| `PhoneService` | Whether the customer has phone service |
| `MultipleLines` | Whether the customer has multiple lines |
| `InternetService` | Type of internet service (DSL / Fiber optic / No) |
| `OnlineSecurity` | Whether the customer has online security |
| `OnlineBackup` | Whether the customer has online backup |
| `DeviceProtection` | Whether the customer has device protection |
| `TechSupport` | Whether the customer has tech support |
| `StreamingTV` | Whether the customer streams TV |
| `StreamingMovies` | Whether the customer streams movies |
| `Contract` | Contract term (Month-to-month / One year / Two year) |
| `PaperlessBilling` | Whether the customer uses paperless billing |
| `PaymentMethod` | Payment method used |
| `MonthlyCharges` | Monthly amount charged |
| `TotalCharges` | Total amount charged |
| `Churn` | **Target** — Yes / No |

- **Total Records:** ~7,043 customers
- **Target Class:** Churn (Yes = 1, No = 0)
- **Class Imbalance:** ~26% churn rate

---

## 📁 Project Structure

```
Customer-Churn-Prediction/
│
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv    # Raw dataset
│
├── notebooks/
│   ├── 01_EDA.ipynb                              # Exploratory Data Analysis
│   ├── 02_Preprocessing.ipynb                    # Data Preprocessing
│   └── 03_Modeling.ipynb                         # Model Training & Evaluation
│
├── models/
│   └── churn_model.pkl                           # Saved trained model
│
├── src/
│   ├── preprocess.py                             # Preprocessing utilities
│   └── predict.py                                # Prediction utilities
│
├── requirements.txt                              # Python dependencies
└── README.md                                     # Project documentation
```

---

## 🛠 Technologies Used

| Category | Tools |
|---|---|
| **Language** | Python 3.8+ |
| **Data Manipulation** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **Machine Learning** | Scikit-learn |
| **Model Evaluation** | ROC-AUC, Confusion Matrix, Classification Report |
| **Notebook Environment** | Jupyter Notebook / Google Colab |

---

## 🔄 Workflow

```
Raw Data
   │
   ▼
Data Cleaning & Preprocessing
   │  - Handle missing values
   │  - Encode categorical features
   │  - Feature scaling
   │
   ▼
Exploratory Data Analysis (EDA)
   │  - Univariate & Bivariate analysis
   │  - Churn correlation heatmaps
   │  - Distribution plots
   │
   ▼
Model Training
   │  - Logistic Regression
   │  - Decision Tree
   │  - Random Forest
   │  - Gradient Boosting / XGBoost
   │
   ▼
Hyperparameter Tuning
   │  - GridSearchCV / RandomizedSearchCV
   │
   ▼
Model Evaluation
   │  - Accuracy, Precision, Recall, F1-Score
   │  - ROC-AUC Curve
   │  - Confusion Matrix
   │
   ▼
Best Model Selection & Deployment
```

---

## 🏆 Models & Results

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|---|---|---|---|---|---|
| Logistic Regression | 80% | 0.67 | 0.55 | 0.60 | 0.84 |
| Decision Tree | 78% | 0.59 | 0.52 | 0.55 | 0.73 |
| Random Forest | 82% | 0.71 | 0.58 | 0.64 | 0.86 |
| **XGBoost** | **84%** | **0.74** | **0.62** | **0.67** | **0.88** |

> ✅ **Best Model:** XGBoost Classifier with hyperparameter tuning.

---

## 💡 Key Insights

From exploratory data analysis and feature importance:

- 📅 **Contract Type:** Customers on **month-to-month** contracts have significantly higher churn rates compared to one-year or two-year contracts.
- 💳 **Payment Method:** Customers paying via **Electronic Check** show the highest churn rates.
- 🌐 **Internet Service:** Customers using **Fiber Optic** internet tend to churn more often than DSL users.
- 🕐 **Tenure:** New customers (low tenure) are more likely to churn — loyalty increases with time.
- 💰 **Monthly Charges:** Higher monthly charges are associated with higher churn probability.
- 🔒 **Online Security & Tech Support:** Customers without these services churn at a higher rate.

---

## 🚀 Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/vinitsonawane45/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Notebooks

```bash
jupyter notebook
```

Open and run the notebooks in order:
1. `01_EDA.ipynb`
2. `02_Preprocessing.ipynb`
3. `03_Modeling.ipynb`

### 5. Predict Churn for New Data

```python
import pickle
import pandas as pd

# Load model
with open('models/churn_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Prepare your input data
data = pd.DataFrame([{
    'tenure': 12,
    'MonthlyCharges': 65.5,
    'Contract': 'Month-to-month',
    # ... other features
}])

prediction = model.predict(data)
print("Churn:", "Yes" if prediction[0] == 1 else "No")
```

---

## 📦 Requirements

```
pandas
numpy
matplotlib
seaborn
scikit-learn
xgboost
jupyter
```

Install all at once:
```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

## 👨‍💻 Author

**Vinit Sonawane**

- GitHub: [@vinitsonawane45](https://github.com/vinitsonawane45)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

<p align="center">⭐ If you found this project helpful, please give it a star!</p>
