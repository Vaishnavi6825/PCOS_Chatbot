# 🌸 PCOS_Chatbot

**AI POWERED PCOS & ENDOMETRIOSIS DIAGNOSIS ASSISTANT**

---

## 📌 Project Overview

Polycystic Ovary Syndrome (PCOS) is a common hormonal disorder affecting millions of women. This AI-powered diagnostic assistant helps predict the likelihood of PCOS using biomedical indicators like hormone levels, BMI, and clinical symptoms. 

The tool provides accessible support for early detection and empowers women’s health decisions through a friendly Streamlit-based chatbot. <br>
⚠️ Disclaimer: This tool is not a substitute for professional medical advice.

---

## 🎯 Problem Statement

Women have diverse health needs that are often not adequately addressed by generic healthcare approaches. This lack of personalization can lead to suboptimal health outcomes and limited access to relevant services.They often face delays in diagnosis due to non-specific symptoms and lack of awareness about conditions like PCOS. This project aims to assist early-stage PCOS prediction using machine learning, improving accessibility and awareness.

---

## 💡 Proposed Solution

- Build a diagnostic chatbot using AI/ML for PCOS prediction.
- Aligns with **UN SDG Goal 3**: *Ensure healthy lives and promote well-being*.
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


## Comparison Chart: PCOS vs. Non-PCOS Patient

| Metric                | PCOS Patient (Example: Row 3) | Non-PCOS Patient (Example: Row 1) | Notes                                    |
|-----------------------|-------------------------------|-----------------------------------|------------------------------------------|
| PCOS (Y/N)            | 1 (Yes)                       | 0 (No)                            | Confirmed diagnosis.                     |
| Age (yrs)             | 33                            | 28                                | Age range typical for PCOS.              |
| BMI                   | 25.3                          | 19.3                              | Higher BMI may correlate with PCOS.      |
| LH (mIU/mL)           | 5.54                          | 7.95                              | LH:FSH ratio often >2 in PCOS.           |
| FSH (mIU/mL)          | 0.88                          | 3.68                              | Lower FSH in PCOS.                       |
| LH/FSH Ratio          | 6.3 (High)                    | 2.16 (Normal)                     | Ratio >2 suggests PCOS.                  |
| AMH (ng/mL)           | 6.63                          | 2.07                              | Elevated AMH common in PCOS.             |
| Follicle No. (L)      | 13                            | 3                                 | Polycystic ovaries (>12 follicles).      |
| Follicle No. (R)      | 15                            | 3                                 | Bilateral cysts common in PCOS.          |
| Hair Growth (Y/N)     | 1 (Yes)                       | 0 (No)                            | Hirsutism is a PCOS symptom.             |
| Skin Darkening (Y/N)  | 1 (Yes)                       | 0 (No)                            | Acanthosis nigricans may occur.          |
| Pimples (Y/N)         | 1 (Yes)                       | 0 (No)                            | Hormonal acne linked to PCOS.            |
| Waist:Hip Ratio       | 0.9                           | 0.83                              | Higher ratio indicates central obesity.  |
| TSH (mIU/L)           | 2.54                          | 0.68                              | Thyroid dysfunction may coexist.         |


## OUTPUTS:

## The AI model has analyzed the provided data and predicts a PCOS Negative (N) outcome - [Non-PCOS Patient (Example: Row 1)] 
## This indicates a low likelihood of PCOS, with a high confidence level of 93.00%.

![WhatsApp Image 2025-06-05 at 14 10 10_098e2361](https://github.com/user-attachments/assets/cadbeea3-1a5c-4f37-9a0b-b8bdfcc97d2a)

![WhatsApp Image 2025-06-05 at 14 10 42_f5d591dd](https://github.com/user-attachments/assets/7def23bc-a05b-43fe-aac1-6a389ee73bf9)

![WhatsApp Image 2025-06-05 at 14 12 22_47c41f7b](https://github.com/user-attachments/assets/a0077f0e-5a58-40a5-b771-64cb50216b1d)

![WhatsApp Image 2025-06-05 at 14 13 08_63027b6d](https://github.com/user-attachments/assets/7e30716f-f235-4d06-bbab-b12bedb7f7e2)

![WhatsApp Image 2025-06-05 at 14 13 44_ae9dc270](https://github.com/user-attachments/assets/98abdf48-03f3-49d3-8ed1-3f953cd3f0dd)

---

## The AI model has analyzed the provided data and predicts a PCOS Positive (Y) outcome - [PCOS Patient (Example: Row 3)] 
## This indicates a likelihood of PCOS, with a confidence level of 69.00%.

![WhatsApp Image 2025-06-05 at 13 58 20_f1b43248](https://github.com/user-attachments/assets/9ecb19de-b7de-4faa-b67d-56faffd57c31)

![WhatsApp Image 2025-06-05 at 13 58 50_1a4c2e9c](https://github.com/user-attachments/assets/3060df73-989d-40e5-b076-100486f13e8b)

![WhatsApp Image 2025-06-05 at 13 59 18_c8b29ecb](https://github.com/user-attachments/assets/32323252-688b-49bb-9f65-3d7694ec64e6)

![WhatsApp Image 2025-06-05 at 13 59 45_03e516d9](https://github.com/user-attachments/assets/0d2c52c8-fa3d-4272-b992-9ea8fe5271e1)

![WhatsApp Image 2025-06-05 at 14 00 03_4845c833](https://github.com/user-attachments/assets/e9be5d92-d9f2-40cc-844a-28736eb8fac0)

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

## 📚 References
-**World Health Organization (WHO) – Information on Polycystic Ovary Syndrome (PCOS)** <br>
https://www.who.int/news-room/fact-sheets/detail/polycystic-ovary-syndrome

-**Kaggle Dataset – Polycystic Ovary Syndrome (PCOS) Dataset by Prasoon Kottarathil** <br>
https://www.kaggle.com/datasets/prasoonkottarathil/polycystic-ovary-syndrome-pcos

-**3.Jyothi Ram et al. (2023). Detection of Polycystic Ovary Syndrome (PCOS) Using Machine Learning Techniques.**<br>
 https://www.researchgate.net/publication/369453284 <br>

 ## THANK YOU.










