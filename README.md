# ❤️ Heart Disease Prediction App

This project is a **Machine Learning web application** built with [Streamlit](https://streamlit.io/) to predict the likelihood of heart disease based on user inputs. The model is trained on healthcare data and deployed on Streamlit Cloud.

🔗 Live Demo: [Heart Disease Prediction App](https://deva-heart-disease-prediction.streamlit.app/)

---

## 🚀 Features

* User-friendly web interface powered by Streamlit
* Predicts probability of heart disease from user input features
* Pre-trained ML model (`heart_disease_model.pkl`) loaded with `joblib`
* Columns reference file (`columns.pkl`) to ensure consistent feature ordering
* Dataset (`Heart.csv`) included for reproducibility and experimentation

---

## 🛠️ Tech Stack

* **Frontend & Deployment**: Streamlit
* **Machine Learning**: scikit-learn
* **Data Handling**: Pandas, NumPy
* **Model Persistence**: Joblib

---

## 📂 Project Structure

```
Heart-Disease-Prediction/
├── app.py                  # Main Streamlit app
├── requirements.txt        # Project dependencies
├── heart_disease_model.pkl # Trained ML model
├── columns.pkl             # Column names/features for model
├── Heart.csv               # Dataset used for training
└── README.md               # Project documentation
```

---

## ⚙️ Installation & Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/Kali-13/Heart-Disease-Prediction.git
   cd Heart-Disease-Prediction
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app locally:

   ```bash
   streamlit run app.py
   ```

5. Open your browser at:

   ```
   http://localhost:8501
   ```

---

## 📦 Requirements

Example `requirements.txt`:

```
streamlit
scikit-learn
pandas
numpy
joblib
```

---

## 📊 Dataset

The dataset `Heart.csv` contains medical attributes (such as age, cholesterol, blood pressure, etc.) used to train the model for predicting heart disease.

---

## 👨‍💻 Author

Developed by **[Kali-13](https://github.com/Kali-13)**
