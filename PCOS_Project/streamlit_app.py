import streamlit as st
import pandas as pd
import joblib
import numpy as np

# --- Configuration ---
# Set the page title and icon
st.set_page_config(
    page_title="AI POWERED PCOS & Endometriosis Diagnosis Assistant", # Changed title here
    page_icon="🌸",
    layout="centered"
)

# --- Load Model ---
# Ensure your 'pcos_model.pkl' is in the same directory as this script.
try:
    model = joblib.load("pcos_model.pkl")
except FileNotFoundError:
    st.error("Error: 'pcos_model.pkl' not found. Make sure the model file is in the same directory.")
    st.stop() # Stop the app if model is not found

# Define the exact feature columns expected by the model
# This list must be IDENTICAL to the X.columns.tolist() output from your model_train.py
# Note: 'Cysts (Y/N)' was removed from this list in previous discussions because the model
# was not trained with it, but it's present in your UI code.
# If your model *was* trained with 'Cysts (Y/N)', you should add it back here.
expected_feature_columns = [
    'Age (yrs)', 'Weight (Kg)', 'Height(Cm)', 'BMI', 'Blood Group',
    'Pulse rate(bpm)', 'RR (breaths/min)', 'Hb(g/dl)', 'Cycle(R/I)',
    'Cycle length(days)', 'Marraige Status (Yrs)', 'Pregnant(Y/N)',
    'No. of aborptions', 'I   beta-HCG(mIU/mL)', 'II    beta-HCG(mIU/mL)', # Corrected spacing here
    'FSH(mIU/mL)', 'LH(mIU/mL)', 'FSH/LH', 'Hip(inch)', 'Waist(inch)',
    'Waist:Hip Ratio', 'TSH (mIU/L)', 'AMH(ng/mL)', 'PRL(ng/mL)',
    'Vit D3 (ng/mL)', 'PRG(ng/mL)', 'RBS(mg/dl)', 'Weight gain(Y/N)',
    'hair growth(Y/N)', 'Skin darkening (Y/N)', 'Hair loss(Y/N)',
    'Pimples(Y/N)', 'Fast food (Y/N)', 'Reg.Exercise(Y/N)',
    'BP _Systolic (mmHg)', 'BP _Diastolic (mmHg)', 'Follicle No. (L)',
    'Follicle No. (R)', 'Avg. F size (L) (mm)', 'Avg. F size (R) (mm)',
    'Endometrium (mm)'
]

# --- Streamlit UI ---
st.title("🌸 AI POWERED PCOS & Endometriosis Diagnosis Assistant") # Main title changed here
st.markdown("Revolutionizing Women's Healthcare with AI") # New subtitle
st.markdown("""
    Welcome! This tool helps predict the likelihood of PCOS based on various health parameters.
    Please enter the patient's details below. **Note: Many of these values come from medical tests
    (like blood tests or ultrasound scans). Please refer to recent reports for accuracy.**
""")

# Create input fields for features
input_data = {}

st.header("Demographic & Physical Information")
col1, col2, col3 = st.columns(3)
with col1:
    input_data["Age (yrs)"] = st.number_input("Age (years)", min_value=10, max_value=80, value=25)
    st.caption("Patient's current age.")
    input_data["Weight (Kg)"] = st.number_input("Weight (Kg)", min_value=30.0, max_value=200.0, value=60.0, format="%.1f")
    st.caption("Patient's weight in kilograms.")
    input_data["Height(Cm)"] = st.number_input("Height (Cm)", min_value=100.0, max_value=250.0, value=160.0, format="%.1f")
    st.caption("Patient's height in centimeters.")
