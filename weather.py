import requests
import time

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    return requests.get(url).json()

def display_weather(api_key, city):
    start_time = time.time()
    weather_data = get_weather(api_key, city)
    response_time = time.time() - start_time
    
    if weather_data.get('cod') != 200:
        print(f"Failed to get weather data: {weather_data.get('message', 'Unknown error')}")
        return
    
    main = weather_data['main']
    wind = weather_data['wind']
    weather_description = weather_data['weather'][0]['description']
    
    print(f"Weather in {city}:")
    print(f"Temperature: {main['temp']}°F")
    print(f"Humidity: {main['humidity']}%")
    print(f"Pressure: {main['pressure']} hPa")
    print(f"Wind Speed: {wind['speed']} m/s")
    print(f"Description: {weather_description.capitalize()}")
    print(f"API response time: {response_time:.2f} seconds")

if __name__ == "__main__":
    api_key = "API Key"  # Replace with your actual API key
    city = "CITY"  # Replace with the city you want to get the weather for
    display_weather(api_key, city)
