import streamlit as st
import requests

st.title("Crypto Price Dashboard 🚀")

url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"

response = requests.get(url, timeout=10)
data = response.json()

btc_price = float(data["data"]["amount"])

st.metric(
    label="Bitcoin Price (BTC/USD)",
    value=f"${btc_price:,.2f}"
)
