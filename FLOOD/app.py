import streamlit as st
import pandas as pd
import numpy as np
import webbrowser

df = pd.read_csv("telangana_weather_data.csv")

required_columns = {"District", "Latitude", "Longitude", "Flood_Risk"}
if not required_columns.issubset(df.columns):
    st.error("Dataset must contain 'District', 'Latitude', 'Longitude', and 'Flood_Risk' columns.")
    st.stop()

def hill_climb_flood_risk(district_data):

    current = district_data.sample(n=1) 
    while True:
        neighbors = district_data.sample(n=5) 
        best_neighbor = neighbors.loc[neighbors['Flood_Risk'].idxmax()]

        if best_neighbor["Flood_Risk"] > current["Flood_Risk"].values[0]:
            current = best_neighbor.to_frame().T
        else:
            break 
    
    return current.iloc[0]  

st.title("🌊 Flood Risk Prediction - Telangana")


district = st.selectbox("📍 Select District", df["District"].unique())


district_data = df[df["District"] == district]

if not district_data.empty:
    
    most_flooded_area = hill_climb_flood_risk(district_data)
    
    latitude = most_flooded_area["Latitude"]
    longitude = most_flooded_area["Longitude"]
    highest_risk_score = most_flooded_area["Flood_Risk"]

    maps_url = f"https://www.google.com/maps/place/{latitude},{longitude}/@{latitude},{longitude},14z"
    
    webbrowser.open(maps_url)

    st.subheader(f"📍 Most Flooded Area in {district}")
    st.write(f"**Latitude:** {latitude}")
    st.write(f"**Longitude:** {longitude}")
    st.write(f"🌊 **Flood Risk Score:** {highest_risk_score:.2f}")
    st.success("🌍 Google Maps opened with the most flood-affected region.")

else:
    st.warning("❌ No data available for this district!")

if st.checkbox("Show Dataset"):
    st.write(df.head())
