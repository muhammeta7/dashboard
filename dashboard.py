import streamlit as st
import pandas as pd
import numpy as np
import requests
option = st.sidebar.selectbox("Which Dashboard?", ('twitter', 'wallstreet bets', 'stocktwits', 'chart', 'pattern'))

st.header(option)

if option == 'twitter':
    st.subheader("Twitter Dashboard")

if option == 'chart':
    st.subheader("Chart Dashboard")

if option == 'stocktwits':
    pass

    req = requests.get('https://api.stocktwits.com/api/2/streams/symbol/AAPL.json')

    data = req.json()

    for message in data['messages']:
        st.image(message['avatar_url'])
        st.write(message['user']['username'])
        st.write(message['created_at'])
        st.write(message['body'])
