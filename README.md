# 🏎️ PitCrew AI // Race Strategy Copilot

> **The Cognitive Strategy Engine for Motorsport Simulation** > Built with Streamlit, IBM Granite AI, and watsonx.ai. Telemetry is infrastructure. Strategy is the product.

---

## 🌌 Overview

**PitCrew AI** is a real-time race strategy inference system designed for Formula racing simulation. While conventional dashboards only display raw numbers, PitCrew AI processes live telemetry—such as tire degradation matrix, fuel remaining delta, track temperature variances, and weather vectors—to compute deterministic, physics-first strategy recommendations.

The engine is engineered to deliver high-stakes decision support (e.g., Undercut/Overcut metrics) backed by explainable generative reasoning via **IBM Granite AI**.

---

## 📂 Repository Architecture

The project follows an industrial-grade modular software tier layout:

```text
PitCrew-AI/
├── src/
│   ├── backend/
│   │   ├── inference/
│   │   │   └── cognitive_engine.py   # Deterministic strategy computations
│   │   └── reasoning/
│   │       └── granite_client.py     # IBM watsonx AI client orchestration
│   └── frontend/
│       └── app.py                    # Streamlit Mission Control surface
├── infrastructure/                   # Deployment configurations & environment stubs
├── docs/                             # Strategy methodology documentation
├── tests/                            # Automation and validation suites
├── requirements.txt                  # Python production dependencies
└── README.md                         # Product documentation
git clone [https://github.com/singhaprajita183-maker/PitCrew-AI.git](https://github.com/singhaprajita183-maker/PitCrew-AI.git)
cd PitCrew-AI
WATSONX_APIKEY = "your_ibm_watsonx_api_key"
PROJECT_ID = "your_ibm_project_id"
streamlit run src/frontend/app.py
cat << 'EOF' > app.py
import os
import sys

# Seedhe src/frontend/app.py ko trigger karne ke liye shortcut
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
from src.frontend import app
