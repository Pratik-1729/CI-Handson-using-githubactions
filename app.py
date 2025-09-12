import streamlit as st

def calculate_power(base, exponent):
    return base ** exponent


st.title("Power Calculator")
st.write("Enter a number and the power you want to raise it to:")

# Input fields
n = st.number_input("Enter an Integer", value=1, step=1)
p = st.number_input("Enter the Power (Exponent)", value=2, step=1)

# Calculate power
if st.button("Calculate"):
    result = n ** p
    st.success(f"{n} raised to the power of {p} is: {result}")



