
import streamlit as st
import numpy as np

st.set_page_config(page_title="Aviator Predictor", layout="centered")

st.title("🛩️ Aviator Predictor")
st.write("Paste your recent crash multipliers below (e.g., `1.2, 1.5, 3.0, 1.01`)")

input_data = st.text_area("Crash Values", placeholder="e.g., 1.2, 1.04, 2.1, 5.0, 1.01")

if st.button("Analyze"):
    try:
        crash_history = [float(x.strip()) for x in input_data.split(",") if x.strip()]
        crash_data = np.array(crash_history)

        st.subheader("📊 Crash Stats")
        st.write(f"**Mean:** {np.mean(crash_data):.2f}")
        st.write(f"**Median:** {np.median(crash_data):.2f}")
        st.write(f"**Standard Deviation:** {np.std(crash_data):.2f}")
        st.write(f"**% High Multipliers (>2.0):** {round(np.sum(crash_data > 2.0) / len(crash_data) * 100, 2)}%")

        avg_last_10 = np.mean(crash_data[-10:])
        st.subheader("🎯 Suggestion")
        if avg_last_10 < 2:
            st.warning("⚠️ Average is low. Wait or bet small.")
        elif avg_last_10 > 3:
            st.success("🟢 Good trend! Consider betting, but cash out early.")
        else:
            st.info("🟡 Medium trend. You can bet cautiously and cash out around 1.8–2.0.")
    except:
        st.error("⚠️ Please enter valid numbers separated by commas.")
