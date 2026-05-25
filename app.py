import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration with Premium F1 Theme
st.set_page_config(
    page_title="PitCrew AI // Race Copilot",
    page_icon="🏎️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Black, Blue, and Red Neon F1 Styling
st.markdown("""
<style>
    /* Main Background - Deep Carbon Black */
    .stApp {
        background-color: #05070A;
    }
    
    /* Sidebar Background - Dark Blue-Black */
    section[data-testid="stSidebar"] {
        background-color: #0A0F18 !important;
        border-right: 2px solid #00F0FF;
    }
    
    /* Metric Boxes - Deep Black with Neon Blue border and Red accent */
    div[data-testid="stMetric"] {
        background-color: #0D131F !important;
        border: 1px solid #00F0FF !important;
        border-left: 6px solid #FF1801 !important;
        padding: 15px !important;
        border-radius: 12px !important;
        box-shadow: 0px 4px 15px rgba(0, 240, 255, 0.1);
    }
    
    /* Strategy & Output Boxes - Dark with Red Border */
    .strategy-box {
        padding: 18px;
        background-color: #0A0F18;
        border: 1px solid #FF1801;
        border-left: 6px solid #00F0FF;
        border-radius: 10px;
        margin-bottom: 15px;
        box-shadow: 0px 4px 15px rgba(255, 24, 1, 0.1);
    }
    
    /* Critical Alert Box - Deep Racing Red */
    .critical-alert {
        padding: 12px;
        background-color: #450A0A;
        border: 1px solid #FF1801;
        border-radius: 6px;
        color: #FFD3D3;
        font-weight: bold;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Text Colors */
    h1, h2, h3, p {
        color: #FFFFFF !important;
    }
    
    /* Custom Title Highlight */
    .f1-title {
        color: #FF1801 !important;
        font-weight: 900;
    }
    .f1-subtitle {
        color: #00F0FF !important;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR: LIVE TELEMETRY INPUTS ---
st.sidebar.markdown("<h2 style='color:#00F0FF;'>📊 TELEMETRY INPUTS</h2>", unsafe_allow_html=True)

selected_driver = st.sidebar.selectbox("🏎️ Select Driver Focus", ["Driver 1 (HAM)", "Driver 2 (RUS)"])

current_lap = st.sidebar.slider("Current Lap", 1, 50, 28)
tire_wear = st.sidebar.slider("Tire Wear (%)", 0, 100, 85)
tire_compound = st.sidebar.selectbox("Current Tire Compound", ["Soft", "Medium", "Hard", "Intermediate", "Wet"], index=1)
fuel_remaining = st.sidebar.slider("Fuel Remaining (%)", 0, 100, 35)
track_temp = st.sidebar.slider("Track Temperature (°C)", 15, 60, 42)

weather_forecast = st.sidebar.selectbox("Current Weather", ["Dry", "Light Drizzle", "Heavy Rain"])
laps_to_rain = st.sidebar.slider("Predicted Rain in (Laps)", 0, 20, 5 if weather_forecast != "Dry" else 0)

st.sidebar.markdown("---")
st.sidebar.markdown("<b style='color:#00F0FF;'>💬 COPILED COMMANDS</b>", unsafe_allow_html=True)
user_command = st.sidebar.text_input("Ask Granite AI (e.g., 'Should I pit?')", "")

# --- MAIN DASHBOARD HEADER ---
st.markdown("<h1 style='margin-bottom:0px;'>🏎️ PITCREW AI // <span class='f1-title'>RACE COPILOT</span></h1>", unsafe_allow_html=True)
st.markdown("<p class='f1-subtitle' style='font-size:18px; margin-top:0px;'>Strategy Engine Powered by IBM Granite AI & watsonx.ai</p>", unsafe_allow_html=True)
st.markdown("<hr style='border: 1px solid #1F2937;'>", unsafe_allow_html=True)

# --- TOP METRICS ROW ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label=f"🛞 TIRE WEAR ({tire_compound.upper()})", value=f"{tire_wear}%")
    if tire_wear > 80:
        st.markdown('<p class="critical-alert">🚨 BOX THIS LAP</p>', unsafe_allow_html=True)

with col2:
    est_laps = int(fuel_remaining * 0.4)
    st.metric(label="⛽ FUEL STATUS", value=f"{fuel_remaining}%", delta=f"Est. {est_laps} Laps")

with col3:
    st.metric(label="🏁 RACE PROGRESS", value=f"Lap {current_lap}/50", delta=f"{50 - current_lap} Laps Left")

with col4:
    st.metric(label="🌡️ TRACK CONDITIONS", value=f"{track_temp}°C", delta=weather_forecast)

st.markdown("<hr style='border: 1px solid #1F2937;'>", unsafe_allow_html=True)

# --- MIDDLE SECTION: AI ENGINE & PLANNERS ---
left_col, right_col = st.columns([1, 1])

with left_col:
    st.markdown("<h3 style='color:#FF1801;'>🧠 IBM GRANITE AI STRATEGY ENGINE</h3>", unsafe_allow_html=True)
    
    if user_command:
        st.markdown(f"**🧐 Analyzing Command:** *'{user_command}'*")
        if "pit" in user_command.lower() or "tire" in user_command.lower():
            if tire_wear > 75 or (weather_forecast != "Dry" and laps_to_rain == 0):
                st.success("🤖 **Granite AI:** BOX NOW! Switch to Hards/Intermediates immediately.")
            else:
                st.info("🤖 **Granite AI:** Stay out. Maintain pace for 2 more laps.")
        else:
            st.write("🤖 **Granite AI:** Telemetry stable. Watch rear tire temps in sector 3.")
    
    if weather_forecast != "Dry" and laps_to_rain > 0:
        st.warning(f"🌧️ **WEATHER ALERT:** Rain expected in {laps_to_rain} laps. Adjusting pit windows.")

    st.markdown('<div class="strategy-box">', unsafe_allow_html=True)
    st.markdown("<b style='color:#00F0FF;'>🎯 Target Window:</b> Lap 29 - Lap 32")
    st.markdown(f"<b style='color:#00F0FF;'>📈 Next Compound:</b> {'Hard' if track_temp > 40 else 'Soft'}")
    st.markdown("<b style='color:#00F0FF;'>⚡ Plan:</b> 2-Stop Strategy (Medium -> Hard -> Soft)")
    st.markdown('</div>', unsafe_allow_html=True)

with right_col:
    st.markdown("<h3 style='color:#00F0FF;'>🏁 LIVE UNDERCUT / OVERCUT PLANNER</h3>", unsafe_allow_html=True)
    gap_to_car_ahead = st.slider("Gap to Car Ahead (seconds)", 0.5, 10.0, 2.5)
    undercut_potential = "HIGH PROFIT" if tire_wear > 70 and gap_to_car_ahead < 3.0 else "LOW PROFIT"
    
    st.markdown(f'<div class="strategy-box">', unsafe_allow_html=True)
    st.markdown(f"📊 **Undercut Potential:** <span style='color:#FF1801; font-weight:bold;'>{undercut_potential}</span>", unsafe_allow_html=True)
    st.markdown(f"⏱️ **Pit Lane Loss Delta:** 22.4 seconds")
    st.markdown(f"🚗 **Track Re-entry:** Predicted P5 (Clean Air)")
    st.markdown('</div>', unsafe_allow_html=True)

# --- BOTTOM SECTION: DEGRADATION MATRIX GRAPH ---
st.markdown("<h3 style='color:#FFFFFF;'>📈 LIVE PERFORMANCE & DEGRADATION MATRIX</h3>", unsafe_allow_html=True)
laps_range = np.arange(0, 15)
pred_wear = np.minimum(100, tire_wear + (laps_range * 1.5))
target_matrix = np.minimum(100, tire_wear + (laps_range * 1.1))

chart_data = pd.DataFrame({
    'Laps From Now': laps_range,
    'Predicted Wear': pred_wear,
    'Target Matrix': target_matrix
}).set_index('Laps From Now')

st.line_chart(chart_data)
