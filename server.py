from flask import Flask, request, jsonify, render_template
import pickle
import json
import numpy as np

app = Flask(__name__)

# 1. Load the Artifacts
with open('house_price_model.pickle', 'rb') as f:
    model = pickle.load(f)

with open('model_columns.json', 'r') as f:
    model_columns = json.load(f)

with open('location_stats.json', 'r') as f:
    location_stats = json.load(f)

# Load locations for the dropdown
with open('locations_by_city.json', 'r') as f:
    locations_by_city = json.load(f)


# 2. Route: Get Locations for Dropdowns
@app.route('/get_locations/<city>')
def get_locations(city):
    locs = locations_by_city.get(city, [])
    return jsonify(locs)


# 3. Route: Homepage
@app.route('/')
def home():
    cities = list(locations_by_city.keys())
    default_locations = locations_by_city.get('Bangalore', [])
    return render_template('app.html', cities=cities, locations=default_locations)


# 4. Route: Prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    area = float(request.form['area'])
    bhk = int(request.form['bhk'])
    resale = int(request.form['resale'])
    city = request.form['city']
    location = request.form['location']
    
    # Calculate Luxury Score
    amenities_list = ['Gymnasium', 'SwimmingPool', 'LandscapedGardens', 
                      'JoggingTrack', 'RainWaterHarvesting', 'IndoorGames', 
                      'ShoppingMall', 'Intercom', 'SportsFacility', 'ATM', 
                      'ClubHouse', '24X7Security', 'PowerBackup', 
                      'CarParking', 'AC', 'Wifi', 'LiftAvailable', 
                      'VaastuCompliant', 'GolfCourse']
    
    luxury_score = 0
    for amenity in amenities_list:
        if request.form.get(amenity): 
            luxury_score += 1

    # Feature Engineering
    loc_value = location_stats.get(location, 0)
    city_hyderabad = 1 if city == 'Hyderabad' else 0

    data_dict = {
        'Area': area,
        'No. of Bedrooms': bhk,
        'Resale': resale,
        'Luxury_Score': luxury_score,
        'Loc_Value': loc_value,
        'City_Hyderabad': city_hyderabad
    }
    
    final_input = [data_dict[col] for col in model_columns]

    # Predict
    prediction = model.predict([final_input])[0]
    output = round(prediction, 2)
    
    # Format price
    formatted_price = "{:,.2f}".format(output)
    
    # Text for Resale
    resale_text = "Resale Property" if resale == 1 else "New Property"
    
    # --- NEW: FEATURE IMPORTANCE LOGIC ---
    importances = model.feature_importances_
    feature_names = model_columns
    
    # Create list of (feature, importance)
    feature_importance_list = sorted(zip(feature_names, importances), key=lambda x: x[1], reverse=True)
    
    # Get top 3 drivers
    top_3 = feature_importance_list[:3]
    
    # Format for HTML (Name, Percentage)
    importance_data = []
    for feat, imp in top_3:
        importance_data.append((feat, round(imp * 100, 1)))
    
    # Return Result
    return render_template('app.html', 
                           prediction_text=f"₹ {formatted_price}",
                           input_location=location,
                           input_city=city,
                           input_area=area,
                           input_bhk=bhk,
                           input_resale=resale_text,
                           luxury_score=luxury_score,
                           importance=importance_data, # NEW DATA
                           cities=list(locations_by_city.keys()),
                           locations=locations_by_city.get(city, [])
                           )

if __name__ == "__main__":
    app.run(debug=True)