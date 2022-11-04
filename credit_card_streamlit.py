import streamlit as st
import pandas as pd
import pickle

header = st.container()
dataset = st.container()
features = st.container()
model = st.container()


with header:
	st.title('Credit Card Use')
	st.text('This project looks at customer age vs credit score to classify card users into 1 of 3 categories; regular card user, infrequent card user, or big purchaser.')