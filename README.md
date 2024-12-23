# South Sudan Flood Prediction App

This project is a **Streamlit-based web application** designed to predict flood risks in South Sudan. The application utilizes a machine learning model to forecast flood events and assess associated risk levels (Low, Medium, High). It aims to aid in flood preparedness and response planning by providing easy-to-understand predictions and interactive visualizations.


## Key Features
- **Interactive User Interface**: Clean, responsive, and user-friendly UI built with Streamlit.
- **Prediction Model**: Uses a trained `RandomForestRegressor` model to predict flood risks based on user inputs.
- **Google Drive Integration**: Loads the machine learning model and feature metadata directly from Google Drive.
- **Customizable Input**: Allows users to input relevant features (e.g., precipitation, temperature) to generate predictions.
- **Risk Levels**: Outputs risk levels (Low, Medium, High) and numerical scores for better understanding.

## Tech Stack
- **Backend**: Python 3.9
- **Frontend**: Streamlit
- **Machine Learning**: Scikit-learn (RandomForestRegressor)
- **Deployment**: Streamlit Community Cloud (or local)
- **Storage**: Google Drive for hosting large files

## Setup and Installation

### Prerequisites
1. **Python**: Install Python 3.8 or higher.
2. **Google Drive**: Ensure the model and feature files are uploaded to Google Drive with correct sharing permissions.

### Steps
1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   streamlit run flood.py
   ```

4. **Access the Application**:
   - The app will run locally at `http://localhost:8501`.
   - For deployment, follow the Streamlit Cloud instructions below.

## File Structure
- **`flood.py`**: The main Streamlit application script.
- **`requirements.txt`**: Lists all required Python libraries.
- **`random_forest_flood_model1.pkl`**: The machine learning model file hosted on Google Drive.
- **`feature_names.pkl`**: A pickle file containing the feature names required by the model.

## Using the App
1. **Home Page**:
   - Provides an overview of the app and its purpose.
2. **Prediction Page**:
   - Input relevant feature values (e.g., Precipitation, Temperature).
   - Click "Predict Flood Risk" to view results.
   - Outputs include:
     - Risk Level: Low, Medium, or High.
     - Risk Score: A numerical representation of the prediction.

## Deployment to Streamlit Cloud
1. **Push the Repository to GitHub**.
2. **Deploy**:
   - Log in to [Streamlit Cloud](https://streamlit.io/cloud).
   - Create a new app by linking your GitHub repository.
   - Specify the `flood.py` file as the entry point.
3. **Configure Environment**:
   - Ensure `requirements.txt` is included.
   - Files are dynamically fetched from Google Drive.

## Model Details
- **Algorithm**: RandomForestRegressor
- **Features**:
  - Example features include `Precipitation`, `Temperature`, and other environmental variables.
- **Training Dataset**: The model was trained on flood-related data to predict risk levels accurately.
- **Model Access**: The model can be accessed [here](https://drive.google.com/file/d/1_V2nFzbnJXLotAKFP2co-lWkOU8ozY0u/view?usp=sharing).


## Known Issues
1. **Google Drive File Access**:
   - Ensure files are publicly accessible via direct download links.
   - Update file IDs in `flood.py` if files are moved or replaced.
2. **Model Size**:
   - Large model files may take time to load; caching mechanisms are implemented to optimize performance.

## Future Improvements
- Enhance the machine learning model with real-time data updates.
- Add geospatial visualizations for better risk assessment.
- Integrate an API for external data sources (e.g., weather forecasts).


3. Submit a pull request with a detailed description of your changes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.



