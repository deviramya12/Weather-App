import requests
import json

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"  # You can change this to "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]

            print(f"Weather in {location}:")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Conditions: {description}")
        else:
            print(f"Error: {data['message']}")

    except Exception as e:
        print(f"Error fetching weather data: {e}")

def main():
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = "2f01790ecfdaa0965b89e60da983b3bb"

    if api_key == "2f01790ecfdaa0965b89e60da983b3bb":
        print("Please replace '2f01790ecfdaa0965b89e60da983b3bb' with your actual OpenWeatherMap API key.")
        #return

    location = input("Enter city name or ZIP code: ")
    get_weather(api_key, location)

if __name__ == "__main__":
    main()
