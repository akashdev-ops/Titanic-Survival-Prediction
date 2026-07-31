# 🚢 Titanic Survival Prediction

A Machine Learning project that predicts whether a passenger would survive the Titanic disaster using **Logistic Regression**.

## 📌 Project Overview

The objective of this project is to build a machine learning model that predicts passenger survival based on features such as:

- Passenger Class (Pclass)
- Gender (Sex)
- Age
- Number of Siblings/Spouses (SibSp)
- Number of Parents/Children (Parch)
- Fare
- Embarked Port

The project includes data preprocessing, visualization, model training, evaluation, and prediction using Python and Scikit-learn.

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

---

## 📂 Project Structure

```
Titanic-Survival-Prediction/
│
├── app.py
├── Titanic_Survival_Prediction.ipynb
├── Titanic-Dataset.csv
├── Titanic_Model.pkl
├── requirements.txt
├── README.md
└── Titanic_Predictions.csv
```

---

## ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Titanic-Survival-Prediction.git
```

Move into the project folder:

```bash
cd Titanic-Survival-Prediction
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## ▶ Run the Project

### Jupyter Notebook

```bash
jupyter notebook
```

Open:

```
Titanic_Survival_Prediction.ipynb
```

### Streamlit Web App

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📊 Machine Learning Workflow

1. Load Dataset
2. Data Cleaning
3. Handle Missing Values
4. Encode Categorical Variables
5. Data Visualization
6. Feature Selection
7. Train Logistic Regression Model
8. Evaluate Model
9. Predict Passenger Survival
10. Save Model

---

## 📈 Model Evaluation

Evaluation Metrics:

- Accuracy Score
- Confusion Matrix
- Classification Report

---

## 🎯 Sample Prediction

Input:

- Passenger Class: 3
- Gender: Male
- Age: 22
- Fare: 7.25

Output:

```
Passenger Did Not Survive
```

---

## 🚀 Future Improvements

- Random Forest Classifier
- XGBoost
- Hyperparameter Tuning
- Feature Engineering
- Web Deployment
- Docker Support

---

## 👨‍💻 Author

Akash Pratap Dev

B.Tech Computer Science Student

---

## 📜 License

This project is developed for educational purposes.
