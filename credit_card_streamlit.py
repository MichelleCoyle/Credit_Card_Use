import streamlit as st
import pandas as pd
import pickle

header = st.container()
dataset = st.container()
features = st.container()
model = st.container()


with header:
	st.title('Credit Card Use')
	st.text('This project looks at customer age vs credit score to classify card users into 1 of 3 categories;\nregular card user, infrequent card user, or big purchaser.')

st.write("# Predict user category✨")
st.write("### Determine user:")

# Customer credit score
score = st.slider('Customer score', min_value=550, max_value=850, value=550, step=1)

# Customer age
age = st.slider('Customer age', min_value=20, max_value=65, value=20, step = 1)



row = [score, age]
columns = ['score', 'age']

user_category = pd.DataFrame(dict(zip(columns, row)), index=[0])

# Show the table?
st.table(user_category)



# Now predicting!
if st.button(label="Click to Predict"):

    # Load the model
    loaded_model = pickle.load(open('credit_card_model.sav','rb'))
    
    # Make predictions (and get out pred probabilities)
    pred = loaded_model.predict(user_category)[0]
    
    st.write(f"User category: {pred:,.0f} user-type ")


