import streamlit as st
import pandas as pd

st.title("My First Cloud App 🚀")
st.write("ทดลองใช้ pandas บน Streamlit Cloud")

data = {
    "Coin": ["BTC", "ETH", "SOL"],
    "Price": [65000, 3200, 180]
}

df = pd.DataFrame(data)

st.dataframe(df)
