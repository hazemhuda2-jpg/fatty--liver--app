import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Fatty Liver Risk", page_icon="🩺")
st.title("🩺 Fatty Liver Risk Assessment")
st.write("دخلي بياناتك وهنحسب نسبة الخطورة")

age = st.slider("العمر", 18, 80, 35)
bmi = st.slider("مؤشر كتلة الجسم BMI", 15.0, 45.0, 25.0)
alt = st.slider("إنزيم ALT", 10, 200, 30)
ast = st.slider("إنزيم AST", 10, 200, 25)

if st.button("احسب الخطورة"):
    risk = (bmi-25)*2 + (alt-30)*0.5 + (age-40)*0.3
    if risk < 10:
        st.success("✅ الخطورة قليلة")
    elif risk < 30:
        st.warning("⚠️ خطورة متوسطة - استشيري دكتور")
    else:
        st.error("❌ خطورة عالية - لازم متابعة طبية")
    st.metric("Risk Score", f"{risk:.1f}")
