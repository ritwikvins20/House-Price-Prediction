🏠 House Price Prediction Web Application

PythonFlaskMachine Learning

📝 Project Overview

This project is a Machine Learning web application that predicts house prices in Bangalore and Hyderabad. 

The model uses a Gradient Boosting Regressor trained on cleaned real estate data, achieving an accuracy of 84.6%. It features a professional Flask web interface with dynamic location dropdowns and feature importance analysis.

 Key Features

    High Accuracy: Focused on specific markets (Bangalore & Hyderabad) for precision.
    Dynamic Dropdowns: Locations automatically update based on the selected city.
    Feature Importance: Visual explanation of what drives the price (Area, Location, Luxury Score).
    Luxury Score: Aggregates amenities into a single influential feature.
    Professional UI: Modern Bootstrap 5 design.

 Tech Stack

    Backend: Python, Flask
    Frontend: HTML5, CSS3, Bootstrap 5, JavaScript
    Machine Learning: Scikit-Learn, Pandas, NumPy
    Model: Gradient Boosting Regressor

 How to Run Locally

    Clone the repository:

    git clone https://github.com/<YOUR-USERNAME>/House-Price-Prediction.git

    Navigate to the folder:

    cd House-Price-Prediction

    Install dependencies:

    pip install -r requirements.txt

    Run the Flask server:

    python server.py

    Open your browser and go to http://127.0.0.1:5000.

 Project Structure

    server.py: Flask backend to handle requests.
    templates/app.html: Frontend user interface.
    house_price_model.pickle: Trained ML model.
    location_stats.json: Data for Location encoding.
    Project.ipynb: Jupyter Notebook with data cleaning and training code.

 Model Performance

    Model Used	R² Score
    Linear Regression	78.3%
    Random Forest	81.0%
    Gradient Boosting	84.6%

 Authors

    V.Ritwik
    P.Pavan
    V.Manikanta
    D.Satish

University Project Submission

    https://github.com/ritwikvins20