# Crop Recommendation System

## Overview

The Crop Recommendation System is a machine learning-based tool designed to recommend the most suitable crop to cultivate based on various soil and environmental factors. By leveraging Random Forest Classification, this system achieves an impressive accuracy of **99.32%**. It uses key parameters such as nitrogen (N), phosphorus (P), potassium (K), temperature (°C), humidity (%), pH, and rainfall (mm) to predict the ideal crop for a given set of conditions.

## Features

- **Accurate Crop Prediction**: Achieves high accuracy using Random Forest Classification.
- **Multi-Parameter Input**: Considers critical agricultural parameters for informed recommendations.
- **User-Friendly**: Easy to integrate into applications for farmers, agricultural researchers, or policy makers.

## Input Parameters

The system requires the following inputs to provide a recommendation:

- **Nitrogen (N)**: The nitrogen content in the soil.
- **Phosphorus (P)**: The phosphorus content in the soil.
- **Potassium (K)**: The potassium content in the soil.
- **Temperature (°C)**: The average temperature in the area.
- **Humidity (%)**: The relative humidity in the environment.
- **pH**: The acidity or alkalinity of the soil.
- **Rainfall (mm)**: The average rainfall in millimeters.

## Technology Stack

- **Programming Language**: Python
- **Machine Learning Algorithm**: Random Forest Classifier
- **Libraries Used**:
  - Scikit-learn
  - Pandas
  - NumPy
  - Matplotlib
  - Seaborn

## Model Performance

The Random Forest Classification model achieves an accuracy of **99.32%**, making it a reliable tool for crop prediction.

![Screenshot 2024-12-14 113519](https://github.com/user-attachments/assets/2f83b654-4890-4eb5-9bb6-3cfdf13e52c2)


## Tree Map Representation

Below is the tree map of the Random Forest model, which visualizes how decisions are made based on input parameters.

---

### Visualization

A tree map will be generated to illustrate the decision-making process of the Random Forest model.

---

## Project Structure

```
Crop Recommendation/
│
├── app.py
├── templates/
│   └── index.html
└── static/
    └── (any static files like images, CSS, or JS)
```

## Usage Instructions

1. **Install Dependencies**: Ensure you have Python and required libraries installed.
   ```bash
   pip install scikit-learn pandas numpy matplotlib seaborn
   ```
2. **Load Dataset**: Provide a dataset containing soil and environmental parameters.
3. **Train Model** (Optional): Train the Random Forest model with your dataset.
4. **Predict Crop**: Input parameters and use the trained model to predict the best crop.

## Conclusion

This Crop Recommendation System is a powerful tool for enhancing agricultural decision-making. By leveraging data-driven insights, it empowers farmers to maximize yield and ensure sustainable practices.
![Screenshot 2024-12-14 113852](https://github.com/user-attachments/assets/0a859cf1-961f-453f-941c-75c64cc114b1)
![Screenshot 2024-12-14 113912](https://github.com/user-attachments/assets/9f35639d-3247-4be5-8659-24109586f7e5)

