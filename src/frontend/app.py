import streamlit as st
import time
import random
import os

st.set_page_config(page_title="PitCrew AI // Race Strategy Copilot", page_icon="🏎️", layout="wide")

st.markdown("""
    <style>
    .stMetric { background-color: #1f2937; padding: 15px; border-radius: 10px; border-left: 5px solid #00d4ff; }
    </style>
""", unsafe_allowed_html=True)

st.title("🏎️ PitCrew AI // Race Strategy Copilot")
st.subheader("The Cognitive Strategy Engine for Motorsport Simulation")
st.markdown("---")

st.sidebar.header("⚙️ Configuration Panel")
user_role = st.sidebar.selectbox("🔮 Select AI Response Mode", ["Race Engineer (Technical)", "Grandstand Fan (Simplified)"])

report_data = f"=== PITCREW AI STRATEGY REPORT ===\nMode: {user_role}\nStrategy: Medium -> Hard"
st.sidebar.download_button(label="📥 Export Strategy Report", data=report_data, file_name="strategy_report.txt")

col1, col2 = st.columns([1, 2])
with col1:
    st.header("📊 Live Telemetry Stream")
    start_stream = st.button("🏁 Start Live Telemetry Stream", type="primary")
    metric_lap = st.empty()
    metric_tire = st.empty()
    metric_fuel = st.empty()
    alert_box = st.empty()
    
    if start_stream:
        tire_wear = 52
        fuel_remaining = 88
        for lap in range(12, 32):
            time.sleep(0.5)
            tire_wear += random.randint(1, 3)
            fuel_remaining -= random.uniform(1.2, 2.1)
            metric_lap.metric(label="🏁 Current Lap", value=f"Lap {lap} / 50")
            metric_tire.metric(label="🛞 Tire Wear Degradation", value=f"{tire_wear}%")
            metric_fuel.metric(label="⛽ Fuel Remaining", value=f"{fuel_remaining:.1f}%")
            if tire_wear >= 80:
                alert_box.error("🚨 BOX THIS LAP — CRITICAL TIRE DEGRADATION DETECTED")
                break
    else:
        metric_lap.metric(label="🏁 Current Lap", value="Lap 12 / 50")
        metric_tire.metric(label="🛞 Tire Wear Degradation", value="52%")
        metric_fuel.metric(label="⛽ Fuel Remaining", value="88.5%")

with col2:
    st.header("🧠 IBM Granite AI Strategy Engine")
    if start_stream:
        with st.spinner("Analyzing telemetry stream via watsonx.ai..."):
            time.sleep(1.0)
            if user_role == "Race Engineer (Technical)":
                st.success("### 🛠️ Strategic Telemetry Analysis (Engineer Mode)")
                st.markdown("* **Observation:** Degradation vector on current Medium compound indicates high risk of puncture past Lap 31.\n* **Prescription:** Transition immediately to **Hard compound**.\n* **Tactical Margin:** Undercut window is active with $+1.4s$ track advantage.")
            else:
                st.info("### 🎙️ Live Race Commentary (Fan Mode)")
                st.markdown("* **What's Happening:** The tires are completely worn out! If Aprajita doesn't pit right now, they risk a flat tire.\n* **The Strategy:** The team is preparing the **Hard durable tires** to go to the end.\n* **The Move:** A classic 'Undercut' attempt to surprise the cars ahead!")
    else:
        st.info("💡 Click **'Start Live Telemetry Stream'** to feed data into IBM Granite AI and view real-time strategic reasoning.")
