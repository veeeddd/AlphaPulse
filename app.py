import streamlit as st
import pandas as pd
import plotly.express as px
from db_manager import get_connection

st.set_page_config(page_title="AlphaPulse: Momentum", layout="wide")

st.title("📈 AlphaPulse: Sentiment Momentum")

def load_data():
    with get_connection() as conn:
        # Fetch data and ensure timestamp is a datetime object
        df = conn.execute("SELECT * FROM alpha_scores ORDER BY timestamp ASC").df()
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

data = load_data()

if not data.empty:
    # Sidebar Filters
    ticker = st.sidebar.selectbox("Select Asset", options=data['ticker'].unique())
    ticker_data = data[data['ticker'] == ticker]

    # Calculate Momentum (3-period rolling average)
    ticker_data['momentum'] = ticker_data['alpha_score'].rolling(window=3).mean()

    # Layout: Top Metrics
    c1, c2 = st.columns(2)
    latest_score = ticker_data['alpha_score'].iloc[-1]
    momentum_val = ticker_data['momentum'].iloc[-1]
    
    c1.metric(f"Current {ticker} Alpha", f"{latest_score:.2f}")
    c2.metric("Pulse Momentum", f"{momentum_val:.2f}", 
              delta=f"{momentum_val - latest_score:.2f}")

    # Layout: Trend Chart
    st.subheader(f"{ticker} Sentiment Trajectory")
    fig = px.line(ticker_data, x='timestamp', y=['alpha_score', 'momentum'],
                  title=f"Raw Score vs. Momentum for {ticker}",
                  labels={'value': 'Score', 'timestamp': 'Time'},
                  template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

    # Detailed Intelligence Table
    st.subheader("Raw Intelligence Feed")
    st.dataframe(ticker_data[['timestamp', 'sentiment', 'headline']].sort_values(by='timestamp', ascending=False))
else:
    st.warning("Data Lake is empty. Run 'python main.py' to generate signals.")