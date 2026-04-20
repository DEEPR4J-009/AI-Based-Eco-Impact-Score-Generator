<div align="center">

# 🌿 AI-Based Eco Impact Score Generator

**Real-time environmental data analysis and AI-powered predictions for India's energy grid**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

</div>

---

## 📌 Overview

An AI-powered platform that tracks carbon intensity, renewable energy share, and energy flow across India's power grid — providing real-time insights and LSTM-based predictions to support eco-friendly decision-making.

---

## 👨‍💻 Team

| Name | Roll No |
|------|---------|
| Deepraj Patel | 22BCS14957 |
| Harman Singh | 22BCS14925 |
| Pratyush Kumar | R319 |

---

## ✨ Features

- ⚡ **Carbon Intensity Tracking** — Monitor real-time CO₂ emissions per kWh
- 🌱 **Renewable Energy Percentage** — Live breakdown of green energy share
- 📊 **Production vs Consumption Analysis** — Visualize energy balance
- 🔄 **Import vs Export Breakdown** — Track cross-region energy flows
- 🤖 **AI Predictions (LSTM)** — Forecast future energy trends using deep learning

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit |
| ML Models | TensorFlow / Keras (LSTM) |
| Visualization | Plotly |
| Data Source | Electricity Maps API |
| Language | Python 3.10+ |

---

## 📂 Project Structure

```
eco-ai-ly/
├── frontend/
│   └── streamlit/
│       ├── Home.py
│       ├── requirements.txt
│       └── pages/
├── models/
├── data/
├── .env.example
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/eco-ai-ly.git
cd eco-ai-ly
```

### 2. Create & Activate Virtual Environment

```bash
cd frontend/streamlit
python -m venv .venv

# macOS / Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
cp .env.example .env
# Open .env and add your Electricity Maps API key
```

### 5. Run the Application

```bash
streamlit run Home.py
```

---

## 🔑 API Key Setup

Get your free API key from 👉 [electricitymap.org](https://www.electricitymap.org)

**`.env.example`**
```env
ELECTRICITYMAP_API_KEY=your_api_key_here
ELECTRICITYMAP_BASE_URL=https://api.electricitymap.org/v3
ELECTRICITYMAP_REGION=IN-WE
```

> ⚠️ **Never commit your `.env` file. Use `.env.example` as a reference only.**

---

## ⚠️ Important Notes

- 🔒 Never expose or upload your `.env` file
- 🗂️ Use `.env.example` as a template for contributors
- 📦 Large model files (`.keras`, `.pkl`) should be handled via **Git LFS**

---

## 📦 Git LFS Setup (Optional — for large model files)

```bash
git lfs install
git lfs track "*.keras"
git lfs track "*.pkl"
git add .gitattributes
git push
```

---

## 📤 Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit - AI-Based Eco Impact Score Generator"
git remote add origin https://github.com/yourusername/your-repo-name.git
git branch -M main
git push -u origin main
```

---

## 🎯 Goal

> To promote **eco-friendly decision-making** and build a **sustainable future** by making India's energy data accessible, interpretable, and predictable through the power of AI.

---

<div align="center">
Made with 💚 for a greener tomorrow
</div>
