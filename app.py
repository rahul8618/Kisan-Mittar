from flask import Flask, request, jsonify
import google.generativeai as genai
import logging

app = Flask(__name__)

# Configure logging to save request and error details
logging.basicConfig(filename='kisanmitra.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Configure Gemini API with your API key
genai.configure(api_key="AIzaSyDftbcdskA0nFkPpM3C-S-IPptEelVGTBk")  # Replace with your Gemini API key
model = genai.GenerativeModel('gemini-1.5-flash')

# Simulated IoT and weather data for demonstration
iot_data = {
    "soil_moisture": 30,  # in percentage
    "temperature": 32,    # in Celsius
    "humidity": 60        # in percentage
}

weather_data = {
    "rainfall": "Rain expected in 3 days",
    "temp_trend": "Rising"
}

# Log all incoming requests
@app.before_request
def log_request():
    logging.info(f"Request: {request.method} {request.path} - {request.remote_addr}")

# Route 1: Weather Advice
@app.route('/weather', methods=['GET'])
def get_weather_advice():
    try:
        prompt = f"Weather data: rainfall = {weather_data['rainfall']}, temperature trend = {weather_data['temp_trend']}. What should the farmer do?"
        response = model.generate_content(prompt)
        advice = response.text
        return jsonify({"advice": advice})
    except Exception as e:
        logging.error(f"Error in weather advice: {str(e)}")
        return jsonify({"error": "Failed to fetch weather advice"}), 500

# Route 2: Soil Advice
@app.route('/soil', methods=['POST'])
def get_soil_advice():
    try:
        farmer_input = request.get_json()
        crop = farmer_input.get("crop", "Tomato")
        prompt = f"Soil data: moisture = {iot_data['soil_moisture']}%, Crop: {crop}. What should be done for soil health?"
        response = model.generate_content(prompt)
        advice = response.text
        return jsonify({"advice": advice})
    except Exception as e:
        logging.error(f"Error in soil advice: {str(e)}")
        return jsonify({"error": "Invalid input or server error"}), 400

# Route 3: Crop Suggestion
@app.route('/crop', methods=['POST'])
def get_crop_advice():
    try:
        farmer_input = request.get_json()
        land_size = farmer_input.get("land_size", "2 acres")
        prompt = f"Weather: {weather_data['rainfall']}, Land size: {land_size}. Which crop should be planted this season?"
        response = model.generate_content(prompt)
        advice = response.text
        return jsonify({"advice": advice})
    except Exception as e:
        logging.error(f"Error in crop advice: {str(e)}")
        return jsonify({"error": "Invalid input or server error"}), 400

# Route 4: Pest Advice
@app.route('/pest', methods=['POST'])
def get_pest_advice():
    try:
        pest_input = request.get_json()
        pest_desc = pest_input.get("pest_desc", "Small insects")
        prompt = f"Crop issue: {pest_desc}. What should be done?"
        response = model.generate_content(prompt)
        advice = response.text
        return jsonify({"advice": advice})
    except Exception as e:
        logging.error(f"Error in pest advice: {str(e)}")
        return jsonify({"error": "Invalid input or server error"}), 400

# Start the server
if __name__ == '__main__':
    logging.info("Starting KisanMitra server...")
    app.run(debug=False, host='0.0.0.0', port=5000)