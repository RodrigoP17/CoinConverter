import streamlit as st
from tools_converter.api import obtain_taxes
from tools_converter.converter import coin_converter
from config.configuration_loader import load_config

config = load_config()
api_key = config["api_key"]
base_coin = config["base_coin"]


st.set_page_config(
    page_title="Coin Converter",
    layout="centered"
)


st.title("Coin Converter🪙")

st.markdown("This app allows you to convert **numerous coins**"
            "with changes of value in real time with our API"
            "[ExchangeRate API](https://v6.exchangerate-api.com/)")

value = st.number_input(
    "Input the value you want to convert:",
    min_value=0.0,
    format="%.2f"
    )


available_coins = obtain_taxes(api_key, base_coin)

original_coin = st.selectbox("From:", available_coins, index=0)
destination_coin = st.selectbox("To:", available_coins, index=1)

if st.button("Convert"):

    try:
        result = coin_converter(value, original_coin, destination_coin, taxes=available_coins)
        st.success(f"{value} {original_coin} = {result} {destination_coin}")
    
    except ValueError as e:
        st.error(f"Error {e}")