with col2:
    height_m = input_data["Height(Cm)"] / 100.0
    bmi_val = input_data["Weight (Kg)"] / (height_m ** 2) if height_m > 0 else 0.0
    input_data["BMI"] = st.number_input("BMI (Calculated)", value=bmi_val, disabled=True, format="%.2f")
    st.caption("Body Mass Index (calculated automatically).")
    input_data["Blood Group"] = st.selectbox("Blood Group (Numerical Encoding)",
                                             options=[1, 2, 3, 4, 5, 6, 7, 8], index=2) # Adjust options based on your actual encoding (e.g. A+=1, B-=2, etc.)
    st.caption("Enter as a number (e.g., 1 for A+, 2 for B-, etc. based on your data's encoding).")
    input_data["Pulse rate(bpm)"] = st.number_input("Pulse Rate (bpm)", min_value=40, max_value=120, value=75)
    st.caption("Heart beats per minute.")
with col3:
    input_data["RR (breaths/min)"] = st.number_input("RR (breaths/min)", min_value=10, max_value=30, value=16)
    st.caption("Respiration Rate (breaths per minute).")
    input_data["Hb(g/dl)"] = st.number_input("Hb (g/dl)", min_value=5.0, max_value=20.0, value=12.0, format="%.1f")
    st.caption("Hemoglobin level (from blood test).")
    input_data["Hip(inch)"] = st.number_input("Hip (inch)", min_value=20.0, max_value=60.0, value=38.0, format="%.1f")
    st.caption("Patient's hip circumference in inches.")


st.header("Cycle & Medical History")
col4, col5, col6 = st.columns(3)
with col4:
    input_data["Waist(inch)"] = st.number_input("Waist (inch)", min_value=15.0, max_value=50.0, value=30.0, format="%.1f")
    st.caption("Patient's waist circumference in inches.")
    waist_hip_ratio_val = input_data["Waist(inch)"] / input_data["Hip(inch)"] if input_data["Hip(inch)"] > 0 else 0.0
    input_data["Waist:Hip Ratio"] = st.number_input("Waist:Hip Ratio (Calculated)", value=waist_hip_ratio_val, disabled=True, format="%.2f")
    st.caption("Waist-to-Hip Ratio (calculated automatically).")
    input_data["Cycle(R/I)"] = st.selectbox("Cycle (Regular/Irregular)", options=[0, 1], format_func=lambda x: "Regular" if x == 0 else "Irregular", index=1)
    st.caption("Select 'Irregular' (1) or 'Regular' (0) based on menstrual cycle.")
