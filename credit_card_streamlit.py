import streamlit as st
import pandas as pd
import pickle

header = st.container()
dataset = st.container()
features = st.container()
model = st.container()


with header:
	st.title('Credit Card Use')
	st.text('This project looks at customer age vs credit score using a decision tree model\nto classify credit card users into 1 of 3 categories; regular card user,\ninfrequent card user, or frequent user.')

st.write("## Predict user category✨")
st.write("#### Determine user:")

# Customer credit score
score = st.slider('Customer score', min_value=550, max_value=850, value=550, step=1)

# Customer age
age = st.slider('Customer age', min_value=20, max_value=65, value=20, step = 1)


st.write("##### User types:")
st.write("###### Type-0: Frequent User")
st.write("###### Type-1: Infrequent User")
st.write("###### Type-2: Regular User")


row = [score, age]
columns = ['score', 'age']

user_info = pd.DataFrame(dict(zip(columns, row)), index=[0])

# Show the table?
# st.table(user_info)



# Now predicting

if pred == 0:
        st.write("### Frequent credit card user")
        st.write(f"Predicted probability of churn: {proba*100:.2f} %")

elif pred == 1:
        st.write("### Infrequent credit card user")
        st.write(f"Predicted probability of churn: {proba*100:.2f} %")
	
elif pred == 2:
        st.write("### Regular credit card user")
        st.write(f"Predicted probability of churn: {proba*100:.2f} %")









# if st.button(label="Click to Predict"):

#     # Load the model
#     loaded_model = pickle.load(open('credit_card_model.sav','rb'))
    
#     # Make predictions 
#     pred = loaded_model.predict(user_info)[0]
    
#     st.write(f"User category: Type-{pred:,.0f} user")


