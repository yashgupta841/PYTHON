# Python program to find current weather details of any city using OpenWeatherMap API
import requests

# Enter your API key here
api_key = "Your_API_Key"

# Base URL variable to store the OpenWeatherMap API endpoint
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Prompt the user for a city name
city_name = input("Enter city name: ")

# Construct the complete API URL
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# Make a GET request to the API
response = requests.get(complete_url)

# Convert the response to JSON
x = response.json()

# Check if the city was found
if x.get("cod") != "404":
    # Extract weather details safely
    y = x.get("main", {})
    current_temperature = y.get("temp", "N/A")
    current_pressure = y.get("pressure", "N/A")
    current_humidity = y.get("humidity", "N/A")

    z = x.get("weather", [])
    weather_description = z[0].get("description", "N/A") if z else "N/A"

    # Display the weather details
    print(f"Temperature (in kelvin unit): {current_temperature}\n"
          f"Atmospheric pressure (in hPa unit): {current_pressure}\n"
          f"Humidity (in percentage): {current_humidity}\n"
          f"Description: {weather_description}")
else:
    print("City Not Found")
