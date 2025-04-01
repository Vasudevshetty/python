import streamlit as st
import pandas as pd

st.title("Streamlit text input")

name = st.text_input("Enter your name: ")
age = st.slider("Select your age:", 0, 100, 25)

options = ["python", "c", "java", "javascript"]
choice = st.selectbox("Choose your favorite programming language:", options)
st.write(f"You selected: {choice}")

if name:
    st.write(f"Hello, {name}!")

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"],
}

df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)
st.write("DataFrame:")
st.write(df)

uploaded_file = st.file_uploader("Upload files", type=["csv", "txt"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
