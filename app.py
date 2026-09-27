import streamlit as st
import pickle
import pandas as pd
from datetime import datetime

st.set_page_config(page_title=" salary predictor",page_icon="💵")
st.title("Salary Prediction based on Years of Experience")
st.subheader("Model deployed: Linear Regression")

with open("model.sp","rb") as file:
    model=pickle.load(file)

if "history" not in st.session_state:
    st.session_state.history = []

st.subheader("Original Dataset")

salary=pd.read_csv("https://raw.githubusercontent.com/SagarChhabriya/data-science/refs/heads/main/datasets/TBD/salary_dataset.csv")
st.scatter_chart(salary, x="Experience Years", y="Salary")

yoe=st.number_input('Years of Experience',min_value=0.0,max_value=10.0,step=0.5,value=2.0)

if st.button("Predict"):
    prediction=model.predict([[yoe]])
    predicted_val = float(prediction[0])
    
    st.success(f"Predicted Salary: {predicted_val:,.2f}")

    timestamp = datetime.now().strftime("%H:%M:%S")
    st.session_state.history.append({
        "Time": timestamp,
        "Years of Experience": yoe,
        "Predicted Salary": f"${predicted_val:,.2f}"
    })

st.write("---")
st.subheader("Prediction History")

if st.session_state.history:
    df_history = pd.DataFrame(st.session_state.history)

    st.dataframe(df_history.iloc[::-1])
    
    if st.button("Clear History"):
        st.session_state.history = []
        st.rerun()
else:
    st.info("No predictions made in this session yet.")

st.subheader("Model Performance")
st.write("With an R2 score of 0.9822, the model apparently has a strong predictive performance. The MAE and RMSE values of 4056 and 4873, respectively, indicate the magnitude of the prediction errors.")
