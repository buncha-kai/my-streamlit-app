import streamlit as st
import requests

st.title("Crypto Price Dashboard 🚀")

coins = ["BTC", "ETH", "SOL"]

cols = st.columns(3)

for i, coin in enumerate(coins):
    url = f"https://api.coinbase.com/v2/prices/{coin}-USD/spot"

    response = requests.get(url, timeout=10)
    data = response.json()

    price = float(data["data"]["amount"])

    cols[i].metric(
        label=f"{coin}/USD",
        value=f"${price:,.2f}"
    )
