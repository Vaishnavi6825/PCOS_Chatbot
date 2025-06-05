# 🌸 PCOS_Chatbot

AI POWERED PCOS & ENDOMETRIOSIS DIAGNOSIS ASSISTANT
---

## 📌 Project Overview

Polycystic Ovary Syndrome (PCOS) is a common hormonal disorder affecting millions of women. This AI-powered diagnostic assistant helps predict the likelihood of PCOS using biomedical indicators like hormone levels, BMI, and clinical symptoms. 

The tool provides accessible support for early detection and empowers women’s health decisions through a friendly Streamlit-based chatbot.

---

## 🎯 Problem Statement

Women often face delays in diagnosis due to non-specific symptoms and lack of awareness about conditions like PCOS. This project aims to assist early-stage PCOS prediction using machine learning, improving accessibility and awareness.

---

## 💡 Proposed Solution

- Build a diagnostic chatbot using AI/ML for PCOS prediction.
- Aligns with **UN SDG Goal 3**:
- *Ensure healthy lives and promote well-being*.
- Supports Targets:
  - **3.7**: Universal access to reproductive healthcare.
  - **3.8**: Universal health coverage.

---

## 📁 Dataset

- Source: [Kaggle PCOS Dataset](https://www.kaggle.com/datasets/prasoonkottarathil/polycystic-ovary-syndrome-pcos)
- File used: `PCOS_data_without_infertility.xlsx`
- Features: Hormonal levels, menstrual patterns, BMI, age, etc.

---

## ⚙️ Technologies & Libraries Used

- Python 3.13.3
- Streamlit
- Pandas, NumPy
- Scikit-learn (RandomForestClassifier)
- Joblib (Model persistence)
- Openpyxl

---

## 🧠 ML Model: Random Forest Classifier

**Why Random Forest?**
- Works well with biomedical and categorical features.
- Robust against overfitting.
- Offers high accuracy and feature importance.

**Process:**
- Data Cleaning & Feature Extraction
- Train-Test Split (80-20)
- Model Training
- Accuracy Achieved: **~92.6%**

---

## 🖥️ Deployment: Streamlit Web App

The chatbot allows users to enter clinical values like age, AMH, BMI, etc., and receive real-time predictions on PCOS status.

### Sample Output:
- **PCOS Positive (Y)** – With Confidence %
- **PCOS Negative (N)** – With Confidence %

---

## 📊 Results & Interpretation

| Result         | Display                  | Confidence Range | Meaning                       |
|----------------|---------------------------|-------------------|-------------------------------|
| PCOS Positive  | 🟥 PCOS Positive (Y) 😥   | 50–100%           | High likelihood of PCOS       |
| PCOS Negative  | 🟩 PCOS Negative (N) 😊   | 50–100%           | Low likelihood of PCOS        |

---

## ✅ Recommendations Based on Prediction

**If Positive:**
- Consult an endocrinologist or gynecologist.
- Follow up with: Transvaginal ultrasound, fasting insulin, androgen level test.

**If Negative:**
- Maintain reproductive health checkups.
- Watch for: Irregular periods, hirsutism, unexplained weight gain.

---

## 📉 Performance Metrics

- **Accuracy**: 92.6%
- **False Positive Rate**: 6.2%
- **False Negative Rate**: 7.8%

> ⚠️ *Disclaimer: This tool is not a substitute for professional medical advice.*

---

## 🔭 Future Scope

- 🔬 **Smarter Models**: Integrate deep learning (e.g., ANN, XGBoost).
- ⌚ **Wearable Integration**: Sync with health tracking devices.
- 🌐 **Multi-language Support**: Regional language support for wider access.
- 💬 **Emotion-aware Chat**: Improve natural interaction quality.
- 📦 **Offline Use**: Edge deployment for low-resource areas.

---

## 🛡️ Key Challenges

- **Data Privacy**: Ensure compliance with HIPAA/GDPR.
- **Bias Mitigation**: Train on diverse datasets.
- **Clinical Trust**: Build reliability through validations.

---

## 📂 File Structure (Recommended)

