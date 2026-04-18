from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import numpy as np
import joblib

app = FastAPI(title="Crop Recommendation System")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Load scalers
sc = joblib.load("model/standscaler.pkl")
mx = joblib.load("model/minmaxscaler.pkl")

# Models
models = {
    "Random Forest": "model/RandomForestClassifier.pkl",
    "Logistic Regression": "model/LogisticRegression.pkl",
    "GaussianNB": "model/GaussianNB.pkl",
    "SVC": "model/SVC.pkl",
    "KNN": "model/KNeighborsClassifier.pkl",
    "Decision Tree": "model/DecisionTreeClassifier.pkl",
    "Gradient Boosting": "model/GradientBoostingClassifier.pkl",
    "ANN": "model/ANN_MLP.pkl"
}

# Accuracy values
accuracies = {
    "Random Forest": 99.31,
    "Logistic Regression": 96.36,
    "GaussianNB": 99.54,
    "SVC": 96.81,
    "KNN": 95.90,
    "Decision Tree": 98.18,
    "Gradient Boosting": 98.18,
    "ANN": round(100 * 0.98, 2)
}

crop_dict = {
    1:"Rice",2:"Maize",3:"Jute",4:"Cotton",5:"Coconut",
    6:"Papaya",7:"Orange",8:"Apple",9:"Muskmelon",10:"Watermelon",
    11:"Grapes",12:"Mango",13:"Banana",14:"Pomegranate",
    15:"Lentil",16:"Blackgram",17:"Mungbean",18:"Mothbeans",
    19:"Pigeonpeas",20:"Kidneybeans",21:"Chickpea",22:"Coffee"
}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "models": models.keys(),
        "accuracies": accuracies
    })

@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    model_name: str = Form(...),
    Nitrogen: float = Form(...),
    Phosporus: float = Form(...),
    Potassium: float = Form(...),
    Temperature: float = Form(...),
    Humidity: float = Form(...),
    pH: float = Form(...),
    Rainfall: float = Form(...)
):
    data = np.array([[Nitrogen, Phosporus, Potassium, Temperature, Humidity, pH, Rainfall]])
    data = mx.transform(data)
    data = sc.transform(data)

    selected_model = joblib.load(models[model_name])
    prediction = selected_model.predict(data)

    result = crop_dict.get(int(prediction[0]), str(prediction[0]))

    return templates.TemplateResponse("index.html", {
        "request": request,
        "models": models.keys(),
        "selected_model": model_name,
        "result": result,
        "accuracy": accuracies[model_name],
        "accuracies": accuracies
    })