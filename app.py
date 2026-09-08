import streamlit as st
import requests
import pandas as pd

st.title("Crypto Price Dashboard 🚀")

if st.button("Refresh Price"):
    st.rerun()

# -------------------------
# Current Prices
# -------------------------
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

# -------------------------
# BTC Historical Price
# -------------------------
st.subheader("BTC Price History")

url = "https://api.exchange.coinbase.com/products/BTC-USD/candles?granularity=3600"

response = requests.get(url, timeout=10)
data = response.json()

df = pd.DataFrame(
    data,
    columns=["time", "low", "high", "open", "close", "volume"]
)

df["time"] = pd.to_datetime(df["time"], unit="s")
df = df.sort_values("time")

st.line_chart(
    df,
    x="time",
    y="close"
)
