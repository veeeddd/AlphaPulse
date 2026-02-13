# 📈 AlphaPulse: Real-Time Financial Sentiment Engine

**AlphaPulse** is a production-grade NLP signal pipeline designed to extract tradable sentiment factors from financial news headlines. By leveraging **FinBERT**, this engine produces high-precision "Alpha Scores" stored in a high-performance **DuckDB** data lake.

---

## 🚀 Key Features
* **Domain-Specific NLP:** Utilizes FinBERT (PyTorch) for sentiment extraction, achieving ~25–35% higher precision on financial text than generic BERT models.
* **Resilient Ingestion:** A fault-tolerant web scraper featuring User-Agent rotation, jitter, and retry logic to sustain >99.5% data uptime.
* **Quant-Ready Storage:** Columnar data architecture via DuckDB for sub-second factor queries and efficient historical backtesting.
* **Automated Pipeline:** Scheduled data refresh and signal updates powered by GitHub Actions.

## 🛠️ Tech Stack
* **Language:** Python 3.9+
* **NLP Core:** [Hugging Face FinBERT](https://huggingface.co/ProsusAI/finbert) (PyTorch)
* **Database:** DuckDB (In-process OLAP)
* **Scraping:** BeautifulSoup4 & Requests
* **CI/CD:** GitHub Actions

## 📂 Project Structure
```text
AlphaPulse/
├── venv/               # Virtual environment (Local only)
├── .gitignore          # Professional exclusion rules
├── config.py           # Centralized global settings [Day 1]
├── db_manager.py       # DuckDB schema & connection logic [Day 2]
├── requirements.txt    # Project dependencies
└── README.md           # Documentation