with col5:
    input_data["Cycle length(days)"] = st.number_input("Cycle Length (days)", min_value=20, max_value=60, value=30)
    st.caption("Average length of menstrual cycle in days.")
    input_data["Marraige Status (Yrs)"] = st.number_input("Marriage Status (Yrs)", min_value=0, max_value=50, value=0)
    st.caption("Years since marriage (enter 0 if not married).")
    input_data["Pregnant(Y/N)"] = st.selectbox("Pregnant (Y/N)", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes", index=0)
    st.caption("Select 'Yes' (1) or 'No' (0) for current pregnancy status.")
with col6:
    input_data["No. of aborptions"] = st.number_input("No. of Abortions", min_value=0, max_value=10, value=0)
    st.caption("Number of previous abortions.")
    input_data["BP _Systolic (mmHg)"] = st.number_input("BP Systolic (mmHg)", min_value=80, max_value=200, value=120)
    st.caption("Blood Pressure Systolic reading.")
    input_data["BP _Diastolic (mmHg)"] = st.number_input("BP Diastolic (mmHg)", min_value=40, max_value=120, value=80)
    st.caption("Blood Pressure Diastolic reading.")


st.header("Symptoms & Lifestyle")
col7, col8, col9 = st.columns(3)
with col7:
    input_data["Weight gain(Y/N)"] = st.selectbox("Weight Gain (Y/N)", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes", index=1)
    st.caption("Unexplained weight gain.")
    input_data["hair growth(Y/N)"] = st.selectbox("Hair Growth (Y/N)", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes", index=0)
    st.caption("Excessive hair growth (hirsutism).")
    input_data["Skin darkening (Y/N)"] = st.selectbox("Skin Darkening (Y/N)", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes", index=0)
    st.caption("Presence of skin darkening (Acanthosis Nigricans).")
with col8:
    input_data["Hair loss(Y/N)"] = st.selectbox("Hair Loss (Y/N)", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes", index=1)
    st.caption("Significant hair loss/thinning.")
    input_data["Pimples(Y/N)"] = st.selectbox("Pimples (Y/N)", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes", index=1)
    st.caption("Presence of acne/pimples.")
    input_data["Fast food (Y/N)"] = st.selectbox("Fast Food (Y/N)", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes", index=1)
    st.caption("Frequent consumption of fast food.")
with col9:
    input_data["Reg.Exercise(Y/N)"] = st.selectbox("Regular Exercise (Y/N)", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes", index=0)
    st.caption("Engages in regular exercise.")
    input_data["Cysts (Y/N)"] = st.selectbox("Ovarian Cysts (Y/N)", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes", index=1)
    st.caption("Presence of ovarian cysts on ultrasound.")


st.header("Hormone & Ultrasound Readings")
col10, col11, col12 = st.columns(3)
with col10:
    input_data["TSH (mIU/L)"] = st.number_input("TSH (mIU/L)", min_value=0.1, max_value=10.0, value=2.0, format="%.2f")
    st.caption("Thyroid Stimulating Hormone (from blood test).")
    input_data["AMH(ng/mL)"] = st.number_input("AMH (ng/mL)", min_value=0.0, max_value=20.0, value=4.0, format="%.2f")
    st.caption("Anti-Müllerian Hormone (from blood test, indicates ovarian reserve).")
    input_data["PRL(ng/mL)"] = st.number_input("PRL (ng/mL)", min_value=0.0, max_value=100.0, value=15.0, format="%.2f")
    st.caption("Prolactin level (from blood test).")
with col11:
    input_data["Vit D3 (ng/mL)"] = st.number_input("Vit D3 (ng/mL)", min_value=0.0, max_value=100.0, value=30.0, format="%.2f")
    st.caption("Vitamin D3 level (from blood test).")
    input_data["PRG(ng/mL)"] = st.number_input("PRG (ng/mL)", min_value=0.0, max_value=50.0, value=0.5, format="%.2f")
    st.caption("Progesterone level (from blood test).")
    input_data["RBS(mg/dl)"] = st.number_input("RBS (mg/dl)", min_value=50.0, max_value=300.0, value=90.0, format="%.1f")
    st.caption("Random Blood Sugar (from blood test).")
with col12:
    input_data["FSH(mIU/mL)"] = st.number_input("FSH (mIU/mL)", min_value=0.1, max_value=30.0, value=6.0, format="%.2f")
    st.caption("Follicle Stimulating Hormone (from blood test).")
    input_data["LH(mIU/mL)"] = st.number_input("LH (mIU/mL)", min_value=0.1, max_value=50.0, value=10.0, format="%.2f")
    st.caption("Luteinizing Hormone (from blood test).")
    fsh_lh_ratio_val = input_data["FSH(mIU/mL)"] / input_data["LH(mIU/mL)"] if input_data["LH(mIU/mL)"] > 0 else 0.0
    input_data["FSH/LH"] = st.number_input("FSH/LH Ratio (Calculated)", value=fsh_lh_ratio_val, disabled=True, format="%.2f")
    st.caption("FSH to LH Ratio (calculated automatically).")

st.header("HCG Readings & Ultrasound")
col13, col14, col15 = st.columns(3)
with col13:
    input_data["I   beta-HCG(mIU/mL)"] = st.number_input("I beta-HCG (mIU/mL)", min_value=0.0, max_value=2000.0, value=0.0, format="%.1f")
    st.caption("First Beta-HCG reading (from blood test, related to pregnancy).")
    input_data["II    beta-HCG(mIU/mL)"] = st.number_input("II beta-HCG (mIU/mL)", min_value=0.0, max_value=2000.0, value=0.0, format="%.1f")
    st.caption("Second Beta-HCG reading (from blood test, related to pregnancy).")
with col14:
    input_data["Follicle No. (L)"] = st.number_input("Follicle No. (Left Ovary)", min_value=0, max_value=50, value=8)
    st.caption("Number of follicles seen on left ovary (from ultrasound).")
    input_data["Follicle No. (R)"] = st.number_input("Follicle No. (Right Ovary)", min_value=0, max_value=50, value=7)
    st.caption("Number of follicles seen on right ovary (from ultrasound).")
with col15:
    input_data["Avg. F size (L) (mm)"] = st.number_input("Avg. Follicle Size (L) (mm)", min_value=0.0, max_value=30.0, value=7.0, format="%.1f")
    st.caption("Average size of follicles on left ovary (from ultrasound).")
    input_data["Avg. F size (R) (mm)"] = st.number_input("Avg. Follicle Size (R) (mm)", min_value=0.0, max_value=30.0, value=7.5, format="%.1f")
    st.caption("Average size of follicles on right ovary (from ultrasound).")
    input_data["Endometrium (mm)"] = st.number_input("Endometrium (mm)", min_value=0.0, max_value=20.0, value=6.0, format="%.1f")
    st.caption("Endometrial thickness (from ultrasound).")


# --- Prediction Button ---
if st.button("Predict PCOS"):
    # Convert input_data dictionary to a pandas DataFrame
    features_df = pd.DataFrame([input_data])

    # Reindex to ensure columns match the training data exactly, fill any missing with 0
    try:
        # Note: 'Cysts (Y/N)' is collected in the UI but was removed from expected_feature_columns
        # in previous steps because the model was not trained with it.
        # Ensure that 'Cysts (Y/N)' is NOT in expected_feature_columns if your model
        # was not trained on it, to avoid "Feature names unseen at fit time" errors.
        final_features = features_df.reindex(columns=expected_feature_columns, fill_value=0)
    except KeyError as e:
        st.error(f"Data formatting error: Missing or incorrect feature '{e}'. Please check the input fields and the 'expected_feature_columns' list.")
        st.stop()

    # Make prediction
    prediction = model.predict(final_features)
    prediction_proba = model.predict_proba(final_features)

    # Display results
    st.subheader("Prediction Result:")
    if prediction[0] == 1:
        st.success("## PCOS Positive (Y) 😥")
        st.write(f"The model predicts this patient likely **has PCOS** with a confidence of **{prediction_proba[0][1]*100:.2f}%**.")
    else:
        st.info("## PCOS Negative (N) 😊")
        st.write(f"The model predicts this patient likely **does NOT have PCOS** with a confidence of **{prediction_proba[0][0]*100:.2f}%**.")

# --- General Preventive Health Tips ---
st.markdown("---") # Add another separator for clarity
st.subheader("💡 A Little Extra for Your Wellness Journey")
st.markdown("""
    Remember, consistent small actions lead to big health benefits!
    * **Balance Your Plate:** Focus on whole foods, lean proteins, and healthy fats.
    * **Stay Active:** Even short bursts of activity add up.
    * **Mind Your Sleep:** Aim for quality rest to support overall health.
    * **Hydrate Often:** Water is essential for every body function.
    * **Find Your Calm:** Practice stress-reducing techniques daily.
    * **Regular Check-ups:** Don't skip your routine doctor visits!
    Your commitment to health is truly inspiring!
""")
st.markdown("---")
st.write("Disclaimer: This is a predictive model and should not be used as a substitute for professional medical advice. Always consult with a healthcare provider for diagnosis and treatment.")

# Add a small footer
st.markdown("Developed with ❤️ using Streamlit")
