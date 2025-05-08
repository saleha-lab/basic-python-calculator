import streamlit as st

st.title("Basic Python Calculator")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")
op = st.selectbox("Select operation", ["+", "-", "*", "/"])

if st.button("Calculate"):
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    st.write("Result:", result)
