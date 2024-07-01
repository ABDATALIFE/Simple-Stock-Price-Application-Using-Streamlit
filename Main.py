import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf



st.write("""
         
     #    Simple Stock Price Application 
         
         Shown are the stock closing and volume of Google
         
         """)
         


ticker_symbol = "GOOGL"

ticker_Data = yf.Ticker(ticker_symbol)


ticker_DF = ticker_Data.history(period='1d',start='2020-5-31', end = '2024-5-31')


st.write("""
         ## Closing Price
         
         """)
st.line_chart(ticker_DF.Close)

st.write("""
         ## Volume
         
         """)
st.line_chart(ticker_DF.Volume)