from flask import Flask, render_template, request, jsonify
from geopy.geocoders import Nominatim

app = Flask(__name__)

def get_lat_long(city, state):
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.geocode(f"{city}, {state}")
    
    if location:
        return {'latitude': location.latitude, 'longitude': location.longitude}
    else:
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_addresses', methods=['POST'])
def process_addresses():
    city = request.form.get('city')
    state = request.form.get('state')
    
    if city and state:
        coordinates = get_lat_long(city, state)
        if coordinates:
            return jsonify(coordinates)
        else:
            return jsonify({'error': 'Coordinates not found for the specified location.'}), 404
    else:
        return jsonify({'error': 'City and state parameters are required.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
