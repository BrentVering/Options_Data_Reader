import streamlit as st
import polygon

st.subheader("Polygon+Streamlit Demo App")
symbol = st.text_input("Enter a stock symbol", "AAPL")

with st.sidebar:
    #Get your Polygon API key from the dashboard.
    #In a real app you want to store this as a secret in your .env
    polygon_api_key = st.text_input("gHsNnpPUQaoIRTbWmueDJbdPeRH4QVqu", type="password")

# Authenticate with the Polygon API
client = polygon.OptionsClient('gHsNnpPUQaoIRTbWmueDJbdPeRH4QVqu')

col1, col2, col3 = st.columns(3)

 #Stock details
if col1.button("Get Details"):
    if not polygon_api_key.strip() or not symbol.strip(): st.error("gHsNnpPUQaoIRTbWmueDJbdPeRH4QVqu")
    else:
            try:
                details = client.get_ticker_details(symbol)
                st.success(f"Ticker: {details.ticker}\\n\\n"
                    f"Company Address: {details.address}\\n\\n"
                    f"Market Cap: {details.market_cap}")
            except Exception as e:
                st.exception(f"Exception: {e}")
