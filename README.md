# 🏎️ PitCrew AI — Race Strategy Copilot

### *Intelligent, Explainable Race Telemetry Analysis Powered by IBM Granite AI & watsonx.ai*

---

## 🎯 Project Overview
**PitCrew AI** is a next-generation decision intelligence platform built for motorsport racing teams. In Formula 1, split-second decisions worth millions of dollars are made based on streams of data. PitCrew AI ingests complex telemetry parameters (tire wear, fuel levels, track temperatures, weather changes) and utilizes **IBM Granite AI** via **watsonx.ai** to generate instant, explainable, and actionable pit-stop strategies.

### ⚡ The One-Line Pitch
> *"Transforming raw racing telemetry into trusted, split-second strategic advantages through explainable AI."*

---

## 🚨 The Problem & Challenge
Modern racing teams handle over **1,000 data points per second** streaming from car sensors. During a live race, strategy engineers face:
* **Cognitive Overload:** Balancing tire degradation, fuel weight, changing weather, and competitor gaps simultaneously under extreme time stress.
* **The 'Black-Box' Issue:** Existing AI tools give data predictions but don't explain *why* a specific decision is recommended, making engineers hesitant to trust them blindly.

## 💡 Our Solution: PitCrew AI
PitCrew AI solves this by introducing an **Explainable AI Race Copilot**:
* **Real-time Data Synthesizer:** Computes tire degradation modeling and stint projections instantly.
* **Transparent AI Reasoning:** Powered by **IBM Granite (13B Chat)**, every recommendation (e.g., *BOX NOW* or *STAY OUT*) comes with clear, text-based analytical reasoning.
* **Dynamic Simulation Dashboard:** Built with Streamlit to present a cinematic, dark-themed F1 dashboard interface.

---

## 🛠️ Tech Stack & IBM Technology Integration

* **AI Engine:** IBM Granite 13B Chat Model (`ibm/granite-13b-chat-v2`)
* **AI Platform & Inference:** IBM watsonx.ai cloud infrastructure
* **Workflow Framework:** Langflow & Python-dotenv orchestration
* **Frontend/UI:** Streamlit & Custom Cinematic CSS Styling
* **Data Processing:** Pandas, NumPy, and Plotly Analytics

---

## 🚀 Quick Start & Installation

### Prerequisites
* Python 3.9+
* GitHub Account

### Local Deployment
1. Clone the repository:
   ```bash
   git clone [https://github.com/singhaprajita183-maker/PitCrew-AI.git](https://github.com/singhaprajita183-maker/PitCrew-AI.git)
   cd PitCrew-AI
