import streamlit as st
import pandas as pd
import numpy as np

st.title("This is the title!")

st.header("This is a header!")

st.write("This is regular text!")

"""
# header
## subheader
"""

some_dictionary = {
    "key": "value",
    "key2": "value2"
}

some_list = [1, 2, 3]

st.write(some_dictionary)
st.write(some_list)

st.sidebar.write("This will be over on the sidebar")

df = pd.DataFrame(np.random.randn(50, 20), columns=('col %d' % i for i in range(20)))

st.dataframe(df)

st.image("https://www.nasdaq.com/sites/acquia.prod/files/styles/720x400/public/image/4b6c84393df1ef26f81356305cf5fba0007f8c2b_f9bcaea802f3a0a5afed32f5702d48e7.png?itok=ApkuIVqH")

