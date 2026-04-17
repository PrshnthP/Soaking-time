import streamlit as st
import math

def wb_to_db(wb):
    return (wb / (100 - wb)) * 100

def calculate_time(initial_wb, final_wb, temp):
    Mi = wb_to_db(initial_wb)
    Mf = wb_to_db(final_wb)

    Ms = 44.2
    K = 0.2098 if temp < 45 else 0.043

    try:
        t = (1 / K) * math.log((Ms - Mi) / (Ms - Mf))
    except:
        t = 0

    return round(abs(t), 3)

st.set_page_config(page_title="Soaking Time Calculator")

st.title("🌾 Paddy Soaking Time Calculator")

initial_wb = st.number_input("Initial Moisture (Wb %)", value=12.0)
final_wb = st.number_input("Final Moisture (Wb %)", value=30.0)
temp = st.number_input("Soaking Temperature (°C)", value=35.0)

if st.button("Calculate"):
    t = calculate_time(initial_wb, final_wb, temp)
    st.success(f"⏱️ Time Required: {t} hours")
