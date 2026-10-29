# 🏠 Boston House Price Prediction

## 📌 Project Overview
Boston House Price Prediction is a Machine Learning project that predicts house prices using the Boston Housing dataset. The project uses regression techniques to learn the relationship between housing features and house values.

## 🎯 Objectives
- Analyze housing data using Exploratory Data Analysis (EDA).
- Perform data preprocessing and feature selection.
- Train a Machine Learning regression model.
- Evaluate model performance.
- Predict house prices based on input features.

## 🛠️ Technologies Used
- **Python** – Programming language
- **Pandas** – Data manipulation
- **NumPy** – Numerical computations
- **Matplotlib & Seaborn** – Data visualization
- **Scikit-learn** – Machine Learning and model evaluation
- **Streamlit** – Web application interface

## 🔄 Project Workflow
1. Load the Boston Housing dataset.
2. Perform data preprocessing.
3. Conduct Exploratory Data Analysis (EDA).
4. Select relevant features.
5. Split the dataset into training and testing sets.
6. Train a regression model.
7. Evaluate the model using MAE, MSE, and R² score.
8. Predict house prices using the trained model.

## 📂 Project Structure
```text
Boston-House-Price-Prediction/
├── app.py
├── Boston_House_Price_Model.pkl
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository
```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Boston-House-Price-Prediction
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Install dependencies
```bash
python -m pip install -r requirements.txt
```

### 3. Run the application
```bash
python -m streamlit run app.py
```

The application will open in your browser.

## 📊 Model Evaluation
The model can be evaluated using:
- **MAE (Mean Absolute Error):** Measures the average absolute prediction error.
- **MSE (Mean Squared Error):** Measures the average squared prediction error.
- **R² Score:** Measures how well the model explains variation in house prices.

Actual evaluation results depend on the trained model.

## 🚀 Deployment
The Streamlit application can be deployed using Streamlit Community Cloud.

## 👩‍💻 Author
**Laxmi Rahangdale**

B.Tech – Computer Science and Engineering  
Specialization: Artificial Intelligence and Machine Learning

## 📌 Note
This project is intended for educational purposes. The original Boston Housing dataset has historical limitations and should not be used as a reliable tool for real-world property valuation.
