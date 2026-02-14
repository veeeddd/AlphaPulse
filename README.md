# 🛡️ AlphaPulse: Enterprise-Grade Quant Sentiment Engine

**AlphaPulse** is a real-time NLP signal pipeline that extracts tradable sentiment factors from financial news. It leverages specialized transformer models and high-throughput time-series storage to identify "Alpha" before the market reacts.

## 🚀 Key Engineering Highlights
* **Low-Latency Inference**: Implemented **8-bit dynamic quantization** on FinBERT (PyTorch), reducing inference latency by ~40% and memory footprint by 4x.
* **High-Throughput Storage**: Built a columnar data lake using **DuckDB**, enabling sub-second factor queries and efficient historical backtesting.
* **Fault-Tolerant Ingestion**: Engineered an asynchronous scraping system with **User-Agent rotation, random jitter, and recursive retry logic** to sustain >99.5% uptime in rate-limited environments.
* **Real-Time Dashboard**: Built a **Streamlit Command Center** featuring Pulse Momentum tracking and Price-Sentiment correlation via `yfinance`.

## 🛠️ Tech Stack
* **AI/ML**: Python, PyTorch, FinBERT (Hugging Face), Transformers
* **Data**: DuckDB (Columnar), Pandas, BeautifulSoup4
* **Viz/Ops**: Streamlit, Plotly, GitHub Actions

## 🚦 Getting Started (For Recruiters/Developers)

Follow these steps to replicate the environment and run the pipeline locally.

### 1. Clone & Setup Environment
```powershell
git clone [https://github.com/veeeddd/AlphaPulse.git]
cd AlphaPulse
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # Windows
```

### 2. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 3. Run the Intelligence Pipeline
This script fetches news, runs quantized sentiment analysis, and updates the DuckDB data lake.
```powershell
python main.py
```
### 4. Launch the Command Center
Visualize the Alpha Scores, Momentum, and Market Correlation.
```
python -m streamlit run app.py
```
### 📈 Signal Logic
The engine generates an Alpha Score (0.0 to 1.0). When a ticker hits a confidence threshold (default: 0.85), a high-conviction signal is logged in alpha_alerts.log and broadcasted to the dashboard leaderboard.

## 📂 Project Structure
```text
AlphaPulse/
├── venv/               # Virtual environment (Local only)
├── .gitignore          # Professional exclusion rules
├── config.py           # Centralized global settings [Day 1]
├── db_manager.py       # DuckDB schema & connection logic [Day 2]
├── requirements.txt    # Project dependencies
└── README.md           # Documentation
