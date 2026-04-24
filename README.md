House Price Prediction Web Application
Overview

This project is a Machine Learning web application that predicts house prices in Bangalore and Hyderabad. The model uses a Gradient Boosting Regressor trained on cleaned real estate data, achieving an accuracy of 84.6%.

Project Structure

    server.py: Flask backend to handle requests and serve the model.
    templates/: Contains HTML files (app.html) for the frontend.
    house_price_model.pickle: The trained machine learning model.
    model_columns.json: Structure of input columns for the model.
    location_stats.json: Mapping for Location Target Encoding.
    locations_by_city.json: Data for dynamic dropdowns.
    Project.ipynb: Jupyter Notebook containing data cleaning, EDA, and model training code.

Features

    Dynamic Dropdowns: Automatically updates locations based on the selected city.
    High Accuracy: Focused on specific markets (Bangalore & Hyderabad) for precision.
    Feature Importance: Visual explanation of what drives the price (Area, Location, Luxury Score).
    Luxury Score: Aggregates amenities into a single influential feature.

Tech Stack

    Backend: Python, Flask
    Frontend: HTML5, CSS3, Bootstrap 5, JavaScript
    Machine Learning: Scikit-Learn, Pandas, NumPy
    Model: Gradient Boosting Regressor

How to Run Locally

    Clone this repository:

    git clone <your-repo-link>

 

    Install dependencies:
    bash
     
      
     
    pip install -r requirements.txt
     
     
      
    Run the Flask server:
    bash
     
      
     
    python server.py
     
     
      
    Open your browser and go to http://127.0.0.1:5000