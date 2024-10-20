from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = '5f87ea1d53dab19f65a760332859773a'  # Your OpenWeatherMap API Key

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def generate_skincare_advice(temp, humidity, condition):
    advice = ""
    if temp < 15:
        advice += "It's cold! Keep your skin moisturized.\n"
    elif temp > 30:
        advice += "It's hot! Use lightweight, oil-free sunscreen.\n"
    
    if humidity < 30:
        advice += "Dry air, use hydrating products."
    elif humidity > 70:
        advice += "High humidity, use lightweight skincare."

    if condition == "Rain":
        advice += "Rainy weather, use waterproof sunscreen."
    elif condition == "Clear":
        advice += "Clear skies, apply sunscreen."

    return advice

@app.route('/')
def home():
    return render_template('weather-skin.html')

@app.route('/get_skincare_advice', methods=['POST'])
def get_skincare_advice():
    data = request.get_json()
    city = data.get('city')
    
    if city:
        weather_data = get_weather_data(city)
        if weather_data.get('cod') != 200:
            return jsonify({'error': 'City not found'}), 404
        
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        condition = weather_data['weather'][0]['main']
        
        advice = generate_skincare_advice(temp, humidity, condition)
        return jsonify({
            'weather': weather_data,
            'advice': advice
        })
    
    return jsonify({'error': 'Invalid data'}), 400

if __name__ == '__main__':
    app.run(debug=True)
