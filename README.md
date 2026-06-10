# 🏥 Annual Medical Charges Prediction

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

A predictive Machine Learning pipeline designed to estimate an individual's annual medical charges based on personal attributes such as age, BMI, smoking habits, and region. 

This project explores the entire Data Science lifecycle—from exploratory data analysis (EDA) in Jupyter Notebooks to model deployment via Flask and Streamlit Web Apps.

## 🎯 Project Highlights
- **Pre-trained ML Model:** Uses a trained regression model (`model.pkl`) to accurately forecast medical insurance costs.
- **Interactive EDA:** A comprehensive Jupyter Notebook (`Untitled.ipynb`) detailing feature engineering, data visualization, and model selection on `medical.csv`.
- **Flexible Deployment:** Choose between a lightweight Flask API (`Flask.py`/`app.py`) or a rich Streamlit UI (`streamlit.py`).

## 🚀 Installation & Usage

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Streamlit Dashboard (Recommended):**
   ```bash
   streamlit run streamlit.py
   ```

3. **Run Flask API:**
   ```bash
   python app.py
   ```
   *(Or run `python Flask.py` for the alternative routing setup)*

## 📊 Dataset
The model was trained on `medical.csv`, a rich dataset mapping personal demographics and health choices against billed insurance costs.

---
*Predictive Healthcare Analytics using Machine Learning.*