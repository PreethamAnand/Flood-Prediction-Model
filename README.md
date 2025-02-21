🌊 Flood Risk Prediction System<br>
This project predicts <b>flood-prone areas in Telangana</b> based on weather conditions and automatically identifies the most flood-affected location in the selected district. The system <b>opens Google Maps</b> to display the affected region.


<br><b>⚙️ Features</b></br>
✅ Takes <b>only district name</b> as input.  <br>
✅ Uses <b>Hill Climbing Algorithm</b> to identify the most flood-prone area.  <br>
✅ <b>Automatically opens Google Maps</b> with the most affected location.  <br>
✅ Displays <b>Flood Risk Score</b> and coordinates.  <br>
✅ <b>Streamlit-based UI</b> for easy interaction.  <br>
✅ <b>Prepares dataset using Jupyter Notebook</b> (`Flood_Risk_Prediction.ipynb`).<br>


<b>📦 Required Libraries</b><br>
Before running the project, install the dependencies:<imp>
    "pip install streamlit pandas numpy"
</imp>


<br><b>🚀 How to Run the Project</b>
<br><b>1️⃣ Preprocess Data (Run Jupyter Notebook)</b>
<br>1. Open <b>`Flood_Risk_Prediction.ipynb`</b> in Jupyter Notebook.
<br>2. Run all cells to <b>process the dataset</b> (`telangana_weather_data.csv`).
3. Ensure the dataset has correct <b>latitude, longitude, and flood risk scores</b>.

<br><b>2️⃣ Start the Streamlit App</b>
<br>Run the Streamlit web app:
<br>" streamlit run app.py "


<br><b>3️⃣ Select a District</b>
<br>- Choose a <b>district name</b> from the dropdown.
<br>- The system automatically <b>finds the most flood-affected location</b>.
<br>- <b>Google Maps opens</b> with the marked flood-prone area.


<br><b>📌 How It Works</b>
<br>1. <b>Loads the dataset</b> (`telangana_weather_data.csv`).
<br>2. Uses the <b>Hill Climbing Algorithm</b> to locate the <b>most flood-prone area</b> in the selected district.
<br>3. <b>Google Maps automatically opens</b> with the marked location.


<br><b>🔍 Example Usage</b>
<br>- <b>Input</b>: Hyderabad
<br>- <b>Output</b>:
  <br>- 📍 <b>Most Flooded Area</b>: `Latitude: 17.3850, Longitude: 78.4867`
  <br>- 🌊 <b>Flood Risk Score</b>: `150.2`
  <br>- <b>Google Maps opens</b> showing the affected area.



<br><b>📧 Contact</b>
<br>For queries, feel free to reach out. 🚀  
