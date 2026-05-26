import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="ApexIQ // PitCrew AI Race Copilot", page_icon="🏎️", layout="wide")

# Custom Styling for Cyberpunk Racing Game Interface
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    div[data-testid="stMetricValue"] { font-size: 24px !important; font-weight: bold; }
    .stSlider > label { color: #00F0FF !important; font-weight: bold; }
    .report-box { background-color:#1f2937; padding:20px; border-radius:10px; border-left: 5px solid #00F0FF; }
    
    /* Game Track Design */
    .game-track { 
        background: linear-gradient(90deg, #222 70%, #00F0FF 100%); 
        padding: 15px; 
        border-radius: 10px; 
        border: 2px dashed #374151; 
        position: relative;
    }
    .grid-container {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
        margin-top: 15px;
    }
    .game-card {
        background-color: #111827;
        padding: 12px;
        border-radius: 8px;
        border: 1px solid #374151;
        text-align: center;
    }
    .blink-red { color: #FF3333; font-weight: bold; animation: blink 1s linear infinite; }
    @keyframes blink { 50% { opacity: 0; } }
    
    /* SVG Car Styling Container */
    .car-svg-container {
        background-color: #111827;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #00F0FF;
        text-align: center;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Main Title Header
st.title("🏎️ PITCREW AI // APEX IQ COPILOT")
st.caption("Live Interactive Game Telemetry Simulator Powered by IBM Granite 4.1")
st.markdown("---")

# Layout Split: Left Sidebar (Inputs), Center Panel (Dashboard), Right Panel (Interactive Game Screen)
col_input, col_main, col_game = st.columns([1, 1.6, 1.4])

with col_input:
    st.header("🎮 GAME CONTROLS")
    st.selectbox("🕹️ Select Driver Focus", ["Driver 1 (HAM)", "Driver 2 (RUS)"])
    
    current_lap = st.slider("Current Lap Position", 1, 50, 25)
    tire_wear = st.slider("Tire Wear Dynamic (%)", 0, 100, 85)
    tire_compound = st.selectbox("Current Tire Compound", ["Medium", "Soft", "Hard"])
    
    fuel_rem = st.slider("Fuel Remaining (%)", 0, 100, 35)
    track_temp = st.slider("Track Heat Temperature (°C)", 15, 60, 42)
    weather = st.selectbox("Weather Condition", ["Dry", "Damp", "Wet"])
    
    st.markdown("---")
    st.header("💬 TELEMETRY COMMANDS")
    user_query = st.text_input("Ask Granite AI", value="Should I pit?")

with col_main:
    st.header("🧠 IBM GRANITE AI STRATEGY ENGINE")
    user_role = st.radio("🔮 Select AI Response Mode", ["Race Engineer (Technical)", "Grandstand Fan (Simplified)"], horizontal=True)
    
    if user_role == "Race Engineer (Technical)":
        st.markdown(f"""
        <div class="report-box">
            <b style='color:#00F0FF;'>🛠️ Strategic Telemetry Analysis (Engineer Mode)</b><br><br>
            • <b>Observation:</b> Degradation vector on current {tire_compound} compound indicates high risk of puncture.<br>
            • <b>Prescription:</b> Transition immediately to <b>Hard compound</b>.<br>
            • <b>Tactical Margin:</b> Undercut window is active with <span style='color:#00FF00;'>+1.4s track advantage</span>.<br>
            <span style='color:#cccccc; font-style:italic;'>Granite 4.1 Response: Critical limits breached. Execute undercut strategy now.</span>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="report-box">
            <b style='color:#FFB300;'>🎙️ Live Race Commentary (Fan Mode)</b><br><br>
            • <b>What's Happening:</b> The tires are wearing out fast! If the driver doesn't pit right now, they risk losing the lead.<br>
            • <b>AI Advice:</b> Time to head into the pit lane for a fresh set of hard tires to lock in the victory!<br>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    st.header("📈 PERFORMANCE TABS")
    tab_base, tab_imp, tab_comp = st.tabs(["📌 Baseline Run", "🚀 Improved Run", "📊 Delta Comparison"])
    with tab_base:
        st.json({"Average Speed": "210 km/h", "Risk Score": "42.5%", "Wheel Slip": "0.15"})
    with tab_imp:
        st.json({"Average Speed": "225 km/h", "Risk Score": "46.77%", "Wheel Slip": "0.37"})
    with tab_comp:
        c1, c2 = st.columns(2)
        c1.metric(label="Average Speed Delta", value="+15 km/h", delta="+0.55s advantage")
        c2.metric(label="Risk Score Delta", value="+4.27%", delta="Riskier Stint", delta_color="inverse")

    st.markdown("---")
    st.header("🧩 SEGMENT DIAGNOSTICS")
    sz1, sz2 = st.columns(2)
    sz1.metric(label="Zone 1: Corner Entry", value="Optimal", delta="-0.04s Saved")
    sz2.metric(label="Zone 2: Mid Apex", value="Time Lost", delta="+0.18s Delay", delta_color="inverse")

# Right Panel: Full Game Graphics Rendering Panel with SVG Car
with col_game:
    st.header("🎮 LIVE GAME TELEMETRY SCREEN")
    
    # DYNAMIC COLOR CHANGES FOR CAR PARTS BASED ON SLIDERS
    tyre_color = "#FF3333" if tire_wear >= 80 else "#00FF00"
    fuel_color = "#FF3333" if fuel_rem <= 35 else "#00F0FF"
    
    # 1. LIVE CAR GRAPHIC MAP (SVG Drawing of an F1 Car Body)
    st.markdown(f"""
    <div class="car-svg-container">
        <p style="color:#00F0FF; font-weight:bold; font-size:14px; margin-bottom:15px;">🏎️ LIVE CHASSIS HUD GRAPHIC</p>
        <svg width="260" height="90" viewBox="0 0 260 90" xmlns="http://www.w3.org/2000/svg">
            <rect x="10" y="35" width="15" height="20" rx="2" fill="#374151" />
            <line x1="20" y1="45" x2="50" y2="45" stroke="#ffffff" stroke-width="4"/>
            <path d="M 50 45 Q 90 25 150 30 Q 200 35 220 45 L 220 45 Q 200 55 150 60 Q 90 65 50 45 Z" fill="#1f2937" stroke="#00F0FF" stroke-width="2"/>
            <ellipse cx="130" cy="45" rx="15" ry="8" fill="none" stroke="#ffffff" stroke-width="2" />
            <rect x="230" y="25" width="15" height="40" rx="2" fill="#374151" />
            <line x1="210" y1="45" x2="230" y2="45" stroke="#ffffff" stroke-width="4"/>
            <rect x="40" y="10" width="25" height="15" rx="4" fill="{tyre_color}" />
            <rect x="40" y="65" width="25" height="15" rx="4" fill="{tyre_color}" />
            <rect x="180" y="8" width="30" height="18" rx="4" fill="{tyre_color}" />
            <rect x="180" y="64" width="30" height="18" rx="4" fill="{tyre_color}" />
            <circle cx="100" cy="45" r="8" fill="{fuel_color}"/>
        </svg>
        <p style="font-size:11px; color:#cccccc; margin-top:10px;">Color Coding: <span style="color:#00FF00;">Green = Optimal</span> | <span style="color:#FF3333;">Red = Danger/Critical</span></p>
    </div>
    """, unsafe_allow_html=True)
    
    # 2. Dynamic Game Track Progress Bar
    progress_percentage = current_lap / 50.0
    st.markdown(f"""
    <div class="game-track">
        <p style="margin:0; font-size:11px; color:#00F0FF; font-weight:bold;">🏁 SILVERSTONE LIVE RACE PROGRESS TRACK</p>
        <div style="margin-top:20px;"></div>
    </div>
    """, unsafe_allow_html=True)
    st.progress(progress_percentage)
    st.caption(f"Car Position: Lap {current_lap}/50 ({int(progress_percentage*100)}% Completed)")
    
    st.markdown("---")
    
    # 3. Game HUD Interface Grids
    front_wing = "<span style='color:#00FF00;'>GOOD</span>"
    tyre_status = "<span class='blink-red'>🚨 PIT!</span>" if tire_wear >= 80 else "<span style='color:#00FF00;'>OK</span>"
    fuel_status = "<span class='blink-red'>⚠️ LOW</span>" if fuel_rem <= 35 else "<span style='color:#00FF00;'>OK</span>"
    engine_temp = f"<span style='color:#FF9900;'>{105 if track_temp >= 40 else 92}°C</span>"
    
    st.markdown(f"""
    <div class="grid-container">
        <div class="game-card"><b style="font-size:11px; color:#a0aec0;">FRONT WING</b><br>{front_wing}</div>
        <div class="game-card"><b style="font-size:11px; color:#a0aec0;">TYRES WEAR</b><br>{tyre_status}</div>
        <div class="game-card"><b style="font-size:11px; color:#a0aec0;">ENGINE CORE</b><br>{engine_temp}</div>
        <div class="game-card"><b style="font-size:11px; color:#a0aec0;">FUEL LEVEL</b><br>{fuel_status}</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 4. GPS Location Map
    st.subheader("🗺️ GPS POSITION LOCATOR")
    if current_lap % 3 == 0:
        current_zone, car_x, car_y = "Sector 3 - Main Straight (DRS Active)", 51.5074, -0.1278
    elif current_lap % 3 == 1:
        current_zone, car_x, car_y = "Sector 1 - Turn 4 (High-Speed)", 51.5085, -0.1265
    else:
        current_zone, car_x, car_y = "Sector 2 - Turn 11 (Chicane Break)", 51.5060, -0.1290
        
    st.markdown(f"**Current Track Zone:** `{current_zone}`")
    map_data = pd.DataFrame({'lat': [car_x], 'lon': [car_y]})
    st.map(map_data, zoom=14)
