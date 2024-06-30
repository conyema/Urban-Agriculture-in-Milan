
import streamlit as st
import pandas as pd
import numpy as np
import requests
import pickle


# Load the trained model
model_path =r"C:\Users\rampr\Documents\Urban-Agriculture-in-Milan\web_app\2_crops_suitable\app\predictingyield.pkl"
with open(model_path, 'rb') as file:
    model = pickle.load(file)
    
    # Title of the app
st.title("Crop Yield Prediction")



def user_input_features():
    col1, col2 = st.columns(2)

    with col1:
        crop_type = st.selectbox('Crop Name', (
            'Apple','Asparagus', 'Broccoli', 'Cabbage', 'Cauliflowers', 'Chilly Peppers',
            'Cucumbers', 'Eggplants', 'Green Peas', 'Potatoes', 'Tomatoes', 
            'Apricot', 'Blueberry', 'Cherries', 'Figs', 'Grapes', 'Kiwi', 'Lemon',
            'Orange', 'Peach', 'Pear', 'Plum', 'Pomegranate', 'Strawberry', 'Watermelon',
            'Argula', 'Beet', 'Chard', 'Cress', 'Endive', 'Kale', 'Lettuce', 'Raddicchio',
            'Spinach'
        ))
        Fertility = st.selectbox('Fertility', ('High', 'Moderate'))
        Photoperiod = st.selectbox('Photoperiod', ('Day Neutral', 'Long Day Period', 'Short Day Period'))
        Temperature = st.number_input('Temperature', min_value=0.0, max_value=100.0, value=20.0)
        Rainfall = st.number_input('Rainfall', min_value=0.0, max_value=2000.0, value=1932.0)
        Light_Hours = st.number_input('Light Hours', min_value=0.0, max_value=100.0, value=12.0)
        Light_Intensity = st.number_input('Light Intensity', min_value=0.0, max_value=900.0, value=860.0)
        Category_pH = st.selectbox('Category pH', ('low_acidic', 'acidic', 'low_alkaline', 'neutral'))
        Season = st.selectbox('Season', ('Fall', 'Spring', 'Summer', 'Winter'))
    with col2:
        Rh = st.number_input('Rh', min_value=0.0, max_value=100.0, value=92.0)
        Nitrogen = st.number_input('Nitrogen', min_value=0.0, max_value=100.0, value=89.0)
        Phosphorus = st.number_input('Phosphorus', min_value=0.0, max_value=100.0, value=40.0)
        Potassium = st.number_input('Potassium', min_value=0.0, max_value=200.0, value=180.0)
        Potassium_Ratio = st.number_input('Potassium Ratio', min_value=0.0, max_value=100.0, value=10.0)
        Phosphorus_Ratio = st.number_input('Phosphorus Ratio', min_value=0.0, max_value=100.0, value=10.0)
        Nitrogen_Ratio = st.number_input('Nitrogen Ratio', min_value=0.0, max_value=100.0, value=10.0)
        
        Soil_Type = st.selectbox('Soil Type', ('Loam', 'Sandy', 'Sandy Loam'))
        

    data = {
        'crop_type': crop_type,
        'Fertility': Fertility,
        'Photoperiod': Photoperiod,
        'Rainfall': Rainfall,
        'Temperature': Temperature,
        'Light_Hours': Light_Hours,
        'Light_Intensity': Light_Intensity,
        'Rh': Rh,
        'Nitrogen': Nitrogen,
        'Phosphorus': Phosphorus,
        'Potassium': Potassium,
        'Potassium_Ratio': Potassium_Ratio,
        'Phosphorus_Ratio': Phosphorus_Ratio,
        'Nitrogen_Ratio': Nitrogen_Ratio,
        'Category_pH': Category_pH,
        'Soil_Type': Soil_Type,
        'Season': Season
    }
    
    features = pd.DataFrame(data, index=[0])
    return features

# Main application
st.write("## Input Features")
features = user_input_features()

col1, col2, col3 = st.columns([1, 2, 1])

#with col1,col2,col3:
if st.button("Predict"):
        prediction = model.predict(features)
        # Display prediction in a beautiful box
        st.subheader('Predicted Crop Yield')
        st.write(f"## Predicted Yield: {prediction[0]}")






#if __name__ == '__main__':
   # st.run()
