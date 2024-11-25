import numpy as np
import pickle
import pandas as pd
import streamlit as st
import joblib

# Load the model
price_finder = joblib.load("C:/Users/Fatin/OneDrive/Desktop/APP/car_price_new1.pkl")

# Prediction function
def car_price_predictor(year, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner):
    year = int(year)
    Present_Price = float(Present_Price)
    Kms_Driven = int(Kms_Driven)
    Owner = int(Owner)

    prediction = price_finder.predict([[year, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner]])
    return prediction[0]  # Extracting the single value from the array

# Main function for the Streamlit app
def main():
    st.title("CAR PRICE PREDICTOR")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Car Price Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # User inputs
    year = st.text_input("Year of Manufacture", "Type Here")
    Present_Price = st.text_input("Present Price (in lacs)", "Type Here")
    Kms_Driven = st.text_input("Kilometers Driven", "Type Here")
    Fuel_Type = st.selectbox("Fuel Type", ("Petrol", "Diesel"))
    Fuel_Type = 0 if Fuel_Type == "Petrol" else 1
    Seller_Type = st.selectbox("Seller Type", ("Dealer", "Individual"))
    Seller_Type = 0 if Seller_Type == "Dealer" else 1
    Transmission = st.selectbox("Transmission Type", ("Manual", "Automatic"))
    Transmission = 0 if Transmission == "Manual" else 1
    Owner = st.text_input("Number of Previous Owners", "Type Here")

    # Prediction and output
    result = None
    if st.button("Predict"):
        try:
            # Input validation
            if not year.isdigit() or int(year) < 1900 or int(year) > 2024:
                st.error("Please enter a valid manufacturing year.")
            elif not Present_Price.replace('.', '', 1).isdigit() or float(Present_Price) <= 0:
                st.error("Please enter a valid present price.")
            elif not Kms_Driven.isdigit() or int(Kms_Driven) <= 0:
                st.error("Please enter a valid value for kilometers driven.")
            elif not Owner.isdigit() or int(Owner) < 0:
                st.error("Please enter a valid number of owners.")
            else:
                result = car_price_predictor(year, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner)
                st.success(f"The predicted price is {result:.2f} lacs.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

    # About section
    if st.button("About"):
        st.text("Project by Fatin")
        st.text("Mail: fatinekassabi1@gmail.com")
        st.text("Built with Streamlit")

if __name__ == '__main__':
    main()
