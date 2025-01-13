import streamlit as st
import numpy as np
import pandas as pd
from time import time

st.title('st.cache')

# Not using cache
a0 = time()
st.subheader('Not using st.cache')

@st.cache(suppress_st_warning=True)
def load_data_a():
    df = pd.DataFrame(
        np.random.rand(2000000, 5),
        columns=['a', 'b', 'c', 'd', 'e']
    )
    for i in range(200):
        np.random.rand(2000000, 5)
    return df

def call_and_measure():
    start = time()
    st.write(load_data_a())
    end = time()
    st.info(end - start)

call_and_measure()
call_and_measure()

def next_page():
    st.query_params['challenge'] = 'Day25'

st.button('Next', on_click=next_page)