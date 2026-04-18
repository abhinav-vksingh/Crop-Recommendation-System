# 🌱 Crop Recommendation System

An intelligent agriculture web application that recommends the best crop for cultivation using Machine Learning and Deep Learning models.  
Built with **FastAPI**, interactive UI, model comparison dashboard, and live crop prediction.

---

# 🚀 Features

- 🌾 Predict best crop using soil + weather data
- 🤖 Multiple model selection
- 📊 Accuracy comparison dashboard
- 📈 Interactive chart visualization
- 🧠 Includes ANN (Deep Learning)
- ⚡ FastAPI backend
- 🎨 Modern responsive UI
- 🧪 Trained models loaded instantly

---

# 📌 Input Parameters

The system uses:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- pH
- Rainfall

---

# 🤖 Models Included

### Machine Learning
- Random Forest
- Logistic Regression
- Gaussian Naive Bayes
- SVC
- KNN
- Decision Tree
- Gradient Boosting

### Deep Learning
- ANN (MLPClassifier)

---

# 📊 Model Accuracy

| Model | Accuracy |
|------|----------|
| Random Forest | 99.31% |
| GaussianNB | 99.54% |
| Gradient Boosting | 98.18% |
| Decision Tree | 98.18% |
| Logistic Regression | 96.36% |
| SVC | 96.81% |
| KNN | 95.90% |
| ANN | 98.00% |

---

# 🛠 Tech Stack

- Python
- FastAPI
- HTML
- CSS
- Bootstrap
- Chart.js
- Scikit-learn
- Pandas
- NumPy
- Joblib

---

# 📄 Project Documents

- Final Project Report
- Partial Report
- Presentation PPT

These files are included in the project root for academic submission and review.

---

# 📁 Project Structure

```text
Crop-Recommendation/
│── main.py
│── requirements.txt
│── README.md
│── crop_recommendation.ipynb
│── Crop Recommendation System - Final Report.pdf
│── Crop Recommendation System - Partial Report.pdf
│── Crop Recommendation System - Presentation PPT.pptx
│
├── data/
│   └── Crop_recommendation.csv
│
├── model/
│   ├── RandomForestClassifier.pkl
│   ├── LogisticRegression.pkl
│   ├── GaussianNB.pkl
│   ├── ANN_MLP.pkl
│   └── other models...
│
├── templates/
│   └── index.html
│
└── static/
    └── crop.png
'''text


## How to Run the Project ->

1. Clone Repository
git clone <repository-link>
cd Crop-Recommendation


2. Install Dependencies
pip install -r requirements.txt


3. Run Application
uvicorn main:app --reload


4. Open in Browser
http://127.0.0.1:5000


# 🧪 How It Works

1. User enters soil and environmental values  
2. User selects model  
3. Input is scaled using saved scalers  
4. Selected model predicts crop  
5. Result shown on dashboard  
6. Accuracy chart compares all models  

# 🎓 Academic Value

This project demonstrates:

- Supervised Learning  
- Model Comparison  
- Data Preprocessing  
- Model Deployment  
- Web Integration with FastAPI  
- Dashboard Design  

# 👨‍💻 Developed By

**Abhinav Singh**
