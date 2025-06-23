import requests

# Ask user for a city
city = input("Enter city name: ")

# Use WeatherAPI's free demo endpoint
url = f"http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY={city}"

# Make the GET request
response = requests.get(url)
data = response.json()

# Check and print weather info
if "current" in data:
    print(f"\n📍 Weather in {city.title()}:")
    print(f"🌡️ Temperature: {data['current']['temp_c']}°C")
    print(f"💨 Wind: {data['current']['wind_kph']} kph")
    print(f"⛅ Condition: {data['current']['condition']['text']}")
else:
    print("\n⚠️ Could not find weather info. Try another city.")
