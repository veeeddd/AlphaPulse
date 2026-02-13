import streamlit as st
import pandas as pd
import plotly.express as px
import yfinance as yf
from db_manager import get_connection

st.set_page_config(page_title="AlphaPulse: Price Correlation", layout="wide")

st.title("📊 AlphaPulse: Price-Sentiment Correlation")

def load_data():
    with get_connection() as conn:
        df = conn.execute("SELECT * FROM alpha_scores ORDER BY timestamp ASC").df()
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

data = load_data()

if not data.empty:
    ticker_symbol = st.sidebar.selectbox("Select Asset", options=data['ticker'].unique())
    ticker_data = data[data['ticker'] == ticker_symbol]

    # Day 9 Feature: Fetch Real Price Data
    st.sidebar.subheader("Price Data Settings")
    period = st.sidebar.selectbox("Period", ["1d", "5d", "1mo"], index=1)
    
    with st.spinner(f"Syncing market data for {ticker_symbol}..."):
        stock = yf.Ticker(ticker_symbol)
        price_history = stock.history(period=period).reset_index()
        price_history['Date'] = pd.to_datetime(price_history['Date']).dt.tz_localize(None)

    # Visualization: Sentiment vs Price
    st.subheader(f"{ticker_symbol} Predictive Pulse")
    
    fig = px.line(ticker_data, x='timestamp', y='alpha_score', 
                  title="AI Alpha Score", template="plotly_dark")
    fig.add_scatter(x=price_history['Date'], y=price_history['Close'], 
                    name="Market Price", yaxis="y2")
    
    fig.update_layout(
        yaxis2=dict(title="Stock Price ($)", overlaying="y", side="right"),
        yaxis=dict(title="Alpha Score (Sentiment)"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    st.plotly_chart(fig, use_container_width=True)

    # Correlation Logic
    st.info("💡 **Quant Insight:** When Alpha Score peaks before a price jump, you've found a 'Lead Indicator'.")
else:
    st.warning("No signals found. Please run the orchestrator.")