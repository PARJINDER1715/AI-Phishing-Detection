# 🔐 AI Phishing Website Detection System

Machine Learning–powered cybersecurity tool that detects whether a website is **legitimate or phishing** by analyzing URL structure and webpage features.

This project uses **AutoML + Streamlit** to build an interactive phishing detection system capable of scanning websites and providing a **risk score dashboard**.

---

## 🚀 Features

* 🌐 **Website URL Scanner** – Enter any URL and analyze it instantly
* 🧠 **Machine Learning Detection** – AutoML model predicts phishing risk
* 📊 **Risk Score Dashboard** – Displays phishing probability and confidence
* 🔎 **Webpage Feature Analysis** – Extracts multiple security indicators
* 💻 **Interactive Streamlit UI** – Easy to use web interface

---

## 🧠 Machine Learning Workflow

1. Dataset preprocessing
2. Feature extraction from URLs
3. Model training using AutoML
4. Model evaluation
5. Deployment using Streamlit

---

## 📊 Features Used for Detection

The system analyzes multiple indicators such as:

* IP address usage in URL
* URL length
* Subdomain structure
* HTTPS usage
* URL redirection
* Presence of forms or iframes
* Anchor link patterns
* Webpage metadata signals

These features help identify **suspicious patterns commonly used in phishing websites**.

---

## 🛠 Tech Stack

**Programming Language**

* Python

**Libraries**

* Streamlit
* NumPy
* Pandas
* Scikit-learn
* Joblib
* Requests
* BeautifulSoup
* tldextract

**Concepts**

* Machine Learning
* Cybersecurity
* Feature Engineering
* Web Scraping

---

## 📂 Project Structure

```
AI-Phishing-Detection
│
├── app.py                # Streamlit web application
├── automl_model.pkl      # Trained ML model
├── requirements.txt      # Project dependencies
├── dataset.csv           # Training dataset
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/AI-Phishing-Detection.git
cd AI-Phishing-Detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 🖥 Example Usage

1. Enter a website URL
2. Click **Run Detection**
3. The system analyzes the webpage
4. View the **phishing risk score and prediction**

---

## 📈 Future Improvements

* Deep learning–based phishing detection
* Real-time domain reputation checking
* Browser extension integration
* API for security tools
* Threat intelligence integration

---

## 👨‍💻 Author

**Parjinder Singh**
AI • Machine Learning • Cybersecurity

LinkedIn: https://www.linkedin.com/in/parjinder-singh

---

## ⭐ If you like this project

Give the repository a **star on GitHub** to support the project.
