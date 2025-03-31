import streamlit as st

st.title("Unit Converter App")

st.markdown("### Converts Length, Weight, and Time instantly!")
st.write("Welcome! Select a catagory, enter a value and get the converted result in real-time.")

catagory = st.selectbox("Choose a catagory", ["Length", "Weight", "Time"])

def convert_units(catagory, value, unit):
    if catagory == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        
    elif catagory == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
        
    elif catagory == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit ==  "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24

if catagory == "Length":
    unit = st.selectbox("Select Conversion", ["Kilometers to Miles", "Miles to Kilometers"])
elif catagory == "Weight":
    unit = st.selectbox("Select Conversion", ["Kilogrames to Pounds", "Pounds to Kilograms"])
elif catagory == "Time":
    unit = st.selectbox("Select Conversion", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])

value = st.number_input("Enter value to convert")

if st.button("Convert"):
        result = convert_units(catagory, value, unit)
        st.success(f"The converted value is: {result: .2f}")
