# weather.py

import requests

# Replace with your WeatherAPI key
API_KEY = "your_api_key_here"
BASE_URL = "http://api.weatherapi.com/v1/current.json"

# Input city name
city = input("Enter the city name: ")

# Construct the API request URL
url = f"{BASE_URL}?key={API_KEY}&q={city}"

try:
    # Make the API request
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    
    # Parse the JSON response
    weather_data = response.json()
    
    # Extract and print relevant weather information
    location = weather_data['location']['name']
    temperature = weather_data['current']['temp_c']
    condition = weather_data['current']['condition']['text']
    
    print(f"Weather in {location}:")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {condition}")
    
except requests.exceptions.RequestException as e:
    print(f"Error fetching weather data: {e}")
except KeyError:
    print("Invalid response from the weather API. Please check the city name or API key.")