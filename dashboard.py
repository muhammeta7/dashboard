import streamlit as st

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
