import streamlit as st
page_image_bg = f"""
<style>
[data-testid="stAppViewContainer"]{{
background-image: url("https://marketplace.canva.com/EAD2962NKnQ/2/0/1600w/canva-rainbow-gradient-pink-and-purple-virtual-background-_Tcjok-d9b4.jpg");
background-size:cover;
background-repeat: no repeat;
}}
[data-testid="stHeader"]{{
background-image: url("https://marketplace.canva.com/EAD2962NKnQ/2/0/1600w/canva-rainbow-gradient-pink-and-purple-virtual-background-_Tcjok-d9b4.jpg");
background-size:cover;
background-repeat: no repeat;
}}
</style>
"""
st.markdown(page_image_bg, unsafe_allow_html = True)
st.title("Lavkesh's Calculator ")

# creates a horizontal line
st.write("---")

# input 1
num1 = st.number_input(label="First number")

# input 2
num2 = st.number_input(label="Second number")

st.write("Operation")

operation = st.radio("Select an operation to perform:",
                    ("Add", "Subtract", "Multiply", "Divide", "Modulus"))

ans = 0

def calculate():
    if operation == "Add":
        ans = num1 + num2
    elif operation == "Subtract":
        ans = num1 - num2
    elif operation == "Multiply":
        ans = num1 * num2
    elif operation=="Divide" and num2!=0:
        ans = num1 / num2
    elif operation=="Modulus":
       ans = num1 % num2
    else:
        st.warning("Division by 0 error. Please enter a non-zero number.")
        ans = "Not defined"

    st.success(f"Answer = {ans}")

if st.button("Calculate result"):
    calculate()

