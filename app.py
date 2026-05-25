import streamlit as st
import pandas as pd
import numpy as np
import time

# Page configuration for a futuristic racing look
st.set_page_config(
    page_title="PitCrew AI - Your Race Copilot",
    page_icon="🏎️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark cinematic F1 racing theme
st.markdown("""
<style>
    .reportview-container { background: #0a0f1d; color: #ffffff; }
    .sidebar .sidebar-content { background: #0f172a; }
    h1, h2, h3 { color: #00f2fe; font-family: 'Arial Black', sans-serif; }
    .stButton>button { background-color: #ff007f; color: white; border-radius: 5px; font-weight: bold; width: 100%; }
    .stButton>button:hover { background-color: #ff0055; color: white; }
    .metric-card { background-color: #1e293b; padding: 15px; border-radius: 10px; border-left: 5px solid #00f2fe; margin-bottom: 10px; }
    .alert-card { background-color: #3b0712; padding: 15px; border-radius: 10px; border-left: 5px solid #ff0055; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

# Application Header
st.title("🏎️ PITCREW AI // RACE COPILOT")
st.subheader("Powered by IBM Granite AI & watsonx.ai")
st.write("---")

# Sidebar for Real-Time Telemetry Inputs
st.sidebar.header("📊 LIVE TELEMETRY INPUTS")
lap_number = st.sidebar.slider("Current Lap", 1, 50, 28)
total_laps = 50

st.sidebar.subheader("🔧 Car Status")
tire_wear = st.sidebar.slider("Tire Wear (%)", 0, 100, 87)
tire_compound = st.sidebar.selectbox("Current Tire Compound", ["Soft", "Medium", "Hard"], index=1)
fuel_level = st.sidebar.slider("Fuel Remaining (%)", 0, 100, 42)

st.sidebar.subheader("🌧️ Track Conditions")
track_temp = st.sidebar.slider("Track Temperature (°C)", 15, 60, 42)
weather = st.sidebar.selectbox("Weather Forecast", ["Dry", "Light Rain", "Heavy Rain"], index=0)

# Main Dashboard Layout
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""<div class='metric-card'>
    <h5>🛞 TIRE STATUS ({tire_compound})</h5>
    <h2>{tire_wear}% Wear</h2>
    <p style='color: {"#ff0055" if tire_wear > 80 else "#00ff88"}'>Status: {'CRITICAL' if tire_wear > 80 else 'OPTIMAL'}</p>
    </div>""", unsafe_allow_html=True)

with col2:
    st.markdown(f"""<div class='metric-card'>
    <h5>⛽ FUEL LEVEL</h5>
    <h2>{fuel_level}%</h2>
    <p>Estimated Laps Left: {int(fuel_level * 0.4)} Laps</p>
    </div>""", unsafe_allow_html=True)

with col3:
    st.markdown(f"""<div class='metric-card'>
    <h5>🏁 RACE PROGRESS</h5>
    <h2>Lap {lap_number} / {total_laps}</h2>
    <p>Track Temp: {track_temp}°C | Weather: {weather}</p>
    </div>""", unsafe_allow_html=True)

st.write("---")

# Action Button to trigger IBM Granite Analysis Simulation
st.write("### 🧠 AI STRATEGY ENGINE")
if st.button("RUN LIVE STRATEGY ANALYSIS"):
    with st.spinner("Analyzing real-time multi-modal telemetry streams with IBM Granite AI..."):
        time.sleep(1.5) # Simulating processing time
        
        st.success("Analysis Complete! Confidence Score: **92%**")
        
        # Strategy Logic Output Simulation based on inputs
        if tire_wear > 80:
            st.markdown("""<div class='alert-card'>
            <h3>🚨 AI STRATEGY ALERT: PIT NOW!</h3>
            <p><b>Reasoning (IBM Granite 13B Engine):</b> Tire degradation on the current Medium compound has hit a critical threshold of 87%. Lap times are projected to drop by 1.8 seconds on the next lap. Competitors behind are pacing on fresh hard sets. Staying out poses a high risk of puncture or an undercut strategy failure.</p>
            <p><b>Recommended Action:</b> Box on Lap 28. Switch to <b>Hard Tires</b> to comfortably secure the P3 position until the end of the race.</p>
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown("""<div class='metric-card' style='border-left: 5px solid #00ff88;'>
            <h3>✅ AI STRATEGY ALERT: STAY OUT</h3>
            <p><b>Reasoning (IBM Granite 13B Engine):</b> Current tire wear and fuel parameters are well within the optimal window. The degradation curve suggests you can extend this stint by 4 more laps to execute an overcut strategy effectively.</p>
            <p><b>Recommended Action:</b> Maintain current pace and target Lap 32 for the next pit stop window.</p>
            </div>""", unsafe_allow_html=True)

# Analytics Chart Simulation
st.write("---")
st.write("### 📈 TIRE DEGRADATION PROJECTION")
chart_data = pd.DataFrame(
    np.random.randn(20, 2) * -0.5 + [tire_wear, tire_wear - 5],
    columns=['Predicted Degradation', 'Optimal Model Target']
)
st.line_chart(chart_data)
